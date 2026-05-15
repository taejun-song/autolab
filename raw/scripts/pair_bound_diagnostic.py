"""
Diagnostic: track V(t) trajectory and dV/dt sign for the near-onset failure cases.
Does V eventually decrease, or does it genuinely grow?
Also check whether the failing trajectories converge to incoherence vs PLS.
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

def enforce_symmetry(alpha, omega_grid):
    N = len(omega_grid)
    result = alpha.copy()
    for i in range(N // 2):
        j = N - 1 - i
        avg = (alpha[i] + np.conj(alpha[j])) / 2
        result[i] = avg
        result[j] = np.conj(avg)
    return result

def run_diagnostic(K_over_Kc, T=100.0, seed=456):
    n_omega = 400
    omega_max = 8.0
    rng = np.random.default_rng(seed)
    omega_grid = np.linspace(-omega_max, omega_max, n_omega)
    d_omega = omega_grid[1] - omega_grid[0]
    g_vals = gaussian_g(omega_grid)
    K_c = 2 / (np.pi * gaussian_g(0))
    K = K_over_Kc * K_c
    r_star = find_r_star(K, omega_grid, g_vals, d_omega)
    a_star = compute_alpha_star(omega_grid, K, r_star)

    print(f"K/Kc = {K_over_Kc:.2f}, r* = {r_star:.6f}")

    for trial in range(6):
        rho0 = rng.uniform(0.05, 0.95, n_omega)
        phi0 = rng.uniform(-np.pi, np.pi, n_omega)
        alpha0 = rho0 * np.exp(1j * phi0)
        alpha0 = enforce_symmetry(alpha0, omega_grid)
        r0 = np.real(np.sum(alpha0 * g_vals * d_omega))
        if r0 < 0.01:
            alpha0 = rho0 * np.exp(1j * phi0 * 0.3)
            alpha0 = enforce_symmetry(alpha0, omega_grid)

        y0 = np.concatenate([np.real(alpha0), np.imag(alpha0)])
        t_eval = np.linspace(0, T, 2000)
        sol = solve_ivp(oa_rhs, [0, T], y0, t_eval=t_eval, method='RK45',
                        args=(omega_grid, g_vals, d_omega, K),
                        rtol=1e-9, atol=1e-11, max_step=0.02)

        Vs, rs, Psis = [], [], []
        for i in range(len(sol.t)):
            a = sol.y[:n_omega, i] + 1j * sol.y[n_omega:, i]
            mask = np.abs(a) >= 1
            if np.any(mask):
                a[mask] = a[mask] / (np.abs(a[mask]) + 1e-8) * 0.999
            p = a - a_star
            V = np.real(np.sum(np.abs(p)**2 * g_vals * d_omega))
            r_val = np.abs(np.sum(a * g_vals * d_omega))
            psi_integrand = -np.log(np.maximum(1 - np.abs(a)**2, 1e-30))
            psi = np.real(np.sum(psi_integrand * g_vals * d_omega))
            Vs.append(V)
            rs.append(r_val)
            Psis.append(psi)

        Vs = np.array(Vs)
        rs = np.array(rs)
        V_max_idx = np.argmax(Vs)
        V_max_t = sol.t[V_max_idx]

        target = "PLS" if rs[-1] > 0.1 else "incoherence"
        print(f"  Trial {trial}: V(0)={Vs[0]:.3f}, V_max={Vs[V_max_idx]:.3f} at t={V_max_t:.1f}, "
              f"V(T)={Vs[-1]:.4f}, |r|(T)={rs[-1]:.4f} -> {target}, "
              f"Psi(T)={Psis[-1]:.2f}")

if __name__ == '__main__':
    print("=== Near onset (K/Kc = 1.1), T=100 ===")
    run_diagnostic(1.1, T=100.0, seed=456)
    print("\n=== Moderate (K/Kc = 1.5), T=100 ===")
    run_diagnostic(1.5, T=100.0, seed=42)
    print("\n=== K/Kc = 2.0, T=60 ===")
    run_diagnostic(2.0, T=60.0, seed=99)
