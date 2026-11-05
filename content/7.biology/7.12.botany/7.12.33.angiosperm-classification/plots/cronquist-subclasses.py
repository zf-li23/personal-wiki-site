# The 11 subclasses of the Cronquist system (1981) redrawn as a "bubble diagram" in the spirit of
# Cronquist's own figure (not traced). Bubble area is proportional to the number of species given by
# Cronquist (as summarised in Wu Guofang, Botany vol. 2, 2nd ed.); connecting lines show the presumed
# derivations: Magnoliidae at the base of the Magnoliopsida, Hamamelidae, Caryophyllidae and Dilleniidae
# from it, Rosidae alongside Dilleniidae, Asteridae from Rosidae; the Liliopsida from an ancestor like
# the Nymphaeales, with Alismatidae as a near-basal side branch.
import math

import wikibio as bio
from matplotlib.patches import Circle

P = bio.P
SUB = {  # name: (x, y, species, token)
    "Magnoliidae": (8.0, 3.6, 12000, "petal"),
    "Hamamelidae": (3.0, 7.0, 3400, "neutral"),
    "Caryophyllidae": (13.4, 6.9, 11000, "channel"),
    "Dilleniidae": (5.0, 10.6, 25000, "chloroplast"),
    "Rosidae": (10.6, 10.6, 58000, "plant"),
    "Asteridae": (10.8, 17.2, 60000, "dna"),
    "Alismatidae": (20.6, 3.0, 500, "rna"),
    "Arecidae": (22.0, 8.4, 5600, "atp"),
    "Commelinidae": (17.6, 11.0, 15000, "rrna"),
    "Zingiberidae": (22.6, 13.6, 3800, "mrna"),
    "Liliidae": (19.4, 17.0, 25000, "receptor"),
    "NODE": (18.2, 4.6, 0, "neutral"),  # the presumed stem of the Liliopsida
}
LINKS = [("Magnoliidae", "Hamamelidae"), ("Magnoliidae", "Caryophyllidae"), ("Magnoliidae", "Dilleniidae"),
         ("Magnoliidae", "Rosidae"), ("Rosidae", "Asteridae"), ("NODE", "Alismatidae"),
         ("NODE", "Arecidae"), ("NODE", "Commelinidae"), ("Commelinidae", "Zingiberidae"),
         ("Commelinidae", "Liliidae")]


def radius(n):
    return 0.0118 * math.sqrt(n)


fig, ax = bio.canvas(25, 21)
x0, y0, n0, _ = SUB["Magnoliidae"]
ux, uy = SUB["NODE"][0] - x0, SUB["NODE"][1] - y0
d = math.hypot(ux, uy)
ax.plot([x0 + ux / d * radius(n0), SUB["NODE"][0]], [y0 + uy / d * radius(n0), SUB["NODE"][1]], color=P.ink(), lw=1.3, zorder=3)
ax.add_patch(Circle(SUB["NODE"][:2], 0.12, color=P.ink(), zorder=6))
bio.label(ax, (SUB["NODE"][0] + 0.3, SUB["NODE"][1] - 0.4), "Nymphaealean-like ancestor", size="tiny", ha="left",
          color=P.muted())
for a, b in LINKS:
    (x0, y0, n0, _), (x1, y1, n1, _) = SUB[a], SUB[b]
    d = math.hypot(x1 - x0, y1 - y0)
    ux, uy = (x1 - x0) / d, (y1 - y0) / d
    r0, r1 = radius(n0), radius(n1)
    bio.arrow(ax, (x0 + ux * r0, y0 + uy * r0), (x1 - ux * (r1 + 0.1), y1 - uy * (r1 + 0.1)), kind="process")
for name, (x, y, n, tok) in SUB.items():
    if name == "NODE":
        continue
    r = radius(n)
    ax.add_patch(Circle((x, y), r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.3, zorder=5))
    inside = r > 1.4
    bio.label(ax, (x, y + (0.25 if inside else -r - 0.45)), name, size="normal", bold=True,
              color=P.on_fill() if inside else None, zorder=8)
    bio.label(ax, (x, y - (0.35 if inside else r + 0.95)), f"c. {n:,} spp.", size="small",
              color=P.on_fill() if inside else P.muted(), zorder=8)
bio.label(ax, (7.5, 20.2), "Magnoliopsida (dicotyledons): 6 subclasses", size="title")
bio.label(ax, (19.6, 20.2), "Liliopsida (monocotyledons): 5 subclasses", size="title")
ax.plot([15.9, 15.9], [1.0, 19.6], color=P.muted(), lw=0.8, ls=(0, (4, 3)))
bio.label(ax, (12.5, 0.6), "Bubble area proportional to number of species; arrows: presumed derivation (Cronquist 1981)",
          size="small", color=P.muted())
