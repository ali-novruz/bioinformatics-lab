"""Small offline integrity checks for metadata and explicit research dependencies."""
import hashlib
import json
from pathlib import Path
import re
from .registry import load_registry,repository_file


def check_health(root):
    root=Path(root)
    load_registry(root)
    manifest=json.loads((root/'datasets/examples/manifest.json').read_text(encoding='utf-8'))
    seen=set()
    for item in manifest['files']:
        if not {'path','sha256','bytes','source_url','source_sha256','transformation'}<=item.keys():
            raise ValueError('Example dataset lacks source/transform metadata')
        if item['path'] in seen:
            raise ValueError(f'Duplicate dataset path: {item["path"]}')
        seen.add(item['path'])
        path=repository_file(root,item['path'])
        if not item['source_url'].startswith('https://') or not item['transformation'].strip():
            raise ValueError('Dataset source URL and transformation required')
        for field in ['sha256','source_sha256']:
            if not re.fullmatch('[0-9a-f]{64}',item[field]):
                raise ValueError(f'Invalid dataset {field}')
        if path.stat().st_size!=item['bytes'] or hashlib.sha256(path.read_bytes()).hexdigest()!=item['sha256']:
            raise ValueError(f'Dataset differs from manifest: {item["path"]}')
    graph_path=root/'research/graph.json'
    if not graph_path.exists():
        raise ValueError('Missing research/graph.json')
    graph=json.loads(graph_path.read_text(encoding='utf-8'))
    nodes={}
    for node in graph['nodes']:
        if node['id'] in nodes:
            raise ValueError(f'Duplicate research node: {node["id"]}')
        if node['status'] not in ['executed','protocol','source']:
            raise ValueError(f'Unknown research status: {node["id"]}')
        repository_file(root,node['path'])
        nodes[node['id']]=node
    dependencies={name:[] for name in nodes}
    for edge in graph['edges']:
        if edge['from'] not in nodes or edge['to'] not in nodes or not edge.get('relation'):
            raise ValueError('Research relation has missing endpoints or description')
        dependencies[edge['to']].append(edge['from'])
    visited=set();active=set()
    def visit(name):
        if name in active:raise ValueError('Cycle in research dependency graph')
        if name in visited:return
        active.add(name)
        for parent in dependencies[name]:visit(parent)
        active.remove(name);visited.add(name)
    for name in nodes:visit(name)
    return {'projects':len(load_registry(root)),'example_inputs':len(seen),'research_nodes':len(nodes),'research_edges':len(graph['edges'])}
