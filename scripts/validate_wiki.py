"""Validate all wiki pages for structural correctness."""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"

VALID_TYPES = {
    "paper", "definition", "axiom", "assumption", "theorem", "lemma",
    "proof-technique", "example", "counterexample", "proof-gap",
    "contradiction-note", "concept-map",
}

REQUIRED_FIELDS = {"id", "type", "title"}

THEOREM_LEMMA_SECTIONS = {"Statement", "Proof Strategy", "Proof", "Verification"}

REF_FIELDS = ["depends_on", "used_by", "blocks", "disproves", "claims_in_tension"]


def parse_frontmatter(path: Path):
    text = path.read_text()
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None, text
    return fm, parts[2]


def extract_sections(body: str) -> set:
    sections = set()
    for line in body.splitlines():
        if line.startswith("## "):
            sections.add(line[3:].strip())
    return sections


def collect_all_ids() -> set:
    ids = set()
    for md in WIKI_DIR.rglob("*.md"):
        if md.parent.name == "indexes":
            continue
        fm, _ = parse_frontmatter(md)
        if fm and "id" in fm:
            ids.add(fm["id"])
    return ids


def section_has_content(body: str, section_name: str) -> bool:
    lines = body.splitlines()
    in_section = False
    for line in lines:
        if line.startswith("## "):
            if in_section:
                return False
            if line[3:].strip() == section_name:
                in_section = True
        elif in_section and line.strip():
            return True
    return False


def main():
    errors = []
    warnings = []
    all_ids = collect_all_ids()

    for md in sorted(WIKI_DIR.rglob("*.md")):
        if md.parent.name == "indexes":
            continue
        rel = md.relative_to(WIKI_DIR)
        fm, body = parse_frontmatter(md)

        if fm is None:
            errors.append(f"{rel}: missing or invalid YAML frontmatter")
            continue

        for field in REQUIRED_FIELDS:
            if field not in fm:
                errors.append(f"{rel}: missing required field '{field}'")

        if "type" in fm and fm["type"] not in VALID_TYPES:
            errors.append(f"{rel}: invalid type '{fm['type']}'")

        for ref_field in REF_FIELDS:
            if ref_field not in fm:
                continue
            refs = fm[ref_field]
            if isinstance(refs, str) and refs:
                if refs not in all_ids:
                    errors.append(f"{rel}: {ref_field} references unknown ID '{refs}'")
            elif isinstance(refs, list):
                for ref in refs:
                    if ref and ref not in all_ids:
                        errors.append(f"{rel}: {ref_field} references unknown ID '{ref}'")

        page_type = fm.get("type", "")
        if page_type in ("theorem", "lemma"):
            sections = extract_sections(body)
            for req in THEOREM_LEMMA_SECTIONS:
                if req not in sections:
                    errors.append(f"{rel}: missing required section '{req}'")

            status = fm.get("status", "")
            if status == "proved":
                if not section_has_content(body, "Proof"):
                    errors.append(f"{rel}: status is 'proved' but Proof section is empty")
                if not section_has_content(body, "Verification"):
                    errors.append(f"{rel}: status is 'proved' but Verification section is empty")

        formal_status = fm.get("formal_status", "")
        if formal_status == "verified":
            lean_file = fm.get("lean_file", "")
            lean_decl = fm.get("lean_decl", "")
            if not lean_file:
                errors.append(f"{rel}: formal_status is 'verified' but lean_file is empty")
            if not lean_decl:
                errors.append(f"{rel}: formal_status is 'verified' but lean_decl is empty")
            if lean_file:
                lean_path = ROOT / lean_file
                if not lean_path.exists():
                    errors.append(f"{rel}: lean_file '{lean_file}' does not exist on disk")
                else:
                    lean_content = lean_path.read_text()
                    if lean_decl and lean_decl not in lean_content:
                        errors.append(f"{rel}: lean_decl '{lean_decl}' not found in {lean_file}")

        if page_type in ("theorem", "lemma"):
            status = fm.get("status", "")
            if status == "proved" and not formal_status:
                warnings.append(f"{rel}: status is 'proved' but formal_status is not set")

        if formal_status == "failed":
            warnings.append(f"{rel}: formal_status is 'failed'")

        if page_type in ("theorem", "lemma"):
            deps = fm.get("depends_on", [])
            if isinstance(deps, list):
                for dep_id in deps:
                    if not dep_id:
                        continue
                    dep_fm = find_page_by_id(dep_id)
                    if dep_fm and dep_fm.get("status") == "unproved":
                        warnings.append(f"{rel}: depends on unproved '{dep_id}'")

    print("=== Validation Summary ===")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    if errors:
        print("\n--- ERRORS ---")
        for e in errors:
            print(f"  ERROR: {e}")
    if warnings:
        print("\n--- WARNINGS ---")
        for w in warnings:
            print(f"  WARN: {w}")
    if not errors and not warnings:
        print("All pages valid.")

    sys.exit(1 if errors else 0)


def find_page_by_id(page_id: str):
    for md in WIKI_DIR.rglob("*.md"):
        if md.parent.name == "indexes":
            continue
        fm, _ = parse_frontmatter(md)
        if fm and fm.get("id") == page_id:
            return fm
    return None


if __name__ == "__main__":
    main()
