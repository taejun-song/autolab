---
type: synthesis
title: "Strategies to Prove r(t) Stays Positive"
created: 2026-05-08
updated: 2026-05-08
sources:
  - "[[order-parameter-persistence]]"
  - "[[continuum-stability-debate]]"
  - "[[dietert-2016-stability-bifurcation]]"
  - "[[dietert-fernandez-2018-asymptotic-stability]]"
  - "[[body-lasalle-gap-analysis]]"
tags:
  - dynamical-systems
  - synchronization
  - open-problem
  - stability
aliases:
  - r-stays-positive-strategies
  - persistence-strategies
---

# Strategies to Prove r(t) Stays Positive

A synthesis of all known mathematical approaches to proving $\exists\, r_{\min} > 0,\, \forall t \geq 0,\, r(t) \geq r_{\min}$ for the OA Kuramoto model with $K > K_c$ and $r(0) > 0$.

## The mathematical setup

$$\dot{\alpha}(\omega,t) = -\gamma(\omega)\alpha + \frac{K}{2}r(t)(1 - \alpha^2), \quad r(t) = \int \alpha(\omega,t)\,g(\omega)\,d\omega$$

Hypotheses: $K > K_c := 2/\int(1/\gamma)g\,d\omega$, $\gamma > 0$ pointwise, $\alpha(\omega,0) \in (0,1)$ for a.e. $\omega$, $r(0) > 0$.

## Strategy 1: Cauchy-Schwarz from V-antitonicity (simplest, partial)

**Status: PROVES persistence for small initial perturbations**

The $L^2$ Lyapunov functional $V(t) = \int (\alpha - \alpha^*)^2 g\,d\omega$ is antitone (proved, 0 sorry). By Cauchy-Schwarz:

$$(r(t) - r^*)^2 = \left(\int (\alpha - \alpha^*) g\,d\omega\right)^2 \leq \int (\alpha-\alpha^*)^2 g\,d\omega = V(t) \leq V(0)$$

Therefore $r(t) \geq r^* - \sqrt{V(0)}$.

**Sufficient condition**: $V(0) < r^{*2}$ implies $r_{\min} = r^* - \sqrt{V(0)} > 0$.

**Lean formalizability**: Immediate. All ingredients proved. Could close the gap for initial data satisfying $V(0) < r^{*2}$.

**Limitation**: For $V(0) \geq r^{*2}$ (far from equilibrium), the bound is negative and useless.

### Extension: time-dependent bound

Since $V$ is antitone, $V(t) \leq V(0)$ for all $t$. If we can show $V(T) < r^{*2}$ for some $T < \infty$, then $r(t) > 0$ for $t \geq T$. Combined with continuity of $r$ on $[0,T]$ and $r(0) > 0$: $r_{\min} = \min(r^* - \sqrt{V(T)},\, \min_{t \in [0,T]} r(t))$.

Gap: showing $V(T) < r^{*2}$ requires a rate bound that doesn't use persistence.

## Strategy 2: Bootstrap from V-rate without persistence

**Status: sketch, most promising for general case**

Key insight: the V-rate bound from body coercivity does NOT need persistence for the initial phase.

**Step 1**: For $t \in [0, T_1]$ where $T_1$ is the first time $r(t)$ might hit some threshold $\epsilon$: use the per-$\omega$ ODE lower bound. Since $r(t) \geq \epsilon$ on $[0,T_1]$:
$$\alpha(\omega,t) \geq \min\left(\alpha(\omega,0),\, \frac{Kr\epsilon}{2\gamma + K\epsilon}\right) \quad \text{on } \{\gamma \leq M\}$$

This is `body_persistence_lower_bound` (proved, 0 sorry) applied with $r_{\min} = \epsilon$.

**Step 2**: Body coercivity with this $\epsilon$-dependent persistence:
$$V'(t) \leq -K \cdot \delta(\epsilon, M) \cdot V_{\text{body}}(M, t)$$

**Step 3**: $V_{\text{body}} \geq V - \mu(\text{tail}(M))$, so:
$$V'(t) \leq -c(\epsilon, M) \cdot V(t) + c(\epsilon, M) \cdot \mu(\text{tail})$$

**Step 4**: Gronwall gives $V(t) \leq V(0)e^{-c t} + \mu(\text{tail})/c$.

**Step 5**: Choose $M$ so $\mu(\text{tail}) < r^{*2}/2$, then choose $T$ so $V(0)e^{-cT} < r^{*2}/2$. Then $V(T) < r^{*2}$, giving $r(t) > 0$ for $t \geq T$.

**Step 6**: On $[0, T]$: $r$ is continuous, $r(0) > 0$. If $r$ never hits $\epsilon$ on $[0,T]$: done. If $r$ hits $\epsilon$: contradiction with step 5 (the V decay was derived assuming $r \geq \epsilon$, but if $r$ hits $\epsilon$ before $T$, the decay estimate breaks).

**Resolution**: Use a CONTINUATION argument. Define $T^* = \inf\{t : r(t) \leq \epsilon\}$. On $[0, T^*]$: the V estimate holds. If $T^* < T$: then at time $T^*$, $r(T^*) = \epsilon$ and $V(T^*) \leq V(0)e^{-cT^*} + \mu/c \leq V(0)$. But $r(T^*) = \epsilon$ and $|r(T^*) - r^*| \leq \sqrt{V(T^*)}$, so $\epsilon \geq r^* - \sqrt{V(0)}$. This is a constraint on $\epsilon$ (must be small enough).

**The correct bootstrap**: Choose $\epsilon = r^*/2$ (say). If $r(t)$ ever reaches $r^*/2$ from above, use the V-rate bound on $[0, T^*]$ to show $V(T^*) < \delta$ for some $\delta$ depending on $T^*$. Then $|r(T^*) - r^*| < \sqrt{\delta}$. If $\sqrt{\delta} < r^*/2$: contradiction with $r(T^*) = r^*/2$. This requires $V(0)e^{-cT^*} < r^{*2}/4$, i.e., $T^* > (1/c)\log(4V(0)/r^{*2})$. So if $r$ stays above $r^*/2$ long enough for V to decay, it can never reach $r^*/2$.

**Problem**: $c = c(\epsilon, M)$ depends on $\epsilon = r^*/2$, which is fixed. The rate $c$ involves:
- $\delta(\epsilon, M) = K\epsilon/(2M + K\epsilon) = Kr^*/(4M + Kr^*)$ (body persistence lower bound)
- Body measure $\mu(\{\gamma \leq M\})$
- Equilibrium lower bound on body

This is $c \sim K^2 r^{*2} / (16 M^2) \cdot \mu(\text{body})$ for large $M$. As $M$ grows: $c$ decreases but tail shrinks.

**Lean formalizability**: HIGH. All pieces exist:
- `body_persistence_lower_bound` (proved)
- `body_gronwall_from_persistence` (proved)
- Continuation/bootstrap argument (standard Lean tactic)
- V-Cauchy-Schwarz (proved)

The key lemma to prove: "if $r(t) \geq r^*/2$ on $[0, T^*]$ and $T^*$ is sufficiently large, then $V(T^*) < r^{*2}/4$, contradicting $r(T^*) = r^*/2$."

## Strategy 3: Instability escape via Psi functional

**Status: argument, needs correction**

On the OA manifold, the Dietert energy $\Psi = -\int g\log(1-\alpha^2)\,d\omega$ satisfies:
$$\Psi' = Kr^2 - 2\int g\gamma\frac{\alpha^2}{1-\alpha^2}\,d\omega$$

Near $\alpha \approx 0$: $\alpha^2/(1-\alpha^2) \approx \alpha^2$, so:
$$\Psi' \approx K\left(\int g\alpha\,d\omega\right)^2 - 2\int g\gamma\alpha^2\,d\omega$$

The quadratic form $Q[\alpha] = K(\int g\alpha)^2 - 2\int g\gamma\alpha^2$ has its maximum eigenvalue $> 0$ iff $K > K_c$ (this is the linear instability of incoherence). Specifically, the maximizer $\alpha_0(\omega) = c/\gamma(\omega)$ gives $Q[\alpha_0] = K(\int g/\gamma)^2 - 2\int g/\gamma = \int g/\gamma \cdot (K\int g/\gamma - 2) > 0$.

**Consequence**: In a cone around $\alpha_0$ near the origin, $\Psi' > 0$.

**Combined with $\Psi$ bounded above** ($\Psi \leq -\log(1-1) = +\infty$... wait, $\alpha < 1$ so $\Psi$ is finite but unbounded as $\alpha \to 1$):

Actually $\Psi$ IS bounded above for bounded $\alpha$: if $\alpha \leq 1-\epsilon$ then $\Psi \leq -\log(\epsilon) \cdot \int g = -\log(\epsilon)$. But $\alpha$ can approach 1 for small-$\gamma$ oscillators.

**Correction**: $\Psi$ may be UNBOUNDED on the OA manifold. For locked oscillators ($\gamma < Kr^*$), $\alpha^* = 1 - \gamma/(Kr^*) + O(\gamma^2/(Kr^*)^2)$ approaches 1, making $-\log(1-\alpha^{*2}) \to +\infty$. So $\Psi$ at equilibrium may be infinite for distributions with $g(0) > 0$.

**Revised argument**: $\Psi$ increasing near incoherence forces the orbit away from 0, but $\Psi \to +\infty$ at equilibrium is consistent (the orbit approaches a state where $\Psi$ is large). The issue is that $\Psi$ monotone + escape from 0 doesn't prevent return to 0 (since $\Psi$ is not bounded above).

**Lean formalizability**: MEDIUM. Requires formalizing the quadratic form $Q$ and its eigenvalue analysis.

## Strategy 4: Ψ-escape + V-trap (combined)

**Status: sketch, most elegant**

Combine Strategies 1 and 3:

**Phase 1** (escape): If $r(t)$ ever enters $B(0, \epsilon)$: the instability of incoherence (Strategy 3) forces $r$ to leave within time $T_{\text{esc}}(\epsilon)$.

**Phase 2** (trap): Once $r(t) \geq \epsilon$ for sufficiently long: V-antitonicity decreases $V$ until $V < r^{*2}$. After that, $r(t) \geq r^* - \sqrt{V(t)} > 0$ forever (Strategy 1 kicks in and persistence holds permanently).

**Key claim**: Phase 1 and Phase 2 cannot alternate infinitely. Each time Phase 2 runs, V decreases. Since V is antitone, V can only reach the threshold $r^{*2}$ once, after which persistence holds forever.

**Formal argument**:
1. V antitone: $V(t_2) \leq V(t_1)$ for $t_2 > t_1$.
2. During Phase 2 intervals $[s_k, e_k]$ (when $r \geq \epsilon$): $V$ decreases at rate $\geq c(\epsilon)$.
3. Total time in Phase 2: $\sum_k (e_k - s_k) \leq V(0)/c(\epsilon) < \infty$ (since V bounded and decreasing at positive rate during Phase 2).

Wait, this isn't quite right. V always decreases (antitone), not just during Phase 2.

**Simpler**: V(t) is antitone, hence V(t) -> L >= 0. If L < r*^2: then eventually V(t) < r*^2, giving r(t) > 0 permanently. If L >= r*^2: need to show this contradicts V-antitone + convergence properties.

In fact: V -> L means r -> r* (since |r-r*|^2 <= V and V antitone implies r confined). If V -> L > 0: then alpha does not converge to alpha* in L^2. But the LaSalle argument (ContinuumRigidity) says V' = 0 implies alpha = alpha*. V antitone + bounded below by L > 0 contradicts V' < 0 unless V' -> 0. V' -> 0 + rigidity -> alpha -> alpha* -> V -> 0. Contradiction with L > 0.

**So V -> 0** (proved abstractly, modulo body antitonicity). And V -> 0 implies r -> r*. And V(t) -> 0 means eventually V(t) < r*^2, giving persistence for large t. For finite time: r continuous + r(0) > 0 gives persistence on [0, T].

**CONCLUSION**: V -> 0 IMPLIES persistence. The two gaps (V -> 0 and r-stays-positive) are NOT independent. Proving V -> 0 automatically gives r-stays-positive. The converse is used in the current Lean proof (persistence -> V -> 0), but logically V -> 0 is stronger and implies persistence.

## Strategy 5: Direct r-ODE estimate without V

**Status: sketch**

Derive an ODE inequality for r(t) directly:
$$r'(t) = -\int \gamma\alpha\,g\,d\omega + \frac{K}{2}r(1 - \int \alpha^2 g\,d\omega)$$

Lower bound: using $\int \alpha^2 g \leq \int \alpha g = r$ (since $0 \leq \alpha \leq 1$):
$$r' \geq -\int \gamma\alpha\,g\,d\omega + \frac{K}{2}r(1-r)$$

Upper bound on damping: $\int \gamma\alpha\,g \leq \int \gamma g = \bar{\gamma}$ (first moment).
$$r' \geq -\bar{\gamma} + \frac{K}{2}r(1-r)$$

This is a scalar ODE for a LOWER BOUND $\underline{r}$:
$$\underline{r}' = -\bar{\gamma} + \frac{K}{2}\underline{r}(1-\underline{r})$$

Equilibria: $\bar{\gamma} = (K/2)\underline{r}(1-\underline{r})$, i.e., $\underline{r}^2 - \underline{r} + 2\bar{\gamma}/K = 0$.
Solution: $\underline{r} = (1 \pm \sqrt{1 - 8\bar{\gamma}/K})/2$.

For $K > 8\bar{\gamma}$: two positive equilibria exist, the lower one is unstable, the upper one is stable. The lower equilibrium is a lower bound for $r(t)$ if $r(0)$ is above it.

**Problem**: $K > 8\bar{\gamma}$ is MUCH stronger than $K > K_c = 2/\int(1/\gamma)g$. For Lorentzian: $\bar{\gamma} = \infty$, so this never applies.

**For bounded $\gamma$**: $\bar{\gamma} \leq \gamma_{\max}$, and $K > K_c \geq 2\gamma_{\max}$ (for bounded $\gamma$, $K_c = 2\gamma_{\max}$ when $g$ is peaked at 0). So $8\bar{\gamma}/K \leq 8\gamma_{\max}/K \leq 4$, which means the discriminant $1 - 8\bar{\gamma}/K$ may be negative.

**Lean formalizability**: LOW for general case (bound too weak). But for specific regimes (large K), straightforward.

## Strategy 6: Passage to limit from n-pole

**Status: argument level, 3 True placeholders**

1. Finite-N theorem: $r_N(t) \to r^*_N$ with persistence (proved, 0 sorry).
2. $N$-pole approximation: $r_N(t) \to r(t)$ as $N \to \infty$ uniformly on compacts.
3. Persistence transfers: $\inf_{t \geq 0} r_N(t) \geq \delta_N > 0$ with $\delta_N \to \delta > 0$.

Gap: Step 2 requires uniform-in-$t$ convergence. The `UniformRate` theorem gives $N$-independent exponential rates, suggesting this is achievable.

**Lean formalizability**: MEDIUM. PassageToLimit.lean has the framework; needs 3 continuous-dependence bounds filled.

## Recommendation for Lean formalization

**Priority 1**: Strategy 2 (bootstrap from V-rate). All building blocks exist in the Lean codebase:
- `body_persistence_lower_bound` gives per-$\omega$ lower bound from $r \geq r_{\min}$
- `body_gronwall_from_persistence` gives V-rate from persistence
- V-Cauchy-Schwarz gives $r \geq r^* - \sqrt{V}$
- Continuation argument is standard

The proof structure: assume for contradiction that $T^* = \inf\{t : r(t) = r^*/2\} < \infty$. On $[0, T^*]$: body persistence holds with $r_{\min} = r^*/2$. Gronwall gives $V(T^*) \leq V(0)e^{-cT^*} + C$. But also $|r(T^*) - r^*| = r^*/2 \leq \sqrt{V(T^*)}$, so $V(T^*) \geq r^{*2}/4$.

Need: $V(0)e^{-cT^*} + C < r^{*2}/4$ to get contradiction. This requires $C < r^{*2}/4$ (i.e., tail is small) and $T^*$ is large enough. If $T^*$ is small: $V(T^*) \approx V(0)$ and we need $V(0) \geq r^{*2}/4$... but this is just the given bound restated.

**The fundamental issue**: we don't control HOW FAST r drops. If r drops to $r^*/2$ very quickly (small $T^*$), V hasn't had time to decrease. The bootstrap only works if $r$ drops slowly enough relative to V's decay rate.

**Priority 2**: Prove persistence for $V(0) < r^{*2}$ (Strategy 1). This is IMMEDIATE from existing Lean code and closes the gap for initial data near equilibrium. Then use V-antitonicity to eventually reach this regime.

**Priority 3**: Combine with instability escape (Strategy 4) for the general case.

## Cross-links

- [[order-parameter-persistence]] — the concept page
- [[continuum-stability-debate]] — full proof status
- [[body-lasalle-gap-analysis]] — why body antitonicity needs persistence
- [[lean-proof-status]] — machine-checked status
- [[subproblem-decomposition]] — problem decomposition
