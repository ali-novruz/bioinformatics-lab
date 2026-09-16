"""Validate the small runnable-project registry before launching commands."""
import json
from pathlib import Path
import re


def repository_file(root, name):
    root = Path(root).resolve()
    if not isinstance(name, str) or not name:
        raise ValueError('Nonempty repository path required')
    path = (root / name).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise ValueError(f'Missing or out-of-repository file: {name}')
    return path


def load_registry(root):
    root = Path(root)
    projects = json.loads((root / 'projects/registry.json').read_text(encoding='utf-8'))['projects']
    if not isinstance(projects, list) or not projects:
        raise ValueError('Nonempty projects list required')
    seen = set()
    for project in projects:
        if not isinstance(project, dict) or not {'id','title','script','args','offline','fetch','docs'} <= project.keys():
            raise ValueError('Incomplete project registry entry')
        identifier = project['id']
        if not isinstance(identifier, str) or not re.fullmatch(r'[a-z][a-z0-9-]*', identifier) or identifier in seen:
            raise ValueError(f'Invalid or duplicate project ID: {identifier}')
        seen.add(identifier)
        if not isinstance(project['title'], str) or not project['title'].strip():
            raise ValueError(f'Missing title: {identifier}')
        for field in ['args','fetch']:
            if not isinstance(project[field], list) or not all(isinstance(s,str) for s in project[field]):
                raise ValueError(f'{identifier}: {field} must be a string list')
        if type(project['offline']) is not bool or type(project.get('research', False)) is not bool:
            raise ValueError(f'{identifier}: offline/research flags must be booleans')
        if set(project['fetch']) - {'phix','giab','pasilla','uniprot','pdb'}:
            raise ValueError(f'{identifier}: unknown download dataset')
        if Path(project['script']).name != project['script'] or not project['script'].endswith('.py'):
            raise ValueError(f'{identifier}: script must be a Python filename')
        repository_file(root, 'scripts/' + project['script'])
        repository_file(root, project['docs'])
    return projects
