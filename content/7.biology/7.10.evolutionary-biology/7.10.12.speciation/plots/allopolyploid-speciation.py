"""Speciation by allopolyploidy, after the goatsbeards Tragopogon in North America (chromosome numbers from
Futuyma and Kirkpatrick 2017): the diploids T. dubius and T. pratensis (both n = 6) hybridized, and genome
doubling in the hybrid produced the allotetraploid T. miscellus (n = 12, 2n = 24). Bars are chromosome sets
(one bar per haploid set of 6; colours: parental genome of origin). The diploid F1 hybrid is largely sterile
because the two sets of chromosomes are not homologous enough to pair regularly at meiosis; after doubling, each
chromosome has a partner and meiosis is regular. A cross between the tetraploid and either diploid parent gives a
triploid (one set from the diploid, two from the tetraploid), which is largely sterile: the tetraploid is
reproductively isolated from its parents from its origin."""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

import wikibio as bio

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(22, 9.5)


def plant(x, y, sets, name, sub, w=3.6, italic=True):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - 1.0), w, 2.0, boxstyle="round,pad=0.05,rounding_size=0.2",
                                facecolor=P.surface(), edgecolor=P.muted(), lw=1.0, zorder=4))
    n = len(sets)
    for i, tok in enumerate(sets):
        bx = x - 0.25 * (n - 1) + 0.5 * i
        for j in range(6):
            ax.plot([bx - 0.13 + 0.05 * (j % 2), bx - 0.13 + 0.05 * (j % 2)], [y - 0.55 + 0.17 * j, y - 0.45 + 0.17 * j],
                    color=P.edge(tok), lw=2.2, solid_capstyle="round", zorder=6)
        ax.add_patch(FancyBboxPatch((bx - 0.2, y - 0.65), 0.4, 1.12, boxstyle="round,pad=0.02,rounding_size=0.1",
                                    facecolor=P.fill(tok), edgecolor="none", alpha=0.35, zorder=5))
    bio.label(ax, (x, y + 1.35), name, size="small", italic=italic)
    bio.label(ax, (x, y - 1.4), sub, size="tiny", color=P.muted())


plant(3.5, 7.2, ["dna", "dna"], "T. dubius", "diploid, 2n = 12")
plant(18.5, 7.2, ["rna", "rna"], "T. pratensis", "diploid, 2n = 12")
plant(11, 7.2, ["dna", "rna"], "F$_1$ hybrid", "2n = 12, sets not homologous: sterile", italic=False)
plant(11, 2.5, ["dna", "dna", "rna", "rna"], "T. miscellus", "allotetraploid, 2n = 24: fertile")
plant(3.5, 2.5, ["dna", "dna", "rna"], "backcross", "triploid, 2n = 18: sterile", italic=False)
bio.arrow(ax, (5.4, 7.2), (9.1, 7.2), kind="process", head=0.2)
bio.arrow(ax, (16.6, 7.2), (12.9, 7.2), kind="process", head=0.2)
bio.arrow(ax, (11, 5.45), (11, 4.15), kind="process", head=0.2)
bio.label(ax, (12.9, 4.8), "genome doubling", size="tiny", color=P.muted())
bio.arrow(ax, (9.1, 2.5), (5.4, 2.5), kind="process", head=0.2, dashed=True)
bio.arrow(ax, (3.5, 5.45), (3.5, 4.15), kind="process", head=0.2, dashed=True)
bio.label(ax, (7.25, 3.05), "cross with\na parent", size="tiny", color=P.muted())
