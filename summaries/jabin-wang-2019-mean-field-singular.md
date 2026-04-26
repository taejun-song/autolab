---
type: source-summary
title: "Bresch, Jabin & Wang (2019) — Mean Field Limit and Quantitative Estimates with Singular Kernels"
created: 2026-04-18
updated: 2026-04-18
sources: []
tags: [pde, kinetic-theory, mean-field, optimal-transport]
aliases: []
source_file: "../raw/papers/jabin-wang-2019-mean-field-singular.pdf"
source_kind: pdf
source_date: 2019-06-10
---

# Mean Field Limit and Quantitative Estimates with Singular Kernels

Develops relative entropy methods for mean-field limits with singular interaction kernels, handling concentration phenomena via weighted relative entropy.

## Key Results

- Proves **quantitative $N$-particle to mean-field convergence** for systems with singular interaction potentials, including Patlak–Keller–Segel type models.
- Introduces a **weighted relative entropy** with adapted weights designed to cancel singular terms arising from the interaction kernel.
- The weights are chosen to match the singularity structure of the kernel, allowing the Gronwall argument to close even when the interaction is not Lipschitz.
- Convergence rates are quantitative: explicit dependence on $N$ and the regularity of the initial data.

## Relevance to [[kuramoto-stability-problem]]

For SP-B3 (passage from finite-$N$ to continuum limit): the $\sin(\theta_i - \theta_j)$ coupling in the [[kuramoto-model]] is Lipschitz (not singular), so the kernel regularity is not the obstruction. However, **PLS formation is a concentration phenomenon** — oscillators collapse to delta measures as they lock. The weighted relative entropy framework could measure distance between smooth empirical distributions and the atomic PLS, providing the quantitative convergence tool needed for [[kuramoto-finite-n-convergence]].

## Connection to Optimal Transport

The relative entropy approach is complementary to the Wasserstein approach of [[carrillo-2013-wasserstein-kuramoto]]. Relative entropy controls $W_2$ via Talagrand's inequality (for log-concave reference measures), but the PLS is not log-concave. The weighted variant in this paper relaxes that requirement by building the weight into the entropy itself.
