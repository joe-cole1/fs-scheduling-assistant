"""Prepare a prospective stable release from the current default-branch commit."""
import json
import os
from pathlib import Path
import re

import release_packages as r

STABLE_TAG_PATTERN = re.compile(r'^v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$')


def next_patch_version(repo):
    """Increment the patch component of GitHub's latest published stable release."""
    release = r.api(f'repos/{repo}/releases/latest')
    if release.get('draft') or release.get('prerelease'):
        raise ValueError('GitHub latest release is not a published stable release; enter the version explicitly.')
    tag = release.get('tag_name', '')
    match = STABLE_TAG_PATTERN.fullmatch(tag)
    if not match:
        raise ValueError(
            f'Latest published release tag {tag!r} is not stable semantic version vMAJOR.MINOR.PATCH; '
            'enter the version explicitly.'
        )
    major, minor, patch = (int(value) for value in match.groups())
    return f'{major}.{minor}.{patch + 1}', tag


def prepare():
    requested_version = os.environ.get('RELEASE_VERSION', '').strip()
    repo = os.environ['GITHUB_REPOSITORY']
    if requested_version:
        version = requested_version
        previous_tag = None
        version_source = 'manual'
    else:
        version, previous_tag = next_patch_version(repo)
        version_source = 'automatic-patch'

    tag = r.tag_from_version(version)
    if '-' in version:
        raise ValueError(
            'Publish release currently supports stable versions only. Use a version such as 0.5.4, not a prerelease suffix.'
        )

    default_branch = os.environ['DEFAULT_BRANCH']
    selected_ref = os.environ.get('WORKFLOW_REF_NAME', default_branch)
    if selected_ref != default_branch:
        raise ValueError(
            f'Run Publish release from the default branch ({default_branch}), not {selected_ref}.'
        )

    source_sha = r.run('git', 'rev-parse', 'HEAD')
    remote_default = r.run('git', 'rev-parse', f'origin/{default_branch}')
    if source_sha != remote_default:
        raise ValueError('Checked-out release tooling is not the current default-branch commit.')

    existing = r.validate_release_slot(repo, tag, source_sha)
    build_contract = r.tagged_build_contract(source_sha, tag)
    state = {
        'repo': repo,
        'tag': tag,
        'version': version,
        'version_source': version_source,
        'previous_release_tag': previous_tag,
        'source_sha': source_sha,
        'controller_sha': source_sha,
        'default_branch': default_branch,
        'existing_draft_id': existing['id'] if existing else None,
        'build_contract': build_contract,
        'workflow_run_url': (
            f"{os.environ.get('GITHUB_SERVER_URL', 'https://github.com')}/{repo}/actions/runs/"
            f"{os.environ.get('GITHUB_RUN_ID', '')}"
        ).rstrip('/'),
    }
    Path(os.environ['RELEASE_STATE']).write_text(json.dumps(state))
    with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
        output.write(f'source_sha={source_sha}\n')
        output.write(f'package_version={version}\n')
        output.write(f'tag={tag}\n')
        output.write(f'version_source={version_source}\n')
        output.write(f'requirements_path={build_contract["requirements_path"]}\n')
        output.write(f'python_version={build_contract["python_version"]}\n')

    if version_source == 'automatic-patch':
        print(f'Blank version input: increment {previous_tag} to {tag}.')
    action = 'Resume matching draft' if existing else 'Prepare new draft'
    print(f'{action} {tag} from {source_sha}; nothing is published by this step.')


if __name__ == '__main__':
    try:
        prepare()
    except (ValueError, KeyError) as exc:
        raise SystemExit(str(exc)) from exc
