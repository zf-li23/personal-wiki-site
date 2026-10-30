"""The proximo-distal code of the limb (schematic).

A: paddle-stage bud with the domains of Meis1/2 (proximal), Hoxa11 (middle) and Hoxa13 (distal).
B: the segments they become. C: deletion of whole paralogue groups (mouse hindlimbs): Hox10 (no stylopod),
Hox11 (no zeugopod), Hoxa13 and Hoxd13 (no autopod).
"""

import numpy as np
import wikibio as bio
from wikibio import limbdev as LD
from matplotlib.patches import Ellipse, PathPatch, Rectangle
from matplotlib.path import Path

P = bio.P
fig, ax = bio.canvas(30.0, 10.5)

bio.panel(ax, "A", (0.2, 10.3))
b = LD.limb_bud(ax, (1.8, 5.6), 6.6, 4.0, stage="paddle", aer=True, pz=False, zpa=False)
o = b["outline"]
clip = PathPatch(Path(np.vstack([o, o[:1]]), closed=True), facecolor="none", edgecolor="none")
ax.add_patch(clip)
wash = lambda t, k=0.35: P.mix(P.fill(t), P.surface(), 0.5 if P.is_dark() else k)
for (s0, s1, tok, name) in ((0.0, 0.42, "humerus", "Meis1/2"), (0.42, 0.66, "radius", "Hoxa11"), (0.66, 1.05, "phalanges", "Hoxa13")):
    x0, y0 = b["at"](s0, -1.6)
    x1, y1 = b["at"](s1, 1.6)
    r = Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor=wash(tok), edgecolor="none", zorder=5.4)
    r.set_clip_path(clip)
    ax.add_patch(r)
    bio.label(ax, b["at"]((s0 + min(s1, 1.0)) / 2, 0.0), name, size="small", italic=True, zorder=12)

bio.panel(ax, "B", (10.4, 10.3))
LD.limb_skeleton(ax, (10.9, 5.6), 8.0, labels=True)

bio.panel(ax, "C", (20.4, 10.3))
rows = [("Hox10 (a, c, d) null", dict(start="zeugopod", dx=0.34 * 6.6)), ("Hox11 (a, c, d) null", dict(proportions=(0.34, 0.0, 0.38))),
        ("Hoxa13; Hoxd13 null", dict(upto="zeugopod"))]
for k, (name, kw) in enumerate(rows):
    y = 8.7 - 3.1 * k
    bio.label(ax, (20.9, y + 0.95), name, size="tiny", italic=False, ha="left", bold=True)
    dx = kw.pop("dx", 0.0)
    LD.limb_skeleton(ax, (21.2 + dx, y), 6.6, width=0.36, **kw)
