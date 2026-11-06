# Two strategies of iron acquisition by roots (after the scheme of Guerinot and Yi 1994 and later work).
# A: Strategy I (eudicots and non-grass monocots, e.g. pea, tomato, Arabidopsis): the plasma membrane H+-ATPase
# (AHA2) acidifies the rhizosphere, raising Fe3+ solubility; roots release chelators (malate, citrate, phenolics,
# coumarins); the ferric-chelate reductase FRO2 reduces Fe3+ to Fe2+ with electrons from cytosolic NAD(P)H; the
# ZIP transporter IRT1 takes up Fe2+. B: Strategy II (grasses: barley, maize, rice, wheat): phytosiderophores of
# the mugineic acid family, made from methionine via nicotianamine, are secreted (TOM1) and chelate Fe3+; the
# Fe(III)-phytosiderophore complex is taken up intact by YELLOW STRIPE 1 (YS1) transporters. Both are induced by
# iron deficiency.
import wikibio as bio
from wikibio import cellbio as CB

P = bio.P
fig, ax = bio.canvas(26.0, 10.5)
y = 5.0
for x0, x1, letter, t1, t2 in ((0.2, 12.6, "A", "Strategy I", "eudicots, non-grass monocots"),
                               (13.4, 25.8, "B", "Strategy II", "grasses (Poaceae)")):
    CB.sides(ax, (x0, x1), y, height=(3.6, 3.2), top="Rhizosphere", bottom="Root epidermal cell", label_x=x0 + 0.2)
    bio.bilayer(ax, [(x0, y), (x1, y)])
    bio.panel(ax, letter, (x0 + 0.1, 10.3))
    bio.label(ax, (x0 + 0.8, 10.25), t1, size="title", ha="left", va="top")
    bio.label(ax, (x0 + 0.8, 9.6), t2, size="small", ha="left", va="top", color=P.muted())

# soil particle with Fe(III)
for cx in (6.4, 19.8):
    ax.add_patch(__import__("matplotlib").patches.Ellipse((cx, 8.3), 3.0, 0.9, facecolor=P.fill("bone"), edgecolor=P.edge("bone"),
                                                         lw=1, zorder=3))
    bio.label(ax, (cx, 8.3), "Fe(OH)₃ on soil", size="tiny")

# Strategy I
x = 2.2
atp = CB.pump(ax, x, y, width=1.5)
bio.arrow(ax, (x - 0.38, 3.4), (x - 0.38, 6.6), kind="process")
bio.ion(ax, (x - 0.38, 6.9), "h", r=0.15, text=False)
bio.label(ax, (x, 7.4), "H⁺ (AHA2)", size="tiny")
bio.molecule(ax, atp + (0.2, 0.1), token="atp", text="ATP", r=0.26, size=5.0)
x = 6.0
CB.carrier(ax, x, y, open="out", token="enzyme", width=1.3, text=None)
bio.label(ax, (x, 3.0), "FRO2", size="small", bold=True)
bio.label(ax, (x - 1.4, 3.7), "NADPH", size="tiny")
bio.arrow(ax, (x - 0.9, 3.8), (x - 0.2, 4.4), kind="process", head=0.15)
bio.label(ax, (x, 7.0), "Fe³⁺-chelate → Fe²⁺", size="tiny", bold=True)
bio.arrow(ax, (6.3, 7.8), (6.1, 7.25), kind="process", head=0.15)
x = 9.4
CB.carrier(ax, x, y, open="out", token="ca", width=1.3)
bio.arrow(ax, (x, 6.6), (x, 3.4), kind="process")
bio.label(ax, (x + 0.6, 6.7), "Fe²⁺", size="tiny", ha="left")
bio.label(ax, (x, 3.0), "IRT1 (ZIP)", size="small", bold=True)
bio.arrow(ax, (7.3, 6.95), (9.0, 6.75), kind="process", head=0.15)
bio.label(ax, (11.2, 7.6), "chelators:\nmalate, citrate,\ncoumarins", size="tiny", color=P.muted())

# Strategy II
x = 16.0
CB.carrier(ax, x, y, open="in", token="drug", width=1.3)
bio.arrow(ax, (x, 3.4), (x, 6.6), kind="process")
bio.label(ax, (x, 3.0), "TOM1", size="small", bold=True)
bio.label(ax, (x + 0.4, 6.9), "PS", size="tiny", ha="left")
bio.label(ax, (18.6, 2.4), "PS from methionine\nvia nicotianamine", size="tiny", color=P.muted())
bio.arrow(ax, (16.6, 7.3), (18.6, 8.0), kind="process", bend=-0.2)
bio.label(ax, (19.8, 7.1), "Fe(III)–PS", size="tiny", bold=True)
bio.arrow(ax, (20.4, 7.9), (20.0, 7.35), kind="process", head=0.15)
x = 22.6
CB.carrier(ax, x, y, open="out", token="ca", width=1.3)
bio.arrow(ax, (21.1, 7.0), (x, 6.5), kind="process", head=0.18)
bio.arrow(ax, (x, 6.4), (x, 3.4), kind="process")
bio.label(ax, (x, 3.0), "YS1", size="small", bold=True)
bio.label(ax, (x + 0.7, 2.3), "Fe(III)–PS\ninto the cell", size="tiny", color=P.muted())
bio.label(ax, (24.5, 8.7), "PS = mugineic-acid-type\nphytosiderophore", size="tiny", color=P.muted())
