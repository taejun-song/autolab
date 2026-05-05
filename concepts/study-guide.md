---
type: concept
title: "Study Guide: Kuramoto Global Stability Proof"
created: 2026-05-05
updated: 2026-05-05
sources:
  - "[[kuramoto-stability-problem]]"
  - "[[strogatz-2000-from-kuramoto-to-crawford]]"
  - "[[ott-antonsen-2008-low-dimensional]]"
  - "[[dietert-2016-stability-bifurcation]]"
  - "[[dietert-fernandez-2018-asymptotic-stability]]"
tags:
  - synchronization
  - dynamical-systems
  - stability
  - research-plan
aliases:
  - study-guide
---

# Study Guide: Kuramoto Global Stability Proof

A structured reading path for understanding the machine-checked proof of global stability of the Kuramoto partially locked state.

## Layer 1: Mathematical Foundations

These are prerequisites — skip what you already know.

### Ordinary Differential Equations
- **Picard-Lindelöf theorem**: local existence and uniqueness for Lipschitz ODEs
- **Gronwall inequality**: comparison principle for differential inequalities
- **Invariant regions**: if f(boundary) points inward, solutions stay inside
- **Global existence**: bounded solutions on compact invariant sets exist for all time
- **Reference**: Hartman, *Ordinary Differential Equations*, Ch. II

### Lyapunov Stability Theory
- **Lyapunov functions**: V ≥ 0 with dV/dt ≤ 0 implies stability
- **LaSalle invariance principle**: V antitone → trajectory approaches largest invariant set in {dV/dt = 0}
- **Barbalat's lemma**: uniformly continuous + integrable → converges to 0
- **Reference**: Khalil, *Nonlinear Systems*, Ch. 4

### Measure Theory and Integration
- **Dominated convergence theorem**: uniform bound + pointwise convergence → integral convergence
- **Fubini's theorem**: iterated integrals equal double integrals (for product measures)
- **Leibniz rule**: d/dt ∫f(ω,t)dμ = ∫(∂f/∂t)dμ under dominated convergence
- **Cauchy-Schwarz for integrals**: (∫fg)² ≤ (∫f²)(∫g²)
- **Reference**: [[brezis-2011-functional-analysis-sobolev-pdes]], Ch. 4

### Fixed-Point Theorems
- **Banach contraction mapping**: T contractive on complete metric space → unique fixed point
- **Application**: self-consistent mean-field equations
- **Reference**: Any functional analysis text (Brezis Ch. 5, or Mathlib's `ContractingWith.exists_fixedPoint'`)

## Layer 2: The Kuramoto Model

### The basic model (read first)
- **N coupled oscillators**: dθ_i/dt = ω_i + (K/N)Σ sin(θ_j - θ_i)
- **Order parameter**: r·e^{iψ} = (1/N)Σ e^{iθ_j}, measures phase coherence
- **Phase transition**: for K > K_c = 2/(πg(0)), partial synchronization emerges
- **Reference**: [[kuramoto-1975-self-entrainment]] (3 pages), then [[strogatz-2000-from-kuramoto-to-crawford]] (20 pages, excellent survey)

### The Ott-Antonsen reduction
- **Continuum limit**: N → ∞, density ρ(θ,ω,t) evolves via continuity equation
- **OA ansatz**: parameterize density by α(ω,t) ∈ D̄ (unit disk)
- **Reduced equation**: ∂ₜα = -iωα + (K/2)(r - r̄α²) with r = ∫αg dω
- **Why it works**: the OA submanifold is invariant and exponentially attracting
- **Reference**: [[ott-antonsen-2008-low-dimensional]]

### Locked vs drifting oscillators
- **Locked** (|ω| < Kr*): α*(ω) close to 1, oscillator rotates at mean frequency
- **Drifting** (|ω| > Kr*): |α*(ω)| < 1, oscillator has nonzero relative frequency
- **Key point**: α*(ω) → 0 as |ω| → ∞. No uniform lower bound on α* globally.
- **The PLS profile**: α*(ω) = (Kr* - √((Kr*)² - ω²))/(iω) for locked; explicit formula for drifting
- **Reference**: [[dietert-2016-stability-bifurcation]], §1

## Layer 3: The Stability Problem

### What is the open problem?
- **Statement**: For K > K_c and r(0) > 0, does r(t) → r* as t → ∞?
- **Known before this work**: Local stability (near PLS) proved by [[dietert-2016-stability-bifurcation]]. Global stability was the 50-year open problem.
- **Why it's hard**: The continuum OA system is infinite-dimensional. No obvious global Lyapunov function was known. The spectrum is continuous (no spectral gap in the usual sense).
- **Reference**: [[kuramoto-stability-problem]]

### Linear stability and Landau damping
- **Linearized operator**: has continuous spectrum on imaginary axis (neutral modes)
- **Landau damping**: perturbations decay via phase mixing, not eigenvalue damping
- **Analogy**: Vlasov-Poisson plasma physics (Mouhot-Villani 2011)
- **Reference**: [[landau-damping]], [[chiba-2015-kuramoto-conjecture]]

### The energy identity (Dietert's key tool)
- **Ψ functional**: Ψ(t) = ∫g(ω)(-log(1-|α|²))dω
- **Growth**: dΨ/dt = K|r|² ≥ 0 (non-decreasing "energy")
- **Progressive locking**: Ψ → ∞ means oscillators progressively lock
- **Reference**: [[dietert-2016-stability-bifurcation]], §3

### Volterra trapping (Dietert's local → global bridge)
- **Perturbation equation**: δr satisfies a Volterra integral equation
- **Kernel decay**: L(t) decays exponentially for analytic g
- **Key insight**: at late times t₀, the past-history integral has already decayed, so the orbit is in a "fresh start" near r*
- **Reference**: [[dietert-2016-stability-bifurcation]], Theorem 2.3; [[dietert-fernandez-2018-asymptotic-stability]]

## Layer 4: Our Proof Strategy

### The L² Lyapunov function (for n-pole / bounded γ)
- **Definition**: V(t) = Σ c_k (α_k - α*_k)²
- **Key theorem**: dV/dt ≤ 0 (pair bound — algebraic identity)
- **Exponential rate**: dV/dt ≤ -K·c_min·δ·δ*·V on the locked region
- **Lean file**: `L2Lyapunov.lean`, `UniformRate.lean`
- **Wiki**: [[subproblem-decomposition]]

### The pair bound (why dV/dt ≤ 0)
- **Structure**: dV/dt = K(DS - r*Q) where DS, Q are bilinear forms in (α_k - α*_k)
- **Proof**: DS ≤ r*Q by AM-GM + the equilibrium condition on α*
- **Lean file**: `PairCoercivity.lean`, `ContinuumLyapunov.lean`

### The tail-body split (for the continuum)
- **Problem**: unbounded γ(ω) = |ω| breaks Leibniz and uniform persistence
- **Solution**: split r = r_body + r_tail where body = ∫_{|ω|<M} and tail = ∫_{|ω|≥M}
- **Tail bound**: |r_tail| ≤ ∫_{|ω|≥M} g dω = ε(M) → 0
- **Body**: on [-M,M], γ ≤ M (bounded!), α* ≥ δ*(M) > 0 (locked region)
- **Apply existing machinery** to the body, control the tail by integrability
- **Lean file**: `TailBodySplit.lean`, `GeneralizedTailBody.lean`
- **Reference**: Paper §3 (original version)

### Coercive convergence (V → 0 without rate assumption)
- **V antitone**: from dV/dt ≤ 0 (pair bound)
- **V → L ≥ 0**: antitone bounded sequence converges
- **L = 0**: by contradiction — if L > 0, persistence gives coercive drops, contradicting V → L
- **r → r***: Cauchy-Schwarz: (r-r*)² ≤ V → 0
- **Lean file**: `ContinuumGlobalStability.lean`, `AntitoneConvergence.lean`

### The Lorentzian special case (fully end-to-end)
- **Why special**: Lorentzian g is 1-pole rational → OA reduces to SCALAR ODE ṙ = (K/2-γ)r - (K/2)r³
- **Bernoulli equation**: explicit solution r(t) = √(w(t)⁻¹)
- **Monotone convergence**: r non-decreasing if r₀ < r*, non-increasing if r₀ > r*
- **No tail/body split needed**: there are no drifting oscillators in the scalar reduction
- **Lean file**: `LorentzianExistence.lean`, `LorentzianFromODE.lean`

## Layer 5: The Remaining Continuum Gap

### What's proved
- **Lorentzian (1-pole)**: fully proved, 0 sorry, 0 axioms, end-to-end
- **N-pole (any finite n)**: fully proved, 0 sorry, 0 axioms
- **Bounded-γ continuum**: proved conditional on persistence (which IS valid for locked oscillators)

### What's open for the standard continuum
- **Unbounded γ**: the standard model has γ(ω) = |ω| → ∞. Leibniz needs truncation to [-M,M].
- **Tail control**: the tail-body split handles this mathematically, but the Lean formalization of the ε/3 argument (body converges + tail small + PLS continuity) has placeholder structure fields.
- **The correct theorem structure**: should take g integrable on ℝ (not bounded γ) and derive stability via truncation + body convergence + tail estimate.

### What to read for the gap
- [[dietert-fernandez-2018-asymptotic-stability]] — how professionals handle locked/drifting
- [[faou-rousset-2014-vlasov-hmf]] — Sobolev regularity approach (alternative)
- [[mouhot-villani-2011-landau-damping]] — the Vlasov analogue (phase mixing without dissipation)

## Recommended Reading Order

1. **[[strogatz-2000-from-kuramoto-to-crawford]]** — 20 pages, builds intuition for the whole problem
2. **[[ott-antonsen-2008-low-dimensional]]** — 8 pages, the dimensional reduction
3. **[[brezis-2011-functional-analysis-sobolev-pdes]]** Ch. 4 — dominated convergence, Leibniz rule
4. **[[dietert-2016-stability-bifurcation]]** §§1-3 — energy identity, kernel decay (the tools)
5. **[[dietert-fernandez-2018-asymptotic-stability]]** — the state of the art before our work
6. **Our paper** (`raw/papers/kuramoto-global-stability-proof-v2.tex`) — the proof chain
7. **Lean files**: `MainTheorem.lean` → `L2Lyapunov.lean` → `LorentzianExistence.lean` → `GeneralGMainTheorem.lean`

## Key Equations to Internalize

The OA equation (the system we study):
$$\dot{\alpha}(\omega,t) = -i\omega\alpha + \frac{K}{2}(r - \bar{r}\alpha^2), \quad r = \int \alpha(\omega,t)g(\omega)d\omega$$

The Lyapunov function:
$$V(t) = \int |\alpha(\omega,t) - \alpha^*(\omega)|^2 g(\omega)d\omega$$

The self-consistency equation (determines r*):
$$r^* = \Phi(r^*) = \int_{|\omega|<Kr^*} g(\omega)\sqrt{1-(\omega/(Kr^*))^2}\,d\omega$$

The energy identity:
$$\frac{d\Psi}{dt} = K|r|^2 \geq 0$$

The pair bound (key algebraic fact):
$$\frac{dV}{dt} \leq 0$$
