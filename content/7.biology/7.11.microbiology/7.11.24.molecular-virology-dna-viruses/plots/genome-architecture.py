# Architectures of DNA virus genomes: what the ends look like and how the strands are arranged.
# Six panels, each drawn natively: circular dsDNA minichromosome (polyomavirus), linear duplex with
# inverted terminal repeats and a terminal protein (adenovirus), large duplex with internal and terminal
# repeats and three origins (herpesvirus), duplex closed by terminal hairpin loops (poxvirus), linear
# single strand with T-shaped self-priming ends (parvovirus), gapped circle (hepadnavirus).
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(18, 10.4)
LW = 2.0


def duplex(y, x0, x1, tok_top="dna", tok_bot="dna2", lw=LW):
    ax.plot([x0, x1], [y + 0.16, y + 0.16], color=P.edge(tok_top), lw=lw, solid_capstyle="round", zorder=6)
    ax.plot([x0, x1], [y - 0.16, y - 0.16], color=P.edge(tok_bot), lw=lw, solid_capstyle="round", zorder=6)


def seg(x0, x1, y, h, tok, text=None, size="tiny"):
    bio.box(ax, ((x0 + x1) / 2, y), x1 - x0, h, tok, text=text, radius=0.06, size=size, zorder=8)


def ring(center, r, tok, lw=LW, dash=False, t0=0.0, t1=2 * np.pi):
    t = np.linspace(t0, t1, 400)
    ax.plot(center[0] + r * np.cos(t), center[1] + r * np.sin(t), color=P.edge(tok), lw=lw,
            solid_capstyle="round", ls="--" if dash else "-", zorder=6)


def title(xy, text):
    bio.label(ax, xy, text, size="title", bold=True)


def note(xy, text, ha="center"):
    bio.label(ax, xy, text, size="tiny", color=P.muted(), ha=ha)


# --- A  polyomavirus: circular dsDNA minichromosome -------------------------------------------------------
bio.panel(ax, "A", (0.1, 10.2))
title((2.7, 9.9), "Polyomavirus, 5 kbp")
c = (2.7, 7.9)
ring(c, 1.15, "dna")
ring(c, 1.0, "dna2")
for k in range(9):  # nucleosomes of the minichromosome
    a = 2 * np.pi * k / 9 + 0.25
    bio.protein(ax, (c[0] + 1.08 * np.cos(a), c[1] + 1.08 * np.sin(a)), 0.3, 0.3, "chromatin", zorder=9)
bio.callout(ax, (c[0] + 1.08, c[1]), (5.0, 8.35), "Ori")
bio.callout(ax, (c[0] - 0.4, c[1] + 1.0), (0.3, 9.1), "Nucleosome")
note((2.7, 6.35), "circular; no ends to lose")

# --- B  adenovirus: protein-linked linear duplex -----------------------------------------------------------
bio.panel(ax, "B", (6.1, 10.2))
title((9.0, 9.9), "Adenovirus, 36 kbp")
y = 8.0
duplex(y, 6.9, 11.1)
seg(6.9, 7.6, y, 0.72, "highlight", "ITR")
seg(10.4, 11.1, y, 0.72, "highlight", "ITR")
for x, yy in ((6.9, y + 0.16), (11.1, y - 0.16)):
    bio.protein(ax, (x, yy), 0.42, 0.42, "enzyme", zorder=10)
bio.callout(ax, (6.9, y + 0.16), (7.2, 9.2), "Terminal protein (5′)")
bio.label(ax, (6.55, y + 0.16), "5′", size="tiny")
bio.label(ax, (6.55, y - 0.16), "3′", size="tiny")
bio.label(ax, (11.45, y + 0.16), "3′", size="tiny")
bio.label(ax, (11.45, y - 0.16), "5′", size="tiny")
note((9.0, 6.35), "two identical origins, one at each end")

# --- C  herpesvirus: repeats and three origins -------------------------------------------------------------
bio.panel(ax, "C", (12.1, 10.2))
title((15.1, 9.9), "Herpesvirus, 150 kbp")
y = 8.0
duplex(y, 12.4, 17.8)
for x0, x1, tok, txt in ((12.4, 12.9, "highlight", "TR"), (14.6, 15.1, "highlight", "IR"),
                         (15.3, 15.8, "highlight", "IR"), (17.3, 17.8, "highlight", "TR")):
    seg(x0, x1, y, 0.72, tok, txt)
bio.label(ax, (13.75, y + 0.62), "U$_L$", size="small")
bio.label(ax, (16.55, y + 0.62), "U$_S$", size="small")
for x, t in ((13.9, "OriL"), (15.2, "OriS"), (16.9, "OriS")):
    ax.plot([x, x], [y - 0.55, y - 0.95], color=P.edge("positive"), lw=1.6, zorder=9)
    bio.label(ax, (x, y - 1.2), t, size="tiny", color=P.edge("positive"))
note((15.1, 6.35), "unique regions between inverted repeats")

# --- D  poxvirus: hairpin ends ------------------------------------------------------------------------------
bio.panel(ax, "D", (0.1, 4.8))
title((2.7, 4.5), "Poxvirus, 200 kbp")
y = 2.7
duplex(y, 1.1, 4.3)
for x, t0, t1 in ((1.1, np.pi / 2, 3 * np.pi / 2), (4.3, -np.pi / 2, np.pi / 2)):
    t = np.linspace(t0, t1, 120)  # a semicircle joining the two strands into one molecule
    ax.plot(x + 0.16 * np.cos(t), y + 0.16 * np.sin(t), color=P.edge("dna"), lw=LW, zorder=6)
seg(1.35, 1.95, y, 0.72, "highlight", "ITR")
seg(3.45, 4.05, y, 0.72, "highlight", "ITR")
bio.callout(ax, (4.46, y), (4.6, 3.9), "Terminal loop: the\ntwo strands are\none molecule")
note((2.7, 1.1), "replicated in cytoplasmic factories")

# --- E  parvovirus: single strand with T-shaped ends -------------------------------------------------------
bio.panel(ax, "E", (6.1, 4.8))
title((9.0, 4.5), "Parvovirus, 5 kb")
y = 2.7
ax.plot([7.4, 10.6], [y, y], color=P.edge("dna"), lw=LW, solid_capstyle="round", zorder=6)


def tee(x, s):
    """A T-shaped hairpin at one end of the strand (s = -1 left, +1 right)."""
    ax.plot([x, x + s * 0.55], [y, y], color=P.edge("dna"), lw=LW, zorder=6)
    ax.plot([x + s * 0.55, x + s * 0.55], [y - 0.42, y + 0.42], color=P.edge("dna"), lw=LW, zorder=6)
    for dy in (-0.42, 0.42):
        ax.plot([x + s * 0.55, x + s * 0.2], [y + dy, y + dy], color=P.edge("dna"), lw=LW, zorder=6)
    for k in range(4):  # base pairs in the stem
        ax.plot([x + s * (0.1 + 0.11 * k)] * 2, [y - 0.07, y + 0.07], color=P.edge("dna2"), lw=1.0, zorder=7)


tee(7.4, -1)
tee(10.6, 1)
bio.callout(ax, (6.85, y + 0.42), (8.4, 4.05), "Palindromic end folds back:\na free 3′-OH primer")
note((9.0, 1.1), "single-stranded; both polarities packaged")

# --- F  hepadnavirus: gapped circle ------------------------------------------------------------------------
bio.panel(ax, "F", (12.1, 4.8))
title((15.1, 4.5), "Hepadnavirus, 3.2 kbp")
c = (15.1, 2.6)
ring(c, 1.1, "dna")                                   # complete (-) strand
ring(c, 0.92, "dna2", t0=-0.35 * np.pi, t1=0.75 * np.pi)   # incomplete (+) strand
bio.protein(ax, (c[0] + 1.1 * np.cos(0.78 * np.pi), c[1] + 1.1 * np.sin(0.78 * np.pi)), 0.42, 0.42, "enzyme", zorder=10)
bio.callout(ax, (c[0] + 1.1 * np.cos(0.78 * np.pi), c[1] + 1.1 * np.sin(0.78 * np.pi)), (13.4, 3.3),
            "P protein on\nthe 5′ (−) end")
t = np.linspace(0.75 * np.pi, 0.95 * np.pi, 40)
ax.plot(c[0] + 0.92 * np.cos(t), c[1] + 0.92 * np.sin(t), color=P.edge("rna"), lw=2.6, zorder=8)
bio.callout(ax, (c[0] + 0.92 * np.cos(0.88 * np.pi), c[1] + 0.92 * np.sin(0.88 * np.pi)), (17.0, 3.95),
            "Capped RNA on\nthe 5′ (+) end")
bio.callout(ax, (c[0] + 0.92 * np.cos(-0.2 * np.pi), c[1] + 0.92 * np.sin(-0.2 * np.pi)), (17.2, 1.8), "Gap")
note((15.1, 1.1), "made by reverse transcription (§25.7)")
