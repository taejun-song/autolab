---
type: source-summary
title: "Fernandez, Gérard-Varet, Giacomin (2016) — Landau Damping in the Kuramoto Model"
created: 2026-04-17
updated: 2026-04-17
sources: []
tags: [dynamical-systems, synchronization, pde, kinetic-theory, statistical-physics]
aliases: ["FGG 2016", "nonlinear Landau damping Kuramoto", "Fernandez-Gérard-Varet-Giacomin 2016"]
source_file: "../raw/papers/1410.6006.pdf"
source_kind: pdf
source_date: 2016-07-01
---

# Fernandez, Gérard-Varet, Giacomin (2016) — Landau Damping in the Kuramoto Model

The first rigorous proof of **nonlinear Landau damping** for the Kuramoto model: under a stability criterion equivalent to $K < K_c$ for standard frequency distributions, the order parameter of the continuum-limit PDE decays polynomially as $\mathrm{R}(t) = O(t^{-n})$ from sufficiently small $C^n$ perturbations of incoherence, with the decay rate controlled by the regularity of the frequency density $g$.

## Bibliographic details

- **Authors:** Bastien Fernandez (Université Paris Diderot / CNRS), David Gérard-Varet (Université Paris Diderot, Institut de Mathématiques de Jussieu), Giambattista Giacomin (Université Paris Diderot / CNRS).
- **Venue:** arXiv:1410.6006v1 (October 22, 2014). Published as *Annales Henri Poincaré* **17** (2016), 1793–1823.
- **Length:** 26 pages.
- **Pages read:** All 26 pages.
- **MSC:** 35Q84, 82C44, 45D05, 35Q92, 92B25.

## The main result

**Theorem 3.1.** Assume $g \in C^n(\mathbb{R})$ for some $n \geq 4$ with the regularity conditions

$$\|g\|_{\mathcal{H}^n} < +\infty, \quad \hat{g} \in L^1(\mathbb{R}^+), \quad \int_{\mathbb{R}^+} t^n |\hat{g}(t)|\,dt < +\infty, \tag{3.1}$$

and that the **stability criterion** holds: for every $K \geq 0$,

$$1 - \frac{K}{2}\int_{\mathbb{R}^+} \hat{g}(t)e^{-i\omega t}\,dt \neq 0, \quad \forall\omega \in \Pi^-. \tag{3.2}$$

Then there exists $\epsilon_K > 0$ such that for any initial probability density $\frac{1}{2\pi} + \mathrm{r}$ with $\|\mathrm{r} \cdot g\|_{\mathcal{H}^n} \leq \epsilon_K$, the order parameter satisfies

$$\mathrm{R}(t) = O(t^{-n}).$$

**Key features:**

- **Nonlinear**, not merely linearized: the full K-S equation dynamics are controlled, not just the linearization about incoherence.
- **Polynomial decay** at rate $n$, governed by the Sobolev regularity of $g$. Higher regularity gives faster decay. The decay rate does not depend on $K$.
- The perturbation size $\epsilon_K$ depends on $K$ — the closer $K$ is to $K_c$, the smaller the admissible perturbation.

## The stability criterion

Condition (3.2) is the Kuramoto analogue of the **Penrose criterion** for the Vlasov equation. The function $D_G(\omega) = 1 - \int_{\mathbb{R}^+} G(t)e^{-i\omega t}\,dt$ with $G = \frac{K}{2}\hat{g}$ defines a closed curve $\gamma_G$ in the complex plane. Criterion (3.2) is equivalent to requiring that this curve does not wind around the origin (Lemma 3.4: $D_G|_{\Pi^-} \neq 0$ iff $\mathrm{Ind}_G(0) = 0$).

For **symmetric unimodal** $g$, the criterion reduces to the familiar threshold:

$$\int_{\mathbb{R}^+} \frac{g(\omega - \sigma) - g(\omega + \sigma)}{\sigma}\,d\sigma = 0 \quad \Longrightarrow \quad K < \frac{2}{\pi g(0)} = K_c. \tag{3.5}$$

Equivalence of (3.2) and (3.5) is verified explicitly for Cauchy (Lorentzian), bi-Cauchy, and Gaussian distributions. For non-symmetric or non-unimodal $g$, the general criterion (3.2) is strictly more informative than the $K_c$ formula.

## Proposition 3.2: large perturbations, small $K$

For any perturbation with finite $\mathcal{H}^n$ norm (not necessarily small), there exists $K_r > 0$ such that the damping conclusion holds for all $K \in [0, K_r)$. This is the complement of Theorem 3.1: instead of fixing $K < K_c$ and requiring small initial data, one fixes the data and finds a coupling threshold below which damping occurs.

## Corollary 3.3: weak convergence to free transport

The perturbation $\mathrm{r}(t, \theta, \omega)$ converges in $\mathcal{H}^{n-2}$ to a function $\mathrm{r}_\infty$ satisfying the free transport equation $\partial_t \mathrm{r} + \omega\,\partial_\theta \mathrm{r} = 0$. This is the Kuramoto analogue of scattering in the Vlasov setting: the density approaches a non-interacting state as $t \to \infty$.

## Proof method: Volterra integral equation + bootstrap

The approach is PDE-analytic, not dynamical-systems-based (contrast with Crawford's center-manifold method and Chiba's rigged Hilbert space). The key steps:

1. **Galilean transformation** $(t, \theta, \omega) \mapsto (t, \theta + t\omega, \omega)$ converts the K-S equation to a frame co-rotating with each oscillator.
2. **Fourier decomposition** in $(\theta, \omega)$ yields an infinite system of coupled ODEs for the Fourier modes $\hat{p}_k(t, \tau)$.
3. **Volterra integral equation** (4.3) for the rescaled order parameter $R(t)$:

$$R(t) - \frac{K}{2}\int_0^t \hat{g}(t - s)R(s)\,ds = F(t),$$

where $F$ is the input signal depending on initial data.

4. **Polynomial decay** of Volterra solutions (Proposition 4.1): under the stability criterion, $\sup_{[0,T]} (1+t)^n |R(t)| \leq C_{n,G} \sup_{[0,T]} (1+t)^n |F(t)|$. The proof uses Fourier-space estimates on the resolvent $\hat{F}/D_G$ with careful splitting into high-frequency ($|x| > \eta$, handled via $L^1$-norm of the inverse Fourier transform of $\chi_\eta/D_G$) and low-frequency ($|x| \leq \eta$, handled via the Plancherel theorem and vanishing properties of $\hat{F}(\cdot - i\epsilon)$ as $\epsilon \to 0$).
5. **Bootstrap** (§5): the Sobolev norm $\|p(t)\|_{\mathcal{H}^n}$ is shown to remain bounded using energy estimates (Lemma 5.3), and this bound feeds back into the Volterra equation to close the argument. The bootstrap proceeds through three stages: $\mathcal{H}^n$ control (Lemma 5.4), $\mathcal{H}^{n-2}$ convergence (Lemma 5.5), and finally the weak-convergence corollary.

## Relationship to other approaches

- **Strogatz–Mirollo–Matthews (1992):** Proved **linear** Landau damping (exponential decay of R at the linearized level). FGG extends this to the **nonlinear** level.
- **Chiba (2015):** Uses a rigged Hilbert space / resonance-pole approach on the **full** K-S state space to prove nonlinear stability of incoherence below $K_c$ (Theorem 1.2) and bifurcation at $K_c$ (Theorem 1.3). The FGG result is the same *conclusion* (nonlinear damping below threshold) reached by a different *method* (Volterra/PDE vs spectral/center-manifold). Chiba obtains **exponential** decay; FGG obtains **polynomial** decay but with explicit dependence on the regularity of $g$.
- **Mouhot–Villani (2011):** The celebrated proof of nonlinear Landau damping for the Vlasov equation. FGG's approach is directly inspired by Faou–Rousset (2014) for the Vlasov-HMF model, which adapted the Mouhot–Villani strategy to a simpler setting. The Kuramoto model is structurally even simpler (only the first Fourier mode couples), making the bootstrap argument cleaner.
- **The [[hyperbolic-lyapunov-attack-on-kuramoto-stability|Lyapunov hypothesis]]:** FGG handles the regime **below** $K_c$ (damping to incoherence); the hypothesis targets the regime **above** $K_c$ (convergence to the partially-synchronized state). They are complementary, not competing.

## Technical caveats

- **Regularity requirement $n \geq 4$:** The authors note (p. 5) "we do not know if Landau damping holds for every, say $C^1$ perturbation, or if there can be arbitrarily small unstable (not $C^4$) perturbations for which $|\mathrm{R}(t)| \geq \delta > 0$ uniformly in time." This is an open regularity question.
- **Polynomial, not exponential, decay:** Chiba's resonance-pole approach gives exponential decay for analytic $g$ (Gaussian, rational). FGG's Volterra approach gives polynomial decay for finitely smooth $g$. For analytic $g$ both methods apply; Chiba's rate is sharper.
- **$K$-dependent smallness:** The perturbation must be small relative to $K_c - K$. As $K \to K_c^-$, $\epsilon_K \to 0$, consistent with the bifurcation at $K_c$.

## Cross-links

- [[kuramoto-stability-problem]] — FGG resolves the **below-threshold** half of the stability picture (nonlinear stability of incoherence for $K < K_c$)
- [[landau-damping]] — FGG provides the rigorous nonlinear proof of Landau damping in the Kuramoto model
- [[kuramoto-sakaguchi-equation]] — the PDE whose solutions FGG analyzes
- [[kinetic-formulation]] — the density-PDE framework within which the result lives
- [[chiba-2015-kuramoto-conjecture]] — the complementary spectral-theoretic approach reaching the same conclusion by different methods
- [[ott-antonsen-ansatz]] — FGG does NOT use the OA ansatz; their result applies on the full K-S state space
- [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] — targets the complementary above-threshold regime
