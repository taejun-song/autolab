"""
Numerical test: does the integral complex pair bound D*S_tilde <= r* * Q_c hold
for the continuum OA equation with Gaussian g?

Under conjugation symmetry alpha(-omega) = conj(alpha(omega)), the L^2_g Lyapunov
derivative is:
    dV/dt = K * [D * S_tilde - r* * Q_c]    (all real)

where:
    p(omega) = alpha(omega) - alpha_star(omega)
    q(omega) = alpha(omega) + 1/alpha_star(omega)
    D       = integral Re(p) * g * domega  (over full line, folded by symmetry)
    S_tilde = integral Re(conj(p)*(1 - alpha^2)) * g * domega
    Q_c     = integral |p|^2 * Re(q) * g * domega
    r*      = integral Re(alpha_star) * g * domega

The pair bound conjecture: D * S_tilde <= r* * Q_c for all alpha in D.
If true: dV/dt <= 0, completing the L^2 Lyapunov proof for the continuum.
If false: the L^2 approach fails and we need the passage-to-limit argument.

This script also computes dV/dt directly (finite differences) as a cross-check.
"""

import numpy as np
from scipy.integrate import solve_ivp

def gaussian_g(omega):
    return np.exp(-omega**2 / 2) / np.sqrt(2 * np.pi)

def find_r_star(K, omega_grid, g_vals, d_omega):
    r = 0.5
    for _ in range(500):
        u = omega_grid / (K * r + 1e-15)
        locked = np.abs(u) <= 1
        beta = np.zeros_like(u, dtype=complex)
        beta[locked] = -1j * u[locked] + np.sqrt(1 - u[locked]**2 + 0j)
        beta[~locked] = -1j * u[~locked] + 1j * u[~locked] * np.sqrt(1 - u[~locked]**(-2) + 0j)
        r_new = np.real(np.sum(beta * g_vals * d_omega))
        if abs(r_new - r) < 1e-14:
            break
        r = 0.5 * r + 0.5 * r_new
    return r

def compute_alpha_star(omega, K, r_star):
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
    dadt = -1j * omega_grid * alpha + (K / 2) * (np.conj(r) - r * alpha**2)
    return np.concatenate([np.real(dadt), np.imag(dadt)])

def compute_pair_bound_quantities(alpha, a_star, g_vals, d_omega, K):
    """Compute D, S_tilde, Q_c, r_star and the pair bound residual."""
    p = alpha - a_star
    q = alpha + 1.0 / a_star
    r_star_val = np.real(np.sum(a_star * g_vals * d_omega))
    r_val = np.sum(alpha * g_vals * d_omega)
    D = np.real(np.sum(p * g_vals * d_omega))
    S_tilde = np.real(np.sum(np.conj(p) * (1 - alpha**2) * g_vals * d_omega))
    Q_c = np.real(np.sum(np.abs(p)**2 * q * g_vals * d_omega))
    DS = D * S_tilde
    rQ = r_star_val * Q_c
    V = np.real(np.sum(np.abs(p)**2 * g_vals * d_omega))
    dVdt_algebraic = K * (DS - rQ)
    return {
        'V': V, 'D': D, 'S_tilde': S_tilde, 'Q_c': Q_c,
        'r_star': r_star_val, 'r': r_val,
        'DS': DS, 'rQ': rQ, 'residual': DS - rQ,
        'dVdt_alg': dVdt_algebraic
    }

def enforce_conjugation_symmetry(alpha, omega_grid):
    """Project alpha to satisfy alpha(-omega) = conj(alpha(omega))."""
    N = len(omega_grid)
    result = alpha.copy()
    for i in range(N // 2):
        j = N - 1 - i
        avg = (alpha[i] + np.conj(alpha[j])) / 2
        result[i] = avg
        result[j] = np.conj(avg)
    return result

def run_test(K_over_Kc, n_omega=400, omega_max=8.0, T=30.0, n_trials=12, seed=42):
    rng = np.random.default_rng(seed)
    omega_grid = np.linspace(-omega_max, omega_max, n_omega)
    d_omega = omega_grid[1] - omega_grid[0]
    g_vals = gaussian_g(omega_grid)
    K_c = 2 / (np.pi * gaussian_g(0))
    K = K_over_Kc * K_c

    r_star = find_r_star(K, omega_grid, g_vals, d_omega)
    a_star = compute_alpha_star(omega_grid, K, r_star)

    print(f"K/Kc = {K_over_Kc:.2f}, K = {K:.4f}, Kc = {K_c:.4f}, r* = {r_star:.6f}")
    print(f"  Locked band: |omega| < {K*r_star:.4f}")

    max_violation = 0.0
    total_steps = 0
    violation_count = 0

    for trial in range(n_trials):
        rho0 = rng.uniform(0.05, 0.95, n_omega)
        phi0 = rng.uniform(-np.pi, np.pi, n_omega)
        alpha0 = rho0 * np.exp(1j * phi0)
        alpha0 = enforce_conjugation_symmetry(alpha0, omega_grid)
        # bias toward positive r(0)
        r0 = np.sum(alpha0 * g_vals * d_omega)
        if np.real(r0) < 0.01:
            alpha0 = rho0 * np.exp(1j * phi0 * 0.3)
            alpha0 = enforce_conjugation_symmetry(alpha0, omega_grid)

        y0 = np.concatenate([np.real(alpha0), np.imag(alpha0)])
        t_eval = np.linspace(0, T, 1000)
        sol = solve_ivp(oa_rhs, [0, T], y0, t_eval=t_eval, method='RK45',
                        args=(omega_grid, g_vals, d_omega, K),
                        rtol=1e-9, atol=1e-11, max_step=0.02)

        residuals = []
        Vs = []
        for i in range(len(sol.t)):
            a = sol.y[:n_omega, i] + 1j * sol.y[n_omega:, i]
            mask = np.abs(a) >= 1
            if np.any(mask):
                a[mask] = a[mask] / (np.abs(a[mask]) + 1e-8) * 0.999
            res = compute_pair_bound_quantities(a, a_star, g_vals, d_omega, K)
            residuals.append(res['residual'])
            Vs.append(res['V'])

        residuals = np.array(residuals)
        Vs = np.array(Vs)
        dV_numerical = np.diff(Vs) / np.diff(sol.t)

        n_steps = len(residuals)
        total_steps += n_steps
        violations = residuals > 1e-10
        n_viol = np.sum(violations)
        violation_count += n_viol
        trial_max = np.max(residuals)
        if trial_max > max_violation:
            max_violation = trial_max

        # cross-check: algebraic dVdt vs numerical
        dVdt_alg_samples = K * residuals[1:-1]
        dV_num_samples = (dV_numerical[:-1] + dV_numerical[1:]) / 2
        max_discrepancy = np.max(np.abs(dVdt_alg_samples - dV_num_samples))

        if n_viol > 0:
            print(f"  Trial {trial:2d}: VIOLATION at {n_viol}/{n_steps} steps, "
                  f"max residual = {trial_max:.4e}, V: {Vs[0]:.4f} -> {Vs[-1]:.6f}, "
                  f"cross-check err = {max_discrepancy:.2e}")
        else:
            print(f"  Trial {trial:2d}: PASS (max residual = {trial_max:.4e}), "
                  f"V: {Vs[0]:.4f} -> {Vs[-1]:.6f}, "
                  f"cross-check err = {max_discrepancy:.2e}")

    print(f"\n  Summary: {violation_count}/{total_steps} violations, "
          f"max residual = {max_violation:.4e}")
    return violation_count == 0

if __name__ == '__main__':
    print("=" * 70)
    print("COMPLEX PAIR BOUND TEST: D*S_tilde <= r* * Q_c")
    print("Continuum OA with Gaussian g, conjugation-symmetric initial data")
    print("=" * 70)

    results = {}
    for label, K_ratio, T, seed in [
        ("moderate coupling", 1.5, 30.0, 42),
        ("strong coupling",   3.0, 20.0, 123),
        ("near onset",        1.1, 50.0, 456),
        ("very strong",       5.0, 15.0, 789),
    ]:
        print(f"\n--- {label} ---")
        ok = run_test(K_ratio, T=T, seed=seed)
        results[label] = ok

    print("\n" + "=" * 70)
    print("FINAL RESULTS:")
    for label, ok in results.items():
        status = "PASS" if ok else "FAIL"
        print(f"  {label:25s}: {status}")
    all_pass = all(results.values())
    print(f"\nOverall: {'ALL PASS — pair bound holds' if all_pass else 'FAILURES DETECTED — pair bound may fail'}")
    print("=" * 70)
