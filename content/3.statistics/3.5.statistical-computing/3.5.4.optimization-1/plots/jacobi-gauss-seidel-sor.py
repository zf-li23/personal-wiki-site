"""Jacobi, Gauss-Seidel and SOR iterations for a 3 x 3 symmetric positive definite system."""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[4.0, 3, 0], [3, 4, -1], [0, -1, 4]])
b = np.array([24.0, 30, -24])
x_true = np.linalg.solve(A, b)  # (3, 4, -5)
n_iter = 40


def iterate(omega=None, jacobi=False):
    x = np.ones(3)
    errs = []
    for _ in range(n_iter):
        x_old = x.copy()
        for i in range(3):
            src = x_old if jacobi else x  # Jacobi uses only old values
            s = b[i] - A[i] @ src + A[i, i] * src[i]
            gs = s / A[i, i]
            x[i] = gs if omega is None else (1 - omega) * x_old[i] + omega * gs
        errs.append(np.max(np.abs(x - x_true)))
    return np.array(errs)


D = np.diag(np.diag(A))
L = np.tril(A, -1)
U = np.triu(A, 1)
rho = lambda B: max(abs(np.linalg.eigvals(B)))
rho_j = rho(-np.linalg.solve(D, L + U))
rho_gs = rho(-np.linalg.solve(D + L, U))
w = 1.25
rho_sor = rho(np.linalg.solve(D + w * L, -(w * U + (w - 1) * D)))

k = np.arange(1, n_iter + 1)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
ax = axes[0]
for errs, label, c in [
    (iterate(jacobi=True), f"Jacobi, rho(B) = {rho_j:.3f}", "C0"),
    (iterate(), f"Gauss-Seidel, rho(B) = {rho_gs:.3f}", "C1"),
    (iterate(omega=w), f"SOR omega = 1.25, rho(B) = {rho_sor:.3f}", "C3"),
]:
    ax.semilogy(k, errs, marker="o", ms=3, lw=1.3, color=c, label=label)
ax.set_xlabel("iteration t")
ax.set_ylabel("max |x(t) - x*|")
ax.set_title("4x1 + 3x2 = 24, 3x1 + 4x2 - x3 = 30, -x2 + 4x3 = -24")
ax.set_ylim(1e-16, 10)
ax.grid(alpha=0.3)
ax.legend(loc="upper right", fontsize=9)

ax = axes[1]
omegas = np.linspace(0.05, 1.95, 191)
rhos = [rho(np.linalg.solve(D + o * L, -(o * U + (o - 1) * D))) for o in omegas]
ax.plot(omegas, rhos, color="C3", lw=1.6, label="rho(B_omega)")
ax.plot(omegas, np.abs(omegas - 1), color="gray", ls="--", lw=1, label="|omega - 1| (lower bound)")
best = 2 / (1 + np.sqrt(1 - rho_j**2))  # optimal omega for this consistently ordered matrix
ax.axvline(best, color="C2", lw=1, ls=":", label=f"optimal omega = {best:.3f}")
ax.set_xlabel("relaxation factor omega")
ax.set_ylabel("spectral radius")
ax.set_title("Spectral radius of the SOR iteration matrix")
ax.set_ylim(0, 1.05)
ax.grid(alpha=0.3)
ax.legend(loc="upper center", fontsize=9)
fig.tight_layout()
