"""Yellow mice (A^y A) intercrossed: A^y A^y embryos die after implantation, leaving 2 yellow : 1 agouti."""
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(13.0, 5.4)


def pheno(loci):
    a, b = loci[0]
    if "y" in a and "y" in b:
        return "Dies (embryo)"
    return "Yellow" if ("y" in a or "y" in b) else "Agouti"


out = G.punnett(ax, (2.2, 3.7), [("A^y", "A")], [("A^y", "A")], cell=1.6, phenotype=pheno,
                colors={"Yellow": "highlight", "Agouti": "enzyme", "Dies (embryo)": "neutral"},
                titles=("Male gametes", "Female gametes"), legend=False)
# cross out the lethal cell (row 0, column 0)
x0, y0, c = 2.2, 3.7, 1.6
for dx in (1, -1):
    ax.plot([x0 + 0.25, x0 + c - 0.25][::dx], [y0 - 0.25, y0 - c + 0.25], color=P.edge("negative"), lw=2.2, zorder=30)
lx = 6.2
for i, (tok, t) in enumerate((("highlight", "Yellow  AʸA   2/3 of survivors"), ("enzyme", "Agouti  AA   1/3 of survivors"),
                              ("neutral", "AʸAʸ dies after implantation"))):
    y = 3.1 - i * 0.8
    ax.add_patch(bio.core.FancyBboxPatch((lx, y - 0.22), 0.44, 0.44, boxstyle="round,pad=0,rounding_size=0.08",
                                         facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8))
    bio.label(ax, (lx + 0.65, y), t, size="small", ha="left")
bio.label(ax, (lx, 0.6), "Ratio among live progeny  2 : 1", size="normal", bold=True, ha="left")
