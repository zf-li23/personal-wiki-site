"""The hallmarks of cancer (Hanahan and Weinberg 2000, 2011; Hanahan 2022).

Outer ring: capabilities acquired by cancer cells during tumor progression, colored by the year in which
they were proposed (six in 2000, two "emerging" hallmarks in 2011, two more in 2022), each with typical
underlying changes. Inner disc: enabling characteristics, which do not themselves confer a capability but
accelerate the acquisition of the hallmarks (genome instability from 2000/2011, tumor-promoting inflammation
from 2011, nonmutational epigenetic reprogramming and polymorphic microbiomes from 2022).
"""

import numpy as np
from matplotlib.patches import Circle, Wedge

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(19.0, 15.0)
c = np.array([9.5, 7.3])
R0, R1 = 3.0, 6.0

items = [
    ("sustaining\nproliferative\nsignaling", "RTK, Ras, Myc", 2000),
    ("evading\ngrowth\nsuppressors", "Rb, p16, TGF-β", 2000),
    ("resisting\ncell death", "p53, Bcl-2", 2000),
    ("enabling\nreplicative\nimmortality", "telomerase, ALT", 2000),
    ("inducing\nangiogenesis", "VEGF, hypoxia", 2000),
    ("activating\ninvasion and\nmetastasis", "E-cadherin loss,\nEMT, MMPs", 2000),
    ("reprogramming\ncellular\nmetabolism", "Warburg effect,\nIDH", 2011),
    ("avoiding\nimmune\ndestruction", "PD-L1, MHC loss", 2011),
    ("unlocking\nphenotypic\nplasticity", "dedifferentiation,\nblocked\ndifferentiation", 2022),
    ("senescent\ncells", "SASP of\nstromal and\ntumor cells", 2022),
]
TOK = {2000: "positive", 2011: "drug", 2022: "channel"}
n = len(items)
for k, (name, ex, yr) in enumerate(items):
    a0 = 90 - 360 * (k + 1) / n
    a1 = 90 - 360 * k / n
    ax.add_patch(Wedge(c, R1, a0, a1, width=R1 - R0, facecolor=P.fill(TOK[yr]), edgecolor=P.surface(), lw=2.5,
                       zorder=3))
    am = np.radians((a0 + a1) / 2)
    p = c + 4.65 * np.array([np.cos(am), np.sin(am)])
    bio.label(ax, p, name, size="small", bold=True, color=P.on_fill(), zorder=5)
    q = c + 6.9 * np.array([np.cos(am), np.sin(am)])
    ha = "left" if np.cos(am) > 0.2 else "right" if np.cos(am) < -0.2 else "center"
    bio.label(ax, q, ex, size="tiny", ha=ha, color=P.muted())
ax.add_patch(Circle(c, R0 - 0.15, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=1.2, zorder=3))
bio.label(ax, c + (0, 1.85), "enabling characteristics", size="small", bold=True, color=P.on_fill(), zorder=5)
bio.label(ax, c + (0, 0.25), "genome instability\nand mutation\n\ntumor-promoting\ninflammation", size="tiny",
          color=P.on_fill(), zorder=5)
bio.label(ax, c + (0, -1.7), "nonmutational epigenetic\nreprogramming\npolymorphic microbiomes", size="tiny",
          color=P.on_fill(), zorder=5)
for j, yr in enumerate((2000, 2011, 2022)):
    x = 15.0 + j * 1.4
    ax.add_patch(Circle((x, 14.4), 0.25, facecolor=P.fill(TOK[yr]), edgecolor=P.edge(TOK[yr]), lw=0.8))
    bio.label(ax, (x + 0.4, 14.4), str(yr), size="tiny", ha="left")
