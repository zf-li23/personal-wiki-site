"""The global methane budget, 2008-2017 (top-down estimates from atmospheric inversions), with the
microbial share marked.

Sources (Tg CH4 per year): natural wetlands 181; other natural sources 37 (inland waters, geological seeps,
termites, wild animals, permafrost, oceans); agriculture and waste 217 (enteric fermentation in ruminants
and manure, rice cultivation, landfills and wastewater); fossil fuels 111; biomass and biofuel burning 30.
Sinks: chemical loss, mainly oxidation by OH radicals in the troposphere, 518; uptake by aerobic
methanotrophs in soils 38. Total sources 576 exceed total sinks 556, consistent with the observed rise of
atmospheric methane. Methane from wetlands, ruminants, rice paddies and landfills is made by methanogenic
archaea (biogenic); fossil and burning sources are not microbial; "other natural" is mixed.
Data from Saunois et al. (2020).
"""
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22.0, 10.5)
src = [("natural wetlands", 181, "positive"), ("other natural", 37, "neutral"),
       ("agriculture and waste", 217, "positive"), ("fossil fuels", 111, "negative"),
       ("biomass and biofuel burning", 30, "negative")]
snk = [("chemical loss (OH)", 518, "negative"), ("soil methanotrophs", 38, "positive")]

pl = quant.Plot(ax, (8.5, 1.6, 12.0, 7.8), xlim=(0, 600), ylim=(-0.5, 9.0), xlabel="Tg CH₄ yr⁻¹",
                xticks=[0, 100, 200, 300, 400, 500, 600], frame="l")
rows = [(r, "src") for r in src] + [(r, "snk") for r in snk]
y = 8.2
for (name, v, tok), kind in rows:
    if kind == "snk" and name.startswith("chemical"):
        y -= 1.0
        bio.label(ax, (0.4, pl.Y(y + 0.75)), "Sinks (total 556)", size="small", bold=True, ha="left")
    if kind == "src" and name.startswith("natural"):
        bio.label(ax, (0.4, pl.Y(y + 0.75)), "Sources (total 576)", size="small", bold=True, ha="left")
    y0, y1 = pl.Y(y - 0.35), pl.Y(y + 0.35)
    ax.add_patch(Rectangle((pl.X(0), y0), pl.X(v) - pl.X(0), y1 - y0, facecolor=P.fill(tok), edgecolor=P.edge(tok),
                           lw=0.8, zorder=8))
    bio.label(ax, (pl.X(0) - 0.2, pl.Y(y)), name, size="small", ha="right")
    bio.label(ax, (pl.X(v) + 0.15, pl.Y(y)), f"{v}", size="tiny", ha="left")
    y -= 1.0
for k, (txt, tok) in enumerate([("microbial", "positive"), ("not microbial", "negative"), ("mixed", "neutral")]):
    x = pl.X(330) + k * 2.6
    ax.add_patch(Rectangle((x, pl.Y(5.6)), 0.5, 0.35, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=8))
    bio.label(ax, (x + 0.65, pl.Y(5.6) + 0.17), txt, size="tiny", ha="left")
