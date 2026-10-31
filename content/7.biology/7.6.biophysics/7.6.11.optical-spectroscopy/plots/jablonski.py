# Jablonski diagram of a fluorophore with the rate constants that compete for the S1 state.
# Singlet manifold S0, S1, S2 (left), triplet T1 (right), vibrational sublevels as thin lines.
# Absorption (~1e-15 s), vibrational relaxation and internal conversion to the lowest S1 level (~1e-12 s,
# Kasha's rule), then fluorescence (k_r ~ 1e8 s^-1), internal conversion (k_ic), collisional quenching
# (k_q [Q]), energy transfer (k_T), intersystem crossing (k_isc) and phosphorescence (1e-3 to 1e2 s).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
ink, muted = P.ink(), P.muted()
fig, ax = plt.subplots(figsize=(10.5, 5.6))
ax.set_xlim(0, 13)
ax.set_ylim(-0.8, 10.2)
ax.axis("off")


def level(x0, x1, y, name, tok):
    ax.plot([x0, x1], [y, y], color=charts.line(tok), lw=2.0)
    for k in range(1, 4):
        ax.plot([x0, x1], [y + 0.32 * k, y + 0.32 * k], color=charts.line(tok), lw=0.6, alpha=0.7)
    ax.text(x0 - 0.15, y, name, ha="right", va="center", fontsize=10, color=ink)


level(1.0, 6.5, 0.0, "S0", "dna")
level(1.0, 6.5, 5.0, "S1", "rna")
level(1.0, 6.5, 8.2, "S2", "rna")
level(8.6, 12.4, 3.6, "T1", "protein")


def arr(x0, y0, x1, y1, col, wavy=False, lab=None, lx=0.0, ly=0.0, ha="left"):
    if wavy:
        t = np.linspace(0, 1, 200)
        xs = x0 + (x1 - x0) * t + 0.08 * np.sin(2 * np.pi * 9 * t) * (1 - abs(2 * t - 1) ** 6)
        ys = y0 + (y1 - y0) * t
        ax.plot(xs, ys, color=col, lw=1.1)
        ax.annotate("", xy=(x1, y1), xytext=(xs[-8], ys[-8]), arrowprops=dict(arrowstyle="-|>", color=col, lw=1.1))
    else:
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="-|>", color=col, lw=1.6))
    if lab:
        ax.text((x0 + x1) / 2 + lx, (y0 + y1) / 2 + ly, lab, fontsize=8.5, color=col, ha=ha, va="center")


blue, green, red, grey = charts.line("dna"), charts.line("positive"), charts.line("negative"), muted
arr(1.6, 0.0, 1.6, 5.9, blue, lab="absorption\n~10⁻¹⁵ s", lx=-0.12, ha="right")
arr(2.3, 0.0, 2.3, 8.9, blue)
arr(3.3, 8.2, 3.3, 5.0, grey, wavy=True, lab="IC, VR\n~10⁻¹² s", lx=0.15)
arr(4.3, 5.0, 4.3, 0.6, green, lab="fluorescence\n$k_\\mathrm{r}$ ~ 10⁸ s⁻¹", lx=0.12)
arr(5.6, 5.0, 5.6, 0.6, grey, wavy=True, lab="IC  $k_\\mathrm{ic}$", lx=0.15)
arr(6.5, 5.0, 8.6, 4.3, P.edge("protein"), wavy=True, lab="ISC  $k_\\mathrm{isc}$", ly=0.45, lx=-0.4)
arr(10.0, 3.6, 10.0, 0.6, P.edge("protein"), lab="phosphorescence\n10⁻³-10² s", lx=0.12)
arr(11.6, 3.6, 11.6, 0.6, grey, wavy=True)
ax.text(6.8, 6.6, "quenching  $k_\\mathrm{q}$[Q]\nenergy transfer  $k_\\mathrm{T}$", fontsize=8.5, color=red, ha="left")
ax.annotate("", xy=(8.4, 6.2), xytext=(6.5, 5.3), arrowprops=dict(arrowstyle="-|>", color=red, lw=1.1, ls=(0, (3, 2))))
ax.text(1.0, 9.85, "singlet states", fontsize=9, color=muted)
ax.text(8.6, 5.2, "triplet state", fontsize=9, color=muted)
ax.text(6.9, 9.3, r"$\tau = 1/(k_\mathrm{r} + k_\mathrm{ic} + k_\mathrm{isc} + k_\mathrm{q}[\mathrm{Q}] + k_\mathrm{T})$" + "\n" + r"$\Phi = k_\mathrm{r}\tau$", fontsize=9.5, color=ink, ha="left")
fig.tight_layout()
