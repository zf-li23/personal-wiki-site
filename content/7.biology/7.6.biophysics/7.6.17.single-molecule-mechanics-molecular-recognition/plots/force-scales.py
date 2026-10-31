# Forces in molecular biology and the instruments that measure them (logarithmic scale, piconewtons).
# Left: characteristic forces: thermal force kT/(1 nm) = 4.1 pN at 25 C, stall forces of motors, DNA
# overstretching (65 pN), unzipping (10-15 pN), RNA hairpin unfolding (~15 pN), titin Ig domains in AFM
# (150-300 pN at ~1 um/s), streptavidin-biotin (~50-300 pN, loading-rate dependent), a covalent bond (~2 nN).
# Right: working ranges of optical tweezers, magnetic tweezers, acoustic force spectroscopy, AFM and
# DNA-based tension probes.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = plt.subplots(figsize=(11.5, 5.2))
events = [
    ("thermal force kT/1 nm", 4.1, 4.1),
    ("kinesin stall", 6, 7),
    ("myosin II stroke", 2, 5),
    ("RNA polymerase stall", 15, 30),
    ("phage packaging motor", 50, 60),
    ("DNA entropic regime", 0.01, 5),
    ("DNA unzipping", 10, 15),
    ("RNA hairpin unfolding", 10, 20),
    ("DNA overstretching", 60, 70),
    ("titin Ig domain (AFM)", 150, 300),
    ("streptavidin–biotin", 50, 300),
    ("covalent bond rupture", 1500, 2500),
]
for i, (name, lo, hi) in enumerate(events):
    y = len(events) - i
    if hi > lo:
        ax.plot([lo, hi], [y, y], color=charts.line("dna"), lw=5, solid_capstyle="round")
    else:
        ax.plot([lo], [y], "o", color=charts.line("dna"), ms=7)
    ax.text(hi * 1.3, y, name, va="center", fontsize=8, color=P.ink())
tools = [("optical tweezers", 0.1, 100, "rna"), ("magnetic tweezers", 0.01, 100, "enzyme"),
         ("acoustic force spectroscopy", 0.1, 100, "neutral"), ("AFM", 10, 1e4, "negative"),
         ("DNA tension probes", 4, 60, "positive")]
for j, (name, lo, hi, tok) in enumerate(tools):
    y = -1 - j * 0.8
    ax.plot([lo, hi], [y, y], color=charts.line(tok), lw=7, alpha=0.8, solid_capstyle="butt")
    ax.text(lo / 1.3, y, name, va="center", ha="right", fontsize=8, color=P.ink())
ax.set_xscale("log")
ax.set_xlim(1e-3, 3e5)
ax.set_ylim(-5.2, len(events) + 0.8)
ax.set_yticks([])
ax.axhline(0, color=P.muted(), lw=0.6)
charts.style_axes(ax, "force / pN", None)
ax.spines["left"].set_visible(False)
charts.title(ax, "Molecular forces (above) and instrument ranges (below)")
fig.tight_layout()
