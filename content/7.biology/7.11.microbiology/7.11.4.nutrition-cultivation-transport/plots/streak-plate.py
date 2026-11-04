"""The four-sector streak plate. A: streak pattern; each sector starts from the end of the previous one
(the loop is sterilized between sectors). B: simulated result for a mixture of two bacteria: the
number of cells deposited per unit length falls about tenfold per sector (Poisson-distributed along the
streak lines), so sector 1 is confluent and sector 4 has separate colonies of both kinds."""

import numpy as np
from matplotlib.patches import Circle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22.0, 10.6)
rng = np.random.default_rng(7)
R = 4.3


def dish(c):
    ax.add_patch(Circle(c, R, facecolor=P.mix(P.fill("highlight"), P.surface(), 0.75), edgecolor=P.edge("neutral"),
                        lw=2.0, zorder=2))
    ax.add_patch(Circle(c, R - 0.18, facecolor="none", edgecolor=P.muted(), lw=0.6, zorder=2))


def sector_paths(c):
    """Zigzag streak lines for four sectors (in polar order), each beginning where the last ended."""
    cx, cy = c
    paths = []
    for k, (a0, a1) in enumerate([(200, 250), (290, 340), (20, 70), (110, 160)]):
        a = np.radians(np.linspace(a0, a1, 11))
        pts = []
        for j, t in enumerate(a):
            r = 3.6 if j % 2 == 0 else 2.2
            pts.append((cx + r * np.cos(t), cy + r * np.sin(t)))
        if k > 0:  # start inside the previous sector
            pts.insert(0, paths[-1][-2])
        paths.append(np.array(pts))
    return paths


def polyline_points(path, n):
    seg = np.diff(path, axis=0)
    L = np.hypot(*seg.T)
    s = np.sort(rng.uniform(0, L.sum(), n))
    out = []
    cum = np.concatenate([[0], np.cumsum(L)])
    for v in s:
        i = min(np.searchsorted(cum, v) - 1, len(seg) - 1)
        f = (v - cum[i]) / L[i]
        out.append(path[i] + f * seg[i])
    return np.array(out) if out else np.zeros((0, 2))


cA, cB = (5.3, 5.0), (16.4, 5.0)
bio.panel(ax, "A", (0.3, 10.3))
bio.panel(ax, "B", (11.4, 10.3))
for c in (cA, cB):
    dish(c)
pA = sector_paths(cA)
cols = [P.edge("protein"), P.edge("enzyme"), P.edge("drug"), P.edge("positive")]
for k, p in enumerate(pA):
    ax.plot(p[:, 0], p[:, 1], color=cols[k], lw=1.6, zorder=4, solid_capstyle="round", solid_joinstyle="round")
    mid = p[len(p) // 2]
    bio.label(ax, (cA[0] + 0.55 * (mid[0] - cA[0]), cA[1] + 0.55 * (mid[1] - cA[1])), str(k + 1),
              size="small", bold=True, color=cols[k])
    if k > 0:
        bio.arrow(ax, tuple(p[0] + (p[1] - p[0]) * 0.05), tuple(p[0] + (p[1] - p[0]) * 0.45), kind="process", color=cols[k],
                  lw=1.0, head=0.16, zorder=6)
bio.label(ax, (cA[0], 0.25), "sterilize the loop between sectors", size="tiny", color=P.muted())

pB = sector_paths(cB)
counts = [900, 70, 20, 7]
for k, p in enumerate(pB):
    if k == 0:
        ax.plot(p[:, 0], p[:, 1], color=P.edge("lipid"), lw=7, alpha=0.55, zorder=3, solid_capstyle="round",
                solid_joinstyle="round")
        continue
    pts = polyline_points(p, counts[k])
    for q in pts:
        q = q + rng.normal(0, 0.06, 2)
        kind = "lipid" if rng.random() < 0.7 else "drug"
        r = 0.2 if k == 3 else 0.14
        ax.add_patch(Circle(q, r, facecolor=P.fill(kind), edgecolor=P.edge(kind), lw=0.6, zorder=5))
bio.callout(ax, tuple(pB[0][3]), (cB[0] - 4.7, 0.9), "confluent growth", size="tiny")
bio.callout(ax, tuple(pB[3][5]), (cB[0] - 4.9, 9.6), "isolated colonies:\npick and restreak", size="tiny")
