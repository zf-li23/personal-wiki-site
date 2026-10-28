"""The monohybrid cross for cotyledon color. A: P (YY x yy) -> F1 (Yy) -> F2 by selfing. B: Punnett square of
Yy x Yy (3:1). C: the F3 progeny test; Mendel's 519 yellow F2 plants: 166 bred true, 353 segregated (1:2)."""
import numpy as np

import wikibio as bio
from wikibio import genetics as G
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(26.0, 8.0)

# A: pedigree of the cross
bio.panel(ax, "A", (0.2, 7.8))
def seed(xy, tok, text):
    ax.add_patch(bio.core.Circle(xy, 0.42, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=10))
    bio.label(ax, (xy[0], xy[1] - 0.72), text, size="small", italic=True)

seed((1.6, 6.3), "highlight", "YY"); seed((4.4, 6.3), "positive", "yy")
bio.label(ax, (3.0, 6.3), "×", size="title")
bio.label(ax, (0.55, 6.3), "P", size="normal", bold=True)
bio.arrow(ax, (3.0, 5.6), (3.0, 4.6))
seed((3.0, 4.0), "highlight", "Yy")
bio.label(ax, (0.55, 4.0), "F₁", size="normal", bold=True)
bio.label(ax, (3.6, 4.0), "all yellow", size="small", ha="left", color=P.muted())
bio.arrow(ax, (3.0, 2.95), (3.0, 2.1))
bio.label(ax, (3.25, 2.7), "self", size="small", ha="left", color=P.muted())
bio.label(ax, (0.55, 1.5), "F₂", size="normal", bold=True)
for i, (tok, t) in enumerate((("highlight", "YY"), ("highlight", "Yy"), ("highlight", "Yy"), ("positive", "yy"))):
    seed((1.5 + i * 1.0, 1.5), tok, t)
bio.label(ax, (3.0, 0.35), "3 yellow : 1 green", size="small")

# B: Punnett square
bio.panel(ax, "B", (6.4, 7.8))
G.punnett(ax, (8.3, 5.6), "Yy", "Yy", cell=1.5, phenotype={"Y_": "Yellow", "yy": "Green"},
          colors={"Yellow": "highlight", "Green": "positive"}, titles=("Pollen", "Eggs"))

# C: F3 test
bio.panel(ax, "C", (16.0, 7.8))
p = quant.Plot(ax, (17.8, 1.6, 7.4, 5.2), xlim=(0, 3), ylim=(0, 400), ylabel="yellow F₂ plants",
               yticks=[0, 100, 200, 300, 400], xticks=[(0.9, "bred true\n(YY)"), (2.1, "segregated\n(Yy)")])
obs = [166, 353]
exp = [519 / 3, 2 * 519 / 3]
for x, o, e, tok in ((0.9, obs[0], exp[0], "highlight"), (2.1, obs[1], exp[1], "dna")):
    ax.add_patch(bio.core.FancyBboxPatch((p.X(x - 0.3), p.Y(0)), p.X(x + 0.3) - p.X(x - 0.3), p.Y(o) - p.Y(0),
                                         boxstyle="square,pad=0", facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8,
                                         zorder=8))
    ax.plot([p.X(x - 0.4), p.X(x + 0.4)], [p.Y(e), p.Y(e)], color=P.ink(), lw=1.3, ls=(0, (3, 2)), zorder=9)
    bio.label(ax, (p.X(x), p.Y(o) + 0.25), str(o), size="small")
bio.label(ax, (p.X(1.5), p.Y(400) + 0.35), "dashed: expected 1 : 2", size="tiny", color=P.muted())
