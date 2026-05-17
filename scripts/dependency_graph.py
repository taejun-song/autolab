"""Generate dependency graph in Mermaid and JSON formats."""
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
INDEX_DIR = WIKI_DIR / "indexes"


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


def collect_graph():
    nodes = []
    edges = []
    for md in sorted(WIKI_DIR.rglob("*.md")):
        if md.parent.name == "indexes":
            continue
        fm = parse_frontmatter(md)
        if not fm or "id" not in fm:
            continue
        pid = fm["id"]
        title = fm.get("title", pid)
        ptype = fm.get("type", "unknown")
        nodes.append({"id": pid, "title": title, "type": ptype})
        deps = fm.get("depends_on", [])
        if isinstance(deps, list):
            for dep in deps:
                if dep:
                    edges.append({"from": pid, "to": dep})
    return nodes, edges


def sanitize_mermaid_id(s: str) -> str:
    return s.replace("-", "_").replace(" ", "_")


def main():
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    nodes, edges = collect_graph()

    mermaid_lines = ["graph TD"]
    for node in nodes:
        sid = sanitize_mermaid_id(node["id"])
        label = node["title"].replace('"', "'")
        mermaid_lines.append(f'    {sid}["{label}"]')
    for edge in edges:
        src = sanitize_mermaid_id(edge["from"])
        dst = sanitize_mermaid_id(edge["to"])
        mermaid_lines.append(f"    {src} --> {dst}")
    mermaid_content = "\n".join(mermaid_lines) + "\n"

    md_content = f"# Dependency Graph\n\n```mermaid\n{mermaid_content}```\n"
    (INDEX_DIR / "dependency-graph.md").write_text(md_content)
    (INDEX_DIR / "dependency-graph.mmd").write_text(mermaid_content)

    graph_json = {"nodes": nodes, "edges": edges}
    (INDEX_DIR / "dependency-graph.json").write_text(json.dumps(graph_json, indent=2) + "\n")

    print(f"Dependency graph generated: {len(nodes)} nodes, {len(edges)} edges")


if __name__ == "__main__":
    main()
