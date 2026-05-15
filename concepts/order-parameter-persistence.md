---
type: concept
title: "Order Parameter Persistence"
created: 2026-05-08
updated: 2026-05-08
sources:
  - "[[dietert-fernandez-2018-asymptotic-stability]]"
  - "[[dietert-2016-stability-bifurcation]]"
  - "[[continuum-stability-debate]]"
tags:
  - dynamical-systems
  - synchronization
  - open-problem
  - stability
aliases:
  - r-stays-positive
  - persistence-of-order-parameter
  - hpersist
---

# Order Parameter Persistence

Order parameter persistence is the property that $r(t) \geq r_{\min} > 0$ for all $t \geq 0$ given $r(0) > 0$ and $K > K_c$ in the Ott-Antonsen reduced Kuramoto model.

## Precise statement

For the OA scalar system:
$$\dot{\alpha}(\omega,t) = -\gamma(\omega)\alpha(\omega,t) + \frac{K}{2}r(t)(1 - \alpha(\omega,t)^2)$$
$$r(t) = \int \alpha(\omega,t)\,g(\omega)\,d\omega$$

with $K > K_c$, $\gamma(\omega) > 0$, $\int (1/\gamma)\,g\,d\omega < \infty$, and $r(0) > 0$:

**Claim**: $\exists\, r_{\min} > 0$ such that $\forall\, t \geq 0$, $r(t) \geq r_{\min}$.

## Role in the Lean formalization

This is the hypothesis `hpersist` in `KuramotoData` (field: `liminf |r| > 0`). It is the SINGLE remaining unproved structural hypothesis in the machine-checked proof chain. Everything else (self-consistency decay, gap exclusion, Lipschitz trapping, global convergence) is derived from it.

In the continuum proof, persistence appears as `h_body_persist` — the assumption that $\alpha(\omega,t) \geq \delta > 0$ on the body $\{\gamma \leq M\}$. This is equivalent to $r(t) \geq r_{\min}$ because the body persistence follows from the per-$\omega$ ODE comparison principle once $r$ is bounded below.

## Known results

| Regime | Persistence | Method |
|---|---|---|
| Lorentzian $g$ | **PROVED** (0 sorry) | Bernoulli closed-form: $r(t) > 0$ explicit |
| Bounded $\gamma$ (finite system) | **PROVED** (0 sorry) | Per-$\omega$ comparison + full pair bound |
| General $g$, local perturbation | **Proved** (Dietert-Fernandez 2018, Prop 4.3) | Volterra + spectral gap |
| General $g$, global | **OPEN** | The gap |

## Why it's hard

1. **No closed-form ODE for r(t)** in general: $r'(t) = -\int \gamma\alpha\,g\,d\omega + (K/2)r(1 - \int \alpha^2 g\,d\omega)$ involves the full $\alpha$-field, not just $r$.

2. **Circular dependency**: The Lyapunov bound $|r(t) - r^*| \leq \sqrt{V(t)}$ gives $r(t) \geq r^* - \sqrt{V(0)}$, which is positive only if $V(0) < r^{*2}$. For general initial data, $V(0)$ may be large. The rate of $V$ decrease depends on body coercivity, which depends on persistence. Circular.

3. **Psi is not monotone on OA**: The Dietert energy $\Psi = -\int g\log(1-\alpha^2)\,d\omega$ satisfies $\Psi' = Kr^2 - 2\int g\gamma\alpha^2/(1-\alpha^2)\,d\omega$ on OA. Unlike the full PDE where $\Psi' = Kr^2$, on OA the damping term competes with the coupling gain.

4. **Instability escape is qualitative**: Chetaev's theorem shows trajectories leave a neighborhood of $\alpha = 0$, but doesn't give a UNIFORM lower bound on $r(t)$ for all future times. The trajectory could in principle revisit near 0 (though V-antitonicity makes this unlikely).

## Proof strategies (ranked by promise)

### Strategy A: V + Cauchy-Schwarz (partial, already formalized)

**Proved**: $V$ antitone implies $|r(t) - r^*| \leq \sqrt{V(t)} \leq \sqrt{V(0)}$.

If $V(0) < r^{*2}$: immediate $r(t) \geq r^* - \sqrt{V(0)} > 0$.

For general $V(0)$: need to show $V$ decreases below $r^{*2}$ before $r$ can hit 0. This requires a rate estimate that doesn't use persistence. See [[r-stays-positive-strategies]] Strategy 2.

### Strategy B: Psi + instability escape

On OA: $\Psi' = Kr^2 - 2\int g\gamma\alpha^2/(1-\alpha^2)\,d\omega$. Near $\alpha \approx 0$: dissipation $\approx 2\int g\gamma\alpha^2$ while gain $= K(\int g\alpha)^2$. For $K > K_c$, the gain dominates for the low-$\gamma$ oscillators, making $\Psi' > 0$ near incoherence.

Combined with $\Psi$ bounded above (since $\alpha \in (0,1)$): trajectory cannot stay near $\alpha = 0$ forever.

Remaining gap: translating "escapes neighborhood" into "never returns" (needs monotonicity or trapping argument).

### Strategy C: Body-comparison bootstrap

1. For body $\{\gamma \leq M\}$: per-$\omega$ ODE gives $\alpha(\omega,t) \geq \min(\alpha(\omega,0), \text{bodyEquil}(M,K,r_{\min}))$ whenever $r(t) \geq r_{\min}$.
2. $r(t) = r_{\text{body}}(t) + r_{\text{tail}}(t)$ with $r_{\text{body}} \geq \delta(M) \cdot \mu(\text{body})$ from step 1.
3. Choose $M$ large enough that $\delta(M) \cdot \mu(\text{body}) > r_{\min}$.
4. Self-consistent: if $r \geq r_{\min}$ then body gives $r \geq \delta \cdot \mu > r_{\min}$.

Gap: step 1 assumes $r \geq r_{\min}$ holds; this is circular unless bootstrapped.

### Strategy D: Passage to limit from n-pole

The finite-$N$ theorem proves $r_N(t) \to r^*$ with persistence. If $r_N \to r$ uniformly: persistence transfers. Gap: uniform-in-$t$ convergence bounds.

## Cross-links

- [[continuum-stability-debate]] — the main synthesis tracking the full proof
- [[body-lasalle-gap-analysis]] — body antitonicity depends on persistence
- [[subproblem-decomposition]] — persistence as a standalone subproblem
- [[r-stays-positive-strategies]] — detailed synthesis of all strategies
- [[kuramoto-stability-problem]] — the parent open problem
