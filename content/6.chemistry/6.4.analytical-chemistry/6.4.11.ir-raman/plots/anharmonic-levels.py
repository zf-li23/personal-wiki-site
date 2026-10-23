"""Harmonic and Morse potentials of H-35Cl with their vibrational levels.
Spectroscopic constants: we = 2990.9 cm-1, wexe = 52.8 cm-1, re = 127.5 pm; the Morse well
depth De = we^2/(4 wexe) reproduces these constants exactly (the true dissociation energy is
smaller). Arrows: fundamental (0 -> 1) and first overtone (0 -> 2)."""

import numpy as np
import matplotlib.pyplot as plt

we, wexe, re = 2990.9, 52.8, 127.5  # cm-1, cm-1, pm
De = we**2 / (4 * wexe)  # cm-1
mu = 1.007825 * 34.968853 / (1.007825 + 34.968853) * 1.66053906660e-27  # kg
c = 2.99792458e10  # cm s-1
omega = 2 * np.pi * c * we  # rad s-1
a = omega * np.sqrt(mu / (2 * De * 1.98644586e-23)) * 1e-12  # pm-1 (De in J)

r = np.linspace(80, 320, 800)
morse = De * (1 - np.exp(-a * (r - re)))**2
harm = De * a**2 * (r - re)**2

fig, ax = plt.subplots(figsize=(7.6, 5.0))
ax.plot(r, harm / 1e3, color="C0", lw=1.5, ls="--", label="harmonic potential")
ax.plot(r, morse / 1e3, color="k", lw=1.8, label="Morse potential")

for v in range(0, 12):
    Eh = we * (v + 0.5)
    Em = we * (v + 0.5) - wexe * (v + 0.5)**2
    # turning points
    xh = np.sqrt(Eh / (De * a**2))
    ax.plot([re - xh, re + xh], [Eh / 1e3] * 2, color="C0", lw=0.8, alpha=0.7)
    rl =re + np.log(1 / (1 + np.sqrt(Em / De))) / a
    rr = re + np.log(1 / (1 - np.sqrt(Em / De))) / a
    ax.plot([rl, rr], [Em / 1e3] * 2, color="k", lw=1.0)
    if v < 3:
        ax.text(rr + 3, Em / 1e3, f"v = {v}", va="center", fontsize=8)

E = lambda v: we * (v + 0.5) - wexe * (v + 0.5)**2
for v2, xpos, col in [(1, 118, "C3"), (2, 136, "C2")]:
    ax.annotate("", xy=(xpos, E(v2) / 1e3), xytext=(xpos, E(0) / 1e3),
                arrowprops=dict(arrowstyle="-|>", color=col, lw=1.6))
ax.text(103, 2.6, f"fundamental\n{E(1) - E(0):.0f} cm$^{{-1}}$", fontsize=8, color="C3",
        ha="right")
ax.text(205, 4.0, f"first overtone\n{E(2) - E(0):.0f} cm$^{{-1}}$\n"
        f"(2 x {E(1) - E(0):.0f} = {2 * (E(1) - E(0)):.0f})", fontsize=8, color="C2")
ax.axhline(De / 1e3, color="0.5", lw=0.8, ls=":")
ax.text(300, De / 1e3 - 1.6, r"$D_{\mathrm{e}}$", fontsize=9, color="0.4")
ax.set_xlim(80, 320)
ax.set_ylim(0, 46)
ax.set_xlabel(r"internuclear distance $r$ / pm")
ax.set_ylabel(r"energy / $10^3$ cm$^{-1}$")
ax.legend(frameon=False, fontsize=9, loc="center right")
fig.tight_layout()
