# Branching and tree architecture, generated from rules (wikibio.botany). (A) Branching patterns as module
# diagrams, each colour one module (the product of one apical meristem): monopodial (the main axis grows on
# from its terminal bud and laterals stay subordinate), sympodial (each module ends in a flower or dies back
# and growth continues from one lateral bud just below: the apparent axis is a chain of modules), dichasial
# (two continuation modules below each terminal flower, a false dichotomy) and dichotomous (the apex itself
# divides into two equal apices, as in early land plants and Lycopodiaceae). (B) Tree habits: excurrent
# (monopodial leader with tiers of laterals, a conical crown; e.g. Picea, Massart's model), decurrent (a
# broad crown without a dominant leader; grown here by space colonisation of an elliptical crown, e.g.
# Quercus), fastigiate (steep, upright branches, e.g. Populus nigra 'Italica'), weeping (pendulous branches,
# e.g. Salix babylonica), sympodial with terminal inflorescences (Leeuwenberg's model, e.g. Plumeria),
# dichotomous (isotomous forking of a leafless axis with terminal sporangia, as in Rhynia-like early land
# plants) and an unbranched palm (Corner's model, e.g. Cocos). Bracketed L-systems with a gravitropism term
# generate all but the decurrent and palm habits; branch widths follow the pipe model (cross-sections add up).
import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(30.0, 19.0)

bio.panel(ax, "A", (0.2, 18.8))
bio.label(ax, (0.85, 18.77), "Branching", size="title", ha="left", va="top")
names = [("monopodial", "Monopodial"), ("sympodial", "Sympodial (monochasial)"), ("dichasial", "Sympodial (dichasial)"),
         ("dichotomous", "Dichotomous")]
for i, (k, name) in enumerate(names):
    x = 3.0 + i * 5.2
    a = B.branching(ax, (x, 12.4), 5.2, kind=k)
    bio.label(ax, (x, 12.0), name, size="normal")
    if k == "monopodial":
        bio.callout(ax, a["apex"], (x + 1.5, 17.9), "Terminal bud", size="small")
        bio.callout(ax, a["lateral"], (x + 1.6, 13.4), "Lateral branch", size="small")
    if k == "sympodial":
        bio.callout(ax, a["flower"], (x - 1.9, 15.6), "Terminal flower", size="small")
        bio.callout(ax, a["module"][1], (x + 1.4, 13.6), "Module", size="small")
    if k == "dichotomous":
        bio.callout(ax, a["fork"], (x + 1.9, 13.6), "Equal fork", size="small")
bio.label(ax, (5.6, 18.77), "(colours: successive modules)", size="small", color=P.muted(), ha="left", va="top")

bio.panel(ax, "B", (0.2, 10.8))
bio.label(ax, (0.85, 10.77), "Tree habits", size="title", ha="left", va="top")
habits = [("excurrent", "Excurrent"), ("decurrent", "Decurrent"), ("fastigiate", "Fastigiate"), ("weeping", "Weeping"),
          ("leeuwenberg", "Sympodial (Leeuwenberg)"), ("dichotomous", "Dichotomous"), ("palm", "Unbranched (palm)")]
for i, (k, name) in enumerate(habits):
    x = 2.2 + i * 4.25
    if k == "decurrent":
        t = B.crown_tree(ax, (x, 1.2), 7.6, crown=(0.3, 0.33), attractors=800, seed=2)
    else:
        t = B.lsystem_tree(ax, (x, 1.2), 7.6 if k not in ("dichotomous",) else 6.0, habit=k, width=3.6, seed=1)
    bio.label(ax, (x, 0.75), name, size="normal")
