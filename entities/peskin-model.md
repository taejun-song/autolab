---
type: entity
title: "Peskin Model"
created: 2026-04-14
updated: 2026-04-14
sources:
  - "[[ha-ko-park-zhang-2016-collective-synchronization]]"
tags: [dynamical-systems, synchronization, mathematical-biology]
aliases: ["Peskin model", "integrate-and-fire model", "pulse-coupled oscillator model"]
year_stated: 1975
---

# Peskin Model

The Peskin model is a pulse-coupled integrate-and-fire model of cardiac pacemaker cells, introduced by Charles S. Peskin in 1975, in which identical oscillators emit instantaneous voltage kicks to their neighbours upon firing and synchronize in finite time.

## Governing equations

Each cell $j$ carries a normalised membrane potential $x_j(t) \in [0, 1]$ that evolves in two steps.

**Integrating step** — between firings, the potential obeys the linear ODE

$$\dot{x}_j \;=\; -\delta_j\, x_j + S_j,$$

with positive intrinsic parameters $\delta_j$ (leakage) and $S_j$ (drive) satisfying $S_j > \delta_j$ so the potential monotonically increases toward the threshold.

**Firing step** — when $x_j(t_*) = 1$ the cell fires: its own potential is reset to zero, and every other cell gets an instantaneous kick

$$x_j(t_*^+) = 0, \qquad x_k(t_*^+) = \min\{1, x_k(t_*) + \varepsilon_{jk}\}, \qquad k \neq j.$$

If a kicked cell is already above $1 - \varepsilon_{jk}$ its potential clips at unity and it fires immediately, possibly triggering a cascade.

Peskin's original study considers **identical** pacemaker cells with all-to-all coupling:

$$\delta_j = \delta, \qquad S_j = S, \qquad \varepsilon_{jk} = \varepsilon > 0 \quad \text{for all } j, k.$$

## Mirollo–Strogatz theorem

Peskin's original 1975 book showed finite-time synchronization for $N = 2$ and conjectured it for all $N$ and generic initial data. Mirollo and Strogatz (1990) settled the conjecture:

**Theorem (Mirollo–Strogatz, 1990).** Let $\{x_j(t)\}$ solve the identical-cell Peskin model with all-to-all coupling. Then, except for a set of initial configurations of Lebesgue measure zero, the ensemble achieves complete synchronization in finite time — there exists $T \in (0, \infty)$ such that

$$|x_i(t) - x_j(t)| \;=\; 0, \qquad t \geq T,\ 1 \leq i, j \leq N.$$

See [[ha-ko-park-zhang-2016-collective-synchronization]] Theorem 2.1 for the statement as it is now commonly quoted.

The proof uses a Poincaré-map / absorption argument: one constructs a firing return map and shows that every orbit outside a measure-zero bad set is eventually captured into the synchronized fixed point. The measure-zero set is characterised only abstractly — the Mirollo–Strogatz argument does not provide an explicit criterion for whether a given initial configuration belongs to it.

## Why pulse-coupled is different

The Peskin model sits in a distinct regime from the phase-coupled models discussed in [[synchronization]]: interactions are **instantaneous and discrete** (firings at isolated times) rather than continuous (phase forcing at all times). This produces qualitative differences:

- **Finite-time synchronization**, not asymptotic. The Peskin ensemble arrives at its synchronized state at a *definite* moment $T$, not in the limit $t \to \infty$.
- **Cascade amplification.** A single firing can trigger a chain of threshold crossings in a single instant — something impossible in a smooth phase model.
- **Measure-zero exceptional set.** Unlike the [[kuramoto-model]] where the basin of attraction is open in configuration space, the Peskin model's bad set is characterised only as "Lebesgue-null," giving no constructive exclusion criterion.

## Open questions (as of 2016)

[[ha-ko-park-zhang-2016-collective-synchronization]] Remark 2.1 records two open-problem directions:

1. **Explicit characterisation of the exceptional measure-zero set.** The Mirollo–Strogatz proof is non-constructive about which initial configurations fail to synchronize. An explicit description would let one check synchronization for a given concrete configuration, which is practically important for modelling cardiac pacemakers where not all configurations are equally likely.
2. **Non-identical Peskin oscillators.** The rigorous justification of synchronization for populations of non-identical pacemaker cells (different $\delta_j, S_j$) is, as of 2016, still open. The identical-cell Mirollo–Strogatz argument does not obviously extend.

## Historical position

Peskin's 1975 book *Mathematical Aspects of Heart Physiology* (Courant Institute) introduced the model specifically to study cardiac pacemaker synchronization — the sinoatrial node's ability to produce regular heartbeats despite cell-level variability. This predates [[kuramoto-1975-self-entrainment]] by essentially zero time (both 1975) but answered a different question: Peskin was modelling biological tissue, Kuramoto was modelling far-from-equilibrium statistical-physics phase transitions. The two lines of work fused in the 2000s when pulse-coupled and phase-coupled models came to be viewed as complementary descriptions of the same physical phenomenon.

The Peskin model's clean finite-time-synchronization result stands in interesting contrast to Kuramoto's asymptotic-synchronization result: the pulse-coupled structure permits a sharper conclusion at the cost of the restrictive identical-cell / all-to-all assumption.
