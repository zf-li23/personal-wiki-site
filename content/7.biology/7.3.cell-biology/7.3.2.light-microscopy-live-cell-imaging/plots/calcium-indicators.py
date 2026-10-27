# Choosing a Ca2+ indicator: the fraction of indicator bound, f = [Ca]^n / (K_d^n + [Ca]^n), against free
# [Ca2+] for representative probes (approximate in vitro values): fura-2 (K_d 0.22 uM, n = 1), Fluo-4
# (0.35 uM, n = 1), GCaMP6s (0.14 uM, n = 2.9), GCaMP6f (0.38 uM, n = 2.3), Mag-Fluo-4 (22 uM, n = 1) and the
# ER-targeted low-affinity sensor G-CEPIA1er (670 uM, n = 1.95). Shaded: resting cytosol (~0.1 uM), cytosolic
# transients (0.5-2 uM) and the ER lumen (100-800 uM). An indicator reports changes well only where its
# curve is steep, roughly 0.1 K_d to 10 K_d; cooperativity (n > 1) steepens the response but makes it
# nonlinear.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
ca = np.logspace(-9, -2, 400)
probes = [
    ("fura-2", 0.22e-6, 1.0, "dna", "-"),
    ("Fluo-4", 0.35e-6, 1.0, "positive", "-"),
    ("GCaMP6s", 0.14e-6, 2.9, "negative", "--"),
    ("GCaMP6f", 0.38e-6, 2.3, "rna", "--"),
    ("Mag-Fluo-4", 22e-6, 1.0, "protein", "-"),
    ("G-CEPIA1er", 670e-6, 1.95, "enzyme", "--"),
]
fig, ax = plt.subplots(figsize=(7.6, 4.0))
for lo, hi, txt in ((0.05e-6, 0.15e-6, "resting\ncytosol"), (0.5e-6, 2e-6, "cytosolic\ntransients"), (1e-4, 8e-4, "ER\nlumen")):
    ax.axvspan(lo, hi, color=P.fill("highlight"), alpha=0.35, lw=0)
    ax.text(np.sqrt(lo * hi), 1.04, txt, fontsize=7, color=P.ink(), ha="center", va="bottom")
for name, kd, n, tok, ls in probes:
    f = ca**n / (kd**n + ca**n)
    ax.semilogx(ca, f, color=charts.line(tok), lw=1.7, ls=ls, label=f"{name} (K_d {kd * 1e6:g} µM, n = {n:g})")
ax.set_xlim(1e-9, 1e-2)
ax.set_ylim(0, 1.18)
ax.set_yticks([0, 0.5, 1])
ax.set_xticks([1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2])
ax.set_xticklabels(["1 nM", "10 nM", "100 nM", "1 µM", "10 µM", "100 µM", "1 mM", "10 mM"])
ax.minorticks_off()
ax.legend(fontsize=6.5, frameon=False, loc="center left", bbox_to_anchor=(1.0, 0.5))
charts.style_axes(ax, "free [Ca²⁺]", "fraction of indicator bound")
fig.tight_layout()
