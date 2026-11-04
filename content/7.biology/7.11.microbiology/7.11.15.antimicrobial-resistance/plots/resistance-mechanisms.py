# Biochemical mechanisms of antibiotic resistance in a Gram-negative cell (schematic cross-section of
# the envelope with part of the cytoplasm; not to scale). Drug molecules are small red diamonds.
# 1 reduced uptake: loss or mutation of a porin; 2 inactivation in the periplasm: a beta-lactamase
# hydrolyses the beta-lactam ring; 3 multidrug efflux: the tripartite RND pump AcrAB-TolC captures drugs
# in the periplasm or inner membrane and expels them across the outer membrane; 4 target modification:
# an Erm methyltransferase methylates 23S rRNA so macrolides no longer bind; 5 target protection: a
# ribosome protection protein (Tet(M)) dislodges tetracycline; 6 drug modification in the cytoplasm:
# aminoglycoside-modifying enzymes (AAC, APH, ANT); 7 bypass: an acquired drug-insensitive enzyme (Sul,
# Dfr) replaces the inhibited one.
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(24, 13)
y_im = 6.4
ax.add_patch(Rectangle((0.5, 1.4), 23, y_im - 1.3 - 1.4, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=4))
L = M.envelope(ax, 0.5, 23.5, y_im, kind="gram-", seed=5)
om, top = L["om"], L["top"]
bio.label(ax, (23.3, top - 0.35), "outside", size="small", ha="right", color=P.muted())
bio.label(ax, (23.3, (y_im + L["om_lo"]) / 2 + 0.25), "periplasm", size="small", ha="right", color=P.muted())
bio.label(ax, (23.3, 1.8), "cytoplasm", size="small", ha="right", color=P.muted())


def drug(xy, s=0.17, zorder=30):
    x, y = xy
    ax.add_patch(Polygon([(x, y + s), (x + s, y), (x, y - s), (x - s, y)], closed=True, facecolor=P.fill("drug"),
                         edgecolor=P.edge("drug"), lw=0.8, zorder=zorder))


def num(xy, k):
    bio.label(ax, xy, str(k), size="normal", bold=True, color=P.ink(), zorder=40)


# 1 porin: drug blocked at a closed (mutant) porin
p0 = L["porins"][0]
drug((p0, top - 0.6))
ax.plot([p0 - 0.35, p0 + 0.35], [om + 0.75, om + 0.75], color=P.edge("negative"), lw=2.2, zorder=31)
num((p0 - 1.0, top - 0.4), 1)
bio.label(ax, (p0, top + 0.35), "porin loss", size="small")

# 2 beta-lactamase in the periplasm
bl = (p0 + 2.6, y_im + 1.5)
bio.protein(ax, bl, 1.6, 0.8, "enzyme", text="β-lactamase", size="tiny")
drug((bl[0] - 1.4, bl[1] + 0.5))
bio.arrow(ax, (bl[0] - 1.15, bl[1] + 0.4), (bl[0] - 0.85, bl[1] + 0.2), kind="process", lw=0.9, head=0.12)
for dx in (0.95, 1.25):
    drug((bl[0] + dx, bl[1] - 0.45 + (dx - 1) * 0.6), s=0.1)
num((bl[0] - 1.9, bl[1] - 0.3), 2)
bio.label(ax, (bl[0], bl[1] - 0.75), "drug inactivation", size="tiny", color=P.ink())

# 3 efflux pump AcrAB-TolC
ex = 13.2
ax.add_patch(Rectangle((ex - 0.7, y_im - 0.55), 1.4, 1.1, facecolor=P.fill("channel"),
                       edgecolor=P.edge("channel"), lw=1.0, zorder=20))
bio.label(ax, (ex, y_im), "AcrB", size="tiny", color=P.on_fill(), zorder=21)
ax.add_patch(Polygon([(ex - 0.75, y_im + 0.55), (ex + 0.75, y_im + 0.55), (ex + 0.45, om - 0.75), (ex - 0.45, om - 0.75)],
                     closed=True, facecolor=P.light("channel"), edgecolor=P.edge("channel"), lw=1.0, zorder=20))
bio.label(ax, (ex + 0.95, y_im + 1.1), "AcrA", size="tiny", ha="left", color=P.ink(), zorder=21)
ax.add_patch(Rectangle((ex - 0.42, om - 0.75), 0.84, top - om + 0.2, facecolor=P.fill("channel"),
                       edgecolor=P.edge("channel"), lw=1.0, zorder=20))
bio.label(ax, (ex, om + 0.55), "TolC", size="tiny", color=P.on_fill(), zorder=21, rotation=90)
drug((ex - 1.2, y_im + 0.9))
bio.arrow(ax, (ex - 1.0, y_im + 0.85), (ex - 0.25, y_im + 0.35), kind="process", lw=0.9, head=0.12, zorder=32)
drug((ex, top + 0.25))
bio.arrow(ax, (ex, top - 0.4), (ex, top + 0.02), kind="process", lw=0.9, head=0.12, zorder=32)
bio.label(ax, (ex, y_im - 0.95), "H$^+$ in", size="tiny", color=P.muted(), zorder=33)
num((ex - 1.7, top - 0.4), 3)
bio.label(ax, (ex, top + 0.75), "multidrug efflux", size="small")

# 4 target modification: methylated ribosome (macrolide cannot bind)
r4 = (3.0, 3.6)
bio.ribosome(ax, r4, size=1.6)
bio.label(ax, (r4[0] + 0.2, r4[1] + 0.85), "CH$_3$", size="tiny", color=P.edge("negative"))
bio.protein(ax, (r4[0] - 1.8, r4[1] + 1.2), 1.0, 0.6, "enzyme", text="Erm", size="tiny")
drug((r4[0] + 1.4, r4[1] + 1.2))
ax.plot([r4[0] + 1.0, r4[0] + 1.25], [r4[1] + 0.95, r4[1] + 1.2], color=P.edge("negative"), lw=1.4, zorder=31)
num((r4[0] - 2.6, r4[1] - 0.6), 4)
bio.label(ax, (r4[0], r4[1] - 1.1), "target modification", size="tiny", color=P.ink())

# 5 target protection
r5 = (8.0, 3.6)
bio.ribosome(ax, r5, size=1.6)
bio.protein(ax, (r5[0] + 1.25, r5[1] - 0.1), 0.9, 0.7, "protein", text="TetM", size="tiny")
drug((r5[0] + 0.4, r5[1] + 1.25))
bio.arrow(ax, (r5[0] + 0.1, r5[1] + 0.55), (r5[0] + 0.32, r5[1] + 1.02), kind="process", lw=0.9, head=0.12, zorder=32)
num((r5[0] - 1.5, r5[1] - 0.6), 5)
bio.label(ax, (r5[0], r5[1] - 1.1), "target protection", size="tiny", color=P.ink())

# 6 drug modification in the cytoplasm
m6 = (16.8, 3.8)
bio.protein(ax, m6, 1.6, 0.8, "enzyme", text="AAC / APH", size="tiny")
drug((m6[0] - 1.4, m6[1] + 0.3))
bio.arrow(ax, (m6[0] - 1.2, m6[1] + 0.25), (m6[0] - 0.85, m6[1] + 0.1), kind="process", lw=0.9, head=0.12)
drug((m6[0] + 1.25, m6[1] - 0.2))
bio.label(ax, (m6[0] + 1.25, m6[1] + 0.15), "-Ac / -P", size="tiny", ha="left", color=P.edge("negative"))
num((m6[0] - 2.0, m6[1] - 0.6), 6)
bio.label(ax, (m6[0], m6[1] - 0.9), "drug modification", size="tiny", color=P.ink())

# 7 bypass: drug-sensitive enzyme inhibited, acquired insensitive enzyme works
b7 = (21.0, 4.0)
bio.protein(ax, (b7[0] - 0.7, b7[1] + 0.3), 1.1, 0.6, "protein", text="DHPS", size="tiny")
drug((b7[0] - 0.7, b7[1] + 0.85))
bio.protein(ax, (b7[0] + 0.9, b7[1] - 0.4), 1.1, 0.6, "positive", text="Sul2", size="tiny")
bio.label(ax, (b7[0], b7[1] - 1.2), "bypass", size="tiny", color=P.ink())
num((b7[0] - 1.8, b7[1] - 0.6), 7)
ax.set_ylim(1.2, 13)
