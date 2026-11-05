"""Plastid evolution and the number of plastid envelope membranes (after Archibald 2009, Keeling 2013,
Burki et al. 2020). Each disc is a plastid in section: green rings are the two membranes of the
cyanobacterial ancestor, the orange ring the plasma membrane of an engulfed eukaryotic alga, the blue ring
the host food-vacuole membrane (the chloroplast ER); the purple dot is a nucleomorph. Short lines inside
show thylakoid arrangement (single, paired, in threes, stacked)."""
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(33, 17)
CY, ALG, HOST, PG = "chloroplast", "rna", "dna", "cell_wall"


def plastid(xy, rings, thyl=1, nm=False, pg=False, phyco=False, r0=0.55, title=None, sub=None, it=False):
    x, y = xy
    ax.add_patch(Circle(xy, r0, facecolor=P.light(CY), edgecolor="none", zorder=4))
    r = r0
    for k, tok in enumerate(rings):
        ax.add_patch(Circle(xy, r, facecolor="none", edgecolor=P.edge(tok), lw=1.6, zorder=6))
        if k == 1 and pg:
            ax.add_patch(Circle(xy, r - 0.06, facecolor="none", edgecolor=P.edge(PG), lw=1.0, ls=(0, (2, 1.5)), zorder=6))
        if k == 1 and nm:
            ax.add_patch(Circle((x + r + 0.08, y + 0.05), 0.11, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.8, zorder=7))
        r += 0.17 if k != 1 else 0.24
    # thylakoids
    gap = 0.07
    for band in (-0.22, 0.0, 0.22):
        for t in range(thyl):
            yy = y + band + (t - (thyl - 1) / 2) * gap
            ax.plot([x - 0.34, x + 0.34], [yy, yy], color=P.edge("thylakoid"), lw=1.1, zorder=7, solid_capstyle="round")
            if phyco and t == 0:
                for xx in np.linspace(x - 0.28, x + 0.28, 5):
                    ax.add_patch(Circle((xx, yy + 0.04), 0.03, color=P.edge("negative"), zorder=8))
    if title:
        bio.label(ax, (x, y - r0 - 0.75), title, size="small", bold=True, italic=it)
    if sub:
        bio.label(ax, (x, y - r0 - 1.25), sub, size="tiny", color=P.muted())
    return np.array(xy)


# column headings
for xh, t in ((3.6, "Free-living ancestor"), (9.6, "Primary plastids"), (19.0, "Secondary plastids"),
              (28.6, "Tertiary plastids and kleptoplasts")):
    bio.label(ax, (xh, 16.4), t, size="normal", bold=True)

# cyanobacterium
ax.add_patch(FancyBboxPatch((2.4, 8.1), 2.4, 1.3, boxstyle="round,pad=0,rounding_size=0.6",
                            facecolor=P.light(CY), edgecolor=P.edge(CY), lw=1.6, zorder=5))
for yy in (8.45, 8.75, 9.05):
    ax.plot([2.75, 4.45], [yy, yy], color=P.edge("thylakoid"), lw=1.1, zorder=6)
bio.label(ax, (3.6, 7.5), "Cyanobacterium", size="small", bold=True)
bio.label(ax, (3.6, 7.0), "engulfed by a heterotrophic\neukaryote (primary endosymbiosis)", size="tiny", color=P.muted())

g = plastid((9.6, 13.2), [CY, CY], thyl=1, pg=True, phyco=True, title="Glaucophytes", sub="2 membranes + peptidoglycan")
rd = plastid((9.6, 8.7), [CY, CY], thyl=1, phyco=True, title="Red algae", sub="2 membranes, single thylakoids")
gr = plastid((9.6, 4.2), [CY, CY], thyl=3, title="Green algae, land plants", sub="2 membranes, thylakoid stacks")
for p in (g, rd, gr):
    bio.arrow(ax, (5.0, 8.75), (p[0] - 1.0, p[1]), kind="process", head=0.18)

# secondary: green
eu = plastid((15.2, 4.2), [CY, CY, HOST], thyl=3, title="Euglenids", sub="3 membranes")
ch = plastid((19.4, 4.2), [CY, CY, ALG, HOST], thyl=3, nm=True, title="Chlorarachniophytes", sub="4 membranes, nucleomorph")
# secondary: red
cr = plastid((15.2, 10.6), [CY, CY, ALG, HOST], thyl=2, nm=True, title="Cryptophytes", sub="4, nucleomorph")
ha = plastid((19.4, 10.6), [CY, CY, ALG, HOST], thyl=3, title="Haptophytes", sub="4, outer one = nuclear ER")
sm = plastid((23.6, 10.6), [CY, CY, ALG, HOST], thyl=3, title="Stramenopiles", sub="4, outer one = nuclear ER")
dn = plastid((19.4, 14.6), [CY, CY, HOST], thyl=3, title="Dinoflagellates", sub="3 membranes, peridinin")
bio.arrow(ax, (10.8, 4.2), (14.0, 4.2), kind="process", head=0.18)
bio.arrow(ax, (10.8, 4.0), (18.1, 3.6), kind="process", head=0.18, bend=-0.15)
bio.label(ax, (12.4, 4.55), "green alga engulfed", size="tiny", color=P.muted())
bio.arrow(ax, (10.8, 8.9), (14.0, 10.3), kind="process", head=0.18)
bio.label(ax, (12.0, 10.2), "red alga engulfed", size="tiny", color=P.muted())
bio.label(ax, (19.4, 12.05), "red-algal plastid: one or several transfers", size="tiny", color=P.muted())
ax.plot([14.2, 24.6], [12.35, 12.35], color=P.muted(), lw=0.7, ls=(0, (3, 2)), zorder=3)
bio.label(ax, (15.2, 6.4), "two independent green events", size="tiny", color=P.muted())

# tertiary
t1 = plastid((27.0, 14.6), [CY, CY, ALG, HOST], thyl=3, title="Karenia", sub="haptophyte-derived", it=True)
t2 = plastid((30.6, 14.6), [CY, CY, ALG, HOST], thyl=3, title="Kryptoperidinium", sub="whole diatom retained", it=True)
t3 = plastid((28.8, 9.6), [CY, CY, ALG, HOST], thyl=2, nm=True, title="Dinophysis", sub="kleptoplast from a cryptophyte\n(via the ciliate Mesodinium)", it=True)
bio.arrow(ax, (20.8, 14.6), (25.8, 14.6), kind="process", head=0.18)
bio.label(ax, (23.3, 15.0), "dinoflagellates replace plastids", size="tiny", color=P.muted())
bio.arrow(ax, (15.2, 8.75), (27.75, 9.1), kind="process", head=0.18, dashed=True, bend=-0.1)

# legend
lx, ly = 25.0, 3.8
for i, (tok, t) in enumerate(((CY, "cyanobacterial membranes (2)"), (ALG, "plasma membrane of engulfed alga"),
                               (HOST, "host food-vacuole membrane"))):
    ax.add_patch(Circle((lx, ly - i * 0.7), 0.22, facecolor="none", edgecolor=P.edge(tok), lw=1.6))
    bio.label(ax, (lx + 0.45, ly - i * 0.7), t, size="tiny", ha="left")
ax.add_patch(Circle((lx, ly - 2.1), 0.12, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.8))
bio.label(ax, (lx + 0.45, ly - 2.1), "nucleomorph (relic algal nucleus)", size="tiny", ha="left")
ax.add_patch(Circle((lx, ly - 2.8), 0.04, color=P.edge("negative")))
bio.label(ax, (lx + 0.45, ly - 2.8), "phycobilisomes on thylakoids", size="tiny", ha="left")
