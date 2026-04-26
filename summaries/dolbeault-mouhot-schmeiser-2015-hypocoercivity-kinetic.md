---
type: source-summary
title: "Dolbeault, Mouhot & Schmeiser (2015) — Hypocoercivity for Linear Kinetic Equations Conserving Mass"
created: 2026-04-18
updated: 2026-04-18
sources: []
tags: [pde, kinetic-theory, functional-analysis, convergence, hypocoercivity]
aliases: []
source_file: "../raw/papers/dolbeault-mouhot-schmeiser-2015-hypocoercivity-kinetic.pdf"
source_kind: pdf
source_date: 2015-05-10
---

# Dolbeault, Mouhot & Schmeiser (2015) — Hypocoercivity for Linear Kinetic Equations Conserving Mass

Explicit hypocoercivity framework for kinetic equations with microscopic coercivity (H1) and macroscopic coercivity (H2) assumptions, giving exponential convergence with quantitative rates.

## Setting

Linear kinetic equation $\partial_t f + Tf = Lf$ where $T$ is the transport operator and $L$ is the collision/relaxation operator. Published in Trans. AMS.

## Key Assumptions

- **(H1) Microscopic coercivity**: $-\langle Lf, f \rangle \geq \lambda_m \|(1 - \Pi)f\|^2$, where $\Pi$ is the projection onto the local equilibrium.
- **(H2) Macroscopic coercivity**: $\|T\Pi f\|^2 \geq \lambda_M \|\Pi f\|^2$.

## Main Construction

Modified entropy $H[f] = \frac{1}{2}\|f\|^2 + \varepsilon\langle Af, f\rangle$ with the auxiliary operator:

$$A = \bigl(1 + (T\Pi)^*(T\Pi)\bigr)^{-1}(T\Pi)^*$$

**Result**: $\frac{dH}{dt} \leq -\lambda H$ with explicit $\lambda$ depending on $\lambda_m$, $\lambda_M$, and operator norms.

## Applications

Applicable to Vlasov–Fokker–Planck, linearized Boltzmann, BGK models, and other kinetic equations satisfying (H1)–(H2).

## Relevance to Kuramoto

For the $n$-pole OA linearization: the damping terms $-\gamma_j$ could provide microscopic coercivity (H1), while the mean-field coupling provides macroscopic coercivity (H2). This would yield quantitative convergence rates uniform in $n$, potentially closing the passage-to-limit gap in Approach 22. See [[villani-2009-hypocoercivity]] for the foundational theory and [[kuramoto-stability-problem]] for the target application.
