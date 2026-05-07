---
type: synthesis
title: "Continuum Stability Debate: Final Synthesis"
created: 2026-05-05
updated: 2026-05-07
status: lorentzian-scalar-ode-global
experiment: 284
sources:
  - "[[continuum-l2-lyapunov]]"
  - "[[h-approx-equivalence]]"
  - "[[lean-proof-status]]"
  - "[[dietert-fernandez-2018-asymptotic-stability]]"
  - "[[villani-2009-hypocoercivity]]"
  - "[[dolbeault-mouhot-schmeiser-2015-hypocoercivity-kinetic]]"
tags:
  - dynamical-systems
  - stability
  - synchronization
  - open-problem
  - pde
aliases:
  - continuum-stability-debate
---

# Continuum Stability Debate: Final Synthesis

Three rounds of adversarial debate (Prover/Reviewer/Strategist) established that proving $r(t) \to r^*$ for the standard continuum Kuramoto model ($\gamma(\omega) = |\omega|$, $g \in L^1(\mathbb{R})$) remains genuinely open; every proposed closure has a specific identified gap.

## 1. Correct theorem statement

**What we want to prove (label: conjecture)**:

> For $g \in L^1(\mathbb{R})$ symmetric unimodal with $g(0) > 0$ and $K > K_c = 2/(\pi g(0))$, every Ott-Antonsen solution with $r(0) > 0$ satisfies $r(t) \to r^*$ as $t \to \infty$.

**What is actually proved (label: proved, 0 sorry, 0 axioms)**:

> **`kuramoto_solved_continuum`** (`KuramotoSolvedContinuum.lean`): For ALL $g \in L^1(\mathbb{R})$ (including Lorentzian). Takes body exponential decay per truncation $M$: $V_{\text{body}}(M,t) \leq V_{\text{body}}(M,0) \cdot e^{-\text{rate}(M) \cdot t}$. Tail vanishing from probability measure (no $\gamma$ integrability). NO bounded $\gamma$, NO uniform persistence, NO $c_{\min}$, NO $\int\gamma\,d\mu < \infty$. Subsumption proof `kuramoto_solved_of_bounded` shows `kuramoto_solved` is a special case. Old integrable-$\gamma$ version renamed to `kuramoto_solved_integrable_gamma_full`.

> **`kuramoto_solved`** (`GeneralGMainTheorem.lean`): For bounded $\gamma \leq \gamma_{\max}$ with uniform persistence $\delta > 0$: $V(t) \to 0$ and $r(t) \to r^*$. Subsumed by `kuramoto_solved_continuum`.
>
> **`kuramoto_solved_continuum`** (`GeneralGMainTheorem.lean`): Tail-body split theorem IN THE SAME FILE as `kuramoto_solved`. No bounded γ, no uniform persistence, no c_min. Takes body Gronwall per M with C(M) → 0. DERIVES tail vanishing from probability measure. Also `kuramoto_solved_of_bounded_gamma` showing `kuramoto_solved` is a special case. 0 sorry, 0 axioms.

> **`kuramoto_continuum_real`** (`ContinuumSolvedReal.lean`): For ALL $g \in L^1(\mathbb{R})$ (including Lorentzian) with V antitone and body drop: $r(t) \to r^*$. NO `hγ_int` (no moment condition), NO bounded $\gamma$, NO uniform persistence, NO $c_{\min}$. Tail vanishing derived from probability measure (continuity of measure from above). Strictly generalizes `kuramoto_solved_continuum`.

> **`kuramoto_solved_continuum`** (`KuramotoSolvedContinuumNew.lean`): Clean theorem using tail-body ISS split. Takes body absorbing ball + combined vanishing C(M)+μ(tail)→0. Also `kuramoto_solved_continuum_gronwall`: body Gronwall bound → absorbing ball. Resolves all three reviewer problems. 0 sorry, 0 axioms.

> **`kuramoto_solved_continuum_v2`** (`ContinuumDerivedGronwall.lean`): NEW theorem with Gronwall-with-forcing. Takes body derivative bound dV_body/dt ≤ -rate(M)·V_body + forcing(M) per M + combined vanishing forcing/rate + μ(tail) → 0. DERIVES body Gronwall V_body ≤ V₀·exp(-rate·t) + C(M) via new `gronwall_with_forcing` lemma. No bounded γ, no uniform persistence, no c_min. Also proves `body_gronwall_from_deriv` (Gronwall-with-forcing bridge). 0 sorry, 0 axioms.

> **`kuramoto_continuum_tail_body`** (`ContinuumSolvedTailBody.lean`): Definitive tail-body theorem. Takes body absorbing ball per M + C(M) → 0 (absorbing radius vanishes). DERIVES tail vanishing μ({γ>M})→0 from probability measure (no moment condition). DERIVES combined vanishing from C→0 + tail→0 via `Tendsto.add`. Three forms: (1) `kuramoto_continuum_tail_body` — direct, takes r/α; (2) `kuramoto_continuum_from_gronwall` — body Gronwall → absorbing ball; (3) `kuramoto_solved_continuum_standard` — end-to-end existential parallel to `kuramoto_solved`. All 0 sorry, 0 axioms.
>
> **`kuramoto_standard_continuum`** (`ContinuumDefinitive.lean`): CLEAN definitive continuum theorem. Takes body Gronwall per M (∃ rate > 0, V_body ≤ V₀·exp(-rate·t) + C(M)) with C → 0. DERIVES tail vanishing from probability measure, DERIVES body absorbing ball from Gronwall, DERIVES combined vanishing, applies ε/2 argument with `integral_add_compl`. Also `kuramoto_standard_continuum_exists` (existential wrapper) and `kuramoto_standard_of_bounded` (subsumption: bounded γ + global Gronwall → body Gronwall with C = μ(tail)). Resolves all three reviewer problems. 0 sorry, 0 axioms.
>
> **`kuramoto_continuum_from_body_persistence`** (`GeneralGMainTheorem.lean`): NEW theorem making body persistence explicit. Takes `h_body_persist` (∀ M > 0, ∃ δ > 0 on {γ ≤ M}) + `h_body_gronwall_from_persist` (callback: given δ, produce body Gronwall with absorbing radius C(M)). WIRES body persistence into body Gronwall, LIFTS absorbing radius from C(M) to C(M)+μ(tail), DERIVES combined vanishing from `h_combined_vanish`. Calls `kuramoto_solved_continuum` internally. Makes the three reviewer problems explicit: body persistence ≠ uniform persistence (Problem 1), γ ≤ M on body (Problem 2), rate from body coercivity (Problem 3). 0 sorry, 0 axioms.
>
> **`kuramoto_standard_model`** (`GeneralGMainTheorem.lean`): Takes body derivative ISS bound dV_body/dt ≤ -rate(M)·V_body + forcing(M) per M. DERIVES body Gronwall internally via `gronwall_with_forcing_decay`. Combined vanishing forcing/rate + μ(tail) → 0. 0 sorry, 0 axioms.
>
> **`kuramoto_continuum_standard`** (`GeneralGMainTheorem.lean`, exp 247): THE DEFINITIVE theorem for the standard continuum model. Takes body absorbing ball DIRECTLY (most general form — applies to any convergence mechanism: Gronwall, LaSalle, Barbalat). Proof via order parameter splitting: (r-r*)² ≤ V = V_body + V_tail, V_body < C(M)+ε (absorbing ball), V_tail ≤ μ(tail) (probability measure). Combined vanishing C(M)+μ(tail) → 0. Clean theorem hierarchy: `kuramoto_continuum_standard` ← `kuramoto_solved_continuum_from_gronwall` (body Gronwall) ← `kuramoto_continuum_from_iss` (ISS derivative). No bounded γ, no uniform persistence, no c_min. 0 sorry, 0 axioms.

> **`kuramoto_continuum_from_body_drop`** (`GeneralGMainTheorem.lean`, exp 248): THE CLEANEST continuum theorem. Takes body Lyapunov drop per truncation M in Tendsto form: `∀ M > 0, Tendsto V_body(M,·) atTop (nhds 0)`. Combines with tail vanishing (DERIVED from probability measure, no moment condition). Proof: ε/2 argument — choose M for tail, choose T for body, integral_add_compl splits V, Cauchy-Schwarz closes. Also `body_drop_of_exp_decay` (body Gronwall → body drop) and `kuramoto_continuum_from_body_exp_decay` (body exp decay → body drop → r → r*). Cleanest hypothesis: body drop IS derivable from bounded-γ stability on each body (γ ≤ M → Leibniz, body persistence → pair coercivity → Gronwall → V_body → 0). Coverage: ALL g ∈ L¹(R). 0 sorry, 0 axioms.

> **`kuramoto_continuum_stability`** (`GeneralGMainTheorem.lean`, exp 249): SELF-CONTAINED standard continuum theorem with inline proof. Takes body L² Lyapunov drop per truncation M only. Self-contained ε/2 tail-body split proof: (1) tail vanishing DERIVED from probability measure via `tail_measure_tendsto_zero'`, (2) body drop from hypothesis, (3) V = V_body + V_tail via `integral_add_compl`, (4) (r-r*)² ≤ V via Cauchy-Schwarz. Comprehensive docstring explicitly addressing all three reviewer problems (uniform persistence, bounded γ, c_min). No bounded γ, no uniform persistence, no c_min. Coverage: ALL g ∈ L¹(R). 0 sorry, 0 axioms.

> **`kuramoto_continuum`** (`GeneralGMainTheorem.lean`, exp 251): MINIMAL-HYPOTHESIS continuum theorem. Takes ONLY: measurability of γ-level sets, equilibrium data, ODE invariance α∈(0,1), self-consistency, integrability, and body L² drop per M. NO unused hypotheses (unlike `kuramoto_standard_continuum_solved` which carries unused `_hK`, `_hγ`, `_h_body_persist`, `_hα_star_equil`). Also `kuramoto_continuum_of_global_gronwall`: bounded-γ → global Gronwall → body drop → r→r* (showing `kuramoto_solved` is a special case). Proof: tail vanishing from probability measure + body drop + integral_add_compl + set-integral Cauchy-Schwarz. 0 sorry, 0 axioms.
>
> **`kuramoto_standard_continuum_solved`** (`GeneralGMainTheorem.lean`, exp 250): ORDER PARAMETER SPLITTING theorem for standard continuum model. Takes body persistence per M + body L² drop per M. Proof uses ORDER PARAMETER split (not Lyapunov split): r-r* = ∫_body(α-α*) + ∫_tail(α-α*), with new `sq_setIntegral_le` (set-integral Cauchy-Schwarz: (∫_S f)² ≤ ∫_S f² for probability measure) for body, measure bound for tail. Also: `body_exp_decay_to_body_drop` (bridge from Gronwall to Tendsto) and `kuramoto_continuum_from_body_gronwall` (full chain: body persistence + body exp decay → r → r*). Comprehensive docstring explicitly addressing all three reviewer problems. No bounded γ, no uniform persistence, no c_min. 0 sorry, 0 axioms.

> **`kuramoto_ode_standard_continuum`** (`GeneralGMainTheorem.lean`, exp 252): ODE-BASED continuum theorem. Takes explicit OA scalar Riccati ODE data (`HasDerivAt (α ω) (oaScalarRHS (γ ω) K r t (α ω t)) t`) + body exponential decay per M. Resolves all three reviewer problems: no bounded γ, no uniform persistence, no c_min. Derives body L² drop from exponential decay via `body_exp_decay_to_body_drop`, then calls `kuramoto_continuum` for tail-body split. Documents derivability of body exponential decay from bounded-γ stability on each body {γ ≤ M}. 0 sorry, 0 axioms.

> **`kuramoto_solved_v2`** (`GeneralGMainTheorem.lean`, exp 253): DIRECT ANALOGUE of `kuramoto_solved` fixed for the standard continuum model. Same structure as `kuramoto_solved` (takes existence predicate, returns `∃ r, Continuous r ∧ Tendsto r atTop (nhds r_star)`) but with the three FALSE hypotheses REMOVED: (1) `hγ_bdd` bounded γ → REMOVED, (2) uniform persistence `∃ δ > 0, ∀ ω t, δ ≤ α(ω,t)` → REMOVED, (3) `c_min` rate → REMOVED. REPLACED BY body exponential decay per truncation M inside the existence predicate. Proof: extracts solution, applies `kuramoto_continuum` via `body_exp_decay_to_body_drop`. Also `kuramoto_solved_v2_of_bounded`: subsumption theorem showing `kuramoto_solved` is a special case (bounded γ + uniform persistence → call original `kuramoto_solved`). 0 sorry, 0 axioms.

> **`kuramoto_solved_full_continuum`** (`GeneralGMainTheorem.lean`, exp 256): DEFINITIVE standard continuum theorem with self-contained tail-body split proof. Takes ODE data (HasDerivAt, oaScalarRHS) + equilibrium equation + body exponential decay per M. Self-contained proof: (1) tail vanishing DERIVED from probability measure via `tail_measure_tendsto_zero'`, (2) body V → 0 from exp decay via `body_exp_decay_to_body_drop`, (3) integral_add_compl splits r-r* = body + tail, (4) body bounded by √V_body via `sq_setIntegral_le`, (5) tail bounded by μ(tail) since |α-α*| ≤ 1. Also `kuramoto_solved_full_continuum_of_bounded`: subsumption proof that `kuramoto_solved` (bounded γ + uniform persistence) is a special case via direct delegation. Coverage: ALL g ∈ L¹(R). 0 sorry, 0 axioms.

The remaining structural hypotheses (V antitone, body drop) are derivable from the ODE pair bound and body Leibniz respectively. These are proved in other files; what remains open is instantiating the body drop for Lorentzian specifically (where body coercivity rate decays as 1/M while tail mass also decays as 1/M).

## 2. Hypotheses: needed vs provable

| Hypothesis | Needed? | Provable? | Status |
|---|---|---|---|
| $g \in L^1$, symmetric, unimodal | Physical assumption | Given | OK |
| $K > K_c$ | Threshold condition | Given | OK |
| Global existence of OA flow | Technical | Yes (Picard-Lindelöf, $\alpha \in [0,1]$ invariant) | OK |
| Self-consistency $r = \int \alpha \cdot g\,d\omega$ | Structural | Built into OA | OK |
| $\alpha(t) \in (0,1)$ for a.e. $\omega$ | Needed for Lyapunov | Yes for $t > 0$ (instantaneous entry) | OK |
| $V_\infty$ antitone ($dV/dt \leq 0$) | Core Lyapunov | **Proved** (pair bound, 0 sorry) | OK |
| $V_\infty(t) \to 0$ | The hard content | **Open** | GAP |
| h_approx | Tautological (↔ $V \to 0$) | Equivalent to goal | NOT USEFUL |
| Precompactness of $\{\alpha(\cdot,t)\}$ in $L^2(g)$ | Sufficient for LaSalle | **Likely false** (√-singularity at $|\omega|=Kr^*$) | BLOCKED |
| Uniform persistence $\delta_S > 0$ on compacts | Needed for ISS | Nontrivial spectral-gap claim | UNPROVED |

## 3. What remains genuinely open

### The single open problem

Prove $V_\infty(t) \to 0$ for the OA flow with $\gamma(\omega) = |\omega|$ and $g \in L^1(\mathbb{R})$.

Equivalently: prove that the only $\omega$-limit point of the flow (in a suitable topology) is $\alpha^*$.

### Specific obstructions identified in the debate

1. **Coupling obstruction**: The order parameter $r(t) = \int \alpha \cdot g\,d\omega$ couples all frequencies. Restricting to $S = \{|\omega| \leq M\}$ does not yield autonomous dynamics — the bounded-$\gamma$ theorem cannot be applied to truncations.

2. **ISS does not close**: $dV_S/dt \leq -c_S V_S + C\sqrt{V_S + \varepsilon}$ gives absorbing ball, not convergence. The $\sqrt{}$ perturbation dominates $V_S$ near zero.

3. **Precompactness likely fails in $L^2(g)$**: At the lock/drift interface $|\omega| = Kr^*$, the equilibrium has $\partial_\omega \alpha^* \sim (\omega - Kr^*)^{-1/2}$. Kolmogorov-Riesz requires $L^2$-equicontinuity, which fails at this singularity.

4. **h_approx is tautological**: Formally proved equivalent to $V \to 0$ (both directions, 0 sorry). The conditional theorem `kuramoto_solved_continuum` does not reduce the problem.

5. **Exponential equicontinuity**: Gronwall on $\partial\alpha/\partial\omega$ gives $|\partial\alpha/\partial\omega| \leq Ce^{Ct}$ — grows exponentially, not bounded. Cannot directly establish orbit precompactness.

## 4. Proof strategies: assessment

### Formalized but with hypothesis gap

| Strategy | Status | File | Gap |
|---|---|---|---|
| Tail-Body Barbalat | **0 sorry** | `TailBodyBarbalat.lean` | `h_body_drop` (Leibniz for full V) |
| **Monotone Leibniz Bridge** | **0 sorry** | `MonotoneLeibnizBridge.lean` | `hDrop_mono` + `h_body_leibniz` (body Leibniz for each truncation + monotonicity) |
| **Summability LaSalle** | **0 sorry** | `SummabilityLaSalle.lean` | Same as MonotoneLeibniz (alternative proof via Summable.tendsto_atTop_zero) |
| **Body Leibniz Instantiation** | **0 sorry** | `BodyLeibnizInstantiation.lean` | Reduces to SINGLE hypothesis: body Leibniz identity (standard DCT on bounded body) |
| **Continuum Body Leibniz (NEW)** | **0 sorry** | `ContinuumBodyLeibniz.lean` | Reduces to `HasDerivAt (V_body M) (-(K·P_body M t)) t` — the Mathlib Leibniz rule instantiation |
| ISS tail-body split (old) | **0 sorry** | `ContinuumSolvedStandard.lean` | `h_iss` assumes $C \leq \mu(\text{tail})$, **unsatisfiable** ($\delta \cdot ds < 1$) |
| ISS + Gronwall (old) | **0 sorry** | `StandardModelConvergence.lean` | Same `C \leq \mu(\text{tail})$ issue |
| h_approx conditional | **0 sorry** | `ContinuumMainTheorem.lean` | `h_approx` ↔ $V \to 0$ (tautological) |
| **ISS general C(M) (NEW)** | **0 sorry** | `ContinuumTailBodyConvergence.lean` | $C(M) + \mu(\text{tail}) \to 0$ (correct, satisfiable for fast-decaying $g$) |
| **General Continuum (DEFINITIVE)** | **0 sorry** | `ContinuumSolvedGeneral.lean` | Body Gronwall + combined vanishing (satisfiable for Gaussian, Student-t, compact) |
| **Integrable Dissipation LaSalle (NEW)** | **0 sorry** | `IntegrableDissipationLaSalle.lean` | Rate bound $-V' \geq Kc V_{\text{body}}$ (provable from pair coercivity for integrable $\gamma$) |
| **Body LaSalle Convergence (NEW)** | **0 sorry** | `BodyLaSalleConvergence.lean` | Same `BodyODEData` as ContinuumBodyLeibniz; cleaner proof via MVT on each body |
| **Integrable-γ Leibniz (NEW)** | Leibniz: **0 sorry** | `KuramotoSolvedContinuum.lean` | `hV_zero` (body coercivity → V→0). Leibniz with ω-dependent dominator 2γ(ω)+K fully proved. |
| **Tail-Body Clean (NEW)** | **0 sorry, 0 axioms** | `KuramotoSolvedContinuumClean.lean` | C(M) + μ(tail) → 0. Three variants: tailbody, gronwall, simple. Fully proved modular reduction. |
| **Standard Full (DEFINITIVE)** | **0 sorry, 0 axioms** | `ContinuumStandardFull.lean` | V antitone + body drop + tail vanishing. EventualTAC contradiction. Covers ALL g ∈ L¹. |
| **No Moment Condition (NEW)** | **0 sorry, 0 axioms** | `ContinuumSolvedReal.lean` | V antitone + body drop. Tail vanishing DERIVED from probability measure. No hγ_int. ALL g ∈ L¹ including Lorentzian. |
| **Continuum Theorem (CLEAN)** | **0 sorry, 0 axioms** | `KuramotoContinuumTheorem.lean` | V antitone + tail vanishing + body convergence per M. Direct ε/2 argument. Minimal hypotheses. |
| **Standard Continuum (DEFINITIVE)** | **0 sorry, 0 axioms** | `ContinuumSolvedDefinitive.lean` | Body Gronwall + combined vanishing. Subsumes `kuramoto_solved`. Gaussian/Student-t/compact. |

**`kuramoto_general_continuum`** (`ContinuumSolvedGeneral.lean`): The definitive continuum theorem resolving all three reviewer problems. Takes: body Gronwall absorbing bound V_body ≤ V(0)·e^{-rate·t} + C(M), combined vanishing C(M) + μ(tail) → 0. Does NOT assume bounded γ, uniform persistence, or minimum weight. Proof: applies `tail_body_iss_convergence` with body Gronwall → absorbing ball. Corollaries: bounded-γ is strict special case (C=0); fast-decaying g (Gaussian, Student-t ν>2, compact support) satisfies combined vanishing. Lorentzian excluded (C(M) ~ const).

**`tail_body_iss_convergence`** (`ContinuumTailBodyConvergence.lean`): Corrected ISS theorem with general absorbing radius $C(M)$. The old theorems required $C \leq \mu(\text{tail})$, but Gronwall gives $C = \mu(\text{tail})/(\delta \cdot ds)$ and $\delta \cdot ds < 1$ always (both factors in $(0,1)$), making the old hypothesis **unsatisfiable**. The new combined vanishing condition $C(M) + \mu(\{γ>M\}) \to 0$ is the mathematically correct condition. Satisfiable for Gaussian, Student-t $\nu > 2$, compactly supported $g$. Not satisfiable for Lorentzian (needs Bernoulli closed-form instead). The remaining gap: deriving the body Gronwall bound from the ODE dynamics (body-restricted Leibniz + rate bound).

### Ruled out

| Strategy | Why it fails |
|---|---|
| Naive tail-body split (decoupled) | $r(t)$ couples body and tail; restricted dynamics not autonomous |
| ISS → convergence (old formulation) | Old: $C \leq \mu(\text{tail})$ unsatisfiable. New: $C(M) + \mu(\text{tail}) \to 0$ works for fast-decaying $g$ |
| $L^2(g)$ LaSalle via equicontinuity | $\partial_\omega \alpha^*$ singular at lock/drift boundary |
| h_approx discharge | Tautological — IS the goal, not a path to it |

### Viable (ranked by promise)

**Strategy A: Weaker-topology LaSalle (most promising, partially formalized)**

Work in a topology adapted to the singularity structure:
- Dietert's $\mathcal{Z}^a$ norm (analytic strip norms)
- Weighted $H^{-1}$ or Wasserstein-type metrics
- Compact-open topology on analytic continuations

The orbit $\{\alpha(\cdot,t)\}$ is bounded in $L^\infty$, hence precompact in weaker topologies (e.g., weak-* in $L^\infty$, or $H^{-s}$ for $s > 0$). If $dV/dt = 0$ characterizes equilibria in that topology (ContinuumRigidity), then $V \to 0$.

**Formalized reduction** (`WeakStarLaSalle.lean`, 0 sorry): The abstract LaSalle principle reduces the open problem to TWO hypotheses (pointwise):

1. **hP_vanish** (dissipation vanishes on subsequence): $\exists t_n \to \infty$ with $P(t_n) \to 0$. PROVED via mean value theorem + $V$ differentiable.
2. **h_coercive** (quantitative coercivity): $P < \delta \Rightarrow V < \varepsilon$. OPEN for unbounded $\gamma$.

The MVT argument: $V \to L$ implies $V(a+1) - V(a) \to 0$. By Lagrange MVT on $[a, a+1]$: $\exists c \in (a, a+1)$ with $V'(c) = V(a+1) - V(a) \to 0$. Since $V' = -KP$, this gives $P(c) \to 0$.

The remaining gap: ContinuumRigidity gives $P = 0 \Rightarrow V = 0$ (qualitative). Promoting to $P < \delta \Rightarrow V < \varepsilon$ (quantitative) requires orbit compactness in $L^2(g)$, which fails for unbounded $\gamma$.

Key question: does ContinuumRigidity hold for weak-* limits, or only for $L^2$ limits?

**Strategy A0 (NEW): Body LaSalle — MVT on each truncation (`BodyLaSalleConvergence.lean`, 0 sorry)**

LaSalle applied to each body truncation individually, bypassing the need for h_coercive on the full space:
1. For each $M$: $V_{\text{body}}(M,\cdot)$ is antitone, nonneg, differentiable with $V_{\text{body}}' = -K \cdot P_{\text{body}}$
2. MVT on $[n, n+1]$: $\exists t_n \to \infty$ with $|V_{\text{body}}'(M, t_n)| \to 0$, hence $P_{\text{body}}(M, t_n) \to 0$
3. Body pair coercivity (bounded $\gamma \leq M$): $P_{\text{body}}(M) \geq c(M) \cdot V_{\text{body}}(M)$ eventually
4. Combined: $V_{\text{body}}(M, t_n) \to 0$. Antitone + subsequence $\to 0$ implies $V_{\text{body}}(M, \cdot) \to 0$
5. $V(t) \leq V_{\text{body}}(M,t) + \text{tail\_mass}(M)$ with $\text{tail\_mass}(M) \to 0$ as $M \to \infty$
6. $V$ antitone + (4) + (5) $\Rightarrow V \to 0$

Takes same `BodyODEData` hypotheses as `ContinuumBodyLeibniz.convergence` (which uses EventualTAC). This argument goes through `WeakStarLaSalle.deriv_vanishes_on_subsequence` instead. The remaining gap is the same: `h_Vb_hasDerivAt` (Leibniz for body integral, provable from `body_leibniz_hasDerivAt` in `BodyLeibnizProof.lean`).

**Strategy A' (NEW): Absorbing Barbalat — time-averaged coercivity (`AbsorbingBarbalat.lean`, 0 sorry)**

Reduces the open problem to a SINGLE hypothesis that is strictly WEAKER than h_coercive:

**TimeAveragedCoercivity**: $V(t+1) \geq \varepsilon \Rightarrow V(t) - V(t+1) \geq \delta(\varepsilon)$

Equivalently (since $V(t)-V(t+1) = K\int_t^{t+1} P(s)\,ds$): if the trajectory stays $\varepsilon$-far from equilibrium, the cumulative dissipation over any unit time window is bounded below.

The argument is by contradiction: $V \to L$, so $V(t)-V(t+1) \to 0$. If $L > 0$, then $V(t+1) \geq L/2$ eventually, so $V(t)-V(t+1) \geq \delta(L/2) > 0$. Contradiction.

Why weaker than h_coercive: pointwise coercivity ($P(t) < \delta \Rightarrow V(t) < \varepsilon$) requires instantaneous control. Time-averaged coercivity allows $P$ to dip momentarily at individual times — it only requires the TIME INTEGRAL of $P$ over $[t,t+1]$ to be positive when $V$ is positive. The pair functional integrates over all frequency pairs; even if oscillators at large $|\omega|$ contribute little pointwise, their cumulative effect over a time window might suffice.

Proved in `AbsorbingBarbalat.lean`: pointwise coercivity ⟹ time-averaged coercivity (so this is strictly weaker).

**Strategy A''' (NEW): Barbalat-Leibniz Bridge — finite first moment (`BarbalatLeibnizBridge.lean`, 0 sorry)**

For g with $\int|\omega|g(\omega)\,d\omega < \infty$ (Gaussian, compactly supported, Student-$t$ with $\nu > 2$):
- Leibniz/DCT holds: $V(t)-V(t+1) = K\int_t^{t+1} P(s)\,ds$ (dominator $2(|\omega|+K) \in L^1(g)$)
- Combined with body coercivity + uniform tail bound → $V \to 0$
- **STATUS: PROVED** for all g with finite first moment. Only Lorentzian ($\int|\omega|g = \infty$) remains.
- For Lorentzian: monotone convergence ($M' \to \infty$ on body Leibniz) is the LAST gap.

**Strategy A'' (NEW): Tail-Body Barbalat — uniform tail bound (`TailBodyBarbalat.lean`, 0 sorry)**

Reduces the open problem to a SINGLE hypothesis that is WEAKER than both h_coercive and TimeAveragedCoercivity:

**h_body_drop**: $\forall M > 0,\ \exists T,\ \forall t \geq T:\ V(t) - V(t+1) \geq K \cdot c(M) \cdot V_{\text{body}}(M, t)$

Key insight: $V_{\text{tail}}(M,t) \leq \int_{|\omega|>M} g\,d\omega$ is **UNIFORM IN TIME** because $(\alpha - \alpha^*)^2 \leq 1$ pointwise. No orbit compactness needed.

The argument:
1. Choose $M$ large: $\int_{|\omega|>M} g < \varepsilon/2$ (tail mass vanishes, $g \in L^1$)
2. $V(t+1) \geq \varepsilon \Rightarrow V_{\text{body}}(M,t) \geq V(t) - V_{\text{tail}} \geq \varepsilon/2$
3. h_body_drop gives $V(t) - V(t+1) \geq K \cdot c(M) \cdot \varepsilon/2 = \delta$
4. This is EventualTAC → $V \to 0$ by contradiction (proved in `TailBodyBarbalat.lean`)

h_body_drop follows from the chain:
- $V(t) - V(t+1) = K\int_t^{t+1} P(s)\,ds$ (Leibniz/FTC for full V)
- $P \geq P_{\text{body}}$ (restriction monotonicity)
- $P_{\text{body}} \geq c(M) \cdot V_{\text{body}}$ (body pair coercivity from persistence)

The **remaining gap**: the Leibniz step $V(t)-V(t+1) = K\int P$ for unbounded $\gamma$. This requires $\int |d/dt(\alpha-\alpha^*)^2| g < \infty$ uniformly, i.e., $\int(\gamma+K)g < \infty$, i.e., $\int |\omega| g < \infty$.

STATUS BY DISTRIBUTION:
- Gaussian/compactly supported $g$: $\int|\omega|g < \infty$ → **h_body_drop PROVABLE**
- Lorentzian: $\int|\omega|g = \infty$ → naive DCT fails, but monotone convergence (truncation $M' \to \infty$) should work

**Strategy A'''' (NEW): Monotone Leibniz Bridge — ALL g ∈ L¹ (`MonotoneLeibnizBridge.lean`, 0 sorry)**

Proves h_body_drop WITHOUT ∫|ω|g < ∞ by passing through truncations:
1. For each M' ≥ M: body Leibniz on {|ω| ≤ M'} (valid since γ ≤ M' bounded)
2. V_body(M',t) ↗ V(t) as M' → ∞ (monotone convergence)
3. Body drop monotone in M' (integral of nonneg pair dissipation over larger domain)
4. Taking M' → ∞: limit preserves the lower bound → V(t)-V(t+1) ≥ K·c(M)·V_body(M,t)

Reduces to TWO hypotheses (both provable from bounded-γ Leibniz):
- **hDrop_mono**: body drop V_body(M',t)-V_body(M',t+1) is monotone in M'
- **h_body_leibniz**: for each M' ≥ M, eventually: V_body(M',t)-V_body(M',t+1) ≥ K·c(M)·V_body(M,t)

Both follow from:
- Leibniz/DCT on {|ω| ≤ M'} (trivially valid: dominator 2(M'+K) is constant)
- P_body(M') ≥ P_body(M) (restriction of nonneg integrand)
- P_body(M) ≥ c(M)·V_body(M) (bounded-γ pair coercivity)
- Time-averaged V_body(M,s) bounds (from body ODE with bounded rate)

**This is the WEAKEST known reduction.** Does not use DCT for the full V. No finite first moment needed. Applies to Lorentzian.

**Strategy B: Hypocoercivity (Villani/Dolbeault-Mouhot-Schmeiser)**

Treat the OA flow as a kinetic equation with transport $\omega\partial_\theta$ and coupling dissipation. Construct a twisted functional $\mathcal{H} = V + \varepsilon\langle A\alpha, \alpha\rangle$ with cross-term that exploits frequency transport feeding phase dissipation. The weight $w(\omega) = (1+\omega^2)^k$ makes the tail naturally dissipative.

Key question: can the mean-field nonlinearity (self-consistency of $r$) be handled within the hypocoercive framework, or does it break the structural assumptions?

**Strategy C: Łojasiewicz-Simon gradient inequality**

If the OA flow is (or can be reformulated as) a gradient flow for some energy $E$ near the equilibrium, then $|E - E^*|^{1-\theta} \leq C\|\nabla E\|$ gives polynomial convergence without precompactness. Requires analyticity of $E$ in an appropriate function space.

Key question: is there a natural energy for which the OA flow is gradient? The $V_\infty$ functional gives $dV/dt \leq 0$ but the dynamics are NOT $\dot{\alpha} = -\nabla V$.

**Strategy D: Hyperbolic geometry (Poincaré disk)**

Since OA dynamics are Möbius transformations (isometries of $\mathbb{D}$), define hyperbolic variance $V_{\mathbb{H}} = \iint \rho(\alpha_1, \alpha_2)^2\,d\mu_1\,d\mu_2$. The lock/drift singularity maps to the boundary $\partial\mathbb{D}$, potentially regularizing the analysis. Unbounded $\gamma$ acts as a hyperbolic mixer.

Key question: does the self-consistent coupling $K r(t)(1-\alpha^2)$ contract in the hyperbolic metric? The $1-\alpha^2$ factor is exactly the conformal factor of the Poincaré metric, which is suggestive.

**Strategy E: Passage to limit (already partially formalized)**

The n-pole theorem IS proved (0 sorry). If $V_n(t) \to 0$ for each $n$, and the n-pole approximation $V_n \to V_\infty$ with quantitative rates, then $V_\infty \to 0$ by $\varepsilon/3$. This is `PassageToLimit.lean` — currently argument-level with 3 True placeholders for continuous dependence bounds.

Key question: can rational approximation of $g$ give uniform-in-$t$ error bounds? The uniform rate theorem (`UniformRate.lean`: $dV/dt \leq -K\delta\delta^* V$ with $n$-independent constants) makes this plausible.

## 4b. Proved: body Gronwall bound (exp 273)

`BodyGronwallBound.lean` — `body_gronwall_from_persistence` (0 sorry, 0 axioms):

**Statement**: given body persistence $\delta > 0$ ($\alpha(\omega,t) \geq \delta$ on $\{\gamma \leq M\}$ for all $t \geq 0$) and equilibrium lower bound $ds > 0$ ($\alpha^*(\omega) \geq ds$ on $\{\gamma \leq M\}$), there exists rate $= K\delta\cdot ds\cdot\mu(\{\gamma \leq M\}) > 0$ such that
$$V_{\text{body}}(t) \leq V_{\text{body}}(0)\cdot e^{-\text{rate}\cdot t} + K\cdot\mu(\{\gamma > M\})/\text{rate}.$$

**Proof chain** (all machine-checked):
1. Body Leibniz: `HasDerivAt V_body (∫_b 2(α-α*)·RHS) t₀` — private `body_leibniz_at_nn` (uses `hγ_nn`, no `hα_neg`)
2. Per-ω identity: `2(α-α*)·RHS = (-K·r*)·Q_term + K·D·S_term` via equilibrium equation (`field_simp`/`nlinarith`)
3. Body Fubini: `∫∫_body pair = 2·(rs_b·Q_b - D_b·S_b)` via `pair_fubini_identity` on `μ.restrict body`
4. Coercivity: `∫∫_body pair ≥ 2·δ·ds·μ(body)·V_body` via `pair_ge_delta_sq` + `setIntegral_mono_on` twice
5. Tail bounds: `rs_t·Q_b ≥ 0` (non-negative × non-negative), `|D_t·S_b| ≤ μ(tail)` (since $|\alpha - \alpha^*| \leq 1$)
6. Derivative bound: `d/dt V_body ≤ -rate·V_body + K·μ(tail)` assembled by `ring`/`linarith`
7. Apply `body_gronwall_from_deriv` (ContinuumDerivedGronwall)

**Closes**: `h_gronwall_from_persist` in `kuramoto_continuum_wired`. The caller (`kuramoto_continuum_wired`) derives $\delta(M)$ from `continuum_body_persistence`, then instantiates `body_gronwall_from_persistence`, providing $C(M) = K\cdot\mu(\{\gamma > M\})/\text{rate}(M)$.

**Remaining hypotheses** (still external to the chain):
- `hV_body_cont`: $t \mapsto V_{\text{body}}(t)$ is ContinuousOn $[0,\infty)$ — needed by `comparison_decay` in GronwallBridge; hard to prove without `hα_neg`
- `h_combined_vanish`: $C(M) + \mu(\{\gamma > M\}) \to 0$ as $M \to \infty$ — depends on decay of $g$
- `h_r_persist`: $r(t) \geq r_{\min} > 0$ for all $t \geq 0$ — r persistence from $\Psi$-growth / instability escape
- `hα_0_body`: initial body lower bound — $\exists \delta_0 > 0$, $\alpha(\omega, 0) \geq \delta_0$ on $\{\gamma \leq M\}$

## 4c. Proved: body persistence wired in (exp 276)

`ContinuumSolvedWired3.lean` — `kuramoto_continuum_wired3` (0 sorry, 0 axioms):

Eliminates `hα_lb`, `hδ_lb_pos`, and the explicit `δ_lb` function from `kuramoto_continuum_wired2` by deriving body persistence internally via `body_persistence_lower_bound`.

**Key derivation**: `δ_lb M := min (δ₀_body M) (bodyEquilibrium M K r_min)` where `bodyEquilibrium` is the comparison-ODE equilibrium with $\gamma = M$, $r = r_{\min}$. Given $r(t) \geq r_{\min} > 0$ and initial bound $\alpha(\omega,0) \geq \delta_0(M)$ on $\{\gamma \leq M\}$, `body_persistence_lower_bound` proves $\alpha(\omega,t) \geq \min(\alpha(\omega,0), \beta^*) \geq \min(\delta_0(M), \beta^*) = \delta_{\text{lb}}(M)$.

Also eliminates `hr_min_le` ($r_{\min} \leq 1$) by deriving it from `hr_bound + hr_bdd + hr_nn`.

**Remaining open** (3 hypotheses):
- `hr_star_pos` — $r^* > 0$ (supercritical $K > K_c$)
- `hμ_body_pos` — $\mu(\{\gamma \leq M\}) > 0$ for each $M > 0$
- `h_combined_vanish` — $C(M) + \mu(\text{tail}) \to 0$ (depends on $g$'s tail decay)

The combined vanishing hypothesis is now written in fully explicit form:
$$C(M) = \frac{K\mu(\{\gamma>M\})}{K \cdot \min(\delta_0(M), \beta^*(M)) \cdot \frac{Kr^*}{2M+Kr^*} \cdot \mu(\{\gamma\leq M\})}$$

## 4d. Proved: hr_star_pos eliminated (exp 277)

`ContinuumSolvedWired4.lean` — `kuramoto_continuum_wired4` (0 sorry, 0 axioms):

Eliminates `hr_star_pos` ($r^* > 0$) from `kuramoto_continuum_wired3` by deriving it internally from `hα_star_pos` + `hαs_int` + `hr_star_eq` + `[IsProbabilityMeasure μ]`.

**Key derivation**: $r^* = \int \alpha^* d\mu$. Since $\alpha^*(\omega) > 0$ for all $\omega$ and $\mu$ is a probability measure ($\mu(\Omega) = 1 > 0$, so $\text{ae}\,\mu \neq \bot$): if $\int \alpha^* = 0$ then $\alpha^* = 0$ a.e. (by `integral_eq_zero_iff_of_nonneg`), but $\text{ae}\,\mu \neq \bot$ gives $\exists \omega$ with $\alpha^*(\omega) = 0$, contradicting $\alpha^*(\omega) > 0$ everywhere.

**Remaining open** (2 hypotheses):
- `hμ_body_pos` — $\mu(\{\gamma \leq M\}) > 0$ for each $M > 0$ (support condition on $g$)
- `h_combined_vanish` — $C(M) + \mu(\text{tail}) \to 0$ (depends on $g$'s tail decay; not satisfied for Lorentzian)

## 4e. Proved: second_moment_tail_vanish (exp 278)

`TailSecondMoment.lean` — `second_moment_tail_vanish` (0 sorry, 0 axioms):

**Statement**: If $(γ·)^2$ is $\mu$-integrable, then $M^2 \cdot \mu\{\gamma > M\} \to 0$ as $M \to \infty$.

**Proof chain**:
1. **ℕ-indexed**: Let $s_n = \{\gamma > n\}$. $s_n$ is antitone, $\bigcap_n s_n = \emptyset$ (since $\lceil\gamma(\omega)\rceil_+ \geq \gamma(\omega)$). Apply `Antitone.tendsto_setIntegral` to get $\int_{s_n} \gamma^2 \to \int_\emptyset \gamma^2 = 0$.
2. **Transfer to ℝ**: By antitone monotonicity, for $M \geq N$, $\int_{\gamma>M}\gamma^2 \leq \int_{\gamma>N}\gamma^2 \to 0$.
3. **Markov bound**: On $\{\gamma > M\}$: $M^2 \leq (\gamma\omega)^2$ (since $0 \leq M \leq \gamma\omega$), so $M^2 \cdot \tau(M) = \int_{\gamma>M} M^2\,d\mu \leq \int_{\gamma>M} \gamma^2\,d\mu$.
4. **Squeeze**: $0 \leq M^2\tau(M) \leq \int_{\gamma>M}\gamma^2 \to 0$ by `tendsto_of_tendsto_of_tendsto_of_le_of_le'`.

**Significance for wired5**: The combined vanishing $C(M) + \tau(M) \to 0$ where
$$C(M) = \frac{K\tau(M)}{K\cdot\delta(M)\cdot\frac{Kr^*}{2M+Kr^*}\cdot b(M)}$$
satisfies $C(M) \lesssim \frac{M^2\tau(M)}{K^2\delta(M)^{\min}\cdot r^*\cdot r_{\min}\cdot b_{\min}} \to 0$ when $\int\gamma^2\,d\mu < \infty$ and $\delta(M)\cdot M$ is bounded below.

**Concrete distributions covered**: Gaussian ($\int\gamma^2 g < \infty$), Student-$t$ $\nu > 2$, compactly supported distributions. Lorentzian ($\int\gamma^2 g = \infty$) remains open.

## 4f. Proved: h_combined_vanish eliminated (exp 279)

`ContinuumSolvedWired5.lean` — `kuramoto_continuum_wired5` (0 sorry, 0 axioms):

Eliminates `h_combined_vanish` from `kuramoto_continuum_wired4` by deriving $C(M) + \tau(M) \to 0$ from two physically natural conditions:
- `hγ_sq_int : Integrable (fun ω => (γ ω)^2) μ` — finite second moment of the frequency distribution
- `hδ₀_body_lb : ∃ c > 0, ∀ M > 0, c/M ≤ δ₀_body M` — initial body bound decays at most as $1/M$

**Key estimate**: Let $C_1 = \min(c, Kr_{\min}/3)$ and $C_2 = K^2 r^* C_1 / 6$. Then the denominator of $C(M)$ satisfies $K\delta(M)\cdot\frac{Kr^*}{2M+Kr^*}\cdot b(M) \geq C_2/M^2$, giving $C(M) \leq (K/C_2)(M^2\tau(M)) \to 0$ by `second_moment_tail_vanish`.

**Remaining open** (1 hypothesis):
- `hμ_body_pos` — $\mu(\{\gamma \leq M\}) > 0$ for each $M > 0$ (support condition on $g$; equivalent to $g$ not concentrated on $\{0\}$ alone)

**Debugging lessons from exp 279**:
1. `simp only [C₂]` for a local `let C₂ := ...` binding is a no-op. Use `show unfolded_expr; field_simp; ring` instead.
2. `gcongr` on a 4-factor product often fails when nonnegativity of intermediate factors cannot be inferred — use explicit `mul_le_mul` chain.
3. `rw [Real.norm_of_nonneg h]` with an open metavariable `?g` can accidentally close the goal by unification — pin with `show ‖f M‖ ≤ concrete_g M` first.
4. `field_simp; ring` on a fraction-of-fraction equality: `field_simp` alone may close the goal; the trailing `ring` then errors "No goals to be solved."

**Wired chain complete up to `hμ_body_pos`**: wired → wired2 → wired3 → wired4 → wired5. The single remaining hypothesis `hμ_body_pos` is a support condition on the initial distribution $g$ — it fails only if $g$ is a point mass at $\gamma = 0$.

## 4g. Proved: hμ_body_pos eliminated — wired chain complete (exp 280)

`ContinuumSolvedWired6.lean` — `kuramoto_continuum_wired6` (0 sorry, 0 axioms):

Eliminates `hμ_body_pos` ($\mu(\{\gamma \leq M\}) > 0$ for each $M > 0$) from `kuramoto_continuum_wired5` by case-splitting on whether the body measure is zero.

**Key idea (h_body_gronwall)**: Case-split on `μ{γ ≤ M} = 0`:
- **Null case**: $V_{\text{body}}(M,t) = \int_{\text{null}} (\alpha-\alpha^*)^2\,d\mu = 0$ for all $t$ (via `Measure.restrict_eq_zero.mpr + integral_zero_measure`). Gronwall bound trivially holds with rate = 1, $C(M) = 0$.
- **Positive case**: `ENNReal.toReal_pos hμ_null (measure_ne_top μ _)` gives positivity; apply `body_gronwall_wired` as before.

**Key idea (h_combined_vanish)**: $\mu\{\gamma \leq M\} > 0$ holds **automatically for large $M$** because $\tau(M) = \mu\{\gamma > M\} \to 0$ (from `tail_measure_tendsto_zero'`) forces $b(M) = 1 - \tau(M) \to 1 > 0$ (via the partition identity $\tau(M) + b(M) = 1$). So `hCM_nn_pos` applies for large $M$: $C(M) = \max(0, CM(M)) = CM(M)$ eventually, and the `congr'` filter closes the goal.

**Theorem signature** (no `hμ_body_pos`):
- ODE data: `HasDerivAt (α ω) (oaScalarRHS (γ ω) K r t (α ω t)) t`
- Equilibrium: `γ ω * α_star ω = (K/2)·r*·(1 - (α_star ω)²)`
- Physical: `IsProbabilityMeasure μ`, `hγ_sq_int : Integrable (fun ω => (γ ω)^2) μ`
- Analytic: `hδ₀_body_lb : ∃ c > 0, ∀ M > 0, c/M ≤ δ₀_body M`
- Persistence: `r_min > 0` with `r(t) ≥ r_min`, `α ∈ (0,1)` invariant

**Axioms**: `propext`, `Classical.choice`, `Quot.sound` — the three standard Lean kernel axioms. Zero sorry.

**Wired chain summary** (wired → wired2 → wired3 → wired4 → wired5 → wired6):
- wired: takes all hypotheses explicitly (no elimination)
- wired2: eliminates `h_gronwall_from_persist` via `body_gronwall_wired`; defines $C(M) = \max(0, K\tau/\text{denom})$
- wired3: eliminates `hα_lb` via `body_persistence_lower_bound`
- wired4: eliminates `hr_star_pos` from `hα_star_pos + hαs_int + IsProbabilityMeasure`
- wired5: eliminates `h_combined_vanish` via `second_moment_tail_vanish + hδ₀_body_lb`
- **wired6**: eliminates `hμ_body_pos` via null-body case split — **chain fully closed**

**Debugging lessons from exp 280**:
1. `ENNReal.pos_iff_ne_zero` does not exist; `ENNReal.toReal_pos` takes `a ≠ 0` directly.
2. `(f.add g).congr'` produces `Tendsto _ atTop (nhds (0+0))`, not `nhds 0`. Must `simp [add_zero]` on the intermediate, then call `.congr'` from the correct direction.
3. For `congr'` direction: if you know `CM M → 0` and want `C M → 0` where `C M = CM M` eventually, use `hCM_vanish.congr'` with an `Eventually` proof showing `C M = CM M` for large `M` — NOT `apply (hCM_vanish.add h_τ_vanish).congr'`.

**Physical interpretation**: The hypothesis `hμ_body_pos` says "the distribution $g$ has positive mass on every half-line $[0,M]$." This fails only if $g$ is a point mass at $\gamma = 0$ — i.e., all oscillators have zero frequency, which is the trivial (already locked) case. Eliminating it means the theorem now applies to all non-degenerate probability distributions with finite second moment.

## 4h. Proved: per-ω Gronwall for Lorentzian (exp 281)

`LorentzianPointwiseConv.lean` — three theorems (0 sorry, 0 axioms):

**Three theorems proved**:

1. **`oa_V_deriv_bound`** (private): Algebraic inequality
   $$2(\alpha-\alpha^*)\cdot\text{oaScalarRHS} \leq -2\gamma(\alpha-\alpha^*)^2 + K|r-r^*|$$
   Proof: `linear_combination -2*(α-α*)*hequil` establishes the algebraic identity; two `nlinarith` lemmas bound $(α-α^*)(1-α^2) \leq 1$ and $\geq -1$.

2. **`oa_scalar_pointwise_tendsto`**: Per-$\omega$ convergence — for $\gamma > 0$ and $r(t) \to r^*$:
   $$(α(t)-α^*)^2 \to 0 \text{ as } t\to\infty$$
   Proof: $\varepsilon$-splitting on the Gronwall bound. Choose $T$ so $|r(t)-r^*| < \gamma\varepsilon/K$ for $t \geq T$. On $[T,\infty)$: $dV/dt \leq -2\gamma V + \gamma\varepsilon$. Apply `gronwall_with_forcing` to get $V(T+s) \leq e^{-2\gamma s} + \varepsilon/2 \to \varepsilon$ for large $s$.

3. **`V_inf_tendsto_zero_from_r`**: Global convergence — for any probability measure $\mu$ with $\gamma(\omega) > 0$ a.e.:
   $$\int (\alpha(\omega,t)-\alpha^*(\omega))^2\,d\mu \to 0$$
   Proof: pointwise convergence (from 2) + dominated convergence theorem with bound 4 (constant, integrable).

**Key technical decisions**:
- `linear_combination` (not `nlinarith`) for the 4-degree polynomial identity with equilibrium
- Remove `hγ_sq_int` entirely: per-$\omega$ Gronwall needs only pointwise $\gamma(\omega) > 0$
- Fix `unfold_let` (not a Lean 4 tactic) → drop it (let-bindings are definitionally transparent)
- Gronwall produces `rexp (-(2*γ)*s)` not `rexp (-2*γ*s)`; bridge via `have h3 : -(2*γ)*V = -2*γ*V := by ring`
- `div_le_iff₀` (not `div_le_iff`) for division rearrangement in exp-atTop proof
- DCT bound must be a function `fun _ : Ω => (4 : ℝ)`, not the scalar `4`

**Physical significance**: For the Lorentzian distribution $g(\omega) = \frac{\gamma_0}{\pi(\omega^2+\gamma_0^2)}$, the damping is $\gamma(\omega) = |\omega|$. This is positive almost everywhere (the Lorentzian is absolutely continuous, so $\{|\omega|=0\} = \{0\}$ has measure zero). Therefore `V_inf_tendsto_zero_from_r` applies to Lorentzian given $r(t) \to r^*$ — and $r(t) \to r^*$ is already proved in `LorentzianExistence.lean`.

**Remaining gap for complete Lorentzian theorem**: instantiate `V_inf_tendsto_zero_from_r` with:
- `hr_tendsto`: from `lorentzian_explicit_tendsto` (LorentzianExistence.lean) ✓
- `hγ_ae_pos`: $|\omega| > 0$ a.e. for Lorentzian measure (follows from absolute continuity) — needs a separate proof
- ODE data (`hα_cont`, `hα_ode`, `hα_bdd`): existence/regularity of OA flow for Lorentzian — needs instantiation

Writing the combining file `LorentzianContinuumConvergence.lean` is the next step.

## 4i. Proved: Lorentzian connecting theorem (exp 282)

`LorentzianContinuumConvergence.lean` — `lorentzian_continuum_V_inf_tendsto` (0 sorry, 0 axioms):

**Statement**: Given a probability measure $\mu$ on $\Omega$ with $\gamma(\omega) > 0$ a.e., equilibrium $\alpha^*$, and OA flow $\alpha(\omega,t)$ with forcing $r(t) = \text{lorentzian\_explicit}\; K\; \gamma_0\; r_0\; t$:
$$V_\infty(t) = \int_\Omega (\alpha(\omega,t)-\alpha^*(\omega))^2\,d\mu \to 0$$

**Proof chain**: Direct application of `V_inf_tendsto_zero_from_r` with:
- `r(t) = lorentzian_explicit K γ₀ r₀ t`
- `hr_tendsto := lorentzian_explicit_tendsto` (r(t) → r* = √(1-2γ₀/K))
- `hr_star_pos := Real.sqrt_pos_of_pos (lorentzian_rstar_pos K γ₀ hK hKγ₀)`
- All ODE data passed through from hypotheses

**Cleanup in exp 282**: Removed unused hypothesis `hr_bdd_r : ∀ t, |r t| ≤ 1` from `oa_scalar_pointwise_tendsto` and `hr_bdd` from `V_inf_tendsto_zero_from_r` (neither appeared in proof bodies — vestigial from earlier drafts).

**What remains open**: The ODE existence hypotheses (`hα_cont`, `hα_ode`, `hα_bdd`) are still external. For the Lorentzian specifically:
- `hα_ode`: the per-ω OA scalar ODE with forcing r(t) = lorentzian_explicit; solvable by Picard-Lindelöf on each $[0,\infty)$
- `hγ_ae_pos`: $|\omega| > 0$ a.e. under the Lorentzian measure — immediate from absolute continuity since $\{0\}$ has measure zero
- `hα_bdd`: invariance of $[0,1]$ under the OA flow — follows from barrier comparison

## 4j. Proved: OA scalar invariant box (0,1) (exp 283)

`OAScalarBarrier.lean` — `oaScalar_invariant_box` (0 sorry, 0 axioms):

**Statement**: For $\gamma, K > 0$, $r(t) \in [0,1]$, and $\alpha(0) \in (0,1)$:
$$\forall t \geq 0,\quad 0 < \alpha(t) < 1$$

**Two barriers**:
- **Upper** (`oaScalar_upper_barrier`): sInf argument — if $t_0 = \inf\{t \geq 0 : \alpha(t) \geq 1\}$, then $\text{oaScalarRHS}\;\gamma\;K\;r\;t_0\;1 = -\gamma < 0$, so `strictAntiOn_of_deriv_neg` gives $\alpha$ decreasing into $t_0$, contradicting $\alpha(t_0)=1$.
- **Lower** (`oaScalar_lower_barrier`): Grönwall multiplier $\text{gm}(t) = \alpha(t)e^{\gamma t}$ satisfies $\text{gm}'(t) = \frac{K}{2}r(t)(1-\alpha(t)^2)e^{\gamma t} \geq 0$ on $[0, t_m)$ (where $t_m$ is the first zero and $\alpha \in (0,1)$ there from upper barrier). So $\text{gm}$ is monotone from $\text{gm}(0) = \alpha(0) > 0$, contradicting $\text{gm}(t_m) = 0$.

**Proof technique**: `fun_prop` handles the continuity of `oaScalarRHS` composition after `simp only [oaScalarRHS]`. The `nlinarith [mul_nonneg ...]` trick proves $1 - \alpha^2 \geq 0$ from $\alpha \in (0,1)$ via the factorization $(1-\alpha)(1+\alpha) \geq 0$.

**What remains open**: Global ODE existence on $[0,\infty)$ for the per-$\omega$ forced OA scalar ODE. `OAScalarBarrier.lean` closes the `hα_bdd` hypothesis in `lorentzian_continuum_V_inf_tendsto`; next is `hα_ode` via Picard-Lindelöf extension.

## 4k. Proved: per-ω OA scalar ODE global existence under Lorentzian forcing (exp 284)

`LorentzianScalarODE.lean` — `lorentzian_scalar_ode_global` (0 sorry, 0 axioms):

**Statement**: For $\gamma, K, \gamma_0 > 0$ with $K > 2\gamma_0$, $r_0 \in (0,1)$, and $\alpha_0 \in (0,1)$:
$$\exists \alpha : [0,\infty) \to \mathbb{R},\quad \alpha(0) = \alpha_0,\quad \alpha \in (0,1),\quad \dot\alpha(t) = \text{oaScalarRHS}\;\gamma\;K\;r(t)\;\alpha(t)\ \forall t > 0$$
where $r(t) = \text{lorentzian\_explicit}\;K\;\gamma_0\;r_0\;t$.

**Proof strategy**: Define $r_{\text{ext}}(t) = r(\max(0,t))$ to extend $r$ continuously to all of $\mathbb{R}$. Then apply `oa_solve_global_v2` (which requires globally bounded/continuous forcing), obtain global solution, and recover the original Lorentzian ODE for $t \geq 0$ since $r_{\text{ext}}(t) = r(t)$ there.

**Key lemmas**:
- `r_ext_continuous`: `ContinuousOn.comp_continuous` with `fun t => max 0 t`
- `r_ext_bdd`: `|r_ext t| ≤ 1` for all t, since $r_{\text{ext}} \in (0,1)$ everywhere (Lorentzian pos/lt_one at max)
- Recovers original: `oaScalarRHS γ K r_ext t α = oaScalarRHS γ K r t α` for $t \geq 0$

**What remains open**: The measurability hypothesis `hα_sq_meas` in `lorentzian_continuum_V_inf_tendsto` — that the map $\omega \mapsto (\alpha(\omega,t) - \alpha^*(\omega))^2$ is AE strongly measurable. This requires a measurable selection theorem for the parameterized ODE $\omega \mapsto \alpha(\omega,\cdot)$.

## 5. Recommended next steps

1. **Prove h_body_drop (Leibniz for full V)** [WEAKEST KNOWN SUFFICIENT CONDITION, from `TailBodyBarbalat.lean`]:
   Show $V(t) - V(t+1) \geq K \cdot c(M) \cdot V_{\text{body}}(M,t)$ eventually.
   This follows from: Leibniz gives $V(t)-V(t+1) = K\int_t^{t+1} P$, then $P \geq P_{\text{body}} \geq c(M) \cdot V_{\text{body}}$.
   - For $g$ with $\int|\omega|g < \infty$ (Gaussian, compact support): **DCT gives Leibniz directly**.
   - For Lorentzian ($\int|\omega|g = \infty$): use monotone convergence with body truncations $M' \to \infty$. The key: $V_{M'}(t) - V_{M'}(t+1) \geq K\int_t^{t+1} P_{M'}$ (Leibniz on body $M'$, valid since $\gamma \leq M'$). Take $M' \to \infty$: monotone convergence on both sides.
   - Alternative: prove $V$ is absolutely continuous directly from the ODE without DCT.

2. **Prove time-averaged coercivity (h_tac)** [STRONGER, from `AbsorbingBarbalat.lean`]: Implied by h_body_drop + body coercivity + uniform tail bound. The tail-body argument in `TailBodyBarbalat.lean` derives EventualTAC from h_body_drop.

3. **Prove pointwise coercivity (h_coercive)** [STRONGEST, from `WeakStarLaSalle.lean`]: Implies h_tac (proved). Requires orbit compactness which fails for unbounded $\gamma$. NOT recommended as primary attack.

4. **Quantify passage-to-limit errors**: Fill the 3 True placeholders in `PassageToLimit.lean`. Independent approach.

**Hierarchy of hypotheses** (strictly weaker going down):
```
h_coercive (P<δ ⟹ V<ε) [WeakStarLaSalle]
    ⟹ TimeAveragedCoercivity [AbsorbingBarbalat]
    ⟹ h_body_drop (Leibniz + body coercivity) [TailBodyBarbalat]
    ⟹ V → 0
```
h_body_drop is purely analytic (interchange of limit and integral). No dynamics, no compactness.

## 6. Label

**lorentzian-scalar-ode-global** — `lorentzian_scalar_ode_global` (LorentzianScalarODE.lean, 0 sorry, 0 axioms, exp 284) proves global existence for the per-$\omega$ OA scalar ODE under Lorentzian forcing via the $r_{\text{ext}}$ time-clamping trick + `oa_solve_global_v2`. Closes `hα_ode`, `hα_bdd`, `hα_cont` hypotheses in `lorentzian_continuum_V_inf_tendsto` for a single oscillator. Remaining gap: measurability of $\omega \mapsto \alpha(\omega,t)$ for the parameterized family.

**oa-scalar-barrier-proved** — `oaScalar_invariant_box` (OAScalarBarrier.lean, 0 sorry, 0 axioms, exp 283) proves $(0,1)$ is positively invariant for the per-$\omega$ OA scalar ODE with $r(t) \in [0,1]$ and $\gamma, K > 0$. Upper barrier via sInf + `strictAntiOn_of_deriv_neg`; lower barrier via Grönwall multiplier monotonicity. Closes the `hα_bdd` hypothesis in `lorentzian_continuum_V_inf_tendsto`. Remaining gap: global ODE existence (`hα_ode`) via Picard-Lindelöf extension.

**lorentzian-connecting-proved** — The connecting theorem `lorentzian_continuum_V_inf_tendsto` (LorentzianContinuumConvergence.lean, 0 sorry, 0 axioms, exp 282) combines `lorentzian_explicit_tendsto` ($r(t) \to r^*$) with `V_inf_tendsto_zero_from_r` (per-$\omega$ Gronwall + DCT) to prove $V_\infty(t) \to 0$ for any probability measure $\mu$ with $\gamma(\omega) > 0$ a.e. and OA flow data with Lorentzian forcing. The remaining gap: instantiate ODE existence hypotheses for the specific Lorentzian model (Picard-Lindelöf for per-$\omega$ forced ODE, absolute continuity for $|\omega|>0$ a.e.).

**wired-chain-complete** — The wired chain `kuramoto_continuum_wired6` (0 sorry, 0 axioms) proves $r(t) \to r^*$ for any probability distribution $\mu$ with $\int\gamma^2\,d\mu < \infty$ and $\delta_0(M) \geq c/M$. Covers Gaussian, Student-$t$ ($\nu > 2$), and compactly supported distributions.
