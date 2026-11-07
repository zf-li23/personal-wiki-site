# Plant processes on one logarithmic time axis (values taken from chapters 2-28 of this course).
# Each bar spans the typical range of the process; the row colour marks the line of the course it belongs to.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
MIN, H, D, YR = 60.0, 3600.0, 86400.0, 3.156e7

# (label, t_min, t_max, group)
ROWS = [
    ("Venus flytrap closes", 0.1, 0.3, "move"),
    ("Mimosa leaflets fold", 1.0, 2.0, "move"),
    ("Cell reaches water-potential equilibrium (t½)", 1.0, 10.0, "water"),
    ("ROS burst after flg22 (onset to peak)", 2 * MIN, 15 * MIN, "signal"),
    ("Phytochrome-induced transcription", 5 * MIN, 30 * MIN, "signal"),
    ("Stomatal opening or closure", 3 * MIN, 30 * MIN, "water"),
    ("Lag of acid growth after auxin", 10 * MIN, 15 * MIN, "growth"),
    ("Phloem moves sucrose 1 m", 0.7 * H, 3.3 * H, "carbon"),
    ("Gravitropic bending of a root", 1 * H, 5 * H, "growth"),
    ("ABA rises ~50-fold in a drying leaf", 4 * H, 8 * H, "signal"),
    ("Free-running circadian period", 24 * H, 25 * H, "signal"),
    ("Systemic acquired resistance builds", 1 * D, 2 * D, "env"),
    ("Photoperiodic induction (1 to ~12 cycles)", 1 * D, 12 * D, "develop"),
    ("Vernalization (days to ~3 months of cold)", 5 * D, 90 * D, "develop"),
    ("Life cycle of an annual crop", 90 * D, 200 * D, "develop"),
    ("Diffusion of glucose over 1 m", 25 * YR, 40 * YR, "water"),
    ("Seed longevity (orthodox seeds)", 1 * YR, 1000 * YR, "develop"),
    ("Oldest bristlecone pine", 4800 * YR, 5000 * YR, "develop"),
]
GROUP = {"water": ("dna", "water & solutes"), "carbon": ("atp", "carbon"),
         "signal": ("rna", "signals"), "growth": ("chloroplast", "growth"),
         "develop": ("petal", "development"), "move": ("enzyme", "movement"), "env": ("negative", "biotic stress")}

fig, ax = bio.canvas(24.0, 14.0)
pa = charts.axes_at(ax, (8.8, 1.4, 14.8, 12.0))
n = len(ROWS)
for k, (name, t0, t1, g) in enumerate(ROWS):
    y = n - 1 - k
    tok = GROUP[g][0]
    pa.plot([t0, t1], [y, y], color=charts.line(tok), lw=7, solid_capstyle="round")
    pa.text(1.5e-2, y, name, ha="right", va="center", fontsize=8.5, color=P.ink(), clip_on=False)
pa.set_xscale("log")
pa.set_xlim(3e-2, 1e12)
pa.set_ylim(-0.8, n - 0.2)
pa.set_yticks([])
ticks = [1, MIN, H, D, 30 * D, YR, 100 * YR, 1e4 * YR]
pa.set_xticks(ticks)
pa.set_xticklabels(["1 s", "1 min", "1 h", "1 d", "1 mo", "1 yr", "100 yr", "10⁴ yr"])
for t in ticks:
    pa.axvline(t, color=P.muted(), lw=0.4, ls=":", zorder=0)
charts.style_axes(pa, "Time (log scale)", None)
pa.spines["left"].set_visible(False)
# legend
seen = []
for k, (g, (tok, text)) in enumerate(GROUP.items()):
    pa.plot([], [], color=charts.line(tok), lw=6, label=text)
pa.legend(frameon=False, fontsize=8, loc="upper right", labelcolor=P.ink(), ncol=2)
