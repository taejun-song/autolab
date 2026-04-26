---
type: source-summary
title: "Dietert (2016) — Contributions to Mixing and Hypocoercivity in Kinetic Models (PhD Thesis)"
created: 2026-04-18
updated: 2026-04-18
sources: []
tags: [dynamical-systems, synchronization, landau-damping, pde, stability, kinetic-theory]
aliases: ["Dietert thesis", "Dietert 2016 thesis"]
source_file: "../raw/papers/dietert-2016-thesis.pdf"
source_kind: pdf
source_date: 2016-07-11
---

# Dietert (2016) — Contributions to Mixing and Hypocoercivity in Kinetic Models

PhD thesis (Cambridge, supervised by Clément Mouhot and Arieh Iserles) providing the detailed proofs underlying [[dietert-2016-stability-bifurcation]] and [[dietert-2017-pls-sobolev]], with additional material on the exponential norms, strip analyticity, and the $\mathcal{Z}^a$ norm construction.

## Structure

- **Chapter 1**: Review of kinetic models with Landau damping (Vlasov-Poisson and Kuramoto)
- **Chapter 2**: Mean-field limit
- **Chapter 3**: Volterra integral equations for linear stability
- **Chapter 4**: Stability of the incoherent state in the Kuramoto equation
- **Chapter 5**: Stability of partially locked states in the Kuramoto model
- **Chapter 6**: Vlasov-Poisson on $S^3$
- **Chapter 7**: Hypocoercivity
- **Chapter 8**: Expansion into Hermite functions

## Key results for [[kuramoto-stability-problem]]

### §4.7 — Exponential norms and strip analyticity

**Lemma 4.28**: If $f \in L^1(\mathbb{R}) \cap C(\mathbb{R})$ with $\hat{f} \in L^\infty(\mathbb{R}, \exp_a)$, then $f$ has an analytic continuation to the strip $\{z : -a < \Im z \leq 0\}$.

**Lemma 4.29**: Conversely, if $f$ has analytic continuation to $\{z : -a \leq \Im z \leq 0\}$ with $|f(z)| \to 0$ uniformly as $|\operatorname{Re} z| \to \infty$ and $f(\cdot - ia) \in L^1(\mathbb{R})$, then
$$\|\hat{f}\|_{L^\infty(\mathbb{R},\exp_a)} \leq \|f(\cdot - ia)\|_{L^1(\mathbb{R})}.$$

These two lemmas establish the **Paley-Wiener equivalence**: finite $\mathcal{Z}^a$ norm $\Leftrightarrow$ analytic continuation to strip of width $a$.

### §4.7 — PLS profile analyticity (Lemma 4.30)

The function $\beta(z) = -iz + \sqrt{1-z^2}$ (for $|z| < 1$) and $\beta(z) = -iz(1 - \sqrt{1-1/z^2})$ (for $|z| \geq 1$) satisfies:
- $\beta$ is **analytic in the lower half-plane** $\{z \in \mathbb{C} : \Im z \leq 0\}$
- $|\beta(z)| \leq 1$ in the lower half-plane
- For $|z| \geq \sqrt{2}$: $|\beta(z)| \leq 1/|z|$
- For any $a > 0$: $\sup_{\omega \in \mathbb{R}}|\beta(\frac{\omega - ia}{K\eta})| < 1$

**This means the PLS satisfies $|\alpha^*(\omega)| \leq 1$ for all $\omega$ in the lower half-plane**, not just on the real axis. This is a crucial bound for Hypothesis (H): the equilibrium is already inside the trapping region.

### §4.7 — PLS $\mathcal{Z}^a$ norm (Theorem 4.31)

For $g \in L^1(\mathbb{R})$ with analytic continuation to $\{z : -a \leq \Im z \leq 0\}$ and $g(\cdot - ia) \in L^1(\mathbb{R})$:
$$\|u\|_{Z^a} \leq \frac{K|\eta|}{2}\|g(\cdot - ia)\|_{L^1(\mathbb{R})}.$$

### §5.3 — Cauchy problem in $\mathcal{X}_{a,k}$ (Proposition 5.6)

The Kuramoto equation in Fourier variables $u_l(t,\xi) = \hat{f}_l(t,\xi)$ evolves as:
$$\partial_t u_l(\xi) = l\partial_\xi u_l(\xi) + \frac{Kl}{2}\left(u_1(0)u_{l-1}(\xi) - \overline{u_1(0)}u_{l+1}(\xi)\right)$$

For initial data with $\|\hat{f}_{\text{in}}\|_{a,0} < \infty$ and $\|\hat{g}\|_a < \infty$:
$$\sup_{t \in [0,T]}\|\hat{f}(t)\|_{a,0} < \infty \quad \text{for all } T > 0$$

with the energy estimate:
$$\|u(t)\|_{a,0}^2 + 2a\int_0^t \|u(s)\|_{a,1/2}^2 ds \leq e^{C_T t}\|u_{\text{in}}\|_{a,0}^2$$

This gives **global existence** (no finite-time blowup) in $\mathcal{X}_{a,0}$, but with at-most-exponential growth — not uniform boundedness.

### §5.5 — Nonlinear stability (Proposition 5.22, Lemma 5.21)

For a stable PLS $f_{\text{st}}$ with rate $a'$: there exist $\epsilon', C > 0$ such that for initial perturbation $u_{\text{in}} \in P_s(\mathcal{X}_{a,0})$ with $\|u_{\text{in}}\|_{a,0} < \epsilon'$:
$$\|u(t)\|_{a,0} \leq C\|u_{\text{in}}\|_{a,0} e^{-a't}, \quad \forall t \in \mathbb{R}^+$$

This is **local** stability: perturbations must start $\epsilon'$-small in $\mathcal{X}_{a,0}$.

### §5.6.2 — OA manifold = full stability

On the OA manifold $\tilde{f}_l(\omega) = \alpha^l(\omega)g(\omega)$, the stability condition is equivalent to the full-space stability condition. "No loss of generality results in investigating the existence and stability of $f_s$ in the OA manifold. The Ott-Antonsen ansatz is perfectly legitimate."

The pole reduction for rational $g$ gives the ODE system:
$$\frac{d}{dt}\alpha_i = -i\omega_i\alpha_i + \frac{K}{2}\left(z(t) - \overline{z(t)}\alpha_i^2\right), \quad z(t) = -\sum_{i=1}^M \omega_i\alpha_i$$

### §5.6.1 — Even frequency distributions

For even unimodal $g$ with $K > K_c$, the unique PLS is always asymptotically stable ($h_s'(0) \neq 0$).

## Relevance to Hypothesis (H)

The thesis provides the key ingredients for the $\mathcal{Z}^a$ precompactness approach:
1. **Paley-Wiener**: $\mathcal{Z}^a$ boundedness $\Leftrightarrow$ strip analyticity with $L^1$ boundary
2. **PLS in strip**: $|\alpha^*| \leq 1$ in the lower half-plane (Lemma 4.30)
3. **Global existence**: solutions in $\mathcal{X}_{a,0}$ exist for all time (no blowup in $\mathcal{Z}^a$-type norms)
4. **Local attraction**: solutions near PLS decay exponentially in $\mathcal{X}_{a,0}$

The gap between 3 (global existence with exponential growth bound) and 4 (local exponential decay) is exactly where Hypothesis (H) — uniform-in-time strip boundedness — would bridge.
