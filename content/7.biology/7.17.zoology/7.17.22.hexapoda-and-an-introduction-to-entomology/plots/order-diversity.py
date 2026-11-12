# Described species of the living hexapod orders (approximate counts as given by Brusca, Giribet & Moore
# 2023, Invertebrates 4th ed., chapter 22), on a log scale, grouped and coloured by lineage.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
DATA = [
    ("Entognatha", "neutral", [("Collembola", 6000), ("Protura", 200), ("Diplura", 800)]),
    ("Apterygote insects", "bone", [("Archaeognatha", 390), ("Zygentoma", 450)]),
    ("Palaeoptera", "channel", [("Ephemeroptera", 2500), ("Odonata", 6000)]),
    ("Polyneoptera", "positive", [("Plecoptera", 1700), ("Dermaptera", 1800), ("Orthoptera", 23000), ("Zoraptera", 40),
                                  ("Embioptera", 430), ("Phasmida", 3000), ("Grylloblattodea", 33),
                                  ("Mantophasmatodea", 21), ("Mantodea", 2400), ("Blattodea", 7000)]),
    ("Paraneoptera", "protein", [("Psocodea", 8500), ("Thysanoptera", 5000), ("Hemiptera", 85000)]),
    ("Holometabola", "enzyme", [("Hymenoptera", 115000), ("Raphidioptera", 260), ("Megaloptera", 300),
                                ("Neuroptera", 6000), ("Coleoptera", 387100), ("Strepsiptera", 600),
                                ("Mecoptera", 600), ("Siphonaptera", 2700), ("Diptera", 159295),
                                ("Trichoptera", 12000), ("Lepidoptera", 157402)]),
]
rows = []
for grp, tok, items in DATA:
    for name, n in items:
        rows.append((name, n, tok, grp))
fig, ax = bio.canvas(22, 17)
pax = charts.axes_at(ax, (5.2, 1.4, 12.5, 15.0))
y = np.arange(len(rows))[::-1]
for yi, (name, n, tok, grp) in zip(y, rows):
    pax.barh(yi, n, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.7, height=0.72)
    pax.text(n * 1.15, yi, f"{n:,}", va="center", ha="left", fontsize=7, color=P.ink())
pax.set_yticks(y)
pax.set_yticklabels([r[0] for r in rows], fontsize=8)
pax.set_xscale("log")
pax.set_xlim(10, 2e6)
pax.set_ylim(-0.7, len(rows) - 0.3)
charts.style_axes(pax, "Described species (log scale)")
# lineage legend
yl = 16.0
for grp, tok, items in DATA:
    bio.shape(ax, [(18.6, yl - 0.2), (19.0, yl - 0.2), (19.0, yl + 0.2), (18.6, yl + 0.2)], tok, lw=0.8, zorder=20)
    bio.label(ax, (19.2, yl), grp, size="small", ha="left")
    yl -= 0.7
