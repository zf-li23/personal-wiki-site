"""Compton scattering: wavelength shift versus angle, and schematic scattered spectra at four angles."""

import numpy as np
import matplotlib.pyplot as plt

lam_C = 2.42631e-3  # nm
lam0 = 0.0709       # Mo K-alpha line, nm

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.2))

th = np.linspace(0, np.pi, 400)
ax1.plot(np.degrees(th), lam_C * (1 - np.cos(th)) * 1e3, color="C0", lw=1.8)
ax1.axhline(2 * lam_C * 1e3, color="0.5", ls=":", lw=1.0)
ax1.text(5, 2 * lam_C * 1e3 + 0.12, "maximum 2λ_C = 4.85 pm (backscattering)", fontsize=8, color="0.4")
ax1.axhline(lam_C * 1e3, color="0.5", ls=":", lw=1.0)
ax1.text(5, lam_C * 1e3 + 0.12, "λ_C = h / (m_e c) = 2.43 pm (at 90°)", fontsize=8, color="0.4")
ax1.set_xlim(0, 180)
ax1.set_ylim(0, 5.6)
ax1.set_xticks([0, 45, 90, 135, 180])
ax1.set_xlabel("scattering angle  θ / degree")
ax1.set_ylabel("Δλ = λ - λ0  / pm")
ax1.set_title("Δλ = λ_C (1 - cos θ), independent of the scatterer")

lam = np.linspace(0.068, 0.0785, 1000)
w = 0.00045
for k, deg in enumerate([0, 45, 90, 135]):
    t = np.radians(deg)
    lam1 = lam0 + lam_C * (1 - np.cos(t))
    a1 = 0.15 + 0.6 * (1 - np.cos(t)) / 2 if deg > 0 else 0.0
    a0 = 1.0 - 0.45 * (1 - np.cos(t)) / 2
    y = a0 * np.exp(-((lam - lam0) / w) ** 2) + a1 * np.exp(-((lam - lam1) / (1.3 * w)) ** 2)
    off = 1.3 * (3 - k)
    ax2.plot(lam, y + off, color=f"C{k}", lw=1.5)
    ax2.text(0.0782, off + 0.25, f"θ = {deg}°", fontsize=8, ha="right")
    if deg > 0:
        ax2.plot([lam1, lam1], [off, off + a1], color=f"C{k}", lw=0.8, ls=":")
ax2.axvline(lam0, color="0.5", lw=0.8, ls="--")
ax2.text(lam0 - 0.0002, 5.2, "λ0", fontsize=9, ha="right", color="0.4")
ax2.set_xlim(0.068, 0.0785)
ax2.set_ylim(-0.1, 5.4)
ax2.set_yticks([])
ax2.set_xlabel("wavelength  λ / nm")
ax2.set_ylabel("scattered intensity (schematic, offset)")
ax2.set_title("Graphite, Mo Kα: unshifted and shifted lines")

fig.tight_layout()
