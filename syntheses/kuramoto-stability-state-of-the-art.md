---
type: synthesis
title: "State of the Art: Global Stability of the Kuramoto PLS"
created: 2026-04-18
updated: 2026-04-25
sources:
  - "[[kuramoto-stability-problem]]"
  - "[[hyperbolic-lyapunov-attack-on-kuramoto-stability]]"
  - "[[chiba-2015-kuramoto-conjecture]]"
  - "[[fernandez-gerard-varet-giacomin-2016-landau-damping]]"
  - "[[dietert-fernandez-2018-asymptotic-stability]]"
  - "[[dietert-2016-stability-bifurcation]]"
  - "[[dietert-2017-pls-sobolev]]"
  - "[[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]]"
  - "[[chen-engelbrecht-mirollo-2017-hyperbolic-geometry]]"
  - "[[ott-antonsen-2008-low-dimensional]]"
  - "[[kuehn-landi-2025-oa-unstable-manifold]]"
  - "[[haraux-jendoubi-2015-convergence-problem]]"
  - "[[hanche-olsen-holden-2010-kolmogorov-riesz]]"
  - "[[bronski-wang-2020-partially-locked]]"
  - "[[morales-poyato-2019-trend-equilibrium]]"
  - "[[cestnik-martens-2024-riccati-array]]"
  - "[[dietert-2016-thesis]]"
tags: [dynamical-systems, synchronization, open-problem, pde, dimension-reduction]
aliases: ["Kuramoto stability state of the art", "PLS global stability survey"]
---

# State of the Art: Global Stability of the Kuramoto PLS

A cross-source synthesis of the current state of the 50-year-old problem of global nonlinear stability of the partially locked state (PLS) of the Kuramoto model, incorporating 20 ingested sources, 5 LEAN 4 files, and 16+ attempted proof approaches.

## The problem

For the continuum Kuramoto model with symmetric unimodal frequency distribution $g(\omega)$ and coupling $K > K_c = 2/(\pi g(0))$: does every trajectory with initial order parameter $r(0) \neq 0$ converge to the PLS? This is Assertion 3 of [[kuramoto-stability-problem]].

## What is proved

### From the literature (ingested and verified)

| Result | Source | Scope |
|---|---|---|
| Local stability of incoherence ($K < K_c$) | [[chiba-2015-kuramoto-conjecture]], [[fernandez-gerard-varet-giacomin-2016-landau-damping]] | Any analytic $g$ |
| Local stability of PLS ($K > K_c$) | [[dietert-2017-pls-sobolev]], [[dietert-fernandez-2018-asymptotic-stability]] | Sobolev or analytic $g$ |
| OA manifold exponentially attracting | [[dietert-fernandez-2018-asymptotic-stability]] Prop 4.1 | Analytic $g$ |
| OA manifold = unstable manifold of incoherence | [[kuehn-landi-2025-oa-unstable-manifold]] | Continuum limit |
| Global stability for identical oscillators | [[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]], [[chen-engelbrecht-mirollo-2017-hyperbolic-geometry]] | Hyperbolic gradient flow |
| Universal energy identity $\partial_t I_0 = K|\eta|^2$ | [[dietert-2016-stability-bifurcation]] §3 | Any $g$, full state space |

### From this project (new results, LEAN 4 verified)

| Result | LEAN 4 file | Sorry count |
|---|---|---|
| Cooperativity of $n$-pole OA ODE | `RationalOA.lean` | 0 |
| Boundary repelling (trapping region) | `RationalOA.lean`, `GlobalStability.lean` | 0 |
| Fixed point uniqueness bounds | `RationalOA.lean` | 0 |
| Almost-global stability for Lorentzian mixtures | `GlobalStability.lean` | 0 (3 axioms) |
| $\dot{\Psi} = K|r|^2 \geq 0$ (global monotone) | `GlobalMonotone.lean` | 0 |
| Rotation drops out of $d/dt|\alpha|^2$ | `GlobalMonotone.lean` | 0 |
| No periodic orbits ($g > 0$ a.e.) | `GlobalMonotone.lean` | 0 |
| Completing the square $-ax^2 + bx \leq b^2/(4a)$ | `WeightedEnergy.lean` | 0 |
| Near-onset scaling $(K-K_c) - C\sqrt{K-K_c} < 0$ | `WeightedEnergy.lean` | 0 |
| Lorentzian $\dot{V} < 0$ | `Lorentzian.lean` | 0 |
| Trapping region $R^*(\tau) = (\tau+\sqrt{\tau^2+K^2})/K$ | `WeightedEnergy.lean` | 0 |

### From this project (new results, on paper)

| Result | Scope | Label |
|---|---|---|
| Dichotomy: $r \to 0$ or $\Psi \to \infty$ | Any analytic $g$, $K > K_c$ | **proved** (Barbalat) |
| Strong-coupling convergence ($K > K_0$) | General analytic $g$ | **proved** (Volterra bootstrap) |
| Fundamental solution identity $|\Phi| = (1-|\alpha_t|^2)/(1-|\alpha_0|^2)$ | Any $g$ | **proved** (exact) |
| $B(t)$ bounded for locked and drifting oscillators | Away from boundary | **proved** |
| $B(t)$ diverges at locked/drifting boundary | At $\omega = K|r|$ | **proved** (saddle-node) |

## Structural insights discovered

### 1. Rotation cancellation (the unifying principle)

The rotation $-i\omega\alpha$ drops out of THREE separate computations:
- $d/dt|\alpha|^2 = K\text{Re}(\bar{r}\alpha)(1-|\alpha|^2)$ → gives $\dot{\Psi} = K|r|^2$
- $d/dt|\partial_\omega\alpha|^2 = 2\text{Im}(\bar{\beta}\alpha) - 2K\text{Re}(\bar{r}\alpha)|\beta|^2$ → gives slope energy dynamics
- $|\Phi(\omega,t)| = (1-|\alpha_t|^2)/(1-|\alpha_0|^2)$ → links fundamental solution to Psi

This is because rotation is a **hyperbolic isometry** of the unit disk ([[chen-engelbrecht-mirollo-2017-hyperbolic-geometry]]), preserving all modulus-based quantities.

### 2. The OA system is gradient-like

With Lyapunov function $-\Psi$: the OA flow decreases $-\Psi$ (equivalently, increases $\Psi$), with $(-\Psi)' = -K|r|^2 \leq 0$ and equality iff $r = 0$. This makes the OA system **gradient-like** in the sense of [[haraux-jendoubi-2015-convergence-problem]] Chapter 6.

### 3. The locked/drifting boundary singularity

The PLS has a structural singularity at $\omega = Kr^*$: locked oscillators ($|\alpha^*| = 1$) and drifting oscillators ($|\alpha^*| < 1$) meet at a saddle-node transition. This singularity causes:
- $|\partial_\omega\alpha^*|^2 \sim 1/|\omega - Kr^*|$ (non-integrable)
- Precompactness in $L^2(g)$ fails ([[hanche-olsen-holden-2010-kolmogorov-riesz]])
- Dietert's norms ([[dietert-2016-stability-bifurcation]] $\mathcal{Z}^a$) are designed to handle this singularity

### 4. The moment hierarchy doesn't close

For general $g$, $d/dt|r|^2$ depends on the frequency-weighted moment $q = \int\omega\alpha g$ and the second moment $s = \int\alpha^2 g$, which are NOT functions of $r$. The scalar $r(t)$ does not satisfy an autonomous ODE. This is the fundamental obstruction to proving $|r| \to r^*$ directly.

## What is NOT proved (the precise gap)

**Near-onset convergence** ($K_c < K < K_0$, general analytic $g$): the trajectory on the OA manifold has $\Psi \to \infty$ and no periodic orbits, but convergence to the PLS is not proved. The gap reduces to:

> Does every bounded orbit of the OA equation on $L^2(g;\mathbb{D})$ with $\Psi \to \infty$ converge to the PLS?

This is equivalent to any one of:
- **Precompactness** of the orbit in a topology where [[haraux-jendoubi-2015-convergence-problem|Haraux-Jendoubi]] applies (NOT $L^2(g)$ due to boundary singularity — possibly Dietert's $\mathcal{Z}^a$ norm)
- **Boundedness of the slope energy** $B(t) = \int|\partial_\omega\alpha|^2 g$ (fails due to boundary singularity — BUT may work in a weighted version that kills the singularity)
- **Direct convergence of $|r(t)|$** to $r^*$ (requires closing the moment hierarchy)

## 16 approaches tried and their outcomes

| # | Approach | Outcome |
|---|---|---|
| 1 | Pointwise hyperbolic Lyapunov kernels | Fails: rotation term even in $\omega$ |
| 2 | $\int g|\alpha-\alpha^*|^2$ as Lyapunov | Fails: wrong sign ($+K|r-r^*|^2$) |
| 3 | Omega-limit of $|r|$ | Inconclusive: oscillation consistent with $\Psi \to \infty$ |
| 4 | Self-consistent Riccati contraction | Bounded not convergent |
| 5 | Iterative Volterra bootstrap | **Works for $K > K_0$** |
| 6 | Bihari inequality for Volterra | Needs initial smallness |
| 7 | Combined $\Psi + E$ functional | No definite sign |
| 8 | Analyticity of $\alpha(\omega)$ | Circular |
| 9 | Time-averaging / Cesàro | Doesn't imply pointwise convergence |
| 10 | $\ddot{\Psi}$ analysis | Lipschitz allows oscillation |
| 11 | Semiconvexity $\ddot{\Psi} \geq -\kappa\dot{\Psi}$ | $\kappa$ too large near onset |
| 12 | Self-consistency feedback | Qualitative only |
| 13 | Weighted energy (Dietert adaptation) | Scaling correct but not rigorous |
| 14 | Montel compactness | Topology mismatch with stability norm |
| 15 | Fourier structure bridge (strip bound $M<1$) | Self-contradictory (PLS has $|\alpha^*|=1$) |
| 16 | $B(t)$ via fundamental solution | **Works away from boundary**, fails at saddle-node |
| 17 | $\mathcal{Z}^a$ precompactness (conditional) | **Conditional success** under Hypothesis (H) (Theorem 6.11) |
| 18 | Trapping region for complex-$\omega$ Riccati | Forward-invariant disk $R^*(\tau)$; PLS inside by Dietert Lemma 4.30 |
| 19 | $\eta \in L^2$ energy absorption | **Fails**: $\Psi_{PLS} = +\infty$ so $\eta \notin L^2$ when approaching PLS |
| 20 | Lyapunov with finite PLS value | **Fails**: $L^2$ distance has wrong-sign $+K\|r-r^*\|^2$; weighted versions can't kill it |
| 21 | Trapping region for initial data | **Fails**: $R^*(\tau) - 1 \sim \tau^2$ but analytic continuation grows linearly in $\tau$ |
| 22 | Rational approximation + cooperativity | Proved for each $n$-pole; gap = uniform entering time $T_n \leq T^*$ |
| 23 | Self-consistency rigidity | **Most promising**: $\Psi \to \infty$ forces locking → self-consistency pins $\|r\| \to r^*$ → full convergence |
| 24 | Generalized tail-body split | **NEW (2026-04-25)**: tail/Ψ → 0 for ALL $g \in L^1$ (not just exponential tail). Gives $r^* \in \Omega_r$ unconditionally |

## Most promising remaining direction

**Approach 19: $\eta \in L^2$ energy absorption — FAILS.**

The idea was to use $\dot{\Psi} = K|\eta|^2$ with $\Psi$ bounded above to get $\eta \in L^2(\mathbb{R}^+)$, then absorb the coupling term in Dietert's energy estimate. However, for the case of interest ($K > K_c$, trajectory approaching PLS):
- $\Psi_{PLS} = +\infty$ because $|\alpha^*| = 1$ for locked oscillators ($|\omega| \leq Kr^*$) gives $-\log(1-|\alpha^*|^2) = +\infty$
- $\Psi(t) \to +\infty$, so $\int_0^\infty |\eta|^2 dt = +\infty$, hence $\eta \notin L^2$
- The approach only works when $\Psi \to L < \infty$ (convergence to INCOHERENCE, $K < K_c$), already proved by Dietert

**The Haraux-Jendoubi framework also faces a topology mismatch**: $\Psi$ is a Lyapunov function for moving AWAY from incoherence (not toward PLS), and $\Psi_{PLS} = +\infty$ means the PLS is at "the boundary at infinity" of the phase space, not an interior equilibrium.

**Approach 17 ($\mathcal{Z}^a$ precompactness under Hypothesis (H))** remains the most promising conditional result. The trapping region from Approach 18 provides partial evidence for (H) but doesn't close the gap: general OA initial data can have $|\alpha(\omega-i\tau, 0)| > R^*(\tau)$ for the analytic continuation.

**Approach 22: Rational approximation + cooperativity — MOST PROMISING.**

For rational $g_n$ (sum of $n$ Lorentzians with poles $\omega_j = \sigma_j - i\gamma_j$, $\gamma_j > 0$), the OA system reduces to an $n$-dimensional cooperative ODE on $\mathbb{D}^n$ with built-in damping ($d/dt|\alpha_j|^2|_{|\alpha_j|=1} = -2\gamma_j < 0$). By Hirsch's theorem for cooperative semiflows:

- Almost every trajectory converges to PLS$_n$ (LEAN 4 proved for $n = 1$, extends to all $n$)
- Incoherence is the only other equilibrium, and it's unstable for $K > K_c(g_n)$

To extend to general analytic $g$: approximate $g$ by rational $g_n \to g$. The spectral gap of PLS$_n$ converges: $\lambda_n \to \lambda > 0$ (Dietert §5.6.1, $h_s'(0) \neq 0$ for even unimodal $g$). Passage to the limit $n \to \infty$ requires:

**Remaining gap** (label: open technical question): Uniform-in-$n$ bound on the entering time $T_n$ — the time it takes the cooperative flow to enter the local basin of PLS$_n$. This is a QUANTITATIVE question about cooperative ODE convergence rates, not a structural one. If $T_n \leq T^* < \infty$ uniformly: the double limit $(t \to \infty, n \to \infty)$ commutes, giving global stability for general analytic $g$.

This approach assembles existing proved components: cooperativity (LEAN 4), spectral gap (Dietert), rational approximation (standard). The gap is the smallest and most concrete of all 22 approaches tried.

**Why direct infinite-dimensional Hirsch doesn't work**: The continuum OA system on $L^2(g;\mathbb{D})$ fails two of Hirsch's conditions: (1) strong monotonicity fails at the boundary $|\alpha|=1$ (PLS has $|\alpha^*|=1$ for locked oscillators, violating interior-of-cone requirement), (2) precompact orbits not established (rapid $\omega$-oscillation prevents equicontinuity). The $n$-pole approximation bypasses both by working in finite-dimensional $\mathbb{D}^n$ with strictly repelling boundary ($\gamma_j > 0$).

**Status of the uniform entering-time bound**: Three-phase argument (linear instability growth → nonlinear monotone → local basin entry) gives a plausible bound $T_n \leq C/\lambda_u + C'/\lambda$, independent of $n$. Phases 1-2 have quantitative estimates. Phase 3 (Psi near Psi* implies alpha near alpha*) is not quantitatively controlled — Psi controls moduli but not phases, and making the cooperative phase control quantitative requires further work.

## Approach 24: Generalized tail-body split (2026-04-25)

**Replaces exponential-tail restriction with universal $L^1$ argument.**

The tail-body split (Approach 23's mechanism) previously required $g(\omega) = O(e^{-c|\omega|})$. The new argument:

1. $|d(\text{tail})/dt| \leq K|r| \cdot \varepsilon(M)$ where $\varepsilon(M) = \int_{|\omega|>M} g \to 0$
2. $d\Psi/dt = K|r|^2 \geq K\delta^2$ (progressive locking: $\liminf|r| \geq \delta > 0$)
3. Choose $M$: $\varepsilon(M)/\delta < 1/2$. Then tail grows at most half as fast as $\Psi$

Therefore body $= \Psi - \text{tail} \to +\infty$. Body divergence on compact $[-M,M]$ gives: $r^* \in \Omega_r$ via Fatou + self-consistency.

**LEAN status**: `GeneralizedTailBody.lean` (0 sorry) + `SelfConsistencyRigidity.lean` (0 sorry, 2 axioms).

**The precise remaining gap**: $r^* \in \Omega_r$ is proved, but $r(t) \to r^*$ requires the orbit to STAY near $r^*$ after visiting it. This reduces to SP-A5: once $r \approx r^*$, is the full profile $\alpha$ close to PLS in Dietert's $\mathcal{Z}^a$ norm? If yes: Dietert's local stability traps the orbit, giving convergence.

**Why SP-A5 might now be closable**: the body divergence gives not just $r \approx r^*$ but also $|\alpha(\omega,t)| \approx 1$ on a growing set of locked $\omega$'s. These locked oscillators have correct phases (Adler equation). So the full profile is close to PLS in $L^2(g)$. For analytic $g$: $L^2(g)$ closeness + analyticity of $\alpha(\omega,t)$ in $\omega$ should give $\mathcal{Z}^a$ closeness (Cauchy integral estimates). The gap is making the strip-width bound uniform in $t$.

## Cross-links

- [[kuramoto-stability-problem]] — the entity page tracking the problem status
- [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] — the detailed working synthesis with all proof attempts
- [[ott-antonsen-ansatz]] — the invariant manifold on which the dynamics live
