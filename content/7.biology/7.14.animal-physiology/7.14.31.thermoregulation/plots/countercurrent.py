"""Countercurrent versus concurrent heat exchange between arterial and venous blood (balanced flows).

Two streams with equal heat-capacity flow rates exchange heat through a wall; NTU = U A / (m c) is the exchanger
size in units of the flow. Effectiveness (fraction of the maximal possible heat transfer):
countercurrent eps = NTU/(1 + NTU); concurrent eps = (1 - exp(-2 NTU))/2, never above 1/2.
A: effectiveness against NTU, and the resulting elevation of a heat-producing tissue above water temperature,
dT = Q/(m c (1 - eps)), relative to the elevation without an exchanger (= 1/(1 - eps)).
B: temperature profiles (concurrent drawn with both streams entering at the left, for comparison) along a tuna-like rete with NTU = 5: cold arterial blood from the gills (15 C) and warm
venous blood leaving the red muscle (30 C).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
ntu = np.linspace(0, 10, 300)
cc = ntu / (1 + ntu)
co = (1 - np.exp(-2 * ntu)) / 2

fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.5, 4.5))
ax.plot(ntu, cc, color=P.edge("dna"), lw=2.2, label="countercurrent")
ax.plot(ntu, co, color=P.edge("rna"), lw=2, ls="--", label="concurrent")
ax.set_xlabel("Exchanger size NTU = UA/($\\dot m c$)")
ax.set_ylabel("Effectiveness $\\varepsilon$")
ax.set_ylim(0, 1)
ax2 = ax.twinx()
ax2.plot(ntu, 1 / (1 - cc), color=P.edge("dna"), lw=1.2, ls=":", label="tissue warming factor, countercurrent")
ax2.plot(ntu, 1 / (1 - co), color=P.edge("rna"), lw=1.2, ls=":", label="tissue warming factor, concurrent")
ax2.set_ylim(0, 12)
ax2.set_ylabel("Tissue warming relative to no exchanger (dotted)")
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, frameon=False, fontsize=8, loc="center right", bbox_to_anchor=(1.0, 0.36))
ax.set_title("A  Only countercurrent flow approaches complete exchange", loc="left", fontsize=10)

x = np.linspace(0, 1, 200)
N, Tc, Th = 5.0, 15.0, 30.0
# countercurrent, balanced: linear profiles with a constant gap
gap = (Th - Tc) / (1 + N)
art = Tc + (Th - Tc - gap) * x  # arterial, flowing towards the muscle (x = 1)
ven = art + gap  # venous, flowing back to the gills
bx.plot(x, art, color=P.edge("blood"), lw=2.2, label="countercurrent: arterial (to muscle)")
bx.plot(x, ven, color=P.edge("dna"), lw=2.2, label="countercurrent: venous (to gills)")
# concurrent: both streams enter at x = 0
mid = (Tc + Th) / 2
bx.plot(x, mid - (mid - Tc) * np.exp(-2 * N * x), color=P.edge("blood"), lw=1.3, ls="--",
        label="concurrent: cold stream")
bx.plot(x, mid + (Th - mid) * np.exp(-2 * N * x), color=P.edge("dna"), lw=1.3, ls="--",
        label="concurrent: warm stream")
bx.text(0.0, 14.3, "gills (water 15 $^\\circ$C)", fontsize=8, color=P.muted())
bx.text(1.0, 14.3, "red muscle", fontsize=8, color=P.muted(), ha="right")
bx.set_ylim(13.5, 31)
bx.set_xlabel("Position along the rete")
bx.set_ylabel("Blood temperature / $^\\circ$C")
bx.legend(frameon=False, fontsize=7.5, loc="lower right", bbox_to_anchor=(1.0, 0.06))
bx.set_title("B  Profiles in a rete with NTU = 5", loc="left", fontsize=10)
fig.tight_layout()
