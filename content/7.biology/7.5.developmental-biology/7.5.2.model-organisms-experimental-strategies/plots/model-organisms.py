"""Model organisms of developmental biology: relationships and generation times.

Left: a cladogram of the main animal models (topology after current phylogenomics; branch lengths not to
scale), with the sea anemone Nematostella as a cnidarian outgroup to the bilaterians, the planarian
Schmidtea as a spiralian, C. elegans and Drosophila as ecdysozoans, and the vertebrates. Right: typical
generation time in the laboratory (egg to egg, days, logarithmic scale; approximate): C. elegans 3.5 d at
20 C, Drosophila 10 d at 25 C, medaka 2-3 months, zebrafish 3 months, mouse 2 months, Xenopus tropicalis
about 5 months, chicken 5-6 months, minipig about 10 months (6 months to maturity plus 4 months of
gestation), Xenopus laevis 1-2 years, marmoset about 1.5 years, human about 25 years. Planarians are
mostly propagated by fission and the generation time of Nematostella varies with culture, so no bar is given.
"""

import numpy as np

import wikibio as bio
from wikibio import phylo, quant

P = bio.P
NEWICK = ("(Nematostella_vectensis,((Schmidtea_mediterranea,(Caenorhabditis_elegans,Drosophila_melanogaster)Ecdysozoa)Protostomia,"
          "((Danio_rerio,Oryzias_latipes)Teleostei,((Xenopus_laevis,Xenopus_tropicalis)Xenopus,(Gallus_gallus,"
          "(Sus_scrofa,(Mus_musculus,(Callithrix_jacchus,Homo_sapiens)Primates))Mammalia)Amniota)Tetrapoda)Vertebrata)Bilateria);")
ICONS = {
    "Nematostella vectensis": "phylopic/nematostella", "Schmidtea mediterranea": "phylopic/planarian",
    "Caenorhabditis elegans": ("phylopic/c-elegans", {"rotate": 90}), "Drosophila melanogaster": "phylopic/drosophila",
    "Danio rerio": "phylopic/zebrafish", "Oryzias latipes": "phylopic/medaka", "Xenopus laevis": "phylopic/xenopus",
    "Gallus gallus": "phylopic/chicken", "Sus scrofa": "servier/pig", "Mus musculus": "phylopic/mouse",
    "Callithrix jacchus": "phylopic/macaque", "Homo sapiens": "phylopic/human",
}
TEXT = {"Sus scrofa": "Sus scrofa (minipig)", "Callithrix jacchus": "Callithrix jacchus (marmoset)"}
GEN = {"Caenorhabditis elegans": 3.5, "Drosophila melanogaster": 10, "Danio rerio": 90, "Oryzias latipes": 75,
       "Xenopus laevis": 550, "Xenopus tropicalis": 150, "Gallus gallus": 165, "Sus scrofa": 300, "Mus musculus": 63,
       "Callithrix jacchus": 560, "Homo sapiens": 9000}
TOK = {"Ecdysozoa": "atp", "Vertebrata": "dna"}

fig, ax = bio.canvas(27, 14.4)
t = phylo.tree(ax, NEWICK, origin=(0.8, 0.9), width=6.8, height=12.6, direction="right", root_edge=0.4, italic=True,
               tip_text=TEXT, icons=ICONS, icon_size=0.75, icon_width=1.3, label_size="small",
               clades=[dict(node="Protostomia", token="atp", style="band", label="Protostomes"),
                       dict(node="Vertebrata", token="dna", style="band", label="Vertebrates")])

# generation-time bars aligned with the tips
x0, w = 17.2, 8.6
p = quant.Plot(ax, (x0, 0.55, w, 13.3), xlim=(1, 20000), ylim=(0, 1), xlog=True, frame=None)
for v, s in ((1, "1 d"), (10, "10 d"), (100, "100 d"), (1000, "1000 d"), (10000, "10⁴ d")):
    xx = float(p.X(v))
    ax.plot([xx, xx], [0.55, 13.6], color=P.mix(P.muted(), P.surface(), 0.6), lw=0.5, zorder=2)
    bio.label(ax, (xx, 0.3), s, size="tiny", color=P.muted())
bio.label(ax, (x0 + w / 2, 14.05), "generation time (egg to egg, log scale)", size="small", bold=True)
for tip in t.tips():
    name = tip.name
    y = t.node(name).xy[1]
    if name in GEN:
        xx = float(p.X(GEN[name]))
        tok = "atp" if name in ("Caenorhabditis elegans", "Drosophila melanogaster") else "dna"
        bio.box(ax, ((x0 + xx) / 2, y), xx - x0, 0.42, tok, radius=0.08)
        d = GEN[name]
        txt = f"{d:g} d" if d < 365 else f"{d / 365:.1f} yr"
        bio.label(ax, (xx + 0.15, y), txt, size="tiny", ha="left")
    else:
        bio.label(ax, (x0 + 0.15, y), "propagated by fission / variable", size="tiny", ha="left", color=P.muted())
