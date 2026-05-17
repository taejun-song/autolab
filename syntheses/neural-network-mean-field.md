---
type: synthesis
title: "Neural Network Mean-Field Theory: Connection to Kuramoto and Attack Strategy"
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[mei-montanari-nguyen-2018]]"
  - "[[chizat-bach-2018]]"
  - "[[rotskoff-vanden-eijnden-2018]]"
tags:
  - mean-field
  - dynamical-systems
  - pde
  - statistical-physics
  - synchronization
aliases:
  - neural-mf
  - nn-mean-field
---

# Neural Network Mean-Field Theory: Connection to Kuramoto and Attack Strategy

The mean-field theory of two-layer neural networks describes gradient descent as a Wasserstein gradient flow of an energy functional over probability measures on parameter space, yielding a McKean-Vlasov PDE structurally analogous to the Kuramoto-Sakaguchi equation.

## 1. Mathematical Setup

### The Model

A two-layer neural network with $m$ hidden units computes:

$$f_m(x) = \frac{1}{m} \sum_{i=1}^m a_i \sigma(w_i \cdot x)$$

where $w_i \in \mathbb{R}^d$ are input weights, $a_i \in \mathbb{R}$ are output weights, and $\sigma$ is the activation. In the mean-field parametrization, $\theta_i = (a_i, w_i) \in \mathbb{R}^{d+1}$ and the network is:

$$f_\mu(x) = \int \phi(x, \theta) \, d\mu(\theta), \quad \phi(x, \theta) = a \cdot \sigma(w \cdot x)$$

### The Mean-Field PDE

In the infinite-width limit $m \to \infty$, SGD with learning rate $\eta$ and noise $\beta^{-1}$ becomes the McKean-Vlasov PDE:

$$\partial_t \rho_t = \nabla_\theta \cdot \left( \rho_t \, \nabla_\theta \frac{\delta \mathcal{F}}{\delta \rho}[\rho_t] \right) + \beta^{-1} \Delta_\theta \rho_t$$

where the free energy is:

$$\mathcal{F}[\rho] = \mathcal{R}[\rho] + \beta^{-1} \mathcal{H}[\rho], \quad \mathcal{R}[\rho] = \frac{1}{2} \mathbb{E}_x \left| \int \phi(x,\theta) d\rho(\theta) - y(x) \right|^2$$

and $\mathcal{H}[\rho] = \int \rho \log \rho$ is the entropy. The first variation gives:

$$\frac{\delta \mathcal{F}}{\delta \rho}[\rho](\theta) = \mathbb{E}_x \left[ (f_\rho(x) - y(x)) \phi(x, \theta) \right] + \beta^{-1} \log \rho(\theta)$$

Without noise ($\beta = \infty$), this is the pure Wasserstein gradient flow:

$$\partial_t \rho_t = \nabla_\theta \cdot \left( \rho_t \, \nabla_\theta V_{\rho_t}(\theta) \right), \quad V_\rho(\theta) = \mathbb{E}_x[(f_\rho(x) - y(x)) \phi(x,\theta)]$$

### Key Papers

| Paper | Result |
|---|---|
| Mei-Montanari-Nguyen 2018 (arXiv:1804.06561) | Derived the PDE; proved SGD converges to it; landscape is "benign" in the mean-field limit |
| Chizat-Bach 2018 (arXiv:1805.09545) | Global convergence for homogeneous activations under full-support initialization |
| Rotskoff-Vanden-Eijnden 2018 (arXiv:1805.00915) | Interacting particle interpretation; LLN + CLT with O(1/n) error |
| De Bortoli-Durmus et al. 2020 (arXiv:2007.06352) | Quantitative propagation of chaos for SGD: O(1/sqrt(m)) in Wasserstein |
| Chen et al. 2025 (arXiv:2504.13110) | Propagation of chaos beyond logarithmic time |

## 2. Connection to Kuramoto

### Structural Parallel

| Kuramoto | Neural Network |
|---|---|
| Phase $\theta_i$ on $S^1$ | Parameter $\theta_i \in \mathbb{R}^{d+1}$ |
| Natural frequency $\omega_i$ | Data-dependent drift (implicit in loss gradient) |
| Mean-field coupling $K r \sin(\psi - \theta_i)$ | Mean-field coupling $V_\rho(\theta) = \mathbb{E}_x[(f_\rho - y)\phi(x,\theta)]$ |
| Order parameter $r = |\langle e^{i\theta}\rangle|$ | Prediction $f_\rho(x) = \int \phi(x,\theta) d\rho$ |
| Kuramoto-Sakaguchi PDE | McKean-Vlasov PDE above |
| Wasserstein gradient flow of $\int V d\rho$ | Wasserstein gradient flow of $\mathcal{F}[\rho]$ |
| Self-consistency equation $r = \Phi(r,K)$ | Fixed-point equation $\rho_\infty = \arg\min \mathcal{F}$ |

### Precise Mathematical Analogy

Both systems are **Wasserstein gradient flows** of a free energy with the structure:

$$\mathcal{F}[\rho] = \underbrace{\frac{1}{2}\langle \rho, W * \rho \rangle}_{\text{interaction}} + \underbrace{\int V d\rho}_{\text{confinement}} + \underbrace{\beta^{-1} \int \rho \log \rho}_{\text{entropy}}$$

For Kuramoto: $W(\theta, \theta') = -K \cos(\theta - \theta')$, $V(\theta) = -\omega\theta$.

For neural nets: $W(\theta, \theta') = \mathbb{E}_x[\phi(x,\theta)\phi(x,\theta')]$, $V(\theta) = -\mathbb{E}_x[y(x)\phi(x,\theta)]$.

The key difference is that the Kuramoto interaction kernel $W$ lives on the circle (compact) with explicit trigonometric structure, while the neural network kernel lives on $\mathbb{R}^{d+1}$ (noncompact) with data-dependent structure.

### What Transfers from Kuramoto

1. **Self-consistency fixed-point methods**: Our `sc_fixed_point_exists_continuum` technique (IVT on the self-consistency map) has a direct analogue for finding stationary states $\rho_\infty$.
2. **Lyapunov function approach**: The L2 Lyapunov $V = \int |\rho - \rho_\infty|^2$ or KL divergence plays the role of our $V_\infty = \int (α - α^*)^2 dμ$.
3. **Body-tail decomposition**: The truncation technique (restrict to $\{|\theta| \leq M\}$, show tail vanishes) applies directly.
4. **Persistence/invariance**: The $(0,1)$-invariance of the OA scalar ODE has an analogue in norm bounds on parameters under gradient flow.

## 3. Known Convergence Results

| Result | Conditions | Rate |
|---|---|---|
| Mei-Montanari-Nguyen 2018 | Noisy SGD ($\beta < \infty$), smooth activation | Global convergence to stationary point of $\mathcal{F}$ |
| Chizat-Bach 2018 | Homogeneous activation, full-support init | Global convergence (no rate) |
| Rotskoff-Vanden-Eijnden 2018 | Smooth activation, convexity at infinity | O(1/n) approximation error |
| Nitanda et al. 2022 | Log-Sobolev inequality for $\rho_\infty$ | Exponential convergence of Mean-Field Langevin |
| Chen et al. 2025 | Uniform convexity of $\mathcal{F}$ | PoC beyond $O(\log m)$ time |

### Open Gaps

- **No quantitative global convergence rate** for the noiseless ($\beta = \infty$) case under realistic (non-log-Sobolev) conditions.
- **Propagation of chaos** uniform in time remains open: existing results are either $O(\log m)$ time or require strong convexity.
- **Non-convex landscape**: without noise or displacement convexity, convergence to global minimum is not guaranteed.

## 4. Key Open Problem We Could Attack

**Problem**: Quantitative convergence rate for the mean-field neural network PDE under a Kuramoto-type self-consistency condition, without log-Sobolev or displacement convexity.

Specifically: Given a two-layer neural network in the mean-field regime with a loss functional $\mathcal{R}[\rho]$ that satisfies an analogue of the Kuramoto supercriticality condition $K > K_c$, prove that $\mathcal{R}[\rho_t] \to 0$ at a quantitative rate, using the body-tail decomposition and Lyapunov techniques developed for Kuramoto.

### Why This Is Tractable

1. We have a complete machine-checked proof of the analogous Kuramoto result (0 sorry, 0 axioms, 255 files).
2. The structural parallel is precise enough that individual lemmas can transfer.
3. The "body persistence" technique (truncate to bounded parameters, prove Gronwall on the body, show tail vanishes) is dimension-free and applies to the neural setting.

## 5. Attack Strategy

### Phase 1: Formal Framework (Lean skeleton)

Define the neural mean-field PDE in Lean 4, state the convergence theorem, identify the hypotheses that correspond to our Kuramoto hypotheses.

### Phase 2: Body-Tail Decomposition

Transfer the body-tail architecture:
- Body: $\{|\theta| \leq M\}$ — bounded parameters, where the loss is locally strongly convex.
- Tail: $\{|\theta| > M\}$ — prove $\rho_t(\{|\theta| > M\}) \to 0$ from moment bounds.
- Combine via $\mathcal{R}[\rho_t] \leq \mathcal{R}[\rho_t|_{\text{body}}] + C \cdot \rho_t(\text{tail})$.

### Phase 3: Body Convergence via Pair Bound

The "pair bound" technique from Kuramoto:
$$\frac{d}{dt} V_{\text{body}} \leq -\text{rate}(M) \cdot V_{\text{body}} + \text{forcing}(M)$$

becomes, for neural networks:
$$\frac{d}{dt} \text{KL}(\rho_t^M \| \rho_\infty^M) \leq -\lambda(M) \cdot \text{KL} + \text{boundary flux}(M)$$

where $\lambda(M)$ is the local log-Sobolev constant on the body.

### Phase 4: Global Assembly

Combine body convergence + tail vanishing via the ISS (input-to-state stability) framework we already have in Lean.

## 6. Feasibility Assessment

| Criterion | Assessment |
|---|---|
| Mathematical novelty | **Medium-high**: body-tail + ISS applied to neural MF is new |
| Difficulty vs. Kuramoto | **Harder**: noncompact state space, data-dependent kernel |
| Lean formalization difficulty | **Medium**: reuses 80% of existing infrastructure |
| Time to first result | **2-4 weeks** for skeleton + first body lemma |
| Publication potential | **High**: bridges two active communities (NN theory + Kuramoto/synchronization) |

### Risk Factors

1. The local log-Sobolev constant $\lambda(M)$ may degenerate as $M \to \infty$ in ways that don't happen for Kuramoto (where $\gamma \leq M$ gives explicit rate).
2. Self-consistency in neural nets is implicit (the loss depends on $\rho$ nonlinearly through the prediction $f_\rho$), unlike Kuramoto where $r = \int \alpha \, d\mu$ is explicit.
3. The entropy regularization ($\beta < \infty$) may be essential for the body-tail technique to work, unlike Kuramoto where we proved the deterministic case.

### Mitigation

Start with the entropy-regularized (noisy SGD) case where log-Sobolev tools are available, then attempt to push $\beta \to \infty$ by showing the convergence rate has controlled dependence on $\beta$.
