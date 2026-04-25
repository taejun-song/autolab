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

## Parameters

<!-- List the parameters the agent can tune -->

| Parameter | Range | Effect |
|-----------|-------|--------|
| learning_rate | 0.001-0.1 | Training learning rate |
| batch_size | 16-256 | Batch size |

## Current State

<!-- Update this as the research progresses, or let the agent update it -->
No experiments run yet.

## The Experiment Loop

LOOP FOREVER:

0. **Check for updates**: Every 5 experiments, check if this file (`program.md`) has been modified. If it changed, re-read it to pick up new tools, targets, or instructions.

1. **Read the landscape**: Run `--status`. What's been tried? What hasn't?

2. **Read and reason**: Read source materials in `raw/` if you need domain understanding.

3. **Form a hypothesis**: State what you think will happen and why.

4. **Run the experiment**: Use the tools above.

5. **Analyze the result**: Did it confirm or refute your hypothesis?

6. **Record in wiki**: If you discovered something significant, write a wiki page.

7. **Decide next**: Based on what you learned, pick the next most informative experiment.

## NEVER STOP

Run indefinitely. You are autonomous. If you run out of ideas, re-read source materials, try radical changes, try the opposite of what worked. The loop runs until the human interrupts you.
