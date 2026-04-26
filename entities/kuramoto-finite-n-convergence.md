---
type: entity
title: "Kuramoto Finite-N Convergence Problem"
created: 2026-04-14
updated: 2026-04-15
sources:
  - "[[strogatz-2000-from-kuramoto-to-crawford]]"
  - "[[ha-ko-park-zhang-2016-collective-synchronization]]"
  - "[[brezis-2011-functional-analysis-sobolev-pdes]]"
  - "[[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]]"
tags: [dynamical-systems, synchronization, statistical-physics, probability, open-problem]
aliases: ["finite-N Kuramoto", "Kuramoto finite-N theorem", "Kopell's question"]
status: open
year_stated: 1986
---

# Kuramoto Finite-N Convergence Problem

Does the finite-$N$ Kuramoto oscillator system converge, in a rigorous probabilistic sense, to its continuum limit as $N \to \infty$, and at what rate do the finite-$N$ fluctuations of the order parameter decay?

## Statement

Fix a symmetric unimodal native-frequency density $g(\omega)$ and coupling $K$. Draw $N$ frequencies $\omega_1,\dots,\omega_N$ i.i.d. from $g$, run the [[kuramoto-model|Kuramoto ODE system]] on the $N$-torus with some initial condition, and form the empirical order parameter $r_N(t) = |N^{-1}\sum_j e^{i\theta_j(t)}|$. Let $r_\infty(K)$ denote the steady-state order parameter predicted by the [[kinetic-formulation|continuum Kuramoto model]] (equivalently, the $r$-value Kuramoto derived from his self-consistency argument).

The finite-$N$ convergence problem asks for rigorous statements of the following types:

1. **Law of large numbers.** For large $N$, most realisations of the frequencies, and most initial conditions, $r_N(t)$ approaches $r_\infty(K)$ and stays within $O(N^{-1/2})$ of it for a large fraction of the time.
2. **Fluctuation theorem.** The fluctuations of $r_N(t)$ around $r_\infty(K)$ are of order $O(N^{-1/2})$ uniformly in $t$, except perhaps in a shrinking neighbourhood of the critical point $K = K_c$.
3. **Propagation of chaos.** Any finite collection of oscillators becomes asymptotically independent as $N \to \infty$, and the marginal law converges to the solution of the continuum PDE.

The three statements are standard mean-field probability targets and all three remain without rigorous proof for the Kuramoto model, according to [[strogatz-2000-from-kuramoto-to-crawford]].

## History

- **Kopell's question (1986).** In the last of her three Bowen lectures at UC Berkeley, Nancy Kopell pointed out that Kuramoto's 1975 self-consistency argument assumes $r(t) \equiv \text{const}$, which is strictly false for any finite $N$. In fact at $K = 0$ the oscillator trajectories are dense on the $N$-torus, so $r(t)$ visits every value in $[0, 1]$ infinitely often — completely unlike the constant-$r$ picture. Kopell asked whether a rigorous finite-$N$ analysis, plus a convergence result as $N \to \infty$, could be supplied. See [[strogatz-2000-from-kuramoto-to-crawford]] for Strogatz's recollection.
- **Daido (1987–1990) and Kuramoto–Nishikawa.** Heuristic and numerical work placed the fluctuations at $O(N^{-1/2})$ for $K$ bounded away from $K_c$, with amplification of fluctuations near the critical point. The analyses are physical / scaling arguments rather than rigorous mean-field probability theorems.
- **As of March 2000 (Strogatz).** Strogatz writes explicitly: "the issue of fluctuations remains wide open mathematically. As of March 2000, there are no rigorous convergence results about the finite-$N$ behavior of the Kuramoto model."
- **Lancellotti (2005), "On the Vlasov limit for systems of nonlinearly coupled oscillators without noise"** (*Transport Theory and Statistical Physics* **34**, 523–535). First formal $N \to \infty$ mean-field convergence result for the deterministic Kuramoto-like system, adapting Vlasov-limit techniques from plasma physics. This is the technical foundation that Cañizo–Carrillo–Rosado (2011) and Carrillo–Choi–Ha–Kang–Kim (2014) built on for measure-valued solutions of the [[kuramoto-sakaguchi-equation]].
- **Measure-valued propagation.** The Lancellotti line establishes that the empirical measure $\mu_t^N = N^{-1}\sum_i\delta_{(\theta_i, \Omega_i)}$ of the finite-$N$ Kuramoto system converges, as $N \to \infty$, to a measure-valued solution of the K-S equation. This is weaker than a quantitative propagation-of-chaos statement — it is a distributional convergence along the empirical-measure path — and it does not give $O(N^{-1/2})$ fluctuation-scale control.

So as of [[ha-ko-park-zhang-2016-collective-synchronization]] (2016) the picture has improved: the qualitative $N \to \infty$ limit has been made precise in the measure-valued sense, and the machinery comes from the kinetic-theory tradition. However:

- No rigorous **quantitative** bound $|r_N(t) - r_\infty(K)| \lesssim N^{-1/2}$ uniformly in $t$ is available.
- No rigorous **propagation-of-chaos theorem** (asymptotic independence of finite marginals) is known beyond the measure-valued level.
- The delicate behaviour near the critical point $K = K_c$, where $O(N^{-1/2})$ fluctuations are expected to be amplified, is not captured.

The status therefore remains **open** at the level Kopell originally asked about — the $O(N^{-1/2})$-uniform fluctuation theorem and the rigorous propagation-of-chaos result — even though the measure-valued mean-field limit has been made rigorous.

## Why it is hard

At $K = 0$ the oscillators decouple, and the natural reference dynamics on the torus is quasi-periodic — fine on a single trajectory but catastrophic for a naive time-averaging argument: $r_N(t)$ is *not* self-averaging pointwise in $t$, only in a distributional sense. For $K > 0$ the population splits into locked and drifting groups separated by a sharp boundary $|\omega_i| = K r(t)$, and finite-$N$ fluctuations of $r$ wiggle this boundary, producing a fuzzy intermediate population of oscillators that are neither cleanly locked nor cleanly drifting. Standard mean-field coupling / propagation-of-chaos machinery (as developed for McKean–Vlasov diffusions) applies cleanly when the drift is Lipschitz in the state; the Kuramoto drift $K r \sin(\psi - \theta)$ is Lipschitz, but the coupling of $r$ itself to the law of the empirical measure is where the subtlety lives — and especially near $K = K_c$ where the law-of-large-numbers scale $O(N^{-1/2})$ is expected to be amplified.

The functional-analytic setting this lives in — weak-* convergence of empirical measures on $\mathcal{M}(\mathbb{T} \times \mathbb{R})$, compactness of bounded sets in the dual topology (Banach–Alaoglu), the crucial caveat that nonlinear maps are *not* in general continuous weak→weak — is the content of Chapter 3 of [[brezis-2011-functional-analysis-sobolev-pdes]]; see the concordance there. Brezis does not treat tightness or Prokhorov's theorem, which are the probabilistic upgrades needed; the user must supplement with a dedicated probability reference for the propagation-of-chaos machinery proper.

## Alternative approach: deterministic finite/infinite-$N$ correspondence via Möbius group

A complementary route avoids the probabilistic propagation-of-chaos framework entirely. [[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]] shows that for the [[kuramoto-on-a-sphere|Kuramoto model on $S^{d-1}$]] with **identical** oscillators, the same Möbius-group action on the unit ball $B^d$ controls finite-$N$ and infinite-$N$ dynamics under a single parameterization: at finite $N$ the dynamics are confined to group orbits of dimension $d(d+1)/2$ (independent of $N$), and at $N \to \infty$ the same group action on the uniform measure on $S^{d-1}$ yields the [[ott-antonsen-ansatz]] manifold of hyperbolic Poisson densities — with the *same* reduced ODE system in both cases. This is the paper's "seamless connection between finite and infinite-$N$ dynamics."

For **identical** oscillators this is a rigorous deterministic answer to the finite-$N$ → infinite-$N$ correspondence, one that does not require tightness or weak-* compactness at all. The limitation is that it works only for identical oscillators: the group-orbit structure relies on the common drift term. For **non-identical** frequencies (which is the main physically interesting case), the reduction breaks down, and the original probabilistic propagation-of-chaos question remains open. The deterministic framework does, however, provide exactly-solvable test problems against which any future propagation-of-chaos theorem can be benchmarked.

## Relation to other open problems

This problem is the probabilistic counterpart of [[kuramoto-stability-problem]]. Even if one had a complete linear and nonlinear stability theory for the continuum-limit partially-synchronized branch, it would not automatically translate back to the original $N$-oscillator ODE system; that translation is what a finite-$N$ convergence theorem would supply. Together the two problems constitute the rigorous foundation of the Kuramoto model that Kopell asked for in 1986.

## Connection to kinetic theory

The problem sits inside a broader mean-field / kinetic-limit literature — McKean–Vlasov diffusions, the Vlasov limit of $N$-body Newtonian systems, propagation of chaos — and any eventual rigorous treatment is likely to draw on that machinery. See [[kinetic-formulation]] for the PDE setting the finite-$N$ system is supposed to converge to.
