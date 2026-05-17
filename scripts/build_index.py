"""Generate index pages for the wiki."""
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


def collect_pages():
    pages = []
    for md in sorted(WIKI_DIR.rglob("*.md")):
        if md.parent.name == "indexes":
            continue
        fm = parse_frontmatter(md)
        if fm:
            pages.append({"path": md, "fm": fm})
    return pages


def rel_path(page_path: Path) -> str:
    from os.path import relpath
    return relpath(page_path, INDEX_DIR)


def entry(page) -> str:
    fm = page["fm"]
    title = fm.get("title", "Untitled")
    pid = fm.get("id", "unknown")
    status = fm.get("status", "n/a")
    formal = fm.get("formal_status", "n/a")
    rp = rel_path(page["path"])
    return f"- **[{title}]({rp})** (ID: {pid}) — Status: {status}, Formal: {formal}"


def write_index(filename: str, title: str, pages: list):
    lines = [f"# {title}", ""]
    if not pages:
        lines.append("_(none)_")
    else:
        for p in pages:
            lines.append(entry(p))
    lines.append("")
    (INDEX_DIR / filename).write_text("\n".join(lines))


def main():
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    pages = collect_pages()

    by_title = sorted(pages, key=lambda p: p["fm"].get("title", "").lower())
    write_index("all-pages.md", "All Pages", by_title)

    type_filters = {
        "papers.md": ("Papers", "paper"),
        "definitions.md": ("Definitions", "definition"),
        "axioms.md": ("Axioms", "axiom"),
        "theorems.md": ("Theorems", "theorem"),
        "lemmas.md": ("Lemmas", "lemma"),
    }
    for filename, (title, ptype) in type_filters.items():
        filtered = [p for p in by_title if p["fm"].get("type") == ptype]
        write_index(filename, title, filtered)

    proved = [
        p for p in by_title
        if p["fm"].get("type") in ("theorem", "lemma") and p["fm"].get("status") == "proved"
    ]
    write_index("proved-results.md", "Proved Results", proved)

    gaps = [p for p in by_title if p["fm"].get("type") == "proof-gap" and p["fm"].get("status") == "open"]
    write_index("open-proof-gaps.md", "Open Proof Gaps", gaps)

    contradictions = [p for p in by_title if p["fm"].get("type") == "contradiction-note"]
    write_index("contradictions.md", "Contradictions", contradictions)

    formal = [p for p in by_title if p["fm"].get("formal_status") and p["fm"]["formal_status"] != "n/a"]
    write_index("formal-verification.md", "Formal Verification Status", formal)

    lines = ["# Dependency Index", ""]
    for p in by_title:
        fm = p["fm"]
        deps = fm.get("depends_on", [])
        if not deps:
            continue
        title = fm.get("title", "Untitled")
        pid = fm.get("id", "unknown")
        rp = rel_path(p["path"])
        lines.append(f"- **[{title}]({rp})** (ID: {pid})")
        for d in deps:
            lines.append(f"  - depends on: {d}")
    if len(lines) == 2:
        lines.append("_(no dependencies recorded)_")
    lines.append("")
    (INDEX_DIR / "dependency-index.md").write_text("\n".join(lines))

    print(f"Index pages generated in {INDEX_DIR}")


if __name__ == "__main__":
    main()
