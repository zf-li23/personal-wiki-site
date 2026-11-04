# Expression of a coronavirus genome.
# A: the genome - ORF1a and, after a -1 ribosomal frameshift at a slippery sequence and pseudoknot, ORF1ab;
#    the polyproteins are cut by viral proteases into sixteen non-structural proteins (nsp12 polymerase,
#    nsp13 helicase, nsp14 proofreading exonuclease). B: discontinuous (-) strand synthesis at the
#    transcription-regulating sequences gives a nested set of subgenomic mRNAs, each translated from its
#    5'-most reading frame. C: the double-membrane replication organelle in which all this happens.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(17.5, 10.6)


def gene(x0, x1, y, tok, text=None, h=0.46, size="tiny"):
    bio.box(ax, ((x0 + x1) / 2, y), x1 - x0, h, tok, text=text, radius=0.05, size=size, zorder=9)


def line(x0, x1, y, tok="rna", lw=2.2, zorder=6):
    ax.plot([x0, x1], [y, y], color=P.edge(tok), lw=lw, solid_capstyle="round", zorder=zorder)


# --- A  the genome and the frameshift ---------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 10.4))
bio.label(ax, (8.6, 10.25), "Genome organization and the −1 frameshift", size="title", bold=True)
y = 9.1
line(1.0, 16.4, y)
bio.molecule(ax, (0.85, y), token="metabolite", r=0.15)
bio.label(ax, (1.0, y + 0.55), "5′ cap", size="tiny", ha="left")
bio.label(ax, (16.6, y), "AAAA", size="tiny", bold=True, ha="left")
gene(1.3, 7.0, y, "positive", "ORF1a")
gene(7.0, 11.4, y, "enzyme", "ORF1b")
for x0, x1, t in ((11.7, 13.2, "S"), (13.3, 13.9, "3a"), (14.0, 14.4, "E"), (14.5, 15.2, "M"),
                  (15.3, 15.7, "6–8"), (15.8, 16.3, "N")):
    gene(x0, x1, y, "virus", t)
ax.plot([7.0, 7.0], [y - 0.32, y - 0.75], color=P.edge("highlight"), lw=1.8, zorder=10)
bio.label(ax, (5.2, y - 1.2), "slippery sequence UUUAAAC + pseudoknot: about a quarter\nof ribosomes shift −1 and read ORF1b",
          size="tiny", color=P.muted())
bio.label(ax, (4.1, y - 0.6), "pp1a", size="tiny", color=P.edge("positive"))
bio.label(ax, (9.6, y - 0.6), "pp1ab", size="tiny", color=P.edge("enzyme"))
bio.label(ax, (14.0, y + 0.55), "structural and accessory genes", size="tiny", color=P.edge("virus"))

yn = 7.0
for x0, w, t, tok in ((1.3, 1.2, "nsp1–11", "positive"), (3.0, 1.2, "nsp12\npolymerase", "enzyme"),
                      (4.9, 1.0, "nsp13\nhelicase", "enzyme"), (6.5, 1.1, "nsp14\nExoN", "highlight"),
                      (8.3, 1.2, "nsp15–16", "enzyme")):
    gene(x0, x0 + w, yn, tok, t, h=0.8, size="tiny")
bio.arrow(ax, (10.8, 8.3), (9.9, 7.4), kind="process")
bio.label(ax, (11.0, 8.4), "cleaved by the viral proteases\nnsp3 (PL$^{\\mathrm{pro}}$) and nsp5 (M$^{\\mathrm{pro}}$)",
          size="tiny", color=P.muted(), ha="left")
bio.label(ax, (11.0, yn - 0.3), "nsp14 proofreads: the mutation rate falls 15- to 20-fold,\nwhich is what allows a 30 kb RNA genome",
          size="tiny", color=P.muted(), ha="left")

# --- B  the nested set -------------------------------------------------------------------------------------
bio.panel(ax, "B", (0.1, 6.0))
bio.label(ax, (5.4, 5.85), "Discontinuous transcription: a nested set", size="title", bold=True)
y0 = 5.1
line(1.0, 10.6, y0)
gene(1.0, 1.45, y0, "highlight", h=0.36)
bio.label(ax, (1.0, y0 + 0.45), "leader", size="tiny", color=P.edge("highlight"), ha="left")
for x in (4.4, 5.6, 6.5, 7.4, 8.6, 9.6):
    ax.plot([x, x], [y0 - 0.3, y0 + 0.3], color=P.edge("negative"), lw=1.4, zorder=10)
bio.label(ax, (7.0, y0 - 0.62), "transcription-regulating sequences", size="tiny", color=P.edge("negative"))
for k, (start, name) in enumerate([(4.4, "S"), (5.6, "3a"), (6.5, "E"), (7.4, "M"), (9.6, "N")]):
    yy = 4.0 - 0.62 * k
    gene(1.0, 1.45, yy, "highlight", h=0.32)
    ax.plot([1.45, start], [yy + 0.16, yy + 0.16], color=P.muted(), lw=0.9, ls=":", zorder=7)
    line(start, 10.6, yy, "rna", lw=1.8)
    gene(start, start + 0.9, yy, "virus", name, h=0.32)
    bio.label(ax, (10.75, yy), "AAAA", size="tiny", ha="left")
bio.label(ax, (5.4, 0.75), "the polymerase detaches at a regulating sequence and resumes at the leader, so every\nmRNA carries the same 5′ leader; only the first open reading frame of each is translated",
          size="tiny", color=P.muted())

# --- C  the replication organelle -----------------------------------------------------------------------------
bio.panel(ax, "C", (12.0, 6.0))
bio.label(ax, (14.8, 5.85), "Replication organelle", size="title", bold=True)
bio.label(ax, (14.8, 5.3), "double-membrane vesicles continuous with the ER", size="tiny", color=P.muted())
for c, r in (((13.7, 3.4), 1.05), ((15.9, 3.0), 0.8), ((15.2, 4.5), 0.55)):
    t = np.linspace(0, 2 * np.pi, 200)
    for rr in (r, r - 0.14):
        ax.plot(c[0] + rr * np.cos(t), c[1] + rr * np.sin(t), color=P.edge("er"), lw=1.8, zorder=6)
bio.label(ax, (13.7, 3.4), "dsRNA", size="tiny", color=P.edge("rna"))
bio.label(ax, (14.8, 1.85), "a pore connects the interior to the cytosol;\nthe membranes keep double-stranded RNA\naway from the innate sensors of the cell",
          size="tiny", color=P.muted())
