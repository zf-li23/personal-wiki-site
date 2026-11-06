# Approximate species numbers of the subfamilies of Asteraceae (log scale), in order of divergence from top
# (earliest) to bottom; compiled from Funk et al. (2009) and Panero & Crozier (2016). Numbers are rounded.
import wikibio as bio
from wikibio import charts

P = bio.P
DATA = [("Barnadesioideae", 90), ("Famatinanthoideae", 1), ("Mutisioideae", 630), ("Stifftioideae", 45),
        ("Wunderlichioideae", 25), ("Gochnatioideae", 90), ("Hecastocleidoideae", 1), ("Carduoideae", 2500),
        ("Pertyoideae", 70), ("Gymnarrhenoideae", 1), ("Cichorioideae", 3600), ("Corymbioideae", 10),
        ("Asteroideae", 17000)]
fig, ax = bio.canvas(22, 11)
ax.set_axis_off()
a = charts.axes_at(ax, (6.0, 1.4, 14.5, 9.0))
names = [d[0] for d in DATA][::-1]
vals = [d[1] for d in DATA][::-1]
big = {"Carduoideae", "Cichorioideae", "Asteroideae"}
cols = [P.fill("petal") if n in big else P.fill("neutral") for n in names]
a.barh(range(len(names)), vals, color=cols, edgecolor=[P.edge("petal") if n in big else P.edge("neutral") for n in names])
a.set_xscale("log")
a.set_yticks(range(len(names)))
a.set_yticklabels(names, fontsize=8)
a.set_xlabel("Number of species (approximate, log scale)")
for i, v in enumerate(vals):
    a.text(v * 1.15, i, f"{v:,}", va="center", fontsize=7, color=P.ink())
a.set_xlim(0.8, 60000)
for s in ("top", "right"):
    a.spines[s].set_visible(False)
