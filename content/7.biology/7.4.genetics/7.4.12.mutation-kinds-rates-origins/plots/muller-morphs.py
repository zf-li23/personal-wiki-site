"""Muller's (1932) classes of mutant alleles placed on a scale of gene activity, relative to the wild type (1).
Amorph (null): no activity. Hypomorph: reduced activity. Hypermorph: increased activity of the normal kind.
Antimorph (dominant negative): the product antagonizes the wild-type product, so the activity of a heterozygote is
below that of a null heterozygote (drawn below zero). Neomorph: a new activity or ectopic expression, off the
scale of the normal function. Below the scale: typical dominance in a heterozygote with the wild-type allele."""

from matplotlib.patches import Rectangle

import wikibio as bio

P = bio.P

fig, ax = bio.canvas(18.0, 6.6)
y = 3.3
x0, x1 = 3.0, 15.0


def X(v):  # activity -0.5 .. 2.0 mapped to the scale
    return x0 + (v + 0.5) / 2.5 * (x1 - x0)


bio.arrow(ax, (X(-0.5), y), (X(2.05), y), kind="process", color=P.muted())
for v, lab in ((0, "0"), (1, "1 (wild type)"), (2, "2")):
    ax.plot([X(v), X(v)], [y - 0.12, y + 0.12], color=P.muted(), lw=1.0)
    bio.label(ax, (X(v), y - 0.42), lab, size="tiny", color=P.muted())
bio.label(ax, (X(2.05) + 0.2, y), "gene activity", size="small", ha="left")
ax.add_patch(Rectangle(
    (X(-0.5), y - 0.08), X(0) - X(-0.5), 0.16, facecolor=P.light("negative"), edgecolor="none", zorder=2))

items = [
    (-0.4, "antimorph", "dominant negative", "dominant", "negative"),
    (0.0, "amorph", "null allele", "recessive (or haplo-\ninsufficient)", "neutral"),
    (0.45, "hypomorph", "reduced function", "recessive or\nsemidominant", "channel"),
    (1.0, "wild type", "", "", "positive"),
    (1.7, "hypermorph", "increased function", "dominant", "highlight"),
]
for v, name, sub, dom, tok in items:
    bio.box(ax, (X(v), y + 1.2), 1.7, 0.75, token=tok, text=name, size="small")
    ax.plot([X(v), X(v)], [y + 0.82, y + 0.1], color=P.edge(tok), lw=1.0)
    ax.plot([X(v)], [y], "o", color=P.edge(tok), ms=5, zorder=5)
    if sub:
        bio.label(ax, (X(v), y + 1.95), sub, size="tiny")
    if dom:
        bio.label(ax, (X(v), y - 1.2), dom, size="tiny", color=P.ink())
bio.label(ax, (1.5, y - 1.2), "in a heterozygote:", size="tiny", ha="center", color=P.muted())
bio.box(ax, (X(1.0), 6.05), 2.6, 0.7, token="drug", text="neomorph", size="small")
bio.label(ax, (X(1.0) + 1.5, 6.05), "new function or ectopic expression\n(off the scale): dominant", size="tiny",
          ha="left")
bio.label(ax, (9.0, 0.6), "loss of function  <-  wild type  ->  gain of function", size="small")
