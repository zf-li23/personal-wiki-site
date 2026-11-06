# Growth of a palm (schematic). A: establishment growth: in the juvenile phase the stem hardly
# elongates while the shoot apex widens through the primary thickening meristem, giving an obconical
# stem base. B: adult single-stemmed palm: a cylindrical trunk of constant width with leaf scars, a
# single apical meristem (palm heart) enclosed by leaf sheaths in the crown, adventitious roots at the
# base. C: transverse section of the trunk with scattered bundles, denser towards the periphery, no
# cambium and no growth rings. D: PhyloPic palm silhouette.
import numpy as np
from matplotlib.patches import Polygon, Ellipse, Circle
import wikibio as bio
from wikibio import botany

P = bio.P
fig, ax = bio.canvas(30, 14)


def poly(pts, token, z=4, light=False, lw=1.2):
    ax.add_patch(Polygon(np.asarray(pts), closed=True, facecolor=P.light(token) if light else P.fill(token),
                         edgecolor=P.edge(token), lw=lw, joinstyle="round", zorder=z))


def leaf(base, ang, L, z=3):
    a = np.radians(ang)
    tip = base + L * np.array([np.cos(a), np.sin(a)])
    n = np.array([-np.sin(a), np.cos(a)])
    mid = base + 0.55 * (tip - base)
    poly([base, mid + n * 0.35 * L * 0.25, tip, mid - n * 0.35 * L * 0.25], "plant", z=z)


# ---- A: establishment growth (three stages)
bio.panel(ax, "A", (0.3, 13.7))
bio.label(ax, (4.6, 13.6), "Establishment growth", size="title")
ground = 2.0
ax.plot([0.6, 9.4], [ground, ground], color=P.edge("neutral"), lw=1.0, zorder=2)
for x, w, h in ((1.6, 0.25, 0.4), (4.2, 0.6, 0.8), (7.6, 1.1, 1.3)):
    poly([(x - 0.12, ground - h), (x - w, ground + 0.3), (x + w, ground + 0.3), (x + 0.12, ground - h)], "bract", z=4)
    for ang in (60, 80, 100, 120):
        leaf(np.array([x, ground + 0.3]), ang, 1.6 + 1.6 * w, z=3)
    for k in range(4):
        ax.plot([x - 0.1 + 0.07 * k, x - 0.4 + 0.27 * k], [ground - h, ground - h - 0.8], color=P.edge("neutral"), lw=0.8)
bio.arrow(ax, (2.3, 5.8), (6.7, 6.6), kind="process")
bio.label(ax, (4.6, 7.0), "years", size="small")
bio.callout(ax, (7.6 - 0.6, ground - 0.4), (5.0, 0.4), "Obconical stem base")

# ---- B: adult palm
bio.panel(ax, "B", (10.3, 13.7))
bio.label(ax, (14.0, 13.6), "Adult palm", size="title")
tx = 14.0
poly([(tx - 0.55, 1.2), (tx - 0.5, 9.8), (tx + 0.5, 9.8), (tx + 0.55, 1.2)], "bract", z=4)
for y in np.arange(1.6, 9.6, 0.55):
    ax.plot([tx - 0.52, tx + 0.52], [y, y + 0.08], color=P.edge("bract"), lw=0.7, zorder=5)
for ang in (10, 35, 60, 85, 110, 135, 160, 185, -10, -30):
    leaf(np.array([tx, 10.1]), ang, 3.2, z=3)
ax.add_patch(Ellipse((tx, 10.0), 0.9, 1.0, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=7))
for k in range(9):
    ax.plot([tx - 0.5 + 0.12 * k, tx - 1.4 + 0.35 * k], [1.4, 0.3], color=P.edge("neutral"), lw=0.8, zorder=3)
bio.callout(ax, (tx + 0.3, 10.0), (18.0, 12.6), "Single apical meristem (palm heart)")
bio.callout(ax, (tx + 0.5, 6.0), (17.4, 7.0), "Leaf scars")
bio.callout(ax, (tx + 0.8, 0.7), (17.4, 1.6), "Adventitious roots")

# ---- C: trunk section
bio.panel(ax, "C", (19.8, 13.7))
bio.label(ax, (23.2, 9.9), "Trunk section", size="title")
botany.stem_section(ax, (23.2, 5.4), 3.6, kind="monocot", seed=5)
bio.label(ax, (23.2, 1.2), "scattered bundles, no cambium, no rings", size="small")
bio.icon(ax, "phylopic/palm", at=(28.2, 11.6), height=3.4, color="plant")
