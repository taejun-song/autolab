"""
SP2 attack: self-consistency tightening.

Hypothesis: as Psi -> infinity, the "self-consistency error"
  E(t) = |r(t) - F(r(t))|
where F(r) = integral alpha_star(omega; r) g(omega) domega
(the self-consistency map evaluated at the CURRENT r),
goes to 0. This would force |r| -> r* since F(r*) = r*.

The mechanism: locked oscillators have alpha(omega) ≈ alpha_star(omega; r(t)),
so r(t) ≈ integral alpha_star(omega; r(t)) g domega = F(r(t)).

Test: track E(t) along OA trajectories and check E(t) -> 0.
Also track the "locking quality" = integral_locked |alpha - alpha_star(omega;r(t))|^2 g.
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

def alpha_star_at_r(omega_grid, K, r):
    """PLS profile at mean-field value r (not r*)."""
    if abs(r) < 1e-15:
        return np.zeros_like(omega_grid, dtype=complex)
    u = omega_grid / (K * r + 1e-15)
    result = np.zeros_like(omega_grid, dtype=complex)
    locked = np.abs(u) <= 1
    result[locked] = -1j * u[locked] + np.sqrt(1 - u[locked]**2 + 0j)
    result[~locked] = -1j * u[~locked] + 1j * u[~locked] * np.sqrt(1 - u[~locked]**(-2) + 0j)
    return result

def self_consistency_map(r, K, omega_grid, g_vals, d_omega):
    """F(r) = integral alpha_star(omega; r) g(omega) domega."""
    a_star = alpha_star_at_r(omega_grid, K, r)
    return np.real(np.sum(a_star * g_vals * d_omega))

def oa_rhs(t, alpha_flat, omega_grid, g_vals, d_omega, K):
    N = len(omega_grid)
    alpha = alpha_flat[:N] + 1j * alpha_flat[N:]
    r = np.sum(alpha * g_vals * d_omega)
    dadt = -1j * omega_grid * alpha + (K / 2) * (np.conj(r) - r * alpha**2)
    return np.concatenate([np.real(dadt), np.imag(dadt)])

def enforce_symmetry(alpha, omega_grid):
    N = len(omega_grid)
    result = alpha.copy()
    for i in range(N // 2):
        j = N - 1 - i
        avg = (alpha[i] + np.conj(alpha[j])) / 2
        result[i] = avg
        result[j] = np.conj(avg)
    return result

def run_test(K_over_Kc, T=200.0, seed=42):
    n_omega = 400
    omega_max = 8.0
    rng = np.random.default_rng(seed)
    omega_grid = np.linspace(-omega_max, omega_max, n_omega)
    d_omega = omega_grid[1] - omega_grid[0]
    g_vals = gaussian_g(omega_grid)
    K_c = 2 / (np.pi * gaussian_g(0))
    K = K_over_Kc * K_c
    r_star = find_r_star(K, omega_grid, g_vals, d_omega)

    print(f"K/Kc = {K_over_Kc:.2f}, r* = {r_star:.6f}")

    for trial in range(3):
        rho0 = rng.uniform(0.1, 0.9, n_omega)
        phi0 = rng.uniform(-np.pi, np.pi, n_omega)
        alpha0 = rho0 * np.exp(1j * phi0 * 0.5)
        alpha0 = enforce_symmetry(alpha0, omega_grid)

        y0 = np.concatenate([np.real(alpha0), np.imag(alpha0)])
        t_eval = np.linspace(0, T, 2000)
        sol = solve_ivp(oa_rhs, [0, T], y0, t_eval=t_eval, method='RK45',
                        args=(omega_grid, g_vals, d_omega, K),
                        rtol=1e-10, atol=1e-12, max_step=0.02)

        errors = []
        rs = []
        lock_quals = []
        psis = []
        for i in range(0, len(sol.t), 10):
            a = sol.y[:n_omega, i] + 1j * sol.y[n_omega:, i]
            mask = np.abs(a) >= 1
            if np.any(mask):
                a[mask] = a[mask] / (np.abs(a[mask]) + 1e-8) * 0.9999

            r_val = np.real(np.sum(a * g_vals * d_omega))
            F_r = self_consistency_map(r_val, K, omega_grid, g_vals, d_omega)
            error = abs(r_val - F_r)

            a_star_r = alpha_star_at_r(omega_grid, K, r_val)
            locked = np.abs(omega_grid) < K * abs(r_val)
            if np.any(locked):
                lock_qual = np.real(np.sum(np.abs(a[locked] - a_star_r[locked])**2 * g_vals[locked] * d_omega))
            else:
                lock_qual = 0.0

            psi = np.real(np.sum(-np.log(np.maximum(1 - np.abs(a)**2, 1e-30)) * g_vals * d_omega))

            errors.append(error)
            rs.append(r_val)
            psis.append(psi)
            lock_quals.append(lock_qual)

        errors = np.array(errors)
        rs = np.array(rs)
        psis = np.array(psis)
        lock_quals = np.array(lock_quals)
        ts = sol.t[::10]

        last_q = len(errors) // 4
        print(f"  Trial {trial}: |r-F(r)| last quarter: mean={np.mean(errors[-last_q:]):.6f}, "
              f"max={np.max(errors[-last_q:]):.6f}; "
              f"lock_qual last q: {np.mean(lock_quals[-last_q:]):.6f}; "
              f"|r|(T)={rs[-1]:.6f}, Psi(T)={psis[-1]:.1f}")
        # Check if E(t) is correlated with 1/Psi
        if psis[-1] > 1:
            late_errors = errors[-last_q:]
            late_psis = psis[-last_q:]
            corr = np.corrcoef(late_errors, 1.0/late_psis)[0,1] if np.std(late_psis) > 0 else 0
            print(f"           corr(E, 1/Psi) = {corr:.4f}")

if __name__ == '__main__':
    print("=" * 70)
    print("SP2: Self-consistency tightening")
    print("E(t) = |r(t) - F(r(t))| -> 0 as Psi -> infinity?")
    print("=" * 70)

    for K_ratio in [1.1, 1.3, 1.5, 2.0, 3.0]:
        print(f"\n--- K/Kc = {K_ratio} ---")
        run_test(K_ratio, T=300.0)
