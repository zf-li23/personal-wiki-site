"""Separation of the digits (schematic autopods, distal right, anterior up).

A: the autopod plate before separation: digit condensations (Sox9) and interdigital mesenchyme expressing BMP2, 4
and 7. B: chick: BMP signalling (with retinoic acid) kills the interdigital cells (dots: apoptosis), freeing the
toes. C: duck: the interdigital mesenchyme also expresses the BMP antagonist Gremlin; death is reduced and the web
persists. D: chick with a dominant-negative BMP receptor (or a Noggin or Gremlin bead) in the interdigits: webbed,
duck-like foot.
"""

import numpy as np
import wikibio as bio
from wikibio import limbdev as LD
from matplotlib.patches import Circle

P = bio.P
rng = np.random.default_rng(5)
fig, ax = bio.canvas(30.0, 7.6)


def autopod(x0, y0, web, dots=False, bmp=False, grem=False):
    probe = LD.limb_skeleton(ax, (x0, y0), 6.0, digits=(1, 2, 3, 4), start="zeugopod", proportions=(0, 0, 0.62),
                             width=0.62, spread=7.0, z=8)
    tips = [np.array(p) for _, p in probe["digits"]]
    wr = np.array(probe["wrist"])
    if web:
        pts = [wr + (-0.2, -1.6)] + [t + (0.2, 0) for t in tips[::-1]] + [wr + (-0.2, 1.6)]
        poly = bio.smooth_closed(np.array(pts), 160)
        tok = "highlight" if bmp else "mesoderm"
        bio.shape(ax, poly, tok, lw=0.9, zorder=4)
        ax.patches[-1].set_facecolor(P.mix(P.fill(tok), P.surface(), 0.55 if P.is_dark() else 0.5))
        if grem:
            for a, b in zip(tips[:-1], tips[1:]):
                m = wr + ((a + b) / 2 - wr) * 0.62
                ax.add_patch(Circle(tuple(m), 0.16, facecolor=P.fill("positive"), edgecolor=P.edge("positive"), lw=0.6, zorder=5))
    if dots:
        for a, b in zip(tips[:-1], tips[1:]):
            for _ in range(14):
                f = rng.uniform(0.45, 0.97)
                m = wr + ((a + b) / 2 - wr) * f + rng.normal(0, 0.035, 2)
                ax.add_patch(Circle(tuple(m), 0.07, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.4, zorder=9))
    return probe


panels = [("A", "Autopod plate: BMP between digits", dict(web=True, bmp=True)),
          ("B", "Chick: interdigital apoptosis", dict(web=False, dots=True)),
          ("C", "Duck: Gremlin blocks BMP", dict(web=True, grem=True)),
          ("D", "Chick + dominant-negative BMPR", dict(web=True))]
for k, (lt, title, kw) in enumerate(panels):
    x0 = 0.8 + 7.4 * k
    bio.panel(ax, lt, (x0 - 0.5, 7.4))
    bio.label(ax, (x0 + 3.0, 7.0), title, size="small", bold=True)
    autopod(x0 + 0.3, 3.8, **kw)
bio.label(ax, (8.0, 0.7), "red dots: dying cells", size="tiny", color=P.muted())
bio.label(ax, (16.3, 0.7), "green: Gremlin", size="tiny", color=P.muted())
