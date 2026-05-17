"""Detect circular dependencies in the wiki dependency graph."""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"


def parse_frontmatter(path: Path):
    text = path.read_text()
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        return yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None


def build_graph():
    graph = {}
    for md in WIKI_DIR.rglob("*.md"):
        if md.parent.name == "indexes":
            continue
        fm = parse_frontmatter(md)
        if not fm or "id" not in fm:
            continue
        pid = fm["id"]
        deps = fm.get("depends_on", [])
        if isinstance(deps, list):
            graph[pid] = [d for d in deps if d]
        else:
            graph[pid] = []
    return graph


def find_cycles(graph: dict) -> list:
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}
    cycles = []
    path = []

    def dfs(node):
        color[node] = GRAY
        path.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in color:
                continue
            if color[neighbor] == GRAY:
                cycle_start = path.index(neighbor)
                cycle = path[cycle_start:] + [neighbor]
                cycles.append(cycle)
            elif color[neighbor] == WHITE:
                dfs(neighbor)
        path.pop()
        color[node] = BLACK

    for node in graph:
        if color[node] == WHITE:
            dfs(node)

    return cycles


def main():
    graph = build_graph()
    cycles = find_cycles(graph)

    if cycles:
        print(f"Found {len(cycles)} circular dependency chain(s):")
        for cycle in cycles:
            print(f"  {' -> '.join(cycle)}")
        sys.exit(1)
    else:
        print("No circular dependencies detected.")
        sys.exit(0)


if __name__ == "__main__":
    main()
