"""
SP2 at weak coupling: what does |r(t)| look like very near onset?
Track |r|, Psi, ddot_Psi, and the total variation of dot_Psi.
Key question: does dot_Psi = K|r|^2 have bounded variation?
If so: dot_Psi converges, SP2 solved.
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

def run_weak(K_over_Kc, T=500.0, seed=42):
    n_omega = 400
    omega_max = 8.0
    rng = np.random.default_rng(seed)
    omega_grid = np.linspace(-omega_max, omega_max, n_omega)
    d_omega = omega_grid[1] - omega_grid[0]
    g_vals = gaussian_g(omega_grid)
    K_c = 2 / (np.pi * gaussian_g(0))
    K = K_over_Kc * K_c
    r_star = find_r_star(K, omega_grid, g_vals, d_omega)

    rho0 = rng.uniform(0.1, 0.9, n_omega)
    phi0 = rng.uniform(-np.pi, np.pi, n_omega)
    alpha0 = rho0 * np.exp(1j * phi0 * 0.5)
    alpha0 = enforce_symmetry(alpha0, omega_grid)

    y0 = np.concatenate([np.real(alpha0), np.imag(alpha0)])
    t_eval = np.linspace(0, T, 5000)
    sol = solve_ivp(oa_rhs, [0, T], y0, t_eval=t_eval, method='RK45',
                    args=(omega_grid, g_vals, d_omega, K),
                    rtol=1e-10, atol=1e-12, max_step=0.05)

    rs = []
    for i in range(len(sol.t)):
        a = sol.y[:n_omega, i] + 1j * sol.y[n_omega:, i]
        mask = np.abs(a) >= 1
        if np.any(mask):
            a[mask] = a[mask] / (np.abs(a[mask]) + 1e-8) * 0.9999
        rs.append(np.real(np.sum(a * g_vals * d_omega)))
    rs = np.array(rs)
    dt = np.diff(sol.t)

    dot_psi = K * rs**2
    ddot_psi = np.diff(dot_psi) / dt
    total_var = np.sum(np.abs(np.diff(dot_psi)))

    # Check convergence: std of |r| in windows
    n4 = len(rs) // 4
    windows = [rs[:n4], rs[n4:2*n4], rs[2*n4:3*n4], rs[3*n4:]]
    stds = [np.std(w) for w in windows]

    print(f"K/Kc={K_over_Kc:.3f}, r*={r_star:.4f}, "
          f"|r| final quarter: mean={np.mean(windows[3]):.6f} std={stds[3]:.6f}, "
          f"TV(dot_Psi)={total_var:.4f}, "
          f"std trend: {stds[0]:.4f} → {stds[1]:.4f} → {stds[2]:.4f} → {stds[3]:.4f}")
    return stds[3]

if __name__ == '__main__':
    print("=" * 80)
    print("Weak-coupling SP2: does |r| converge? Is TV(dot_Psi) bounded?")
    print("=" * 80)
    for K_ratio in [1.01, 1.02, 1.05, 1.1, 1.2, 1.3, 1.5]:
        run_weak(K_ratio, T=500.0)
