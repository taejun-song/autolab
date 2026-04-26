---
type: source-summary
title: "Ha, Ko, Park, Zhang (2016) — Collective Synchronization of Classical and Quantum Oscillators"
created: 2026-04-14
updated: 2026-04-14
sources: []
tags: [dynamical-systems, synchronization, statistical-physics, kinetic-theory, pde, mathematical-biology]
aliases: ["Ha-Ko-Park-Zhang 2016", "Ha 2016 survey", "HKPZ 2016", "collective synchronization of classical and quantum oscillators"]
source_file: "../raw/papers/EMS-HKPZ-final(16-8-29).pdf"
source_kind: pdf
source_date: 2016-08-29
---

# Ha, Ko, Park, Zhang (2016) — Collective Synchronization of Classical and Quantum Oscillators

A 60-page survey by Seung-Yeal Ha, Dongnam Ko, Jinyeong Park, and Xiongtao Zhang presenting five synchronization models — Peskin, Winfree, Kuramoto, Lohe, and Schrödinger–Lohe — in a unified framework, with a rigorous mathematical treatment of complete synchronization, phase-locked states, and kinetic limits. This wiki intentionally scopes out the two quantum-synchronization models (Lohe §5 and Schrödinger–Lohe §6) and distils only the classical content (§§1–4).

## Bibliographic details

- **Authors:** Seung-Yeal Ha (Seoul National University + Korea Institute for Advanced Study), Dongnam Ko, Jinyeong Park, Xiongtao Zhang (all Seoul National University).
- **Venue:** *EMS Surveys in Mathematical Sciences* (DOI 10.4171/EMSS/x), published by the European Mathematical Society. Filename dates the final version as `16-8-29`, giving `source_date: 2016-08-29`; a handwritten note on the last page reads "Received submission date; revised February 1, 2017," so the refereed version was finalised early 2017. I've used the 2016 manuscript date.
- **Length:** 60 pages (pages 1–55 text, 56–60 references).
- **Pages read:** all 60, in four chunks (1–10, 11–25, 26–40, 41–60).
- **MSC:** 70F99, 92D25 (given in frontmatter).
- **Keywords** (given): Kuramoto oscillators, large-time dynamics, Lohe oscillators, synchronization, Winfree oscillators.

## What the paper does

The paper is a **unified survey** of five agent-based synchronization models, organised around the Kuramoto model as the common core. The authors explicitly frame the subject by the modelling question:

> Under what conditions on initial data and parameters in the model can we expect some desired collective behaviors of the model?

and then answer that question in parallel for each of the five models. The paper also derives reductions between models, showing that Winfree, Lohe, and Schrödinger–Lohe all contain Kuramoto as a limit.

### Five models, three classes

§2 introduces a classification of agent-based synchronization models into three categories and names one or two representatives of each:

| Class | State variable | Paper's models |
|---|---|---|
| Pulse-coupled | Voltage-like potential with firing threshold | Peskin (integrate-and-fire) |
| Phase-coupled | Scalar phase $\theta_j \in S^1$ | Winfree, Kuramoto |
| State-coupled | Matrix or wave function | Lohe ($U(d)$), Schrödinger–Lohe ($L^2$) |

The third class — state-coupled quantum models — is intentionally not tracked in this wiki and is mentioned here only to describe the source's full scope. The summary below distils §§1–4 (pulse- and phase-coupled / classical) and ignores §§5–6 (Lohe, Schrödinger–Lohe / quantum).

## Bullet distillation

- **Kuramoto as gradient flow (§2.2.2).** Under symmetric network and $\sum \Omega_k = 0$, the Kuramoto model is $\dot{\Theta} = -\nabla V$ with analytic potential $V = -\sum\Omega_k\theta_k + (K/(2N))\sum c_{kl}(1 - \cos(\theta_k - \theta_l))$. Analytic potential rules out chaos; convergence is equivalent to uniform boundedness.
- **Complete synchronization for generic initial data (Theorem 4.2, Ha–Kim–Ryoo 2016).** For zero-sum natural frequencies and generic initial configuration $\Theta^0$ (distinct components, $R^0 > 0$), there exists $K_\infty$ such that for $K \geq K_\infty$ the solution converges to a phase-locked state. This removes the earlier $D(\Theta^0) < \pi$ (half-circle) restriction. Five-ingredient proof: scaling, gradient flow, identical-oscillator asymptotics, finite-time continuity between identical and non-identical systems, strong-black-hole confinement.
- **Finiteness of phase-locked states (Theorem 4.3, Verwoerd–Mason / Ha–Kim–Ryoo).** For $K \gg ||\Omega||_\infty$, $2^{N-1} \leq |\mathcal{P}| \leq 2^N$ where $\mathcal{P}$ is the set of phase-locked states up to rigid rotation, parameterised by $(\beta, \Sigma) \in [||\Omega||_\infty/K, 1] \times \{-1, 1\}^N$ via an explicit transcendental self-consistency equation. See [[phase-locked-state]].
- **Half-circle structure (Theorems 4.4–4.5, Choi et al.).** Phase-locked states confined to $D(\Theta) < \pi$ have frequency-ordered phases, are unique up to rotation, and admit explicit upper/lower bounds on transversal phase differences.
- **Kuramoto–Sakaguchi equation (§4.5).** The kinetic limit $\partial_t f + \partial_\theta(\omega[f]f) = 0$ with $\omega[f] = \Omega - KL[f]$. Solution classes: measure-valued (Lancellotti 2005, Cañizo–Carrillo–Rosado, CCHKK), $L^\infty$-weak, BV entropy weak (Amadori–Ha–Park, via wave-front tracking). See [[kuramoto-sakaguchi-equation]].
- **Nonlinear Landau damping for the K-S equation.** "Kuramoto conjecture that below the critical coupling strength the incoherent solution is expected to be nonlinearly stable ... The verification of this nonlinear phenomena rigorously has been done in aforementioned literature" — referring to Chiba (2015), Fernandez–Gérard-Varet–Giacomin (2016), Ha–Xiao, Benedetto–Caglioti–Montemagno. This is the direct post-2000 resolution of what [[strogatz-2000-from-kuramoto-to-crawford]] flagged as open. See [[kuramoto-stability-problem]] for the updated status.
- **Winfree model (§3).** Four asymptotic patterns classified by rotation number: COD, POD, CPLS, PPLS. Emergence of COD under sufficient coupling and confined initial data (Theorem 3.1, Ha–Park–Ryoo). Exponential emergence of PPLS for majority sub-ensembles (Theorem 3.2, Ha–Ko–Park–Ryoo). Existence of periodic locked orbits in a bifurcation region (Theorem 3.4, Oukil–Kessi–Thieullen). Gradient-flow structure iff $S = I'$ (Proposition 2.1).
- **Winfree → Kuramoto reduction.** Low-coupling slow-phase averaging gives the Kuramoto model up to a coupling rescaling, for short time windows. Long-time dynamics of Winfree and Kuramoto diverge; Winfree admits oscillator death, Kuramoto does not.
- **Peskin model (§2.1.1).** Integrate-and-fire pulse-coupled oscillators; Mirollo–Strogatz (1990) theorem: except on a measure-zero set, identical all-to-all Peskin oscillators achieve complete synchronization in finite time. Explicit characterisation of the exceptional set and non-identical extensions remain open.
- **Lohe (§5) and Schrödinger–Lohe (§6).** Two state-coupled quantum-synchronization models. **Read but intentionally not distilled** — this wiki scopes out the quantum side of the subject. The Lohe model is a matrix-valued non-abelian generalization of Kuramoto on $(U(d))^N$ that reduces to Kuramoto at $d = 1$; the Schrödinger–Lohe model is its infinite-dimensional PDE version, a coupled nonlinear Schrödinger system that reduces to the finite-dimensional Lohe system via a free-Schrödinger-propagator isometry for identical potentials. Both were introduced by Max Lohe (2009–2010). If the wiki's scope expands to quantum synchronization in future, this source is the natural entry point for that direction.

## Why this source matters

Within the classical scope this wiki tracks, this survey does two things no earlier source did:

1. **Consolidates the post-2000 Kuramoto theory** — the resolution of the nonlinear Landau damping conjecture, the extension of complete-synchronization results to generic initial data, the finiteness of phase-locked states, and the measure-valued / BV well-posedness theory for the [[kuramoto-sakaguchi-equation]]. Every one of these is cited as a specific theorem with attribution, and they collectively transform the landscape from what [[strogatz-2000-from-kuramoto-to-crawford]] described.

2. **Places Peskin, Winfree, and Kuramoto under a single classification** — three classes (pulse / phase / state coupled), with explicit reductions from Winfree to Kuramoto. Before this survey the three models were typically treated in separate literatures.

Beyond the classical scope, the survey also develops the Lohe and Schrödinger–Lohe quantum-synchronization models in detail (§§5–6). That content is not distilled in this wiki by scoping decision.

## What the paper does not cover

- **Network topology effects.** The paper works almost entirely in the all-to-all coupling regime $c_{kj} = 1/N$. General graph topology (small-world, scale-free, dynamic networks, locality) is beyond its scope. The authors point to the Dörfler–Bullo 2014 survey "Synchronization in complex networks of phase oscillators" as complementary reading for that side of the subject.
- **Finite-$N$ propagation of chaos.** Well-posedness of the Kuramoto–Sakaguchi kinetic equation is developed, but rigorous quantitative convergence of finite-$N$ Kuramoto trajectories to K-S solutions — in the $O(N^{-1/2})$-fluctuation sense — is not treated. [[kuramoto-finite-n-convergence]] remains open.
- **Entire-branch nonlinear stability of the partially-synchronized state.** The paper reports Chiba 2015 and Fernandez–Gérard-Varet–Giacomin 2016 as resolving major parts of the stability problem, but does not claim full resolution of the entire-branch linear stability question; [[kuramoto-stability-problem]] remains `partially-resolved`.
- **Proofs in detail.** As a survey, the paper states and briefly sketches theorems but rarely gives full proofs. Readers wanting proofs are directed to the primary-source papers; this is explicitly acknowledged in the authors' "style of presentation" paragraph at the end of §1.
- **Physical / engineering applications.** Applications in biology, control theory, power grids, etc. are listed as motivations but not developed. The paper is a mathematical survey, not a modelling textbook.

## Notable quotes

> Our main focus is to present synchronization estimates for several synchronization models in a unified framework.
> — §1, stating the paper's thesis.

> Kuramoto conjecture that below the critical coupling strength the incoherent solution is expected to be nonlinearly stable, in contrast above the critical coupling strength, it is expected to be nonlinearly unstable. The verification of this nonlinear phenomena rigorously has been done in aforementioned literature.
> — §4.5, closing the question [[strogatz-2000-from-kuramoto-to-crawford]] had left open.

## Key references cited

Already ingested as primary sources in this wiki:

- **[40] Ha, S.-Y., Kim, H. K., Ryoo, S. W.** "Emergence of phase-locked states for the Kuramoto model in a large coupling regime." *Commun. Math. Sci.* **14** (2016), 1073–1091. — Present in the wiki as [[ha-kim-ryoo-2016-emergence-phase-locked-states]]. This is the primary source for the generic-initial-data complete-synchronization theorem the survey cites as its Theorem 4.2.

Not yet in wiki (high-priority next ingests based on what this survey cites):

- **[20] Chiba, H.** "A proof of the Kuramoto conjecture for a bifurcation structure of the infinite-dimensional Kuramoto model." *Ergodic Theory and Dynamical Systems* **35** (2015), 762–834. — The decisive post-2000 result on [[kuramoto-stability-problem]].
- **[35] Fernandez, B., Gérard-Varet, D., Giacomin, G.** "Landau damping in the Kuramoto model." *Annales Henri Poincaré* **17** (2016), 1793–1823. — Rigorous nonlinear Landau damping.
- **[68] Mirollo, R. E., Strogatz, S. H.** "Stability of incoherence in a population of coupled oscillators." *J. Stat. Phys.* **63** (1991), 613–635. — The continuum-limit PDE formulation that underlies everything.
- **[69] Mirollo, R. E., Strogatz, S. H.** "Synchronization of pulse-coupled biological oscillators." *SIAM J. Appl. Math.* **50** (1990), 1645. — The Mirollo–Strogatz theorem for the [[peskin-model]].
- **[30] Dörfler, F., Bullo, F.** "Synchronization in complex networks of phase oscillators: A survey." *Automatica* **50** (2014), 1539–1564. — Complementary survey on the network-topology side.
- **[1] Acebrón, J. A., Bonilla, L. L., Pérez Vicente, C. J. P., Ritort, F., Spigler, R.** "The Kuramoto model: A simple paradigm for synchronization phenomena." *Rev. Mod. Phys.* **77** (2005), 137–185. — The other major review paper covering Kuramoto through 2005, complementary to Strogatz 2000 and this survey.
- **[59] Lancellotti, C.** "On the Vlasov limit for systems of nonlinearly coupled oscillators without noise." *Transport Theory and Statistical Physics* **34** (2005), 523–535. — First formal $N \to \infty$ mean-field result; cited on [[kuramoto-finite-n-convergence]].
