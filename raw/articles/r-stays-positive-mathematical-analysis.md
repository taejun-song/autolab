# r-stays-positive: Mathematical Analysis of Strategies

## The Problem Statement

For the Ott-Antonsen reduced Kuramoto model:
  alpha'(w,t) = -gamma(w)*alpha(w,t) + (K/2)*r(t)*(1 - alpha(w,t)^2)
  r(t) = int alpha(w,t) * g(w) dw

Given: K > K_c, gamma(w) > 0 for all w, int (1/gamma) g dw < infty (finite first moment of 1/gamma), r(0) > 0.
Prove: exists r_min > 0 such that for all t >= 0, r(t) >= r_min.

## Strategy 1: Chetaev Instability of Incoherence

The incoherent state alpha = 0 is an UNSTABLE equilibrium when K > K_c.

Linearization about alpha = 0: alpha'(w,t) ~ -gamma(w)*alpha + (K/2)*r*(1-0) = -gamma*alpha + (K/2)*r
So r'(t) = int alpha'*g dw ~ -int gamma*alpha*g dw + (K/2)*r*int g dw
For Lorentzian: r' = (K/2 - gamma_0)*r - (K/2)*r^3 (Bernoulli ODE)
Near r=0: r' ~ (K/2 - gamma_0)*r with K/2 - gamma_0 > 0 when K > K_c = 2*gamma_0

Chetaev's theorem: If there exists a function W(x) such that:
1. W(0) = 0
2. W(x_0) > 0 for some x_0 arbitrarily close to 0
3. dW/dt > 0 on {W > 0} near 0
Then x = 0 is unstable.

For Kuramoto: W = r works. dW/dt ~ (K/2 - gamma_0)*r > 0 near r = 0.
This gives instability but NOT persistence (trajectory could revisit near 0).

Need: W = Psi (Dietert's energy) as a Chetaev function.
Psi = -int g*log(1-alpha^2) dw, dPsi/dt = K*r^2 >= 0.
Psi is bounded above. So int_0^infty r^2 dt < infty.
This means r cannot stay positive forever at any fixed level... wait, it means r^2 is integrable, so r(t) -> 0 in time-average sense.

CONTRADICTION? No. int r^2 < infty means r(t_n) -> 0 for SOME subsequence t_n.
But r Lipschitz + int r^2 < infty does NOT imply r -> 0 (Barbalat's lemma needs uniform continuity of r^2, which follows from r Lipschitz).

Actually: r is Lipschitz (from ODE with bounded RHS when alpha in [0,1]).
|r'(t)| <= int |alpha'| g dw <= int (gamma + K/2 + K/2*alpha^2) g dw <= int (gamma + K) g dw.
If int gamma*g < infty (first moment), then r is Lipschitz.
r Lipschitz + int_0^infty r^2 dt < infty => r(t) -> 0 (Barbalat).

WAIT: This would mean r -> 0, which contradicts stability of PLS for K > K_c!

RESOLUTION: Psi' = K*r^2 is valid for the FULL K-S equation but the OA manifold has alpha in [0,1], so Psi' = K*r^2 only if r is the order parameter of the K-S equation, not the OA reduced system.

Actually on the OA manifold:
d/dt [-int g log(1-alpha^2) dw] = int g * 2*alpha*alpha' / (1-alpha^2) dw
= int g * 2*alpha*[-gamma*alpha + (K/2)*r*(1-alpha^2)] / (1-alpha^2) dw
= int g * [-2*gamma*alpha^2/(1-alpha^2) + K*r*alpha] dw
= -2*int g*gamma*alpha^2/(1-alpha^2) dw + K*r*int g*alpha dw
= -2*int g*gamma*alpha^2/(1-alpha^2) dw + K*r^2

So Psi' = K*r^2 - 2*int g*gamma*alpha^2/(1-alpha^2) dw.
The second term is NEGATIVE (dissipation from damping).

So Psi' <= K*r^2, but Psi' = K*r^2 - (dissipation).
Psi is NOT monotone! The Dietert energy identity Psi' = K*r^2 is for the FULL PDE, not OA.

On OA: Psi' = K*r^2 - 2*int g*gamma*alpha^2/(1-alpha^2) dw.
For equilibrium: alpha = alpha*(w), the per-omega balance gives alpha'=0, so -gamma*alpha* + (K/2)*r**(1-alpha*^2) = 0, so gamma*alpha*/(1-alpha*^2) = Kr*/(2*(1+alpha*)).
The dissipation at equilibrium = 2*int g * gamma*alpha*^2/(1-alpha*^2) dw = K*r* * int g*alpha*/(1+alpha*) dw.
At self-consistency: r* = int g*alpha* dw.
So Psi'(equil) = K*r*^2 - K*r* * int g*alpha*/(1+alpha*) dw.
Since alpha*/(1+alpha*) < alpha*, we have int g*alpha*/(1+alpha*) < r*, so Psi'(equil) > 0.
But equilibrium means alpha' = 0, so Psi' should be 0 there. CONTRADICTION.

CORRECTION: At equilibrium, r = r* (constant), and Psi' involves time derivatives of alpha which are 0. So the calculation gives Psi'(equil) = K*r*^2 - 2*int g*gamma*alpha*^2/(1-alpha*^2) dw.
Using the equilibrium equation: gamma*alpha* = (K/2)*r**(1-alpha*^2), so gamma*alpha*^2/(1-alpha*^2) = (K/2)*r**alpha*.
So dissipation = 2*(K/2)*r* * int g*alpha* dw = K*r*^2.
Therefore Psi'(equil) = K*r*^2 - K*r*^2 = 0. Correct!

This means Psi is NOT a Lyapunov function for OA (unlike the full PDE). It's a balance between coupling gain and damping dissipation.

## Strategy 2: Direct ODE Comparison for r(t)

For general g, the ODE for r is:
r'(t) = int alpha'(w,t) * g(w) dw
= int [-gamma*alpha + (K/2)*r*(1-alpha^2)] * g dw
= -(int gamma*alpha*g dw) + (K/2)*r*(1 - int alpha^2*g dw)
= -(int gamma*alpha*g dw) + (K/2)*r - (K/2)*r*(int alpha^2*g dw)

For Lorentzian g(w) = (gamma_0/pi)/(w^2 + gamma_0^2):
The OA gives exactly r' = (K/2 - gamma_0)*r - (K/2)*r^3 (Bernoulli).
Solution: r(t) = r_0 * [(K/2-gamma_0) / ((K/2-gamma_0-K*r_0^2/2)*exp(-2(K/2-gamma_0)*t) + K*r_0^2/2)]^{1/2}
This shows r(t) -> r* = sqrt(1 - 2*gamma_0/K) > 0 for K > 2*gamma_0.
Moreover r(t) > 0 for all t >= 0 if r(0) > 0.

For general g: no closed form. But can we get a comparison?
If alpha(w,t) >= 0 and alpha(w,t) <= 1:
r' >= -(int gamma*g dw)*1 + (K/2)*r*(1-1) = -int gamma*g dw
This gives r(t) >= r(0) - (int gamma*g dw)*t, which goes negative. Useless.

Better: use the V = int (alpha-alpha*)^2 g dw Lyapunov function.
V antitone => r(t) close to r* in L^2 sense.
(r(t) - r*)^2 = (int (alpha-alpha*)*g dw)^2 <= int (alpha-alpha*)^2*g dw * int g dw = V(t)*1
So |r(t) - r*| <= sqrt(V(t)).
If V(t) <= V(0), then |r(t) - r*| <= sqrt(V(0)).
So r(t) >= r* - sqrt(V(0)).

KEY INSIGHT: If r* > sqrt(V(0)), then r(t) > 0 for all t >= 0!

This gives: r_min = r* - sqrt(V(0)) > 0 whenever V(0) < r*^2.

For the GENERAL case (V(0) might be large):
Need V(t) to decrease fast enough before r hits 0.
Since V is antitone: V(t) <= V(0) * exp(-c*t) for some rate c (if body coercivity).
So r(t) >= r* - sqrt(V(0))*exp(-c*t/2).
This is positive for all t if the minimum of r* - sqrt(V(0))*exp(-c*t/2) is positive.
Minimum at t=0: r* - sqrt(V(0)).
If V(0) >= r*^2: the bound is negative at t=0. Need finer analysis.

## Strategy 3: Self-Consistency Gap Exclusion (current Lean approach)

This is what's actually in the MainTheorem.lean chain:
1. Phi(r) = int explicitEquil(gamma(w), K, r) * g(w) dw is the self-consistency map
2. For K > K_c: Phi has unique fixed point r* in (0,1)
3. Gap exclusion: |r(t) - Phi(r(t))| -> 0 (self-consistency decay)
4. gap_min = min_{r not near 0 or r*} |r - Phi(r)| > 0
5. Therefore r(t) must be near 0 or r* eventually
6. Persistence (hpersist): lim inf r > 0 rules out r near 0
7. Therefore r -> r*

The persistence hypothesis hpersist is ASSUMED. It's exactly the r-stays-positive gap.

## Strategy 4: Psi + Instability Escape (most promising for formalization)

Key idea: combine Psi monotonicity with instability of r=0.

On OA: Psi' = K*r^2 - 2*int g*gamma*alpha^2/(1-alpha^2) dw
Near alpha = 0: alpha^2/(1-alpha^2) ~ alpha^2, so dissipation ~ 2*int g*gamma*alpha^2 dw.
Coupling gain = K*r^2 = K*(int g*alpha dw)^2.
By Cauchy-Schwarz: (int g*alpha)^2 <= (int g)(int g*alpha^2) = int g*alpha^2.
So coupling gain K*r^2 <= K*int g*alpha^2 dw.
Dissipation = 2*int g*gamma*alpha^2 dw.

Near incoherence (alpha small): Psi' ~ K*r^2 - 2*int g*gamma*alpha^2 dw.
If gamma < K/2 for some oscillators: those oscillators have POSITIVE contribution to the balance, driving growth.
Self-consistency: r = int alpha*g. For K > K_c: the low-gamma oscillators amplify r.

Formalization path:
1. Define Psi on OA manifold
2. Compute Psi' (verified calculation)  
3. Show Psi' > 0 in a neighborhood of alpha=0 (for K > K_c)
4. Show Psi bounded above => trajectory leaves neighborhood of alpha=0
5. Once r(t) >= delta > 0, self-consistency gap exclusion keeps r bounded below

Step 4 uses: Psi increasing while alpha near 0, Psi bounded above, so trajectory cannot stay near alpha=0.

## Strategy 5: V_inf Lyapunov + Cauchy-Schwarz (simplest, already partly formalized)

The L^2 Lyapunov V = int (alpha-alpha*)^2 g dw is antitone (proved, 0 sorry).
V bounded => |r - r*| <= sqrt(V) (Cauchy-Schwarz, proved).

If V(0) < r*^2: r(t) >= r* - sqrt(V(0)) > 0. Done.

If V(0) >= r*^2: need to show V decreases below r*^2 in finite time.
Body coercivity: V'(t) <= -c * V_body(t) (for bounded gamma).
V_body >= V - tail_mass. For small t: tail_mass may dominate.
But V decreasing + tail_mass fixed => eventually V_body dominates.

Actually simpler: V antitone => V(t) <= V(0) for all t.
So the bound r(t) >= r* - sqrt(V(0)) is the best we can get from V alone.
If V(0) >= r*^2, this bound is useless.

Need: V decreases fast initially. The rate depends on body coercivity, which depends on persistence. CIRCULAR.

## Strategy 6: Direct comparison with Lorentzian

For any g, approximate by Lorentzian g_n -> g.
For Lorentzian: r_n(t) > 0 with explicit lower bound.
If convergence is uniform: r(t) >= lim r_n(t) > 0.

This is essentially the passage-to-limit strategy (Strategy E).
Gap: uniform-in-t convergence of n-pole to continuum.

## Summary: Most Promising for Lean

1. **V + Cauchy-Schwarz** (Strategy 5): Works when V(0) < r*^2. Already partly formalized.
2. **Psi + instability escape** (Strategy 4): Works in general but requires formalizing Psi derivative on OA.
3. **Passage to limit** (Strategy 6): Conceptually clean but technically hardest.
4. **Self-consistency gap** (Strategy 3): Already the Lean approach; just needs hpersist proved.
