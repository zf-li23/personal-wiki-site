"""Water budget of a desert rodent.

A: water budget of Merriam's kangaroo rat (Dipodomys merriami) eating 100 g of barley at 25 C and moderate humidity
(Schmidt-Nielsen 1964): gains 54.0 mL oxidation water + 6.0 mL free water; losses 43.9 mL evaporation,
13.5 mL urine, 2.6 mL feces.
B: a minimal respiratory water model per liter of O2 consumed. Air breathed per liter O2: V = 25 L (about 4 %
absolute O2 extraction). Exhaled air is saturated at temperature T_ex; inhaled air at T_a = 25 C has relative
humidity RH. Respiratory loss = V * (rho_sat(T_ex) - RH * rho_sat(T_a)). Saturation vapor density from the
Tetens formula. Oxidation water per liter O2: starch 0.67 g, fat 0.53 g.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P


def rho_sat(t):
    """Saturation water-vapor density in g per liter at t degrees C (Tetens)."""
    e = 0.61078 * np.exp(17.27 * t / (t + 237.3)) * 1000.0  # Pa
    return e * 18.015 / (8.314 * (t + 273.15)) / 1000.0  # g per L


fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.0, 4.6), gridspec_kw={"width_ratios": [1, 1.35]})

gains = [("oxidation water", 54.0, "metabolite"), ("free water in food", 6.0, "dna")]
losses = [("evaporation", 43.9, "rna"), ("urine", 13.5, "plant"), ("feces", 2.6, "neutral")]
for xpos, items in ((0, gains), (1, losses)):
    bottom = 0.0
    for name, v, tok in items:
        ax.bar(xpos, v, bottom=bottom, width=0.55, color=P.fill(tok), edgecolor=P.edge(tok), lw=1.0)
        side = -1 if xpos == 0 else 1
        ax.text(xpos + side * 0.32, bottom + v / 2, f"{name}  {v:.1f}", va="center", fontsize=8, color=P.ink(),
                ha="right" if side < 0 else "left")
        bottom += v
ax.set_xticks([0, 1])
ax.set_xticklabels(["gains", "losses"])
ax.set_xlim(-1.5, 2.1)
ax.set_ylim(0, 66)
ax.set_ylabel("water per 100 g barley eaten / mL")
ax.set_title("A  Kangaroo rat: a budget without drinking", loc="left", fontsize=10)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)

rh = np.linspace(0, 1, 200)
V, Ta = 25.0, 25.0
for tex, tok, lab in ((37.0, "negative", "exhaled at 37 $^\\circ$C (no nasal cooling)"),
                      (27.0, "positive", "exhaled at 27 $^\\circ$C (nasal countercurrent cooling)")):
    loss = V * (rho_sat(tex) - rh * rho_sat(Ta))
    bx.plot(rh * 100, loss, color=P.edge(tok), lw=2.0, label=lab)
for val, ls, lab in ((0.67, "--", "oxidation water, starch"), (0.53, ":", "oxidation water, fat")):
    bx.axhline(val, color=P.edge("metabolite"), lw=1.5, ls=ls)
    bx.text(101, val, lab, va="center", fontsize=8, color=P.edge("metabolite"))
bx.set_xlim(0, 100)
bx.set_ylim(0, 1.2)
bx.set_xlabel("relative humidity of inhaled air (25 $^\\circ$C) / %")
bx.set_ylabel("water per liter O$_2$ consumed / g")
bx.legend(frameon=False, fontsize=8, loc="lower left")
bx.set_title("B  Respiratory water loss versus oxidation water", loc="left", fontsize=10)
for s in ("top", "right"):
    bx.spines[s].set_visible(False)
fig.tight_layout()
