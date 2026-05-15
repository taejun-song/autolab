"""
Test Path B: Busemann kernel H_B = log((1 - |alpha|^2) / |1 - conj(alpha_star)*alpha|^2)

The Busemann kernel differs from the log-ratio kernel in the denominator:
  log-ratio:  |alpha - alpha_star|^2
  Busemann:   |1 - conj(alpha_star)*alpha|^2

For |alpha_star| = 1 (locked oscillators), these are proportional.
For |alpha_star| < 1 (drifting oscillators), the Busemann denominator
is related to the hyperbolic distance via the Poincare disk model.

Also test a weighted kernel: w(omega) * H_log_ratio where w is chosen
to suppress the rotation contribution.
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def gaussian_g(omega):
    return np.exp(-omega**2 / 2) / np.sqrt(2 * np.pi)


def find_r_star(K, omega_grid, d_omega):
    r = 0.5
    g_vals = gaussian_g(omega_grid)
    for _ in range(200):
        u = omega_grid / (K * r + 1e-15)
        locked = np.abs(u) <= 1
        beta_vals = np.zeros_like(u, dtype=complex)
        beta_vals[locked] = -1j * u[locked] + np.sqrt(1 - u[locked]**2 + 0j)
        beta_vals[~locked] = -1j * u[~locked] + 1j * u[~locked] * np.sqrt(1 - u[~locked]**(-2) + 0j)
        r_new = np.real(np.sum(beta_vals * g_vals * d_omega))
        if abs(r_new - r) < 1e-12:
            break
        r = 0.5 * r + 0.5 * r_new
    return r


def alpha_star_func(omega, K, r_star):
    u = omega / (K * r_star + 1e-15)
    result = np.zeros_like(omega, dtype=complex)
    locked = np.abs(u) <= 1
    result[locked] = -1j * u[locked] + np.sqrt(1 - u[locked]**2 + 0j)
    result[~locked] = -1j * u[~locked] + 1j * u[~locked] * np.sqrt(1 - u[~locked]**(-2) + 0j)
    return result


def oa_rhs(t, alpha_flat, omega_grid, g_vals, d_omega, K):
    N = len(omega_grid)
    alpha = alpha_flat[:N] + 1j * alpha_flat[N:]
    r = np.sum(alpha * g_vals * d_omega)
    dadt = -1j * omega_grid * alpha + (K / 2) * (r - np.conj(r) * alpha**2)
    return np.concatenate([np.real(dadt), np.imag(dadt)])


def phi_busemann(alpha, a_star, g_vals, d_omega):
    """Busemann kernel: log((1 - |alpha|^2) / |1 - conj(a_star)*alpha|^2)"""
    numer = np.maximum(1 - np.abs(alpha)**2, 1e-30)
    denom = np.maximum(np.abs(1 - np.conj(a_star) * alpha)**2, 1e-30)
    return np.sum(g_vals * np.log(numer / denom) * d_omega)


def phi_hyp_dist(alpha, a_star, g_vals, d_omega):
    """Negative hyperbolic distance squared: -d_hyp(alpha, alpha_star)^2
    d_hyp = arctanh(|(alpha - a_star)/(1 - conj(a_star)*alpha)|)"""
    pseudo = np.abs((alpha - a_star) / (1 - np.conj(a_star) * alpha + 1e-30))
    pseudo = np.minimum(pseudo, 1 - 1e-10)
    d_hyp = np.arctanh(pseudo)
    return -np.sum(g_vals * d_hyp**2 * d_omega)


def phi_log_cross_ratio(alpha, a_star, g_vals, d_omega):
    """Log cross-ratio: log((1-|alpha|^2)(1-|a_star|^2) / |alpha - a_star|^2)
    This is the symmetrized version that equals -2*log(tanh(d_hyp/2))."""
    numer = np.maximum((1 - np.abs(alpha)**2) * (1 - np.abs(a_star)**2), 1e-30)
    denom = np.maximum(np.abs(alpha - a_star)**2, 1e-30)
    return np.sum(g_vals * np.log(numer / denom) * d_omega)


def run_kernel_test(K, kernel_name, kernel_func, n_omega=200, omega_max=6.0,
                    T=20.0, n_trials=8, seed=42):
    rng = np.random.default_rng(seed)
    omega_grid = np.linspace(-omega_max, omega_max, n_omega)
    d_omega = omega_grid[1] - omega_grid[0]
    g_vals = gaussian_g(omega_grid)
    K_c = 2 / (np.pi * gaussian_g(0))

    r_star = find_r_star(K, omega_grid, d_omega)
    a_star = alpha_star_func(omega_grid, K, r_star)

    n_pass = 0
    for trial in range(n_trials):
        rho0 = rng.uniform(0.1, 0.9, n_omega)
        phi0 = rng.uniform(-np.pi, np.pi, n_omega)
        alpha0 = rho0 * np.exp(1j * phi0 * 0.3)
        y0 = np.concatenate([np.real(alpha0), np.imag(alpha0)])

        t_eval = np.linspace(0, T, 500)
        sol = solve_ivp(oa_rhs, [0, T], y0, t_eval=t_eval, method='RK45',
                        args=(omega_grid, g_vals, d_omega, K),
                        rtol=1e-8, atol=1e-10, max_step=0.05)

        phis = []
        for i in range(len(sol.t)):
            a = sol.y[:n_omega, i] + 1j * sol.y[n_omega:, i]
            mask = np.abs(a) >= 1
            if np.any(mask):
                a[mask] = a[mask] / (np.abs(a[mask]) + 1e-6) * 0.999
            phis.append(kernel_func(a, a_star, g_vals, d_omega))

        phis = np.array(phis)
        diffs = np.diff(phis)
        n_increases = np.sum(diffs > 1e-8)
        if n_increases == 0:
            n_pass += 1
            status = "✓"
        else:
            status = f"✗ ({n_increases} increases, max={np.max(diffs):.2e})"
        print(f"  {kernel_name} trial {trial}: {status} (Phi: {phis[0]:.3f} -> {phis[-1]:.3f})")

    return n_pass


if __name__ == '__main__':
    K_c = 2 / (np.pi * gaussian_g(0))
    K = 1.5 * K_c

    print(f"K_c = {K_c:.4f}, K = {K:.4f}")
    print()

    kernels = [
        ("Busemann", phi_busemann),
        ("Neg-hyp-dist-sq", phi_hyp_dist),
        ("Log-cross-ratio", phi_log_cross_ratio),
    ]

    results = {}
    for name, func in kernels:
        print(f"--- {name} kernel (K = 1.5*Kc) ---")
        n = run_kernel_test(K, name, func)
        results[name] = n
        print(f"  Passed: {n}/8\n")

    print("=" * 60)
    print("SUMMARY (K = 1.5 * K_c, Gaussian g, 8 trials each)")
    print("=" * 60)
    for name, n in results.items():
        status = "PASS" if n == 8 else "FAIL"
        print(f"  {name:20s}: {n}/8 monotone  [{status}]")
    print("=" * 60)

    best = max(results, key=results.get)
    if results[best] == 8:
        print(f"\nBest kernel: {best} — monotone in all trials!")
    else:
        print(f"\nNo kernel achieved full monotonicity.")
        print(f"Best: {best} ({results[best]}/8)")
        print("Further kernel engineering needed.")
