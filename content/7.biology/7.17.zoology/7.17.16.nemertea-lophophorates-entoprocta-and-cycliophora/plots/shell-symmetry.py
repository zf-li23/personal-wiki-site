# Two valves, two symmetries (schematic). Top row: a bivalve. Its valves are LEFT and RIGHT; the plane of
# bilateral symmetry of the body runs between them, so the two valves are mirror images of each other, while
# each valve is usually asymmetrical (inequilateral) from front to back. Bottom row: a brachiopod. Its valves
# are DORSAL and VENTRAL; the plane of symmetry cuts through both valves, so each valve is symmetrical about
# its own midline, while the two valves differ (the ventral valve is larger and carries the pedicle opening).
# Left: outside view of one valve (dorsal up); right: transverse section with the plane of symmetry (dashed).
import numpy as np
from matplotlib.patches import Circle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 13.0)
shell, body = "bone", "neutral"


def dashed(p, q):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge("negative"), lw=1.4, ls="--", zorder=30)


# ---------------- bivalve ----------------
bio.label(ax, (1.2, 12.6), "Bivalve (clam): left and right valves", size="normal", bold=True, ha="left")
bio.panel(ax, "A", (0.3, 12.6))
v = bio.smooth_closed([[1.6, 9.0], [2.6, 10.6], [3.6, 11.3], [5.4, 11.0], [7.6, 10.0], [8.2, 8.6], [6.8, 7.6],
                       [4.0, 7.4], [2.2, 7.9]])
bio.shape(ax, v, token=shell, zorder=5)
for s in (0.82, 0.64, 0.46):
    c = np.array([3.6, 11.2])
    ax.plot(c[0] + (v[:, 0] - c[0]) * s, c[1] + (v[:, 1] - c[1]) * s, color=P.edge(shell), lw=0.6, zorder=6)
bio.callout(ax, (3.6, 11.25), (7.0, 12.0), "Umbo (off-centre, pointing forward)")
bio.label(ax, (1.2, 7.0), "anterior", size="tiny", color=P.muted())
bio.label(ax, (8.6, 7.0), "posterior", size="tiny", color=P.muted())
bio.label(ax, (4.9, 6.6), "Left valve (outside view): no plane divides it into mirror halves", size="small", color=P.muted())
bio.panel(ax, "B", (12.3, 12.6))
cx, cy = 17.6, 9.4
t = np.linspace(-np.pi / 2, np.pi / 2, 60)
for sgn in (-1, 1):
    ax.plot(cx + sgn * (0.25 + 1.6 * np.cos(t)), cy + 2.0 * np.sin(t), color=P.edge(shell), lw=5, zorder=8,
            solid_capstyle="round")
bio.shape(ax, bio.smooth_closed([[cx, cy + 1.7], [cx + 1.1, cy + 0.6], [cx + 0.9, cy - 1.5], [cx, cy - 1.9],
                                  [cx - 0.9, cy - 1.5], [cx - 1.1, cy + 0.6]]), token=body, zorder=6)
ax.add_patch(Circle((cx, cy + 2.15), 0.18, facecolor=P.fill("neutral"),
                                                                edgecolor=P.edge("neutral"), zorder=9))
dashed((cx, cy - 2.8), (cx, cy + 2.8))
bio.label(ax, (cx - 2.6, cy), "Left\nvalve", size="small")
bio.label(ax, (cx + 2.6, cy), "Right\nvalve", size="small")
bio.callout(ax, (cx, cy + 2.15), (cx + 2.6, cy + 2.8), "Ligament and hinge (dorsal)")
bio.label(ax, (cx, cy - 3.2), "Plane of symmetry between the valves", size="small", color=P.edge("negative"))

# ---------------- brachiopod ----------------
bio.label(ax, (1.2, 5.9), "Brachiopod (lamp shell): dorsal and ventral valves", size="normal", bold=True, ha="left")
bio.panel(ax, "C", (0.3, 5.9))
c = np.array([4.9, 2.8])
th = np.linspace(0, 2 * np.pi, 120)
outline = np.c_[c[0] + 2.4 * np.sin(th), c[1] + 2.1 * np.cos(th) - 0.5 * np.cos(th) ** 2 * (np.cos(th) > 0)]
bio.shape(ax, outline, token=shell, zorder=5)
for s in (0.8, 0.6, 0.4):
    ax.plot(c[0] + (outline[:, 0] - c[0]) * s, c[1] + 1.6 + (outline[:, 1] - c[1] - 1.6) * s, color=P.edge(shell),
            lw=0.6, zorder=6)
ax.add_patch(Circle((c[0], c[1] + 1.75), 0.2, facecolor=P.surface(),
                                                                edgecolor=P.edge(shell), zorder=7))
dashed((c[0], c[1] - 2.6), (c[0], c[1] + 2.6))
bio.callout(ax, (c[0] + 0.1, c[1] + 1.8), (c[0] + 2.8, c[1] + 2.5), "Pedicle foramen (posterior)")
bio.label(ax, (c[0], 0.0), "Ventral valve: symmetrical about its midline", size="small", color=P.muted())
bio.panel(ax, "D", (12.3, 5.9))
cx, cy = 17.6, 2.6
xs = np.linspace(-1, 1, 60)
ax.plot(cx + 2.2 * xs, cy + 0.15 + 1.0 * (1 - xs ** 2), color=P.edge(shell), lw=5, zorder=8, solid_capstyle="round")
ax.plot(cx + 2.4 * xs, cy - 0.15 - 1.6 * (1 - xs ** 2), color=P.edge(shell), lw=5, zorder=8, solid_capstyle="round")
bio.shape(ax, bio.smooth_closed([[cx - 1.6, cy], [cx, cy + 0.8], [cx + 1.6, cy], [cx + 0.9, cy - 1.0], [cx, cy - 1.3],
                                  [cx - 0.9, cy - 1.0]]), token=body, zorder=6)
dashed((cx, cy - 2.4), (cx, cy + 1.9))
bio.label(ax, (cx + 3.6, cy + 0.9), "Dorsal (brachial) valve", size="small", ha="left")
bio.label(ax, (cx + 3.6, cy - 1.0), "Ventral (pedicle) valve", size="small", ha="left")
bio.label(ax, (cx, cy - 2.8), "Plane of symmetry through both valves", size="small", color=P.edge("negative"))
