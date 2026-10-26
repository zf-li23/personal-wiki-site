"""Light switches the Calvin cycle on (SBGN activity flow).

Two signals of illumination act on stromal enzymes. (1) Redox: photosystem I reduces ferredoxin;
ferredoxin:thioredoxin reductase (FTR) reduces thioredoxin, which reduces regulatory disulfides and
activates FBPase, SBPase, phosphoribulokinase (PRK) and NADP-GAPDH (and NADP-malate dehydrogenase and the
CF1 ATP synthase), while inactivating glucose 6-phosphate dehydrogenase of the oxidative pentose phosphate
pathway. Thioredoxin also activates rubisco activase. (2) Proton pumping into the lumen raises stromal pH
from about 7 to 8, and Mg2+ moves from the lumen into the stroma (1-3 to 3-6 mM); high pH and Mg2+ favour
carbamoylation of rubisco and activate FBPase. In the dark the disulfides re-form, CA1P accumulates and
binds rubisco, and the cycle stops.
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import network
from wikibio import photosynthesis as ps

P = bio.P
fig, ax = bio.canvas(25.0, 13.0, scale=0.42)
d = network.Diagram(ax, size="small")
for (x0, y0, x1, y1), tok, txt, ty in (((0.3, 2.9, 24.7, 12.7), "chloroplast", "Chloroplast stroma", 12.25),
                                      ((0.3, 0.3, 24.7, 2.5), "h", "Thylakoid membrane and lumen", 2.2)):
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0, boxstyle="round,pad=0,rounding_size=0.6",
                                facecolor=ps.tint(tok), edgecolor=P.edge(tok), lw=1.6, zorder=1))
    bio.label(ax, (x0 + 0.4, ty), txt, size="small", bold=True, ha="left", color=P.edge(tok))

d.perturbation("light", (2.4, 1.5), "light", token="highlight", w=2.2, h=0.9)
d.activity("psi", (6.6, 1.5), "photosystem I", token="psi")
d.activity("pump", (19.5, 1.5), "H⁺ pumping into lumen", token="h")
d.connect("light", "psi", "positive")
d.connect("light", "pump", "positive", via=[(2.4, 0.65), (19.5, 0.65)], end=(19.5, 1.05))

d.activity("fd", (6.6, 4.4), "ferredoxin (red.)", token="ferredoxin")
d.activity("ftr", (6.6, 6.6), "FTR", token="enzyme")
d.activity("trx", (6.6, 8.8), "thioredoxin (–SH HS–)", token="protein")
d.connect("psi", "fd", "positive")
d.connect("fd", "ftr", "positive")
d.connect("ftr", "trx", "positive")

targets = [("fbp", "FBPase", 10.8), ("sbp", "SBPase", 9.6), ("prk", "PRK", 8.4), ("gap", "NADP-GAPDH", 7.2)]
for id, t, y in targets:
    d.activity(id, (13.0, y), t, token="carbohydrate", w=3.6)
    d.connect("trx", id, "positive")
d.activity("g6pd", (13.0, 12.0), "G6P dehydrogenase", token="negative", w=3.8)
d.connect("trx", "g6pd", "negative")
d.activity("rca", (13.0, 5.0), "rubisco activase", token="enzyme", w=3.6)
d.connect("trx", "rca", "positive")

d.activity("rub", (19.5, 5.0), "rubisco (carbamoylated, Mg²⁺)", token="enzyme", w=5.6)
d.connect("rca", "rub", "positive", text="releases RuBP, CA1P", text_offset=(0, 0.2))
d.unspecified("phmg", (19.5, 3.55), "stroma pH 7 → 8; [Mg²⁺] 1–3 → 3–6 mM", token="mg", w=7.2, h=0.9)
d.connect("pump", "phmg", "positive")
d.connect("phmg", "rub", "positive")
d.connect("phmg", "fbp", "positive", via=[(23.8, 3.55), (23.8, 10.8)])

d.phenotype("cyc", (19.5, 8.8), "Calvin cycle on", token="highlight", w=4.4, h=1.1)
for id in ("fbp", "sbp", "prk", "gap"):
    d.connect(id, "cyc", "positive")
d.connect("rub", "cyc", "positive")
bio.label(ax, (19.5, 12.2), "Dark: disulfides re-form, CA1P binds rubisco", size="tiny", color=P.muted())
