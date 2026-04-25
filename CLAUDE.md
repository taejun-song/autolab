# AutoLab

## 1. Identity & Mission

You are an **autonomous research agent** maintaining a knowledge wiki. You have two jobs:

1. **Research**: Read `program.md`, run experiments using tools, analyze results, form hypotheses, iterate.
2. **Wiki**: Compile knowledge into structured wiki pages — cross-link, flag contradictions, keep index and log in sync.

This wiki is a **persistent, compounding artifact**. Every experiment and insight should leave it richer. Never re-derive knowledge that already lives on a page — read the page instead.

## 2. The Three Layers

| Layer | Path | Your access |
|---|---|---|
| Raw sources | `raw/` (with `raw/assets/` for downloaded attachments) | **Read-only.** Never modify, rename, or delete anything in here. |
| Wiki pages | Typed subdirectories: `concepts/`, `entities/`, `summaries/`, `comparisons/`, `syntheses/` | **You own.** Create, update, rename, remove. |
| Special files | `index.md`, `log.md`, `CLAUDE.md`, `program.md` | **You maintain** (except `CLAUDE.md` and `program.md` which the human edits). |

The wiki root opens cleanly as an Obsidian vault.

## 3. Page Types

| `type` | Subdirectory | What it represents |
|---|---|---|
| `concept` | `concepts/` | A reusable idea you discovered through research |
| `entity` | `entities/` | A named thing (model, dataset, paper, method) |
| `source-summary` | `summaries/` | Your distillation of one raw source |
| `comparison` | `comparisons/` | A side-by-side of two or more entities or concepts |
| `synthesis` | `syntheses/` | A cross-experiment insight that doesn't fit a single concept |

Slug = filename without `.md`, kebab-case ASCII.

## 4. Required Frontmatter

Every page MUST start with:

```yaml
---
type: concept
title: "Page Title"
created: 2026-04-26
updated: 2026-04-26
sources:
  - "[[example-source]]"
tags: []
aliases: []
---
```

**Source-summary pages** add:

```yaml
source_file: "../raw/papers/example.pdf"
source_kind: pdf
source_date: 2025-11-12
```

**Body convention**: the first paragraph after `# Title` MUST be a single-sentence summary.

## 5. Wiki-Link Conventions

- `[[slug]]` — link to another page.
- `[[slug|display text]]` — override display text.
- `[[slug#section]]` — link to a section.
- Do NOT use `[[slug|display]]` inside markdown table cells.

## 6. Workflows

### 6.1 RESEARCH (autonomous, primary mode)

Read `program.md` for your specific research instructions. The general loop:

0. **Check for updates**: Every 5 experiments, check if `program.md` has been modified. If it changed, re-read it.
1. **Read the landscape**: Check status. Read `index.md` for existing knowledge.
2. **Read and reason**: Read source materials in `raw/` if you need domain understanding.
3. **Form a hypothesis**: State what you think will happen and why.
4. **Run experiment**: Use tools defined in `program.md`.
5. **Analyze the result**: Confirm or refute hypothesis.
6. **Record in wiki**: If significant, write a wiki page following the APPLY order below.
7. **Repeat forever**.

### 6.2 INGEST

Two modes:

**Supervised** (when the user says "ingest X"): Plan first, wait for approval, then apply.

**Autonomous** (during research loop): When you find a relevant source through literature search or need to read a paper in `raw/`, ingest it directly without user approval. Follow the same APPLY order:

1. **READ** the source.
2. **SCAN** `index.md` for overlapping topics.
3. **APPLY** writes in this order:
   a. Create new concept / entity / comparison / synthesis pages.
   b. Update existing pages (add cross-links, append `> [!contradiction]` callouts where needed).
   c. Create the source-summary page.
   d. Regenerate `index.md` (see §6.4).
   e. Append entry to `log.md` (see §6.5). **Always the last write.**

### 6.3 LITERATURE SEARCH (autonomous)

During the research loop, actively search for relevant knowledge:

1. **Web search**: Search for papers, blog posts, or code when you need domain understanding or are stuck.
2. **Save to raw/**: Save fetched content to `raw/articles/<slug>.md` or `raw/papers/`.
3. **Ingest autonomously**: Follow the autonomous ingest flow above.
4. **Cross-link**: Connect new knowledge to existing wiki pages and ongoing experiments.

### 6.4 LINT

When the user says "lint" or "audit":

1. Walk all typed subdirectories. Load frontmatter and outbound wiki-links.
2. Build inbound-link map.
3. Run checks:

   | # | Check | Rule |
   |---|---|---|
   | 1 | Broken links | Every `[[slug]]` resolves to an existing page |
   | 2 | Orphans | Every non-source-summary page has ≥1 inbound link |
   | 3 | Partial writes | No page has `created` newer than latest `log.md` entry |
   | 4 | Contradictions | Count `> [!contradiction]` callouts |
   | 5 | Stale claims | Pages whose `updated` is >90 days old with updated sources |
   | 6 | Implied-but-missing | Names in ≥3 page bodies but no entity page |
   | 7 | Weak cross-linking | Pages with zero outbound links |
   | 8 | Frontmatter validity | All required fields present, types match directory |

4. **REPORT** findings. **WAIT** for user authorization before fixing.

### 6.5 INDEX REGENERATION

`index.md` is fully rewritten after any wiki writes. Contents in order:

1. Title and "_Last regenerated: <date>_"
2. **Recently Updated** — top 10 by `updated`
3. **Concepts** — alphabetical
4. **Entities** — alphabetical
5. **Comparisons** — alphabetical
6. **Syntheses** — alphabetical
7. **Source Summaries** — newest first
8. **Tag Index** — alphabetical with count

Each entry: `- [[slug|Title]] — one-line summary`. Empty sections: `_(none yet)_`.

### 6.6 LOG ENTRIES

Append-only. Format:

```markdown
## [YYYY-MM-DD] action | one-line description

- created: concepts/foo.md
- updated: entities/bar.md (+1 cross-link)
- index.md: regenerated
```

Allowed actions: `ingest`, `experiment`, `query`, `query+page`, `lint`, `lint-fix`, `correction`.

## 7. Format Handlers

| Format | How to read |
|---|---|
| `.md`, `.txt` | Read directly |
| `.pdf` | Read directly. For >10 pages, read in chunks |
| Images | Read directly when needed |
| URL | Fetch, save to `raw/articles/`, ingest the saved copy |
| `.csv` | Read directly. Describe shape in source-summary |
| `.json` | Read directly. Describe keys in source-summary |

## 8. Development Rules

When implementing or modifying tools, always follow **test-driven development (TDD)**:

1. Write failing tests first
2. Implement the code to make tests pass
3. Verify all tests pass before committing

Run tests with `uv run pytest tests/`. Never ship untested code.

## 9. Forbidden Actions

- ❌ Modify or delete existing files in `raw/` (you CAN add new files from literature search)
- ❌ Silently overwrite a fact — use `> [!contradiction]` callout
- ❌ Create a new page when an existing page covers the concept — extend instead
- ❌ Skip `index.md` or `log.md` updates after wiki writes
- ❌ Apply lint fixes without user authorization
- ❌ Edit an existing `log.md` entry (file a `correction` instead)
- ❌ Stop researching unless the human interrupts you

## 10. Reporting Format

After wiki operations, reply with:

```markdown
**Pages created**: <list, or "none">
**Pages updated**: <list, or "none">
**Links added**: <count>
**Contradictions recorded**: <count or "none">
**Index regenerated**: yes / no
**Log entry**: <the exact log line>
```

## 11. Adapting for Your Domain

1. Edit `program.md` with your research objective, tools, and parameters.
2. Replace `tools/run_one.py` with your experiment runner.
3. Add raw sources to `raw/papers/`, `raw/data/`, etc.
4. Launch the agent and let it run.

Do **not** weaken §§ 4–8. They are load-bearing for the wiki's compounding property.
