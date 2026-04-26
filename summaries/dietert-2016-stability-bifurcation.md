---
type: source-summary
title: "Dietert (2016) — Stability and Bifurcation for the Kuramoto Model"
created: 2026-04-17
updated: 2026-04-17
sources: []
tags: [dynamical-systems, synchronization, pde, kinetic-theory, spectral-theory]
aliases: ["Dietert 2016", "Kuramoto stability bifurcation energy method"]
source_file: "../raw/papers/dietert-fernandez-gv-2018-cpam.pdf"
source_kind: pdf
source_date: 2016-01-01
---

# Dietert (2016) — Stability and Bifurcation for the Kuramoto Model

The foundational paper establishing rigorous stability theory for the Kuramoto model via Fourier-space energy methods. Contains the **universal energy identity** $\partial_t I_0 = K|\eta|^2$ and a **global stability by energy method** (Section 3) that gives $\int|\eta|^2 < \infty$ for $K < K_c$ without ANY smallness assumption on initial data.

## The universal energy identity (p.4)

For the K-S equation in Fourier variables $\hat{f}(t,l,\omega)$:

$$\partial_t \int_{\mathbb{R}} \sum_{l=1}^{\infty} \frac{1}{l} |\hat{f}(t,l,\omega)|^2 g^{-1}(\omega)\,d\omega = K|\eta(t)|^2$$

where $\eta(t) = r(t)$ is the order parameter. This is a consequence of the **skew-Hermitian** structure of the nonlinear interaction. On the [[ott-antonsen-ansatz|OA manifold]] where $\hat{f}(t,l,\omega) = \alpha(\omega,t)^l g(\omega)$, the LHS reduces to $\Psi = -\int g\log(1-|\alpha|^2)\,d\omega$, recovering the global monotone functional of [[hyperbolic-lyapunov-attack-on-kuramoto-stability]].

## Theorem 1: Global stability by weighted energy (p.5)

For $K < K_{ec} := 2/\int_0^\infty |\hat{g}(\xi)|d\xi$ and a bounded increasing weight $\phi \in C^1(\mathbb{R}^+)$ with $\phi(0) = 1$, the weighted energy

$$I(t) = \int_{\xi=0}^\infty \sum_{l \geq 1} \frac{1}{l} |u(t,l,\xi)|^2 \phi(\xi)\,d\xi$$

satisfies $I(t) + c\int_0^t |\eta(s)|^2 ds \leq I(0)$. In particular, $\int_0^\infty |\eta|^2 < \infty$.

For Lorentzian and Gaussian $g$: $K_{ec} = K_c$, so the global result matches the critical threshold exactly.

## Why this matters for the near-onset gap

The energy method technique — choosing $\phi$ to balance the coupling gain $K|\eta|^2$ against the free-transport decay — is currently applied only around the **incoherent state** ($K < K_c$). Adapting it to perturbations around the **PLS** ($K > K_c$) would:

1. Replace the coupling gain $K|\eta|^2$ with the perturbation growth rate around the PLS
2. Use the PLS spectral gap $\lambda > 0$ (from [[dietert-fernandez-2018-asymptotic-stability]] Theorem 2.3) to provide the decay that $\phi$ amplifies
3. Potentially give a **global** (not local) stability result for the PLS

The key advantage over the Volterra bootstrap: the energy method doesn't require the spectral gap to be LARGE — it only needs it to be POSITIVE. So it could work near onset where the bootstrap fails.

## The proof technique (Lemma 17, pp.12-15)

The key step is a **completing-the-square** estimate in Fourier space. Define the mollified energy $I_{\delta,\epsilon,\zeta}(t) = \sum_l \int \frac{1}{l}|u_\delta|^2 \phi(\xi) e^{-\epsilon l} e^{-\zeta\xi} d\xi$. Its time derivative involves:

1. A **transport decay** term $-\sum |u_\delta(t,l,0)|^2 e^{-\epsilon l} - \int |u_\delta|^2 \phi'(\xi) e^{-\epsilon l} e^{-\zeta\xi}$ (negative — this is the "good" term)
2. A **coupling gain** term $K\,\mathrm{Re}[\overline{\eta}u_\delta \bar{\hat{g}}_\delta]$ (from the $l=1$ interaction; indefinite sign)
3. Remainder terms controlled by Gronwall

The completing-the-square bound (p.14) absorbs the coupling into the transport:

$$-|u|^2\phi' + K\,\mathrm{Re}(\bar{\eta}u\bar{\hat{g}}) \leq -\left|u - \frac{K\bar{\eta}\bar{\hat{g}}\phi}{2\phi'}\right|^2\phi' + \frac{K^2|\eta|^2|\hat{g}|^2\phi^2}{4\phi'} \leq \alpha|\eta|^2$$

where $\alpha = \frac{K^2}{4}\int \frac{|\hat{g}|^2}{\phi'}\phi^2 d\xi$. If $\alpha < 1$, the coupling gain is absorbed by the energy, giving $I(t) + (1-\alpha)\int|\eta|^2 \leq I(0)$.

The weight $\phi$ is explicitly constructed via the Euler-Lagrange equation $0 = |\hat{g}| + \partial_\xi[|\hat{g}|\phi/\phi']$, giving $\phi(\xi) = \bar{A}/(\bar{A} - \int_0^\xi |\hat{g}|)$.

## Adaptation to the PLS (the near-onset attack plan)

To close the near-onset gap, adapt Lemma 17 to perturbations around the PLS $f_s$:

1. Replace incoherent linearization ($l=1$ only couples) with PLS linearization ($l=1$ couples through $\hat{f}_s$)
2. The PLS evolution has an ADDITIONAL damping from the spectral gap $\lambda > 0$ (absent for incoherence)
3. Compute the new $\alpha_{\text{PLS}}$: the spectral gap provides a NEGATIVE contribution to $\alpha$, potentially making $\alpha_{\text{PLS}} < 1$ even for $K > K_c$
4. If $\alpha_{\text{PLS}} < 1$: global stability of the PLS follows from the same argument

The key question: does the PLS spectral gap $\lambda > 0$ reduce $\alpha$ enough to compensate for the coupling gain at $K > K_c$?

## Pages read

pp 1–15 (introduction through Section 3 proof of Theorem 1; Section 2 mean-field limit).

## Cross-links

- [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] — the Ψ functional is Dietert's $I_0$ restricted to the OA manifold
- [[kuramoto-stability-problem]] — Theorem 1 resolves global stability of incoherence for $K < K_c$
- [[landau-damping]] — the energy identity is the K-S analogue of the Vlasov energy identity
- [[dietert-fernandez-2018-asymptotic-stability]] — the review that extends this to PLS local stability
