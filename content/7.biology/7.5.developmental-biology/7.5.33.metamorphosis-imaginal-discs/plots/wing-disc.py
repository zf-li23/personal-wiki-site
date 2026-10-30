"""Patterning of the Drosophila wing imaginal disc (third instar; schematic, anterior left, notum up).

A: compartments and selector genes: engrailed and hedgehog in the posterior compartment, apterous in the dorsal
compartment; Hedgehog signals across the AP boundary and induces dpp in a stripe of anterior cells; Notch
signalling at the DV boundary induces wingless; vestigial (the wing selector) in the pouch. B: the Dpp gradient
(shading) and its nested readouts spalt (narrow) and optomotor-blind (wider) on both sides of the source.
C: a model of the readout: Dpp ~ exp(-|x| / 20 um) from the stripe; spalt above the higher threshold, omb above
the lower; brinker is repressed by Dpp and is expressed where Dpp is low.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import limbdev as LD
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(30.0, 10.4)

bio.panel(ax, "A", (0.2, 10.2))
w = LD.WingDisc(ax, (4.6, 5.2), 3.6, 3.4)
w.region("P", "positive", shade=0.55)
w.region("D", "receptor", shade=0.75)
w.stripe(-0.15, 0.0, "highlight")
w.dv_stripe(0.08, "drug")
w.boundaries()
bio.callout(ax, (w.xap - 0.25, w.anchors["notum"][1] + 0.6), (2.0, 9.6), "dpp stripe (anterior)", size="tiny")
bio.callout(ax, (w.anchors["P"][0] + 0.6, w.anchors["P"][1] + 0.8), (7.9, 9.6), "en, hh (posterior)", size="tiny")
bio.callout(ax, (w.pc[0] - 1.2, w.ydv), (0.6, 1.0), "wg at the DV boundary", size="tiny")
bio.callout(ax, (w.pc[0] - 0.9, w.ydv + 0.75), (0.5, 7.0), "apterous (dorsal)", size="tiny")
bio.callout(ax, w.anchors["pouch"], (7.9, 1.0), "pouch: vestigial", size="tiny")

bio.panel(ax, "B", (9.8, 10.2))
w2 = LD.WingDisc(ax, (14.2, 5.2), 3.6, 3.4)
w2.gradient(lambda d: np.exp(-abs(d + 0.07) / 0.22), "highlight", pouch_only=True)
w2.stripe(-0.13, 0.13, "protein", pouch_only=True, shade=0.35, z=w2.z + 0.9)
w2.stripe(-0.06, 0.06, "protein", pouch_only=True, z=w2.z + 0.95)
w2.boundaries(dv=False)
bio.callout(ax, (w2.xap - 0.05, w2.pc[1] + 0.9), (12.0, 9.6), "spalt", size="tiny")
bio.callout(ax, (w2.xap + 0.35, w2.pc[1] - 0.9), (17.6, 1.0), "optomotor-blind", size="tiny")

bio.panel(ax, "C", (19.6, 10.2))
pa = C.axes_at(ax, (21.0, 1.6, 8.4, 7.0))
x = np.linspace(-100, 100, 400)
dpp = np.exp(-np.abs(x) / 20.0)
pa.plot(x, dpp, color=Q.line_color("highlight"), lw=1.8, label="Dpp signal (pMad)")
pa.plot(x, 1 / (1 + (dpp / 0.12) ** 3), color=Q.line_color("neutral"), lw=1.3, ls=(0, (4, 2)), label="brinker")
for tval, tk, nm, yb in ((0.35, "protein", "spalt", -0.03), (0.12, "k", "omb", -0.085)):
    pa.axhline(tval, color=Q.line_color(tk), lw=0.9, ls=(0, (2, 2)))
    xb = 20 * np.log(1 / tval)
    pa.fill_between([-xb, xb], [yb - 0.022, yb - 0.022], [yb + 0.022, yb + 0.022], color=Q.line_color(tk), lw=0)
    pa.text(xb + 3, tval + 0.02, nm, fontsize=bio.core.FONT["tiny"], color=P.ink())
pa.set_ylim(-0.12, 1.05)
pa.set_xlim(-100, 100)
C.style_axes(pa, "distance from the dpp stripe / µm", "level")
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right")
