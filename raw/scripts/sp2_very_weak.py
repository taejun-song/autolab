"""
Very weak coupling (K/Kc = 1.01): run for T=5000 to check if |r| eventually converges.
"""

import numpy as np
from scipy.integrate import solve_ivp

def gaussian_g(omega):
    return np.exp(-omega**2 / 2) / np.sqrt(2 * np.pi)

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

n_omega = 400
omega_max = 8.0
rng = np.random.default_rng(42)
omega_grid = np.linspace(-omega_max, omega_max, n_omega)
d_omega = omega_grid[1] - omega_grid[0]
g_vals = gaussian_g(omega_grid)
K_c = 2 / (np.pi * gaussian_g(0))
K = 1.01 * K_c

rho0 = rng.uniform(0.1, 0.9, n_omega)
phi0 = rng.uniform(-np.pi, np.pi, n_omega)
alpha0 = rho0 * np.exp(1j * phi0 * 0.5)
alpha0 = enforce_symmetry(alpha0, omega_grid)
y0 = np.concatenate([np.real(alpha0), np.imag(alpha0)])

print(f"K/Kc = 1.01, K = {K:.4f}, Kc = {K_c:.4f}")

for T_end, label in [(500, "T=500"), (2000, "T=2000"), (5000, "T=5000")]:
    t_eval = np.linspace(0, T_end, min(T_end * 10, 20000))
    sol = solve_ivp(oa_rhs, [0, T_end], y0, t_eval=t_eval, method='RK45',
                    args=(omega_grid, g_vals, d_omega, K),
                    rtol=1e-10, atol=1e-12, max_step=0.1)
    rs = []
    for i in range(len(sol.t)):
        a = sol.y[:n_omega, i] + 1j * sol.y[n_omega:, i]
        mask = np.abs(a) >= 1
        if np.any(mask):
            a[mask] = a[mask] / (np.abs(a[mask]) + 1e-8) * 0.9999
        rs.append(np.real(np.sum(a * g_vals * d_omega)))
    rs = np.array(rs)
    n4 = len(rs) // 4
    last = rs[3*n4:]
    print(f"  {label}: |r| last 1/4: mean={np.mean(last):.6f}, std={np.std(last):.6f}, "
          f"min={np.min(last):.6f}, max={np.max(last):.6f}")
