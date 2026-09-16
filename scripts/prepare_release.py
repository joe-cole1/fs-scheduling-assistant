"""Prepare a prospective release from the current default-branch commit."""
import json
import os
from pathlib import Path

import release_packages as r


def prepare():
    version = os.environ['RELEASE_VERSION'].strip()
    tag = r.tag_from_version(version)
    repo = os.environ['GITHUB_REPOSITORY']
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
        output.write(f'requirements_path={build_contract["requirements_path"]}\n')
        output.write(f'python_version={build_contract["python_version"]}\n')

    action = 'Resume matching draft' if existing else 'Prepare new draft'
    print(f'{action} {tag} from {source_sha}; nothing is published by this step.')


if __name__ == '__main__':
    try:
        prepare()
    except (ValueError, KeyError) as exc:
        raise SystemExit(str(exc)) from exc
