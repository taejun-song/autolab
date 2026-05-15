"""
Gap 1: Can we approximate analytic g by positive-weight Lorentzian mixtures?

For the passage-to-limit proof, we need:
  g_n(omega) = sum_k c_k * gamma_k / [pi * (omega^2 + gamma_k^2)]
with c_k > 0, sum c_k = 1, approximating g in the H^1_{e^{a*tau}} norm:
  ||g_n - g|| = integral_0^infty e^{a*tau} |hat_g_n(tau) - hat_g(tau)| (1+tau) d_tau

Approach: fix a grid of gamma_k values, use NNLS to find optimal positive weights.
Test with Gaussian g(omega) = exp(-omega^2/2) / sqrt(2*pi).
"""

import numpy as np
from scipy.optimize import nnls
from scipy.integrate import quad

def gaussian_g_hat(tau):
    """Fourier transform of standard Gaussian: hat_g(tau) = exp(-tau^2/2)."""
    return np.exp(-tau**2 / 2)

def lorentzian_hat(tau, gamma):
    """Fourier transform of Lorentzian L_gamma: exp(-gamma*|tau|)."""
    return np.exp(-gamma * np.abs(tau))

def build_nnls_system(gamma_grid, tau_grid, weights=None):
    """Build the NNLS system A*c ≈ b for approximating hat_g by sum c_k exp(-gamma_k*tau).

    The matrix A has entries A[i,k] = exp(-gamma_k * tau_i) * w_i
    The vector b has entries b[i] = hat_g(tau_i) * w_i
    where w_i are optional weights (e.g., e^{a*tau_i} for the H^1 norm).
    """
    n_tau = len(tau_grid)
    n_gamma = len(gamma_grid)
    A = np.zeros((n_tau, n_gamma))
    for k in range(n_gamma):
        A[:, k] = np.exp(-gamma_grid[k] * tau_grid)
    b = gaussian_g_hat(tau_grid)
    if weights is not None:
        A = A * weights[:, None]
        b = b * weights
    return A, b

def evaluate_approximation(c, gamma_grid, a=0.0):
    """Evaluate the H^1_{e^{a*tau}} error of the approximation."""
    def integrand(tau):
        approx = sum(c[k] * np.exp(-gamma_grid[k] * tau) for k in range(len(gamma_grid)))
        exact = np.exp(-tau**2 / 2)
        return np.exp(a * tau) * np.abs(approx - exact) * (1 + tau)
    error, _ = quad(integrand, 0, 30, limit=200)
    return error

def evaluate_l1_error(c, gamma_grid):
    """L^1(R) error of the density approximation."""
    def integrand(omega):
        approx = sum(c[k] * gamma_grid[k] / (np.pi * (omega**2 + gamma_grid[k]**2))
                      for k in range(len(gamma_grid)))
        exact = np.exp(-omega**2 / 2) / np.sqrt(2 * np.pi)
        return np.abs(approx - exact)
    error, _ = quad(integrand, 0, 20, limit=200)
    return 2 * error  # symmetry

def run_nnls_test(n_poles, gamma_strategy='geometric', a_weight=0.0):
    """Run NNLS with n poles and evaluate the result."""
    if gamma_strategy == 'geometric':
        gamma_grid = np.geomspace(0.1, 10.0, n_poles)
    elif gamma_strategy == 'linear':
        gamma_grid = np.linspace(0.1, 5.0, n_poles)
    elif gamma_strategy == 'dense_low':
        gamma_grid = np.concatenate([np.linspace(0.05, 1.0, n_poles // 2),
                                      np.geomspace(1.0, 10.0, n_poles - n_poles // 2)])

    tau_grid = np.linspace(0, 15, 500)
    if a_weight > 0:
        weights = np.exp(a_weight * tau_grid) * np.sqrt(1 + tau_grid)
    else:
        weights = np.ones_like(tau_grid)

    A, b = build_nnls_system(gamma_grid, tau_grid, weights)
    c, residual_norm = nnls(A, b)

    # normalize to sum = 1
    c_sum = np.sum(c)
    if c_sum > 0:
        c_normalized = c / c_sum
    else:
        c_normalized = c

    n_active = np.sum(c_normalized > 1e-10)
    l1_err = evaluate_l1_error(c_normalized, gamma_grid)

    # evaluate hat_g approximation quality at key points
    tau_test = np.array([0.0, 0.5, 1.0, 2.0, 3.0, 5.0])
    approx_vals = np.array([sum(c_normalized[k] * np.exp(-gamma_grid[k] * t)
                                for k in range(n_poles)) for t in tau_test])
    exact_vals = gaussian_g_hat(tau_test)

    # check that g_n is a valid density (positive, normalized)
    omega_test = np.linspace(-6, 6, 1000)
    g_n_vals = np.zeros_like(omega_test)
    for k in range(n_poles):
        if c_normalized[k] > 1e-15:
            g_n_vals += c_normalized[k] * gamma_grid[k] / (np.pi * (omega_test**2 + gamma_grid[k]**2))
    is_positive = np.all(g_n_vals >= -1e-15)
    g_n_integral = np.trapz(g_n_vals, omega_test)

    # K_c for the approximation vs exact
    g_n_at_0 = sum(c_normalized[k] / (np.pi * gamma_grid[k]) for k in range(n_poles) if c_normalized[k] > 1e-15)
    g_exact_at_0 = 1 / np.sqrt(2 * np.pi)
    Kc_ratio = g_n_at_0 / g_exact_at_0

    return {
        'n_poles': n_poles, 'n_active': n_active,
        'c': c_normalized, 'gamma': gamma_grid,
        'l1_error': l1_err,
        'tau_test': tau_test, 'approx_vals': approx_vals, 'exact_vals': exact_vals,
        'is_positive': is_positive, 'integral': g_n_integral,
        'Kc_ratio': Kc_ratio, 'g_at_0': g_n_at_0,
        'residual_norm': residual_norm,
    }

if __name__ == '__main__':
    print("=" * 70)
    print("GAP 1: Positive-weight Lorentzian approximation of Gaussian")
    print("=" * 70)

    for strategy in ['geometric', 'dense_low']:
        print(f"\n--- Gamma strategy: {strategy} ---")
        for n in [5, 10, 20, 40, 80]:
            res = run_nnls_test(n, gamma_strategy=strategy)
            print(f"  n={n:3d}: active={res['n_active']:3d}, "
                  f"L1_err={res['l1_error']:.6f}, "
                  f"pos={res['is_positive']}, "
                  f"integral={res['integral']:.6f}, "
                  f"Kc_ratio={res['Kc_ratio']:.4f}")

    print("\n--- Best configuration: n=40, geometric ---")
    res = run_nnls_test(40, gamma_strategy='geometric')
    print(f"  Active poles: {res['n_active']}")
    print(f"  L1 error: {res['l1_error']:.8f}")
    print(f"  hat_g approximation quality:")
    for i, tau in enumerate(res['tau_test']):
        print(f"    tau={tau:.1f}: exact={res['exact_vals'][i]:.6f}, "
              f"approx={res['approx_vals'][i]:.6f}, "
              f"error={abs(res['approx_vals'][i]-res['exact_vals'][i]):.2e}")

    print(f"\n  Active poles (c_k > 0.001):")
    for k in range(len(res['gamma'])):
        if res['c'][k] > 0.001:
            print(f"    gamma={res['gamma'][k]:.4f}, c={res['c'][k]:.6f}")

    print("\n--- Weighted NNLS (H^1 norm, a=0.3) ---")
    for n in [10, 20, 40, 80]:
        res = run_nnls_test(n, gamma_strategy='geometric', a_weight=0.3)
        h1_err = evaluate_approximation(res['c'], res['gamma'], a=0.3)
        print(f"  n={n:3d}: active={res['n_active']:3d}, "
              f"L1_err={res['l1_error']:.6f}, "
              f"H1_err(a=0.3)={h1_err:.6f}")

    print("\n" + "=" * 70)
    print("CONCLUSION: Can positive-weight Lorentzian mixtures approximate Gaussian?")
    res40 = run_nnls_test(40, gamma_strategy='geometric')
    res80 = run_nnls_test(80, gamma_strategy='geometric')
    print(f"  n=40: L1 error = {res40['l1_error']:.8f}")
    print(f"  n=80: L1 error = {res80['l1_error']:.8f}")
    print(f"  Convergence rate: {np.log(res40['l1_error']/res80['l1_error'])/np.log(2):.2f}x per doubling")
    print("=" * 70)
