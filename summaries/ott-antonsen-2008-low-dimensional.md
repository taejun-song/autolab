---
type: source-summary
title: "Ott & Antonsen (2008) — Low Dimensional Behavior of Large Systems of Globally Coupled Oscillators"
created: 2026-04-16
updated: 2026-04-16
sources: []
tags: [dynamical-systems, synchronization, dimension-reduction]
aliases: ["Ott-Antonsen 2008", "OA 2008", "Ott Antonsen original"]
source_file: "../raw/papers/0806.0004.pdf"
source_kind: pdf
source_date: 2008-06-02
---

# Ott & Antonsen (2008) — Low Dimensional Behavior of Large Systems of Globally Coupled Oscillators

The foundational paper introducing the Ott–Antonsen ansatz: an exact reduction of the infinite-dimensional Kuramoto–Sakaguchi continuum dynamics to a finite set of ODEs by restricting to a specific invariant manifold of distribution functions whose Fourier coefficients are geometric powers of a single complex function $\alpha(\omega, t)$.

## Bibliographic details

- **Authors:** Edward Ott and Thomas M. Antonsen (University of Maryland, College Park).
- **Venue:** arXiv:0806.0004v1 (June 2, 2008). Published as *Chaos* **18**, 037113 (2008).
- **Length:** 16 pages (arXiv version).
- **Pages read:** all 16.

## The ansatz

Expand the distribution function $f(\omega, \theta, t)$ in a Fourier series in $\theta$:

$$f = \frac{g(\omega)}{2\pi}\left\{1 + \left[\sum_{n=1}^{\infty} f_n(\omega, t)\exp(in\theta) + \text{c.c.}\right]\right\}.$$

The ansatz restricts to the class where **all Fourier coefficients are geometric**:

$$f_n(\omega, t) = \alpha(\omega, t)^n, \qquad |\alpha(\omega, t)| \leq 1.$$

This is equivalent to saying $f$ is a **Poisson-kernel density** on $S^1$ parameterised by $\alpha(\omega) \in \overline{\mathbb{D}}$.

## The OA ODE (Eq. 6)

Substituting the ansatz into the [[kuramoto-sakaguchi-equation|K-S continuity equation]] gives the closed ODE:

$$\partial_t \alpha + \frac{K}{2}(r\alpha^2 - r^*) + i\omega\alpha = 0,$$

equivalently $\partial_t\alpha = -i\omega\alpha + (K/2)(r^* - r\alpha^2)$, where $r = \int g(\omega)\overline{\alpha(\omega, t)}\,d\omega$ is the complex order parameter and $r^* = \bar{r}$.

## Invariance of the manifold

The paper proves (§III, using note [13] on ODE theory and note [14] on the maximum principle for $|\alpha|$ in the complex $\omega$-plane) that if:
- $|\alpha(\omega, 0)| \leq 1$ for real $\omega$,
- $\alpha(\omega, 0)$ is analytically continuable to the lower half complex $\omega$-plane with no singularities and $|\alpha| \to 0$ as $\text{Im}(\omega) \to -\infty$,

then these properties are **preserved for all $t > 0$**. The manifold $M$ of such distributions is invariant under the K-S dynamics. This is the rigorous justification that the ansatz is self-consistent.

## Lorentzian solution (Eq. 10–11)

For Lorentzian $g(\omega) = (\Delta/\pi)[(\omega - \omega_0)^2 + \Delta^2]^{-1}$, the $\omega$-integral is evaluated by residue at $\omega = \omega_0 - i\Delta$, giving $r(t) = \alpha^*(-i\Delta, t)$ and the scalar ODE

$$d\rho/dt + (1 - K/2)\rho + (K/2)\rho^3 = 0, \qquad \rho = |r|,$$

with exact solution (Eq. 11). For $K < K_c = 2$ the order parameter decays to zero; for $K > 2$ it converges to $\rho_\infty = \sqrt{1 - 2/K}$.

## Generalizations (§IV)

The method extends to:
- **Rational $g(\omega)$**: any $g = P_1/P_2$ with $P_2$ having $m$ poles in the lower half-plane gives $m$ coupled complex ODEs.
- **External driving**: $\Lambda\sin(\Omega t - \theta_i)$ added to the Kuramoto model gives a 2D ODE for $r(t)$ (Eq. 14).
- **Multi-community**: $s$ communities with inter-community coupling $K_{\sigma\sigma'}$ give $s$ coupled complex ODEs (Eq. 15).
- **Time-delayed coupling**: $\theta_j(t) \to \theta_j(t - \tau)$ gives an infinite-dimensional delay-ODE (Eq. 19), but still low-dimensional in the order parameter.
- **Gaussian $g(\omega)$**: numerics show the same macroscopic attractors and bifurcations as Lorentzian, suggesting the reduction captures the essential dynamics for general unimodal $g$.

## CRITICAL CAVEAT: the OA manifold is NOT attracting (note [24])

The paper's final note [24] (p. 15) is essential for the [[hyperbolic-lyapunov-attack-on-kuramoto-stability|stability hypothesis]]:

> While the time-asymptotic behavior of the order-parameter obtained from the dynamics of the reduced systems (10) and (13) is seen to correspond to the attractors of the full system [...], **we emphasize that $M$ need not be attracting for the *microscopic* state** $f(\omega, \theta, t)$.

Explicit counterexample: $f = [g(\omega)/2\pi]\{1 + \sum_m \beta_m(\omega)\exp[im(\theta - \omega t)]\}$ with $\beta_{\pm 1}(\omega) = 0$ and arbitrary $\beta_m$ for $|m| \geq 2$ is a solution of the K-S equation with $r(t) = 0$ for all $t$ — i.e., a distribution that stays incoherent and never approaches $M$. These are perturbations in the higher Fourier modes ($|m| \geq 2$) that are invisible to the order parameter but exist as legitimate solutions off the OA manifold.

**Implication for the Lyapunov hypothesis**: the Ott–Antonsen manifold is NOT a global attractor of the full K-S dynamics. The hypothesis in [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] is therefore correctly scoped to stability **restricted to $M$**. The full problem (stability from generic initial conditions) CANNOT be solved by the OA approach alone — it requires a separate argument for transversal dynamics (the Chiba direction).

## What this adds beyond the wiki's secondary sources

The wiki previously described OA only through [[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]] (which generalizes to spheres) and [[ha-ko-park-zhang-2016-collective-synchronization]] (which summarizes briefly). This primary source adds:

1. **The exact ODE** (Eq. 6) with its precise sign conventions and the definition $r = \int g\bar\alpha\,d\omega$.
2. **The invariance proof** via analytic continuation to the lower half $\omega$-plane — a complex-analysis argument not described in any secondary source in the wiki.
3. **The explicit non-attractivity counterexample** (note [24]) — the most important single fact for the stability hypothesis, not mentioned in any secondary source.
4. **Gaussian $g$ numerical evidence** — the ansatz captures macroscopic dynamics for non-Lorentzian distributions, supporting the hypothesis that the OA manifold contains the relevant attractors even though it's not globally attracting.

## Cross-links

- [[ott-antonsen-ansatz]] — the concept page this source is the primary reference for
- [[kuramoto-sakaguchi-equation]] — the PDE whose invariant manifold the ansatz defines
- [[kuramoto-stability-problem]] — note [24] directly constrains what the OA approach can and cannot prove
- [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] — the synthesis page whose scope is validated by note [24]
- [[kuramoto-model]] — the finite-$N$ ODE system whose $N \to \infty$ limit the ansatz reduces
- [[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]] — generalizes the OA ansatz to $S^{d-1}$ via hyperbolic Poisson kernels
