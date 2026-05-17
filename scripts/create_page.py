"""Create a new wiki page from a template."""
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = ROOT / "templates"
WIKI_DIR = ROOT / "wiki"

TYPE_TO_DIR = {
    "paper": "papers",
    "definition": "definitions",
    "axiom": "axioms",
    "assumption": "assumptions",
    "theorem": "theorems",
    "lemma": "lemmas",
    "proof-technique": "proof-techniques",
    "example": "examples",
    "counterexample": "counterexamples",
    "proof-gap": "gaps",
    "contradiction-note": "contradictions",
    "concept-map": "concept-maps",
}

TYPE_TO_TEMPLATE = {
    "paper": "paper.md",
    "definition": "definition.md",
    "axiom": "axiom.md",
    "assumption": "assumption.md",
    "theorem": "theorem.md",
    "lemma": "lemma.md",
    "proof-technique": "proof_technique.md",
    "example": "example.md",
    "counterexample": "counterexample.md",
    "proof-gap": "proof_gap.md",
    "contradiction-note": "contradiction_note.md",
    "concept-map": "concept_map.md",
}


def slugify(title: str) -> str:
    slug = title.lower().strip()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def main():
    if len(sys.argv) < 3:
        print("Usage: python scripts/create_page.py <type> \"<title>\"")
        print(f"Valid types: {', '.join(sorted(TYPE_TO_DIR.keys()))}")
        sys.exit(1)

    page_type = sys.argv[1]
    title = sys.argv[2]

    if page_type not in TYPE_TO_DIR:
        print(f"Error: invalid type '{page_type}'")
        print(f"Valid types: {', '.join(sorted(TYPE_TO_DIR.keys()))}")
        sys.exit(1)

    slug = slugify(title)
    page_id = f"{page_type}-{slug}"
    today = date.today().isoformat()

    template_path = TEMPLATES_DIR / TYPE_TO_TEMPLATE[page_type]
    if not template_path.exists():
        print(f"Error: template not found at {template_path}")
        sys.exit(1)

    template = template_path.read_text()
    content = template.replace("{{id}}", page_id)
    content = content.replace("{{title}}", title)
    content = content.replace("{{created_at}}", today)
    content = content.replace("{{updated_at}}", today)

    output_dir = WIKI_DIR / TYPE_TO_DIR[page_type]
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{slug}.md"

    if output_path.exists():
        print(f"Error: file already exists at {output_path}")
        sys.exit(1)

    output_path.write_text(content)
    print(output_path)


if __name__ == "__main__":
    main()
