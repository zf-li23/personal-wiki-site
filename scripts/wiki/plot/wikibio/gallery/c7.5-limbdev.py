# Limb development and imaginal discs (wikibio.limbdev). A: an early chick wing bud in dorsal view with the
# apical ectodermal ridge (AER) along the distal rim, the progress zone beneath it and the zone of polarizing
# activity (ZPA) at the posterior margin; the three limb axes. B: a paddle-stage bud. C: a schematic limb
# skeleton coloured by segment (stylopod, zeugopod, autopod), digits 1-5 from anterior (top) to posterior.
# D: a mirror-image duplication 4-3-2-2-3-4 and a skeleton truncated after the zeugopod. E: a section through
# the bud along the proximo-distal and dorso-ventral axes. F: the wing imaginal disc with its posterior
# compartment, the dpp stripe and the wg stripe at the DV boundary. G: leg disc and everted leg.
# H: a third-instar larva with its imaginal discs.
import numpy as np
import wikibio as bio
from wikibio import limbdev as LD

P = bio.P
fig, ax = bio.canvas(30, 17)

bio.panel(ax, "A", (0.2, 16.8))
b = LD.limb_bud(ax, (2.0, 13.4), 4.0, 3.2)
bio.callout(ax, b["aer"], (7.4, 15.6), "AER")
bio.callout(ax, b["pz"], (7.6, 13.4), "Progress zone")
bio.callout(ax, b["zpa"], (7.4, 11.3), "ZPA")
LD.axes_glyph(ax, (1.2, 10.4), 1.0)

bio.panel(ax, "B", (9.8, 16.8))
b2 = LD.limb_bud(ax, (11.2, 13.4), 4.6, 2.6, stage="paddle")
bio.callout(ax, b2["anterior"], (12.0, 16.3), "Anterior")
bio.callout(ax, b2["posterior"], (12.0, 10.6), "Posterior")

bio.panel(ax, "C", (18.6, 16.8))
s = LD.limb_skeleton(ax, (19.0, 13.4), 8.6, labels=True, digit_labels=True)

bio.panel(ax, "D", (0.2, 8.8))
LD.limb_skeleton(ax, (0.8, 6.6), 6.8, digits=(4, 3, 2, 2, 3, 4), digit_labels=True, colored="bone")
LD.limb_skeleton(ax, (0.8, 2.3), 6.8, upto="zeugopod")
bio.label(ax, (0.8, 1.2), "AER removed early: no autopod", size="tiny", ha="left", color=P.muted())

bio.panel(ax, "E", (9.8, 8.8))
x = LD.bud_section(ax, (10.6, 5.5), 4.2, 3.2)
bio.callout(ax, x["aer"], (15.6, 6.8), "AER")
bio.label(ax, (10.3, 5.5), "Flank", size="tiny", ha="right", color=P.muted())

bio.panel(ax, "F", (17.4, 8.8))
w = LD.WingDisc(ax, (20.4, 5.4), 2.8, 2.6)
w.region("P", "positive", shade=0.6)
w.gradient(lambda d: np.exp(-abs(d) / 0.25), "highlight")
w.stripe(-0.16, 0.0, "highlight")
w.dv_stripe(0.09, "receptor")
w.boundaries()
bio.callout(ax, w.anchors["notum"], (17.8, 8.3), "Notum")
bio.callout(ax, w.anchors["hinge"], (17.6, 3.0), "Hinge")

bio.panel(ax, "G", (24.0, 8.8))
LD.leg_disc(ax, (25.6, 6.6), 1.3)
LD.telescoped_leg(ax, (28.2, 8.0), 6.5)

bio.panel(ax, "H", (17.4, 2.2))
lv = LD.larva(ax, (25.0, 1.3), 8.0, height=1.8)
bio.callout(ax, lv["discs"]["wing"], (22.4, 2.4), "Wing disc", size="tiny")
