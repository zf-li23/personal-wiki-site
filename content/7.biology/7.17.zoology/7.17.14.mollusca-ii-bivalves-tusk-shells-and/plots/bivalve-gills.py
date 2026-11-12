# Bivalve ctenidia in schematic transverse section (dorsal up): protobranch, filibranch, eulamellibranch and
# septibranch. Gill axis dark blue, filaments and lamellae light blue, shell beige, mantle green,
# visceral mass and foot grey; arrows show the water flow through the gills.
import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse

P = bio.P
AX, FIL, SHELL, MANTLE = "dna", "dna2", "bone", "positive"


def wash(tok, k=0.55):
    return P.mix(P.fill(tok), P.surface(), 0.78 if P.is_dark() else k)


def body(ax, cx, top):
    """Shell, mantle and visceral mass of a transverse section; returns key points."""
    t = np.linspace(0, 0.86 * np.pi, 80)
    for sx in (-1, 1):
        xs = cx + sx * (2.4 * np.sin(t))
        ys = top - 0.2 - 3.0 * (1 - np.cos(t))
        ax.plot(xs, ys, color=P.edge(SHELL), lw=6, zorder=3, solid_capstyle="round")
        ax.plot(cx + sx * (2.1 * np.sin(t)), top - 0.35 - 2.85 * (1 - np.cos(t)), color=P.edge(MANTLE), lw=2.4, zorder=4)
    ax.add_patch(Circle((cx, top + 0.05), 0.22, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.8, zorder=5))  # ligament
    v = bio.smooth_closed([(cx - 0.45, top - 0.5), (cx + 0.45, top - 0.5), (cx + 0.55, top - 2.6), (cx + 0.4, top - 4.9),
                           (cx, top - 5.6), (cx - 0.4, top - 4.9), (cx - 0.55, top - 2.6)])
    ax.fill(v[:, 0], v[:, 1], facecolor=wash("neutral", 0.6), edgecolor=P.edge("neutral"), lw=1.0, zorder=4)
    return dict(axL=(cx - 1.15, top - 0.9), axR=(cx + 1.15, top - 0.9))


def axis_dot(ax, p):
    ax.add_patch(Circle(p, 0.16, facecolor=P.fill(AX), edgecolor=P.edge(AX), lw=0.9, zorder=8))


def demibranch(ax, base, side, outer, depth, fused, lw=1.6):
    """A W-half: descending limb from the axis, ascending limb back up (outer or inner demibranch)."""
    bx, by = base
    dx = side * (0.45 if outer else -0.2)
    gap = side * (0.22 if outer else -0.22)
    x1, y1 = bx + dx, by - depth
    pts_d = [(bx, by), (x1, y1)]
    pts_a = [(x1, y1), (x1 + gap, y1 + 0.15), (x1 + gap * 1.2, by - 0.35)]
    for pts in (pts_d, pts_a):
        p = np.array(pts)
        ax.plot(p[:, 0], p[:, 1], color=P.edge(FIL), lw=lw, zorder=7, ls="-" if fused else (0, (2, 1.4)))
    if fused:  # interlamellar junctions
        for f in (0.3, 0.55, 0.8):
            ya = by - depth * f
            xa = bx + dx * f
            xb = x1 + gap * (1.2 - 0.6 * f) if f < 1 else x1 + gap
            ax.plot([xa, xa + gap * 1.0], [ya, ya], color=P.edge(FIL), lw=0.9, zorder=7)
    ax.add_patch(Circle((x1 + gap / 2, y1 + 0.02), 0.07, facecolor=P.edge(FIL), edgecolor="none", zorder=8))  # food groove


def flow(ax, a, b):
    bio.arrow(ax, a, b, kind="process", lw=0.9, head=0.15, color=P.muted())


fig, ax = bio.canvas(26.5, 10.4)
W, top = 6.6, 8.3
titles = [("A", "Protobranch", "Nucula"), ("B", "Filibranch", "Mytilus"), ("C", "Eulamellibranch", "Anodonta"),
          ("D", "Septibranch", "Cuspidaria")]
for i, (L, t, ex) in enumerate(titles):
    cx = 3.2 + i * W
    k = body(ax, cx, top)
    bio.label(ax, (cx, top + 1.5), f"{L}  {t}", size="normal", bold=True)
    bio.label(ax, (cx, top + 0.95), ex, size="small", italic=True, color=P.muted())
    for side, key in ((-1, "axL"), (1, "axR")):
        bx, by = k[key]
        if t == "Protobranch":
            u = np.array([side * 0.55, -0.85]); u /= np.linalg.norm(u)
            n = np.array([-u[1], u[0]])
            tip = np.array([bx, by]) + u * 1.2
            ax.plot([bx, tip[0]], [by, tip[1]], color=P.edge(AX), lw=1.8, zorder=7)
            for s in np.linspace(0.15, 0.95, 5):
                c = np.array([bx, by]) + u * 1.2 * s
                for sg in (-1, 1):
                    q = c + n * sg * 0.32 * (1.05 - s * 0.5)
                    ax.plot([c[0], q[0]], [c[1], q[1]], color=P.edge(FIL), lw=1.3, zorder=7)
        elif t in ("Filibranch", "Eulamellibranch"):
            fused = t == "Eulamellibranch"
            demibranch(ax, (bx, by), side, True, 3.2, fused)
            demibranch(ax, (bx, by), side, False, 3.0, fused)
            flow(ax, (bx + side * 0.15, by - 4.0), (bx + side * 0.2, by - 2.6))
        else:
            xs = np.linspace(cx + side * 0.55, cx + side * 2.05, 8)
            y = by - 0.9
            for a_, b_ in zip(xs[:-1:2], xs[1::2]):
                ax.plot([a_, b_], [y, y], color=P.edge("muscle"), lw=4.0, zorder=7, solid_capstyle="butt")
            flow(ax, (cx + side * 1.3, by - 2.4), (cx + side * 1.3, by - 1.2))
        axis_dot(ax, (bx, by))
    if i == 0:
        bio.callout(ax, (cx + 1.15, top - 0.9), (cx + 2.9, top + 0.3), "Gill axis", size="tiny")
        bio.callout(ax, (cx, top - 3.5), (cx - 0.2, 1.6), "Visceral mass and foot", size="tiny")
    if i == 1:
        bio.callout(ax, (cx + 1.55, top - 3.0), (cx + 3.0, 2.0), "Outer demibranch", size="tiny")
        bio.callout(ax, (cx + 0.8, top - 2.4), (cx + 0.6, 1.4), "Inner demibranch", size="tiny")
        bio.label(ax, (cx, 0.85), "filaments joined by ciliary junctions (dashed)", size="tiny", color=P.muted())
    if i == 2:
        bio.callout(ax, (cx + 1.25, top - 1.9), (cx + 3.0, 2.0), "Interlamellar junctions", size="tiny")
        bio.callout(ax, (cx + 1.4, top - 0.55), (cx + 2.9, top + 0.3), "Suprabranchial chamber", size="tiny")
        bio.label(ax, (cx, 0.85), "filaments fused into lamellae with ostia", size="tiny", color=P.muted())
    if i == 3:
        bio.callout(ax, (cx + 1.6, top - 1.8), (cx + 2.9, top + 0.3), "Muscular perforated septum", size="tiny")
        bio.label(ax, (cx, 0.85), "septum pumps water and prey", size="tiny", color=P.muted())
