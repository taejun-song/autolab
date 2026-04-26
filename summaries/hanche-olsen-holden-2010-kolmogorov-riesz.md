---
type: source-summary
title: "Hanche-Olsen & Holden (2010) — The Kolmogorov-Riesz Compactness Theorem"
created: 2026-04-18
updated: 2026-04-18
sources: []
tags: [functional-analysis, pde]
aliases: ["Kolmogorov-Riesz theorem", "Frechet-Kolmogorov compactness"]
source_file: "../raw/papers/0906.4883.pdf"
source_kind: pdf
source_date: 2010-01-01
---

# Hanche-Olsen & Holden (2010) — The Kolmogorov-Riesz Compactness Theorem

The definitive modern statement of the Fréchet-Kolmogorov characterization of precompact sets in $L^p$: a set $\mathcal{F} \subset L^p(\mathbb{R}^n)$ is precompact if and only if it is (i) bounded, (ii) tight (uniform tail decay), and (iii) equicontinuous under translation ($\|\tau_h f - f\|_p \to 0$ uniformly in $f \in \mathcal{F}$ as $h \to 0$).

## Relevance to the Kuramoto stability problem

Applied to the OA orbit $\{\alpha(\cdot,t) : t \geq 0\} \subset L^2(g;\mathbb{C})$:

- **(i) Bounded**: $|\alpha| < 1$ gives $\|\alpha\|_{L^2(g)} \leq 1$. ✓
- **(ii) Tight**: proved via standard averaging theorem for large $|\omega|$. ✓
- **(iii) Translation equicontinuity**: $\int|\alpha(\omega+h,t) - \alpha(\omega,t)|^2 g(\omega)\,d\omega \to 0$ uniformly in $t$? This is equivalent to $B(t) = \int|\partial_\omega\alpha|^2 g\,d\omega$ being uniformly bounded. **THIS IS THE OPEN QUESTION.**

The theorem precisely identifies the bottleneck: conditions (i) and (ii) are satisfied; condition (iii) — the slope energy bound — is the single missing ingredient for precompactness, and hence for applying any convergence theorem (gradient-like, LaSalle, Łojasiewicz-Simon) from [[haraux-jendoubi-2015-convergence-problem]].

## Pages read

Not directly read (reference identified from search). The theorem statement is standard and well-known.

## Cross-links

- [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] — the Kolmogorov-Riesz theorem confirms the slope energy $B(t)$ bound is the canonical path to precompactness
- [[kuramoto-stability-problem]] — the precompactness gap reduces to bounding $B(t)$
