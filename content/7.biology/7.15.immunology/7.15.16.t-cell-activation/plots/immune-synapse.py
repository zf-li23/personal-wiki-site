# The immunological synapse between a CD4+ T cell and an antigen-presenting cell.
# A: side view (schematic, not to scale). In the central zone (cSMAC) the membranes are held about 15 nm apart
#    by short complexes: TCR-pMHC II with CD4, and CD28-CD80. In the peripheral ring (pSMAC) the integrin
#    LFA-1 binds ICAM-1, a longer pair (about 40 nm). The phosphatase CD45, whose ectodomain is too large to
#    fit the narrow central gap, is segregated to the distal ring (dSMAC) - the basis of the kinetic
#    segregation model.
# B: face-on view of the mature "bull's-eye" synapse.
import numpy as np
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import immuno

P = bio.P
fig, ax = bio.canvas(30, 11.2)

# ---------------- A: side view ----------------
bio.panel(ax, "A", (0.1, 11.1))
y_apc = 1.9
bio.bilayer(ax, [(0.4, y_apc), (19.6, y_apc)])
S = 0.4                                     # bilayer half-thickness used for anchors
y_near, y_far = y_apc + 2 * S + 2.85, y_apc + 2 * S + 5.2
pts = [(0.4, y_far), (5.6, y_far), (6.8, y_near), (13.2, y_near), (14.4, y_far), (19.6, y_far)]
bio.bilayer(ax, pts)
bio.label(ax, (10.0, y_apc - 0.75), "Antigen-presenting cell", size="small", bold=True)
bio.label(ax, (10.0, y_far + 0.95), "CD4⁺ T cell", size="small", bold=True)

a0 = y_apc + S          # APC outer surface (anchor)
t_near = y_near - S     # T-cell outer surface in the centre
t_far = y_far - S

# centre: TCR-pMHC II + CD4
m = immuno.mhc_ii(ax, 10.6, a0)
immuno.tcr(ax, m["center_x"], t_near, up=-1, cd3_side="left")
immuno.cd4(ax, 11.6, t_near, up=-1, reach=m["beta2"][1] - 0.1, labels=False)
bio.label(ax, (12.05, a0 + 1.8), "CD4", size="tiny", ha="left")
bio.label(ax, (10.6, a0 - 0.05 + 0.0), "", size="tiny")

# CD28 - CD80 (B7-1)
x = 7.9
immuno.domain(ax, (x, a0 + 0.14 + 0.31), 0.5, 0.62, "antibody")
immuno.domain(ax, (x, a0 + 0.14 + 0.93), 0.5, 0.62, "antibody")
ax.plot([x, x], [a0 - 0.14, a0 + 0.14], color=P.edge("antibody"), lw=2)
ax.plot([x, x], [t_near + 0.14, t_near - 1.25], color=P.edge("receptor"), lw=2)
immuno.domain(ax, (x, a0 + 0.14 + 1.55), 0.5, 0.62, "receptor")
bio.label(ax, (x - 0.4, a0 + 0.75), "CD80", size="tiny", ha="right")
bio.label(ax, (x - 0.4, a0 + 1.9), "CD28", size="tiny", ha="right")

# pSMAC: LFA-1 - ICAM-1 on both sides of the centre
for x in (4.0, 16.0):
    for k in range(5):
        immuno.domain(ax, (x, a0 + 0.14 + 0.28 + k * 0.56), 0.42, 0.54, "enzyme")
    ax.plot([x, x], [a0 - 0.14, a0 + 0.14], color=P.edge("enzyme"), lw=2)
    for dx in (-0.28, 0.28):
        ax.plot([x + dx, x + dx], [t_far + 0.14, a0 + 3.15], color=P.edge("protein"), lw=2.2)
    immuno.domain(ax, (x, a0 + 3.25), 1.0, 0.55, "protein", text="αLβ2", size="tiny")
    bio.label(ax, (x + 0.6, a0 + 1.3), "ICAM-1", size="tiny", ha="left")
    bio.label(ax, (x + 0.6, a0 + 4.3), "LFA-1", size="tiny", ha="left")

# dSMAC: CD45 at the edges
for x in (1.4, 18.6):
    ax.plot([x, x], [t_far + 0.14, t_far - 0.6], color=P.edge("neutral"), lw=2)
    for k in range(4):
        immuno.domain(ax, (x, t_far - 0.9 - k * 0.6), 0.55, 0.58, "neutral")
    bio.label(ax, (x, t_far - 3.6), "CD45", size="tiny")

# zone brackets
for (a, b, name) in ((7.0, 13.0, "cSMAC"), (2.8, 6.0, "pSMAC"), (14.0, 17.2, "pSMAC"), (0.5, 2.4, "dSMAC"),
                     (17.6, 19.5, "dSMAC")):
    ax.plot([a, b], [0.15, 0.15], color=P.muted(), lw=0.9)
    for xx in (a, b):
        ax.plot([xx, xx], [0.08, 0.25], color=P.muted(), lw=0.9)
    bio.label(ax, ((a + b) / 2, 0.42), name, size="tiny", color=P.muted())
bio.label(ax, (10.0, y_near + 0.95), "gap ~15 nm", size="tiny", color=P.muted())
bio.label(ax, (4.0, y_far + 0.95), "gap ~40 nm", size="tiny", color=P.muted())

# ---------------- B: face-on bull's-eye ----------------
bio.panel(ax, "B", (20.6, 11.1))
c = (25.4, 5.6)
for r, tok, name in ((4.0, "neutral", "dSMAC"), (2.9, "enzyme", "pSMAC"), (1.35, "receptor", "cSMAC")):
    ax.add_patch(Circle(c, r, facecolor=P.light(tok), edgecolor=P.edge(tok), lw=1.0, zorder=3))
bio.label(ax, c, "TCR–pMHC\nCD28–CD80\nPKCθ", size="tiny", color=P.on_fill(), zorder=6)
bio.label(ax, (c[0], c[1] + 2.15), "LFA-1–ICAM-1, talin", size="tiny", color=P.on_fill(), zorder=6)
bio.label(ax, (c[0], c[1] + 3.45), "CD45, CD43", size="tiny", color=P.on_fill(), zorder=6)
bio.label(ax, (c[0], 0.5), "face-on view of the contact", size="tiny", color=P.muted())
