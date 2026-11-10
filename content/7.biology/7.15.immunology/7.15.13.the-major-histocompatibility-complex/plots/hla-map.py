# The human MHC (HLA complex) on chromosome 6p21.3 and the mouse H-2 complex on chromosome 17.
# Gene positions are approximate GRCh37 coordinates (Mb) and are drawn to scale along the human bar;
# the mouse bar is a schematic of region order only. The telomere of 6p is on the left, the
# centromere on the right, so the order reads class I - class III - class II.
import numpy as np
from matplotlib.patches import FancyBboxPatch

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 9.4)

X0, X1 = 1.2, 23.0          # canvas x of the bar ends
MB0, MB1 = 29.55, 33.15     # Mb shown


def X(mb):
    return X0 + (mb - MB0) / (MB1 - MB0) * (X1 - X0)


y = 6.0
regions = [("Class I region", 29.55, 31.50, "protein"), ("Class III region", 31.50, 32.40, "antibody"),
           ("Class II region", 32.40, 33.15, "enzyme")]
for name, a, b, tok in regions:
    ax.add_patch(FancyBboxPatch((X(a), y - 0.3), X(b) - X(a), 0.6, boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=P.light(tok), edgecolor=P.edge(tok), lw=1.0, zorder=5))
    bio.label(ax, ((X(a) + X(b)) / 2, y + 2.0), name, size="small", bold=True, color=P.edge(tok))

# genes above the bar: classical (bold) and nonclassical class I, MIC; below: class III and class II
above = [("HLA-F", 29.69, False), ("HLA-G", 29.79, False), ("HLA-A", 29.91, True), ("HLA-E", 30.46, False),
         ("HLA-C", 31.24, True), ("HLA-B", 31.32, True), ("MICA", 31.37, False), ("MICB", 31.47, False)]
cls3 = [("TNF", 31.54), ("LTA", 31.53), ("HSPA1A", 31.78), ("C2", 31.87), ("CFB", 31.91), ("C4A", 31.95),
        ("C4B", 31.99), ("CYP21A2", 32.01)]
cls2 = [("HLA-DRA", 32.41, True), ("HLA-DRB1", 32.55, True), ("HLA-DQA1", 32.61, True), ("HLA-DQB1", 32.63, True),
        ("HLA-DOB", 32.78, False), ("TAP2", 32.79, False), ("PSMB8", 32.81, False), ("TAP1", 32.82, False),
        ("PSMB9", 32.83, False), ("HLA-DMB", 32.90, False), ("HLA-DMA", 32.92, False), ("HLA-DOA", 32.97, False),
        ("HLA-DPA1", 33.03, True), ("HLA-DPB1", 33.04, True)]


def spread(xs, gap):
    """Shift label positions apart (keeping order) so neighbouring labels do not overlap."""
    xs = list(xs)
    for _ in range(200):
        moved = False
        for i in range(1, len(xs)):
            if xs[i] - xs[i - 1] < gap:
                d = (gap - (xs[i] - xs[i - 1])) / 2
                xs[i - 1] -= d
                xs[i] += d
                moved = True
        if not moved:
            break
    return xs


def gene_row(genes, side, tok_of, gap, lift):
    gx = [X(g[1]) for g in genes]
    lx = spread(gx, gap)
    for g, x, xl in zip(genes, gx, lx):
        name, classical = g[0], (g[2] if len(g) > 2 else False)
        tok = tok_of(name)
        ax.plot([x, x], [y - 0.3, y + 0.3], color=P.edge(tok), lw=2.4 if classical else 1.4, zorder=7,
                solid_capstyle="butt")
        yl = y + side * lift
        ax.plot([x, xl], [y + side * 0.32, yl - side * 0.12], color=P.muted(), lw=0.6, zorder=6)
        bio.label(ax, (xl, yl), name, size="tiny", rotation=60 if side > 0 else -60,
                  ha="left" if side > 0 else "left", va="bottom" if side > 0 else "top", bold=classical,
                  color=P.ink() if classical else P.muted())


gene_row(above, +1, lambda n: "protein", 0.62, 0.75)
gene_row([(n, p, False) for n, p in sorted(cls3, key=lambda t: t[1])], -1, lambda n: "antibody", 0.62, 0.75)
gene_row(cls2, -1, lambda n: "enzyme", 0.5, 0.75)

# Mb axis
ya = y - 3.35
ax.plot([X0, X1], [ya, ya], color=P.muted(), lw=0.8)
for mb in np.arange(29.6, 33.11, 0.4):
    ax.plot([X(mb), X(mb)], [ya, ya - 0.12], color=P.muted(), lw=0.8)
    bio.label(ax, (X(mb), ya - 0.22), f"{mb:.1f}", size="tiny", color=P.muted(), va="top")
bio.label(ax, ((X0 + X1) / 2, ya - 0.75), "Position on chromosome 6 / Mb (GRCh37)", size="small", va="top")
bio.label(ax, (X0 - 0.2, y), "6p ter", size="tiny", ha="right", color=P.muted())
bio.label(ax, (X1 + 0.2, y), "cen", size="tiny", ha="left", color=P.muted())
bio.label(ax, (0.3, 9.2), "Human HLA complex (6p21.3, ~3.6 Mb)", size="normal", bold=True, ha="left", va="top")

# legend
bio.label(ax, (16.6, 9.0), "bold: classical class I / class II genes", size="tiny", ha="left", color=P.ink())
bio.label(ax, (16.6, 8.6), "grey: nonclassical, processing and other genes", size="tiny", ha="left", color=P.muted())

# mouse H-2 schematic
ym = 0.75
bio.label(ax, (0.3, 0.75), "Mouse H-2 (chromosome 17), order only:", size="small", bold=True, ha="left")
parts = [("cen", None, 1.2), ("K", "protein", 1.4), ("I-A  I-E", "enzyme", 3.0), ("S (C4, Bf, C2, TNF)", "antibody", 4.2),
         ("D  L", "protein", 1.9), ("Q  T  M", "neutral", 2.4)]
x = 9.6
for name, tok, w in parts:
    if tok is None:
        bio.label(ax, (x, ym), name, size="tiny", color=P.muted())
        x += 0.7
        continue
    bio.box(ax, (x + w / 2, ym), w - 0.1, 0.55, tok, text=name, size="tiny", radius=0.1)
    x += w
