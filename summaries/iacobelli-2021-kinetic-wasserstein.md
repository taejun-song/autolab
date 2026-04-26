---
type: source-summary
title: "Iacobelli (2021) — A New Perspective on Wasserstein Distances for Kinetic Problems"
created: 2026-04-18
updated: 2026-04-18
sources: []
tags: [pde, kinetic-theory, optimal-transport, functional-analysis]
aliases: []
source_file: "../raw/papers/iacobelli-2021-kinetic-wasserstein.pdf"
source_kind: pdf
source_date: 2021-08-13
---

# A New Perspective on Wasserstein Distances for Kinetic Problems

Introduces anisotropic kinetic Wasserstein distances tailored for Vlasov-type equations, improving classical Loeper/Dobrushin stability estimates and naturally handling measure-valued solutions including atoms.

## Key Ideas

- Defines $W_p$ distances that **weight position and velocity differently**, reflecting the anisotropic structure of kinetic equations where spatial and velocity variables play distinct roles.
- Introduces **time-dependent Wasserstein distances** adapted to the characteristic flow of the underlying kinetic equation, so that the distance contracts along solutions by construction.
- Improves classical Dobrushin stability estimates by exploiting the kinetic structure rather than treating the equation as a generic ODE in measure space.
- Handles **atomic measures** (Dirac masses) without requiring absolute continuity — no density assumptions needed.

## Relevance to [[kuramoto-stability-problem]]

For SP-D1 (finding a topology where the PLS is an interior point): the PLS has atoms (locked oscillators concentrate on delta measures where $|\alpha| = 1$), and classical Sobolev or analytic norms see these as boundary/singular objects. Iacobelli's kinetic Wasserstein distances could provide a metric where the PLS has **finite distance from smooth distributions**, making it an interior point of the function space rather than a boundary point. This directly addresses the topology obstruction identified in [[subproblem-decomposition]].

## Connection to [[landau-damping]]

The framework applies to Vlasov-type equations generally. The Vlasov-Poisson equation (Landau damping setting) and the Vlasov-type formulation of the Kuramoto equation share the same kinetic structure, making the anisotropic Wasserstein tools transferable.
