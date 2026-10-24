"""The orbital picture of the anomeric effect: Newman projections along the ring O5-C1 bond of
2-methoxytetrahydropyran (O5 in front, C1 behind). The ring bonds O5-C5 and C1-C2 are gauche,
as in the chair. With the methoxy group axial (left), the C1-OMe bond is antiperiplanar to one
lone pair of the ring oxygen, which can delocalize into the sigma* orbital of that bond
(n(O) -> sigma*(C-O), negative hyperconjugation). With the methoxy group equatorial (right), the
C1-OMe bond is antiperiplanar to the ring O5-C5 bond, and no lone pair is aligned with it."""

import math

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse

BLUE = "#2563eb"
RED = "#dc2626"
R = 1.0


def pol(cx, cy, ang, r):
    t = math.radians(ang)
    return cx + r * math.cos(t), cy + r * math.sin(t)


def newman(ax, cx, axial):
    ink = plt.rcParams["text.color"]
    ax.add_patch(Circle((cx, 0), R, fill=False, lw=1.6, color=ink))
    # back carbon C1: C2 at 150, then OMe and H at 30 / 270
    back = {150: "C2", 30: "OMe" if axial else "H", 270: "H" if axial else "OMe"}
    for ang, lab in back.items():
        x0, y0 = pol(cx, 0, ang, R)
        x1, y1 = pol(cx, 0, ang, 1.9)
        ax.plot([x0, x1], [y0, y1], color=RED if lab == "OMe" else ink, lw=1.8)
        tx, ty = pol(cx, 0, ang, 2.3)
        ax.text(tx, ty, lab, ha="center", va="center", fontsize=12, color=ink)
    # front oxygen O5: bond to C5 at 90, lone pairs at 210 and 330
    x1, y1 = pol(cx, 0, 90, 1.7)
    ax.plot([cx, x1], [0, y1], color=ink, lw=1.8)
    ax.text(*pol(cx, 0, 90, 2.05), "C5", ha="center", va="center", fontsize=12, color=ink)
    ax.text(cx + 0.28, 0.28, "O5", ha="left", va="bottom", fontsize=10, color=ink)
    for ang in (210, 330):
        ex, ey = pol(cx, 0, ang, 0.62)
        aligned = axial and ang == 210
        ax.add_patch(Ellipse((ex, ey), 0.95, 0.5, angle=ang, color=BLUE, alpha=0.45 if aligned else 0.2, lw=0))
        for d in (-0.09, 0.09):
            px, py = pol(ex, ey, ang + 90, d)
            ax.plot(px, py, "o", ms=3, color=ink)
    if axial:
        # sigma* lobe of C1-OMe on the far side of C1, pointing toward the anti lone pair
        sx, sy = pol(cx, 0, 210, 1.25)
        ax.add_patch(Ellipse((sx, sy), 0.7, 0.42, angle=210, color=RED, alpha=0.3, lw=0))
        ax.annotate("", xy=pol(cx, 0, 210, 1.05), xytext=pol(cx, 0, 210, 0.95),
                    arrowprops=dict(arrowstyle="->", color=ink, lw=1.2))
        ax.text(cx, -2.75, "axial OMe: n(O) anti to C1-OMe\n" + r"n(O) $\to$ $\sigma^*$(C-O) stabilizes", ha="center", va="center", fontsize=11, color=ink)
    else:
        ax.text(cx, -2.75, "equatorial OMe: C1-OMe anti to O5-C5\nno lone pair aligned", ha="center", va="center", fontsize=11, color=ink)


fig, ax = plt.subplots(figsize=(8.4, 4.4))
newman(ax, -3.0, True)
newman(ax, 3.0, False)
ax.set_xlim(-6.2, 6.2)
ax.set_ylim(-3.4, 2.7)
ax.set_aspect("equal")
ax.axis("off")
fig.subplots_adjust(0, 0, 1, 1)
