"""Kin selection and alarm calling: call if r N b > c.

A: minimum number of listeners N* = c / (r b) against c/b for r = 0.5, 0.25, 0.125.
B: model inclusive-fitness gain r N b - c for a philopatric female (N = 3 close kin, r = 0.5, plus 4 distant
kin, r = 0.125) and a dispersed male (r = 0) with b = 0.04 and c = 0.05 (illustrative).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.8), gridspec_kw={"width_ratios": [1.3, 1]})
x = np.linspace(0.05, 2, 200)
for r, tok in ((0.5, "dna"), (0.25, "positive"), (0.125, "rna")):
    a.plot(x, x / r, color=P.edge(tok), lw=1.8, label=f"r = {r:g}")
a.set_xlabel("Cost to caller / benefit to each listener, c/b")
a.set_ylabel("Listeners needed, N* = c/(r b)")
a.set_ylim(0, 16)
a.legend(frameon=False, fontsize=8)
a.text(0.3, 13, "calling favored above the line", fontsize=8, color=P.muted())
a.set_title("A", loc="left", fontweight="bold")
bb, c = 0.04, 0.05
gain_f = 3 * 0.5 * bb + 4 * 0.125 * bb - c
gain_m = 0 - c
b.bar([0, 1], [gain_f, gain_m], color=[P.fill("dna"), P.fill("rna")], edgecolor=[P.edge("dna"), P.edge("rna")])
b.axhline(0, color=P.ink(), lw=0.8)
b.set_xticks([0, 1]); b.set_xticklabels(["philopatric female\n(kin nearby)", "dispersed male\n(no kin)"], fontsize=8)
b.set_ylabel("Inclusive fitness gain of calling")
b.text(0, gain_f + 0.002, "call", ha="center", fontsize=8)
b.text(1, gain_m - 0.006, "stay silent", ha="center", fontsize=8)
b.set_ylim(-0.065, 0.04)
b.set_title("B", loc="left", fontweight="bold")
for ax in (a, b):
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
fig.tight_layout()
