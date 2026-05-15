"""
Verify the SP2 bootstrap: check that the adiabatic constant C_A * C_B < 1 - F'(r*).
C_A = ∫ g * ||d_r alpha*|| / lambda domega
C_B = sensitivity of dot_E to dot_r
F'(r*) = derivative of self-consistency map at PLS
"""

import numpy as np

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

def compute_F_prime(K, r_star, omega_grid, g_vals, d_omega):
    """Numerical derivative F'(r*) via finite differences."""
    dr = 1e-7
    def F(r):
        u = omega_grid / (K * r + 1e-15)
        locked = np.abs(u) <= 1
        beta = np.zeros_like(u, dtype=complex)
        beta[locked] = -1j * u[locked] + np.sqrt(1 - u[locked]**2 + 0j)
        beta[~locked] = -1j * u[~locked] + 1j * u[~locked] * np.sqrt(1 - u[~locked]**(-2) + 0j)
        return np.real(np.sum(beta * g_vals * d_omega))
    return (F(r_star + dr) - F(r_star - dr)) / (2 * dr)

def compute_contraction_rate(omega, K, r):
    """Contraction rate lambda(omega) of the Riccati at the fixed point."""
    u = abs(omega) / (K * r + 1e-15)
    if u < 1:
        return K * np.sqrt(r**2 - omega**2 / K**2)
    else:
        return K**2 * r**2 / (2 * omega**2 + 1e-15)

def compute_C_A(K, r_star, omega_grid, g_vals, d_omega):
    """C_A = ∫ g * |d_r alpha*| / lambda domega."""
    dr = 1e-7
    C_A = 0.0
    for i, omega in enumerate(omega_grid):
        lam = compute_contraction_rate(omega, K, r_star)
        if lam < 1e-10:
            continue
        u1 = omega / (K * (r_star + dr) + 1e-15)
        u2 = omega / (K * (r_star - dr) + 1e-15)
        def beta_val(u):
            if abs(u) <= 1:
                return -1j * u + np.sqrt(1 - u**2 + 0j)
            else:
                return -1j * u + 1j * u * np.sqrt(1 - u**(-2) + 0j)
        d_alpha = abs(beta_val(u1) - beta_val(u2)) / (2 * dr)
        C_A += g_vals[i] * d_alpha / lam * d_omega
    return C_A

if __name__ == '__main__':
    n_omega = 2000
    omega_max = 10.0
    omega_grid = np.linspace(-omega_max, omega_max, n_omega)
    d_omega = omega_grid[1] - omega_grid[0]
    g_vals = gaussian_g(omega_grid)
    K_c = 2 / (np.pi * gaussian_g(0))

    print(f"{'K/Kc':>8} {'r*':>8} {'F_prime':>8} {'1-F_prime':>10} {'C_A':>8} {'margin':>10}")
    print("-" * 60)

    for K_ratio in [1.05, 1.1, 1.2, 1.3, 1.5, 2.0, 3.0, 5.0]:
        K = K_ratio * K_c
        r_star = find_r_star(K, omega_grid, g_vals, d_omega)
        F_prime = compute_F_prime(K, r_star, omega_grid, g_vals, d_omega)
        C_A = compute_C_A(K, r_star, omega_grid, g_vals, d_omega)
        margin = (1 - F_prime) - C_A
        print(f"{K_ratio:8.2f} {r_star:8.4f} {F_prime:8.4f} {1-F_prime:10.4f} {C_A:8.4f} {margin:10.4f} "
              f"{'OK' if margin > 0 else 'FAIL'}")
