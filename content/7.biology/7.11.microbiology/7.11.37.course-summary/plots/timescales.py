"""Microbial processes on one logarithmic time axis, from the run of a swimming cell to the history of
microbial life, with the values used in the chapters of the course. Rows: physiology and regulation,
growth and infection, evolution, Earth history."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
MIN, H, D, Y = 60.0, 3600.0, 86400.0, 3.156e7

ROWS = [
    ("Physiology\nand regulation", "enzyme", [
        (1.0, "run of a swimming\n$\\it{E.\\ coli}$ cell", 0),
        (3 * MIN, "transcriptional\nresponse", 1),
        (40 * MIN, "change of a whole\nexpression program", 0),
    ]),
    ("Growth and\ninfection", "positive", [
        (10 * MIN, "$\\it{V.\\ natriegens}$\ndoubling", 1),
        (25 * MIN, "latent period\nof phage T4", 0),
        (20 * H, "$\\it{M.\\ tuberculosis}$\ngeneration", 1),
        (2.5 * 7 * D, "Asgard archaeon\nin co-culture", 0),
        (300 * Y, "deep biosphere:\nyears to millennia", 1),
    ]),
    ("Evolution", "dna", [
        (3 * Y, "resistance after\na new antibiotic", 0),
        (15 * Y, "citrate use in the\nLTEE (31 500 gen.)", 1),
        (5e7 * Y, "1 % 16S rRNA\ndivergence", 0),
    ]),
    ("Earth history", "bacterium", [
        (2.4e9 * Y, "Great Oxidation\nEvent", 1),
        (3.43e9 * Y, "oldest\nstromatolites", 0),
    ]),
]

fig, ax = bio.canvas(26, 12.5)
a = charts.axes_at(ax, (4.6, 1.4, 20.8, 10.4))
a.set_xscale("log")
a.set_xlim(0.3, 3e17)
a.set_ylim(-0.6, len(ROWS) - 0.45)
for i, (lab, tok, items) in enumerate(ROWS):
    y = len(ROWS) - 1 - i
    a.axhline(y, color=P.mix(P.muted(), P.surface(), 0.55), lw=0.6, zorder=1)
    a.text(0.22, y, lab, ha="right", va="center", fontsize=FT["small"], color=P.ink(),
           )
    for t, txt, up in items:
        a.scatter([t], [y], s=60, color=P.fill(tok), edgecolor=charts.line(tok), lw=1.0, zorder=3)
        dy = 0.13 if up else -0.13
        a.text(t, y + dy, txt, ha="center", va="bottom" if up else "top", fontsize=FT["tiny"], color=P.ink())
ticks = [(1, "1 s"), (MIN, "1 min"), (H, "1 h"), (D, "1 d"), (Y, "1 yr"), (1e3 * Y, "1 kyr"),
         (1e6 * Y, "1 Myr"), (1e9 * Y, "1 Gyr")]
a.set_xticks([t for t, _ in ticks])
a.set_xticklabels([s for _, s in ticks])
a.minorticks_off()
a.set_yticks([])
charts.style_axes(a, "time (logarithmic scale)")
a.spines["left"].set_visible(False)
