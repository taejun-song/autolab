"""
SP2 Investigation: Does |r(t)| -> r* when Psi -> infinity?

Track the trajectory of |r(t)| for the continuum OA equation with Gaussian g.
Check whether |r(t)| converges, oscillates, or has other behavior.
Also track the "locking fraction" = g-measure of {omega : |alpha(omega)| > 1-epsilon}.
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

def run_sp2_test(K_over_Kc, T=200.0, seed=42):
    n_omega = 400
    omega_max = 8.0
    rng = np.random.default_rng(seed)
    omega_grid = np.linspace(-omega_max, omega_max, n_omega)
    d_omega = omega_grid[1] - omega_grid[0]
    g_vals = gaussian_g(omega_grid)
    K_c = 2 / (np.pi * gaussian_g(0))
    K = K_over_Kc * K_c
    r_star = find_r_star(K, omega_grid, g_vals, d_omega)

    print(f"K/Kc = {K_over_Kc:.2f}, K = {K:.4f}, r* = {r_star:.6f}")

    for trial in range(4):
        rho0 = rng.uniform(0.1, 0.9, n_omega)
        phi0 = rng.uniform(-np.pi, np.pi, n_omega)
        alpha0 = rho0 * np.exp(1j * phi0 * 0.5)
        alpha0 = enforce_symmetry(alpha0, omega_grid)

        y0 = np.concatenate([np.real(alpha0), np.imag(alpha0)])
        t_eval = np.linspace(0, T, 4000)
        sol = solve_ivp(oa_rhs, [0, T], y0, t_eval=t_eval, method='RK45',
                        args=(omega_grid, g_vals, d_omega, K),
                        rtol=1e-10, atol=1e-12, max_step=0.02)

        rs = []
        psis = []
        lock_fracs = []
        for i in range(len(sol.t)):
            a = sol.y[:n_omega, i] + 1j * sol.y[n_omega:, i]
            mask = np.abs(a) >= 1
            if np.any(mask):
                a[mask] = a[mask] / (np.abs(a[mask]) + 1e-8) * 0.9999
            r_val = np.sum(a * g_vals * d_omega)
            rs.append(r_val)
            mod_sq = np.abs(a)**2
            psi = np.real(np.sum(-np.log(np.maximum(1 - mod_sq, 1e-30)) * g_vals * d_omega))
            psis.append(psi)
            lock_frac = np.real(np.sum((mod_sq > 0.81) * g_vals * d_omega))
            lock_fracs.append(lock_frac)

        rs = np.array(rs)
        psis = np.array(psis)
        lock_fracs = np.array(lock_fracs)
        abs_rs = np.abs(rs)

        # check |r| convergence in last quarter
        last_quarter = abs_rs[3*len(abs_rs)//4:]
        r_mean = np.mean(last_quarter)
        r_std = np.std(last_quarter)
        r_osc = np.max(last_quarter) - np.min(last_quarter)
        phase_rs = np.angle(rs)
        phase_last = phase_rs[3*len(phase_rs)//4:]
        phase_drift = phase_last[-1] - phase_last[0]

        # also check d/dt|r|^2
        abs_r_sq = abs_rs**2
        d_abs_r_sq = np.diff(abs_r_sq) / np.diff(sol.t)

        print(f"  Trial {trial}: |r|(T)={abs_rs[-1]:.6f}, "
              f"|r| mean(last 1/4)={r_mean:.6f} ± {r_std:.6f}, "
              f"osc={r_osc:.6f}, "
              f"Psi(T)={psis[-1]:.1f}, lock_frac(T)={lock_fracs[-1]:.4f}")
        print(f"           phase_drift={phase_drift:.4f}, "
              f"d|r|^2/dt last={np.mean(d_abs_r_sq[-100:]):.2e}")

if __name__ == '__main__':
    print("=" * 70)
    print("SP2: Does |r(t)| -> r* when Psi -> infinity?")
    print("=" * 70)

    for K_ratio in [1.1, 1.3, 1.5, 2.0, 3.0]:
        print(f"\n--- K/Kc = {K_ratio} ---")
        run_sp2_test(K_ratio, T=200.0)
