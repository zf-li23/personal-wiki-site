"""Body size and the pace of life.

A: the "mouse-elephant curve": mass-specific resting metabolic rate of eleven mammals (the standard comparative table
also used in 7.14.30: resting O2 consumption converted with 20.1 J per mL O2) against body mass, with the Kleiber line
B/M = 3.39 M^(-1/4) W/kg.
B: schematic of the size scaling of maximal population growth rate r_max: three parallel lines of slope -1/4
(Fenchel 1974 found slopes near -0.27 for unicells, ectothermic metazoans and endotherms, with intercepts in that
increasing order; the offsets drawn here, 1 : 8 : 40, are illustrative);
the vertical axis is relative (log scale, arbitrary units).
C: schematic of the energy equivalence rule: population density N proportional to M^(-3/4) (Damuth 1981) times
individual metabolic rate B proportional to M^(3/4) gives a population energy use N B independent of M.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
mass = np.array([0.0048, 0.009, 0.025, 0.096, 0.29, 2.5, 11.7, 42.7, 70, 650, 3833])
vo2 = np.array([0.0355, 0.0225, 0.041, 0.09, 0.25, 1.7, 3.87, 9.59, 14.76, 71.1, 268])  # L O2 per hour
names = ["shrew", "harvest mouse", "mouse", "ground squirrel", "rat", "cat", "dog", "sheep", "human", "horse",
         "elephant"]
spec = vo2 * 20.1 / 3.6 / mass  # W per kg

fig, axes = plt.subplots(1, 3, figsize=(14.0, 4.3))
ax = axes[0]
mm = np.logspace(-2.5, 4, 50)
ax.plot(mm, 3.39 * mm ** -0.25, color=P.edge("blood"), lw=1.8, label="Kleiber: $B/M = 3.39\\,M^{-1/4}$")
ax.scatter(mass, spec, s=30, color=P.fill("dna"), edgecolor=P.edge("dna"), zorder=5)
for m_, b_, n_ in zip(mass, spec, names):
    if n_ in ("shrew", "harvest mouse", "mouse", "rat", "dog", "human", "horse", "elephant"):
        ax.annotate(n_, (m_, b_), xytext=(5, 3), textcoords="offset points", fontsize=7.5, color=P.muted())
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("body mass $M$ / kg")
ax.set_ylabel("mass-specific metabolic rate $B/M$ / (W kg$^{-1}$)")
ax.legend(frameon=False, fontsize=8, loc="lower left")
ax.set_title("A  The mouse-elephant curve", loc="left", fontsize=10)

bx = axes[1]
for lo, hi, c, tok, lab in ((1e-15, 1e-8, 1.0, "dna", "unicells"), (1e-9, 1e2, 8.0, "plant", "ectotherms"),
                            (1e-3, 1e4, 40.0, "blood", "endotherms")):
    m = np.logspace(np.log10(lo), np.log10(hi), 50)
    bx.plot(m, c * m ** -0.25, color=P.edge(tok), lw=2.2, label=lab)
bx.set_xscale("log")
bx.set_yscale("log")
bx.set_yticklabels([])
bx.set_xlabel("body mass $M$ / kg")
bx.set_ylabel("$r_{\\max}$ (relative, log scale)")
bx.legend(frameon=False, fontsize=8, loc="lower left")
bx.text(1e-6, 3e2, "slope $-1/4$", fontsize=8.5, color=P.muted())
bx.set_title("B  $r_{\\max} \\propto M^{-1/4}$ (schematic)", loc="left", fontsize=10)

cx = axes[2]
m = np.logspace(-3, 4, 50)
cx.plot(m, m ** 0.75, color=P.edge("rna"), lw=2.0, label="individual metabolism $B \\propto M^{3/4}$")
cx.plot(m, m ** -0.75, color=P.edge("dna"), lw=2.0, label="population density $N \\propto M^{-3/4}$")
cx.plot(m, np.ones_like(m), color=P.edge("plant"), lw=2.4, ls="--", label="population energy use $NB \\propto M^0$")
cx.set_xscale("log")
cx.set_yscale("log")
cx.set_yticklabels([])
cx.set_xlabel("body mass $M$ (relative)")
cx.set_ylabel("relative value (log scale)")
cx.legend(frameon=False, fontsize=8, loc="upper center")
cx.set_ylim(1e-4, 1e5)
cx.set_title("C  Energy equivalence (schematic)", loc="left", fontsize=10)
for a in axes:
    for s in ("top", "right"):
        a.spines[s].set_visible(False)
fig.tight_layout()
