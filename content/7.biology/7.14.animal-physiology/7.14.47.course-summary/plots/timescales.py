"""Time scales of physiological control loops, from milliseconds to weeks.

Each bar spans the approximate range of the response time (latency to full correction) of one
mechanism, as given in the chapters of this course; values are order-of-magnitude ranges.
Colours mark the carrier of the signal: neural, chemical (buffers and local), hormonal, renal
and cellular (production and growth).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
s, mn, h, d, wk = 1.0, 60.0, 3600.0, 86400.0, 604800.0
rows = [
    ("Stretch reflex", 0.02, 0.05, "neural"),
    ("Cerebellar correction of a reach", 0.05, 0.3, "neural"),
    ("Baroreceptor reflex", 1 * s, 30 * s, "neural"),
    ("Chemical buffering of H+", 0.01, 1 * s, "chemical"),
    ("Respiratory compensation of pH", 1 * mn, 30 * mn, "neural"),
    ("Local metabolic vasodilation", 5 * s, 2 * mn, "chemical"),
    ("Adrenaline (sympathoadrenal)", 5 * s, 3 * mn, "hormone"),
    ("Thermoregulation (shivering, sweating)", 1 * mn, 1 * h, "neural"),
    ("Insulin and glucagon on blood glucose", 10 * mn, 3 * h, "hormone"),
    ("ADH and water balance", 15 * mn, 6 * h, "hormone"),
    ("PTH and plasma Ca2+", 30 * mn, 1 * d, "hormone"),
    ("Cortisol (HPA axis)", 30 * mn, 1 * d, "hormone"),
    ("Renal acid excretion", 12 * h, 5 * d, "renal"),
    ("Pressure natriuresis (long-term pressure)", 1 * d, 2 * wk, "renal"),
    ("Thyroid hormone (HPT axis)", 3 * d, 6 * wk, "hormone"),
    ("Erythropoietin and red-cell mass", 5 * d, 8 * wk, "cell"),
]
cols = {"neural": P.edge("dna"), "chemical": P.edge("enzyme"), "hormone": P.edge("rna"),
        "renal": P.edge("plant"), "cell": P.edge("protein")}
names = {"neural": "neural", "chemical": "chemical / local", "hormone": "hormonal",
         "renal": "renal", "cell": "cell production"}

fig, ax = plt.subplots(figsize=(10.5, 5.6))
for i, (lab, a, b, kind) in enumerate(rows[::-1]):
    ax.plot([a, b], [i, i], color=cols[kind], lw=7, solid_capstyle="round")
    ax.text(a / 1.6, i, lab, ha="right", va="center", fontsize=8, color=P.ink())
ax.set_xscale("log")
ax.set_xlim(1e-4, 1e7)
ax.set_ylim(-0.8, len(rows) - 0.2)
ax.set_yticks([])
ticks = [0.01, 1, mn, h, d, wk]
ax.set_xticks(ticks)
ax.set_xticklabels(["10 ms", "1 s", "1 min", "1 h", "1 day", "1 week"])
for t in ticks:
    ax.axvline(t, color=P.muted(), lw=0.5, alpha=0.5)
for k in names:
    ax.plot([], [], color=cols[k], lw=6, label=names[k])
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_xlabel("Response time (log scale)")
for sp in ("left", "top", "right"):
    ax.spines[sp].set_visible(False)
ax.set_title("Control loops nest by time scale: fast ones correct, slow ones set the level",
             loc="left", fontsize=10)
fig.tight_layout()
