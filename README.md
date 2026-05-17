# AutoProof

A Markdown-based mathematical LLM Wiki with a Lean 4 formal verification engine.

AutoProof maintains two synchronized tracks for mathematical knowledge:

1. **Natural-language wiki** — understanding, ontology, proof skeletons, dependencies
2. **Lean 4 formalization** — formal definitions, theorem statements, machine-checked proofs

A result is maximally reliable when both tracks agree: the wiki proof is rigorous and the Lean formalization compiles.

## Why Ontology?

Mathematical proof is an ontological connection between an accepted axiomatic space (definitions, axioms, previously proved theorems) and a target statement. AutoProof makes this connection structure explicit through dependency metadata, concept maps, and proof skeletons.

## Directory Structure

```
autoproof/
  CLAUDE.md              # Agent instructions
  README.md              # This file
  requirements.txt       # Python dependencies
  lean-toolchain         # Lean version
  lakefile.lean          # Lake project config
  AutoProof.lean         # Root Lean import file

  AutoProof/             # Lean 4 formalization
    Basic.lean
    Definitions/
    Axioms/
    Lemmas/
    Theorems/
    Examples/
    ProofTechniques/

  wiki/                  # Natural-language wiki
    papers/
    definitions/
    axioms/
    assumptions/
    theorems/
    lemmas/
    proof-techniques/
    examples/
    counterexamples/
    gaps/
    contradictions/
    concept-maps/
    indexes/

  templates/             # Page templates
  scripts/               # Automation scripts
  tests/                 # Test suite
```

## Page Types

| Type | Directory | Description |
|---|---|---|
| paper | wiki/papers/ | Raw paper ingestion and analysis |
| definition | wiki/definitions/ | Mathematical definitions |
| axiom | wiki/axioms/ | Foundational axioms |
| assumption | wiki/assumptions/ | Working assumptions |
| theorem | wiki/theorems/ | Proved or unproved theorems |
| lemma | wiki/lemmas/ | Supporting lemmas |
| proof-technique | wiki/proof-techniques/ | Proof method descriptions |
| example | wiki/examples/ | Illustrative examples |
| counterexample | wiki/counterexamples/ | Refutations |
| proof-gap | wiki/gaps/ | Incomplete proof bridges |
| contradiction-note | wiki/contradictions/ | Conflicting claims |
| concept-map | wiki/concept-maps/ | Structural overviews |

## Metadata

Every wiki page has YAML frontmatter with:

- `id` — stable kebab-case identifier (e.g., `theorem-unique-identity`)
- `type` — page type
- `title` — human-readable title
- `status` — current state (`unproved`, `needs-lemma`, `proved`, `disproved`, etc.)
- `formal_status` — Lean state (`unformalized`, `partial`, `verified`, `failed`)
- `lean_file` — path to corresponding Lean file
- `lean_decl` — Lean declaration name
- `depends_on` — list of page IDs this result depends on
- `used_by` — list of page IDs that use this result

## Status Values

**Theorem/Lemma status:** `unproved` | `needs-lemma` | `proved` | `disproved`

**Formal status:** `unformalized` | `partial` | `verified` | `failed`

A theorem reaches maximum acceptance when `status: proved` AND `formal_status: verified`.

## Raw Paper Ingestion

When a paper is introduced:

1. Create a paper page extracting goals, definitions, theorems, lemmas
2. Build proof skeleton and ontological concept map
3. Create missing wiki pages for extracted concepts
4. Create Lean formalization plan
5. Formalize incrementally (definitions → statements → proofs)
6. Run `lake build` and update formal status

## Commands

```bash
# Create a new wiki page from template
python scripts/create_page.py theorem "My Theorem Title"
python scripts/create_page.py paper "Some Paper Title"

# Validate all wiki pages
python scripts/validate_wiki.py

# Build index pages
python scripts/build_index.py

# Generate dependency graph
python scripts/dependency_graph.py

# Check for circular dependencies
python scripts/check_circular_dependencies.py

# Run Lean verification
python scripts/check_lean.py
lake build
```

## Example Workflow

1. Ingest a paper:
   ```bash
   python scripts/create_page.py paper "Uniqueness Theorems in Group Theory"
   ```

2. Extract and create pages for definitions and theorems found in the paper.

3. Write proofs in wiki pages, filling in all sections.

4. Create corresponding Lean files with formal proofs.

5. Verify:
   ```bash
   lake build
   python scripts/validate_wiki.py
   python scripts/build_index.py
   python scripts/check_circular_dependencies.py
   ```

6. Mark proved results:
   ```yaml
   status: proved
   formal_status: verified
   ```

## Installation

```bash
pip install -r requirements.txt
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh
lake build
```
