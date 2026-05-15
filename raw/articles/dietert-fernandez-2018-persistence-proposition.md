# Dietert & Fernandez (2018) — Persistence and Energy Identity Extracts

Source: "The mathematics of asymptotic stability in the Kuramoto model" (Proc. R. Soc. A 474(2220), 2018). arXiv:1801.01309.

## Proposition 4.3 — Persistence of Order Parameter (from Dietert-Fernandez 2018)

For the Ott-Antonsen flow with K > K_c and analytic g: if r(0) > 0, then lim inf_{t->infty} |r(t)| > 0.

Proof strategy: The universal energy identity (Dietert 2016) gives
  d/dt I_0 = K|r(t)|^2
where I_0 = int_R sum_{l>=1} (1/l)|f_hat(t,l,w)|^2 g^{-1}(w) dw.

On the OA manifold, I_0 = -int g log(1-|alpha|^2) dw =: Psi(t).

Key properties:
1. Psi is monotonically non-decreasing (dPsi/dt = K|r|^2 >= 0)
2. Psi is bounded above (alpha in (0,1) implies log(1-alpha^2) bounded)
3. Therefore Psi -> L (some finite limit)
4. If r(t) -> 0, then Psi would be eventually constant, but...

The persistence argument uses the instability of the incoherent state:
- alpha = 0 is an unstable equilibrium of the per-omega ODE when K > K_c
- The linearization about alpha = 0 has eigenvalue (K/2)r - gamma
- For oscillators with gamma < (K/2)r, this eigenvalue is positive
- By Chetaev-type instability, if r(t_n) -> 0 on a subsequence but alpha(w,t) not identically 0, then the instability forces r to grow again
- This contradicts r(t_n) -> 0 persistently

The quantitative version: lim inf |r(t)| >= delta > 0 where delta depends on K, K_c, and the initial data.

## The Universal Energy Identity (Dietert 2016, Section 2)

For the Kuramoto-Sakaguchi equation in Fourier variables:

d/dt int_R sum_{l=1}^{infty} (1/l) |f_hat(t,l,w)|^2 g^{-1}(w) dw = K|r(t)|^2

This is the "pair bound" in disguise. On the OA manifold where f_hat(t,l,w) = alpha(w,t)^l g(w):

LHS = d/dt int_R sum_{l>=1} (1/l) alpha^{2l} g(w) dw
     = d/dt int_R (-log(1 - alpha^2)) g(w) dw
     = d/dt Psi(t)

So Psi' = K*r^2 >= 0.

## Connection to r-stays-positive

The persistence result (Prop 4.3) is proved only LOCAL-in-neighborhood (for perturbations near the PLS). The GLOBAL version — r(0) > 0 implies inf_{t>=0} r(t) > 0 — requires ruling out that r can approach 0 from arbitrary initial data when K > K_c.

The key mathematical ingredients for a global proof:
1. Psi monotone + bounded => Psi converges
2. dPsi/dt = Kr^2 => int_0^infty r^2 dt < infty
3. r Lipschitz in t (from ODE regularity) + int r^2 < infty => ...but this does NOT give r -> 0
4. Need: instability of incoherence prevents r from dwelling near 0
5. Chetaev theorem: if alpha=0 is unstable and Psi is a Chetaev function (positive on unstable manifold, derivative positive), then trajectories escape any neighborhood of alpha=0

## Relevance to Lean formalization

The r-stays-positive result is ASSUMED in the current Lean formalization as a field of KuramotoData (hpersist). Proving it from the ODE would require:
1. Formalizing the instability of alpha=0 for K > K_c
2. Formalizing Psi as a Chetaev function
3. Connecting the escape from incoherence to a uniform lower bound on r(t)

This is a fundamentally different argument from the Lyapunov convergence (which shows r -> r*). It's about the REPULSIVE nature of the origin, not the ATTRACTIVE nature of r*.
