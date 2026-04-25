# AutoLab

Autonomous research agent on top of an LLM wiki.

*You write `program.md`. The agent reads it, runs experiments, writes findings to a wiki, and re-reads the program for updates. You wake up to a wiki full of insights and a log of experiments.*

## How it works

```
Human edits program.md
        ↓
   LLM Agent (Claude)
        ↓
    ┌───┴───┐
    │       │
 Tools    Wiki
 (your     (persistent
  CLIs)    knowledge)
    │       │
    └───┬───┘
        ↓
  Results + Wiki Pages
```

Three files matter:

- **`program.md`** — your instructions to the agent. What to optimize, what tools to use, what matters. Edited by the human.
- **`CLAUDE.md`** — wiki rules + lab rules. Defines how knowledge is structured. Edited by the human.
- **`tools/run_one.py`** — your domain-specific experiment runner. The agent calls this. Written by you.

The agent reads `program.md`, uses your tools, records results, writes wiki pages about what it discovers, and periodically re-reads `program.md` for updates. You steer the research by editing the program — no need to restart the agent.

## Quick start

```bash
# 1. Clone and set up
git clone https://github.com/taejun-song/autolab.git
cd autolab

# 2. Copy the example for your domain (or start from scratch)
cp -r examples/hello/ my-lab/
cd my-lab/

# 3. Edit program.md with your research objective and tools
vim program.md

# 4. Launch the agent
claude --dangerously-skip-permissions -p "Read program.md for your instructions. You are an autonomous research agent. Start the experiment loop. Never stop."
```

## Concepts

### The Wiki

AutoLab uses an Obsidian-compatible wiki as the agent's persistent memory. The agent writes:

- **`concepts/`** — reusable ideas it discovers (e.g., "learning rate warmup helps convergence")
- **`entities/`** — named things (models, datasets, papers)
- **`summaries/`** — distillations of sources it reads
- **`comparisons/`** — side-by-side analyses
- **`syntheses/`** — cross-experiment insights

Every page has YAML frontmatter with `type`, `title`, `created`, `updated`, `tags`. The wiki compounds over time — future agent sessions read past findings before starting new experiments.

### The Program

`program.md` is your interface to the agent. It defines:

1. **Goal** — what to optimize (lower loss, higher accuracy, better binding score)
2. **Tools** — CLI commands the agent can run
3. **Constraints** — what the agent can and cannot modify
4. **Current state** — scoreboard, known insights, unexplored areas
5. **Loop** — the experiment cycle (check status → hypothesize → experiment → analyze → record)

The agent re-reads `program.md` every N experiments to pick up your updates. You can add new tools, change the objective, redirect focus — all without restarting.

### Hot Reload

Every few experiments, the agent checks if `program.md` has been modified. If yes, it re-reads the file. This means you can:

- Add a new tool mid-run → agent starts using it
- Change the objective → agent redirects
- Add insights you noticed → agent incorporates them

No kill, no restart, no lost context.

## Project structure

```
my-lab/
├── program.md          # Your instructions to the agent (you edit this)
├── CLAUDE.md           # Wiki + lab rules (you edit this)
├── index.md            # Wiki index (agent maintains)
├── log.md              # Chronological log (agent maintains)
├── tools/
│   └── run_one.py      # Your experiment runner (you write this)
├── raw/                # Source materials (read-only)
│   ├── papers/
│   └── data/
├── concepts/           # Wiki pages (agent writes)
├── entities/           #
├── summaries/          #
├── comparisons/        #
├── syntheses/          #
└── results/            # Experiment outputs (agent writes)
    └── results.tsv
```

## Examples

### `examples/hello/` — Train a small LLM (Karpathy-style)
The agent modifies `train.py`, trains for 5 minutes, evaluates val_bpb, keeps or discards.

### `examples/binder/` — Design protein binders (DNA/protein)
The agent runs RFdiffusion3 experiments, scores with RoseTTAFold3, optimizes ipTM across multiple targets.

## Design principles

1. **The agent is the researcher.** Not a script runner. It reads papers, forms hypotheses, designs experiments, interprets results.

2. **The wiki is the lab notebook.** Knowledge persists across sessions. A new agent reads past findings before starting.

3. **program.md is your steering wheel.** Edit it to redirect. No process management needed.

4. **Tools are atomic.** One experiment per call. The agent decides what to run, not a loop script.

5. **Simpler is better.** A small improvement from understanding is worth more than a large improvement from brute force.

## Requirements

- [Claude Code](https://claude.ai/claude-code) (CLI)
- Your domain-specific tools
- A GPU (if your experiments need one)

## License

MIT
