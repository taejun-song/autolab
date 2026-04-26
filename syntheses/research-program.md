---
type: synthesis
title: "Research Program: Systematic Attack on the Kuramoto Global Stability Problem"
created: 2026-04-19
updated: 2026-04-19

sources:
  - "[[kuramoto-stability-problem]]"
  - "[[subproblem-decomposition]]"
  - "[[cooperative-oa-global-stability]]"
  - "[[dietert-2016-thesis]]"
  - "[[mouhot-villani-2011-landau-damping]]"
  - "[[carrillo-2013-wasserstein-kuramoto]]"
  - "[[iacobelli-2021-kinetic-wasserstein]]"
tags: [open-problem, research-plan, dynamical-systems, synchronization]
aliases: ["Kuramoto research program", "systematic attack plan"]
---

# Research Program: Systematic Attack on the Kuramoto Global Stability Problem

A concrete sequence of progressively harder problems. Each level builds on the previous. The final level IS the open problem.

## The method: progressive generalization

Instead of attacking the full problem directly, prove it for progressively harder cases. At each level, identify what NEW technique is needed beyond the previous level.

## Level 0: Proved (LEAN 4, 0 sorry)

**Single Lorentzian** ($n=1$, $g(\omega) = \gamma/[\pi(\omega^2+\gamma^2)]$).

OA reduces to scalar ODE $\dot{r} = (K/2-\gamma)r - (K/2)r^3$. Perfect-square Lyapunov gives explicit exponential convergence.

**Technique**: Scalar ODE analysis. No cooperation, no Hirsch, no axioms.

**LEAN**: `Lorentzian.lean` — `lorentzian_lyapunov_identity`, 0 sorry.

## Level 1: Prove for $n = 2$ (bi-Lorentzian)

**Target**: $g = c_1 L(\gamma_1) + c_2 L(\gamma_2)$ with $\gamma_1 \neq \gamma_2$.

OA reduces to 2D ODE on $(0,1)^2$. This is the SIMPLEST case where the moment hierarchy doesn't close ($r = c_1\alpha_1 + c_2\alpha_2$ is not a function of $r$ alone).

**Why it's tractable**: In 2D, the Poincaré-Bendixson theorem applies. Combined with:
- Compact invariant region $[0,1]^2$ (boundary repelling — LEAN proved)
- No periodic orbits (from $\dot\Psi \geq 0$ — LEAN proved)
- Two equilibria: 0 (unstable) and $\alpha^*$ (stable)

$\Rightarrow$ Every trajectory not converging to 0 converges to $\alpha^*$.

**New technique needed**: 2D Poincaré-Bendixson theorem (NOT Hirsch, NOT Kamke — just topology of 2D flows).

**LEAN formalization**: State Poincaré-Bendixson as axiom. Prove convergence for $n=2$.

**Concrete steps**:
1. State 2D Poincaré-Bendixson as axiom in LEAN
2. Prove: compact invariant + no periodic orbits + 2 equilibria → each trajectory converges to one
3. Prove: trajectories starting with $r(0) > 0$ cannot converge to 0 (using $\Psi$ monotone + instability)
4. Conclude: convergence to PLS

**Difficulty**: Low-medium. All ingredients exist; need to assemble.

## Level 2: Prove for general $n$-pole

**Target**: $g_n = \sum_{k=1}^n c_k L(\gamma_k)$ for arbitrary $n$.

**Why it's harder than Level 1**: Poincaré-Bendixson fails for $n \geq 3$. Need cooperative systems theory.

**What we have**: Cooperativity (LEAN proved), boundary repelling (LEAN proved), no periodic orbits (LEAN proved), 2 equilibria (LEAN proved).

**New technique needed**: ONE of:
- (a) Hirsch's theorem for cooperative systems (current axiom)
- (b) Kamke comparison + monotone bounded convergence (NPoleConvergence.lean axioms)
- (c) A direct Lyapunov argument for the $n$-pole system

**Option (c) research question**: Can the perfect-square Lyapunov from Level 0 be generalized to a multi-dimensional version?

For $n=1$: $W = (r^2 - r^{*2})^2$, $\dot{W} = -2Kr^2 W$.

For general $n$: define $W_k = (\alpha_k^2 - \alpha_k^{*2})^2$ and $W = \sum c_k W_k$. Compute $\dot{W}$. The coupling through $r = \sum c_j\alpha_j$ creates cross-terms. **Can these cross-terms be controlled?**

This is a CONCRETE COMPUTATION. If $\dot{W} \leq -\lambda W + C|r - r^*|^2$ with $|r-r^*|^2 \leq W$ (from Cauchy-Schwarz): then $\dot{W} \leq (-\lambda + C)W$. If $\lambda > C$: exponential decay. The question: for which $(K, g_n)$ is $\lambda > C$?

**Concrete steps**:
1. Compute $\dot{W}$ for the $n$-pole system (algebra, checkable in LEAN)
2. Identify the cross-terms and bound them
3. Find conditions on $K, \gamma_k, c_k$ under which $\dot{W} \leq -\mu W$
4. If the conditions hold for all $n$ with $g_n \to g$: Level 3 follows

**Difficulty**: Medium. The computation is concrete; success depends on whether the cross-terms cooperate.

## Level 3: Passage to limit $n \to \infty$

**Target**: From $n$-pole convergence to continuum convergence.

**Core obstacle**: Semigroup constant $C_n \to \infty$ as $\gamma_{\min} \to 0$, and $\Psi_n^* \to \infty$.

**What would bypass the obstacle**: A convergence metric/Lyapunov function that:
- Is finite at the continuum PLS (unlike $\Psi$)
- Gives exponential decay with rate independent of $n$

**Research question 3a**: Does the multi-dimensional Lyapunov $W$ from Level 2 have a well-defined continuum limit $W_\infty = \int g(\omega)(\alpha(\omega)^2 - \alpha^*(\omega)^2)^2 d\omega$?

If so: $\dot{W}_\infty \leq -\mu W_\infty$ would give convergence directly, without passage to limit!

**Critical check**: Is $W_\infty$ finite at the PLS? At the PLS: $\alpha^*(\omega)^2 = \beta(\omega/(Kr^*))^2$. For locked oscillators ($|\omega| \leq Kr^*$): $|\alpha^*|^2 = 1$. For any trajectory: $|\alpha(\omega)|^2 < 1$. So $W_\infty = \int g (|\alpha|^2 - |\alpha^*|^2)^2 d\omega$. For locked $\omega$: the integrand is $(|\alpha|^2 - 1)^2 = (1-|\alpha|^2)^2 \leq 1$. So $W_\infty \leq \int g \cdot 1 = 1$.

**$W_\infty$ IS FINITE AT PLS!** (Unlike $\Psi$ which is $+\infty$.)

This is a potential breakthrough: $W_\infty = \int g(|\alpha|^2 - |\alpha^*|^2)^2 d\omega$ is finite everywhere, including at PLS.

**Research question 3b**: Is $\dot{W}_\infty \leq 0$ along the OA flow?

Computing:
$$\frac{d}{dt}\int g(|\alpha|^2 - |\alpha^*|^2)^2 d\omega = 2\int g(|\alpha|^2 - |\alpha^*|^2) \frac{d}{dt}|\alpha|^2 d\omega$$

Using $\frac{d}{dt}|\alpha|^2 = K\operatorname{Re}(\bar{r}\alpha)(1-|\alpha|^2)$:

$$= 2K\int g(|\alpha|^2 - |\alpha^*|^2)\operatorname{Re}(\bar{r}\alpha)(1-|\alpha|^2) d\omega$$

The sign of this depends on whether $(|\alpha|^2 - |\alpha^*|^2)$ and $\operatorname{Re}(\bar{r}\alpha)(1-|\alpha|^2)$ are correlated. This is NOT obviously negative.

**However**: if $|\alpha| < |\alpha^*|$ (below PLS) and $\operatorname{Re}(\bar{r}\alpha) > 0$ (aligned with order parameter): then $(|\alpha|^2 - |\alpha^*|^2) < 0$ and $\operatorname{Re}(\bar{r}\alpha)(1-|\alpha|^2) > 0$, giving a negative contribution. Conversely, if $|\alpha| > |\alpha^*|$ (impossible on real axis since $|\alpha| < 1 = |\alpha^*|$ for locked): this case doesn't arise.

**For locked oscillators** ($|\omega| \leq Kr^*$, $|\alpha^*| = 1$): $|\alpha|^2 - 1 < 0$ and $\operatorname{Re}(\bar{r}\alpha)(1-|\alpha|^2) > 0$ when phases are aligned. Product is negative. ✓

**For drifting oscillators** ($|\omega| > Kr^*$, $|\alpha^*| < 1$): the sign depends on whether $|\alpha| > |\alpha^*|$ or $|\alpha| < |\alpha^*|$. The dynamics pushes $|\alpha|$ toward $|\alpha^*|$ (by the stability of the PLS), so the product should be negative on average.

**This is the most promising concrete computation to try.** If $\dot{W}_\infty \leq 0$ can be proved (or $\leq -\mu W_\infty$ with corrections): it would give global convergence directly.

## Level 4: The full theorem

Combine Levels 0-3 to prove: for symmetric unimodal analytic $g$ and $K > K_c$, almost every trajectory on the OA manifold converges to the PLS.

## Summary: the research program

| Level | Target | New technique | Difficulty | Status |
|-------|--------|---------------|------------|--------|
| 0 | $n=1$ (Lorentzian) | Scalar Lyapunov | — | **DONE** (LEAN) |
| 1 | $n=2$ (bi-Lorentzian) | 2D Poincaré-Bendixson | Low-medium | Provable |
| 2 | General $n$-pole | Multi-dim Lyapunov OR Hirsch | Medium | Key computation |
| 3 | Continuum limit | $W_\infty = \int g(\|\alpha\|^2 - \|\alpha^*\|^2)^2$ as Lyapunov? | Medium-hard | **Most promising** |
| 4 | Full theorem | Assembly | Low (given L0-L3) | — |

**The critical research question** (Level 3): Is $W_\infty = \int g(|\alpha|^2 - |\alpha^*|^2)^2 d\omega$ a Lyapunov function for the OA flow? It IS finite at PLS (unlike $\Psi$). If $\dot{W}_\infty \leq 0$: this solves the problem.

## Perron convergence insight (2026-04-19)

**Level 2 update**: The semigroup constant blowup $C_n \to \infty$ that blocked Path B is an ARTIFACT. On the positive cone (monotone trajectories from Kamke), Perron-Frobenius gives $C = 1$. The effective convergence rate at PLS is $Kr^*$ (not $\gamma_{\min}$), proved in LEAN 4 (0 sorry) via AM-GM: $(1+x^2)/(2x) \geq 1$.

This means Level 2 → Level 3 passage may work WITHOUT solving the $W_\infty$ question: if $T_n \leq T^*$ (uniform convergence time) can be proved, the $\epsilon/3$ argument (SP-B3, already proved) gives the continuum result directly.

**LEAN**: `PerronConvergence.lean` — `jacobian_diagonal_bound`, `jacobian_diagonal_rate`, `uniform_convergence_time`. 0 sorry, 1 axiom (Perron-Frobenius).

**Remaining gap**: Perron eigenvector condition number $\kappa_n$ — does it stay bounded as $n \to \infty$? The scalar order parameter $r = \sum c_k \alpha_k$ averages over these weights, so the passage to limit for $r$ may work even if $\kappa_n \to \infty$.
