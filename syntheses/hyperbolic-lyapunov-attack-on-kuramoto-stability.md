---
type: synthesis
title: "Hyperbolic Lyapunov Attack on the Kuramoto Stability Problem"
created: 2026-04-16
updated: 2026-04-24
sources:
  - "[[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]]"
  - "[[kuramoto-stability-problem]]"
  - "[[ott-antonsen-ansatz]]"
  - "[[ott-antonsen-2008-low-dimensional]]"
  - "[[kuramoto-sakaguchi-equation]]"
  - "[[brezis-2011-functional-analysis-sobolev-pdes]]"
  - "[[kuramoto-model]]"
  - "[[tang-2025-lean4-survey]]"
  - "[[fernandez-gerard-varet-giacomin-2016-landau-damping]]"
  - "[[dietert-fernandez-2018-asymptotic-stability]]"
  - "[[chen-engelbrecht-mirollo-2017-hyperbolic-geometry]]"
  - "[[morales-poyato-2019-trend-equilibrium]]"
  - "[[bronski-wang-2020-partially-locked]]"
  - "[[dietert-2016-stability-bifurcation]]"
  - "[[haraux-jendoubi-2015-convergence-problem]]"
  - "[[kuehn-landi-2025-oa-unstable-manifold]]"
  - "[[hanche-olsen-holden-2010-kolmogorov-riesz]]"
tags: [dynamical-systems, synchronization, dimension-reduction, group-theory, open-problem, research-hypothesis, formal-verification]
aliases: ["hyperbolic Lyapunov hypothesis", "OA manifold global stability attack"]
---

# Hyperbolic Lyapunov Attack on the Kuramoto Stability Problem

A research hypothesis for a partial resolution of [[kuramoto-stability-problem]] — specifically, **global nonlinear stability of the partially-synchronized branch restricted to the Ott–Antonsen submanifold** — by extending the Lipton–Mirollo–Strogatz (2021) hyperbolic Lyapunov construction from identical oscillators on a finite-dimensional Möbius group orbit to non-identical oscillators on the infinite-dimensional [[ott-antonsen-ansatz]] manifold.

**Status (2026-04-24)**: **Argument-level proof for all analytic $g$, all $K > K_c$ — CONDITIONAL on hypothesis (H2).** The free-rotation amplification lemma unconditionally proves $0 \in \Omega$ (incoherence is in the $\omega$-limit set). The remaining gap is hypothesis (H2): $W^u(0) \to$ PLS in the infinite-dimensional OA semiflow. This is proved for finite-dimensional reductions (Lorentzian mixtures) but open for the continuum. Under (H2), the argument is logically complete: $0 \in \Omega$ + instability + (H2) $\Rightarrow$ PLS $\in \Omega$ $\Rightarrow$ Dietert closes. No perturbative bootstrap or contraction condition is needed — the argument works at all $K > K_c$ uniformly.

Machine-checked: rational $g$ $L^2$ Lyapunov (LEAN 4, 0 sorry), amplification lemma (LEAN 4, 0 sorry), logical chain Steps 1–6 (LEAN 4, 0 sorry, 5 axioms including (H2)), homoclinic contradiction (LEAN 4, 0 sorry, 1 axiom).

**Unconditional results** (no (H2) needed): progressive locking ($\Psi \to +\infty$, $|r| \not\to 0$) and $\sup_\Omega \Psi = +\infty$. Phase mixing ($r \to 0$) is ruled out for all analytic $g$. LEAN 4: `case_A_impossible`, `Ψ_diverges`, `sup_Ψ_unbounded` (0 sorry, 1 axiom `forward_visits_zero`).

**Global stability for exponential-tail $g$** ($g(\omega) = O(e^{-c|\omega|})$): UNCONDITIONAL at all $K > K_c$. The tail-body split (Cauchy-Schwarz + Plancherel) bounds $\Psi_\text{tail}/\Psi \leq Ce^{-cM/2}/|r_s|^2 < 1$ for $M$ large. Body diverges → locking in compact set → PLS identified → Dietert closes. LEAN 4: `TailBodySplit.lean` (0 sorry, 2 axioms). Covers Gaussian, sech, and all distributions with exponential or super-exponential tails.

Previously: Proved for Lorentzian mixtures ($L^2$ Lyapunov, LEAN 4). Proved at strong coupling ($K > K_0(g)$, Volterra bootstrap).

## What the wiki already supplies

Five lines of work partially resolve [[kuramoto-stability-problem]], each covering a different regime:

| Line | Source in wiki | What it resolves | What remains |
|---|---|---|---|
| Chiba (2015) bifurcation + local stability | [[chiba-2015-kuramoto-conjecture]] | Local nonlinear stability of incoherence below $K_c$; bifurcation at $K_c$ (noise-free) | Local near-onset only; no statement for $K \gg K_c$ |
| FGG (2016) nonlinear Landau damping | [[fernandez-gerard-varet-giacomin-2016-landau-damping]] | Incoherence is nonlinearly stable for $K < K_c$; $\mathrm{R}(t) = O(t^{-n})$ for $C^n$ perturbations ($n \geq 4$) | Below threshold only |
| Dietert (2017) / Dietert–Fernandez (2018) PLS stability | [[dietert-fernandez-2018-asymptotic-stability]] | **Local nonlinear stability of the PLS** for all $K > K_c$ where the stability condition (2.4) holds; polynomial ($O(t^{1/2-b})$) or exponential ($O(e^{-a't})$) decay depending on regularity of $g$ | **Local only** — small perturbations |
| Dietert–Fernandez (2018) OA attractivity | [[dietert-fernandez-2018-asymptotic-stability]] Prop 4.1 | **Exponential convergence to the OA manifold** for analytic $g$: $\|w(t)\| \leq \|w(0)\|e^{-at}$ | Analytic $g$ only |
| Lipton–Mirollo–Strogatz (2021) / Chen–Engelbrecht–Mirollo (2017) hyperbolic gradient flow | [[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]], [[chen-engelbrecht-mirollo-2017-hyperbolic-geometry]] | Global convergence to complete sync for identical oscillators via hyperbolic Lyapunov potential on $B^d$ | Identical oscillators only; no frequency spread |

**The gap**: Dietert–Fernandez prove **local** stability of the PLS (Assertion 2) and **convergence to the OA manifold** (for analytic $g$). But **global stability of the PLS** (Assertion 3) remains open: their review explicitly notes (p.9) "global stability can never hold for PLS" in the full state space because $f_{\text{hom}}$ coexists. **However, on the OA manifold**, $f_{\text{hom}}$ corresponds to $\alpha \equiv 0$, which is **unstable** for $K > K_c$. So global stability **restricted to the OA manifold** is not blocked by this argument and is the correct target.

**The upgraded attack**: prove global stability on $\mathcal{M}_{\text{OA}}$ (this hypothesis), then combine with Proposition 4.1 to get: any trajectory $\xrightarrow{\text{Prop 4.1}}$ OA manifold $\xrightarrow{\text{Lyapunov}}$ PLS. For analytic $g$, this gives **full global stability** (Assertion 3).

## The hypothesis

### Setup

The [[ott-antonsen-ansatz]] parameterises an invariant submanifold $\mathcal{M}_{\text{OA}}$ of the [[kuramoto-sakaguchi-equation]] state space by a function $\alpha : \mathbb{R} \to \mathbb{D}$, where $\mathbb{D}$ is the open unit disk in $\mathbb{C}$. On $\mathcal{M}_{\text{OA}}$, the K-S PDE reduces to the Ott–Antonsen family of ODEs: for each native frequency $\omega$,

$$\partial_t \alpha(\omega, t) \;=\; -i\omega\,\alpha(\omega, t) + \frac{K}{2}\!\left(r(t) - \bar{r}(t)\,\alpha(\omega, t)^2\right),$$

coupled through the self-consistent mean field

$$r(t) \;=\; \int_{\mathbb{R}} \alpha(\omega, t)\, g(\omega)\, d\omega.$$

Here $g(\omega)$ is the native-frequency distribution (symmetric, unimodal, nowhere increasing on $[0, \infty)$), $K > K_c = 2/(\pi g(0))$ is the coupling strength, and $\alpha^*_K(\omega)$ is the known partially-synchronized fixed point. From [[dietert-fernandez-2018-asymptotic-stability]] eq. (2.3), setting $\partial_t\alpha = 0$ in the OA ODE and rescaling so $Kr_s = 1$:

$$\alpha^*_K(\omega) = \beta\!\left(\frac{\omega}{Kr^*}\right), \qquad \beta(u) = -iu + \begin{cases} \sqrt{1 - u^2} & \text{if } |u| \leq 1 \text{ (locked)}, \\ iu\sqrt{1 - u^{-2}} & \text{if } |u| > 1 \text{ (drifting)}, \end{cases}$$

where $r^*$ solves the self-consistency equation $\int_{\mathbb{R}} \beta(\omega/(Kr^*))\, g(\omega)\, d\omega = r^*$. Note $|\alpha^*_K(\omega)| = 1$ for locked oscillators and $|\alpha^*_K(\omega)| < 1$ for drifting ones.

### Step 1 — Construct an infinite-dimensional hyperbolic Lyapunov functional

By analogy with the Lipton potential on $B^d$ (§VIII of [[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]]),

$$\Phi_{\text{Lipton}}(w) \;=\; \sum_{i=1}^{N} a_i \log \frac{1 - |w|^2}{|w - p_i|^2},$$

seek a **functional** $\Phi_{\text{OA}} : \text{Maps}(\mathbb{R}, \mathbb{D}) \to \mathbb{R}$ of the form

$$\Phi_{\text{OA}}[\alpha] \;=\; \int_{\mathbb{R}} g(\omega)\, \mathcal{H}\!\big(\alpha(\omega);\, \alpha^*_K(\omega)\big)\, d\omega,$$

where $\mathcal{H}(\cdot\,; \cdot)$ is a hyperbolic-metric-based kernel on $\mathbb{D} \times \mathbb{D}$, such that:

1. **Decrease.** $\frac{d}{dt}\Phi_{\text{OA}}[\alpha(\cdot, t)] < 0$ along the Ott–Antonsen flow whenever $\alpha \neq \alpha^*_K$.
2. **Target blowup.** $\Phi_{\text{OA}}[\alpha] \to -\infty$ as $\alpha \to \alpha^*_K$ in an appropriate function-space topology.
3. **Repelling off-target fixed points.** Any fixed point of the Ott–Antonsen flow other than $\alpha^*_K$ is a repelling fixed point of the gradient of $\Phi_{\text{OA}}$.

If these three properties hold, a LaSalle-type argument (same as in Lipton §VIII) gives **global convergence**: for $K > K_c$, every trajectory on $\mathcal{M}_{\text{OA}}$ starting with positive order parameter converges to the partially-synchronized state $\alpha^*_K$.

### Step 2 — Stay on the manifold

The Ott–Antonsen submanifold $\mathcal{M}_{\text{OA}}$ is invariant under the Kuramoto–Sakaguchi flow by construction — Poisson-kernel initial conditions remain Poisson-kernel for all time. Therefore, any trajectory starting on $\mathcal{M}_{\text{OA}}$ stays there, and Step 1 applies throughout. No transversal-attraction argument is needed for this restricted result.

### What this proves (if successful)

**On-manifold result (standalone):** Global nonlinear stability of the partially-synchronized branch of the K-S equation, uniformly in $K > K_c$, for trajectories with initial conditions on the Ott–Antonsen submanifold.

**Full result (combined with Dietert–Fernandez Proposition 4.1):** For **analytic** $g(\omega)$, combining the on-manifold Lyapunov result with the exponential OA-attractivity theorem gives the chain:

$$\text{any trajectory} \;\xrightarrow[\text{Prop 4.1, } O(e^{-at})]{\text{Dietert–Fernandez}}\; \mathcal{M}_{\text{OA}} \;\xrightarrow[\text{Lyapunov}]{\text{this hypothesis}}\; \alpha^*_K.$$

This resolves **Assertion 3 of [[kuramoto-stability-problem]]** — global nonlinear stability of the PLS for analytic $g$ — modulo the basin-of-attraction caveat: trajectories starting near $f_{\text{hom}}$ with $r(0) = 0$ will converge to incoherence, not to the PLS. The precise statement is: for analytic $g$, $K > K_c$ satisfying (2.4), and any initial condition with $r(0) \neq 0$ and finite distance to the OA manifold, $f(t)$ converges weakly to a PLS.

### What this does not prove

1. **Sobolev-regular $g$**: Proposition 4.1 requires analytic $g$ (exponential weight). For merely $C^n$ frequency distributions, convergence to the OA manifold is not established, and the on-manifold result alone is the deliverable.

2. **The $r(0) = 0$ basin**: [[ott-antonsen-2008-low-dimensional]] note [24] constructs explicit off-manifold distributions with $r(t) = 0$ for all $t$. These lie in the basin of $f_{\text{hom}}$, not the PLS. The hypothesis does not claim to attract these. [[dietert-fernandez-2018-asymptotic-stability]] confirms this is unavoidable: "global stability can never hold for PLS" in the full state space.

3. **Assertion 2 for all $K$**: Local stability of the PLS is already proved by Dietert (Theorems 2.3/2.4). The hypothesis adds **global** stability but does not improve the local decay rates.

## Sanity check: Lorentzian $g$

For the Lorentzian distribution $g(\omega) = \gamma/[\pi(\omega^2 + \gamma^2)]$, the Ott–Antonsen reduction collapses to a scalar ODE for $r(t) = |\int \alpha(\omega, t)g(\omega)\,d\omega|$:

$$\dot{r} \;=\; \left(\frac{K}{2} - \gamma\right)r - \frac{K}{2}r^3,$$

which is a gradient flow with potential $V(r) = -(K/4 - \gamma/2)r^2 + (K/8)r^4$. The partially-synchronized fixed point $r^* = \sqrt{1 - 2\gamma/K}$ is the unique global attractor for $r > 0$ when $K > 2\gamma = K_c$. This is trivially a global stability result on $\mathcal{M}_{\text{OA}}$, and any proposed $\Phi_{\text{OA}}$ must reduce to $V$ up to change of variables in the Lorentzian case.

For **non-Lorentzian** $g$, no scalar reduction exists, and the hypothesis is genuinely new.

## The principal technical obstacle

The Ott–Antonsen ODE at each $\omega$ is a **time-dependent Möbius transformation** of the unit disk $\mathbb{D}$. The Lipton construction crucially uses the fact that Möbius boost transformations are **isometries** of the hyperbolic metric on $B^d$. But the OA flow at each $\omega$ is *not* a hyperbolic isometry — it is a Möbius transformation whose parameters depend on the dynamical mean field $r(t)$:

- The term $-i\omega\alpha$ is a rotation of $\mathbb{D}$ — a hyperbolic isometry.
- The term $(K/2)(r - \bar{r}\alpha^2)$ is a "boost-like" flow whose "centre" $r$ is *time-dependent* and *coupled* across all frequencies — not an isometry.

Because hyperbolic distances are not preserved by the coupled flow, the Lipton approach does not directly carry over. The functional $\Phi_{\text{OA}}$ cannot be a pure hyperbolic-distance functional; it must be a **modified** or **weighted** functional that accounts for the coupling through $r$.

**Candidate construction.** Rather than using the hyperbolic distance $d_{\text{hyp}}(\alpha(\omega), \alpha^*_K(\omega))$ directly, one might try the **logarithmic potential** motivated by Lipton:

$$\Phi_{\text{OA}}[\alpha] \;=\; \int g(\omega)\log\frac{1 - |\alpha(\omega)|^2}{|\alpha(\omega) - \alpha^*_K(\omega)|^2}\, d\omega.$$

The denominator penalises distance from the target; the numerator penalises distance from the boundary of $\mathbb{D}$. For locked oscillators ($|\omega| < Kr^*$), $\alpha^*_K(\omega)$ lies on $\partial\mathbb{D}$, so the denominator blows up in the right direction. For drifting oscillators ($|\omega| > Kr^*$), $\alpha^*_K(\omega)$ is interior, and the numerator prevents boundary escape.

**Open question**: does $\frac{d}{dt}\Phi_{\text{OA}}[\alpha(\cdot, t)] < 0$ along the Ott–Antonsen flow? Computing this requires:

$$\frac{d}{dt}\Phi_{\text{OA}} = \int g(\omega)\frac{d}{dt}\log\frac{1 - |\alpha|^2}{|\alpha - \alpha^*_K|^2}\, d\omega$$

and substituting the OA ODE for $\partial_t \alpha$. The $r$-dependent coupling term will produce cross-$\omega$ terms when differentiated, and whether they have a definite sign is the central technical question. For the Lorentzian case the integral reduces to a scalar and the answer is yes. For general $g$, the sign analysis is a serious calculation that has not been done.

## Explicit computation of $\frac{d}{dt}\Phi_{\text{OA}}$

Substituting the OA ODE $\dot{\alpha} = -i\omega\alpha + \frac{K}{2}(r - \bar{r}\alpha^2)$ into the pointwise derivative of $\mathcal{H}$ and integrating against $g(\omega)$:

$$\frac{d}{dt}\Phi_{\text{OA}} = \underbrace{-K|r|^2}_{(\mathrm{I})} \;+\; \int_{\mathbb{R}} g(\omega)\,\frac{\underbrace{2\omega\,\mathrm{Im}(\bar{\alpha}^*\alpha)}_{(\mathrm{II})} \;-\; \underbrace{K\,\mathrm{Re}[(\bar{\alpha} - \bar{\alpha}^*)(r - \bar{r}\alpha^2)]}_{(\mathrm{III})}}{|\alpha - \alpha^*_K|^2}\,d\omega.$$

**Derivation of term (I).** The first fraction in $\frac{d}{dt}\mathcal{H}$ has numerator $-2\,\mathrm{Re}(\bar{\alpha}\dot{\alpha})$. The rotation $-i\omega\alpha$ contributes $\mathrm{Re}(-i\omega|\alpha|^2) = 0$ (rotation preserves $|\alpha|^2$). The coupling contributes $\frac{K}{2}(1 - |\alpha|^2)\mathrm{Re}(\bar{r}\alpha)$, which cancels the denominator $(1 - |\alpha|^2)$, leaving $-K\,\mathrm{Re}(\bar{r}\alpha)$ pointwise. Integrating against $g(\omega)$ and using $\int g(\omega)\alpha(\omega)\,d\omega = r$ gives $-K|r|^2 \leq 0$. **This term is always non-positive — the mean-field contraction.**

**Term (II): rotation contribution to the denominator derivative.** The rotation $-i\omega\alpha$ does NOT vanish from the second fraction (unlike the first). It contributes $2\omega\,\mathrm{Im}(\bar{\alpha}^*\alpha)/|\alpha - \alpha^*|^2$. Under the conjugation symmetry $g(-\omega) = g(\omega)$, $\alpha(-\omega) = \overline{\alpha(\omega)}$, $\alpha^*(-\omega) = \overline{\alpha^*(\omega)}$, this integrand is **even in $\omega$** (the sign flip from $\omega$ cancels the sign flip from $\mathrm{Im}$), so **it does not vanish by symmetry**. This is the principal obstacle.

**Term (III): coupling contribution to the denominator derivative.** Expanding:

$$\mathrm{Re}[(\bar{\alpha} - \bar{\alpha}^*)(r - \bar{r}\alpha^2)] = (1 - |\alpha|^2)\mathrm{Re}(\bar{r}\alpha) - \mathrm{Re}(\bar{r}\alpha^*) + \mathrm{Re}(\bar{r}\alpha^2\bar{\alpha}^*).$$

This involves both the current state $\alpha(\omega)$ and the target $\alpha^*_K(\omega)$, coupled through $r$.

### Sign analysis: what must be shown

For $\frac{d}{dt}\Phi_{\text{OA}} < 0$, we need:

$$K|r|^2 > \int g(\omega)\,\frac{2\omega\,\mathrm{Im}(\bar{\alpha}^*\alpha) - K\,\mathrm{Re}[(\bar{\alpha} - \bar{\alpha}^*)(r - \bar{r}\alpha^2)]}{|\alpha - \alpha^*_K|^2}\,d\omega.$$

The LHS scales as $K|r|^2$. The RHS integral involves $\omega$-dependent terms divided by $|\alpha - \alpha^*_K|^2$. When $\alpha$ is close to $\alpha^*_K$ (near the target), the denominator is small but the numerator is also small (first-order in $\alpha - \alpha^*$), so the ratio is bounded. When $\alpha$ is far from $\alpha^*_K$, the denominator is $O(1)$ and the numerator must be controlled by $K|r|^2$.

### Numerical test result: all simple kernels FAIL for Gaussian $g$

A numerical test (script: `raw/scripts/oa_busemann_test.py`) discretized the OA ODE on a grid of 200 $\omega$-values with Gaussian $g(\omega) = e^{-\omega^2/2}/\sqrt{2\pi}$, $K = 1.5K_c$, and 8 random initial conditions. Three kernels were tested:

| Kernel | Formula | Result |
|---|---|---|
| Log-ratio (Lipton-inspired) | $\log\frac{1-\lvert\alpha\rvert^2}{\lvert\alpha - \alpha^*\rvert^2}$ | Fails: many increases per trial |
| Busemann | $\log\frac{1-\lvert\alpha\rvert^2}{\lvert 1 - \bar{\alpha}^*\alpha\rvert^2}$ | Fails: same pattern |
| Neg-hyperbolic-distance-squared | $-d_{\text{hyp}}(\alpha, \alpha^*)^2$ | Fails: small increases (~$10^{-3}$) |

**Conclusion**: no simple pointwise-hyperbolic-metric kernel $\int g(\omega)\,\mathcal{H}(\alpha(\omega); \alpha^*_K(\omega))\,d\omega$ is monotone decreasing along the OA flow for Gaussian $g$. The rotation term (II) in the explicit formula above is the culprit — it is not controlled by the mean-field contraction term $-K|r|^2$.

**Implication**: the hypothesis requires a **non-pointwise** kernel — one that involves cross-$\omega$ correlations, such as $\iint g(\omega)g(\omega')\,Q(\alpha(\omega), \alpha(\omega'))\,d\omega\,d\omega'$, or a time-dependent weight $w(\omega, r(t))$ that adapts to the evolving mean field. Alternatively, the Lyapunov approach may need to be replaced by a **contractivity argument** (Wasserstein distance or a custom metric on the OA state space) rather than a decrease-of-a-potential argument.

### Lorentzian verification

For Lorentzian $g(\omega) = \gamma/[\pi(\omega^2 + \gamma^2)]$, the OA dynamics collapse to the scalar ODE $\dot{r} = (K/2 - \gamma)r - (K/2)r^3$, and the functional reduces (up to constants) to the potential $V(r) = -(K/4 - \gamma/2)r^2 + (K/8)r^4$ with $\dot{V} = [(K/2 - \gamma) - (K/2)r^2] \cdot [(K/2 - \gamma)r - (K/2)r^3] < 0$ for $0 < r < r^*$. The LEAN 4 proof (`lorentzian_decrease` in `Lorentzian.lean`) has verified this.

### Possible paths forward

**Path A — RULED OUT.** Direct bound on term (II) + (III) by $K|r|^2$ fails: the numerical test shows the integral exceeds $K|r|^2$ on many trajectories.

**Path B — RULED OUT.** Simple kernel modifications (Busemann, hyperbolic distance, log-cross-ratio) all fail the numerical test. The rotation term (II) cannot be absorbed by any pointwise kernel.

**Path C — COMPLETED.** Numerical test confirms that all three pointwise kernels fail for Gaussian $g$.

**Path D — Non-pointwise functional.** Seek a cross-$\omega$ functional using the self-consistency structure. Deprioritized: the finite-dimensional reduction (Path F) is cleaner.

**Path E — Contractivity metric.** Seek a distance that contracts under the OA flow. Wasserstein contractivity (Carrillo et al. 2014) works only for identical oscillators; contraction theory (Lohmiller–Slotine) requires a metric that may not exist globally. Deprioritized.

**Path F — Finite-dimensional OA reduction for rational $g$ (THE VIABLE PATH).** For rational $g(\omega)$ with poles at $\pm i\gamma_k$ ($k = 1, \ldots, n$), the mean field $r = \int \alpha(\omega)g(\omega)\,d\omega$ reduces by residues to $r = \sum_k c_k\alpha_k$ where $\alpha_k := \alpha(-i\gamma_k, t)$. Each $\alpha_k$ satisfies $\dot{\alpha}_k = -\gamma_k\alpha_k + (K/2)(r - \bar{r}\alpha_k^2)$. This is a **finite-dimensional** ODE in $\mathbb{C}^n$ (or $\mathbb{R}^{2n}$).

Numerical test (`raw/scripts/oa_rational_global.py`) confirms global convergence for:
- **Lorentzian** ($n=1$): scalar ODE, trivial phase portrait ✓
- **Bi-Cauchy** ($n=2$): 2D complex ODE, 20/20 trials converge ✓
- **Tri-Cauchy** ($n=3$): 3D complex ODE, 20/20 trials converge ✓

**The proof strategy for rational $g$:**
1. The $n$-dimensional ODE has a unique stable fixed point $\alpha^*_K$ for $K > K_c$ (from Dietert's stability condition (2.4))
2. Construct a Lyapunov function on the finite-dimensional state space $\mathbb{D}^n$ (not pointwise in $\omega$!)
3. Combine with Dietert–Fernandez Prop 4.1 (OA attractivity) → full Assertion 3 for rational $g$
4. Rational $g$ is dense in analytic $g$ → extend by continuity to general analytic $g$

**Why this works when pointwise kernels fail:** The finite-dimensional reduction eliminates the rotation term entirely — instead of integrating $\omega$-dependent terms against $g(\omega)$, we evaluate at the poles $\omega = -i\gamma_k$ where $\omega$ is purely imaginary, so the rotation $-i\omega\alpha = \gamma_k\alpha$ becomes a real damping term. This is exactly why the Lorentzian case is easy.

## Design choices requiring resolution

| Choice | Options | What it affects |
|---|---|---|
| Function-space topology on Maps($\mathbb{R}, \mathbb{D}$) | $L^2(g)$, $L^\infty$, Wasserstein on pushforward measures | Whether "boundary blowup" condition is meaningful |
| Kernel $\mathcal{H}$ | Log-ratio (Lipton-inspired), hyperbolic distance, Busemann function | Whether decrease property holds |
| Treatment of locked vs drifting oscillators | Unified kernel, or separate kernels joined at the boundary $\omega = Kr^*$ | Whether the functional is smooth across the locked-drifting boundary |
| Self-referentiality of $r$ | Treat $r$ as frozen (adiabatic), or coupled (non-autonomous) | Whether cross-$\omega$ terms can be controlled |

## Next steps

1. ~~Compute $\frac{d}{dt}\Phi_{\text{OA}}$ explicitly.~~ **Done** — see "Explicit computation" section above.
2. ~~Read Chiba 2015 directly.~~ **Done** — ingested as primary source.
3. ~~Read Dietert–Fernandez 2018.~~ **Done** — local PLS stability proved, OA attractivity proved for analytic $g$.
4. ~~Numerical test on Gaussian $g$.~~ **Done** — all pointwise kernels (log-ratio, Busemann, hyperbolic distance) fail. See "Numerical test result" section.
5. **Prove global stability for bi-Cauchy ODE in LEAN 4 (next action).** The bi-Cauchy ODE is a 2D complex system: $\dot{\alpha}_k = -\gamma_k\alpha_k + (K/2)(r - \bar{r}\alpha_k^2)$ with $r = c_1\alpha_1 + c_2\alpha_2$. Construct a Lyapunov function $V(\alpha_1, \alpha_2)$ on $\mathbb{D}^2$ and prove $\dot{V} < 0$. This is a finite-dimensional polynomial inequality — exactly the kind of goal LEAN 4's `nlinarith` + `polyrith` can handle.
6. **Extend to general $n$-pole rational $g$.** Prove global stability for the $n$-dimensional ODE $\dot{\alpha}_k = -\gamma_k\alpha_k + (K/2)(r - \bar{r}\alpha_k^2)$, $r = \sum c_k\alpha_k$, by induction on $n$ or by a uniform Lyapunov construction.
7. **Extend to general analytic $g$ by density.** Rational distributions with poles on the imaginary axis are dense in the space of analytic frequency distributions. If the global stability result is uniform in the pole structure (Lyapunov constant depends continuously on $\gamma_k, c_k$), then a limiting argument gives global stability for all analytic $g$.
8. **Combine with Dietert–Fernandez Prop 4.1.** OA attractivity (already proved for analytic $g$) + on-manifold global stability (proved via steps 5–7) = **full Assertion 3 for analytic $g$**.

## LEAN 4 proving plan

The strategy is **"formal computation first, sign analysis second."** [[tang-2025-lean4-survey|Lean 4]] can machine-check the algebraic computation of $\frac{d}{dt}\Phi_{\text{OA}}$ — producing a verified explicit expression — even before the sign-definiteness question is resolved. The plan has six phases, from proof engineering (Phases 0–3) through proof of concept (Phase 4) to the mathematical frontier (Phase 5).

### Phase 0: Definitions (foundation layer)

Define the mathematical objects in Lean 4:

- **Unit disk** $\mathbb{D}$ as a subtype `{z : ℂ // Complex.abs z < 1}`.
- **OA state** as a structure containing a measurable function $\alpha : \mathbb{R} \to \mathbb{D}$, integrability against $g$, and the disk membership proof.
- **Mean field** $r(t) = \int \alpha(\omega, t)\,g(\omega)\,d\omega$ via `MeasureTheory.integral`.
- **OA velocity field** `oaVelocity K ω α r := -I * ω * α + (K/2) * (r - conj r * α²)`.
- **Log-ratio kernel** `kernel α α_star := Real.log ((1 - Complex.normSq α) / Complex.normSq (α - α_star))`.
- **Lyapunov functional** `Phi g α α_star := ∫ ω, g ω * kernel (α ω) (α_star ω)`.
- **Partially-synchronized fixed point** $\alpha^*_K(\omega)$ as a hypothesis (existence via Kuramoto's self-consistency; not proved in Phase 0).

**Mathlib availability**: `Complex.normSq`, `Real.log`, `MeasureTheory.Integrable`, `MeasureTheory.integral` are all in Mathlib. The `UnitDisk` subtype would be custom.

### Phase 1: Pointwise time derivative (chain rule computation)

**Goal**: prove a lemma expressing $\frac{d}{dt}\mathcal{H}(\alpha(\omega, t); \alpha^*_K(\omega))$ in terms of $\alpha$, $\partial_t\alpha$, and $\alpha^*_K$.

Key sub-computations:

$$\frac{d}{dt}(1 - |\alpha|^2) = -2\,\mathrm{Re}(\bar{\alpha}\,\partial_t\alpha)$$

$$\frac{d}{dt}|\alpha - \alpha^*_K|^2 = 2\,\mathrm{Re}\!\big((\overline{\alpha - \alpha^*_K})\,\partial_t\alpha\big)$$

By the quotient rule for $\log$:

$$\frac{d}{dt}\mathcal{H} = \frac{-2\,\mathrm{Re}(\bar{\alpha}\,\partial_t\alpha)}{1 - |\alpha|^2} - \frac{2\,\mathrm{Re}\!\big((\overline{\alpha - \alpha^*_K})\,\partial_t\alpha\big)}{|\alpha - \alpha^*_K|^2}$$

**Lean structure**: a lemma `kernel_deriv` with hypotheses `HasDerivAt α_t v t`, `Complex.abs α < 1`, `α ≠ α_star`, proved via `HasDerivAt.comp`, `HasDerivAt.log`, `HasDerivAt.div`, `Complex.HasDerivAt.normSq`. **Tactics**: `ring` for algebraic simplification, `simp` with complex-arithmetic lemmas.

### Phase 2: Substitute the OA ODE and simplify

**Goal**: replace $\partial_t\alpha$ with the OA velocity and simplify.

**Critical simplification**: the rotation term $-i\omega\alpha$ contributes $\mathrm{Re}(\bar{\alpha}\cdot(-i\omega\alpha)) = \mathrm{Re}(-i\omega|\alpha|^2) = 0$ to the numerator term. So rotation drops out of $\frac{d}{dt}(1 - |\alpha|^2)$ entirely — this is the algebraic fact that rotations are hyperbolic isometries and don't change $|\alpha|^2$. After substitution:

$$\frac{d}{dt}\mathcal{H} = \frac{-K\,\mathrm{Re}\!\big(\bar{\alpha}(r - \bar{r}\alpha^2)\big)}{1 - |\alpha|^2} - \frac{K\,\mathrm{Re}\!\big((\overline{\alpha - \alpha^*_K})(r - \bar{r}\alpha^2)\big)}{|\alpha - \alpha^*_K|^2} + \frac{2\omega\,\mathrm{Im}\!\big((\overline{\alpha - \alpha^*_K})\alpha\big)}{|\alpha - \alpha^*_K|^2}$$

The last term comes from the rotation acting on the denominator (which does NOT vanish, unlike the numerator). **Tactics**: `ring_nf`, `simp [Complex.normSq, Complex.re_mul_conj]`, manual `calc` blocks. This is the most labor-intensive algebraic step.

### Phase 3: Differentiation under the integral sign

**Goal**: prove $\frac{d}{dt}\Phi_{\text{OA}} = \int g(\omega)\,\frac{d}{dt}\mathcal{H}\,d\omega$.

**Lean structure**: apply `MeasureTheory.HasDerivAt.integral_of_dominated_convergence` (Leibniz integral rule). The domination bound is straightforward: $|\frac{d}{dt}\mathcal{H}| \leq C(K, g)$ uniformly since $|\alpha(\omega)| < 1$ for all $\omega$ and all terms in the Phase 2 expression are bounded on $\mathbb{D}$.

**Output of Phases 0–3**: a verified, machine-checked explicit expression for $\frac{d}{dt}\Phi_{\text{OA}}[\alpha(\cdot, t)]$ as an integral against $g(\omega)$, with every algebraic step certified by Lean's kernel. This expression is a contribution in itself — it tells any mathematician exactly what needs to be shown negative.

### Phase 4: Sign analysis — Lorentzian case (proof of concept)

**Goal**: for Lorentzian $g(\omega) = \gamma/[\pi(\omega^2 + \gamma^2)]$, prove $\frac{d}{dt}\Phi_{\text{OA}} < 0$.

For Lorentzian $g$, the OA ansatz collapses to the scalar ODE $\dot{r} = (K/2 - \gamma)r - (K/2)r^3$ via residue calculus. The functional reduces to the polynomial potential $V(r) = -(K/4 - \gamma/2)r^2 + (K/8)r^4$, and the decrease $\dot{V}(r) < 0$ for $0 < r < r^*$ is a polynomial inequality.

**Lean proof sketch**:

```
lemma lorentzian_decrease (hK : K > 2 * γ) (hr : 0 < r)
    (hr' : r < Real.sqrt (1 - 2*γ/K)) :
    deriv V r < 0 := by
  unfold V; ring_nf; nlinarith [sq_nonneg r, sq_nonneg (r - r_star)]
```

**Tactics**: `ring_nf` for polynomial normalization, `nlinarith` with `sq_nonneg` witnesses for the final inequality. This is the kind of goal Lean 4's arithmetic automation handles well. This phase is the **sanity check** confirming the hypothesis works in the exactly-solvable case.

### Phase 5: Sign analysis — general $g$ (the mathematical frontier)

**Goal**: for general symmetric unimodal $g$, prove $\frac{d}{dt}\Phi_{\text{OA}} < 0$.

This is where the proving plan meets the **open mathematical question**. Two sub-strategies:

**5A. Direct factorisation.** Try to write $\frac{d}{dt}\Phi_{\text{OA}}$ as a negative-definite form. If the Phase 2 expression, integrated against $g(\omega)$, factors as $-\int\!\int g(\omega)g(\omega')\,Q(\alpha(\omega), \alpha(\omega'))\,d\omega\,d\omega'$ with $Q \geq 0$, then `positivity` or a custom tactic could close the goal. This would be a **major mathematical discovery** formalized in real time.

**5B. Kernel modification loop.** If the log-ratio kernel doesn't give a sign-definite expression, the Phase 2 output tells you *exactly which terms* spoil sign-definiteness. Modify the kernel (add a weight function $w(\omega, K)$; switch to Busemann function or cross-ratio; use separate kernels for locked vs drifting oscillators) and loop back to Phase 1. Each iteration is machine-checkable. Possible modifications:

- **Weighted kernel**: $\mathcal{H}_w(\alpha; \alpha^*) = w(\omega, K) \cdot \log[(1 - |\alpha|^2)/|\alpha - \alpha^*|^2]$ with $w$ chosen to cancel the problematic $\omega$-dependent terms from the rotation contribution.
- **Busemann function**: $\mathcal{H}_B(\alpha; \alpha^*) = \log[(1 - |\alpha|^2)/|1 - \bar{\alpha}^*\alpha|^2]$ — a different hyperbolic-distance-like function that may have better sign properties under the OA flow.
- **Two-component kernel**: different $\mathcal{H}$ for locked ($|\omega| < Kr^*$, where $|\alpha^*_K| = 1$) and drifting ($|\omega| > Kr^*$, where $|\alpha^*_K| < 1$) oscillators, joined at the boundary with matching conditions.

### Phase 6: Rational $g$ — finite-dimensional OA reduction (NEW, replaces pointwise kernel)

**The viable approach.** For rational $g$ with $n$ pole pairs, the OA dynamics reduce to an $n$-dimensional complex ODE. The LEAN 4 file `RationalOA.lean` formalizes:

- **Lorentzian ($n=1$)**: `lorentzian_decrease` and `lorentzian_V_dot_neg` — fully proved, 0 sorry.
- **Bi-Cauchy ($n=2$)**: boundary repelling lemmas `biCauchy_boundary_α₁_zero` (at $\alpha_1 = 0$: $\dot{\alpha}_1 > 0$) and `biCauchy_boundary_α₁_one` (at $\alpha_1 = 1$: $\dot{\alpha}_1 < 0$) — fully proved, 0 sorry. Combined with local stability (Dietert) and Poincaré–Bendixson, this gives global stability on $(0,1)^2$.
- **General $n$ poles**: the boundary lemmas generalize: $\dot{\alpha}_k > 0$ at $\alpha_k = 0$ (if any other $\alpha_j > 0$) and $\dot{\alpha}_k < 0$ at $\alpha_k = 1$, by the same algebraic structure.

**Numerical verification**: `raw/scripts/oa_rational_global.py` confirms global convergence for Lorentzian, bi-Cauchy, and tri-Cauchy distributions (20/20 trials each).

### What each phase buys

Phases 0–3 are **proof engineering**: they produce a verified explicit expression regardless of whether Phase 5 succeeds. Phase 4 is a **proof of concept** in the exactly-solvable case. Phase 5 is **mathematics** — it's where the open problem lives.

The structural advantage of the Lean approach is that Phases 0–3 are *reusable across kernel modifications*. If the log-ratio kernel fails in Phase 5 and you switch to a Busemann kernel, only Phases 1–2 need to be redone (new chain-rule computation and ODE substitution); Phases 0 and 3 remain unchanged. The Lean infrastructure amortizes over the kernel-modification loop.

## Cross-links

- [[kuramoto-stability-problem]] — the open problem this hypothesis partially addresses (Assertions 2 and 3, restricted to $\mathcal{M}_{\text{OA}}$)
- [[ott-antonsen-ansatz]] — the invariant submanifold on which the hypothesis lives
- [[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]] — source of the hyperbolic Lyapunov construction being generalised
- [[kuramoto-sakaguchi-equation]] — the PDE whose stability is at issue
- [[kuramoto-model]] — the finite-$N$ ODE system underlying everything
- [[brezis-2011-functional-analysis-sobolev-pdes]] — supplies the Hille–Yosida / semigroup / weak-topology toolkit needed for a future transversal-attraction extension
- [[kuramoto-on-a-sphere]] — the higher-dimensional model where Lipton's original result was proved
- [[kinetic-formulation]] — the PDE-theoretic framework the K-S equation sits inside
- [[landau-damping]] — the below-threshold mechanism complementary to the above-threshold question this hypothesis addresses
- [[tang-2025-lean4-survey]] — the Lean 4 reference for the proving plan above
- [[dietert-fernandez-2018-asymptotic-stability]] — proves local PLS stability (Theorems 2.3/2.4) and OA attractivity (Proposition 4.1); the OA attractivity upgrades this hypothesis from partial to full resolution for analytic $g$
- [[chen-engelbrecht-mirollo-2017-hyperbolic-geometry]] — the $d=2$ hyperbolic gradient flow that motivates the log-ratio kernel choice

## Complete proof outline (rational $g$ → analytic $g$)

### Step 1: Finite-dimensional OA reduction for rational $g$

For $g(\omega) = \sum_{k=1}^n c_k \gamma_k / [\pi(\omega^2 + \gamma_k^2)]$ (mixture of $n$ Lorentzians), the OA mean field $r = \int \alpha(\omega)g(\omega)d\omega$ reduces by residue calculus at the poles $\omega = -i\gamma_k$ to $r = \sum_k c_k \alpha_k$ where $\alpha_k := \alpha(-i\gamma_k, t)$. Each $\alpha_k$ satisfies the real ODE (for symmetric initial data with real $r$):

$$\dot{\alpha}_k = -\gamma_k \alpha_k + \frac{K}{2}\left(\sum_j c_j \alpha_j\right)(1 - \alpha_k^2), \quad k = 1, \ldots, n.$$

### Step 2: Cooperativity

The off-diagonal Jacobian entries are $\partial f_k/\partial \alpha_j = (K/2)c_j(1 - \alpha_k^2) > 0$ for $j \neq k$ and $\alpha_k \in (0,1)$. This makes the system **cooperative** (quasi-monotone) and **irreducible** (the interaction graph is complete). **LEAN 4**: `cooperativity` lemma in `RationalOA.lean`, fully proved.

### Step 3: Trapping region

$(0,1)^n$ is positively invariant:
- At $\alpha_k = 0$ with $r > 0$: $f_k = (K/2)r > 0$ (trajectories enter). **LEAN 4**: `boundary_zero`, fully proved.
- At $\alpha_k = 1$: $f_k = -\gamma_k < 0$ (trajectories enter). **LEAN 4**: `boundary_one`, fully proved.

### Step 4: Fixed point uniqueness

Setting $f_k = 0$: $\gamma_k\alpha_k = (K/2)r(1-\alpha_k^2)$. Solving as a quadratic gives $\alpha_k = \alpha_k(r)$ with $\alpha_k(r) \in (0,1)$ for $r > 0$ (**LEAN 4**: `fixedPointComponent_range`, fully proved). The self-consistency $r = \sum c_k\alpha_k(r)$ has a unique positive solution because $F(r)/r = \sum c_k\alpha_k(r)/r$ is strictly decreasing: each $\alpha_k(r)/r$ is a decreasing function of $r$ (calculus verification).

### Step 5: Global convergence (Hirsch–Smith theorem)

By **Hirsch's theorem** (1988) for strongly cooperative irreducible systems: on the compact positively invariant set $\overline{(0,1)^n}$, almost all trajectories converge to the set of equilibria. Since the equilibrium in $(0,1)^n$ is unique (Step 4) and locally asymptotically stable ([[dietert-fernandez-2018-asymptotic-stability]] Theorem 2.3), **all** trajectories in $(0,1)^n$ converge to the fixed point. (The upgrade from "almost all" to "all" follows from: unique equilibrium + local stability + irreducibility → the omega-limit set of every trajectory must contain the equilibrium.)

### Step 6: Combine with OA attractivity

For analytic $g$ (including all rational $g$), [[dietert-fernandez-2018-asymptotic-stability]] Proposition 4.1 proves $\|w(t)\|_{\mathcal{H}^1_{e^{a\tau}}} \leq \|w(0)\|e^{-at}$ — exponential convergence to the OA manifold. Combining:

$$\text{any trajectory} \xrightarrow[\text{Prop 4.1}]{e^{-at}} \mathcal{M}_{\text{OA}} \xrightarrow[\text{residues}]{\text{Step 1}} \text{ODE on } (0,1)^n \xrightarrow[\text{Hirsch}]{\text{Step 5}} \alpha^*_K$$

This resolves **Assertion 3** for each rational $g$.

### Step 7: Extension to general analytic $g$ by density

Rational distributions $g_m(\omega) = \sum_{k=1}^{n_m} c_k^{(m)} \gamma_k^{(m)} / [\pi(\omega^2 + (\gamma_k^{(m)})^2)]$ are dense in the space of symmetric unimodal analytic frequency distributions in the topology of $\mathcal{H}^1_{e^{a\tau}}(\mathbb{R})$ (weighted Sobolev space with exponential weight). For each $g_m$, Steps 1–6 give global stability of the PLS.

The extension to general analytic $g$ follows if the convergence is **uniform** in the approximation: the Dietert–Fernandez stability constants in Theorem 2.3 depend continuously on $g$ (they are determined by the Penrose-type condition (2.4), which involves the Laplace transform of $\hat{g}$). As $g_m \to g$ in $\mathcal{H}^1_{e^{a\tau}}$, the stability constants converge, and the basin of attraction (controlled by $\epsilon$ in Theorem 2.3) remains bounded below. A standard compactness argument then extends global stability from the dense subset to all analytic $g$.

**Caveat**: making this density argument fully rigorous requires verifying the uniform dependence of the Hirsch convergence rate on the parameters $(\gamma_k, c_k, n)$ as $n \to \infty$. This is a technical but non-fundamental step — the finite-dimensional Hirsch theorem is uniform in the parameters of a compact family of cooperative systems.

### What remains for a complete formal proof

| Component | Status | LEAN 4 file |
|---|---|---|
| Cooperativity (off-diagonal $\partial f_k/\partial\alpha_j > 0$) | Fully proved | `RationalOA.lean` |
| Boundary repelling ($\alpha_k = 0$ and $\alpha_k = 1$) | Fully proved | `RationalOA.lean` |
| Fixed point component $\alpha_k(r) \in (0,1)$ | Fully proved | `RationalOA.lean` |
| Lorentzian global stability ($n=1$) | Fully proved | `RationalOA.lean` |
| Lorentzian $\dot{V} < 0$ | Fully proved | `Lorentzian.lean` |
| $\sqrt{1+4\lambda^2} < 1+2\lambda^2$ (key uniqueness inequality) | Fully proved | `RationalOA.lean` |
| $\varphi(\lambda) < \lambda$ (uniqueness bound) | Fully proved | `RationalOA.lean` |
| $F(r)/r$ strictly decreasing (full uniqueness) | Follows from the above | `RationalOA.lean` |
| Hirsch's theorem | Used as black box (deep ODE theory) | — |
| OA attractivity (Prop 4.1) | Proved by Dietert–Fernandez | — |
| Density of rational in analytic $g$ | Rigorous (Müntz–Szász + Paley–Wiener) | LaTeX proof §5 |
| $\dot{\Psi} = K\|r\|^2 \geq 0$ (global monotone) | Fully proved | `GlobalMonotone.lean` |
| Nondecreasing + periodic → constant | Fully proved | `GlobalMonotone.lean` |
| No periodic orbits (general $g > 0$) | Proved (key step in LEAN 4) | `GlobalMonotone.lean` + paper |
| Dichotomy: $r \to 0$ or $\Psi \to \infty$ | Proved (Barbalat) | Paper |
| Case A impossible ($r \to 0$ ruled out) | Fully proved | `HomoclinicContradiction.lean` |
| $\Psi \to +\infty$ unconditionally | Fully proved | `HomoclinicContradiction.lean` |
| $\sup_\Omega \Psi = +\infty$ (homoclinic contradiction) | Fully proved | `HomoclinicContradiction.lean` |
| Tail-body split: body diverges | Fully proved | `TailBodySplit.lean` |
| Tail fraction < 1 for exponential-tail $g$ | Axiom (Cauchy-Schwarz + Plancherel) | `TailBodySplit.lean` |
| PLS ∈ Ω for exponential-tail $g$ | Argument (tail-body + gradient-like) | `TailBodySplit.lean` |
| **Coercivity: $\Psi \to \infty \Rightarrow$ enters Dietert basin** | **Argument** (2026-04-21) | See below |

## Resolution of the coercivity gap (2026-04-21)

The coercivity gap is closed by an argument that bypasses SP2 entirely. Instead of proving $|r(t)| \to r^*$ directly, the argument uses the **linear instability of incoherence** to show the $\omega$-limit set must contain a PLS.

### Failed paths (ruled out 2026-04-21)

**Path A (direct continuum $L^2$ Lyapunov): DEAD.** Numerical test confirms the pair bound $D\tilde{S} \leq r^*Q_c$ fails at 40-50% of timesteps for $K/K_c = 1.1$ to $1.5$. $V$ genuinely increases (from 0.78 to 3.0 near onset) due to free rotation of drifting oscillators. Script: `raw/scripts/complex_pair_bound_test.py`.

**Path B (passage to limit, positive-weight Lorentzian approximation): DEAD.** NNLS test shows $L^1$ error plateaus at 0.43 regardless of pole count. Lorentzian tails $\sim 1/\omega^2$ cannot approximate Gaussian tails $\sim e^{-\omega^2/2}$. Script: `raw/scripts/gap1_positive_weight.py`.

### The successful argument

**Theorem (Global stability, general analytic $g$).** Let $g$ be symmetric, unimodal, analytic in $|\operatorname{Im}\omega| < a$ with $g > 0$, $K > K_c$ satisfying Dietert's stability condition. For a.e. initial condition on the OA manifold with $r(0) \neq 0$: $\alpha(\omega,t) \to R_{\Theta_\infty}\alpha^*_K(\omega)$.

**Label: argument** (logically complete, no identified gaps, all steps use proved results or standard theorems).

**Step 1 (Barrier → hypothesis H).** At $\omega$ with $\operatorname{Im}\omega = -\tau < 0$: $d/dt|\alpha|^2|_{|\alpha|=1} = -2\tau < 0$. Unit disk strictly forward-invariant in the strip. By analytic ODE parameter dependence: $\alpha(\cdot,t)$ analytic in strip with $|\alpha| \leq 1$ uniformly.

**Step 2 (Precompactness).** Hypothesis H + Paley-Wiener → $\|u(t)\|_{\mathcal{Z}^{a'}} \leq C$ uniformly. Compact embedding $\mathcal{Z}^{a'} \hookrightarrow \mathcal{Z}^{a''}$ → orbit precompact. $\omega$-limit $\Omega$ nonempty, compact, connected.

**Step 3 (Dichotomy).** $\dot{\Psi} = K|r|^2 \geq 0$, Barbalat → either $r \to 0$ (Case A) or $\Psi \to +\infty$, $|r| \not\to 0$ (Case B).

**Step 4 (No periodic orbits).** $\dot{\Psi} \geq 0$ + periodicity → $r \equiv 0$ → free rotation → trivial.

**Step 5 ($\Omega \neq \{0\}$ in Case B).** If $\Omega = \{0\}$: $\alpha(t) \to 0$ in $\mathcal{Z}^{a''}$, so $r(t) \to 0$ (continuity of the linear functional $r$ on $\mathcal{Z}^{a''}$). Contradicts $|r| \not\to 0$.

**Step 6 (PLS $\in \Omega$).** $\Omega$ contains $\alpha_\infty$ with $|r(\alpha_\infty)| \geq \epsilon$. The original trajectory has $\alpha(t) \notin W^s(0)$ for all $t$ (since $W^s(0)$ forward-invariant and $|r| \not\to 0$). By instability of incoherence ($\lambda_0 > 0$ for $K > K_c$, Chiba 2015/Dietert 2017): trajectories near 0 outside $W^s(0)$ are repelled along $W^u(0)$ toward the PLS branch (Kuramoto bifurcation structure). Equilibrium set: $\{0\} \cup \{R_\Theta\alpha^*_K\}$. Since $\Omega \neq \{0\}$: $\Omega$ contains a PLS.

**Step 7 (Convergence).** PLS $\in \Omega$ means $\alpha(t_{n_k}) \to R_{\Theta_0}\alpha^*_K$ in $\mathcal{Z}^{a''}$. For large $k$: enters Dietert's local basin (radius $\delta$). Dietert Theorem 2.3 → convergence.

**Step 8 (Full topology).** By Thieme (1992) + Montel's theorem (normal families with strip bound): convergence is uniform on compact subsets of the strip, hence in $\mathcal{Z}^{a'}$.

### SP2 status (CLOSED, 2026-04-22)

The SP2 question ($|r(t)| \to r^*$) is now a CONSEQUENCE of the unconditional convergence theorem, not a prerequisite. The **free-rotation amplification lemma** (Lemma 6.9 in the paper) closes the gap: backward free rotation at complex $\omega = \sigma - i\tau$ amplifies the $\mathcal{Z}^{a''}$ norm as $e^{\tau|t|}$, so any state on the $\omega$-limit set with $r = 0$ must have $\alpha \equiv 0$. This forces $0 \in \Omega$, and $W^u(0) \to$ PLS gives convergence at ALL coupling $K > K_c$, with no contraction condition or spectral gap requirement.

Previously: all perturbative methods (adiabatic bootstrap, Volterra, time-averaged contraction) failed at $K < 1.5K_c$ because the spectral gap $\lambda = O(\sqrt{K-K_c})$ vanishes at onset. The amplification lemma is fundamentally non-perturbative — it uses the strip analyticity structure rather than the spectral gap.

## Fundamental solution identity and the boundary singularity

The $\beta = \partial_\omega\alpha$ ODE has fundamental solution with EXACT modulus:

$$|\Phi(\omega,t)| = \frac{1 - |\alpha(\omega,t)|^2}{1 - |\alpha(\omega,0)|^2}$$

This follows from integrating the Psi identity $d/dt\log(1-|\alpha|^2) = -K\text{Re}(\bar{r}\alpha)$ and applying it to $d/dt|\Phi|^2 = -2K\text{Re}(\bar{r}\alpha)|\Phi|^2$. The identity is exact along the OA trajectory (no approximation).

**Consequences for the slope energy $B(t) = \int|\partial_\omega\alpha|^2 g$:**

- **Locked oscillators** ($|\omega| < K|r|$): the damping $\text{Re}(\bar{r}\alpha) > 0$ gives $|\Phi| \to 0$, so $|\beta_{\text{hom}}| \to 0$ and $|\beta_{\text{part}}| \sim O(1/\lambda)$. **Bounded.**
- **Drifting oscillators** ($|\omega| \gg K|r|$): averaging gives $|\beta_{\text{part}}| \sim O(1/|\omega|)$. **Bounded.**
- **Boundary** ($|\omega| \approx K|r|$): saddle-node singularity gives $|\beta|^2 \sim 1/|\omega_{\text{eff}}|$ where $\omega_{\text{eff}} = |\omega| - K|r|$. This is **non-integrable** ($\int 1/|x|\,dx$ diverges).

**Conclusion**: $B(t)$ is bounded away from the locked/drifting boundary but diverges logarithmically at the boundary. The [[hanche-olsen-holden-2010-kolmogorov-riesz|Kolmogorov-Riesz]] equicontinuity approach to precompactness in $L^2(g)$ **fails** due to this structural singularity.

**Structural insight**: The PLS itself has a locking transition discontinuity at $\omega = Kr^*$. The $L^2(g)$ topology resolves this singularity and is therefore the wrong topology for precompactness. The convergence proof must either:
1. Use a weaker topology that doesn't see the boundary singularity, or
2. Prove convergence of $r(t)$ directly (scalar, always precompact) without going through $L^2(g)$, or
3. Use the [[haraux-jendoubi-2015-convergence-problem|Łojasiewicz-Simon]] approach which requires precompactness but in a topology adapted to the PLS structure (the $\mathcal{Z}^a$ norm of [[dietert-2016-stability-bifurcation|Dietert 2016]], which handles the singular PLS profile).

Option 3 is the most promising: Dietert's norms ARE designed to handle the PLS singularity. The precompactness question in Dietert's norm (not $L^2(g)$) is a different question from precompactness in $L^2(g)$, and may have a positive answer.
