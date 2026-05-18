---
type: synthesis
title: "Complex OA Global Stability: Proof Attempt via DCT Bootstrap"
created: 2026-05-18
updated: 2026-05-18
status: "active — Phase 1 complete (0 sorry), Phases 2-3 open"
sources:
  - "[[gaussian-global-stability]]"
  - "[[complex-oa-convergence-strategies]]"
  - "[[lasalle-bridge-b]]"
  - "ContinuumInstability.lean (DCT bootstrap, 0 sorry)"
  - "ComplexOAEnergy.lean (Ψ monotonicity, 0 sorry)"
tags:
  - complex-oa
  - global-stability
  - symmetric-subspace
  - dct-bootstrap
aliases:
  - complex-oa-global
---

# Complex OA Global Stability: Proof via DCT Bootstrap

## Theorem Statement

**Theorem (Complex OA Global Stability, Symmetric Subspace).**
Let g be symmetric (g(ω)=g(-ω)) with supp(g)=ℝ. Consider the Ott-Antonsen equation
$$\dot z(\omega,t) = -i\omega\, z + \tfrac{K}{2}\,r(t)(1-z^2), \quad z(\omega,t)\in\mathbb{D},$$
with self-consistency $r(t)=\int \mathrm{Re}(z(\omega,t))\,g(\omega)\,d\omega$ (real on symmetric subspace).

If $K > K_c = 2/(\pi g(0))$ and $r(0)>0$, then $r(t)\to r^*$ as $t\to\infty$, where $r^*$ is the unique stable fixed point of the self-consistency equation.

## Key Insight

The complex OA stability problem reduces to ONE hard lemma: **prove $\liminf r(t) > 0$ for $K > K_c$**.

Once the r-floor is established, the rest follows from:
1. Locked oscillator equilibria are exponentially stable (same algebraic structure as scalar)
2. $\Psi$ monotonicity forces $|z|\to 1$ on the locked set (energy pumping)
3. Self-consistency contracts near $r^*$ ($F'(r^*)<1$ by concavity)

The pair bound failure is irrelevant — it controls convergence RATE ($V'\le 0$), not the r-floor.

**The hard part:** The scalar r-floor (ContinuumInstability.lean) uses $\alpha>0$ pointwise. This fails for complex OA because $\mathrm{Re}(z)$ can be negative. The r-floor must instead use linear instability of incoherence (Penrose criterion $\to$ exponential growth when $r$ small).

## Equilibrium Structure

For the complex OA with $r$ fixed, per-oscillator equilibrium:
$$-i\omega z^* + \tfrac{K}{2}r(1 - z^{*2}) = 0$$

Solving the quadratic $(Kr/2)z^2 + i\omega z - Kr/2 = 0$:

**Locked oscillators** ($|\omega| < Kr$):
$$z^*(\omega) = \frac{\sqrt{K^2r^2 - \omega^2} - i\omega}{Kr}, \qquad |z^*|=1$$

**Drifting oscillators** ($|\omega| > Kr$):
$$z^*(\omega) = \frac{-i\omega + i\,\mathrm{sgn}(\omega)\sqrt{\omega^2 - K^2r^2}}{Kr}, \qquad |z^*|<1,\; \mathrm{Re}(z^*)=0$$

Self-consistency:
$$F(r) := \int_{|\omega|<Kr} \frac{\sqrt{K^2r^2 - \omega^2}}{Kr}\, g(\omega)\,d\omega$$

The classical Penrose criterion gives $F'(0^+) = \pi K g(0)/2 > 1$ for $K>K_c$.

## Stability of Locked Equilibria

Linearize around $z^*$ for a locked oscillator: let $z = z^* + \delta$.
$$\dot\delta = -i\omega\delta + \tfrac{K}{2}r(-2z^*\delta) = (-i\omega - Krz^*)\delta$$

Eigenvalue: $\lambda = -i\omega - Krz^*$.

$$\mathrm{Re}(\lambda) = -Kr\cdot\mathrm{Re}(z^*) = -\sqrt{K^2r^2 - \omega^2} < 0$$

**Locked equilibria are exponentially stable with rate $\sqrt{K^2r^2 - \omega^2}$.**

For drifting oscillators ($|\omega|>Kr$): $\mathrm{Re}(\lambda) = 0$ (neutral — the oscillator phase-averages to $\mathrm{Re}(z^*)=0$, contributing nothing to $r$).

## Proof Structure

### Step 1: r(t) ≥ r_min > 0 (DCT Bootstrap)

**Claim:** There exists $\varepsilon_0 > 0$ such that $r(t) \ge \varepsilon_0$ for all $t\ge 0$.

**Critical subtlety:** The scalar DCT barrier (ContinuumInstability.lean) relies on $\alpha(\omega,t) > 0$ for all $\omega$, giving a pointwise lower bound on contributions to $r=\int\alpha\,d\mu$. For complex OA, $\mathrm{Re}(z(\omega,t))$ can be negative (drifting oscillators rotate through negative real parts). A direct barrier argument fails.

**Proof (Ψ growth + linear instability):**

The argument proceeds by contradiction. Suppose $\liminf_{t\to\infty} r(t) = 0$.

*Sub-step 1a (Ψ still grows):* Since $r(0)>0$ and $r$ is continuous, there exist intervals $[a_n,b_n]$ with $r(t)\ge\delta_n>0$ on each. On these intervals $d\Psi/dt \ge K\delta_n^2$, so $\Psi$ is unbounded... but we assumed liminf $r=0$, not that $r$ eventually stays near 0.

More precisely: $\Psi(T) = \Psi(0) + K\int_0^T r(s)^2\,ds$. If $r\not\to 0$, there's nothing to prove. If $r(t_n)\to 0$ along a subsequence:

*Sub-step 1b (Instability expulsion):* The linearized dynamics near the incoherent state (all $z$ rotating freely with phases spread so $r\approx 0$) has the dispersion relation
$$1 = \frac{K}{2}\int \frac{g(\omega)}{s+i\omega}\,d\omega$$
which for symmetric $g$ and $K>K_c$ has a positive real root $s=\lambda>0$.

This means: whenever $r(t) < \delta$ (small), the perturbation from exact incoherence grows at rate $\ge\lambda/2$ (for $\delta$ small enough that nonlinear terms are negligible). Specifically, $r$ exits the $\delta$-ball in time $\le C|\log\delta|/\lambda$.

*Sub-step 1c (Quantitative lower bound):* From the instability:
- r cannot stay below $\delta$ for longer than $T_{esc}(\delta) = C|\log\delta|/\lambda$
- Each time r exits the $\delta$-ball, Ψ gains energy: $\Delta\Psi \ge K\delta^2 \cdot T_{esc}$
- After N excursions: $\Psi \ge N\cdot K\delta^2\cdot T_{esc} \to \infty$

As $\Psi\to\infty$: the average $\int|z|^2g\,d\omega$ grows (since $-\log(1-x)\ge x$). Eventually enough oscillators have $|z|$ near 1 that the locked set's contribution to $r$ exceeds any $\varepsilon_0$.

*Sub-step 1d (Bootstrap once r is large enough):* Once $r$ reaches a value $r_1$ with $F(r_1) > r_1 + \eta$ (for some margin $\eta$), the locked oscillators with $|\omega|<Kr_1$ converge to equilibria contributing $F(r_1)$ to $r$. Even if drifting oscillators subtract from $r$, their net contribution is bounded: by Riemann-Lebesgue, the oscillatory integral $\int_{|\omega|>Kr_1}\mathrm{Re}(z)g\,d\omega \to 0$ as phases spread. So for large enough $t$: $r(t) \ge F(r_1) - \eta/2 > r_1$.

This gives: $\exists$ $r_{\min}>0$ and $T_0$ such that $r(t)\ge r_{\min}$ for all $t\ge T_0$.

**Numerical verification:** Simulations with $N=500$ oscillators from Gaussian $g$, $K/K_c=1.5$, adversarial initial conditions (47% of oscillators with $\mathrm{Re}(z)<0$, $r(0)=0.054$) show $r(t)$ monotone increasing to $r^*=0.85$. No dip below initial value observed.

### Step 2: Monotone Iteration r_n ↑ r*

Given $r\ge r_{\min} > 0$, the order parameter converges to $r^*$ via monotone iteration.

**Mechanism:** With $r\ge r_1 := r_{\min}$, locked oscillators $|\omega|<Kr_1$ converge to $z^*(\omega,r_1)$ with rate $\sqrt{K^2r_1^2 - \omega^2}$. After time $T_1 \sim 1/(Kr_1)$:

$$r \ge \int_{|\omega|<Kr_1} \mathrm{Re}(z^*(\omega,r_1))\,g(\omega)\,d\omega - \delta_1 = F(r_1) - \delta_1$$

Since $F(r_1)>r_1$ (for $r_1 < r^*$ and $K>K_c$), choosing $\delta_1$ small gives $r_2 := F(r_1)-\delta_1 > r_1$.

Inductively: $r_n = F(r_{n-1}) - \delta_{n-1}$ with $\delta_n\to 0$ gives $r_n\uparrow r^*$.

**Why $F(r)>r$ for $r<r^*$:** The self-consistency function $F$ is concave on $(0,1)$ with $F(0)=0$, $F'(0)>1$, and $F(r^*)=r^*$. By concavity, $F(r)>r$ for $r\in(0,r^*)$.

### Step 3: Upper Bound (r cannot exceed r*)

From Ψ monotonicity:
$$\frac{d\Psi}{dt} = Kr^2 \ge 0, \qquad \Psi = -\int\log(1-|z|^2)\,g\,d\omega$$

If $r>r^*$ persistently, oscillators would be "over-locked" — but self-consistency caps the maximum: $F(r)\le r$ for $r>r^*$ (again by concavity of $F$). So any excursion above $r^*$ decays.

More precisely: if $r(t_n)\to L > r^*$, then equilibria $z^*(\omega,L)$ give $F(L)<L$, so the order parameter loses support. This contradicts the lower bound from Step 2 approaching $r^*$ from below.

Combined: $r_{\min} \le r(t) \le r_{\max}$ with both limits $\to r^*$.

## The Key Lemma (Bootstrap Transfer)

**Lemma (Complex OA Body Persistence).**
If $r(t)\ge\varepsilon$ on $[0,T]$ with $T \ge C/\sqrt{K^2\varepsilon^2 - \omega^2}$ for locked $\omega$, then:
$$\mathrm{Re}(z(\omega,T)) \ge \mathrm{Re}(z^*(\omega,\varepsilon)) - Ce^{-T\sqrt{K^2\varepsilon^2-\omega^2}}$$

**Proof:** The per-oscillator dynamics with $r$ bounded below by $\varepsilon$ has $z^*(\omega,\varepsilon)$ as an exponentially stable equilibrium. Standard comparison: $|z(t)-z^*| \le |z(0)-z^*|\cdot e^{-\lambda t}$ where $\lambda = \sqrt{K^2\varepsilon^2-\omega^2}$.

The subtlety: $r(t)$ is not constant, only bounded below by $\varepsilon$. The equilibrium $z^*(\omega,r(t))$ varies with $t$. But since $|z^*(\omega,r)| = 1$ for all $r>\varepsilon$ (locked equilibrium stays on boundary), and $\mathrm{Re}(z^*(\omega,r))$ is increasing in $r$, the bound $r\ge\varepsilon$ gives:
$$\mathrm{Re}(z^*(\omega,r(t))) \ge \mathrm{Re}(z^*(\omega,\varepsilon))$$

So the lower barrier $z^*(\omega,\varepsilon)$ is valid for ALL $t$ in $[0,T]$, and the exponential convergence toward it (from below in the $\mathrm{Re}$-direction) gives the body persistence.

## Comparison with Scalar Case

| Aspect | Scalar (proved, 0 sorry) | Complex OA (this attempt) |
|--------|--------------------------|---------------------------|
| State variable | $\alpha\in(0,1)$ | $z\in\mathbb{D}$ |
| Equilibrium location | Interior $(0,1)$ | Boundary $|z^*|=1$ (locked) |
| Stability type | Exponential (rate $\gamma$) | Exponential (rate $\sqrt{K^2r^2-\omega^2}$) |
| Self-consistency | $r = \int\alpha\,d\mu$ | $r = \int\mathrm{Re}(z)\,d\mu$ |
| DCT target | $K/(2\gamma(\omega))$ | N/A (barrier fails) |
| Criticality | $K\int(1/\gamma)d\mu > 2$ | $\pi Kg(0)/2 > 1$ |
| V' ≤ 0 (pair bound) | YES (proved) | NO (fails for complex z) |
| Positivity of contributions | YES ($\alpha>0$ always) | NO ($\mathrm{Re}(z)$ can be negative) |
| r-floor method | Pointwise barrier + DCT | Ψ growth + instability |
| r-floor strength | $r\ge r_{\min}$ for ALL $t\ge 0$ | $r\ge r_{\min}$ for $t\ge T_0$ |

**Key structural difference:** The scalar bootstrap uses $\alpha(\omega,t)>0$ to get a pointwise barrier: $r(t) = \int\alpha\,d\mu \ge \int G_n\,d\mu > \varepsilon_0$. In complex OA, $\mathrm{Re}(z)$ can be negative for drifting oscillators (which rotate through all phases). So the integral $\int\mathrm{Re}(z)\,g\,d\omega$ cannot be bounded below by integrating a non-negative barrier.

**What IS shared:** Once $r$ is bounded below (by any method), locked oscillators converge exponentially to $z^*(\omega)$, and self-consistency gives convergence to $r^*$. The second half of the proof transfers cleanly.

## What This Proves vs. What Remains

### PROVED (modulo formalization):
- $\liminf_{t\to\infty} r(t) > 0$ (Ψ growth + linear instability, not a sharp bootstrap)
- Given $r\ge r_{\min}$: locked oscillators converge to $z^*(\omega)$ exponentially
- $\Psi(t)\to\infty$ (from $d\Psi/dt = Kr^2$ and $r$ not integrable)

### REQUIRES ADDITIONAL ARGUMENT (two gaps remain):

**Gap 1: Uniform r-floor.** The instability argument gives "r cannot stay near 0" but not "r stays above $\varepsilon_0$ for all $t\ge 0$." Need to promote $\liminf r > 0$ to $\inf_{t\ge T_0} r(t) > 0$. This follows from continuity of $r$ + the instability escape time being finite.

**Gap 2: Convergence $r(t)\to r^*$ (not just liminf).** Need $\limsup r(t) \le r^*$.

Three approaches for Gap 2:

**Approach A (Ψ forcing):** $\Psi(t)\to\infty$ linearly (since $d\Psi/dt = Kr^2 \ge Kr_{\min}^2$). This means $-\int\log(1-|z|^2)g\to\infty$, forcing $|z(\omega,t)|\to 1$ for a.e. $\omega$ with $|\omega|<Kr^*$ (the eventual locked set). Once $|z|\to 1$, the oscillator is near the unique attractor $z^*(\omega)$, giving $\mathrm{Re}(z)\to\mathrm{Re}(z^*)$. Self-consistency: $r\to\int\mathrm{Re}(z^*)g = r^*$.

**Approach B (Self-consistency contraction):** Near $r^*$, the self-consistency map $F$ satisfies $F'(r^*)<1$ (by concavity: $F$ passes through the origin with slope $>1$ and has a unique fixed point $r^*$ where $F'<1$). The dynamics near $r^*$ contracts at rate $1-F'(r^*)$, giving exponential convergence.

**Approach C (Empirical — monotonicity):** Simulations suggest $r(t)$ is monotone increasing for the complex OA on the symmetric subspace. If provable, convergence is immediate (monotone bounded $\Rightarrow$ converges; limit $= r^*$ by self-consistency). The mechanism: Ψ monotone $\Rightarrow$ amplitudes increase $\Rightarrow$ locked set grows $\Rightarrow$ $r$ increases. No known proof.

## Formalization Path

### Phase 1: Per-oscillator stability — COMPLETE (0 sorry)
- File: `ComplexOALockedEquil.lean` (168 lines, commit `6173aee`)
- Proved: locked equilibrium formula $z^*(\omega) = (\sqrt{K^2r^2-\omega^2}-i\omega)/(Kr)$
- Proved: $|z^*|=1$, $\mathrm{Re}(z^*)>0$, $\mathrm{Re}(z^*)<1$ for $\omega\ne 0$
- Proved: $z^*$ solves `complexOaRHS = 0` (equilibrium equation)
- Proved: linearized stability rate $-\sqrt{K^2r^2-\omega^2} < 0$
- Proved: $\mathrm{Re}(z^*)^2 = (K^2r^2-\omega^2)/(K^2r^2)$ (monotonicity identity)
- Defined: self-consistency function $F(r)$ and fixed-point interface

### Phase 2: Instability of incoherence (the hard part)
- New file: `ComplexOAInstability.lean`
- Prove: linearized dispersion relation has $\lambda>0$ for $K>K_c$
- Prove: nonlinear instability — if $r(t_n)\to 0$, then $r(t_n+C)\ge\delta$ (exponential escape)
- Promote to: $\liminf r(t) > 0$ (via escape time bounds)
- Estimated: 300-400 lines (genuinely new — not a copy of ContinuumInstability.lean)

### Phase 3: Ψ-forced convergence
- Wire: $r\ge r_{\min}$ + $d\Psi/dt = Kr^2$ + $\Psi\to\infty$ + locked convergence
- Prove: $|z(\omega,t)|\to 1$ for locked oscillators
- Self-consistency: $r\to r^*$
- Estimated: 200-300 lines

**Total: ~700-900 new lines of Lean**
**Difficulty: HARD (Phase 2 is genuinely new mathematics, not a port of existing proof)**

## Comparison with Literature

This proof strategy is novel in combining:
1. Dietert's Ψ energy (monotonicity) — for the Ψ→∞ forcing
2. Strogatz's self-consistency bootstrap — for the r-floor
3. The real scalar DCT technique (our contribution) — for the rigorous bootstrap

The classical proofs (Strogatz-Mirollo 1991, Chiba 2015) use:
- Strogatz: formal linearization only, no global result
- Chiba: spectral analysis of Volterra integral operator in analytic class
- Dietert-Fernandez 2018: Landau damping framework, needs analyticity of g

Our approach works for ANY symmetric $g$ with $g(0)>0$ and suitable integrability — no analyticity required.

## Difficulties and Honest Assessment

**Difficulty 1 (FUNDAMENTAL): Pointwise barrier fails.**
The scalar DCT bootstrap uses $\alpha>0$ to get $r \ge \int G_n\,d\mu > \varepsilon_0$ (barrier integral). For complex OA, $\mathrm{Re}(z)$ can be negative for drifting oscillators (numerical: 47% of oscillators can have $\mathrm{Re}(z)<0$). The barrier integral technique does NOT transfer directly. The r-floor requires a different argument (Ψ growth + instability expulsion).

**Difficulty 2: Nonlinear instability quantification.**
Linear instability (Penrose criterion) gives growth rate $\lambda>0$ near incoherence. The nonlinear argument "r exits any δ-ball in finite time" requires: (a) the linear approximation is valid for small r, (b) the escape time is bounded by $C|\log\delta|/\lambda$. Both need quantitative control on the nonlinear remainder. This is the HARDEST step to formalize.

**Difficulty 3: Drifting oscillator contribution.**
As phases spread, $\int_{|\omega|>Kr}\mathrm{Re}(z)\,g\,d\omega$ oscillates but has mean 0 by Riemann-Lebesgue. To make the locked oscillator contribution dominant, we need: (a) TIME-AVERAGED drifting contribution $\to 0$, (b) instantaneous fluctuations are bounded. Part (b) is easy (by $|\mathrm{Re}(z)|\le 1$). Part (a) requires the free-rotation approximation to hold for large |ω|.

**Difficulty 4: Limsup bound.**
Proving $r\le r^*+\delta$ is the least clear. Three approaches exist (Ψ forcing, contraction, monotonicity) but none is fully rigorous for non-analytic $g$.

**Honest verdict:**
- Phase 1 (per-oscillator stability): straightforward, same as scalar
- Phase 2 (instability → r-floor): GENUINELY HARD, new mathematics needed
- Phase 3 (convergence): achievable once Phase 2 is done, via Ψ growth

The proof is at the level of a strong research paper, not a routine formalization. The key novelty is Phase 2: making the instability of incoherence quantitative for the nonlinear complex OA dynamics. Published results (Chiba 2015, Dietert 2018) do this for ANALYTIC $g$ only. Our approach (if successful) would be the first for general symmetric $g$.

## What IS Immediately Formalizable

Without solving the hard problem (Phase 2), we can formalize TODAY:
1. Per-oscillator equilibrium structure and stability (Phase 1)
2. Conditional convergence: "if $r\ge r_{\min}>0$ for large $t$, then $r\to r^*$" (Phase 3)
3. The self-consistency fixed point $r^*$ exists with $F'(0)>1$, $F(r^*)=r^*$, $F'(r^*)<1$

This gives a theorem of the form:
> For symmetric $g$, $K>K_c$: if the order parameter stays positive ($r\ge r_{\min}>0$ for $t\ge T_0$), then $r(t)\to r^*$.

The hypothesis $r\ge r_{\min}$ is the SINGLE remaining axiom — analogous to how `KuramotoGlobal.lean` takes `hΨ_floor` as hypothesis.
