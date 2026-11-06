# Biphasic (dual-isotherm) uptake of K+ by roots, modelled as the sum of a high-affinity system
# (Mechanism I of Epstein, HATS: Km = 20 uM, Vmax = 10 umol g-1 h-1) and a low-affinity system (Mechanism II,
# LATS: Km = 10 mM, Vmax = 15 umol g-1 h-1), parameters of the order measured for barley roots (illustrative).
# A: the low concentration range, where HATS dominates and saturates near 0.2 mM. B: the full range on a
# different scale: LATS adds a second saturating phase in the millimolar range. C: Eadie-Hofstee plot
# (v against v/[S], log abscissa); one Michaelis-Menten system is a straight line of slope -Km on linear axes; the sum of two gives a
# curve with two nearly linear limbs whose slopes approximate the two Km values.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
K1, V1 = 0.020, 10.0
K2, V2 = 10.0, 15.0


def hats(s):
    return V1 * s / (K1 + s)


def lats(s):
    return V2 * s / (K2 + s)


fig, axs = plt.subplots(1, 3, figsize=(14.0, 4.2), gridspec_kw=dict(wspace=0.34))
ax = axs[0]
s = np.linspace(0, 0.2, 400)
ax.plot(s * 1000, hats(s) + lats(s), color=charts.line("k"), lw=2.2, label="total")
ax.plot(s * 1000, hats(s), color=charts.line("dna"), lw=1.4, ls="--", label="HATS ($K_{\\mathrm{m}}$ = 20 µM)")
ax.plot(s * 1000, lats(s), color=charts.line("rna"), lw=1.4, ls="--", label="LATS ($K_{\\mathrm{m}}$ = 10 mM)")
ax.axhline(V1 / 2, color=P.muted(), lw=0.6, ls=":")
ax.plot([K1 * 1000] * 2, [0, V1 / 2], color=P.muted(), lw=0.6, ls=":")
ax.legend(fontsize=6.8, frameon=False, loc="lower right")
ax.set_xlim(0, 200)
ax.set_ylim(0, 13)
charts.style_axes(ax, "external [K$^+$] / µM", "K$^+$ uptake / (µmol g$^{-1}$ h$^{-1}$)")
charts.title(ax, "A   Mechanism I (µM range)")

ax = axs[1]
s = np.linspace(0, 50, 600)
ax.plot(s, hats(s) + lats(s), color=charts.line("k"), lw=2.2)
ax.plot(s, hats(s), color=charts.line("dna"), lw=1.4, ls="--")
ax.plot(s, lats(s), color=charts.line("rna"), lw=1.4, ls="--")
ax.axhline(V1, color=P.muted(), lw=0.6, ls=":")
ax.text(49, V1 + 0.4, "plateau of Mechanism I", ha="right", fontsize=6.8, color=P.muted())
ax.set_xlim(0, 50)
ax.set_ylim(0, 25)
charts.style_axes(ax, "external [K$^+$] / mM", "K$^+$ uptake / (µmol g$^{-1}$ h$^{-1}$)")
charts.title(ax, "B   Mechanism II (mM range)")

ax = axs[2]
s = np.geomspace(1e-4, 200, 800)
v = hats(s) + lats(s)
ax.plot(v / s, v, color=charts.line("k"), lw=2.2)
for f, K, tok, lab in ((hats, K1, "dna", "slope ≈ $-K_{\\mathrm{m1}}$"), (lats, K2, "rna", "slope ≈ $-K_{\\mathrm{m2}}$")):
    vv = f(s)
    ax.plot(vv / s, vv, color=charts.line(tok), lw=1.2, ls="--")
ax.text(3, 3.0, "high-affinity limb", fontsize=7, color=charts.line("dna"))
ax.text(12, 21, "low-affinity limb", fontsize=7, color=charts.line("rna"))
ax.set_xscale("log")
ax.set_xlim(0.1, 1000)
ax.set_ylim(0, 26)
charts.style_axes(ax, "$v/[\\mathrm{S}]$ / (µmol g$^{-1}$ h$^{-1}$ mM$^{-1}$)", "$v$ / (µmol g$^{-1}$ h$^{-1}$)")
charts.title(ax, "C   Eadie–Hofstee plot")
