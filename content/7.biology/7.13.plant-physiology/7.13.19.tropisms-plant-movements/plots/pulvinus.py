# Seismonastic movement of Mimosa pudica: the primary pulvinus at the base of the petiole (schematic, after
# the classic description of extensor and flexor motor cells; Sibaoka 1991). (A) Before stimulation the
# motor cells of the lower half (extensor) are turgid and hold the petiole up. (B) After a touch, an action
# potential reaches the pulvinus; the lower motor cells release K+ and Cl- (and water follows osmotically
# through aquaporins), lose turgor and shrink, and the petiole drops within about a second. Recovery, by
# H+-ATPase-driven reuptake of K+ and Cl-, takes 10-30 min.
import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon

P = bio.P
fig, ax = bio.canvas(16, 7.8)


def pulvinus(cx, cy, drop):
    # stem
    ax.add_patch(FancyBboxPatch((cx - 0.45, 0.4), 0.9, 6.6, boxstyle="round,pad=0,rounding_size=0.3",
                                facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=2))
    ang = np.radians(25 - drop)
    # petiole
    base = np.array([cx + 1.9, cy])
    tip = base + 4.2 * np.array([np.cos(ang), np.sin(ang)])
    nrm = np.array([-np.sin(ang), np.cos(ang)]) * 0.17
    ax.add_patch(Polygon([base + nrm, tip + nrm * 0.6, tip - nrm * 0.6, base - nrm], closed=True,
                         facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=3))
    # pulvinus body with upper and lower motor cells
    ax.add_patch(Ellipse((cx + 1.15, cy), 1.9, 1.5, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=4))
    for k in range(4):
        x = cx + 0.55 + k * 0.4
        ax.add_patch(Ellipse((x, cy + 0.42), 0.34, 0.42, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cell_wall"),
                             lw=0.8, zorder=5))
        rl = 0.42 if drop == 0 else 0.26
        ax.add_patch(Ellipse((x, cy - 0.40), 0.36 if drop == 0 else 0.3, rl, facecolor=P.fill("cytoplasm"),
                             edgecolor=P.edge("cell_wall"), lw=0.8, zorder=5))
    ax.plot([cx + 0.35, cx + 1.95], [cy, cy], color=P.edge("xylem"), lw=1.4, zorder=6)
    return tip


bio.panel(ax, "A", (0.1, 7.7))
bio.label(ax, (3.6, 7.35), "Before touch: lower motor cells turgid", size="small", bold=True)
t1 = pulvinus(1.4, 4.2, 0)
bio.callout(ax, (2.15, 3.8), (2.6, 2.0), "Extensor (lower) cells: high K⁺, Cl⁻", size="tiny")
bio.callout(ax, (2.15, 4.62), (2.9, 6.6), "Flexor (upper) cells", size="tiny")
bio.callout(ax, (3.0, 4.2), (4.4, 5.2), "Vascular strand", size="tiny")
bio.panel(ax, "B", (8.2, 7.7))
bio.label(ax, (11.8, 7.35), "Within ~1 s after touch: petiole drops", size="small", bold=True)
t2 = pulvinus(9.5, 4.2, 65)
for k in range(3):
    x = 10.05 + k * 0.4
    bio.arrow(ax, (x, 3.75), (x + 0.1, 2.85), kind="process", color=P.fill("k"), lw=1.2, head=0.15)
bio.label(ax, (11.0, 2.45), "K⁺, Cl⁻, water leave lower cells", size="tiny")
bio.arrow(ax, (12.6, 6.0), (13.4, 3.0), kind="activation", bend=-0.25)
bio.label(ax, (14.0, 5.2), "action potential\n(~2 cm/s)", size="tiny", color=P.muted())
bio.label(ax, (12.6, 0.6), "Recovery: H⁺-ATPase-driven K⁺, Cl⁻ reuptake, 10–30 min", size="tiny", color=P.muted())
