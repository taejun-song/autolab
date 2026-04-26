---
type: source-summary
title: "Kuehn & Landi (2025) — The Mean-Field Ott-Antonsen Manifold is an Unstable Manifold in the Continuum Limit"
created: 2026-04-18
updated: 2026-04-18
sources: []
tags: [dynamical-systems, synchronization, dimension-reduction]
aliases: ["Kuehn-Landi 2025", "OA unstable manifold"]
source_file: "../raw/papers/2511.03833.pdf"
source_kind: pdf
source_date: 2025-11-07
---

# Kuehn & Landi (2025) — The Mean-Field Ott-Antonsen Manifold is an Unstable Manifold in the Continuum Limit

Proves that the OA manifold of the mean-field limit (MFL) is the direct dynamical analogue of the **unstable manifold** of the homogeneous steady state in the continuum limit (CL). This provides a structural explanation for why the OA manifold captures the macroscopic synchronization dynamics: it IS the unstable manifold along which perturbations of incoherence grow.

## Key result

The paper establishes a dynamical correspondence between two different PDE limits of the Kuramoto particle system:
- The **mean-field limit** (MFL): the Vlasov-type transport PDE for the distribution $\mu_t$
- The **continuum limit** (CL): the integro-differential equation for pointwise particle trajectories $x(t,\xi)$

The OA manifold, originally defined as an invariant submanifold of the MFL with Poisson-kernel densities, is shown to equal the unstable manifold $W^u$ of the homogeneous steady state in the CL. This is a STRUCTURAL identification, not just an analogy.

## Implications for the stability problem

**This paper DOES NOT say the OA manifold is "unstable" in the sense of repelling nearby trajectories.** It says the OA manifold IS the unstable manifold of INCOHERENCE — meaning it's the set of states that grow AWAY from incoherence when $K > K_c$. This is consistent with (and explains why) trajectories starting near incoherence approach the OA manifold: they are attracted to the unstable manifold, which then carries them toward the PLS.

For the [[hyperbolic-lyapunov-attack-on-kuramoto-stability|precompactness question]]: this paper implies that the OA manifold is NOT a global attractor in the traditional sense (as the Dietert-Fernandez Prop 4.1 shows for the MFL). The CL dynamics may leave the OA manifold, but the macroscopic observable $r(t)$ is still governed by the OA reduction for analytic $g$.

## Pages read

pp 1–3 (abstract, introduction, mean-field limit, continuum limit, Kuramoto model, OA manifold review).

## Cross-links

- [[ott-antonsen-ansatz]] — the OA manifold is structurally identified as the unstable manifold of incoherence
- [[kuramoto-stability-problem]] — the unstable manifold interpretation explains why the OA reduction captures synchronization dynamics
- [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] — affects the precompactness argument: OA is NOT a global attractor for the CL, but IS for the MFL (by Dietert-Fernandez)
