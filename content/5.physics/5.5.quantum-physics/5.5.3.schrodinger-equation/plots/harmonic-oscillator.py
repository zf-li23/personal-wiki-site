"""Quantum harmonic oscillator: eigenfunctions in the parabolic potential, and n = 11 density versus the classical one."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_hermite, factorial

xi = np.linspace(-5.5, 5.5, 2000)  # xi = alpha x


def psi(n, xi):
    norm = 1 / np.sqrt(2.0**n * factorial(n) * np.sqrt(np.pi))
    return norm * eval_hermite(n, xi) * np.exp(-xi**2 / 2)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.6))

ax1.plot(xi, xi**2 / 2, color="0.4", lw=1.2)
for n in range(5):
    E = n + 0.5
    turn = np.sqrt(2 * n + 1)
    ax1.plot([-turn, turn], [E, E], color="0.6", lw=0.6, ls=":")
    ax1.plot(xi, E + 0.7 * psi(n, xi), color=f"C{n}", lw=1.6)
    ax1.text(4.0, E, f"n = {n}", va="center", fontsize=9)
ax1.set_xlim(-4.5, 4.9)
ax1.set_ylim(0, 5.6)
ax1.set_xlabel(r"$\alpha x$")
ax1.set_ylabel(r"$E\,/\,\hbar\omega$")
ax1.set_title(r"$\Phi_n$ at $E_n = (n + 1/2)\hbar\omega$, with $U(x)$")

n = 11
A = np.sqrt(2 * n + 1)
ax2.plot(xi, psi(n, xi) ** 2, color="C0", lw=1.5, label=r"quantum, $|\Phi_{11}|^2$")
xc = np.linspace(-A + 1e-3, A - 1e-3, 1000)
ax2.plot(xc, 1 / (np.pi * np.sqrt(A**2 - xc**2)), "k--", lw=1.2, label="classical")
ax2.axvline(-A, color="0.6", lw=0.8, ls=":")
ax2.axvline(A, color="0.6", lw=0.8, ls=":")
ax2.set_xlim(-6, 6)
ax2.set_ylim(0, 0.4)
ax2.set_xlabel(r"$\alpha x$")
ax2.set_ylabel(r"probability density / $\alpha$")
ax2.set_title("n = 11: quantum and classical distributions")
ax2.legend(fontsize=8, loc="upper center")

fig.tight_layout()
