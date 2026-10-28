"""Approximate composition of the human genome by class of transposable element (complete T2T assembly;
values as in 7.2.2), with the number of copies and the fraction of copies still able to move."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rows = [("LINEs (mostly L1)", 21, "dna", "about 500 000 copies; about 100 active L1"),
        ("SINEs (mostly Alu)", 13, "enzyme", "over 1 million Alu; mobilized by L1"),
        ("LTR retrotransposons, ERVs", 9, "receptor", "about 450 000 copies; none known active"),
        ("DNA transposons", 4, "protein", "about 300 000 copies; all inactive"),
        ("protein-coding sequence", 1.2, "positive", "for comparison")]
fig, ax = plt.subplots(figsize=(8.4, 3.0))
fig.subplots_adjust(left=0.28, right=0.62, bottom=0.2, top=0.95)
y = np.arange(len(rows))[::-1]
for yi, (name, pct, tok, note) in zip(y, rows):
    ax.barh(yi, pct, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, height=0.6)
    ax.text(pct + 0.4, yi, f"{pct:g} %", va="center", fontsize=bio.core.FONT["small"], color=P.ink())
    ax.text(27.5, yi, note, va="center", fontsize=bio.core.FONT["tiny"], color=P.muted(), clip_on=False)
ax.set_yticks(y, [r[0] for r in rows])
ax.set_xlim(0, 25)
charts.style_axes(ax, "percent of the genome", None)
