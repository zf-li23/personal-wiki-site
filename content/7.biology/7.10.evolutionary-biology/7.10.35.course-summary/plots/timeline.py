"""The history of life on a logarithmic time axis (years before present), with the dates used in the
chapters on the origin of life, eukaryotes, the history of life, diversity and human evolution. Rows:
the Earth and prokaryotes (blue), eukaryotes and animals (brown), plants (green), humans (orange);
red triangles: the five mass extinctions. The date of LUCA is an estimate from molecular clocks and is
marked with a question mark."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = plt.subplots(figsize=(12.0, 4.6))
fig.subplots_adjust(left=0.03, right=0.98, bottom=0.14, top=0.97)

EVENTS = [  # (years ago, label, row, token)
    (4.54e9, "Earth\nforms", 1, "dna"),
    (4.2e9, "LUCA?", 2.4, "dna"),
    (3.4e9, "life secure:\nstromatolites,\nmicrofossils", 4, "dna"),
    (2.4e9, "Great Oxidation\nEvent", 2.4, "dna"),
    (1.65e9, "oldest eukaryote\nfossils", 1, "animal"),
    (1.05e9, "$\\it{Bangiomorpha}$\n(multicellular\nred alga)", 4, "animal"),
    (7.2e8, "Snowball\nEarth", 2, "dna"),
    (5.75e8, "Ediacaran\nbiota", 1, "animal"),
    (5.39e8, "Cambrian\nexplosion", 3, "animal"),
    (4.3e8, "vascular plants\non land", 4.6, "plant"),
    (3.7e8, "tetrapods", 2, "animal"),
    (1.3e8, "angiosperms", 3.4, "plant"),
    (7e6, "human–chimpanzee\nsplit", 1, "rna"),
    (2.8e6, "$\\it{Homo}$", 3, "rna"),
    (3e5, "$\\it{H.\\ sapiens}$", 1.6, "rna"),
    (6e4, "out of\nAfrica", 3.4, "rna"),
]
EXT = [(445e6, "end-Ord."), (372e6, "Late Dev."), (252e6, "end-Perm."), (201.4e6, "end-Tri."), (66e6, "K/Pg")]

lo, hi = 3e4, 6e9
ax.set_xscale("log")
ax.set_xlim(hi, lo)
ax.set_ylim(-2.7, 6.2)
ax.axhline(0, color=P.ink(), lw=1.2)
for yr, lab, row, tok in EVENTS:
    ax.plot([yr, yr], [0, row - 0.15], color=P.muted(), lw=0.6)
    ax.scatter([yr], [0], s=22, color=charts.line(tok), zorder=4)
    ax.text(yr, row, lab, ha="center", va="bottom", fontsize=FT["tiny"], color=P.ink())
for k, (yr, lab) in enumerate(EXT):
    y = -0.55 - 0.55 * (k % 2)
    ax.plot([yr], [-0.25], marker="v", ms=7, color=P.edge("negative"), zorder=4)
    ax.text(yr, y, lab, ha="center", va="top", fontsize=FT["tiny"], color=P.edge("negative"))
ax.text(4.5e7, -0.55, "mass extinctions", ha="left", va="top",
        fontsize=FT["tiny"], color=P.edge("negative"))
for v, t in ((1e9, "1 Ga"), (1e8, "100 Mya"), (1e7, "10 Mya"), (1e6, "1 Mya"), (1e5, "100 ka")):
    ax.plot([v, v], [-0.08, 0.08], color=P.ink(), lw=0.8)
    ax.text(v, -1.7, t, ha="center", va="top", fontsize=FT["tiny"], color=P.muted())
ax.axis("off")
ax.text(np.sqrt(hi * lo), -2.7, "years before present (logarithmic scale)", ha="center", va="bottom",
        fontsize=FT["small"], color=P.muted())
