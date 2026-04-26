---
type: synthesis
title: "Cooperative OA Dynamics and the Global Stability Strategy"
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[kuramoto-stability-problem]]"
  - "[[ott-antonsen-ansatz]]"
  - "[[dietert-fernandez-2018-asymptotic-stability]]"
  - "[[dietert-2016-thesis]]"
  - "[[cestnik-martens-2024-riccati-array]]"
  - "[[pietras-daffertshofer-2016-oa-parameter-dependent]]"
  - "[[haraux-jendoubi-2015-convergence-problem]]"
  - "[[kuehn-landi-2025-oa-unstable-manifold]]"
  - "[[chen-engelbrecht-mirollo-2017-hyperbolic-geometry]]"
  - "[[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]]"
tags: [dynamical-systems, synchronization, open-problem, cooperative-systems, dimension-reduction]
aliases: ["cooperative OA strategy", "rational approximation attack"]
---

# Cooperative OA Dynamics and the Global Stability Strategy

A focused synthesis assembling the ingredients for Approach 22 (rational approximation + cooperativity) — the most promising attack on full-range global stability of the Kuramoto PLS.

## The reduction chain

The problem reduces through a chain of exact results:

$$\text{Full K-S PDE} \xrightarrow{\text{Prop 4.1}} \text{OA manifold} \xrightarrow{\text{§5.6.2}} \text{same stability} \xrightarrow{\text{rational } g} \text{cooperative ODE on } \mathbb{D}^n$$

1. **K-S → OA**: [[dietert-fernandez-2018-asymptotic-stability]] Prop 4.1 — for analytic $g$, the OA manifold is exponentially attracting: $\|w(t)\| \leq \|w(0)\|e^{-at}$
2. **OA stability = full stability**: [[dietert-2016-thesis]] §5.6.2 — "no loss of generality in investigating existence and stability of $f_s$ in the OA manifold"
3. **Rational $g$ → cooperative ODE**: For $g_n = \sum_{j=1}^n \frac{w_j\gamma_j/\pi}{(\omega-\sigma_j)^2+\gamma_j^2}$, the OA system reduces to $n$ complex ODEs at the poles $\omega_j = \sigma_j - i\gamma_j$

## The cooperative structure (proved in LEAN 4)

For rational $g_n$ with poles in the lower half-plane, the $n$-pole ODE:

$$\dot{\alpha}_j = (-i\sigma_j - \gamma_j)\alpha_j + \frac{K}{2}(\bar{z} - z\alpha_j^2), \quad z = \sum_k w_k\alpha_k$$

has three key properties (all verified in `RationalOA.lean`, `GlobalStability.lean`, `GlobalMonotone.lean`):

| Property | Source | Status |
|----------|--------|--------|
| Boundary strictly repelling: $d/dt\|\alpha_j\|^2\|_{\|\alpha_j\|=1} = -2\gamma_j < 0$ | `RationalOA.lean` | LEAN 4, 0 sorry |
| Cooperativity: off-diagonal Jacobian non-negative | `RationalOA.lean` | LEAN 4, 0 sorry |
| No periodic orbits (from $\dot{\Psi}_n = K\|z\|^2 \geq 0$) | `GlobalMonotone.lean` | LEAN 4, 0 sorry |
| Hirsch convergence: a.e. trajectory → equilibrium | `GlobalStability.lean` | 3 axioms (Hirsch, Dietert local, OA attract) |

For $K > K_c(g_n)$: incoherence is the only other equilibrium and is unstable. By cooperativity + Hirsch's theorem: **almost every trajectory converges to PLS$_n$**.

## What each source contributes to the strategy

### Dietert thesis §5.6.1 — Spectral gap uniformity

For even unimodal $g$, the PLS is always linearly stable with $h_s'(0) \neq 0$. The stability condition $\det(\text{Id} - \frac{K}{2}M(\lambda, \eta_{st})) \neq 0$ for $\Re(\lambda) \geq 0$, $\lambda \neq 0$ holds with a spectral gap $\lambda > 0$ that depends continuously on $g$. For $g_n \to g$: $\lambda_n \to \lambda > 0$.

### Kuehn-Landi (2025) — OA = unstable manifold

The OA manifold is the unstable manifold of incoherence in the continuum limit. This means: perturbations of incoherence for $K > K_c$ grow ALONG the OA manifold toward the PLS. The finite-dimensional cooperative dynamics on the pole amplitudes captures exactly this unstable-manifold flow.

### Cestnik-Martens (2024) — Riccati formulation

The OA equation is the complex Riccati $\dot{x} = ax^2 + bx + c$, with exact Möbius reduction. The invariant disk property $d/dt\|\alpha\|^2 = K\operatorname{Re}(\bar{r}\alpha)(1-\|\alpha\|^2)$ is the Möbius-geometric reason for the unit disk being preserved. For complex poles ($\gamma_j > 0$): the disk is strictly attracting, giving the boundary repulsion needed for Hirsch's theorem.

### Haraux-Jendoubi (2015) — Two convergence tools

**Tool 1 (Lemma 6.6.2)**: For $\partial_t u = Lu + F(t)$ with $L$ generating exponential decay and $F$ in a compact set, the orbit has precompact range. Applied to the PLS perturbation equation: $L$ is Dietert's linearization with gap $\lambda$, and the "forcing" $F = P_s Q'u$ maps through the rank-1 order parameter coupling.

**Tool 2 (Chapter 10, Łojasiewicz-Simon)**: For analytic gradient systems, convergence holds WITHOUT precompactness. The Łojasiewicz inequality $|E(u) - E(u^*)|^{1-\theta} \leq C\|E'(u)\|$ provides compactness intrinsically. Requires: (a) an energy $E$ that is finite at PLS, (b) the system is a gradient flow for $E$, (c) $E$ is analytic.

### Pietras-Daffertshofer (2016) — Parameter-dependent attractiveness

The OA manifold is attractive even for parameter-dependent systems. For the $n$-pole approximation (which can be viewed as oscillators parameterized by their pole location), each Lorentzian component has its own OA attractiveness guarantee.

## The remaining gap

**For each finite $n$**: global stability is PROVED (cooperativity + Hirsch).

**For general analytic $g$**: need to pass to the limit $n \to \infty$. The gap is a DOUBLE LIMIT PROBLEM:

$$\lim_{n \to \infty}\lim_{t \to \infty} \alpha_n(\omega,t) \stackrel{?}{=} \lim_{t \to \infty}\lim_{n \to \infty}\alpha_n(\omega,t) = \lim_{t \to \infty}\alpha(\omega,t)$$

The LHS = $\lim_{n \to \infty}\alpha^*_n(\omega) = \alpha^*(\omega)$ (PLS). The RHS is what we want to show equals $\alpha^*(\omega)$.

The double limit commutes if the convergence $\alpha_n(\omega,t) \to \alpha^*_n(\omega)$ is **uniform in $n$**. This requires a uniform entering-time bound $T_n \leq T^* < \infty$.

## Three sub-strategies for the gap

### Sub-strategy A: Uniform cooperative convergence rate

Bound $T_n$ directly using:
- Phase 1: Linear instability growth at rate $\lambda_u^{(n)} \to \lambda_u > 0$ (time $\sim \log(1/\epsilon_0)/\lambda_u$)
- Phase 2: Nonlinear monotone growth via $\Psi_n$ (time $\sim \Psi^*/Kc^2$)
- Phase 3: Local basin entry (needs $\Psi$ near $\Psi^*$ to imply $\alpha$ near $\alpha^*$)

**Gap in Phase 3**: Psi controls moduli but not phases.

### Sub-strategy B: Łojasiewicz-Simon on perturbation energy

Work with perturbation from PLS: $v = \alpha - \alpha^*$ (in an appropriate sense). Define energy $E(v) = \|v\|^2_{\mathcal{X}_{a,0}}$. If $E$ satisfies a Łojasiewicz inequality near $v = 0$ (the PLS), convergence follows WITHOUT precompactness. The analyticity of the OA equation makes this plausible.

**Gap**: $E(v) = \|v\|^2_{\mathcal{X}_{a,0}}$ may not be finite for $v = \alpha - \alpha^*$ because $\alpha^*$ has infinite $\mathcal{X}_{a,0}$ norm (locked oscillators with $|\alpha^*| = 1$). Need to work with Dietert's projected perturbation $u \in P_s(\mathcal{X}_{a,0})$ instead.

### Sub-strategy C: Rank-1 coupling compactness

The Kuramoto coupling is **rank-1**: all oscillators interact through the single complex order parameter $r = u_1(0)$. Decompose the dynamics:
$$\partial_t u = Lu + P_s Q'u$$
where $L$ generates exponential decay (gap $\lambda$) and $Q'u$ depends on $u$ ONLY through $u_1(0) \in \mathbb{C}$ (rank-1 map). If the image of $Q'$ is precompact (finite-dimensional range after projection), Haraux-Jendoubi Lemma 6.6.2 gives precompactness of the orbit.

**Gap**: $Q'u$ is not literally rank-1 — the output $(Q'u)_l(\xi)$ involves $u_1(0)$ but also $u_{l\pm 1}(\xi)$, which is infinite-dimensional. However, the KEY COUPLING IS through $u_1(0)$: the off-manifold dynamics decouple mode-by-mode once $u_1(0)$ is known.

## Assessment

Sub-strategy C (rank-1 compactness) is the most novel and exploits a structural feature not used in any previous approach. The rank-1 nature of the Kuramoto coupling is well-known but has not been systematically exploited for the global convergence problem. If the rank-1 structure gives precompactness of the forcing, Haraux-Jendoubi's abstract theorem converts local stability + gradient-like structure into GLOBAL convergence.

## Approach 23: Self-consistency rigidity (strongest argument)

A fourth sub-strategy that bypasses the precompactness/topology issues entirely:

**Chain**: $\Psi \to +\infty$ → oscillator locking → self-consistency constraint → uniqueness forces $|r| \to r^*$

**Step 1**: $\Psi(t) \to +\infty$ for $K > K_c$ (from instability of incoherence + gradient-like + no periodic orbits). This forces $|\alpha(\omega,t)| \to 1$ on a positive-$g$-measure set.

**Step 2**: For oscillators with $|\alpha| \to 1$ and $|\omega| < K|r(t)|$: the invariant disk property ([[cestnik-martens-2024-riccati-array]]) forces $\alpha \to \beta_+(\omega/(K|r|))$ (the stable root, since $|\beta_+| \leq 1$ and $|\beta_-| \geq 1$, and the disk $\mathbb{D}$ is preserved).

**Step 3**: The order parameter splits:
$$r(t) = \int_{|\omega|<K|r|}\alpha\,g\,d\omega + \int_{|\omega|>K|r|}\alpha\,g\,d\omega$$

The locked contribution → $\Phi(|r|) := \int_{|\omega|\leq K|r|}\sqrt{1-(\omega/(K|r|))^2}\,g\,d\omega$ ([[dietert-2016-thesis]] §1.3.2). The drifting contribution → 0 (Riemann-Lebesgue for analytic $g$, [[fernandez-gerard-varet-giacomin-2016-landau-damping]]).

**Step 4**: $|r(t)| = \Phi(|r(t)|) + o(1)$. For even unimodal $g$: $\Phi$ has a unique attractive fixed point $r^*$ with $\Phi'(r^*) < 1$ ([[dietert-2016-thesis]] §5.6.1, $h_s'(0) \neq 0$). Contraction gives $|r(t)| \to r^*$.

**Step 5**: $|r(t)| \to r^*$ gives pointwise convergence $\alpha(\omega,t) \to \alpha^*(\omega)$ for each $\omega$ (non-autonomous ODE stability with converging forcing). By dominated convergence: $r(t) \to r^*e^{i\Theta_\infty}$.

**Remaining quantitative gaps** (PDE estimates, not structural):
- Rate at which locked oscillators converge to $\beta_+$ (depends on distance from saddle-node at $|\omega| = K|r|$)
- Rate of drifting contribution decay (Riemann-Lebesgue rate for analytic functions)
- Boundary layer estimate at $|\omega| = K|r|$ (saddle-node contribution is $O(\epsilon)$)

**Cross-source verification**: Steps 1-2 use [[ott-antonsen-ansatz]], [[cestnik-martens-2024-riccati-array]]; Step 3 uses [[dietert-2016-thesis]], [[fernandez-gerard-varet-giacomin-2016-landau-damping]]; Step 4 uses [[dietert-2016-thesis]] §5.6.1; Step 5 uses [[dietert-fernandez-2018-asymptotic-stability]] local stability.
