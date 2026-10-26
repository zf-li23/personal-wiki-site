# The catalytic centres of four ribozymes, drawn as "what must be aligned" rather than as folds.
# A: group I intron - an exogenous guanosine bound in a pocket attacks the 5' splice site, which the internal
#    guide sequence holds by base pairing; two metal ions (A activates the nucleophile, B stabilizes the
#    leaving 3'-oxygen).
# B: group II intron and the U2/U5/U6 centre of the spliceosome - the 2'-OH of a bulged branch-point adenosine
#    attacks the same phosphate, giving a lariat; the metals are held by domain V (by U6 in the spliceosome).
# C: RNase P - a metal-activated water attacks the phosphodiester 5' of the mature tRNA; the enzyme reads the
#    shape of the acceptor stem and the CCA end, not a sequence.
# D: peptidyl transferase centre - the alpha-amino group of the A-site aminoacyl-tRNA attacks the ester carbonyl
#    of the peptidyl-tRNA, with the 2'-OH of A76 shuttling the proton; no protein side chain reaches the site.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(25.0, 12.6)

NEG = P.edge("negative")


def phosphate(xy, text="P", token="negative", r=0.22):
    ax.add_patch(bio.core.Circle(xy, r, facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.9, zorder=14))
    bio.label(ax, xy, text, size="tiny", color=P.on_fill(), zorder=15)


def nucleophile(xy, text, dy=0.5):
    ax.add_patch(bio.core.Circle(xy, 0.11, color=P.edge("highlight"), zorder=14))
    bio.label(ax, (xy[0], xy[1] + dy), text, size="tiny", color=P.edge("highlight"), zorder=15)


def metals(xys, names=("A", "B")):
    for xy, name in zip(xys, names):
        bio.ion(ax, xy, "mg", r=0.21, text=False, zorder=13)
        bio.label(ax, xy, name, size="tiny", color=P.on_fill(), zorder=14)


def strandline(a, b, token="rna", lw=1.9):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge(token), lw=lw, zorder=6, solid_capstyle="round")


def pairs(x0, x1, y, n=5, h=0.42):
    """Short base-pair rungs between two antiparallel strands at y and y - h."""
    xs = np.linspace(x0, x1, n)
    strandline((x0 - 0.2, y), (x1 + 0.2, y))
    strandline((x0 - 0.2, y - h), (x1 + 0.2, y - h), token="mrna")
    for x in xs:
        ax.plot([x, x], [y, y - h], color=P.muted(), lw=0.8, zorder=5)


# ----------------------------------------------------------------- A: group I intron
bio.panel(ax, "A", (0.1, 12.4))
bio.label(ax, (3.0, 12.4), "Group I intron", size="small", bold=True, ha="left")
yA = 10.2
bio.box(ax, (1.9, yA), 2.4, 0.62, token="mrna", text="5′ exon", size="tiny", radius=0.08, zorder=8)
strandline((3.2, yA), (9.8, yA))
bio.label(ax, (6.2, yA + 0.42), "intron", size="tiny", color=P.edge("rna"))
phosphate((3.25, yA))
pairs(5.6, 7.8, yA - 1.2, n=5)
strandline((3.2, yA), (5.4, yA - 1.2))
bio.label(ax, (6.7, yA - 2.15), "internal guide sequence\npairs with the 5′ exon", size="tiny", color=P.muted())
bio.molecule(ax, (8.6, yA + 1.5), token="metabolite", text="G", r=0.34, size="tiny")
bio.label(ax, (8.6, yA + 2.15), "exogenous guanosine\nin its binding pocket", size="tiny", color=P.muted())
nucleophile((8.26, yA + 1.2), "3′-OH", dy=-0.45)
bio.arrow(ax, (8.1, yA + 1.0), (3.5, yA + 0.3), kind="process", bend=-0.3, color=NEG)
bio.label(ax, (5.6, yA + 0.95), "attack on the 5′ splice site", size="tiny", color=NEG)
metals([(2.6, yA - 0.62), (4.0, yA - 0.62)])
bio.label(ax, (3.3, yA - 1.2), "two metal ions", size="tiny", color=P.muted())

# ----------------------------------------------------------------- B: group II / spliceosome
bio.panel(ax, "B", (12.9, 12.4))
bio.label(ax, (15.8, 12.4), "Group II intron / spliceosome", size="small", bold=True, ha="left")
yB = 10.2
bio.box(ax, (14.7, yB), 2.4, 0.62, token="mrna", text="5′ exon", size="tiny", radius=0.08, zorder=8)
strandline((16.0, yB), (22.6, yB))
phosphate((16.05, yB))
ax.add_patch(bio.core.Circle((19.9, yB + 0.95), 0.26, facecolor=P.fill("highlight"),
                             edgecolor=P.edge("highlight"), lw=0.9, zorder=12))
bio.label(ax, (19.9, yB + 0.95), "A", size="tiny", bold=True, color=P.on_fill(), zorder=13)
strandline((19.2, yB), (19.9, yB + 0.72))
strandline((19.9, yB + 0.72), (20.6, yB))
bio.label(ax, (19.9, yB + 1.55), "bulged branch-point\nadenosine", size="tiny", color=P.muted())
nucleophile((19.62, yB + 0.78), "", dy=0)
bio.label(ax, (20.75, yB + 0.45), "2′-OH", size="tiny", color=P.edge("highlight"), ha="left")
bio.arrow(ax, (19.4, yB + 0.62), (16.3, yB + 0.3), kind="process", bend=-0.3, color=NEG)
bio.label(ax, (17.9, yB + 1.0), "attack → lariat", size="tiny", color=NEG)
bio.box(ax, (16.9, yB - 1.35), 3.4, 0.74, token="rrna", text="domain V  /  U6 snRNA", size="tiny", radius=0.1)
metals([(15.5, yB - 0.6), (16.9, yB - 0.6)])
bio.arrow(ax, (16.9, yB - 0.98), (16.9, yB - 0.78), kind="link", color=P.muted())
bio.label(ax, (20.5, yB - 1.35), "same geometry,\nsame chemistry", size="tiny", color=P.muted(), ha="left")

# ----------------------------------------------------------------- C: RNase P
bio.panel(ax, "C", (0.1, 6.2))
bio.label(ax, (3.0, 6.2), "RNase P", size="small", bold=True, ha="left")
yC = 3.4
# pre-tRNA: acceptor stem as a paired duplex with a CCA end, plus the 5' leader to be removed
pairs(5.0, 8.4, yC + 1.1, n=7, h=0.5)
bio.label(ax, (9.3, yC + 1.1), "CCA", size="tiny", bold=True, color=P.edge("trna"))
bio.label(ax, (6.7, yC + 2.0), "acceptor stem of the pre-tRNA", size="tiny", color=P.muted())
strandline((1.4, yC + 1.1), (4.8, yC + 1.1), token="mrna")
bio.label(ax, (2.6, yC + 1.55), "5′ leader", size="tiny", color=P.edge("mrna"))
phosphate((4.85, yC + 1.1))
bio.molecule(ax, (4.85, yC - 0.5), token="neutral", text="H$_2$O", r=0.33, size="tiny")
nucleophile((4.85, yC - 0.17), "", dy=0)
bio.arrow(ax, (4.85, yC - 0.17), (4.85, yC + 0.85), kind="process", color=NEG)
metals([(3.9, yC + 0.25)], names=("Mg",))
bio.label(ax, (2.6, yC - 0.5), "metal-activated\nwater", size="tiny", color=P.muted())
bio.box(ax, (7.0, yC - 1.3), 5.0, 0.74, token="rna", text="M1 RNA reads shape, not sequence", size="tiny", radius=0.1)

# ----------------------------------------------------------------- D: peptidyl transferase centre
bio.panel(ax, "D", (12.9, 6.2))
bio.label(ax, (15.8, 6.2), "Peptidyl transferase centre", size="small", bold=True, ha="left")
yD = 3.4
bio.shape(ax, bio.blob((18.9, yD + 0.4), 4.3, 2.5, wobble=0.05, seed=3), token="rrna", alpha=0.35, zorder=2)
bio.label(ax, (18.9, yD + 2.5), "23S rRNA", size="tiny", color=P.edge("rrna"))
# P-site peptidyl-tRNA (left) and A-site aminoacyl-tRNA (right)
for x, tok, lab in ((16.9, "trna", "P site"), (20.9, "trna", "A site")):
    strandline((x, yD + 1.6), (x, yD + 0.55), token=tok)
    bio.label(ax, (x, yD + 2.0), lab, size="tiny", color=P.edge(tok))
    bio.label(ax, (x + 0.55, yD + 1.0), "A76", size="tiny", color=P.muted(), ha="left")
bio.molecule(ax, (16.9, yD + 0.2), token="protein", text="", r=0.3, size="tiny")
bio.label(ax, (15.3, yD + 0.1), "peptide\nester", size="tiny", color=P.muted())
bio.molecule(ax, (20.9, yD + 0.2), token="metabolite", text="", r=0.3, size="tiny")
bio.label(ax, (22.2, yD + 0.2), "α-NH$_2$ of the\nnew amino acid", size="tiny", color=P.muted(), ha="left")
bio.arrow(ax, (20.6, yD + 0.0), (17.2, yD - 0.02), kind="process", bend=0.25, color=NEG)
bio.label(ax, (18.9, yD - 0.95), "attack on the ester carbonyl: a carbon centre", size="tiny", color=NEG)
nucleophile((16.68, yD + 0.62), "", dy=0)
bio.callout(ax, (16.6, yD + 0.62), (15.4, yD + 1.8), "2′-OH of A76\nshuttles the proton")
bio.label(ax, (18.9, yD - 1.75), "catalysis by positioning; no protein side chain reaches the site",
          size="tiny", color=P.muted())
