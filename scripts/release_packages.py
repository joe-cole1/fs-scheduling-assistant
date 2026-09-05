"""GitHub release orchestration. No source edits, branch pushes or asset replacement."""
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
TAG_PATTERN = r'v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z]+(?:[.-][0-9A-Za-z]+)*)?'
REQUIRED_HUMAN_HEADINGS = ('## What changed', '## What you need to do', '## Validation and known limitations')
SUPPORTED_REPRO = {'schema_version': 1, 'package_format': 1, 'python_version': '3.12.14', 'archive_mode': 'stored'}
LEGACY_TAG = 'v0.4.1'
LEGACY_REQUIREMENTS = 'packaging/legacy/v0.4.1-requirements.txt'


def run(*args, input=None):
    return subprocess.run(args, input=input, text=True, check=True, capture_output=True).stdout.strip()


def git_show_bytes(sha, path):
    return subprocess.run(['git', 'show', f'{sha}:{path}'], check=True, capture_output=True).stdout


def api(endpoint, method='GET', payload=None):
    args = ['gh', 'api', endpoint, '--method', method]
    if payload is not None:
        args += ['--input', '-']
    return json.loads(run(*args, input=json.dumps(payload) if payload is not None else None))


def validate_release(release, tag, version):
    if not re.fullmatch(TAG_PATTERN, tag):
        raise ValueError('Use a version tag such as v0.4.2; no paths or shell expressions.')
    if release['tag_name'] != tag or release['draft']:
        raise ValueError('The tag must identify an already published release.')
    if version != tag[1:]:
        raise ValueError(f'Tag {tag} does not match packaging/version.txt ({version}).')
    if release.get('immutable') and not set(FILES).issubset(a['name'] for a in release['assets']):
        raise ValueError('Immutable release cannot receive missing assets after publication. Use a draft-before-publication release process; do not move the tag.')


def validate_reproducibility_contract(contract, requirements_bytes):
    for key,value in SUPPORTED_REPRO.items():
        if contract.get(key) != value:
            raise ValueError(f'Unsupported tagged reproducibility contract: {key}={contract.get(key)!r}; expected {value!r}.')
    expected = hashlib.sha256(requirements_bytes).hexdigest()
    if contract.get('requirements_sha256') != expected:
        raise ValueError('Tagged reproducibility contract does not match tagged packaging/requirements.txt.')
    return contract


def tagged_build_contract(sha, tag):
    """Return immutable tagged build metadata. Only the original v0.4.1 is legacy."""
    if tag == LEGACY_TAG:
        return {'legacy': True, 'requirements_path': LEGACY_REQUIREMENTS,
                'python_version': SUPPORTED_REPRO['python_version']}
    try:
        requirements = git_show_bytes(sha, 'packaging/requirements.txt')
        contract = json.loads(git_show_bytes(sha, 'packaging/reproducibility.json').decode())
    except (subprocess.CalledProcessError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ValueError('Future release tags must contain packaging/requirements.txt and packaging/reproducibility.json.') from exc
    validate_reproducibility_contract(contract, requirements)
    return {'legacy': False, 'requirements_path': 'release-source/packaging/requirements.txt',
            'python_version': contract['python_version'], 'contract': contract}


def prepare():
    tag = os.environ['RELEASE_TAG']
    if not re.fullmatch(TAG_PATTERN, tag):
        raise ValueError('Invalid release tag.')
    repo = os.environ['GITHUB_REPOSITORY']
    release = api(f'repos/{repo}/releases/tags/{tag}')
    sha = run('git', 'rev-parse', f'refs/tags/{tag}^{{commit}}')
    run('git', 'merge-base', '--is-ancestor', sha, 'HEAD')
    version = run('git', 'show', f'{sha}:packaging/version.txt')
    validate_release(release, tag, version)
    build_contract = tagged_build_contract(sha, tag)
    event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())
    if os.environ['GITHUB_EVENT_NAME'] == 'release' and event['release']['id'] != release['id']:
        raise ValueError('Release identity changed since this workflow was triggered.')
    state = {'repo': repo, 'tag': tag, 'id': release['id'], 'source_sha': sha,
             'controller_sha': run('git', 'rev-parse', 'HEAD'), 'version': version,
             'build_contract': build_contract}
    Path(os.environ['RELEASE_STATE']).write_text(json.dumps(state))
    with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
        output.write(f'source_sha={sha}\n')
        output.write(f'requirements_path={build_contract["requirements_path"]}\n')
        output.write(f'python_version={build_contract["python_version"]}\n')
    print(f'Build {tag} from {sha}' + (' using the frozen v0.4.1 legacy contract' if build_contract['legacy'] else ' using its tagged reproducibility contract'))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_build(folder, version):
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


def without_download_block(body):
    body = body or ''
    if START not in body and END not in body:
        return body
    if body.count(START) != 1 or body.count(END) != 1 or body.index(END) < body.index(START):
        raise ValueError('Malformed generated notes block; preserve human text and repair markers manually.')
    first, tail = body.split(START)
    _, last = tail.split(END)
    return first + last


def has_structured_human_summary(body):
    human = without_download_block(body)
    return all(heading in human for heading in REQUIRED_HUMAN_HEADINGS)


def notes(body, state, folder):
    human = without_download_block(body).rstrip()
    structured = has_structured_human_summary(human)
    base = f'https://github.com/{state["repo"]}'
    assets = f'{base}/releases/download/{state["tag"]}'
    labels = ('Pantons setup', 'First-time squadron setup', 'Update existing setup')
    links = '\n'.join(f'- [{label}]({assets}/{name})' for label, name in zip(labels, ZIPS))
    checks = '\n'.join(f'| {name} | `{digest(folder / name)}` |' for name in ZIPS)
    qc = f'{base}/blob/{state["source_sha"]}/docs/v0.4/repository-qc.md'
    validation = (
        f'Automated package structure, content and update-preservation checks passed. '
        f'This does not establish visual review, ChatGPT Mil behavior, operational readiness or approval of local policy. '
        f'See the human **Validation and known limitations** section above and the [tagged QC record]({qc}).'
        if structured else
        f'Automated package structure, content and update-preservation checks passed. '
        f'No structured human release-validation summary was present above when this block was generated; GitHub-generated change notes are not validation evidence. '
        f'This does not establish visual review, ChatGPT Mil behavior, operational readiness or approval of local policy. '
        f'See the [tagged QC record]({qc}) for checks recorded in the released source.'
    )
    legacy = state.get('build_contract', {}).get('legacy', False)
    build_line = f'Built from [{state["tag"]}]({base}/tree/{state["source_sha"]}) (`{state["source_sha"]}`). Packaging controller: `{state["controller_sha"]}`.'
    if legacy:
        build_line += ' This is the documented v0.4.1 legacy build path; later releases use their tagged reproducibility contract.'
    block = f'''{START}
## Downloads

{links}

Download a named setup ZIP, extract it and open START HERE.docx. GitHub's automatic "Source code" ZIP is for maintainers and does not contain the built Word kit.

Existing setups: use the update next week. It replaces System and START HERE; keep Local Guidance and weekly work in place.

## Build verification

{build_line}

{validation}

[File manifest]({assets}/manifest.json) · [SHA-256 checksums]({assets}/SHA256SUMS.txt)

| Download | SHA-256 |
| --- | --- |
{checks}
{END}'''
    return human + ('\n\n' if human else '') + block + '\n'


def asset_plan(release, folder, download):
    """Check all existing names before any upload. Never silently replace bytes."""
    names = [a['name'] for a in release['assets']]
    missing = []
    for name in FILES:
        if names.count(name) > 1:
            raise ValueError(f'Duplicate release asset: {name}')
        if name in names:
            if download(name) != (folder / name).read_bytes():
                raise ValueError(f'Existing release asset differs: {name}. Keep this release intact; use a new version for changed content.')
        else:
            missing.append(name)
    return missing


def publish():
    state = json.loads(Path(os.environ['RELEASE_STATE']).read_text())
    repo, tag = state['repo'], state['tag']
    if run('git', '-C', 'release-source', 'rev-parse', 'HEAD') != state['source_sha']:
        raise ValueError('Source checkout changed during build.')
    remote_tag = api(f'repos/{repo}/git/ref/tags/{tag}')['object']
    while remote_tag['type'] == 'tag':
        remote_tag = api(f'repos/{repo}/git/tags/{remote_tag["sha"]}')['object']
    if remote_tag['sha'] != state['source_sha']:
        raise ValueError('Release tag moved during build.')
    folder = Path(os.environ['PACKAGE_OUTPUT']) / 'downloads'
    verify_build(folder, state['version'])
    release = api(f'repos/{repo}/releases/{state["id"]}')
    validate_release(release, tag, state['version'])
    without_download_block(release.get('body'))
    with tempfile.TemporaryDirectory() as temp:
        def download(name):
            dest = Path(temp) / name.removesuffix('.zip')
            dest.mkdir(exist_ok=True)
            run('gh', 'release', 'download', tag, '--repo', repo, '--pattern', name, '--dir', str(dest), '--clobber')
            return (dest / name).read_bytes()
        missing = asset_plan(release, folder, download)
        if missing:
            run('gh', 'release', 'upload', tag, *(str(folder / n) for n in missing), '--repo', repo)
        refreshed = api(f'repos/{repo}/releases/{state["id"]}')
        if asset_plan(refreshed, folder, download):
            raise ValueError('Release upload is incomplete.')
    refreshed = api(f'repos/{repo}/releases/{state["id"]}')
    body = refreshed.get('body') or ''
    if not without_download_block(body).strip():
        generated = api(f'repos/{repo}/releases/generate-notes', 'POST', {'tag_name': tag})
        body = generated['body']
    api(f'repos/{repo}/releases/{state["id"]}', 'PATCH', {'body': notes(body, state, folder)})
    with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
        summary.write(f'### Downloads verified for {tag}\n\nAll three ZIPs, the manifest and checksums are attached to the release. No repository branch was modified.\n')
    print(f'Verified release downloads: {tag}')


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('prepare', 'publish'):
        raise SystemExit('Usage: release_packages.py prepare|publish')
    try:
        {'prepare': prepare, 'publish': publish}[sys.argv[1]]()
    except (ValueError, KeyError, subprocess.CalledProcessError) as exc:
        if isinstance(exc, subprocess.CalledProcessError):
            print(exc.stderr, file=sys.stderr)
        raise SystemExit(str(exc)) from exc
