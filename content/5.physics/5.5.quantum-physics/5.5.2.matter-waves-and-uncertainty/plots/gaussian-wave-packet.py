"""Gaussian wave packets: a narrow and a wide packet in position space and their momentum distributions (hbar = 1).
For a Gaussian, sigma_x * sigma_p = hbar / 2 exactly."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8, 8, 2000)
p = np.linspace(-1, 9, 2000)
p0 = 4.0

fig, axes = plt.subplots(2, 2, figsize=(10.5, 5.6), sharex="col")
for row, sx in enumerate([0.6, 1.8]):
    sp = 0.5 / sx
    psi = (2 * np.pi * sx ** 2) ** -0.25 * np.exp(-x ** 2 / (4 * sx ** 2) + 1j * p0 * x)
    phi2 = np.exp(-(p - p0) ** 2 / (2 * sp ** 2)) / np.sqrt(2 * np.pi * sp ** 2)

    ax = axes[row, 0]
    ax.plot(x, psi.real, color="C0", lw=1.0, label="Re ψ(x)")
    ax.plot(x, np.abs(psi) ** 2, color="C3", lw=1.8, label="|ψ(x)|²")
    ax.plot(x, -np.abs(psi) ** 2, color="C3", lw=0.6, ls=":")
    ax.axvspan(-sx, sx, color="C3", alpha=0.1, lw=0)
    ax.set_ylabel(f"σ_x = {sx}")
    ax.set_xlim(-8, 8)
    ax.legend(loc="upper right", fontsize=8, frameon=False)

    ax = axes[row, 1]
    ax.plot(p, phi2, color="C2", lw=1.8, label="|φ(p)|²")
    ax.axvspan(p0 - sp, p0 + sp, color="C2", alpha=0.1, lw=0)
    ax.text(0.02, 0.85, f"σ_p = {sp:.3g},  σ_x σ_p = {sx * sp:.2f} ħ", transform=ax.transAxes, fontsize=9)
    ax.set_xlim(-1, 9)
    ax.set_ylim(0, 1.6)
    ax.legend(loc="upper right", fontsize=8, frameon=False)

axes[0, 0].set_title("position space")
axes[0, 1].set_title("momentum space (centred at p0)")
axes[1, 0].set_xlabel("x")
axes[1, 1].set_xlabel("p")
fig.tight_layout()
