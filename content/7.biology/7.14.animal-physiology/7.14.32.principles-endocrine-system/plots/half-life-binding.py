# Plasma half-life of hormones against the unbound (free) fraction in plasma.
# Typical adult values from standard physiology texts (Boron & Boulpaep, Guyton & Hall) and reviews;
# ranges are wide and the points are indicative. Peptides and catecholamines circulate essentially free
# (f ~ 1). Dashed line: t1/2 = 5 min / f, the expectation if only the free hormone is cleared, with a
# clearance and distribution volume like those of a small peptide (Eq. 32.3 in the text).
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
# name, free fraction, half-life in minutes, class token, label side ("l"/"r" seen on the page), dy (log10)
data = [
    ("Epinephrine", 1.0, 2.5, "dna", "r", 0.0),
    ("PTH", 1.0, 4.0, "dna", "l", 0.0),
    ("Insulin", 1.0, 6.0, "dna", "r", 0.03),
    ("ADH", 1.0, 15.0, "dna", "l", 0.0),
    ("TSH", 1.0, 60.0, "dna", "r", 0.0),
    ("GH", 0.6, 22.0, "dna", "r", 0.1),
    ("Aldosterone", 0.4, 20.0, "rna", "r", -0.12),
    ("Cortisol", 0.05, 80.0, "rna", "l", 0.08),
    ("Testosterone", 0.02, 15.0, "rna", "r", 0.0),
    ("IGF-1 (total)", 0.01, 900.0, "dna", "l", 0.08),
    ("T3", 0.003, 1440.0, "positive", "r", -0.08),
    ("T4", 0.0003, 9360.0, "positive", "l", 0.0),
    ("25(OH)D", 0.0003, 25000.0, "rna", "l", 0.0),
]

fig, ax = bio.canvas(16.0, 10.0)
pa = charts.axes_at(ax, (2.4, 1.6, 12.6, 7.6))
ff = np.logspace(-4, 0, 50)
pa.plot(ff, 5.0 / ff, color=P.muted(), lw=1.1, ls="--")
pa.text(3e-2, 5.0 / 3e-2 * 1.6, "t½ = 5 min / f", color=P.muted(), fontsize=7.5, rotation=24,
        ha="center", va="bottom")
for name, f, t, tok, side, dy in data:
    pa.scatter([f], [t], s=34, color=charts.line(tok), zorder=3)
    # the x axis is inverted: a smaller f lies further to the right
    if side == "r":
        pa.text(f / 10 ** 0.07, t * 10 ** dy, name, fontsize=7.5, color=P.ink(), ha="left", va="center")
    else:
        pa.text(f * 10 ** 0.07, t * 10 ** dy, name, fontsize=7.5, color=P.ink(), ha="right", va="center")
pa.set_xscale("log")
pa.set_yscale("log")
pa.set_xlim(2.0, 1e-4)
pa.set_ylim(1.0, 6e4)
for y, lab in ((1, "1 min"), (60, "1 h"), (1440, "1 d"), (10080, "1 wk")):
    pa.axhline(y, color=P.mix(P.muted(), P.surface(), 0.55), lw=0.6, zorder=0)
    pa.text(1.1e-4, y * 1.1, lab, fontsize=6.5, color=P.muted(), ha="right", va="bottom")
for tok, lab, y in (("dna", "peptides, amines (water-soluble)", 3.1), ("rna", "steroids, vitamin D", 2.6),
                    ("positive", "thyroid hormones", 2.1)):
    ax.scatter([10.2], [y], s=30, color=charts.line(tok), zorder=30, clip_on=False)
    bio.label(ax, (10.5, y), lab, size="small", ha="left")
charts.style_axes(pa, "free (unbound) fraction in plasma, f", "plasma half-life / min")
charts.title(pa, "Protein binding protects hormones from clearance")
