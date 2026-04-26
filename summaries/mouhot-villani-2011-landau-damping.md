---
type: source-summary
title: "Mouhot & Villani (2011) — On Landau Damping"
created: 2026-04-18
updated: 2026-04-18
sources: []
tags: [pde, kinetic-theory, plasma-physics, landau-damping, functional-analysis]
aliases: []
source_file: "../raw/papers/mouhot-villani-2011-landau-damping.pdf"
source_kind: pdf
source_date: 2011-01-01
---

# On Landau Damping

Proves nonlinear Landau damping for the Vlasov-Poisson equation in analytic regularity — the landmark result showing convergence to equilibrium without dissipation, purely through phase mixing.

## Key Results

- **180+ pages**, published in *Acta Mathematica*. Establishes exponential Landau damping for the collisionless Vlasov equation (no diffusion/collision operator).
- Uses a **Newton iteration scheme** (Nash–Moser type) in analytic function spaces to handle the loss of regularity inherent in the nonlinear problem.
- **Phase mixing** transfers regularity between kinetic and spatial variables: the distribution function develops finer and finer oscillations in velocity, causing the spatial density to decay.
- The key technical tools are **scattering estimates** and **analytic norms** that track the width of the analyticity strip as it shrinks through the iteration.

## Relevance to [[kuramoto-stability-problem]]

Dietert's work ([[dietert-2016-stability-bifurcation]], [[dietert-2016-thesis]]) adapts the Mouhot–Villani framework to the Kuramoto equation. The central lesson for the Kuramoto problem:

- **Landau damping is the substitute for hypocoercivity** when there is no collision operator. The deterministic Kuramoto equation has no noise/diffusion term, so classical hypocoercivity (which requires a degenerate diffusion) does not apply. Phase mixing provides the decay mechanism instead.
- The **analytic norms** ($\mathcal{Z}^a$ in Dietert's notation) and **scattering estimates** are directly relevant to Hypothesis (H) in the [[kuramoto-stability-state-of-the-art]].
- For SP-A2 ($|r|$ converges): the Mouhot–Villani proof shows that the force field (analogous to the order parameter $r$) converges exponentially. Adapting this to the Kuramoto PLS regime requires handling the non-zero asymptotic value $r \to r_\infty > 0$.

## Connection to [[fernandez-gerard-varet-giacomin-2016-landau-damping]]

FGG (2016) proved nonlinear Landau damping for the Kuramoto equation near incoherence ($r = 0$), directly following Mouhot–Villani. The open problem is extending this to the PLS ($r > 0$), where the linearized operator has continuous spectrum on the imaginary axis rather than a spectral gap.
