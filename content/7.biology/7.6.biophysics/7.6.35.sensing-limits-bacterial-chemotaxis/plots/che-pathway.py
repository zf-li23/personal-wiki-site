"""The chemotaxis network of E. coli as an SBGN activity-flow map. Attractant binding inhibits the
activity of the receptor-CheW-CheA complex at the inner membrane; active CheA phosphorylates CheY
and CheB. CheY-P binds the flagellar motor and promotes clockwise rotation (tumbles); the
phosphatase CheZ removes the phosphate. The methyltransferase CheR adds methyl groups to the
receptors and raises their activity; CheB-P removes them and lowers it. Because CheB is activated by
the receptor's own kinase, methylation closes a slow negative feedback loop around the fast
signaling path (dashed box), the loop responsible for adaptation."""

import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(16, 8.2)
d = network.Diagram(ax, size="small")
d.compartment("out", (0.3, 6.4, 15.7, 7.9), "Outside", token="extracellular", label_pos="tl")
d.compartment("cyt", (0.3, 0.3, 15.7, 6.1), "Cytoplasm", token="cytoplasm", label_pos="bl")

d.activity("att", (4.0, 7.15), "attractant", token="metabolite")
d.activity("rec", (4.0, 5.0), "receptor-CheW-CheA", token="receptor", w=3.6)
d.activity("chey", (9.2, 5.0), "CheY-P", token="protein")
d.activity("cheb", (4.0, 2.0), "CheB-P", token="enzyme")
d.activity("cher", (0.9 + 0.95, 3.5), "CheR", token="enzyme")
d.activity("chez", (9.2, 2.6), "CheZ", token="enzyme")
d.activity("mot", (13.2, 5.0), "motor CW", token="flagellum")
d.phenotype("tum", (13.2, 2.6), "tumble")

d.connect("att", "rec", kind="negative")
d.connect("rec", "chey", kind="positive")
d.connect("rec", "cheb", kind="positive", bend=-0.25)
d.connect("cheb", "rec", kind="negative", bend=-0.25)
d.connect("cher", "rec", kind="positive")
d.connect("chez", "chey", kind="negative")
d.connect("chey", "mot", kind="positive")
d.connect("mot", "tum", kind="positive")

bio.label(ax, (4.75, 3.5), "demethylation", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (1.85, 4.15), "methylation", size="tiny", color=P.muted())
bio.label(ax, (6.6, 5.35), "P", size="tiny", color=P.muted())
bio.label(ax, (4.25, 6.25), "binding (fast, ms)", size="tiny", color=P.muted(), ha="left")
x0, y0, x1, y1 = 0.7, 1.35, 7.6, 5.75
ax.plot([x0, x1, x1, x0, x0], [y0, y0, y1, y1, y0], color=P.muted(), lw=0.8, ls="--", zorder=3)
bio.label(ax, (x0 + 0.15, y0 + 0.25), "slow loop (s): adaptation", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (11.2, 5.5), "fast path: amplification", size="tiny", color=P.muted())
