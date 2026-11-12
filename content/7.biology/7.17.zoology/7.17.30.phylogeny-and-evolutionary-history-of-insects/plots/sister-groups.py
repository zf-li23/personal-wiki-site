# Sister-group comparisons among insect lineages: described species (approximate counts from Brusca, Giribet &
# Moore 2023) on a log scale, and the equal-rates (Yule) probability that the smaller clade is this small or
# smaller, P = 2 n / (N - 1) (Slowinski & Guyer 1989; Eq. 30.2).
import numpy as np
import wikibio as bio
from matplotlib.patches import FancyBboxPatch
from wikibio import quant

P = bio.P
pairs = [
    ("Pterygota", 987700, "Zygentoma", 450, "wings"),
    ("Holometabola", 841300, "Paraneoptera", 98500, "complete metamorphosis"),
    ("Coleopterida", 387700, "Neuropterida", 6560, ""),
    ("Coleoptera", 387100, "Strepsiptera", 600, ""),
    ("Diptera", 159300, "Mecoptera + fleas", 3300, ""),
    ("Lepidoptera", 157400, "Trichoptera", 12000, ""),
    ("Hemiptera", 85000, "Thysanoptera", 5000, ""),
]
fig, ax = bio.canvas(26, 13)
pl = quant.Plot(ax, (9.0, 1.4, 11.0, 10.6), xlim=(100, 2e6), ylim=(0, len(pairs)), xlog=True,
                xlabel="Described species (log scale)",
                xticks=[(100, "100"), (1e3, "1,000"), (1e4, "10,000"), (1e5, "100,000"), (1e6, "1,000,000")])
bio.label(ax, (23.3, 12.4), "P (equal rates)", size="small", bold=True)
for k, (a, na, b, nb, note) in enumerate(pairs):
    yc = len(pairs) - k - 0.5
    for (name, n, dy, tok) in ((a, na, 0.18, "enzyme"), (b, nb, -0.18, "neutral")):
        x0, y0 = pl.xy(100, yc + dy - 0.15)
        x1, y1 = pl.xy(n, yc + dy + 0.15)
        ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0, boxstyle="round,pad=0,rounding_size=0.06",
                                        facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.7, zorder=6))
        bio.label(ax, (x0 - 0.2, (y0 + y1) / 2), name, size="small", ha="right")
        bio.label(ax, (x1 + 0.15, (y0 + y1) / 2), f"{n:,}", size="tiny", ha="left", color=P.muted())
    N = na + nb
    p = 2 * min(na, nb) / (N - 1)
    tok = "negative" if p < 0.05 else "neutral"
    bio.label(ax, (23.3, pl.xy(100, yc)[1]), ("%.4f" % p) if p < 0.001 else ("%.3f" % p), size="small",
              color=P.edge(tok), bold=p < 0.05)
    if note:
        bio.label(ax, (23.3, pl.xy(100, yc)[1] - 0.45), note, size="tiny", color=P.muted())
    if k:
        yy = pl.xy(100, yc + 0.5)[1]
        ax.plot([1.0, 25.0], [yy, yy], color=P.muted(), lw=0.4, ls=(0, (2, 2)), zorder=3)
bio.label(ax, (13, 0.2), "Upper bar of each pair: the richer clade. Bold: P < 0.05 under the Yule model (Eq. 30.2).",
          size="tiny", color=P.muted())
