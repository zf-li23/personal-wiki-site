# Origin of allohexaploid bread wheat (schematic). Triticum urartu (AA) x an Aegilops speltoides-like
# goat grass (BB) gave, after chromosome doubling, wild emmer (AABB); emmer was domesticated about
# 10 000 years ago (durum wheat derives from it); cultivated emmer x Aegilops tauschii (DD) in farmers'
# fields south of the Caspian, followed by doubling, gave bread wheat (AABBDD) about 8000-9000 years ago.
from matplotlib.patches import FancyBboxPatch
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(28, 12)
G = {"A": "dna", "B": "rna", "D": "plant"}


def sp(x, y, name, genome, n2, w=5.6, it=True):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - 1.0), w, 2.0, boxstyle="round,pad=0,rounding_size=0.25",
                                fill=False, edgecolor=P.edge("neutral"), lw=1.2, zorder=5))
    bio.label(ax, (x, y + 0.55), name, size="small", italic=it)
    gx = x - 0.35 * len(genome) + 0.35
    for i, g in enumerate(genome):
        bio.box(ax, (gx + 0.7 * i, y - 0.25), 0.6, 0.6, token=G[g], text=g, size="small")
    bio.label(ax, (x, y - 0.8), f"2n = {n2}", size="tiny")
    return x, y


a = sp(3.4, 9.8, "Triticum urartu", "AA", 14)
b = sp(10.6, 9.8, r"$\it{Aegilops\ speltoides}$ (relative)", "BB", 14, w=6.6, it=False)
e = sp(7.0, 5.6, r"$\it{T.\ turgidum}$ subsp. $\it{dicoccoides}$", "AABB", 28, w=6.6, it=False)
c = sp(15.2, 5.6, "Cultivated emmer", "AABB", 28, it=False)
d = sp(23.6, 9.8, "Aegilops tauschii", "DD", 14)
w = sp(20.6, 1.6, r"$\it{T.\ aestivum}$ (bread wheat)", "AABBDD", 42, w=7.0, it=False)
du = sp(9.2, 1.6, "Durum wheat", "AABB", 28, it=False)
bio.arrow(ax, (3.4, 8.8), (6.0, 6.6), kind="process")
bio.arrow(ax, (10.6, 8.8), (8.0, 6.6), kind="process")
bio.label(ax, (7.0, 8.0), "×  hybrid, 2n → 4n", size="small")
bio.label(ax, (7.0, 7.4), "~0.5 Myr ago", size="tiny")
bio.arrow(ax, (10.4, 5.6), (12.3, 5.6), kind="process")
bio.label(ax, (11.4, 6.3), "domestication", size="tiny")
bio.label(ax, (11.4, 4.9), "~10 000 yr", size="tiny")
bio.arrow(ax, (14.0, 4.6), (10.4, 2.6), kind="process")
bio.arrow(ax, (16.4, 4.6), (19.4, 2.6), kind="process")
bio.arrow(ax, (23.6, 8.8), (21.8, 2.6), kind="process")
bio.label(ax, (23.4, 5.8), "×  hybrid in fields,", size="small", ha="left")
bio.label(ax, (23.4, 5.2), "2n → 6n, ~8000-9000 yr", size="tiny", ha="left")
