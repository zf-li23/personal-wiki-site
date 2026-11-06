# Classic experiments that led to the discovery of auxin (oat / canary-grass coleoptiles, schematic).
# A Darwin 1880, B Boysen-Jensen 1913, C Paal 1919, D Went 1926-1928.
import math

import numpy as np
import wikibio as bio
from matplotlib.patches import Polygon
from wikibio import P

W, H = 30, 7.0
fig, ax = bio.canvas(W, H)
WID = 0.42


def centerline(x, y, h, bend):
    """Points of a coleoptile axis of height h; the upper 55% bends by `bend` degrees (+ = right)."""
    s = np.linspace(0, h, 80)
    pts, ang, px, py = [], 0.0, x, y
    ds = s[1] - s[0]
    for si in s:
        pts.append((px, py))
        if si > 0.45 * h:
            ang += math.radians(bend) * ds / (0.55 * h)
        px += ds * math.sin(ang)
        py += ds * math.cos(ang)
    return np.array(pts)


def coleoptile(x, y, h=3.0, bend=0.0, tip=True):
    c = centerline(x, y, h, bend)
    d = np.gradient(c, axis=0)
    d /= np.linalg.norm(d, axis=1)[:, None]
    n = np.c_[-d[:, 1], d[:, 0]]
    left, right = c + n * WID / 2, c - n * WID / 2
    top = c[-1]
    if tip:
        a0 = math.atan2(n[-1, 1], n[-1, 0])
        arc = [top + WID / 2 * np.array([math.cos(a0 - t), math.sin(a0 - t)]) for t in np.linspace(0, math.pi, 20)]
        outline = np.vstack([left, arc, right[::-1]])
    else:
        outline = np.vstack([left, right[::-1]])
    ax.add_patch(Polygon(outline, closed=True, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.1, zorder=6))
    ax.plot([x - 0.6, x + 0.6], [y, y], color=P.muted(), lw=1.2, zorder=5)
    return top, d[-1]


def light(x, y):
    for dy in (-0.35, 0.0, 0.35):
        bio.arrow(ax, (x, y + dy), (x + 0.9, y + dy), kind="process", color=P.fill("highlight"), lw=1.6, head=0.2)
    bio.label(ax, (x + 0.45, y + 0.75), "Light", size="tiny")


def cap(top, dirn, opaque=True):
    n = np.array([-dirn[1], dirn[0]])
    pts = [top - dirn * 0.55 + n * 0.3, top + dirn * 0.32, top - dirn * 0.55 - n * 0.3]
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.edge("neutral") if opaque else "none", edgecolor=P.edge("neutral"), lw=1.1, zorder=8))


def band(x, y, w, h, token, text=None):
    bio.box(ax, (x, y), w, h, token=token, radius=0.05, lw=0.9, zorder=9)
    if text:
        bio.label(ax, (x + w / 2 + 0.15, y), text, size="tiny", ha="left")


base = 1.6
# ---------------- A: Darwin
bio.panel(ax, "A", (0.3, 6.6))
bio.label(ax, (4.0, 6.6), "Darwin (1880)", size="small")
light(0.3, 4.3)
coleoptile(1.6, base, bend=28)
bio.label(ax, (1.6, 0.9), "intact", size="tiny")
t, d = coleoptile(3.4, base, h=2.3, tip=False)
bio.label(ax, (3.4, 0.9), "tip cut", size="tiny")
t, d = coleoptile(5.0, base)
cap(t, d)
bio.label(ax, (5.0, 0.9), "opaque cap", size="tiny")
c = centerline(6.6, base, 3.0, 26)
coleoptile(6.6, base, bend=26)
band(6.6, base + 0.9, 0.62, 1.7, "neutral")
bio.label(ax, (6.6, 0.9), "base shaded", size="tiny")

# ---------------- B: Boysen-Jensen
bio.panel(ax, "B", (8.2, 6.6))
bio.label(ax, (11.2, 6.6), "Boysen-Jensen (1913)", size="small")
light(8.4, 4.3)
coleoptile(10.0, base, bend=26)
band(10.0, base + 1.55, 0.7, 0.28, "carbohydrate")
bio.label(ax, (10.0, 0.9), "gelatin", size="tiny")
coleoptile(12.4, base, bend=0)
ax.plot([12.4 + 0.1, 12.4 + 0.1], [base + 1.2, base + 2.2], color=P.ink(), lw=2.4, zorder=9)
bio.label(ax, (12.85, base + 1.7), "mica", size="tiny", ha="left")
bio.label(ax, (12.4, 0.9), "mica, shaded side", size="tiny")

# ---------------- C: Paal
bio.panel(ax, "C", (14.6, 6.6))
bio.label(ax, (17.3, 6.6), "Paál (1919), darkness", size="small")
c = centerline(16.6, base, 2.3, -30)
coleoptile(16.6, base, h=2.3, bend=-30, tip=False)
top = c[-1]
d = c[-1] - c[-2]
d /= np.linalg.norm(d)
n = np.array([-d[1], d[0]])
tipc = top - n * 0.11 + d * 0.03
ax.add_patch(Polygon([tipc - n * 0.1, tipc - n * 0.1 + d * 0.3, tipc + d * 0.5, tipc + n * 0.1 + d * 0.3, tipc + n * 0.1],
                     closed=True, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.1, zorder=7))
bio.label(ax, (16.6, 0.9), "tip placed on one side", size="tiny")
bio.label(ax, (18.6, 4.6), "tip on the right half:\nbends away from it", size="tiny")

# ---------------- D: Went
bio.panel(ax, "D", (20.6, 6.6))
bio.label(ax, (25.3, 6.6), "Went (1926–1928)", size="small")
# tips on agar
for xx in (21.6, 22.4):
    ax.add_patch(Polygon([(xx - 0.21, 3.25), (xx - 0.21, 3.6), (xx, 3.95), (xx + 0.21, 3.6), (xx + 0.21, 3.25)], closed=True,
                         facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=7))
band(22.0, 3.05, 1.5, 0.4, "lipid")
bio.label(ax, (22.0, 2.3), "tips on agar:\nauxin diffuses in", size="tiny")
bio.arrow(ax, (23.2, 3.1), (24.3, 3.1), kind="process")
# decapitated coleoptile with block on the left
c = centerline(25.6, base, 2.5, 32)
coleoptile(25.6, base, h=2.5, bend=32, tip=False)
top = c[-1]
d = c[-1] - c[-2]
d /= np.linalg.norm(d)
n = np.array([-d[1], d[0]])
bp = top + n * 0.1 + d * 0.01
ax.add_patch(Polygon([bp - n * 0.11, bp + n * 0.11, bp + n * 0.11 + d * 0.3, bp - n * 0.11 + d * 0.3], closed=True,
                     facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.9, zorder=8))
# angle
ax.plot([25.6, 25.6], [base + 1.1, base + 3.4], color=P.muted(), lw=0.8, ls="--", zorder=4)
bio.label(ax, (25.95, base + 3.15), "α", size="small", italic=True)
bio.label(ax, (25.6, 0.9), "block on one side", size="tiny")
# calibration inset
x0, y0, w, h = 27.4, 3.3, 2.2, 2.6
ax.plot([x0, x0, x0 + w], [y0 + h, y0, y0], color=P.muted(), lw=0.9)
m = np.linspace(0, 1, 30)
ax.plot(x0 + m * w, y0 + h * 0.92 * (1 - np.exp(-1.4 * m)) / (1 - np.exp(-1.4)), color=P.edge("plant"), lw=1.6)
ax.plot([x0, x0 + 0.5 * w], [y0, y0 + h * 0.92 * 0.5 * 1.4 / (1 - np.exp(-1.4)) * 0.62], color=P.muted(), lw=0.8, ls=":")
bio.label(ax, (x0 + w / 2, y0 - 0.35), "auxin in block", size="tiny")
bio.label(ax, (x0 - 0.3, y0 + h / 2), "α", size="small", italic=True)
