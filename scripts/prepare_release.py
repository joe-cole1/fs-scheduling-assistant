"""Prepare one published release using the release tag as package-version authority."""
import json
import os
from pathlib import Path
import re

import release_packages as r


def prepare():
    tag = os.environ['RELEASE_TAG']
    if not re.fullmatch(r.TAG_PATTERN, tag):
        raise ValueError('Invalid release tag.')
    repo = os.environ['GITHUB_REPOSITORY']
    release = r.api(f'repos/{repo}/releases/tags/{tag}')
    sha = r.run('git', 'rev-parse', f'refs/tags/{tag}^{{commit}}')

    # The release tag is the human-selected package version. The tagged commit
    # still must be merged into the default branch and remains the immutable
    # source for every package input other than this injected release identity.
    r.run('git', 'merge-base', '--is-ancestor', sha, 'HEAD')
    version = tag[1:]
    r.validate_release(release, tag, version)
    build_contract = r.tagged_build_contract(sha, tag)

    event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())
    if os.environ['GITHUB_EVENT_NAME'] == 'release' and event['release']['id'] != release['id']:
        raise ValueError('Release identity changed since this workflow was triggered.')

    state = {
        'repo': repo,
        'tag': tag,
        'id': release['id'],
        'source_sha': sha,
        'controller_sha': r.run('git', 'rev-parse', 'HEAD'),
        'version': version,
        'build_contract': build_contract,
    }
    Path(os.environ['RELEASE_STATE']).write_text(json.dumps(state))
    with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
        output.write(f'source_sha={sha}\n')
        output.write(f'package_version={version}\n')
        output.write(f'requirements_path={build_contract["requirements_path"]}\n')
        output.write(f'python_version={build_contract["python_version"]}\n')
    print(
        f'Build {tag} as package {version} from {sha}'
        + (' using the frozen v0.4.1 legacy contract' if build_contract['legacy']
           else ' using its tagged reproducibility contract')
    )


if __name__ == '__main__':
    try:
        prepare()
    except (ValueError, KeyError) as exc:
        raise SystemExit(str(exc)) from exc
