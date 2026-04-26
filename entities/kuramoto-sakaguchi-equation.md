---
type: entity
title: "Kuramoto–Sakaguchi Equation"
created: 2026-04-14
updated: 2026-04-14
sources:
  - "[[ha-ko-park-zhang-2016-collective-synchronization]]"
  - "[[strogatz-2000-from-kuramoto-to-crawford]]"
tags: [dynamical-systems, synchronization, kinetic-theory, pde, statistical-physics]
aliases: ["Kuramoto-Sakaguchi equation", "K-S equation", "kinetic Kuramoto equation", "Kuramoto-Sakaguchi Fokker-Planck equation"]
year_stated: 1988
---

# Kuramoto–Sakaguchi Equation

The Kuramoto–Sakaguchi equation is the nonlinear integro-differential PDE obtained as the mean-field / kinetic limit $N \to \infty$ of the [[kuramoto-model|Kuramoto model]], introduced by Hidetsugu Sakaguchi in 1988 in its Fokker–Planck (noisy) form and now understood to be the canonical infinite-dimensional target of the finite-$N$ Kuramoto system.

## The equation

Let $f(\theta, \Omega, t)$ be the density of oscillators with phase $\theta \in \mathbb{T} := \mathbb{R}/2\pi\mathbb{Z}$ and native frequency $\Omega \in \mathbb{R}$ at time $t$. The Kuramoto–Sakaguchi (K-S) equation is

$$
\partial_t f + \partial_\theta(\omega[f]\, f) \;=\; 0, \qquad (\theta, \Omega) \in \mathbb{T} \times \mathbb{R},\ t > 0,
$$

with the velocity field

$$
\omega[f](\theta, \Omega, t) \;=\; \Omega - K\, L[f](\theta, t), \qquad L[f](\theta, t) \;:=\; \int_{\mathbb{T}}\sin(\theta - \theta_*)\,\rho(\theta_*, t)\,d\theta_*,
$$

and the local phase density

$$\rho(\theta, t) \;:=\; \int_{\mathbb{R}}f(\theta, \Omega, t)\, d\Omega.$$

The initial data satisfies $\int_{\mathbb{T}}f^0(\theta, \Omega)\,d\theta = g(\Omega)$ for a prescribed native-frequency distribution $g$, and $\iint f^0\,d\Omega\,d\theta = 1$. The nonlinear-mean-field velocity $\omega[f]$ collapses the pair-wise Kuramoto interaction into a self-consistent force that every oscillator experiences, in the spirit of the [[kinetic-formulation]].

See [[ha-ko-park-zhang-2016-collective-synchronization]] §4.5 for the detailed derivation and well-posedness theory. The noisy version adds a diffusive term $D\,\partial_\theta^2 f$ (Sakaguchi's original 1988 form) and is called the **Kuramoto–Sakaguchi–Fokker–Planck equation**.

## Relation to the Kuramoto model

The K-S equation is the exact mean-field limit of the finite-$N$ [[kuramoto-model]] as $N \to \infty$. Two concrete links:

1. **Empirical measure.** If $(\theta_i(t), \Omega_i)$ solves the $N$-oscillator Kuramoto ODE system, the empirical measure $\mu_t = N^{-1}\sum_{i=1}^{N}\delta_{(\theta_i(t), \Omega_i)}$ is a measure-valued solution of the K-S equation. This is a distributional statement and does not by itself give propagation of chaos.
2. **Self-consistency rewriting.** The Kuramoto model can be rewritten in terms of the complex mean field $re^{i\psi} = N^{-1}\sum_j e^{i\theta_j}$ as $\dot{\theta}_i = \Omega_i + Kr\sin(\psi - \theta_i)$. The K-S equation is the continuum version in which $re^{i\psi}$ is replaced by $\iint e^{i\theta}f\,d\theta\,d\Omega$ and the ODE becomes a transport equation. This is the language of the Strogatz–Mirollo 1991 paper summarised in [[strogatz-2000-from-kuramoto-to-crawford]].

The [[kinetic-formulation]] concept page discusses the general pattern (density plus continuity equation plus self-consistent mean field); this page is about the specific named instance that the Kuramoto literature calls the K-S equation.

## Stationary states

Steady states of the K-S equation satisfy $\partial_\theta(\omega[f] f) = 0$, hence $\omega[f]\cdot f \equiv C(\Omega)$ for a function $C$ depending only on the native frequency. Two cases:

- **Incoherent state.** $f_0(\theta, \Omega) = g(\Omega)/(2\pi)$, uniform in $\theta$. This is the "disordered phase" of the Kuramoto transition.
- **Partially-synchronized state.** $f$ is a delta in $\theta$ at a locked phase for $|\Omega| \leq Kr$ (the "locked" sub-population) plus $C(\Omega)/|\omega[f](\theta, \Omega)|$ for $|\Omega| > Kr$ (the "drifting" sub-population). This is Kuramoto's 1975 steady-state ansatz, now rigorously a fixed point of a PDE.

The critical coupling $K_c = 2/(\pi g(0))$ at which a continuous family of partially-synchronized states bifurcates from incoherence is the same threshold Kuramoto derived — see [[kuramoto-model]].

## Well-posedness

[[ha-ko-park-zhang-2016-collective-synchronization]] surveys four notions of solution for the K-S equation (Definition 4.2):

| Class | Reference | Form |
|---|---|---|
| Classical $C^1$ solution | Standard | Strong $C^1$ regularity in $(\theta, t)$ |
| Measure-valued solution | Carrillo–Choi–Ha–Kang–Kim (2014), Lancellotti (2005), Cañizo–Carrillo–Rosado (2011) | Weakly continuous $\mu \in L^\infty([0, T]; \mathcal{M}(\mathbb{T} \times \mathbb{R}))$ satisfying the weak form |
| $L^\infty$-weak solution | Amadori–Ha–Park | Distributional weak solution in $L^\infty$ |
| Entropy / BV weak solution | Amadori–Ha–Park | Uses entropy-condition / BV framework inherited from hyperbolic conservation laws with nonlocal flux |

**Theorem 4.6** (Amadori–Ha–Park). For the identical-oscillator case $g = \delta_0$, the K-S equation reduces to the scalar conservation law $\partial_t\rho + K\partial_\theta(L[\rho]\rho) = 0$. For initial data $\rho_0 \in BV(\mathbb{T})$, there exists an entropy weak solution $\rho(\cdot, t) \in BV(\mathbb{T})$, unique in this class, and the $L^1$-stability estimate

$$||\rho_1(\cdot, t) - \rho_2(\cdot, t)||_{L^1} \;\leq\; e^{Ct}||\rho_{0,1} - \rho_{0,2}||_{L^1}$$

holds. The proof uses wave-front tracking / characteristic methods adapted to the nonlocal flux $L[\rho]$. For non-identical oscillators the corresponding theory is incomplete as of 2016.

## Nonlinear Landau damping

The **Kuramoto conjecture** from §5 of [[kuramoto-1975-self-entrainment]] asserted that below the critical coupling strength the incoherent solution should be **nonlinearly** stable — not merely Landau-damped at the linearised level. The post-2000 literature has settled this:

- **Chiba (2015)** "A proof of the Kuramoto conjecture for a bifurcation structure of the infinite-dimensional Kuramoto model" (*Ergodic Theory and Dynamical Systems* 35, 762–834) — establishes the bifurcation structure rigorously.
- **Fernandez–Gérard-Varet–Giacomin (2016)** "Landau damping in the Kuramoto model" (*Annales Henri Poincaré* 17, 1793–1823) — rigorous nonlinear Landau damping for the K-S equation.
- **Ha–Xiao (2015)**, **Benedetto–Caglioti–Montemagno (2015)** — nonlinear stability / instability refinements.

[[ha-ko-park-zhang-2016-collective-synchronization]] §4.5 summarises: "Kuramoto conjecture that below the critical coupling strength the incoherent solution is expected to be nonlinearly stable, in contrast above the critical coupling strength, it is expected to be nonlinearly unstable. The verification of this nonlinear phenomena rigorously has been done in aforementioned literature." This is the direct resolution of the question flagged as open in [[strogatz-2000-from-kuramoto-to-crawford]]. The [[kuramoto-stability-problem]] entity records the details of what is now resolved and what remains.

## Relation to plasma physics

The K-S equation is structurally a Vlasov-type equation: a continuity equation for a density on a phase space with a self-consistent mean-field velocity. This is the same formal structure as the Vlasov–Poisson system of collisionless plasma physics, and the analogy is not superficial — the Landau-damping phenomenon is common to both, and the analytical tools used to prove it (analytic continuation, resolvent / Laplace-transform methods) cross-apply. See [[landau-damping]] for the detailed explanation and history, and [[strogatz-2000-from-kuramoto-to-crawford]] for the narrative of how the analogy was recognised.

## Open questions (as of 2016)

- **BV theory for non-identical oscillators.** The Amadori–Ha–Park BV well-posedness theory is complete for identical oscillators (Dirac $g$) but not yet for general smooth $g$. This is a PDE-technical question that parallels the finite-$N$ open question of propagation of chaos.
- **Finite-$N$ convergence.** How finite-$N$ Kuramoto trajectories approximate K-S solutions is part of [[kuramoto-finite-n-convergence]] — still open in the quantitative / rigorous-propagation-of-chaos sense.
- **Global nonlinear stability of partially-synchronized states.** See [[kuramoto-stability-problem]].
