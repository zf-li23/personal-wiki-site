"""Kin competition can cancel the benefit of helping relatives.

The actor pays c, a neighbor gains b, and a fraction a of the competition for resources that the extra offspring
face is local, among neighbors related to the actor by r (large groups assumed). The inclusive fitness effect is
-c + r b - a r (b - c) (West, Pen and Griffin 2002); a = 0 recovers Hamilton's rule, and with a = 1 it reduces to
-c (1 - r) < 0, so that altruism is never favored however high r is (Taylor 1992).
A: the critical benefit-to-cost ratio, b/c > (1 - a r) / (r (1 - a)), against r for four scales of competition.
B: the inclusive fitness effect against a for b = 3, c = 1 and two relatednesses; it becomes negative above
a* = (r b - c) / (r (b - c)).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)

pa = Ch.axes_at(ax, (2.4, 1.8, 11.0, 7.2))
r = np.linspace(0.05, 1.0, 300)
for a, tok in ((0.0, "dna"), (0.5, "protein"), (0.8, "rna"), (0.95, "negative")):
    bc = (1 - a * r) / (r * (1 - a))
    pa.plot(r, bc, color=Ch.line(tok), lw=1.6)
    i = np.argmin(np.abs(bc - 9.0)) if bc.min() < 9 else -1
    xi = r[np.argmin(np.abs(bc - 6.5))] if (bc < 6.5).any() else 0.95
    pa.text(min(xi + 0.02, 0.9), 6.5, f"a = {a:g}", fontsize=FS["tiny"], color=Ch.line(tok))
pa.set_xlim(0, 1.0)
pa.set_ylim(0, 12)
Ch.style_axes(pa, "relatedness r", "critical b/c")
pa.text(0.4, 0.5, "altruism favored above each curve", fontsize=FS["tiny"], color=P.muted(), ha="center")
bio.panel(ax, "A", (0.3, 9.8))

pb = Ch.axes_at(ax, (18.2, 1.8, 10.8, 7.2))
b, c = 3.0, 1.0
a = np.linspace(0, 1, 200)
for rr, tok in ((0.5, "dna"), (0.75, "rna")):
    eff = -c + rr * b - a * rr * (b - c)
    pb.plot(a, eff, color=Ch.line(tok), lw=1.6)
    astar = (rr * b - c) / (rr * (b - c))
    pb.plot([astar], [0], "o", ms=4.5, color=Ch.line(tok))
    pb.text(0.03, eff[0] + 0.05, f"r = {rr:g}", fontsize=FS["tiny"], color=Ch.line(tok), va="bottom")
pb.axhline(0, color=P.muted(), lw=0.8)
pb.set_xlim(0, 1)
pb.set_ylim(-0.4, 1.4)
Ch.style_axes(pb, "scale of competition a (fraction local)", "inclusive fitness effect")
bio.panel(ax, "B", (15.8, 9.8))
