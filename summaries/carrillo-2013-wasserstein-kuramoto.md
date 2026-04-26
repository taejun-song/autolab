---
type: source-summary
title: "Carrillo, Choi, Ha, Kang & Kim (2013) — Contractivity of the Wasserstein Metric for the Kinetic Kuramoto Equation"
created: 2026-04-18
updated: 2026-04-18
sources: []
tags: [dynamical-systems, synchronization, optimal-transport, kinetic-theory]
aliases: []
source_file: "../raw/papers/carrillo-2013-wasserstein-kuramoto.pdf"
source_kind: pdf
source_date: 2013-01-09
---

# Contractivity of the Wasserstein Metric for the Kinetic Kuramoto Equation

Proves Wasserstein $p$-distance between measure-valued solutions of the kinetic Kuramoto equation decays exponentially for identical oscillators with initial data in a half-circle.

## Key Results

- For **identical natural frequencies**, measure-valued solutions of the kinetic [[kuramoto-model]] converge to a Dirac delta (complete [[synchronization]]) in Wasserstein distance.
- Uses the **cumulative distribution function + pseudo-inverse** technique for 1D optimal transport, reducing the Wasserstein distance computation to an $L^p$ norm of the pseudo-inverse difference.
- Exponential decay of $W_p$ requires initial data supported in a half-circle ($\operatorname{diam}(\operatorname{supp}) < \pi$).
- Contraction requires **identical frequencies** or matching frequency distributions across solutions.

## Relevance to [[kuramoto-stability-problem]]

This paper establishes the Wasserstein framework for the Kuramoto problem but does **not** cover the partially locked state (PLS) regime. The PLS involves non-identical frequencies and coexistence of locked and drifting oscillators, which breaks the identical-frequency assumption needed for contractivity. Nevertheless, the 1D optimal transport tools (pseudo-inverse, cumulative distribution) are directly relevant to any Wasserstein-based stability argument for the full problem.

## Limitations

- Identical frequencies only — no frequency heterogeneity.
- Half-circle support assumption — does not apply to partially locked states where drifting oscillators spread over $[-\pi, \pi]$.
- No treatment of the mixed locked/drifting structure characteristic of the PLS.
