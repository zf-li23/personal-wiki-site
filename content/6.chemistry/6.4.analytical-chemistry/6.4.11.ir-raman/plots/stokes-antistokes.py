"""Left: simulated Raman spectrum of liquid CCl4 excited at 532 nm and 298 K, showing the
Stokes and anti-Stokes lines symmetric about the (filtered) Rayleigh line; relative Stokes
intensities are schematic, anti-Stokes lines are scaled by the Boltzmann and nu^4 factors.
Right: anti-Stokes/Stokes intensity ratio as a function of temperature for several Raman
shifts, I_aS/I_S = ((nu0 + dnu)/(nu0 - dnu))^4 exp(-h c dnu / (kB T))."""

import numpy as np
import matplotlib.pyplot as plt

h, c, kB = 6.62607015e-34, 2.99792458e10, 1.380649e-23
nu0 = 1e7 / 532.0  # cm-1
T0 = 298.15
modes = [(218, 0.55, 4), (314, 0.70, 4), (459, 1.0, 1.5), (762, 0.18, 3), (790, 0.20, 3)]


def ratio(d, T):
    return ((nu0 + d) / (nu0 - d))**4 * np.exp(-h * c * d / (kB * T))


x = np.linspace(-900, 900, 3601)
y = np.zeros_like(x)
for d, s, w in modes:
    lor = lambda x0: (w / 2)**2 / ((x - x0)**2 + (w / 2)**2)
    y += s * lor(d) + s * ratio(d, T0) * lor(-d)

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.0))
ax = axes[0]
ax.plot(x, y, color="k", lw=1.0)
ax.axvspan(-80, 80, color="C0", alpha=0.12, lw=0)
ax.text(0, 0.9, "Rayleigh line\n(removed by\nnotch filter)", ha="center", fontsize=8, color="C0")
ax.text(500, 0.75, "Stokes", ha="center", fontsize=9)
ax.text(-500, 0.4, "anti-Stokes", ha="center", fontsize=9)
for d, s, w in modes[:3]:
    ax.text(d, s + 0.04, f"{d}", ha="center", fontsize=7)
    ax.text(-d, s * ratio(d, T0) + 0.04, f"-{d}", ha="center", fontsize=7)
ax.set_xlim(-900, 900)
ax.set_ylim(0, 1.12)
ax.set_xlabel(r"Raman shift $\Delta\tilde\nu$ / cm$^{-1}$ (positive = Stokes)")
ax.set_ylabel("intensity (a.u.)")
ax.set_title("CCl$_4$, 532 nm, 298 K", fontsize=10)

ax = axes[1]
T = np.linspace(100, 1200, 400)
for d, col in zip([218, 459, 1000, 3000], ["C0", "C1", "C2", "C3"]):
    ax.semilogy(T, ratio(d, T), color=col, lw=1.6, label=f"{d} cm$^{{-1}}$")
ax.axvline(T0, color="0.6", lw=0.7, ls=":")
ax.set_xlim(100, 1200)
ax.set_ylim(1e-8, 2)
ax.set_xlabel(r"$T$ / K")
ax.set_ylabel(r"$I_{\mathrm{aS}}/I_{\mathrm{S}}$")
ax.legend(frameon=False, fontsize=8, title="Raman shift", title_fontsize=8, loc="lower right")
fig.tight_layout()
