"""Fates of a duplicated gene with two enhancers (tissue 1, tissue 2) and a coding region: after the
duplication the copies are redundant; nonfunctionalization (a null mutation silences one copy),
neofunctionalization (one copy gains a new function), subfunctionalization (complementary loss of one
enhancer in each copy, the DDC model)."""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 11.5)
CROSS = P.edge("negative")


def gene(x, y, e1=True, e2=True, cds=True, new=False, dead=False):
    """Enhancer 1 (blue), enhancer 2 (orange), coding region; optional new function and null mutation."""
    ax.plot([x, x + 4.6], [y, y], color=P.muted(), lw=1.0, zorder=4)
    for k, (ok, tok) in enumerate(((e1, "dna"), (e2, "rna"))):
        cx = x + 0.45 + 0.95 * k
        if ok:
            bio.box(ax, (cx, y), 0.7, 0.42, tok, radius=0.08, lw=0.7)
        else:
            bio.box(ax, (cx, y), 0.7, 0.42, "neutral", radius=0.08, lw=0.5)
            ax.plot([cx - 0.25, cx + 0.25], [y - 0.18, y + 0.18], color=CROSS, lw=1.1, zorder=14)
            ax.plot([cx - 0.25, cx + 0.25], [y + 0.18, y - 0.18], color=CROSS, lw=1.1, zorder=14)
    bio.box(ax, (x + 3.3, y), 2.2, 0.5, "neutral" if dead else "protein", radius=0.08, lw=0.8)
    if dead:
        ax.plot([x + 2.9, x + 3.7], [y - 0.25, y + 0.25], color=CROSS, lw=1.4, zorder=14)
        ax.plot([x + 2.9, x + 3.7], [y + 0.25, y - 0.25], color=CROSS, lw=1.4, zorder=14)
    if new:
        ax.plot([x + 4.3], [y + 0.45], marker="*", ms=11, color=P.edge("positive"), zorder=15)


# ancestral gene and the duplication
bio.label(ax, (2.6, 10.9), "ancestral gene", size="small", bold=True)
gene(0.3, 10.2)
bio.arrow(ax, (5.2, 10.2), (6.6, 10.2), kind="process")
bio.label(ax, (5.9, 10.65), "duplication", size="tiny", color=P.muted())
bio.label(ax, (9.3, 10.9), "redundant copies", size="small", bold=True)
gene(7.0, 10.4)
gene(7.0, 9.7)
# legend
lx = 14.0
bio.box(ax, (lx, 10.6), 0.7, 0.42, "dna", radius=0.08, lw=0.7)
bio.label(ax, (lx + 0.5, 10.6), "enhancer, tissue 1", size="tiny", ha="left")
bio.box(ax, (lx, 10.0), 0.7, 0.42, "rna", radius=0.08, lw=0.7)
bio.label(ax, (lx + 0.5, 10.0), "enhancer, tissue 2", size="tiny", ha="left")
bio.box(ax, (lx + 5.2, 10.6), 1.2, 0.42, "protein", radius=0.08, lw=0.7)
bio.label(ax, (lx + 6.0, 10.6), "coding region", size="tiny", ha="left")
ax.plot([lx + 5.2], [10.0], marker="*", ms=11, color=P.edge("positive"))
bio.label(ax, (lx + 6.0, 10.0), "new function", size="tiny", ha="left")

cols = [(0.6, "Nonfunctionalization", "one copy silenced: pseudogene", dict(dead=True), {}),
        (8.6, "Neofunctionalization", "one copy gains a new function", {}, dict(new=True)),
        (16.6, "Subfunctionalization (DDC)", "each copy keeps one function;\nboth now required", dict(e2=False),
         dict(e1=False))]
for x, title, note, a, b in cols:
    bio.arrow(ax, (9.3, 9.2), (x + 2.3, 7.9), kind="process", bend=0.0, shrink=0.1)
    bio.label(ax, (x + 2.3, 7.4), title, size="small", bold=True)
    gene(x, 6.4, **a)
    gene(x, 5.4, **b)
    bio.label(ax, (x + 2.3, 4.4), note, size="tiny", color=P.muted(), va="top")

bio.label(ax, (12.0, 2.6), "Probability of each fate depends on which mutation comes first: null mutations of the coding region "
          "lead to loss,\nrare gain-of-function mutations to neofunctionalization, complementary enhancer losses to "
          "subfunctionalization (Formula 18.2.1)", size="tiny", color=P.muted())
