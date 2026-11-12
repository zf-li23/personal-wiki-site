# Optical designs of compound eyes (schematic sections; light from a distant point arrives as parallel rays).
# A apposition: pigment isolates each ommatidium, the rhabdom lies just below the cone; only the ommatidium
# whose axis points at the source receives its light. B refracting superposition: the cones redirect rays from
# several facets across the clear zone onto one rhabdom of the deep retina. C neural superposition (flies):
# each ommatidium has separate rhabdomeres (R1-R6 around the central R7/8) looking in different directions; the
# receptors in neighbouring ommatidia that view the same point send their axons to one lamina cartridge.
import numpy as np
from matplotlib.patches import Ellipse, Circle, Polygon
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(33, 13)


def rot(v, a):
    c, s = np.cos(a), np.sin(a)
    return np.array([c * v[0] - s * v[1], s * v[0] + c * v[1]])


def ommatidium(c, ang, kind, lit=False):
    """c: centre of the facet; ang: axis angle (rad from vertical, positive = to the left)."""
    u = rot(np.array([0, -1.0]), ang)   # inward axis
    n = rot(np.array([1.0, 0]), ang)    # across
    w = 0.38
    # facet lens
    ax.add_patch(Ellipse(c, 2 * w, 0.32, angle=np.degrees(ang), facecolor=P.fill("er"), edgecolor=P.edge("er"), lw=0.6, zorder=6))
    cone_top, cone_tip = c + 0.15 * u, c + 1.2 * u
    ax.add_patch(Polygon([cone_top - w * 0.9 * n, cone_top + w * 0.9 * n, cone_tip + 0.06 * n, cone_tip - 0.06 * n],
                         closed=True, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=0.6, zorder=6))
    if kind == "app":
        pig = [c + 0.15 * u - w * n, c + 4.2 * u - w * n, c + 4.2 * u + w * n, c + 0.15 * u + w * n]
        ax.plot(*np.array([pig[0], pig[1]]).T, color=P.edge("neutral"), lw=3.0, zorder=5)
        ax.plot(*np.array([pig[2], pig[3]]).T, color=P.edge("neutral"), lw=3.0, zorder=5)
        a, b = cone_tip, c + 4.1 * u
    elif kind == "sup":
        ax.plot(*np.array([c + 0.15 * u - w * n, c + 1.3 * u - w * n]).T, color=P.edge("neutral"), lw=3.0, zorder=5)
        a, b = c + 3.3 * u, c + 5.2 * u
    tok = "negative" if lit else "rna"
    ax.plot(*np.array([a, b]).T, color=P.fill(tok) if not lit else P.edge(tok), lw=4.0 if lit else 3.0, zorder=7,
            solid_capstyle="butt")
    return u, n


def eye(x0, kind, title):
    cx, cy, R = x0 + 4.8, 0.5, 9.5
    angs = np.radians(np.arange(-24, 25, 8))
    src = np.radians(16)                    # light from the upper left
    centers = []
    for a in angs:
        c = np.array([cx, cy]) + R * np.array([-np.sin(a), np.cos(a)])
        centers.append(c)
        lit = (kind == "app" and abs(a - src) < 1e-6) or (kind == "sup" and abs(a) < 1e-6)
        ommatidium(c, a, kind, lit=lit)
    d = rot(np.array([0, -1.0]), src)       # ray direction
    if kind == "app":
        c = centers[list(np.round(np.degrees(angs))).index(16)]
        for off in (-0.22, 0, 0.22):
            p0 = c + rot(np.array([off, 0]), src) - 2.4 * d
            ax.annotate("", xy=c + 3.3 * d + rot(np.array([off * 0.1, 0]), src), xytext=p0,
                        arrowprops=dict(arrowstyle="-|>", color=P.edge("highlight"), lw=0.8), zorder=9)
        for c2 in centers[:3]:
            p0 = c2 - 2.0 * d
            ax.annotate("", xy=c2 + 0.5 * d, xytext=p0, arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=0.6), zorder=9)
        bio.callout(ax, centers[0] + 2.2 * rot(np.array([0, -1.0]), angs[0]) + 0.4 * rot(np.array([1, 0]), angs[0]),
                    (x0 + 9.4, 6.3), "Screening pigment", size="tiny")
    else:
        target = np.array([cx, cy]) + (R - 4.25) * np.array([0, 1.0])
        for c, a in zip(centers, angs):
            if abs(np.degrees(a)) > 17:
                continue
            p0 = c - 2.4 * np.array([0, -1.0])
            tip = c + 1.2 * rot(np.array([0, -1.0]), a)
            ax.plot([p0[0], c[0], tip[0], target[0]], [p0[1], c[1], tip[1], target[1]], color=P.edge("highlight"), lw=0.8, zorder=9)
        bio.label(ax, (cx + 2.6, cy + R - 3.0), "clear zone", size="tiny", color=P.muted())
        bio.callout(ax, target, (x0 + 9.6, 4.0), "Rhabdom receiving light", size="tiny")
    bio.label(ax, (cx, 12.6), title, size="small", bold=True)
    if kind == "app":
        i, j, lx = -1, -2, x0 + 0.2
    else:
        i, j, lx = 0, 1, x0 + 9.6
    bio.callout(ax, centers[i], (lx, 10.9), "Facet lens", size="tiny")
    cc = centers[j] + 0.7 * rot(np.array([0, -1.0]), angs[j])
    bio.callout(ax, cc, (lx, 9.3), "Crystalline cone", size="tiny")
    rr = centers[i] + (3.0 if kind == "app" else 4.3) * rot(np.array([0, -1.0]), angs[i])
    bio.callout(ax, rr, (lx, 6.0 if kind == "app" else 2.6), "Rhabdom", size="tiny")


eye(0.0, "app", "A  Apposition eye")
eye(10.0, "sup", "B  Superposition eye")

# ---- C neural superposition
x0 = 23.0
bio.label(ax, (x0 + 5.0, 12.6), "C  Neural superposition (flies)", size="small", bold=True)
cents = [x0 + 2.0, x0 + 5.0, x0 + 8.0]
offs = [(0.0, 0.55), (0.48, 0.28), (0.48, -0.28), (0.0, -0.55), (-0.48, -0.28), (-0.48, 0.28)]
chosen = [2, 1, 5]   # which peripheral rhabdomere of each ommatidium looks at the same point
cart = (x0 + 5.0, 2.2)
for k, cx in enumerate(cents):
    cy = 8.8
    ax.add_patch(Circle((cx, cy), 1.05, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8, zorder=5))
    ax.add_patch(Circle((cx, cy), 0.16, facecolor=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.5, zorder=7))
    for j, (dx, dy) in enumerate(offs):
        hl = j == chosen[k]
        ax.add_patch(Circle((cx + dx, cy + dy), 0.17, facecolor=P.edge("negative") if hl else P.fill("rna"),
                            edgecolor=P.edge("negative" if hl else "rna"), lw=0.5, zorder=7))
        if hl:
            ax.plot([cx + dx, cart[0] + (k - 1) * 0.25], [cy + dy - 0.17, cart[1] + 0.5], color=P.edge("negative"), lw=1.0, zorder=6)
    bio.label(ax, (cx, 10.3), "ommatidium %d" % (k + 1), size="tiny", color=P.muted())
ax.add_patch(Ellipse(cart, 2.0, 1.0, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.8, zorder=6))
bio.label(ax, (cart[0], cart[1] - 1.0), "one lamina cartridge", size="tiny")
bio.callout(ax, (cents[0] - 0.48, 8.8 + 0.28), (x0 + 0.1, 11.4), "R1-R6", size="tiny")
bio.callout(ax, (cents[0], 8.8), (x0 + 0.1, 6.3), "R7/R8 (central)", size="tiny")
bio.label(ax, (x0 + 5.0, 5.4), "receptors viewing the same point (red)", size="tiny", color=P.muted())
bio.label(ax, (x0 + 5.0, 4.9), "converge on the same cartridge", size="tiny", color=P.muted())
