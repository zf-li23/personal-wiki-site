"""The three routes of lipid transport by plasma lipoproteins.

Exogenous (top): enterocytes package dietary triacylglycerol and cholesterol around apoB-48 into chylomicrons;
lipoprotein lipase (LPL, activated by apoC-II) on the capillary endothelium of muscle and adipose tissue
releases fatty acids; cholesterol-rich chylomicron remnants are taken up by the liver through apoE.
Endogenous (middle): the liver secretes VLDL (apoB-100); LPL converts VLDL to IDL and, with hepatic lipase,
to cholesterol-rich LDL, which LDL receptors on peripheral cells and on the liver take up by
receptor-mediated endocytosis. Reverse cholesterol transport (bottom): lipid-poor apoA-I takes up
cholesterol from peripheral cells and macrophages through ABCA1 (and mature HDL through ABCG1); LCAT
esterifies it, making mature spherical HDL; the liver removes cholesteryl esters selectively through SR-BI,
and CETP transfers some to apoB-containing lipoproteins. The liver excretes cholesterol into bile, as such
or as bile acids. Particle circles are drawn with their relative diameters compressed.
"""

from matplotlib.patches import Circle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(28.0, 15.0, scale=0.42)


def particle(xy, r, tok, name, sub):
    ax.add_patch(Circle(xy, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.2, zorder=12))
    ax.add_patch(Circle(xy, r * 0.62, facecolor=P.light(tok), edgecolor="none", zorder=13))
    bio.label(ax, xy, name, size="tiny", bold=True, color=P.on_fill(), zorder=14)
    bio.label(ax, (xy[0], xy[1] - r - 0.3), sub, size="tiny", color=P.muted(), va="top")


def go(a, b, tok, text=None, dy=0.3, bend=0.0, dashed=False):
    bio.arrow(ax, a, b, kind="process", color=P.edge(tok), lw=1.6, bend=bend, dashed=dashed)
    if text:
        bio.label(ax, ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + dy), text, size="tiny", color=P.edge(tok), bold=True)


# organs
bio.icon(ax, "servier/small-intestine", at=(2.0, 12.6), height=2.2)
bio.label(ax, (2.0, 11.1), "intestine", size="tiny", color=P.muted())
bio.icon(ax, "servier/liver", at=(24.8, 8.0), height=2.6)
bio.label(ax, (24.8, 6.45), "liver", size="small", bold=True, color=P.muted())
bio.icon(ax, "servier/muscle", at=(11.8, 14.2), height=1.2)
bio.icon(ax, "servier/adipocyte", at=(13.6, 14.2), height=1.2)
bio.label(ax, (12.7, 13.3), "muscle, adipose tissue: LPL", size="tiny", color=P.muted())
bio.icon(ax, "servier/macrophage", at=(2.0, 2.2), height=2.0)
bio.label(ax, (2.0, 0.85), "peripheral cells,\nmacrophages", size="tiny", color=P.muted())
bio.icon(ax, "servier/adipocyte", at=(2.0, 7.0), height=1.4)
bio.label(ax, (2.0, 5.9), "peripheral cells\n(LDL receptor)", size="tiny", color=P.muted())

# exogenous pathway
EX, EN, RV = "lipid", "drug", "dna"
particle((6.0, 12.2), 1.05, EX, "CM", "chylomicron\napoB-48, C-II, E")
particle((17.6, 12.2), 0.75, EX, "CM\nremnant", "apoB-48, E")
go((3.3, 12.4), (4.85, 12.3), EX)
go((7.2, 12.2), (16.7, 12.2), EX, "TAG → fatty acids (LPL + apoC-II)")
go((18.4, 11.7), (23.6, 9.0), EX, "apoE → receptor", dy=0.45)

# endogenous pathway
particle((19.8, 7.0), 0.8, EN, "VLDL", "apoB-100, C-II, E")
particle((14.4, 7.0), 0.6, EN, "IDL", "")
particle((9.0, 7.0), 0.45, EN, "LDL", "apoB-100; cholesteryl esters")
go((23.4, 7.4), (20.7, 7.1), EN)
go((19.0, 7.0), (15.1, 7.0), EN, "LPL: TAG out")
go((13.8, 7.0), (9.55, 7.0), EN, "hepatic lipase")
go((8.5, 7.0), (2.9, 7.0), EN, "LDL receptor", dy=0.35)
go((9.3, 6.55), (23.6, 6.8), EN, "liver LDL receptors (most LDL)", dy=-1.25, bend=-0.08)

# reverse cholesterol transport
particle((7.6, 2.4), 0.4, RV, "", "apoA-I,\nnascent HDL")
particle((14.6, 2.4), 0.55, RV, "HDL", "mature HDL")
go((3.2, 2.4), (7.15, 2.4), RV, "ABCA1, ABCG1")
go((8.05, 2.4), (14.0, 2.4), RV, "LCAT: C → CE")
go((15.2, 2.6), (23.8, 6.9), RV, "SR-BI: selective CE uptake", dy=-0.6)
go((14.7, 3.0), (9.2, 6.4), RV, "CETP", dy=0.0, dashed=True)
bio.label(ax, (24.8, 4.6), "bile: cholesterol,\nbile acids", size="tiny", bold=True, color=P.muted())
bio.arrow(ax, (24.8, 6.3), (24.8, 5.2), kind="process", color=P.muted())
for y, t, tok in ((14.5, "exogenous", EX), (9.9, "endogenous", EN), (4.4, "reverse cholesterol transport", RV)):
    bio.label(ax, (5.0, y), t, size="small", bold=True, color=P.edge(tok), ha="left")
