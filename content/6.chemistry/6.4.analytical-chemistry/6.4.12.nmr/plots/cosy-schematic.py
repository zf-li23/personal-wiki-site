"""Schematic 1H-1H COSY spectrum of methyl butanoate, CH3CH2CH2C(=O)OCH3
(delta 0.95 t, 1.65 sextet, 2.30 t, 3.67 s): diagonal peaks reproduce the 1D spectrum,
cross peaks connect protons on adjacent carbons; the OCH3 singlet has no cross peak."""

import numpy as np
import matplotlib.pyplot as plt

shifts = {"OCH$_3$": 3.67, "CH$_2$C=O": 2.30, "CH$_2$": 1.65, "CH$_3$": 0.95}
pairs = [("CH$_2$C=O", "CH$_2$"), ("CH$_2$", "CH$_3$")]
mult = {"OCH$_3$": [1], "CH$_2$C=O": [1, 2, 1], "CH$_2$": [1, 5, 10, 10, 5, 1],
        "CH$_3$": [1, 2, 1]}
nH = {"OCH$_3$": 3, "CH$_2$C=O": 2, "CH$_2$": 2, "CH$_3$": 3}

fig = plt.figure(figsize=(6.6, 6.6))
gs = fig.add_gridspec(2, 1, height_ratios=[1, 4.2], hspace=0.04)
ax1 = fig.add_subplot(gs[0])
ax = fig.add_subplot(gs[1], sharex=ax1)

x = np.linspace(0.5, 4.2, 6000)
y = np.zeros_like(x)
J, w, mhz = 7.4 / 400, 0.004, 400  # J in ppm at 400 MHz
for k, d in shifts.items():
    m = np.array(mult[k], float)
    m = m / m.sum() * nH[k]
    for i, a in enumerate(m):
        c = d + (i - (len(m) - 1) / 2) * J
        y += a * (w / 2)**2 / ((x - c)**2 + (w / 2)**2)
ax1.plot(x, y, color="k", lw=0.8)
ax1.set_yticks([])
ax1.tick_params(labelbottom=False)

for k, d in shifts.items():
    ax.plot(d, d, "o", ms=11, color="C0", alpha=0.7)
    ax.text(d + 0.08, d - 0.12, k, fontsize=8, ha="right", va="top")
for a, b in pairs:
    for p, q in [(shifts[a], shifts[b]), (shifts[b], shifts[a])]:
        ax.plot(p, q, "s", ms=10, color="C3", alpha=0.8)
    ax.plot([shifts[a], shifts[a]], [shifts[a], shifts[b]], color="C3", lw=0.6, ls=":")
    ax.plot([shifts[a], shifts[b]], [shifts[b], shifts[b]], color="C3", lw=0.6, ls=":")
ax.plot([4.2, 0.5], [4.2, 0.5], color="0.6", lw=0.6, ls="--")
ax.set_xlim(4.2, 0.5)
ax.set_ylim(4.2, 0.5)
ax.set_xlabel(r"$\delta_2$ / ppm (F2)")
ax.set_ylabel(r"$\delta_1$ / ppm (F1)")
ax.text(3.9, 1.2, "circles: diagonal peaks\nsquares: cross peaks", fontsize=8)
