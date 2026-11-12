"""Numbers of described living species in the animal phyla, on a logarithmic axis.

Data: Brusca, Giribet & Moore, Invertebrates, 4th ed. (2023), Table 1.1 (described valid living species,
1,453,163 in total; compiled from Zhang 2011, 2013 and later counts). Arthropoda is split into its four
subphyla. Bars are coloured by the major clade of the phylum (see the animal tree of 7.17.6).
"""

import wikibio as bio
from wikibio import charts

P = bio.P
FONT = bio.core.FONT

CLADE = {"N": "neutral", "X": "lipid", "S": "positive", "E": "atp", "D": "dna"}
NAMES = {"N": "non-bilaterians", "X": "Xenacoelomorpha", "S": "Spiralia", "E": "Ecdysozoa", "D": "Deuterostomia"}
rows = [
    ("Porifera", 9300, "N"), ("Ctenophora", 130, "N"), ("Placozoa", 4, "N"), ("Cnidaria", 13300, "N"),
    ("Xenacoelomorpha", 400, "X"),
    ("Platyhelminthes", 30000, "S"), ("Gastrotricha", 860, "S"), ("Rotifera", 3350, "S"),
    ("Gnathostomulida", 100, "S"), ("Micrognathozoa", 1, "S"), ("Chaetognatha", 130, "S"), ("Dicyemida", 120, "S"),
    ("Mollusca", 73000, "S"), ("Annelida", 20000, "S"), ("Nemertea", 1300, "S"),
    ("Bryozoa", 6300, "S"), ("Brachiopoda", 440, "S"), ("Phoronida", 15, "S"), ("Entoprocta", 200, "S"), ("Cycliophora", 2, "S"),
    ("Nematoda", 27000, "E"), ("Nematomorpha", 365, "E"), ("Kinorhyncha", 300, "E"), ("Priapulida", 22, "E"),
    ("Loricifera", 38, "E"), ("Tardigrada", 1300, "E"), ("Onychophora", 200, "E"),
    ("Arthropoda: Chelicerata", 113000, "E"), ("Arthropoda: Myriapoda", 16000, "E"),
    ("Arthropoda: Crustacea", 72000, "E"), ("Arthropoda: Hexapoda", 995521, "E"),
    ("Echinodermata", 7300, "D"), ("Hemichordata", 130, "D"),
    ("Chordata: Cephalochordata", 35, "D"), ("Chordata: Urochordata", 3000, "D"),
    ("Chordata: Vertebrata", 58000, "D"),
]
n = len(rows)
fig, ax = bio.canvas(17.4, 20.0)
a = charts.axes_at(ax, (6.6, 1.3, 9.6, 17.6))
for i, (name, k, c) in enumerate(rows):
    y = n - 1 - i
    tok = CLADE[c]
    a.barh(y, k, height=0.66, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.9)
    a.text(k * 1.25, y, f"{k:,}", va="center", fontsize=FONT["tiny"], color=P.ink())
a.set_xscale("log")
a.set_xlim(0.7, 1e7)
a.set_yticks(range(n))
a.set_yticklabels([r[0] for r in rows][::-1], fontsize=FONT["small"])
a.set_ylim(-0.7, n - 0.3)
charts.style_axes(a, "described living species (log scale)")
for x in (10, 100, 1000, 10000, 100000, 1000000):
    a.axvline(x, color=P.muted(), lw=0.4, ls=":", zorder=0)

# legend of clades
x0, y0 = 14.0, 18.2
bio.label(ax, (x0, y0 + 0.55), "Major clade", size="small", bold=True, ha="left")
for j, c in enumerate("NXSED"):
    yy = y0 - j * 0.5
    bio.box(ax, (x0 + 0.2, yy), 0.32, 0.26, token=CLADE[c], radius=0.04)
    bio.label(ax, (x0 + 0.55, yy), NAMES[c], size="small", ha="left")
bio.label(ax, (14.0, 14.6), "Total 1,453,163\nArthropoda 82%\nHexapoda 68.5%", size="small",
          ha="left", color=P.muted())
