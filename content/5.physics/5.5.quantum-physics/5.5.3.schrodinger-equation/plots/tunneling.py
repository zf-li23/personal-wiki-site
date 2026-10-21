"""Rectangular barrier: probability density of a scattering state, and transmission coefficient versus width."""

import numpy as np
import matplotlib.pyplot as plt

hbar = 1.054571817e-34
me = 9.1093837e-31
eV = 1.602176634e-19


def transmission(E, U0, a):
    # exact transmission through a rectangular barrier, E < U0
    kappa = np.sqrt(2 * me * (U0 - E) * eV) / hbar
    return 1 / (1 + U0**2 * np.sinh(kappa * a) ** 2 / (4 * E * (U0 - E)))


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.3))

# dimensionless scattering state: hbar = 2m = 1, U0 = 1, E = 0.5, width a = 2.5
U0, E, a = 1.0, 0.5, 2.5
k = np.sqrt(E)
q = np.sqrt(U0 - E)
# unknowns: B (reflected), C, D (inside), F (transmitted); incident amplitude 1
M = np.array([
    [-1, 1, 1, 0],
    [1j * k, -q, q, 0],
    [0, np.exp(-q * a), np.exp(q * a), -np.exp(1j * k * a)],
    [0, -q * np.exp(-q * a), q * np.exp(q * a), -1j * k * np.exp(1j * k * a)],
], dtype=complex)
rhs = np.array([1, 1j * k, 0, 0], dtype=complex)
B, C, D, F = np.linalg.solve(M, rhs)

x1 = np.linspace(-12, 0, 600)
x2 = np.linspace(0, a, 200)
x3 = np.linspace(a, 14, 600)
p1 = np.abs(np.exp(1j * k * x1) + B * np.exp(-1j * k * x1)) ** 2
p2 = np.abs(C * np.exp(-q * x2) + D * np.exp(q * x2)) ** 2
p3 = np.abs(F * np.exp(1j * k * x3)) ** 2 * np.ones_like(x3)
ax1.fill_between([0, a], 0, 4.2, color="0.85", lw=0)
ax1.plot(x1, p1, color="C0", lw=1.6)
ax1.plot(x2, p2, color="C0", lw=1.6)
ax1.plot(x3, p3, color="C0", lw=1.6)
ax1.text(a / 2, 3.9, "barrier", ha="center", fontsize=9)
ax1.text(-6, 3.75, "incident + reflected", ha="center", fontsize=9)
ax1.text(8.5, abs(F) ** 2 + 0.25, f"transmitted, T = {abs(F) ** 2:.2f}", ha="center", fontsize=9)
ax1.set_xlim(-12, 14)
ax1.set_ylim(0, 4.2)
ax1.set_xlabel(r"$x\,/\,(\hbar/\sqrt{2mU_0})$")
ax1.set_ylabel(r"$|\Phi|^2$ (incident wave $|A|^2 = 1$)")
ax1.set_title(r"Scattering state, $E = U_0/2$")

w = np.linspace(0.05, 1.5, 300) * 1e-9
for i, (E, U0) in enumerate([(5.0, 10.0), (1.0, 6.0)]):
    kappa = np.sqrt(2 * me * (U0 - E) * eV) / hbar
    ax2.semilogy(w * 1e9, transmission(E, U0, w), color=f"C{i}", lw=1.8,
                 label=f"exact, $E$ = {E:g} eV, $U_0$ = {U0:g} eV")
    ax2.semilogy(w * 1e9, np.exp(-2 * kappa * w), color=f"C{i}", ls="--", lw=1.1,
                 label=r"$\mathrm{e}^{-2\kappa a}$")
ax2.set_xlabel("barrier width a / nm")
ax2.set_ylabel("transmission coefficient T")
ax2.set_title("Electron tunneling through a barrier")
ax2.set_ylim(1e-17, 1.5)
ax2.legend(fontsize=8)

fig.tight_layout()
