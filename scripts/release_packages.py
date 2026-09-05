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


def run(*args, input=None):
    return subprocess.run(args, input=input, text=True, check=True, capture_output=True).stdout.strip()


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


def prepare():
    tag = os.environ['RELEASE_TAG']
    if not re.fullmatch(TAG_PATTERN, tag):
        raise ValueError('Invalid release tag.')
    repo = os.environ['GITHUB_REPOSITORY']
    release = api(f'repos/{repo}/releases/tags/{tag}')
    sha = run('git', 'rev-parse', f'refs/tags/{tag}^{{commit}}')
    # Controller checkout is the default branch. Release source must have been merged.
    run('git', 'merge-base', '--is-ancestor', sha, 'HEAD')
    version = run('git', 'show', f'{sha}:packaging/version.txt')
    validate_release(release, tag, version)
    event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())
    if os.environ['GITHUB_EVENT_NAME'] == 'release' and event['release']['id'] != release['id']:
        raise ValueError('Release identity changed since this workflow was triggered.')
    state = {'repo': repo, 'tag': tag, 'id': release['id'], 'source_sha': sha,
             'controller_sha': run('git', 'rev-parse', 'HEAD'), 'version': version}
    Path(os.environ['RELEASE_STATE']).write_text(json.dumps(state))
    with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
        output.write(f'source_sha={sha}\n')
    print(f'Build {tag} from {sha}')


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


def notes(body, state, folder):
    human = without_download_block(body).rstrip()
    base = f'https://github.com/{state["repo"]}'
    assets = f'{base}/releases/download/{state["tag"]}'
    labels = ('Pantons setup', 'First-time squadron setup', 'Update existing setup')
    links = '\n'.join(f'- [{label}]({assets}/{name})' for label, name in zip(labels, ZIPS))
    checks = '\n'.join(f'| {name} | `{digest(folder / name)}` |' for name in ZIPS)
    block = f'''{START}
## Downloads

{links}

Download a named setup ZIP, extract it and open START HERE.docx. GitHub's automatic "Source code" ZIP is for maintainers and does not contain the built Word kit.

Existing setups: use the update next week. It replaces System and START HERE; keep Local Guidance and weekly work in place.

## Build verification

Built from [{state['tag']}]({base}/tree/{state['source_sha']}) (`{state['source_sha']}`). Packaging controller: `{state['controller_sha']}`.

Automated package structure, content and update-preservation checks passed. This does not establish visual review, ChatGPT Mil behavior, operational readiness or approval of local policy; see the human validation notes above and the tagged QC record.

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
    # Check tag identity again; no publishing against a moved tag.
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
    without_download_block(release.get('body')) # Validate before attaching files.
    with tempfile.TemporaryDirectory() as temp:
        def download(name):
            dest = Path(temp) / name.removesuffix('.zip')
            dest.mkdir(exist_ok=True)
            run('gh', 'release', 'download', tag, '--repo', repo, '--pattern', name, '--dir', str(dest), '--clobber')
            return (dest / name).read_bytes()
        missing = asset_plan(release, folder, download)
        if missing:
            # No --clobber on upload. Partial uploads can be safely resumed.
            run('gh', 'release', 'upload', tag, *(str(folder / n) for n in missing), '--repo', repo)
        refreshed = api(f'repos/{repo}/releases/{state["id"]}')
        if asset_plan(refreshed, folder, download):
            raise ValueError('Release upload is incomplete.')
    # Re-read just before editing to retain the publisher's current written notes.
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
