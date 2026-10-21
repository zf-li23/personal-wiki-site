"""Blackbody spectral exitance: Planck curves at several temperatures, and Planck versus the Rayleigh-Jeans and Wien formulas."""

import numpy as np
import matplotlib.pyplot as plt

h = 6.62607015e-34
kB = 1.380649e-23
c = 2.99792458e8


def planck(nu, T):
    return 2 * np.pi * h * nu ** 3 / c ** 2 / np.expm1(h * nu / (kB * T))


def rayleigh_jeans(nu, T):
    return 2 * np.pi * nu ** 2 * kB * T / c ** 2


def wien(nu, T):
    return 2 * np.pi * h * nu ** 3 / c ** 2 * np.exp(-h * nu / (kB * T))


nu = np.linspace(1e12, 1.6e15, 1500)
x_peak = 2.821439  # root of x = 3 (1 - exp(-x))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.0))

ax1.axvspan(3.95, 7.5, color="0.5", alpha=0.12, lw=0)
ax1.text(5.7, 13.2, "visible", ha="center", fontsize=8, color="0.4")
for i, T in enumerate([3000, 4500, 6000]):
    ax1.plot(nu / 1e14, planck(nu, T) / 1e-8, color=f"C{i}", lw=1.8, label=f"T = {T} K")
    nm = x_peak * kB * T / h
    ax1.plot([nm / 1e14], [planck(nm, T) / 1e-8], "o", color=f"C{i}", ms=4)
nm = x_peak * kB * np.array([3000, 4500, 6000]) / h
ax1.plot(nm / 1e14, planck(nm, np.array([3000, 4500, 6000])) / 1e-8, color="0.5", ls=":", lw=1.0)
ax1.text(4.6, 6.0, "peak: ν_m = C_ν T", fontsize=8, color="0.4")
ax1.set_xlim(0, 16)
ax1.set_ylim(0, 14)
ax1.set_xlabel("frequency  ν / (10^14 Hz)")
ax1.set_ylabel("M_ν / (10^-8 W m^-2 Hz^-1)")
ax1.set_title("Planck's law at three temperatures")
ax1.legend(loc="upper right", fontsize=9, frameon=False)

T = 1600
nu2 = np.linspace(1e12, 6e14, 1500)
ax2.plot(nu2 / 1e14, planck(nu2, T) / 1e-9, color="C0", lw=2.0, label="Planck")
ax2.plot(nu2 / 1e14, rayleigh_jeans(nu2, T) / 1e-9, color="C3", lw=1.5, ls="--", label="Rayleigh-Jeans")
ax2.plot(nu2 / 1e14, wien(nu2, T) / 1e-9, color="C2", lw=1.5, ls="-.", label="Wien")
ax2.set_xlim(0, 6)
ax2.set_ylim(0, 3.0)
ax2.set_xlabel("frequency  ν / (10^14 Hz)")
ax2.set_ylabel("M_ν / (10^-9 W m^-2 Hz^-1)")
ax2.set_title(f"T = {T} K: classical formulas")
ax2.annotate("ultraviolet catastrophe", xy=(0.47, 2.6), xytext=(1.3, 2.6), fontsize=8,
             arrowprops=dict(arrowstyle="->", color="0.5"), va="center")
ax2.legend(loc="center right", fontsize=9, frameon=False)

fig.tight_layout()
