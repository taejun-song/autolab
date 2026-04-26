---
type: concept
title: "Phase-Locked State"
created: 2026-04-14
updated: 2026-04-14
sources:
  - "[[ha-ko-park-zhang-2016-collective-synchronization]]"
  - "[[ha-kim-ryoo-2016-emergence-phase-locked-states]]"
  - "[[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]]"
tags: [dynamical-systems, synchronization, statistical-physics]
aliases: ["phase locking", "phase-locked configuration", "CPLS", "PPLS", "complete phase-locked state", "partially phase-locked state"]
---

# Phase-Locked State

A phase-locked state of a coupled-oscillator ensemble is a configuration in which every pairwise phase difference is constant in time, so the whole population rotates rigidly while its shape in phase space is frozen.

## Formal definition

Let $\Theta(t) = (\theta_1(t), \dots, \theta_N(t))$ be a trajectory of a phase-coupled oscillator model. The state $\Theta$ is **phase-locked** if there exist constants $\theta_{ij}^\infty$ with

$$\theta_i(t) - \theta_j(t) \;=\; \theta_{ij}^\infty \qquad \forall\, t \geq 0,\ 1 \leq i, j \leq N.$$

The state $\Theta$ **asymptotically approaches a phase-locked state** if the phase differences only settle as $t \to \infty$:

$$\exists\, \lim_{t \to \infty} |\theta_i(t) - \theta_j(t)|, \qquad 1 \leq i, j \leq N.$$

These two notions coincide in the identical-oscillator setting but diverge when there are differing native frequencies and one is working in a rotating frame.

## Rotation numbers

A coarser asymptotic invariant is the **rotation number**

$$\rho(\theta) \;=\; \lim_{t \to \infty} \frac{\theta(t)}{t},$$

when the limit exists. [[ha-ko-park-zhang-2016-collective-synchronization]] uses rotation numbers to classify the asymptotic patterns of the [[winfree-model|Winfree model]] and related phase-coupled systems into four regimes:

| Code | Name | Definition |
|---|---|---|
| **COD** | Complete oscillator death | $\rho_i = 0$ for every $i$ — every oscillator asymptotically stops |
| **POD** | Partial oscillator death | $\rho_i = 0$ for at least two but not all $i$ |
| **CPLS** | Complete phase-locked state | $\rho_i = \rho \neq 0$ for every $i$ — the ensemble rotates rigidly at a common nonzero rate |
| **PPLS** | Partially phase-locked state | $\rho_i = \rho \neq 0$ for at least two but not all $i$ |

Note that CPLS and PPLS use the rotation-number equality only; the phase-locked-state definition above requires constancy of phase *differences*. The two notions agree in the generic case where the asymptotic motion is rigid.

## In the Kuramoto model

For the [[kuramoto-model|Kuramoto model]] with zero-sum native frequencies, phase-locked states are equilibria of the rotating-frame dynamics

$$0 \;=\; \Omega_j + \frac{K}{N}\sum_{k=1}^{N}\sin(\theta_k^\infty - \theta_j^\infty), \qquad j = 1, \dots, N.$$

These are transcendental equations. Basic observations:

- **Translation invariance.** If $\Theta^\infty$ is a phase-locked state, so is $\Theta^\infty + \alpha(1, \dots, 1)$ for any $\alpha$. Phase-locked states are counted modulo this rotation.
- **Existence requires coupling to dominate frequency spread.** Because $|(K/N)\sum \sin(\theta_k^\infty - \theta_j^\infty)| \leq K$, the system has no phase-locked solutions at all if $K < |\Omega_j|$ for any $j$.
- **Nontrivial configurations at $R = 0$.** For $N \geq 4$ identical Kuramoto oscillators, there exist continuous families of phase-locked states with order parameter $R = 0$ — for instance $\Theta^\mu_k = 2k\pi/(N-2) + \mu$ for $k = 1, \dots, N-2$ together with $\theta^\mu_{N-1} = 0$, $\theta^\mu_N = \pi$ (the "splay state plus bi-polar" family). These wash out under the modulus-of-mean-field order parameter.

## Finiteness and cardinality bounds

For $N \geq 3$ Kuramoto oscillators with non-identical frequencies, the set $\mathcal{P}$ of phase-locked states modulo rotation need not be finite in general — the transcendental system has no closed-form solution — but under coupling dominance, the following counting result holds (Theorem 4.3 in [[ha-ko-park-zhang-2016-collective-synchronization]], originally in Verwoerd–Mason and Ha–Kim–Ryoo):

**Theorem (Verwoerd–Mason, Ha–Kim–Ryoo).** Let $\sum \Omega_i = 0$ and $K \geq ||\Omega||_\infty := \max_i |\Omega_i|$. Then:

1. $\mathcal{P}$ is nonempty iff there exists $\beta \in [||\Omega||_\infty/K, 1]$ and $\Sigma = (\sigma_1, \dots, \sigma_N) \in \{-1, 1\}^N$ such that
$$\beta \;=\; \frac{1}{N}\sum_{j=1}^{N}\sigma_j\sqrt{1 - (\Omega_j/(K\beta))^2}.$$
2. Each $(\beta, \Sigma)$ pair corresponds to a unique phase-locked state (up to global rotation) satisfying $K\beta\sin(\phi - \theta_j) = -\Omega_j$ and $\sigma_j\cos(\phi - \theta_j) \geq 0$. The $\beta$ is exactly the Kuramoto [[order-parameter]] $R(\Theta)$.
3. For $K \gg ||\Omega||_\infty$, the cardinality satisfies $2^{N-1} \leq |\mathcal{P}| \leq 2^N$.

In particular, $\mathcal{P}$ is finite for sufficiently large $K$, with at most $2^N$ elements. Physically, each $\Sigma \in \{-1, 1\}^N$ records a "sign choice" for each oscillator, and the $2^N$ combinatorial possibilities are refined by the geometric constraint (1).

## Half-circle confinement and ordering

When the initial phase diameter $D(\Theta^0) = \max_{j, k} |\theta_j^0 - \theta_k^0| < \pi$ — the configuration lies inside a half-circle — the asymptotic phase-locked state inherits a clean structure (Theorem 4.4 in the Ha et al. survey, originally Choi et al.):

- The phase ordering matches the frequency ordering: if $\Omega_i < \Omega_j$ then $\theta_i(t) < \theta_j(t)$ for all sufficiently large $t$.
- Phase-locked states confined to a half-circle are unique up to rigid rotation.
- The transversal phase differences $\theta_{ij} = \theta_i - \theta_j$ satisfy $\sin^{-1}(\Omega_{ij}/(KU)) \leq \lim_{t\to\infty}\theta_{ij}(t) \leq \mathcal{D}^\infty$ for explicit constants $U$ and $\mathcal{D}^\infty$.

This is what makes the half-circle regime analytically tractable: the phase ordering prevents collisions, and Gronwall-type estimates give exponential relaxation.

## Existence of phase-locked limits from generic data

The half-circle confinement analysis settles the phase-locked-state *structure* for configurations with small diameter, but it does not by itself answer the question: does a solution starting from an *arbitrary* generic configuration actually converge to a phase-locked state? [[ha-kim-ryoo-2016-emergence-phase-locked-states]] settles this for the large-coupling regime: for any initial configuration with positive order parameter $r_0 > 0$ and pairwise-distinct phases, there exists a coupling threshold $K_\infty$ such that $K \geq K_\infty$ guarantees convergence to *some* phase-locked state. The excluded set $r_0 = 0$ has Lebesgue measure zero in configuration space. See [[kuramoto-model#Complete synchronization for generic initial data]] for the theorem statement and proof strategy; the key novelty is that no half-circle assumption on the initial data is needed.

This is an *existence* statement for the limit, not a uniqueness or stability statement. The counting result above still applies: for $K \gg ||\Omega||_\infty$ there are up to $2^N$ phase-locked states, and Ha–Kim–Ryoo's theorem gives one such limit per generic initial configuration without telling you which one.

## In the Winfree model

The [[winfree-model|Winfree model]] uses the same scalar-phase formalism as Kuramoto, so phase-locked states are defined identically: a Winfree configuration is phase-locked if every pairwise phase difference is constant in time. What differs is the asymptotic classification — Winfree dynamics admit *oscillator death* regimes (COD, POD) in which some rotation numbers vanish, which Kuramoto dynamics cannot produce because Kuramoto's gradient-flow structure gives the boundedness-iff-convergence dichotomy. See the Winfree model page for the sufficient-condition frameworks for each of COD, POD, CPLS, PPLS.

## In the Kuramoto model on a sphere

For the [[kuramoto-on-a-sphere|Kuramoto model on $S^{d-1}$]] with $d \geq 3$, phase-locked states correspond to configurations in which all particles $x_i \in S^{d-1}$ rotate together under a common Möbius transformation of the unit ball $B^d$. The **completely phase-synchronized state** is the diagonal manifold $\Delta \subset (S^{d-1})^N$ where all $x_i$ coincide. [[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]] §VIII proves a rare global-convergence result: for identical sphere oscillators with a first-order linear order parameter $Z = \sum_i a_i x_i$ having positive weights $0 < a_i < 1/2$ summing to 1, *almost all* trajectories converge to $\Delta$ as $t \to \infty$. The proof uses a **hyperbolic Lyapunov potential** $\Phi(w) = \sum_i a_i \log[(1 - |w|^2)/|w - p_i|^2]$ on the reduced state space $B^d$, exploiting the fact that $\Phi \to -\infty$ on the boundary $|w| \to 1$ and every interior fixed point of the gradient flow is repelling. This is the only known example in the wiki of a *global* phase-locking theorem for a Kuramoto-type model.
