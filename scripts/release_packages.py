"""Build-time GitHub release orchestration for draft-first immutable releases."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ZIPS = ('Pantons_Setup.zip', 'First_Time_Squadron_Setup.zip', 'Update_Existing_Setup.zip')
FILES = (*ZIPS, 'manifest.json', 'SHA256SUMS.txt')
START = '<!-- scheduling-downloads:start -->'
END = '<!-- scheduling-downloads:end -->'
VERSION_PATTERN = r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z]+(?:[.-][0-9A-Za-z]+)*)?'
TAG_PATTERN = 'v' + VERSION_PATTERN
REQUIRED_SUMMARY_HEADINGS = ('## What changed', '## What you need to do', '## Validation and known limitations')
SUPPORTED_REPRO = {'schema_version': 1, 'package_format': 1, 'python_version': '3.12.14', 'archive_mode': 'stored'}
LEGACY_TAG = 'v0.4.1'
LEGACY_REQUIREMENTS = 'packaging/legacy/v0.4.1-requirements.txt'


def run(*args, input=None):
    return subprocess.run(args, input=input, text=True, check=True, capture_output=True).stdout.strip()


def run_bytes(*args):
    return subprocess.run(args, check=True, capture_output=True).stdout


def git_show_bytes(sha, path):
    return subprocess.run(['git', 'show', f'{sha}:{path}'], check=True, capture_output=True).stdout


def api(endpoint, method='GET', payload=None):
    args = ['gh', 'api', endpoint, '--method', method]
    if payload is not None:
        args += ['--input', '-']
    return json.loads(run(*args, input=json.dumps(payload) if payload is not None else None))


def tag_from_version(version):
    if not re.fullmatch(VERSION_PATTERN, version):
        raise ValueError('Use a version such as 0.5.3 with no leading v, path or shell expression.')
    return 'v' + version


def release_for_tag(repo, tag):
    matches = [r for r in api(f'repos/{repo}/releases?per_page=100') if r.get('tag_name') == tag]
    if len(matches) > 1:
        raise ValueError(f'Multiple releases unexpectedly use tag {tag}.')
    return matches[0] if matches else None


def remote_tag_commit(repo, tag):
    result = subprocess.run(
        ['gh', 'api', f'repos/{repo}/git/ref/tags/{tag}'],
        text=True,
        capture_output=True,
    )
    if result.returncode:
        if '404' in result.stderr or 'Not Found' in result.stderr:
            return None
        raise subprocess.CalledProcessError(result.returncode, result.args, result.stdout, result.stderr)
    obj = json.loads(result.stdout)['object']
    while obj['type'] == 'tag':
        obj = api(f'repos/{repo}/git/tags/{obj["sha"]}')['object']
    return obj['sha']


def validate_release_slot(repo, tag, source_sha):
    if not re.fullmatch(TAG_PATTERN, tag):
        raise ValueError('Invalid release tag.')
    release = release_for_tag(repo, tag)
    tag_sha = remote_tag_commit(repo, tag)
    if release:
        if not release.get('draft'):
            raise ValueError(
                f'{tag} is already published. Immutable releases are never repaired or replaced; use a new version.'
            )
        if release.get('immutable'):
            raise ValueError(f'Draft {tag} is unexpectedly immutable; stop and inspect it manually.')
        if release.get('target_commitish') != source_sha:
            raise ValueError(
                f'Existing draft {tag} targets {release.get("target_commitish")}, not {source_sha}.'
            )
        if tag_sha and tag_sha != source_sha:
            raise ValueError(f'Existing tag {tag} points to {tag_sha}, not {source_sha}.')
        return release
    if tag_sha:
        raise ValueError(
            f'Tag {tag} already exists without a matching draft release. Use a new version; do not move the tag.'
        )
    return None


def validate_reproducibility_contract(contract, requirements_bytes):
    for key, value in SUPPORTED_REPRO.items():
        if contract.get(key) != value:
            raise ValueError(
                f'Unsupported source reproducibility contract: {key}={contract.get(key)!r}; expected {value!r}.'
            )
    expected = hashlib.sha256(requirements_bytes).hexdigest()
    if contract.get('requirements_sha256') != expected:
        raise ValueError('Source reproducibility contract does not match packaging/requirements.txt.')
    return contract


def tagged_build_contract(sha, tag):
    """Return build metadata for the commit that will become the release tag."""
    if tag == LEGACY_TAG:
        return {
            'legacy': True,
            'requirements_path': LEGACY_REQUIREMENTS,
            'python_version': SUPPORTED_REPRO['python_version'],
        }
    try:
        requirements = git_show_bytes(sha, 'packaging/requirements.txt')
        contract = json.loads(git_show_bytes(sha, 'packaging/reproducibility.json').decode())
    except (subprocess.CalledProcessError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ValueError(
            'Release source must contain packaging/requirements.txt and packaging/reproducibility.json.'
        ) from exc
    validate_reproducibility_contract(contract, requirements)
    return {
        'legacy': False,
        'requirements_path': 'release-source/packaging/requirements.txt',
        'python_version': contract['python_version'],
        'contract': contract,
    }


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_build(folder, version):
    allowed = {*ZIPS, 'manifest.json', 'SHA256SUMS.txt'}
    if {p.name for p in folder.iterdir()} - {'SHA256SUMS.txt'} != {*ZIPS, 'manifest.json'}:
        raise ValueError('Unexpected or missing release files.')
    manifest = json.loads((folder / 'manifest.json').read_text())
    if manifest['package_version'] != version or set(manifest['packages']) != set(ZIPS):
        raise ValueError('Build manifest does not match this release.')
    for name in ZIPS:
        if digest(folder / name) != manifest['packages'][name]['sha256']:
            raise ValueError(f'Build checksum mismatch: {name}')
    sums = ''.join(f'{digest(folder / name)}  {name}\n' for name in (*ZIPS, 'manifest.json'))
    (folder / 'SHA256SUMS.txt').write_text(sums)
    if {p.name for p in folder.iterdir()} != allowed:
        raise ValueError('Final release inventory is incomplete.')


def without_download_block(body):
    body = body or ''
    if START not in body and END not in body:
        return body
    if body.count(START) != 1 or body.count(END) != 1 or body.index(END) < body.index(START):
        raise ValueError('Malformed generated notes block; repair the draft before publishing.')
    first, tail = body.split(START)
    _, last = tail.split(END)
    return first + last


def has_structured_summary(body):
    base = without_download_block(body)
    return all(heading in base for heading in REQUIRED_SUMMARY_HEADINGS)


def current_version_migrations(state):
    manifest = json.loads(git_show_bytes(state['source_sha'], 'packaging/persistent-artifacts.json').decode())
    return [
        item for item in manifest.get('migrations', [])
        if item.get('introduced_in') == state['version'] and item.get('action') != 'none'
    ]


def release_summary(state):
    update_note = git_show_bytes(state['source_sha'], 'packaging/update-note.md').decode().strip()
    migrations = current_version_migrations(state)
    if migrations:
        migration_action = (
            'This version includes a declared persistent migration. Existing setups must read '
            '**PERSISTENT MIGRATIONS.docx** and merge only the human-approved changes; do not overwrite Local Guidance.'
        )
    else:
        migration_action = 'No new persistent installed-state migration is declared for this version.'
    run_link = state.get('workflow_run_url')
    validation_link = f' [Workflow run]({run_link}).' if run_link else ''
    return f'''## What changed

{update_note}

## What you need to do

Existing setups: use **Update_Existing_Setup.zip** at the normal next-week boundary if adopting this release. Replace System and START HERE; preserve Local Guidance and weekly work. {migration_action}

First installation: choose **Pantons_Setup.zip** or **First_Time_Squadron_Setup.zip**, extract it, and open START HERE.docx.

## Validation and known limitations

**Passed in this release workflow:** persistent-state declaration validation, two independent package builds, package integrity and Markdown-to-Word source coverage, byte-for-byte reproducibility, and release/package regression tests.{validation_link}

**Not established by those checks:** native Word visual review, GenAI.mil instruction-following, or operational readiness. Those remain separate human/model validation when applicable.

## Changes and contributors
'''


def generated_changes(state):
    payload = {'tag_name': state['tag'], 'target_commitish': state['source_sha']}
    generated = api(f'repos/{state["repo"]}/releases/generate-notes', 'POST', payload)
    return (generated.get('body') or '').strip()


def notes(body, state, folder):
    human = without_download_block(body).rstrip()
    if not has_structured_summary(human):
        raise ValueError('Release notes are missing the required structured summary headings.')
    base = f'https://github.com/{state["repo"]}'
    assets = f'{base}/releases/download/{state["tag"]}'
    labels = ('Pantons setup', 'First-time squadron setup', 'Update existing setup')
    links = '\n'.join(f'- [{label}]({assets}/{name})' for label, name in zip(labels, ZIPS))
    checks = '\n'.join(f'| {name} | `{digest(folder / name)}` |' for name in ZIPS)
    block = f'''{START}
## Downloads

{links}

Download a named setup ZIP, extract it, and open START HERE.docx. GitHub's automatic "Source code" ZIP is for maintainers and does not contain the built Word kit.

Existing setups use the update at the next-week boundary. It replaces System and START HERE while preserving Local Guidance and weekly work.

## Build verification

Built from `{state["source_sha"]}` as **{state["tag"]}**. The draft was populated and verified before publication.

[File manifest]({assets}/manifest.json) · [SHA-256 checksums]({assets}/SHA256SUMS.txt)

| Download | SHA-256 |
| --- | --- |
{checks}
{END}'''
    return human + '\n\n' + block + '\n'


def validate_draft(release, state):
    if release.get('tag_name') != state['tag'] or not release.get('draft'):
        raise ValueError('Expected a matching draft release.')
    if release.get('target_commitish') != state['source_sha']:
        raise ValueError('Draft release source changed.')
    if release.get('immutable'):
        raise ValueError('Draft became immutable before publication.')
    return release


def ensure_draft(state, body):
    existing = validate_release_slot(state['repo'], state['tag'], state['source_sha'])
    if existing:
        release = existing
    else:
        release = api(
            f'repos/{state["repo"]}/releases',
            'POST',
            {
                'tag_name': state['tag'],
                'target_commitish': state['source_sha'],
                'name': state['tag'],
                'body': body,
                'draft': True,
                'prerelease': '-' in state['version'],
            },
        )
    validate_draft(release, state)
    api(f'repos/{state["repo"]}/releases/{release["id"]}', 'PATCH', {'body': body})
    return api(f'repos/{state["repo"]}/releases/{release["id"]}')


def asset_plan(release, folder, download_asset):
    by_name = {}
    for asset in release.get('assets', []):
        by_name.setdefault(asset['name'], []).append(asset)
    missing = []
    for name in FILES:
        matches = by_name.get(name, [])
        if len(matches) > 1:
            raise ValueError(f'Duplicate draft release asset: {name}')
        if matches:
            if download_asset(matches[0]) != (folder / name).read_bytes():
                raise ValueError(
                    f'Existing draft asset differs: {name}. Do not overwrite it; inspect the draft or use a new version.'
                )
        else:
            missing.append(name)
    extras = sorted(set(by_name) - set(FILES))
    if extras:
        raise ValueError(f'Unexpected draft release assets: {extras}')
    return missing


def validate_published(release, state):
    if release.get('tag_name') != state['tag'] or release.get('draft'):
        raise ValueError('Release did not publish as expected.')
    if set(a['name'] for a in release.get('assets', [])) != set(FILES):
        raise ValueError('Published release asset inventory is incomplete.')
    return release


def publish():
    state = json.loads(Path(os.environ['RELEASE_STATE']).read_text())
    repo, tag = state['repo'], state['tag']
    if run('git', '-C', 'release-source', 'rev-parse', 'HEAD') != state['source_sha']:
        raise ValueError('Source checkout changed during build.')

    folder = Path(os.environ['PACKAGE_OUTPUT']) / 'downloads'
    verify_build(folder, state['version'])
    human = release_summary(state)
    changes = generated_changes(state)
    body = notes(human + ('\n\n' + changes if changes else ''), state, folder)
    release = ensure_draft(state, body)

    with tempfile.TemporaryDirectory() as temp:
        def download_asset(asset):
            return run_bytes(
                'gh', 'api', f'repos/{repo}/releases/assets/{asset["id"]}',
                '-H', 'Accept: application/octet-stream'
            )

        missing = asset_plan(release, folder, download_asset)
        if missing:
            run(
                'gh', 'release', 'upload', tag,
                *(str(folder / name) for name in missing),
                '--repo', repo,
            )
        refreshed = api(f'repos/{repo}/releases/{release["id"]}')
        validate_draft(refreshed, state)
        if asset_plan(refreshed, folder, download_asset):
            raise ValueError('Draft release upload is incomplete.')

    tag_sha = remote_tag_commit(repo, tag)
    if tag_sha and tag_sha != state['source_sha']:
        raise ValueError('Release tag does not point to the validated source commit.')

    api(f'repos/{repo}/releases/{release["id"]}', 'PATCH', {'body': body})
    final_draft = api(f'repos/{repo}/releases/{release["id"]}')
    validate_draft(final_draft, state)
    if set(a['name'] for a in final_draft.get('assets', [])) != set(FILES):
        raise ValueError('Refusing to publish a draft with missing or extra assets.')

    published = api(
        f'repos/{repo}/releases/{release["id"]}',
        'PATCH',
        {'draft': False, 'make_latest': 'true'},
    )
    validate_published(published, state)
    published_tag_sha = remote_tag_commit(repo, tag)
    if published_tag_sha != state['source_sha']:
        raise ValueError('Published tag does not point to the validated source commit.')

    immutable = 'immutable' if published.get('immutable') else 'published'
    with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
        summary.write(
            f'### Published {tag}\n\n'
            f'All release assets and notes were verified while the release was a draft, then the draft was published. '
            f'GitHub reports the resulting release as **{immutable}**. No branch was modified.\n'
        )
    print(f'Published verified release: {tag}')


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] != 'publish':
        raise SystemExit('Usage: release_packages.py publish')
    try:
        publish()
    except (ValueError, KeyError, subprocess.CalledProcessError) as exc:
        if isinstance(exc, subprocess.CalledProcessError) and exc.stderr:
            print(exc.stderr, file=sys.stderr)
        raise SystemExit(str(exc)) from exc
