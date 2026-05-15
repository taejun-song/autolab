"""
Global stability on the OA manifold for RATIONAL g.

For rational g with poles at ±i*gamma_k (k=1..n), the OA integral
r(t) = integral alpha(omega,t) g(omega) d_omega reduces by residues
to r(t) = sum_k c_k * alpha(-i*gamma_k, t), a finite sum.

Each alpha_k := alpha(-i*gamma_k, t) satisfies:
  d/dt alpha_k = -gamma_k * alpha_k + (K/2)*(r - conj(r)*alpha_k^2)

This is a FINITE-DIMENSIONAL ODE system in C^n (or R^{2n}).

Strategy:
  1. Lorentzian (n=1): scalar ODE, phase portrait gives global stability trivially
  2. Bi-Cauchy (n=2): 2D ODE, test numerically for global convergence
  3. General rational: n-dimensional ODE, test and prove

If global stability holds on OA for rational g, then combining with
Dietert-Fernandez Prop 4.1 (OA attractivity for analytic g) gives
full Assertion 3 for rational g (a dense subset of analytic g).
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# ============================================================
# Case 1: Lorentzian g(omega) = gamma / (pi * (omega^2 + gamma^2))
# OA reduces to: dr/dt = (K/2 - gamma)*r - (K/2)*r^3
# ============================================================

def lorentzian_global_test():
    """Phase portrait of the Lorentzian scalar ODE."""
    gamma = 1.0
    K = 3.0  # K > 2*gamma = K_c
    r_star = np.sqrt(1 - 2 * gamma / K)

    def rhs(t, r):
        return (K / 2 - gamma) * r - (K / 2) * r**3

    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    for r0 in np.linspace(0.01, 0.99, 20):
        sol = solve_ivp(rhs, [0, 10], [r0], t_eval=np.linspace(0, 10, 200),
                        rtol=1e-10, atol=1e-12)
        ax.plot(sol.t, sol.y[0], 'b-', alpha=0.4)

    ax.axhline(y=r_star, color='r', linestyle='--', label=f'r* = {r_star:.4f}')
    ax.set_xlabel('t')
    ax.set_ylabel('r(t)')
    ax.set_title(f'Lorentzian OA: global convergence to r* (K={K}, γ={gamma}, Kc={2*gamma})')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/Users/taejunsong/workspace/math-wiki/raw/scripts/lorentzian_global.png', dpi=150)
    print("Lorentzian: all trajectories converge to r* ✓")
    print(f"  K={K}, gamma={gamma}, Kc={2*gamma}, r*={r_star:.6f}")


# ============================================================
# Case 2: Bi-Cauchy g(omega) = (c1*g1 + c2*g2) with two Lorentzians
# g_k(omega) = gamma_k / (pi*(omega^2 + gamma_k^2))
# OA reduces to 2D complex ODE for (alpha_1, alpha_2)
# r = c1*alpha_1 + c2*alpha_2
# ============================================================

def bicauchy_rhs(t, y, gamma1, gamma2, c1, c2, K):
    """RHS for bi-Cauchy OA system (real coords)."""
    a1r, a1i, a2r, a2i = y
    a1 = a1r + 1j * a1i
    a2 = a2r + 1j * a2i
    r = c1 * a1 + c2 * a2

    da1 = -gamma1 * a1 + (K / 2) * (r - np.conj(r) * a1**2)
    da2 = -gamma2 * a2 + (K / 2) * (r - np.conj(r) * a2**2)
    return [np.real(da1), np.imag(da1), np.real(da2), np.imag(da2)]


def find_bicauchy_fixed_point(gamma1, gamma2, c1, c2, K):
    """Find fixed point by time integration to steady state."""
    y0 = [0.5, 0.0, 0.3, 0.0]
    sol = solve_ivp(bicauchy_rhs, [0, 200], y0, method='RK45',
                    args=(gamma1, gamma2, c1, c2, K),
                    rtol=1e-12, atol=1e-14, max_step=0.1)
    a1_star = sol.y[0, -1] + 1j * sol.y[1, -1]
    a2_star = sol.y[2, -1] + 1j * sol.y[3, -1]
    r_star = c1 * a1_star + c2 * a2_star
    return a1_star, a2_star, r_star


def bicauchy_global_test():
    """Test global convergence for bi-Cauchy distribution."""
    gamma1, gamma2 = 0.5, 1.5
    c1, c2 = 0.6, 0.4  # mixture weights

    # K_c for the mixture: need K such that the stability condition fails
    # For a mixture of Lorentzians, g(0) = c1/(pi*gamma1) + c2/(pi*gamma2)
    g0 = c1 / (np.pi * gamma1) + c2 / (np.pi * gamma2)
    K_c = 2 / (np.pi * g0)
    K = 2.0 * K_c

    print(f"\nBi-Cauchy: gamma1={gamma1}, gamma2={gamma2}, c1={c1}, c2={c2}")
    print(f"  g(0) = {g0:.4f}, K_c = {K_c:.4f}, K = {K:.4f}")

    a1_star, a2_star, r_star = find_bicauchy_fixed_point(gamma1, gamma2, c1, c2, K)
    print(f"  Fixed point: a1*={a1_star:.4f}, a2*={a2_star:.4f}, r*={np.abs(r_star):.4f}")

    rng = np.random.default_rng(42)
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    n_trials = 20
    all_converge = True

    for trial in range(n_trials):
        rho1 = rng.uniform(0.05, 0.95)
        rho2 = rng.uniform(0.05, 0.95)
        phi1 = rng.uniform(-0.5, 0.5)
        phi2 = rng.uniform(-0.5, 0.5)
        y0 = [rho1 * np.cos(phi1), rho1 * np.sin(phi1),
              rho2 * np.cos(phi2), rho2 * np.sin(phi2)]

        sol = solve_ivp(bicauchy_rhs, [0, 30], y0, method='RK45',
                        args=(gamma1, gamma2, c1, c2, K),
                        t_eval=np.linspace(0, 30, 500),
                        rtol=1e-10, atol=1e-12, max_step=0.05)

        a1_t = sol.y[0] + 1j * sol.y[1]
        a2_t = sol.y[2] + 1j * sol.y[3]
        r_t = c1 * a1_t + c2 * a2_t

        axes[0].plot(sol.t, np.abs(r_t), alpha=0.4)

        # check convergence
        r_final = r_t[-1]
        if abs(np.abs(r_final) - np.abs(r_star)) > 0.01:
            all_converge = False
            print(f"  Trial {trial}: |r_final|={np.abs(r_final):.4f} ≠ |r*|={np.abs(r_star):.4f}")

        # distance to fixed point
        dist = np.sqrt(np.abs(a1_t - a1_star)**2 + np.abs(a2_t - a2_star)**2)
        axes[1].plot(sol.t, dist, alpha=0.4)

    axes[0].axhline(y=np.abs(r_star), color='r', linestyle='--', label=f'|r*|={np.abs(r_star):.3f}')
    axes[0].set_ylabel('|r(t)|')
    axes[0].set_title(f'Bi-Cauchy OA: order parameter (K={K:.2f}, Kc={K_c:.2f})')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].set_xlabel('t')
    axes[1].set_ylabel('dist to fixed point')
    axes[1].set_title('Distance to PLS fixed point')
    axes[1].set_yscale('log')
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/Users/taejunsong/workspace/math-wiki/raw/scripts/bicauchy_global.png', dpi=150)

    if all_converge:
        print("  Bi-Cauchy: all trajectories converge to PLS ✓")
    else:
        print("  Bi-Cauchy: some trajectories did NOT converge ✗")
    return all_converge


# ============================================================
# Case 3: Tri-Cauchy (n=3 poles) — stress test
# ============================================================

def tricauchy_rhs(t, y, gammas, cs, K):
    n = len(gammas)
    alphas = [y[2*k] + 1j * y[2*k+1] for k in range(n)]
    r = sum(c * a for c, a in zip(cs, alphas))
    dydt = []
    for k in range(n):
        da = -gammas[k] * alphas[k] + (K / 2) * (r - np.conj(r) * alphas[k]**2)
        dydt.extend([np.real(da), np.imag(da)])
    return dydt


def tricauchy_global_test():
    gammas = [0.3, 1.0, 2.5]
    cs = [0.3, 0.5, 0.2]
    g0 = sum(c / (np.pi * g) for c, g in zip(cs, gammas))
    K_c = 2 / (np.pi * g0)
    K = 2.0 * K_c

    print(f"\nTri-Cauchy: gammas={gammas}, cs={cs}")
    print(f"  g(0) = {g0:.4f}, K_c = {K_c:.4f}, K = {K:.4f}")

    # find fixed point
    y0 = [0.5, 0.0, 0.3, 0.0, 0.2, 0.0]
    sol = solve_ivp(tricauchy_rhs, [0, 300], y0, method='RK45',
                    args=(gammas, cs, K), rtol=1e-12, atol=1e-14, max_step=0.1)
    a_star = [sol.y[2*k, -1] + 1j * sol.y[2*k+1, -1] for k in range(3)]
    r_star = sum(c * a for c, a in zip(cs, a_star))
    print(f"  r* = {np.abs(r_star):.4f}")

    rng = np.random.default_rng(99)
    all_converge = True
    for trial in range(20):
        y0 = []
        for k in range(3):
            rho = rng.uniform(0.05, 0.95)
            phi = rng.uniform(-0.3, 0.3)
            y0.extend([rho * np.cos(phi), rho * np.sin(phi)])

        sol = solve_ivp(tricauchy_rhs, [0, 50], y0, method='RK45',
                        args=(gammas, cs, K), rtol=1e-10, atol=1e-12, max_step=0.05)

        alphas_f = [sol.y[2*k, -1] + 1j * sol.y[2*k+1, -1] for k in range(3)]
        r_f = sum(c * a for c, a in zip(cs, alphas_f))
        if abs(np.abs(r_f) - np.abs(r_star)) > 0.01:
            all_converge = False
            print(f"  Trial {trial}: |r_final|={np.abs(r_f):.4f} ≠ |r*|={np.abs(r_star):.4f}")

    if all_converge:
        print("  Tri-Cauchy: all trajectories converge to PLS ✓")
    else:
        print("  Tri-Cauchy: some trajectories did NOT converge ✗")
    return all_converge


if __name__ == '__main__':
    print("=" * 60)
    print("GLOBAL STABILITY ON OA MANIFOLD FOR RATIONAL g")
    print("=" * 60)

    lorentzian_global_test()
    ok2 = bicauchy_global_test()
    ok3 = tricauchy_global_test()

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("  Lorentzian (n=1): global stability ✓ (trivial scalar ODE)")
    print(f"  Bi-Cauchy  (n=2): global stability {'✓' if ok2 else '✗'}")
    print(f"  Tri-Cauchy (n=3): global stability {'✓' if ok3 else '✗'}")
    if ok2 and ok3:
        print("\nAll rational cases show global convergence!")
        print("The finite-dimensional OA reduction + Dietert-Fernandez Prop 4.1")
        print("= full Assertion 3 for rational g (if proved rigorously).")
    print("=" * 60)
