"""Home range and core area from simulated radio-tracking fixes.

Two neighbouring animals move around their own centres of activity (a discrete Ornstein-Uhlenbeck process, i.e.
a random walk with attraction to a home site, plus a second, smaller attraction to a favoured spot such as a den).
A: the fixes, the minimum convex polygon (MCP) of each animal and the 95 % and 50 % contours of a Gaussian
kernel density estimate; the 50 % contour is the core area. The home ranges overlap, the core areas do not.
B: estimated area against the number of fixes for animal 1: both estimates grow with sampling effort, the MCP
most steeply, because it is set by the few most extreme fixes. One simulation unit is 100 m, so one square unit is 1 ha.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(2)


def track(center, den, n=1500):
    x = np.zeros((n, 2))
    x[0] = center
    for t in range(1, n):
        pull = 0.04 * (center - x[t - 1]) + 0.02 * (den - x[t - 1])
        x[t] = x[t - 1] + pull + rng.normal(0, 0.6, 2)
    return x[::5]


def hull(pts):
    pts = sorted(map(tuple, pts))

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return np.array(lower[:-1] + upper[:-1])


def area(poly):
    x, y = poly[:, 0], poly[:, 1]
    return 0.5 * abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


gx, gy = np.meshgrid(np.linspace(-5, 14, 230), np.linspace(-7, 7, 170))
cell = (gx[0, 1] - gx[0, 0]) * (gy[1, 0] - gy[0, 0])


def kde(pts, h=0.6):
    d = np.zeros_like(gx)
    for p in pts:
        d += np.exp(-((gx - p[0]) ** 2 + (gy - p[1]) ** 2) / (2 * h * h))
    return d / d.sum()


def level(d, frac):
    s = np.sort(d.ravel())[::-1]
    c = np.cumsum(s)
    return s[np.searchsorted(c, frac)]


animals = [track(np.array([2.0, 0.5]), np.array([0.5, 2.0])), track(np.array([7.0, 0.0]), np.array([8.5, -1.5]))]
fig, ax = bio.canvas(32.0, 11.0)
pa = Ch.axes_at(ax, (1.2, 1.2, 17.0, 9.2))
for pts, tok, name in zip(animals, ("rna", "dna"), ("animal 1", "animal 2")):
    col = Ch.line(tok)
    pa.plot(pts[:, 0], pts[:, 1], ".", ms=2.2, color=col, alpha=0.5)
    h = hull(pts)
    hh = np.vstack([h, h[:1]])
    pa.plot(hh[:, 0], hh[:, 1], color=col, lw=0.9, ls=(0, (4, 2)))
    d = kde(pts)
    pa.contour(gx, gy, d, levels=[level(d, 0.95)], colors=[col], linewidths=1.3)
    pa.contourf(gx, gy, d, levels=[level(d, 0.5), d.max() + 1], colors=[col], alpha=0.25)
    pa.text(pts[:, 0].mean(), pts[:, 1].max() + 0.3, name, color=col, fontsize=FS["small"], ha="center")
pa.set_aspect("equal")
pa.set_xlim(-5, 14)
pa.set_ylim(-7, 7)
pa.set_xticks([])
pa.set_yticks([])
for s in pa.spines.values():
    s.set_visible(False)
bio.scale_bar(ax, (14.6, 1.6), 2 * 9.2 / 14, "200 m")
bio.label(ax, (1.4, 0.55), "dashed: minimum convex polygon;  line: 95 % kernel (home range);  shaded: 50 % kernel "
          "(core area)", size="tiny", color=P.muted(), ha="left")
bio.panel(ax, "A", (0.3, 10.9))

pb = Ch.axes_at(ax, (22.4, 1.8, 8.6, 7.8))
pts = animals[0]
ns = np.arange(10, len(pts) + 1, 10)
mcp = [area(hull(pts[:n])) for n in ns]
ker = []
for n in ns:
    d = kde(pts[:n])
    ker.append((d >= level(d, 0.95)).sum() * cell)
pb.plot(ns, mcp, color=Ch.line("rna"), lw=1.5, ls=(0, (4, 2)))
pb.plot(ns, ker, color=Ch.line("rna"), lw=1.7)
pb.text(ns[12], mcp[12] - 3, "MCP", color=Ch.line("rna"), fontsize=FS["tiny"], ha="left", va="top")
pb.text(ns[8], ker[8] + 3, "95 % kernel", color=Ch.line("rna"), fontsize=FS["tiny"], ha="right", va="bottom")
pb.set_xlim(0, ns[-1])
pb.set_ylim(0, max(max(mcp), max(ker)) * 1.15)
Ch.style_axes(pb, "number of fixes", "estimated area / ha")
bio.panel(ax, "B", (20.2, 10.9))
