---
type: source-summary
title: "Dietert & Fernandez (2018) — The Mathematics of Asymptotic Stability in the Kuramoto Model"
created: 2026-04-17
updated: 2026-04-17
sources: []
tags: [dynamical-systems, synchronization, pde, kinetic-theory, statistical-physics, dimension-reduction]
aliases: ["Dietert-Fernandez 2018", "Kuramoto asymptotic stability review"]
source_file: "../raw/papers/1801.01309.pdf"
source_kind: pdf
source_date: 2018-12-15
---

# Dietert & Fernandez (2018) — The Mathematics of Asymptotic Stability in the Kuramoto Model

The definitive review of rigorous asymptotic stability results for stationary solutions of the continuum Kuramoto PDE, synthesizing and extending the work of Chiba, Fernandez–Gérard-Varet–Giacomin, and Dietert on both the homogeneous (incoherent) and partially locked states (PLS), with a crucial original result proving exponential convergence to the [[ott-antonsen-ansatz|Ott–Antonsen manifold]] for analytic frequency distributions.

## Bibliographic details

- **Authors:** Helge Dietert (IMJ-PRG, Sorbonne Université) and Bastien Fernandez (CNRS, Université Paris Diderot).
- **Venue:** *Proc. R. Soc. A* **474**(2220), 20180467 (2018). arXiv:1801.01309v3.
- **Length:** 20 pages + references.
- **Pages read:** All 20 pages.

## Main results

### Theorem 2.1 — Asymptotic relaxation to homogeneous state ($K < K_c$)

For $g \in C^2$ with $\|\hat{g}\|_{L^1_{(1+\tau)^b}(\mathbb{R}^+)} < +\infty$ ($b > 1$) and stability condition (2.1) holding, there exists $\epsilon > 0$ such that small perturbations converge weakly to $f_{\text{hom}}$. Order parameter decay rate depends on regularity: $r(t) = O(t^{-b})$ for Sobolev, $r(t) = O(e^{-a't})$ for analytic $g$ (Proposition 2.2).

### Theorem 2.3 — Asymptotic relaxation to PLS (Sobolev case)

For $b > 3/2$, $b_g > b + 3$, and a linearly stable PLS $f_s$ satisfying the stability condition (2.4), sufficiently small perturbations converge weakly to a nearby PLS $R_{\Theta_\infty}f_s$ with polynomial decay of the order parameter:

$$|r(t) - r_s e^{i\Theta_\infty}| = O(t^{1/2 - b}).$$

The stability condition (2.4) is: $\det(\text{Id} - \frac{K}{2}M(z, r_s)) \neq 0$ for all $z \neq 0$ with $\Re(z) \geq 0$, and $z = 0$ is a simple zero.

### Theorem 2.4 — Asymptotic relaxation to PLS (analytic case)

For analytic $g$ (exponential weight $\phi(\tau) = e^{a\tau}$), under the same stability condition (2.4), sufficiently small perturbations converge exponentially:

$$|r(t) - r_s e^{i\Theta_\infty}| = O(e^{-a't}).$$

### Proposition 4.1 — Convergence to the OA manifold (original result)

**This is the most important result for the [[hyperbolic-lyapunov-attack-on-kuramoto-stability|Lyapunov hypothesis]].**

The OA manifold is characterized as the set of measures whose Fourier transform satisfies $\hat{f}_\ell = h^{*\ell} * \hat{g}$ for some function $h : \mathbb{R} \to \mathbb{C}$. The distance to the OA manifold is measured by $w_{n,m}(\tau) = \hat{f}_{n+m} * \hat{g} - \hat{f}_n * \hat{f}_m$.

For analytic $g$ with $\|\hat{g}\|_{\mathcal{H}^1_{e^{a\tau}}(\mathbb{R}^+)} < +\infty$ and initial data satisfying $\|w(0)\|_{\mathcal{H}^1_{e^{a\tau}}(\mathbb{N}^2 \times \mathbb{R})} < +\infty$:

$$\|w(t)\|_{\mathcal{H}^1_{e^{a\tau}}(\mathbb{N}^2 \times \mathbb{R})} \leq \|w(0)\|_{\mathcal{H}^1_{e^{a\tau}}(\mathbb{N}^2 \times \mathbb{R})}\, e^{-at}.$$

In particular, $\lim_{t \to +\infty} w_{n,m}(t, \tau) = 0$ for all $n, m, \tau$. **The OA manifold is exponentially attracting for analytic $g$.**

The proof uses the evolution equation for $w_{n,m}$ and the key identity $\frac{d}{dt}\|w\|^2 \leq -2a\|w\|^2$, which follows from the structure of the Kuramoto dynamics in Fourier space.

## Critical observation: global stability is blocked in the full state space but NOT on OA

The review notes (p.9): "global stability can never hold for PLS because $f_{\text{hom}}$ is a distinct stationary state." This means in the full K-S state space, the basin of attraction of the PLS cannot include all initial conditions — $f_{\text{hom}}$ and its neighbourhood are excluded.

**However, on the OA manifold**, $f_{\text{hom}}$ corresponds to $\alpha(\omega) \equiv 0$. For $K > K_c$, this state is **unstable** on $\mathcal{M}_{\text{OA}}$ — the OA ODE for the order parameter has a positive growth rate $(K/2 - \gamma > 0$ for Lorentzian, and more generally the linearization about $\alpha \equiv 0$ has an unstable eigenvalue). So the obstruction to global stability vanishes on the OA manifold. Global stability of the PLS restricted to $\mathcal{M}_{\text{OA}}$ is a well-posed and non-trivially open question.

## The explicit PLS profile

The stable PLS $f_s$ has the explicit form (after rescaling so $r_s$ is real):

$$\beta\!\left(\frac{\omega}{Kr_s}\right) = -i\omega + \begin{cases} \sqrt{1 - \omega^2} & \text{if } |\omega| \leq 1, \\ i\omega\sqrt{1 - \omega^{-2}} & \text{if } |\omega| > 1, \end{cases}$$

where $\beta$ determines the locked-oscillator phase via the self-consistency equation $\int_{\mathbb{R}} \beta(\omega/(Kr_s))\, g(\omega)\, d\omega = r_s$. This is the explicit $\alpha^*_K(\omega)$ needed for the Lyapunov functional construction.

## Proof strategy: Volterra equations + bootstrap

All stability proofs in the review follow the same strategy:
1. Linearize about the stationary state, separating transport ($L_1$) from order-parameter coupling ($L_2$).
2. Derive a **Volterra equation** for the order parameter perturbation.
3. Prove **linear stability** via the Penrose-type criterion (dispersion relation $D_G$ or characteristic equation (2.4)).
4. For nonlinear stability: handle the nonlinearity $Q$ as a forcing term, controlling it via a **bootstrap argument** (Gearhart–Prüss theorem in the exponential case, or energy estimates in the Sobolev case).

## Open questions (§6, p.18)

The review lists two remaining open problems:
1. **Standing waves:** Prove asymptotic stability of standing wave solutions (not just stationary PLS).
2. **Higher harmonics:** Prove PLS stability for Kuramoto extensions with interactions involving several Fourier modes (the Daido model). Landau damping for $f_{\text{hom}}$ extends straightforwardly; PLS stability "remains entirely open."

## Cross-links

- [[kuramoto-stability-problem]] — Theorems 2.3/2.4 resolve Assertion 2 (local stability along the branch) for smooth/analytic $g$
- [[landau-damping]] — Theorem 2.1 extends FGG's result with exponential rates for analytic $g$
- [[ott-antonsen-ansatz]] — Proposition 4.1 proves OA manifold is exponentially attracting for analytic $g$
- [[fernandez-gerard-varet-giacomin-2016-landau-damping]] — subsumed and extended by this review
- [[chiba-2015-kuramoto-conjecture]] — complementary spectral-theoretic approach
- [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] — Proposition 4.1 upgrades the hypothesis from partial (on-manifold) to potentially full resolution for analytic $g$
- [[kuramoto-sakaguchi-equation]] — the PDE analyzed throughout
