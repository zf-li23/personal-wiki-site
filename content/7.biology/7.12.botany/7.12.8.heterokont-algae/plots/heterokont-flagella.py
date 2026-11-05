"""The heterokont zoospore and its flagella. A: zoospore of a brown alga with laterally inserted flagella:
the long anterior flagellum bears two rows of tripartite tubular hairs, the short posterior one is smooth, with
a paraflagellar swelling at its base lying over the eyespot in the plastid. B: one tripartite hair (base,
tubular shaft, terminal filaments). C: thrust reversal. A base-to-tip wave on a smooth flagellum pushes water
towards the tip and the cell moves backwards; the same wave on a flagellum with stiff hairs drives water the
other way, so the cell is pulled forwards. Blue arrows: water; black arrows: cell movement."""
import numpy as np
from matplotlib.patches import Ellipse, Circle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 12)


def wave(p0, ang, L, amp=0.22, waves=2.0, hairs=False, hl=0.32, lw=1.6):
    t = np.linspace(0, 1, 200)
    a = np.radians(ang)
    u, n = np.array([np.cos(a), np.sin(a)]), np.array([-np.sin(a), np.cos(a)])
    off = amp * np.minimum(1, 4 * t) * np.sin(2 * np.pi * waves * t)
    pts = p0 + np.outer(t * L, u) + np.outer(off, n)
    ax.plot(pts[:, 0], pts[:, 1], color=P.ink(), lw=lw, zorder=8, solid_capstyle="round")
    if hairs:
        d = np.gradient(pts, axis=0)
        d /= np.linalg.norm(d, axis=1)[:, None]
        nn = np.c_[-d[:, 1], d[:, 0]]
        for k in range(14, 200, 9):
            for sg in (1, -1):
                q = pts[k] + sg * nn[k] * hl
                ax.plot([pts[k, 0], q[0]], [pts[k, 1], q[1]], color=P.muted(), lw=0.7, zorder=7)
    return pts


# A zoospore
bio.panel(ax, "A", (0.2, 11.8))
c = np.array([6.0, 5.4])
ax.add_patch(Ellipse(c, 3.6, 2.6, angle=20, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("highlight"), lw=1.4, zorder=4))
ax.add_patch(Ellipse(c + np.array([0.3, -0.3]), 1.6, 1.0, angle=20, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=5))
ax.add_patch(Circle(c + np.array([0.9, 0.05]), 0.2, color=P.edge("negative"), zorder=6))
ax.add_patch(Circle(c + np.array([-0.7, 0.2]), 0.42, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=1.0, zorder=5))
base = c + np.array([0.4, 1.1])
wave(base, 145, 5.2, hairs=True)
pts = wave(base + np.array([0.2, -0.05]), 0, 4.6, amp=0.18)
ax.add_patch(Ellipse(base + np.array([0.6, 0.0]), 0.5, 0.28, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.9, zorder=9))
bio.callout(ax, (2.2, 7.9), (1.0, 10.6), "anterior tinsel flagellum", size="tiny")
bio.callout(ax, (9.6, 6.5), (9.2, 8.6), "posterior smooth flagellum", size="tiny")
bio.callout(ax, tuple(base + np.array([0.6, 0.0])), (8.6, 3.0), "paraflagellar swelling", size="tiny")
bio.callout(ax, tuple(c + np.array([0.9, 0.05])), (8.2, 2.1), "eyespot in plastid", size="tiny")
bio.callout(ax, tuple(c + np.array([-0.7, 0.2])), (2.6, 2.6), "nucleus", size="tiny")

# B hair
bio.panel(ax, "B", (11.6, 11.8))
x0, y0 = 13.0, 3.0
ax.plot([x0, x0], [y0, y0 + 0.5], color=P.edge("protein"), lw=3, solid_capstyle="round")
ax.plot([x0, x0], [y0 + 0.5, y0 + 5.0], color=P.edge("protein"), lw=6, solid_capstyle="butt")
ax.plot([x0, x0], [y0 + 0.5, y0 + 5.0], color=P.fill("cytoplasm"), lw=2.5, solid_capstyle="butt")
for dx in (-0.12, 0.0, 0.12):
    ax.plot([x0 + dx * 0.2, x0 + dx * 2.5], [y0 + 5.0, y0 + 6.4], color=P.edge("protein"), lw=0.9)
ax.plot([x0 - 1.2, x0 + 1.2], [y0 - 0.1, y0 - 0.1], color=P.ink(), lw=3)
bio.label(ax, (x0 + 1.4, y0 - 0.1), "flagellar membrane", size="tiny", ha="left")
bio.label(ax, (x0 + 0.6, y0 + 0.3), "base", size="tiny", ha="left")
bio.label(ax, (x0 + 0.6, y0 + 2.8), "tubular shaft", size="tiny", ha="left")
bio.label(ax, (x0 + 0.6, y0 + 6.1), "terminal filaments", size="tiny", ha="left")

# C thrust reversal
bio.panel(ax, "C", (17.8, 11.8))
for row, (y, hairs, txt) in enumerate(((8.6, False, "smooth flagellum"), (3.6, True, "tinsel flagellum"))):
    cc = np.array([20.0, y])
    ax.add_patch(Ellipse(cc, 1.6, 1.1, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("highlight"), lw=1.2, zorder=4))
    wave(cc + np.array([0.8, 0]), 0, 6.0, amp=0.3, hairs=hairs, hl=0.35)
    bio.label(ax, (23.8, y + 1.5), txt, size="small")
    bio.arrow(ax, (22.0, y - 0.9), (26.2, y - 0.9), kind="process", head=0.16, color=P.muted(), dashed=True)
    bio.label(ax, (21.6, y - 1.35), "wave base to tip", size="tiny", ha="left", color=P.muted())
    if not hairs:
        bio.arrow(ax, (27.4, y + 0.6), (29.4, y + 0.6), kind="process", color=P.edge("dna"), head=0.16)
        bio.arrow(ax, (19.4, y + 0.9), (18.2, y + 0.9), kind="process", head=0.18)
        bio.label(ax, (28.4, y + 1.0), "water", size="tiny", color=P.edge("dna"))
        bio.label(ax, (18.8, y + 1.35), "cell", size="tiny")
    else:
        bio.arrow(ax, (29.4, y + 0.6), (27.4, y + 0.6), kind="process", color=P.edge("dna"), head=0.16)
        bio.arrow(ax, (20.6, y + 0.9), (21.8, y + 0.9), kind="process", head=0.18)
        bio.label(ax, (28.4, y + 1.0), "water", size="tiny", color=P.edge("dna"))
        bio.label(ax, (21.2, y + 1.35), "cell", size="tiny")
