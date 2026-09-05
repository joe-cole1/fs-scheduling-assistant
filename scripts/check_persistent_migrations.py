"""Validate persistent installed-state declarations and migration history."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / 'packaging/persistent-artifacts.json'
VERSION_PATH = ROOT / 'packaging/version.txt'
ALLOWED_ACTIONS = {'none', 'review-and-merge'}


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f'blob {len(data)}\0'.encode()
    return hashlib.sha1(header + data).hexdigest()


def load_manifest(path: Path | None = None) -> dict:
    path = MANIFEST_PATH if path is None else path
    return json.loads(path.read_text())


def _artifact_state(spec: dict) -> dict:
    if 'source' in spec:
        return {'source': spec['source'], 'git_blob_sha': spec['git_blob_sha']}
    return {'directories': spec.get('directories', [])}


def validate_current(root: Path | None = None, manifest: dict | None = None) -> dict:
    root = ROOT if root is None else root
    manifest = load_manifest(root / 'packaging/persistent-artifacts.json') if manifest is None else manifest
    if manifest.get('schema_version') != 1:
        raise ValueError('persistent-artifacts.json schema_version must be 1')
    artifacts = manifest.get('artifacts')
    if not isinstance(artifacts, dict) or not artifacts:
        raise ValueError('persistent-artifacts.json must declare persistent artifacts')

    for name, spec in artifacts.items():
        if 'source' in spec:
            source = root / spec['source']
            if not source.is_file():
                raise ValueError(f'Persistent source is missing: {name}: {spec["source"]}')
            actual = git_blob_sha(source)
            if actual != spec.get('git_blob_sha'):
                raise ValueError(
                    f'Persistent source changed without updating packaging/persistent-artifacts.json: '
                    f'{name} expected {spec.get("git_blob_sha")} got {actual}'
                )
            if not spec.get('migration_filename', '').endswith('.docx'):
                raise ValueError(f'Persistent source needs a .docx migration_filename: {name}')
        elif 'directories' in spec:
            directories = spec['directories']
            if not isinstance(directories, list) or not directories or len(set(directories)) != len(directories):
                raise ValueError(f'Persistent directory layout must be a unique nonempty list: {name}')
            for directory in directories:
                p = Path(directory)
                if p.is_absolute() or '..' in p.parts or len(p.parts) != 1:
                    raise ValueError(f'Unsafe persistent directory name: {directory}')
        else:
            raise ValueError(f'Unknown persistent artifact declaration: {name}')

    migrations = manifest.get('migrations')
    if not isinstance(migrations, list) or not migrations:
        raise ValueError('persistent-artifacts.json must retain migration history')
    ids = [item.get('id') for item in migrations]
    if any(not item for item in ids) or len(ids) != len(set(ids)):
        raise ValueError('Persistent migration IDs must be unique and nonempty')
    for item in migrations:
        action = item.get('action')
        if action not in ALLOWED_ACTIONS:
            raise ValueError(f'Unsupported persistent migration action: {action}')
        affected = item.get('artifacts', [])
        if not isinstance(affected, list) or any(name not in artifacts for name in affected):
            raise ValueError(f'Persistent migration references unknown artifact: {item.get("id")}')
        instructions = item.get('instructions', [])
        if not isinstance(instructions, list):
            raise ValueError(f'Persistent migration instructions must be a list: {item.get("id")}')
        if action != 'none' and not instructions:
            raise ValueError(f'Actionable persistent migration needs instructions: {item.get("id")}')
        if not item.get('introduced_in') or not item.get('summary'):
            raise ValueError(f'Persistent migration needs introduced_in and summary: {item.get("id")}')
    return manifest


def _git_show(base: str, path: str) -> str | None:
    result = subprocess.run(
        ['git', 'show', f'{base}:{path}'],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    return result.stdout if result.returncode == 0 else None


def validate_change_declaration(previous: dict, current: dict, base_version: str, current_version: str) -> set[str]:
    previous_migrations = previous.get('migrations', [])
    current_migrations = current.get('migrations', [])
    if current_migrations[:len(previous_migrations)] != previous_migrations:
        raise ValueError('Persistent migration history is append-only; do not rewrite prior records')
    names = set(previous.get('artifacts', {})) | set(current.get('artifacts', {}))
    changed = {
        name for name in names
        if _artifact_state(previous.get('artifacts', {}).get(name, {}))
        != _artifact_state(current.get('artifacts', {}).get(name, {}))
    }
    if not changed:
        return changed
    if current_version == base_version:
        raise ValueError(
            'Persistent installed state changed without a new package version. '
            'Bump packaging/version.txt and append a migration record.'
        )
    new_records = current_migrations[len(previous_migrations):]
    if not new_records:
        raise ValueError('Persistent installed state changed without an appended migration record')
    covered = set().union(*(set(item.get('artifacts', [])) for item in new_records))
    missing = changed - covered
    if missing:
        raise ValueError(f'Persistent migration records do not cover changed artifacts: {sorted(missing)}')
    for item in new_records:
        if item.get('introduced_in') != current_version:
            raise ValueError(
                f'New persistent migration {item.get("id")} must use introduced_in={current_version}'
            )
    return changed


def validate_against_base(base: str, current: dict | None = None) -> None:
    current = validate_current(manifest=current)
    base_text = _git_show(base, 'packaging/persistent-artifacts.json')
    if base_text is None:
        return
    previous = json.loads(base_text)
    base_version = (_git_show(base, 'packaging/version.txt') or '').strip()
    current_version = VERSION_PATH.read_text().strip()
    validate_change_declaration(previous,current,base_version,current_version)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--base', help='Base commit SHA for PR change-declaration enforcement')
    args = parser.parse_args()
    validate_current()
    if args.base:
        validate_against_base(args.base)
    print('PASS: persistent installed-state fingerprints and migration declarations are consistent.')


if __name__ == '__main__':
    main()
