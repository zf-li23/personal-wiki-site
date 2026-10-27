"""How Cdk activity is controlled (schematic).

(A) The states of a Cdk subunit (human Cdk1 or Cdk2 numbering). A free Cdk is inactive: its T loop blocks the
substrate site. Cyclin binding moves the T loop and makes the kinase partly active; phosphorylation of the
T-loop threonine (Thr161 in Cdk1, Thr160 in Cdk2) by CAK (cyclin H-Cdk7) activates it fully. Wee1 (nucleus)
and Myt1 (Golgi and ER) phosphorylate Tyr15 and Thr14 in the ATP-binding loop, which inhibits it even when the
activating phosphate is present; the Cdc25 phosphatases remove these phosphates. A Cdk inhibitor protein (CKI,
here p27) wraps around the cyclin-Cdk complex and blocks the active site.
(B) The mitotic entry circuit in SBGN activity-flow notation (open arrows activate, bars inhibit). Active
M-Cdk (cyclin B-Cdk1) activates its activator Cdc25 and inhibits its inhibitor Wee1 (two positive feedback
loops, the first helped by Plk1); it also activates Greatwall, whose substrates ENSA and ARPP19 inhibit
PP2A-B55, the phosphatase that reverses Cdk phosphorylation of Cdc25, Wee1 and mitotic substrates (a double
negative, therefore positive, loop); M-Cdk activates APC/C-Cdc20 with a delay, which destroys cyclin B
(the negative feedback that ends M phase). Checkpoints act by inhibiting Cdc25 (Chk1, Chk2) or Cdc20 (the
spindle assembly checkpoint).
"""

import math

import numpy as np
from matplotlib.patches import Circle, PathPatch, Polygon
from matplotlib.path import Path

import wikibio as bio
from wikibio import network

P = bio.P
FT = bio.core.FONT

fig, ax = bio.canvas(27.0, 12.0)


def cdk(c, open_=False):
    """A two-lobed kinase blob with the T loop either blocking (closed) or swung out."""
    bio.protein(ax, (c[0], c[1] - 0.15), 1.5, 1.35, token="enzyme", text="Cdk", size="small", zorder=8)
    # T loop
    if open_:
        pts = np.array([[c[0] + 0.55, c[1] + 0.1], [c[0] + 0.95, c[1] + 0.2], [c[0] + 1.0, c[1] - 0.25]])
    else:
        pts = np.array([[c[0] + 0.2, c[1] + 0.25], [c[0] - 0.05, c[1] + 0.05], [c[0] + 0.25, c[1] - 0.12]])
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge("negative"), lw=2.4, solid_capstyle="round", zorder=9)
    return pts


def cyclin(c):
    bio.protein(ax, (c[0] - 1.15, c[1] + 0.25), 1.2, 1.55, token="protein", text="cyclin", size="tiny", zorder=7)


def phos(xy, text="P", tok="highlight"):
    ax.add_patch(Circle(xy, 0.2, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=12))
    bio.label(ax, xy, text, size="tiny", bold=True, color=P.on_fill(), zorder=13)


bio.panel(ax, "A", (0.2, 11.8))
Y1, Y2 = 9.0, 4.4
# 1 free Cdk
cdk((1.6, Y1))
bio.label(ax, (1.6, Y1 - 1.35), "inactive", size="tiny", color=P.muted())
# 2 cyclin-Cdk
cyclin((5.0, Y1)); cdk((5.0, Y1), open_=True)
bio.label(ax, (4.6, Y1 - 1.35), "partly active", size="tiny", color=P.muted())
# 3 + CAK phosphate
cyclin((9.0, Y1)); tl = cdk((9.0, Y1), open_=True)
phos(tl[2] + [0.2, -0.1])
bio.label(ax, (8.6, Y1 - 1.35), "fully active", size="tiny", color=P.edge("positive"), bold=True)
bio.arrow(ax, (2.55, Y1), (3.45, Y1), kind="process")
bio.label(ax, (2.8, Y1 + 0.45), "+ cyclin", size="tiny")
bio.arrow(ax, (6.4, Y1), (7.4, Y1), kind="process")
bio.label(ax, (6.9, Y1 + 0.45), "CAK", size="tiny", bold=True)
bio.label(ax, (6.9, Y1 - 0.4), "Thr161", size="tiny", color=P.muted())
# 4 inhibitory phosphates (Wee1/Myt1) and Cdc25
cyclin((9.0, Y2)); tl2 = cdk((9.0, Y2), open_=True)
phos(tl2[2] + [0.2, -0.1])
phos((9.05, Y2 + 0.55), "P", "negative")
phos((9.45, Y2 + 0.62), "P", "negative")
bio.label(ax, (8.6, Y2 - 1.35), "inactive (Tyr15, Thr14)", size="tiny", color=P.edge("negative"))
bio.arrow(ax, (9.2, Y1 - 1.65), (9.2, Y2 + 1.15), kind="process")
bio.arrow(ax, (8.4, Y2 + 1.15), (8.4, Y1 - 1.65), kind="process")
bio.label(ax, (10.3, (Y1 + Y2) / 2 + 0.1), "Wee1\nMyt1", size="tiny", bold=True, ha="left")
bio.label(ax, (8.2, (Y1 + Y2) / 2 - 0.9), "Cdc25", size="tiny", bold=True, ha="right")
# 5 CKI
cyclin((4.4, Y2)); tl3 = cdk((4.4, Y2), open_=True)
phos(tl3[2] + [0.2, -0.1])
ax.add_patch(PathPatch(Path(np.array([[3.0, Y2 + 1.15], [4.4, Y2 + 1.35], [5.3, Y2 + 0.55], [4.9, Y2 - 0.1],
                                      [5.2, Y2 - 0.5], [4.95, Y2 - 0.6], [4.6, Y2 - 0.1], [4.95, Y2 + 0.45],
                                      [4.3, Y2 + 1.0], [3.0, Y2 + 0.9], [3.0, Y2 + 1.15]]), closed=True),
                       facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=0.9, zorder=11))
bio.label(ax, (3.2, Y2 + 1.45), "CKI (p27)", size="tiny", bold=True, ha="left")
bio.label(ax, (4.0, Y2 - 1.35), "inactive (CKI-bound)", size="tiny", color=P.edge("negative"))
bio.arrow(ax, (7.7, Y1 - 1.55), (5.75, Y2 + 1.55), kind="process")
bio.arrow(ax, (5.35, Y2 + 1.75), (7.3, Y1 - 1.75), kind="process", dashed=True)
bio.label(ax, (5.55, (Y1 + Y2) / 2 + 0.45), "+ CKI", size="tiny", ha="right")
bio.label(ax, (5.25, (Y1 + Y2) / 2 - 0.05), "SCF destroys\nthe CKI", size="tiny", ha="right", color=P.muted())
bio.label(ax, (1.0, 1.9), "Inhibitory phosphates override the activating one;\n"
          "cyclin destruction (APC/C, SCF) resets the cycle.", size="tiny", ha="left", color=P.muted())

# ----- B: circuit
bio.panel(ax, "B", (12.6, 11.8))
d = network.Diagram(ax, size="small")
d.compartment("cyt", (13.0, 0.4, 26.7, 11.2), "M phase entry and exit", token="cytoplasm")
d.activity("syn", (19.8, 9.9), "cyclin B synthesis", token="protein", w=3.6)
d.activity("mcdk", (19.8, 6.8), "M-Cdk\n(cyclin B–Cdk1)", token="negative", w=3.2, h=1.4)
d.activity("c25", (15.5, 6.8), "Cdc25", token="enzyme", w=2.0)
d.activity("wee", (15.5, 4.7), "Wee1, Myt1", token="receptor", w=2.4)
d.activity("plk", (15.5, 8.9), "Plk1", token="positive", w=1.6)
d.activity("gwl", (24.6, 9.9), "Greatwall", token="drug", w=2.4)
d.activity("ensa", (24.6, 7.9), "ENSA, ARPP19", token="drug", w=2.8)
d.activity("pp2a", (24.6, 5.5), "PP2A-B55", token="channel", w=2.6)
d.activity("apc", (19.8, 2.4), "APC/C–Cdc20", token="enzyme", w=3.0)
d.activity("chk", (15.0, 2.4), "Chk1, Chk2\n(DNA damage)", token="neutral", w=2.6, h=1.2)
d.activity("sac", (24.4, 2.4), "spindle assembly\ncheckpoint", token="neutral", w=3.0, h=1.2)
d.connect("syn", "mcdk", "positive")
d.connect("c25", "mcdk", "positive", start=(16.5, 7.0), end=(18.2, 7.0))
d.connect("mcdk", "c25", "positive", start=(18.2, 6.55), end=(16.5, 6.55))
d.connect("wee", "mcdk", "negative", start=(16.7, 4.95), end=(18.2, 6.35))
d.connect("mcdk", "wee", "negative", start=(18.4, 6.1), end=(16.9, 4.5))
d.connect("mcdk", "plk", "positive", via=[(18.6, 8.9)], start=(18.6, 7.5))
d.connect("plk", "c25", "positive")
d.connect("mcdk", "gwl", "positive", via=[(21.8, 9.9)], start=(21.4, 7.2))
d.connect("gwl", "ensa", "positive")
d.connect("ensa", "pp2a", "negative")
d.connect("pp2a", "gwl", "negative", via=[(26.3, 5.5), (26.3, 9.9)], start=(25.9, 5.5), end=(25.8, 9.9))
d.connect("pp2a", "mcdk", "negative", start=(23.3, 5.7), end=(21.4, 6.5), text="Cdk substrates,\nCdc25, Wee1",
          text_at=0.5, text_offset=(0.1, -0.75))
d.connect("mcdk", "apc", "positive", text="delay", text_offset=(0.45, 0.0), dashed=True)
d.connect("apc", "mcdk", "negative", via=[(17.9, 2.4), (17.9, 4.6), (19.0, 4.6)], start=(18.3, 2.4), end=(19.0, 6.1),
          text="cyclin B\ndestruction", text_at=0.25, text_offset=(-0.95, 0.0))
d.connect("chk", "c25", "negative", via=[(13.9, 6.8)], start=(13.9, 3.0), end=(14.5, 6.8))
d.connect("sac", "apc", "negative")
bio.label(ax, (13.4, 0.85), "positive loops: Cdc25, Wee1, Greatwall–PP2A-B55;  negative loop: APC/C", size="tiny", ha="left", color=P.muted())
