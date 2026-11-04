"""Global biomass by taxon (Gt C) with uncertainty fold-ranges, after Bar-On, Phillips and Milo (2018)."""
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
DATA = [("Plants", 450, 1.2, "plant"), ("Bacteria", 70, 10, "bacterium"), ("Fungi", 12, 3, "carbohydrate"),
        ("Archaea", 7, 13, "enzyme"), ("Protists", 4, 4, "protein"), ("Animals", 2, 5, "animal"),
        ("Viruses", 0.2, 20, "virus")]
TOTAL = 550
fig, ax = bio.canvas(16, 8)
pax = charts.axes_at(ax, (3.2, 1.3, 11.6, 6.0))
y = np.arange(len(DATA))[::-1]
for yi, (name, v, fold, tok) in zip(y, DATA):
    pax.barh(yi, v, height=0.62, left=0.01, color=P.fill(tok), edgecolor=P.edge(tok), lw=1.0)
    pax.plot([v / fold, v * fold], [yi, yi], color=P.ink(), lw=0.9)
    for e in (v / fold, v * fold):
        pax.plot([e, e], [yi - 0.12, yi + 0.12], color=P.ink(), lw=0.9)
    share = 100 * v / TOTAL
    txt = f"{v:g} Gt C ({share:.0f}%)" if share >= 1 else f"{v:g} Gt C (<1%)"
    pax.text(v * fold * 1.25, yi, txt, va="center", ha="left", fontsize=bio.FONT["tiny"] if hasattr(bio, "FONT") else 6.8,
             color=P.ink())
pax.set_xscale("log")
pax.set_xlim(0.01, 1e5)
pax.set_ylim(-0.6, len(DATA) - 0.4)
pax.set_yticks(y)
pax.set_yticklabels([d[0] for d in DATA])
pax.set_xticks([0.01, 0.1, 1, 10, 100, 1000])
pax.set_xticklabels(["0.01", "0.1", "1", "10", "100", "1000"])
charts.style_axes(pax, "biomass / Gt C (log scale)", None)
pax.spines["right"].set_visible(False)
pax.set_xlim(0.01, 3e4)
bio.label(ax, (8.5, 7.7), "Global biomass: total about 550 Gt C", size="normal", bold=True)
