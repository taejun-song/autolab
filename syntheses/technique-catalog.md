---
type: synthesis
title: "Complete Technique Catalog for Kuramoto Stability"
created: 2026-05-16
updated: 2026-05-16
sources:
  - "[[dietert-2016-thesis]]"
  - "[[dietert-fernandez-2018-asymptotic-stability]]"
  - "[[ott-antonsen-2008-low-dimensional]]"
  - "[[chiba-2015-kuramoto-conjecture]]"
  - "[[kuehn-landi-2025-oa-unstable-manifold]]"
  - "[[cestnik-martens-2024-riccati-array]]"
  - "[[continuum-stability-debate]]"
tags:
  - techniques
  - stability
  - catalog
  - subproblems
aliases:
  - technique-catalog
---

# Complete Technique Catalog for Kuramoto Stability

75 techniques from 30+ papers, mapped to subproblems and Lean status.

## The 4 remaining subproblems to close the full theorem

| Subproblem | What's needed | Best technique | Lean infrastructure needed |
|---|---|---|---|
| **SP1: V→0 for complex OA** | Landau damping or body persistence | Volterra trapping (#72) | Volterra integral equations |
| **SP2: OA manifold attractivity** | Transversal decay | Dietert-Fernandez Prop 4.1 (#57) | Analytic function spaces |
| **SP3: Global stability (no basin)** | Instability of incoherence | Free-rotation amplification (#70) + Ψ dichotomy (#54) | Already proved (0 sorry) |
| **SP4: Sobolev conditions formalized** | Weighted Sobolev spaces | Fourier analysis + p_b norms (#16) | Not in Mathlib |

## Techniques most likely to close SP1 (V→0) without Landau damping

| # | Technique | Why it might work | Difficulty |
|---|---|---|---|
| 72 | Volterra trapping | Scalar r convergence → full V convergence. Already argued (0 sorry, 3 axioms) | Medium — needs Volterra equation theory |
| 40 | Cooperative monotone (n-pole) | Each finite n converges (PROVED). Passage to limit (#69) | Medium — needs uniform rates |
| 52 | Tail-body split | Body antitone (bounded ω → real pair bound). Tail vanishes. PROVED for real case | Low — but pair bound fails for complex z |
| 22 | Hypocoercivity | Modified energy H = V + ε⟨Af,f⟩ could give exponential decay | High — mean-field nonlinearity blocks standard DMS |
| 44 | Łojasiewicz-Simon | If V is analytic near PLS → gradient-like convergence | High — OA is not gradient flow |

## Techniques for closing SP2 (OA attractivity) without axiom

| # | Technique | Lean needs |
|---|---|---|
| 21 | Paley-Wiener | Complex analysis, strip analyticity |
| 47 | Volterra integral equations | Volterra operator theory |
| 51 | Montel's theorem | Normal families, complex analysis |
| 18 | Rigged Hilbert spaces | Gelfand triplets (very advanced) |

## What's already fully machine-checked (0 sorry, 0 axioms)

| Technique | Lean file | What it proves |
|---|---|---|
| L² Lyapunov (#67) | L2Lyapunov.lean | Pair bound for real scalar |
| Rotation cancellation (#63) | ComplexOAPairBound.lean | Re(w̄·(-iω·w)) = 0 |
| Dietert energy (#46) | ComplexOAEnergy.lean | dΨ/dt = K|η|² |
| Symmetry preservation (#23) | ComplexOASymmetry.lean | z(ω) = conj(z(-ω)) |
| Cooperative monotone (#40) | RationalOA.lean | n-pole global convergence |
| Tail-body split (#52) | ComplexOAVZero.lean | V_body + V_tail → 0 |
| Gronwall bootstrap | GronwallBootstrap.lean | V'≤-rate·V → V→0 |
| Cauchy-Schwarz | ComplexOAEndToEnd.lean | V→0 ⟹ Re(η)→r* |
| Self-consistency (#65) | SelfConsistencyFixedPoint.lean | r* unique for K > Kc |
| Barbalat (#5) | BarbalatLemma.lean | Monotone bounded → convergence |

## Recommended attack sequence

1. **Volterra trapping (#72)** for SP1: reduce V→0 to scalar δr convergence. Most of the infrastructure exists. Needs: Volterra integral operator in Lean.

2. **Passage to limit (#69)** for SP1: bypass complex pair bound via n-pole. Needs: uniform convergence rates (Perron-Frobenius #68, already argued).

3. **Paley-Wiener (#21)** for SP2: strip analyticity ↔ exponential decay. Needs: complex analysis infrastructure in Mathlib.

4. **Free-rotation amplification (#70)** for SP3: already proved. Shows incoherence unstable. Combined with Ψ dichotomy (#54) gives global convergence (modulo SP1).
