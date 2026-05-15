"""
Numerical test: does Phi_OA decrease along the OA flow for Gaussian g?

We discretize the OA ODE on a grid of omega values, integrate forward
from random initial conditions with r(0) > 0, and evaluate Phi_OA(t).

The OA ODE:  d/dt alpha(omega) = -i*omega*alpha + (K/2)*(r - conj(r)*alpha^2)
Mean field:  r(t) = integral alpha(omega,t) * g(omega) d_omega
Target:      alpha_star(omega) = beta(omega/(K*r_star))
Kernel:      H(alpha; alpha_star) = log((1 - |alpha|^2) / |alpha - alpha_star|^2)
Functional:  Phi = integral g(omega) * H(alpha(omega); alpha_star(omega)) d_omega
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import erfc
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def gaussian_g(omega):
    return np.exp(-omega**2 / 2) / np.sqrt(2 * np.pi)


def find_r_star(K, g_func, omega_grid, d_omega):
    """Find r* by iterating the self-consistency equation."""
    r = 0.5
    for _ in range(200):
        u = omega_grid / (K * r + 1e-15)
        locked = np.abs(u) <= 1
        beta_vals = np.zeros_like(u, dtype=complex)
        beta_vals[locked] = -1j * u[locked] + np.sqrt(1 - u[locked]**2 + 0j)
        beta_vals[~locked] = -1j * u[~locked] + 1j * u[~locked] * np.sqrt(1 - u[~locked]**(-2) + 0j)
        r_new = np.real(np.sum(beta_vals * g_func(omega_grid) * d_omega))
        if abs(r_new - r) < 1e-12:
            break
        r = 0.5 * r + 0.5 * r_new
    return r


def alpha_star(omega, K, r_star):
    """Compute the PLS fixed point on the OA manifold."""
    u = omega / (K * r_star + 1e-15)
    result = np.zeros_like(omega, dtype=complex)
    locked = np.abs(u) <= 1
    result[locked] = -1j * u[locked] + np.sqrt(1 - u[locked]**2 + 0j)
    result[~locked] = -1j * u[~locked] + 1j * u[~locked] * np.sqrt(1 - u[~locked]**(-2) + 0j)
    return result


def oa_rhs(t, alpha_flat, omega_grid, g_vals, d_omega, K):
    """RHS of the OA ODE system (real/imag interleaved)."""
    N = len(omega_grid)
    alpha = alpha_flat[:N] + 1j * alpha_flat[N:]
    r = np.sum(alpha * g_vals * d_omega)
    dadt = -1j * omega_grid * alpha + (K / 2) * (r - np.conj(r) * alpha**2)
    return np.concatenate([np.real(dadt), np.imag(dadt)])


def compute_phi(alpha, a_star, g_vals, d_omega):
    """Evaluate Phi_OA = integral g(omega) * log((1-|alpha|^2)/|alpha-a_star|^2) d_omega."""
    numer = 1 - np.abs(alpha)**2
    denom = np.abs(alpha - a_star)**2
    numer = np.maximum(numer, 1e-30)
    denom = np.maximum(denom, 1e-30)
    integrand = g_vals * np.log(numer / denom)
    return np.sum(integrand * d_omega)


def run_test(K, n_omega=200, omega_max=6.0, T=20.0, n_trials=8, seed=42):
    """Run the numerical test for a given K."""
    rng = np.random.default_rng(seed)
    omega_grid = np.linspace(-omega_max, omega_max, n_omega)
    d_omega = omega_grid[1] - omega_grid[0]
    g_vals = gaussian_g(omega_grid)

    K_c = 2 / (np.pi * gaussian_g(0))
    print(f"K_c = {K_c:.4f}, K = {K:.4f}, K/K_c = {K/K_c:.4f}")

    r_star = find_r_star(K, gaussian_g, omega_grid, d_omega)
    print(f"r* = {r_star:.6f}")
    a_star = alpha_star(omega_grid, K, r_star)

    fig, axes = plt.subplots(2, 1, figsize=(10, 8))

    all_monotone = True
    for trial in range(n_trials):
        rho0 = rng.uniform(0.1, 0.9, n_omega)
        phi0 = rng.uniform(-np.pi, np.pi, n_omega)
        alpha0 = rho0 * np.exp(1j * phi0)
        # ensure r(0) > 0 by biasing phases toward 0
        alpha0 = rho0 * np.exp(1j * phi0 * 0.3)
        y0 = np.concatenate([np.real(alpha0), np.imag(alpha0)])

        t_eval = np.linspace(0, T, 500)
        sol = solve_ivp(oa_rhs, [0, T], y0, t_eval=t_eval, method='RK45',
                        args=(omega_grid, g_vals, d_omega, K),
                        rtol=1e-8, atol=1e-10, max_step=0.05)

        phis = []
        rs = []
        for i in range(len(sol.t)):
            a = sol.y[:n_omega, i] + 1j * sol.y[n_omega:, i]
            # project back into disk if numerical drift
            mask = np.abs(a) >= 1
            if np.any(mask):
                a[mask] = a[mask] / (np.abs(a[mask]) + 1e-6) * 0.999
            phis.append(compute_phi(a, a_star, g_vals, d_omega))
            rs.append(np.abs(np.sum(a * g_vals * d_omega)))

        phis = np.array(phis)
        rs = np.array(rs)

        # check monotonicity
        diffs = np.diff(phis)
        n_increases = np.sum(diffs > 1e-8)
        if n_increases > 0:
            all_monotone = False
            print(f"  Trial {trial}: {n_increases} increases detected (max increase = {np.max(diffs):.2e})")
        else:
            print(f"  Trial {trial}: monotone decrease ✓ (Phi: {phis[0]:.4f} -> {phis[-1]:.4f})")

        axes[0].plot(sol.t, phis, label=f'trial {trial}')
        axes[1].plot(sol.t, rs, label=f'trial {trial}')

    axes[0].set_ylabel('Phi_OA(t)')
    axes[0].set_title(f'Lyapunov functional (K={K:.2f}, K/Kc={K/K_c:.2f}, Gaussian g)')
    axes[0].legend(fontsize=7)
    axes[0].grid(True, alpha=0.3)

    axes[1].set_xlabel('t')
    axes[1].set_ylabel('|r(t)|')
    axes[1].set_title('Order parameter')
    axes[1].axhline(y=r_star, color='k', linestyle='--', alpha=0.5, label=f'r*={r_star:.3f}')
    axes[1].legend(fontsize=7)
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/Users/taejunsong/workspace/math-wiki/raw/scripts/phi_oa_test.png', dpi=150)
    print(f"\nPlot saved. All trials monotone: {all_monotone}")
    return all_monotone


if __name__ == '__main__':
    # Test at K = 1.5 * K_c (well above threshold)
    K_c = 2 / (np.pi * gaussian_g(0))
    print("=" * 60)
    print("TEST 1: K = 1.5 * K_c")
    print("=" * 60)
    ok1 = run_test(K=1.5 * K_c)

    print("\n" + "=" * 60)
    print("TEST 2: K = 3.0 * K_c")
    print("=" * 60)
    ok2 = run_test(K=3.0 * K_c, seed=123)

    print("\n" + "=" * 60)
    print("TEST 3: K = 1.1 * K_c (near onset)")
    print("=" * 60)
    ok3 = run_test(K=1.1 * K_c, T=40.0, seed=456)

    print("\n" + "=" * 60)
    if ok1 and ok2 and ok3:
        print("ALL TESTS PASSED: Phi_OA decreases monotonically in all trials.")
        print("The log-ratio kernel appears to work for Gaussian g.")
    else:
        print("SOME TESTS FAILED: Phi_OA is NOT monotonically decreasing.")
        print("The log-ratio kernel may need modification (Path B).")
    print("=" * 60)
