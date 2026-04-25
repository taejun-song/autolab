# AutoLab Program

This file controls the autonomous research agent. Edit it to steer the research.

## Goal

<!-- Replace with your research objective -->
Get the lowest val_bpb on the validation set.

## Tools

<!-- Define the CLI commands the agent can use -->

### Check status
```bash
python tools/run_one.py --status
```

### Run an experiment
```bash
python tools/run_one.py --config param1=value1 param2=value2
```

### Read results
```bash
tail -20 results/results.tsv
```

### Search literature
```bash
# Search arXiv
python tools/literature.py search "your query here"

# Search Semantic Scholar
python tools/literature.py scholar "your query here"

# Download a paper by arXiv ID
python tools/literature.py fetch 2310.15138

# Download by DOI (open-access via Unpaywall)
python tools/literature.py fetch-doi 10.1038/s41586-023-06415-8

# Search and download top result
python tools/literature.py search "your query" --download

# List downloaded papers
python tools/literature.py list
```

## Parameters

<!-- List the parameters the agent can tune -->

| Parameter | Range | Effect |
|-----------|-------|--------|
| learning_rate | 0.001-0.1 | Training learning rate |
| batch_size | 16-256 | Batch size |

## Current State

<!-- Update this as the research progresses, or let the agent update it -->
No experiments run yet.

## The Research Loop

LOOP FOREVER:

### Phase 0: Check for updates

Every 5 experiments, check if this file (`program.md`) has been modified. If it changed, re-read it.

### Phase 1: Literature & Knowledge

Before experimenting, build understanding:

1. **Search for relevant literature**: Use web search to find papers, blog posts, or code related to your current problem. Search terms should come from your current hypothesis or the domain.
2. **Ingest into wiki**: When you find a useful source, save it to `raw/` and create a source-summary page. Unlike supervised mode, you do NOT need user approval for ingests during autonomous research — just follow the APPLY order (create pages → update cross-links → source-summary → regenerate index → log entry).
3. **Read existing wiki**: Check `index.md`. Has a previous session already covered this? Build on existing knowledge, don't re-derive.
4. **Synthesize**: If you see connections across multiple sources or experiments, write a `synthesis` page.

### Phase 2: Ideation

Generate experiment ideas from multiple sources:

1. **From literature**: "This paper says X works. Does it apply to our problem?"
2. **From cross-experiment patterns**: "Parameter A helps target 1 but hurts target 2. Why?"
3. **From failures**: "The last 10 experiments all failed when using X. What if we tried the opposite?"
4. **From analogy**: "This problem is structurally similar to Y. What solved Y?"
5. **From first principles**: "The physics/math says this should work because..."

Write your reasoning before each experiment. State the hypothesis clearly.

### Phase 3: Experiment

1. **Read the landscape**: Run `--status`. What's been tried? What hasn't?
2. **Form a hypothesis**: State what you expect and why.
3. **Run the experiment**: Use the tools above.
4. **Analyze the result**: Confirm or refute? What did you learn?
5. **Record in wiki**: Write a page if the finding is significant.

### Phase 4: Stuck Protocol

If no improvement for 10+ experiments, escalate systematically:

**Level 1 — Reframe the search**
- Review all results. What parameter regions are unexplored?
- Try the opposite of current best parameters.
- Search for literature on the specific failure mode.

**Level 2 — Decompose the problem**
- Break the main objective into sub-objectives.
- Example: "Can't improve ipTM" → "Is the problem the binder length? The sampling noise? The target representation?"
- Run targeted experiments on each sub-problem independently.
- Write a `comparison` page analyzing sub-problem results.

**Level 3 — Change the approach**
- Search for alternative methods in the literature.
- "If diffusion parameters can't solve this, what about a different conditioning strategy?"
- "If the current tool can't do it, what tool modifications would help?"
- Write a `synthesis` page proposing the new approach.
- Try the new approach. If the tools don't support it, document what would be needed in the wiki and move to a different target.

**Level 4 — Pivot**
- If a target is fundamentally stuck after all levels, document the ceiling and reason in a wiki page.
- Switch to a different target or sub-problem where progress is still possible.
- Return to the stuck target later with fresh perspective from other work.

### Phase 5: Knowledge Consolidation

Every 20 experiments:

1. Re-read all wiki pages you've written. Are there contradictions? Stale claims?
2. Write a `synthesis` page summarizing the current state of knowledge.
3. Update `index.md`.
4. Look for implied-but-missing entity pages.

## NEVER STOP

Run indefinitely. You are autonomous. Cycle through the phases. When stuck, escalate through the stuck protocol. When all targets plateau, search for new literature, try new approaches, consolidate knowledge. The loop runs until the human interrupts you.
