"""A: the life cycle of a mushroom-forming basidiomycete (Agaricomycetes, schematic). Haploid basidiospores
germinate into monokaryotic (primary) mycelia; plasmogamy between compatible mycelia gives a dikaryotic
(secondary) mycelium, in which every cell has two nuclei, one from each parent, kept paired by clamp
connections; the dikaryon grows for months or years and forms the basidiocarp; karyogamy in the young basidium
gives the only diploid nucleus, which undergoes meiosis at once to give four basidiospores.
B: a clamp connection: the two nuclei of the apical cell divide at the same time, one of them inside a backward
hook (the clamp); septa then separate the products, and the clamp fuses with the cell behind, so that each cell
again receives one nucleus of each mating type."""
import numpy as np
from matplotlib.patches import Ellipse, FancyBboxPatch, Arc
import wikibio as bio
from wikibio import ecology as E

P = bio.P
fig, ax = bio.canvas(27, 13)
steps = [dict(text="basidiospores (n)", shape="box", token="rna"),
         dict(text="monokaryotic\nmycelia (n)", shape="box", token="rna"),
         dict(text="dikaryotic mycelium\n(n + n), clamps", shape="box", token="highlight"),
         dict(text="basidiocarp", icon="phylopic/agaricus", icon_size=1.6, shape="none"),
         dict(text="young basidium:\nkaryogamy (2n)", shape="box", token="dna")]
E.cycle(ax, (8.0, 6.4), 4.6, steps, start=90, clockwise=True, size="small", label_size="tiny",
        arrow_labels=["germination", "plasmogamy", "growth", "gills, hymenium", "meiosis"],
        sectors=[dict(start=-0.5, end=1.5, token="rna", text="haploid", r0=1.2, r1=6.2),
                 dict(start=1.5, end=3.5, token="highlight", text="dikaryotic", r0=1.2, r1=6.2),
                 dict(start=3.5, end=4.5, token="dna", text="diploid", r0=1.2, r1=6.2)])
bio.panel(ax, "A", (0.2, 12.8))

# B: clamp connection in three stages
bio.panel(ax, "B", (16.6, 12.8))
W = "cell_wall"


def cell_row(y, stage):
    ax.add_patch(FancyBboxPatch((17.4, y - 0.4), 8.4, 0.8, boxstyle="round,pad=0,rounding_size=0.38",
                                facecolor=P.fill("cytoplasm"), edgecolor=P.edge(W), lw=1.4, zorder=4))
    ax.plot([18.6, 18.6], [y - 0.4, y + 0.4], color=P.edge(W), lw=1.6, zorder=5)
    if stage == 0:
        nuc = [(22.0, "rna"), (23.2, "dna")]
        ax.add_patch(Arc((21.4, y + 0.4), 1.6, 1.4, theta1=0, theta2=180, color=P.edge(W), lw=1.4, zorder=5))
        bio.label(ax, (21.4, y + 1.35), "clamp forms", size="tiny", color=P.muted())
    elif stage == 1:
        nuc = [(20.7, "rna"), (22.4, "rna"), (24.6, "dna"), (21.1, "dna")]
        ax.add_patch(Arc((21.4, y + 0.4), 1.6, 1.4, theta1=0, theta2=180, color=P.edge(W), lw=1.4, zorder=5))
        bio.label(ax, (21.4, y + 1.35), "synchronous mitosis", size="tiny", color=P.muted())
    else:
        nuc = [(19.6, "rna"), (20.4, "dna"), (23.0, "rna"), (24.6, "dna")]
        ax.add_patch(Arc((21.4, y + 0.4), 1.6, 1.4, theta1=0, theta2=180, color=P.edge(W), lw=1.4, zorder=5))
        ax.plot([22.0, 22.0], [y - 0.4, y + 0.4], color=P.edge(W), lw=1.6, zorder=5)
        bio.label(ax, (21.4, y + 1.35), "septa; clamp fuses backward", size="tiny", color=P.muted())
    for (x, tok) in nuc:
        yy = y + 0.75 if (stage == 1 and tok == "dna" and x < 22) else y
        ax.add_patch(Ellipse((x, yy), 0.5, 0.36, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=7))


for k, y in enumerate((10.2, 6.6, 3.0)):
    cell_row(y, k)
bio.arrow(ax, (26.3, 3.0), (26.9, 3.0), kind="process", head=0.15)
bio.label(ax, (21.6, 1.2), "each cell: one nucleus of each mating type", size="tiny", color=P.muted())
