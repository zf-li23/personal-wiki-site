# Genome size against the number of protein-coding genes (log-log). Values are approximate (genome
# assemblies and annotation releases differ by a few per cent): bacteria and archaea lie on the line of one
# gene per kilobase, eukaryotes spread far to the right of it. The gene count rises only about 100-fold from
# the smallest free-living bacteria to vertebrates and plants, while eukaryotic genome size spans more than
# four orders of magnitude.
import numpy as np
import wikibio as bio
from wikibio import charts as C

# (name, genome size / Mb, protein-coding genes, group)
data = [
    ("Carsonella", 0.16, 182, "p"),
    ("M. genitalium", 0.58, 476, "p"),
    ("Buchnera", 0.64, 564, "p"),
    ("M. jannaschii", 1.66, 1740, "p"),
    ("H. influenzae", 1.83, 1740, "p"),
    ("Synechocystis", 3.57, 3170, "p"),
    ("B. subtilis", 4.22, 4240, "p"),
    ("E. coli", 4.64, 4300, "p"),
    ("P. aeruginosa", 6.26, 5570, "p"),
    ("S. coelicolor", 8.67, 7830, "p"),
    ("S. cellulosum", 13.0, 9370, "p"),
    ("E. cuniculi", 2.9, 2000, "e"),
    ("S. cerevisiae", 12.1, 6000, "e"),
    ("S. pombe", 12.6, 5100, "e"),
    ("P. falciparum", 23.3, 5300, "e"),
    ("C. elegans", 100, 20000, "e"),
    ("Chlamydomonas", 111, 17700, "e"),
    ("Arabidopsis", 135, 27600, "e"),
    ("Drosophila", 144, 13900, "e"),
    ("Anopheles", 265, 13100, "e"),
    ("Rice", 389, 37800, "e"),
    ("Fugu", 390, 21000, "e"),
    ("Chicken", 1050, 17000, "e"),
    ("Zebrafish", 1370, 25600, "e"),
    ("Maize", 2300, 39000, "e"),
    ("Mouse", 2730, 22000, "e"),
    ("Human", 3100, 20000, "e"),
    ("Wheat", 15000, 107900, "e"),
    ("Axolotl", 32000, 23000, "e"),
]
P = bio.P
fig, ax = bio.canvas(15, 10)
a = C.axes_at(ax, (2.0, 1.5, 12.4, 8.0))
a.set_xscale("log")
a.set_yscale("log")
x = np.logspace(-1, 5, 50)
a.plot(x, x * 1000, color=P.muted(), lw=0.9, ls=(0, (4, 3)))
a.text(22, 22 * 1000 * 1.35, "1 gene per kb", fontsize=bio.core.FONT["tiny"], color=P.muted(), rotation=36, ha="center")
for name, mb, genes, grp in data:
    tok = "bacterium" if grp == "p" else "animal"
    a.plot(mb, genes, "o", ms=6, mfc=P.fill(tok), mec=C.line(tok), mew=0.9, zorder=5)
# labels for a subset of points (offset in points); scientific names in italics
offsets = {"Carsonella": (7, -2), "M. genitalium": (7, -5), "M. jannaschii": (-7, 5), "E. coli": (7, -6),
           "S. coelicolor": (-7, 5), "S. cellulosum": (7, -5), "E. cuniculi": (7, -6),
           "S. cerevisiae": (7, -7), "P. falciparum": (7, 8), "C. elegans": (-7, 5), "Arabidopsis": (-7, 6),
           "Drosophila": (7, -7), "Rice": (-7, 6), "Fugu": (0, -10), "Maize": (-7, 6), "Mouse": (7, 5),
           "Human": (7, -7), "Wheat": (-7, 6), "Axolotl": (-7, 6)}
common = {"Rice", "Fugu", "Maize", "Mouse", "Human", "Wheat", "Axolotl"}
for name, mb, genes, grp in data:
    if name not in offsets:
        continue
    dx, dy = offsets[name]
    a.annotate(name, (mb, genes), xytext=(dx, dy), textcoords="offset points", fontsize=bio.core.FONT["tiny"],
               color=P.ink(), ha="center" if dx == 0 else ("left" if dx > 0 else "right"), va="center",
               style="normal" if name in common else "italic")
a.set_xlim(0.1, 1e5)
a.set_ylim(100, 3e5)
a.set_xticks([0.1, 1, 10, 100, 1000, 1e4, 1e5], ["0.1", "1", "10", "100", "10³", "10⁴", "10⁵"])
a.set_yticks([100, 1000, 1e4, 1e5], ["10²", "10³", "10⁴", "10⁵"])
a.minorticks_off()
C.style_axes(a, "Genome size / Mb", "Protein-coding genes")
for k, (tok, text) in enumerate((("bacterium", "Bacteria and archaea"), ("animal", "Eukaryotes"))):
    yy = 9.0 - 0.45 * k
    ax.plot([2.4], [yy], "o", ms=6, mfc=P.fill(tok), mec=C.line(tok), mew=0.9)
    bio.label(ax, (2.65, yy), text, size="small", ha="left")
