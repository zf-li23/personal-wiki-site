# Torsion in gastropods, schematic dorsal views with anterior up (the animal's right is on the viewer's
# right). The visceral mass and mantle cavity rotate counterclockwise relative to the head and foot.
# A: pre-torsional; B: 90 degrees; C: 180 degrees (torted, streptoneurous); D: detorted heterobranch
# (mantle cavity back on the right, connectives uncrossed, the post-torsional right gill not regained).
import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, Wedge

P = bio.P
MANTLE, GUT, NERVE = "positive", "endoderm", "negative"
GILL_R, GILL_L = "protein", "dna"   # the pre-torsional right and left ctenidia


def wash(tok, k=0.55):
    return P.mix(P.fill(tok), P.surface(), 0.78 if P.is_dark() else k)


def unit(deg):
    a = np.radians(deg)
    return np.array([np.cos(a), np.sin(a)])


def gill(ax, base, direction, tok, n=5, L=0.75):
    d = direction / np.linalg.norm(direction)
    nn = np.array([-d[1], d[0]])
    tip = base + d * L
    ax.plot([base[0], tip[0]], [base[1], tip[1]], color=P.edge(tok), lw=1.6, zorder=9)
    for s in np.linspace(0.15, 0.95, n):
        c = base + d * L * s
        for sg in (-1, 1):
            q = c + nn * sg * 0.16 * (1.1 - s * 0.5)
            ax.plot([c[0], q[0]], [c[1], q[1]], color=P.edge(tok), lw=1.1, zorder=9)


def bez(a, b, c, n=60):
    t = np.linspace(0, 1, n)[:, None]
    return (1 - t) ** 2 * a + 2 * (1 - t) * t * b + t ** 2 * c


def animal(ax, cx, cy, angle, nerves_crossed, gills=("L", "R"), title="", sub=""):
    # foot and head (fixed)
    ax.add_patch(Ellipse((cx, cy - 0.2), 2.6, 7.0, facecolor=wash("muscle", 0.5), edgecolor=P.edge("muscle"), lw=1.0, zorder=2))
    ax.add_patch(Ellipse((cx, cy + 3.0), 1.8, 1.3, facecolor=wash("muscle", 0.35), edgecolor=P.edge("muscle"), lw=1.0, zorder=3))
    for sx in (-1, 1):
        ax.plot([cx + sx * 0.45, cx + sx * 0.9], [cy + 3.5, cy + 4.3], color=P.edge("muscle"), lw=2.2, zorder=3, solid_capstyle="round")
    c = np.array([cx, cy - 0.3])
    R = 1.75
    ax.add_patch(Circle(c, R, facecolor=wash("neutral", 0.65), edgecolor=P.edge("neutral"), lw=1.0, zorder=4))
    d = unit(angle - 90)          # direction of the mantle cavity from the centre
    left = np.array([d[1], -d[0]])  # the animal's (pre-torsional) left side of the visceral mass
    # mantle cavity: a wedge on the rim
    ax.add_patch(Wedge(tuple(c), R * 1.08, angle - 90 - 50, angle - 90 + 50, width=R * 0.62, facecolor=wash(MANTLE, 0.5),
                       edgecolor=P.edge(MANTLE), lw=1.0, zorder=5))
    inner = c + d * R * 0.72
    if "L" in gills:
        gill(ax, inner + left * 0.55, d, GILL_L)
    if "R" in gills:
        gill(ax, inner - left * 0.55, d, GILL_R)
    anus = c + d * R * 0.62
    mouth = np.array([cx, cy + 3.3])
    g = np.r_[bez(mouth, np.array([cx, cy + 1.6]), c + np.array([0, 0.4])), bez(c + np.array([0, 0.4]), c - d * 0.6 + left * 0.2, anus)]
    ax.plot(g[:, 0], g[:, 1], color=P.edge(GUT), lw=2.4, zorder=6, solid_capstyle="round")
    ax.add_patch(Circle(anus, 0.12, facecolor=P.edge(GUT), edgecolor="none", zorder=7))
    # nerves: pleural ganglia beside the oesophagus, visceral loop near the mantle cavity
    pl_l, pl_r = np.array([cx - 0.55, cy + 2.4]), np.array([cx + 0.55, cy + 2.4])
    if nerves_crossed:
        v_l, v_r = c + d * R * 0.35 + left * 0.75, c + d * R * 0.35 - left * 0.75
    else:  # euthyneury: connectives straight back on each side
        v_l, v_r = c + np.array([-0.75, -0.2]), c + np.array([0.75, -0.2])
    vg = (v_l + v_r) / 2 + (d * 0.25 if nerves_crossed else np.array([0, -0.25]))
    for a, b in ((pl_l, v_l), (pl_r, v_r)):
        mid = (a + b) / 2 + np.array([0, -0.2])
        q = bez(a, mid, b)
        ax.plot(q[:, 0], q[:, 1], color=P.edge(NERVE), lw=1.6, zorder=8)
    q = bez(v_l, vg, v_r)
    ax.plot(q[:, 0], q[:, 1], color=P.edge(NERVE), lw=1.6, zorder=8)
    for p in (pl_l, pl_r):
        ax.add_patch(Circle(p, 0.16, facecolor=P.fill(NERVE), edgecolor=P.edge(NERVE), lw=0.8, zorder=9))
    ax.add_patch(Circle(vg, 0.16, facecolor=P.fill(NERVE), edgecolor=P.edge(NERVE), lw=0.8, zorder=9))
    bio.label(ax, (cx, cy + 5.1), title, size="normal", bold=True)
    bio.label(ax, (cx, cy - 4.3), sub, size="small", color=P.muted())
    return dict(anus=anus, mantle=c + d * R * 0.95, vg=vg)


fig, ax = bio.canvas(25, 13.6)
cy = 7.0
A = animal(ax, 3.2, cy, 0, True, title="A  Before torsion", sub="Mantle cavity posterior")
B = animal(ax, 9.4, cy, 90, True, title="B  90°", sub="Mantle cavity on the right")
C = animal(ax, 15.6, cy, 180, True, title="C  180°: torted", sub="Mantle cavity anterior;\nconnectives crossed")
D = animal(ax, 21.8, cy, 90, False, gills=("R",), title="D  Detorted", sub="Connectives uncrossed;\none gill")
for x in (6.3, 12.5):
    bio.arrow(ax, (x - 0.5, cy + 0.3), (x + 0.5, cy + 0.3), kind="process", lw=1.2, head=0.22)
bio.callout(ax, C["anus"], (13.4, cy + 4.3), "Anus above the head", size="tiny")
bio.callout(ax, A["mantle"], (5.6, cy - 3.2), "Mantle cavity", size="tiny")
# legend
items = [(GILL_R, "Pre-torsional right ctenidium"), (GILL_L, "Pre-torsional left ctenidium"), (NERVE, "Pleural ganglia, connectives, visceral ganglion"),
         (GUT, "Gut and anus")]
for i, (tok, t) in enumerate(items):
    x, y = 1.2 + (i % 2) * 11.5, 1.3 - (i // 2) * 0.75
    ax.plot([x - 0.35, x + 0.35], [y, y], color=P.edge(tok), lw=2.4, zorder=9)
    bio.label(ax, (x + 0.6, y), t, size="small", ha="left")
bio.label(ax, (0.4, cy + 4.8), "Anterior", size="tiny", color=P.muted(), ha="left")
