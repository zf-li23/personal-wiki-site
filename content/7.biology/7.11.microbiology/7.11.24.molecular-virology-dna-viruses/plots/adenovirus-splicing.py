# Alternative processing of adenovirus pre-mRNA.
# A: one promoter, one long primary transcript carrying the tripartite leader, five poly(A) sites and many
#    3' splice sites; each mature mRNA has the same leader and a different body (L1-L5 families).
# B: the immediate-early E1A unit: alternative 5' splice sites within one coding sequence give the 13S, 12S
#    and 9S mRNAs, whose products differ in regulatory function.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(17, 9.4)
LW = 2.0


def line(x0, x1, y, tok="dna", lw=LW, dashed=False, zorder=6):
    col = P.muted() if tok == "muted" else P.edge(tok)
    ax.plot([x0, x1], [y, y], color=col, lw=lw, ls="--" if dashed else "-",
            solid_capstyle="round", zorder=zorder)


def exon(x0, x1, y, tok="rna", h=0.3, text=None):
    bio.box(ax, ((x0 + x1) / 2, y), x1 - x0, h, tok, text=text, radius=0.04, size="tiny", zorder=9)


def caret(x0, x1, y, h=0.3, tok="muted"):
    """An intron drawn as a caret between two exons."""
    xm = (x0 + x1) / 2
    col = P.muted() if tok == "muted" else P.edge(tok)
    ax.plot([x0, xm, x1], [y, y + h, y], color=col, lw=1.1, zorder=8)


# --- A  the major late transcription unit ------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 8.8))
bio.label(ax, (8.5, 8.65), "Adenovirus major late transcription unit", size="title", bold=True)
y = 7.5
line(1.0, 15.8, y, "dna", lw=2.4)
bio.label(ax, (1.0, y + 0.55), "MLP", size="tiny", bold=True, ha="left")
ax.plot([1.0, 1.0, 1.35], [y, y + 0.38, y + 0.38], color=P.edge("positive"), lw=2.0, zorder=9)
ax.plot([1.35, 1.25, 1.35, 1.25], [y + 0.38, y + 0.45, y + 0.38, y + 0.31], color=P.edge("positive"), lw=2.0, zorder=9)
for x in (1.6, 2.4, 3.2):          # the three leader segments
    exon(x, x + 0.4, y, "highlight")
bio.label(ax, (2.6, y - 0.55), "tripartite leader", size="tiny", color=P.edge("highlight"))
for i, (x0, name) in enumerate([(5.0, "L1"), (7.2, "L2"), (9.4, "L3"), (11.6, "L4"), (13.8, "L5")]):
    exon(x0, x0 + 1.3, y, "virus", text=name)
    ax.plot([x0 + 1.45, x0 + 1.45], [y - 0.42, y + 0.42], color=P.edge("rna"), lw=1.6, ls=":", zorder=9)
    bio.label(ax, (x0 + 1.45, y + 0.62), "pA", size="tiny", color=P.edge("rna"))
bio.label(ax, (8.5, 6.55), "one primary transcript: choice of poly(A) site and of 3′ splice site makes about twenty mRNAs",
          size="small", color=P.muted())

for k, (name, body, bx) in enumerate([("L1 mRNA", "L1", 5.0), ("L3 mRNA (hexon)", "L3", 9.4), ("L5 mRNA (fibre)", "L5", 13.8)]):
    yy = 5.85 - 0.95 * k
    for j, x in enumerate((1.6, 2.4, 3.2)):
        exon(x, x + 0.4, yy, "highlight")
        if j < 2:
            caret(x + 0.4, x + 0.8, yy, 0.22)
    caret(3.6, bx, yy, 0.3)
    exon(bx, bx + 1.3, yy, "virus", text=body)
    bio.label(ax, (bx + 1.5, yy), "AAAA", size="tiny", bold=True, ha="left")
    bio.label(ax, (0.95, yy), name, size="tiny", ha="right")

# --- B  the E1A unit ----------------------------------------------------------------------------------------
bio.panel(ax, "B", (0.1, 3.25))
bio.label(ax, (4.6, 3.1), "The E1A unit: one gene, three mRNAs", size="title", bold=True)
y = 2.35
exon(1.2, 5.6, y, "positive")
exon(6.2, 7.6, y, "positive")
line(5.6, 6.2, y, "muted", lw=1.0)
bio.label(ax, (1.2, y + 0.45), "E1A coding sequence", size="tiny", ha="left")
for k, (name, cut, note) in enumerate([("13S", 4.9, "activates transcription"), ("12S", 3.9, "binds Rb, no activation domain"),
                                       ("9S", 2.4, "made late")]):
    yy = 1.55 - 0.5 * k
    exon(1.2, cut, yy, "positive")
    caret(cut, 6.2, yy, 0.2)
    exon(6.2, 7.6, yy, "positive")
    bio.label(ax, (0.95, yy), name, size="tiny", ha="right")
    bio.label(ax, (7.85, yy), note, size="tiny", color=P.muted(), ha="left")
bio.label(ax, (4.4, 0.15), "the 5′ splice site chosen determines which part of the protein is kept",
          size="small", color=P.muted())

# --- the discovery, as a note --------------------------------------------------------------------------------
bio.label(ax, (13.0, 2.7), "Electron microscopy of mRNA–DNA hybrids (1977)", size="small", bold=True)
bio.label(ax, (13.0, 2.1), "showed three loops of unhybridized DNA between\nthe 5′ end of a late mRNA and its body:\nmRNA is assembled from separated pieces.",
          size="tiny", color=P.muted())
hx, hy = 10.6, 0.9
pts = np.array([(hx, hy), (hx + 0.5, hy), (hx + 1.1, hy + 0.45), (hx + 1.7, hy), (hx + 2.2, hy),
                (hx + 2.9, hy + 0.5), (hx + 3.6, hy), (hx + 4.1, hy), (hx + 4.8, hy + 0.55), (hx + 5.5, hy), (hx + 6.0, hy)])
ax.plot(pts[:, 0], pts[:, 1], color=P.edge("dna"), lw=1.6, zorder=8)
for a, b in ((hx, hx + 0.5), (hx + 1.7, hx + 2.2), (hx + 3.6, hx + 4.1), (hx + 5.5, hx + 6.0)):
    ax.plot([a, b], [hy, hy], color=P.edge("rna"), lw=3.0, solid_capstyle="round", zorder=9)
bio.label(ax, (13.6, 0.3), "RNA–DNA hybrid (thick) and looped-out DNA", size="tiny", color=P.muted())
