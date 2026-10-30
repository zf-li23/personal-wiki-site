"""The polar coordinate model: shortest intercalation and supernumerary limbs (Algorithm 35.4.1, Theorem 35.4.1).

Circumferential positional values are hours on a clock face (0 = 12 dorsal, 3 anterior, 6 ventral, 9 posterior).
A: a right blastema is grafted onto a left stump (contralateral graft): the dorso-ventral axis is kept and the
antero-posterior axis is reversed, so the graft value opposite a host value h is g = -h (mod 12).
B: at 12 points around the junction the regenerate intercalates the shorter series of values from the host value
(inner ring) to the graft value (outer ring); numbers along each spoke are the intercalated values. Where host and
graft values are opposite (anterior and posterior) the two routes are equally short; around these two points a
small loop meets every value once, a complete circle, and distal transformation makes a supernumerary limb (stars).
The winding number of the values around each point is computed numerically: +1 at both, total 2 = deg(stump)
- deg(graft) = 1 - (-1). C: proximo-distal intercalation in the cockroach tibia (values 1-5): a distal piece on a
proximal stump gives a normal tibia; a proximal piece on a distal stump gives a longer tibia whose intercalated part
(values 3, 2) has reversed polarity.
"""

import math

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch
import wikibio as bio

P = bio.P
LW = bio.core.LINE
fig, ax = bio.canvas(34.0, 14.0)


def wrap(d):
    """Signed difference in (-6, 6]."""
    return (d + 6.0) % 12.0 - 6.0 if (d + 6.0) % 12.0 != 0 else 6.0


def value(theta, s, graft):
    h = theta % 12.0
    d = wrap(graft(theta) - h)
    return h + s * d


def index(theta0, graft, r=0.25, n=720):
    """Winding number of the positional values around (theta0, s = 0.5) in the (theta, s) junction strip."""
    tot, prev = 0.0, None
    for k in range(n + 1):
        phi = 2 * math.pi * k / n
        th, s = theta0 + r * 2.0 * math.cos(phi), 0.5 + r * math.sin(phi)
        v = value(th, s, graft) * 2 * math.pi / 12.0
        if prev is not None:
            dv = (v - prev + math.pi) % (2 * math.pi) - math.pi
            tot += dv
        prev = v
    return round(tot / (2 * math.pi))


def clock(c, r, labels, title, tok, numbers=True):
    ax.add_patch(Circle(c, r, fc=P.light(tok), ec=P.edge(tok), lw=LW, zorder=4))
    for k in range(12):
        a = math.radians(90 - 30 * k)
        p = (c[0] + 0.8 * r * math.cos(a), c[1] + 0.8 * r * math.sin(a))
        if numbers:
            bio.label(ax, p, str(labels(k)), size="tiny", zorder=8)
    bio.label(ax, (c[0], c[1] - r - 0.5), title, size="tiny")


# A: the graft
bio.panel(ax, "A", (0.2, 13.8))
bio.label(ax, (1.4, 13.5), "Contralateral graft", size="small", bold=True, ha="left")
clock((3.0, 9.0), 2.0, lambda k: 12 if k == 0 else k, "left stump (host)", "animal")
clock((8.4, 9.0), 2.0, lambda k: 12 if (-k) % 12 == 0 else (-k) % 12, "right blastema on it", "drug")
for c in ((3.0, 9.0), (8.4, 9.0)):
    bio.label(ax, (c[0], c[1] + 2.4), "D", size="tiny", bold=True)
    bio.label(ax, (c[0], c[1] - 2.0 + 0.0), "", size="tiny")
bio.label(ax, (5.1, 9.0), "A", size="tiny", bold=True)
bio.label(ax, (0.7, 9.0), "P", size="tiny", bold=True)
bio.label(ax, (5.7, 6.0), "graft value g = -h: D and V match, A and P swap", size="tiny", color=P.muted())

# B: shortest intercalation at the junction
bio.panel(ax, "B", (12.0, 13.8))
bio.label(ax, (13.2, 13.5), "Shortest intercalation at the junction", size="small", bold=True, ha="left")
cB = (18.6, 7.6)
r0, r1 = 1.6, 5.2
ax.add_patch(Circle(cB, r1, fc="none", ec=P.edge("drug"), lw=LW, zorder=4))
ax.add_patch(Circle(cB, r0, fc=P.light("animal"), ec=P.edge("animal"), lw=LW, zorder=4))
graft = lambda th: -th
sing = []
for k in range(12):
    a = math.radians(90 - 30 * k)
    u = (math.cos(a), math.sin(a))
    h = k
    g = (-k) % 12
    d = wrap(g - h)
    if abs(d) == 6:
        sing.append(k)
    steps = int(abs(d))
    seq = [(h + (1 if d > 0 else -1) * j) % 12 for j in range(steps + 1)] if steps else [h]
    for j, val in enumerate(seq):
        rr = r0 + (r1 - r0) * (j / max(steps, 1)) if steps else (r0 + r1) / 2
        p = (cB[0] + rr * u[0], cB[1] + rr * u[1])
        bio.label(ax, p, str(12 if val == 0 else val), size="tiny",
                  color=P.edge("negative") if abs(d) == 6 else P.ink(), zorder=9)
    ax.plot([cB[0] + (r0 + 0.2) * u[0], cB[0] + (r1 - 0.2) * u[0]], [cB[1] + (r0 + 0.2) * u[1], cB[1] + (r1 - 0.2) * u[1]],
            color=P.muted(), lw=0.5, zorder=5)
for k in sing:
    a = math.radians(90 - 30 * k)
    p = (cB[0] + (r1 + 0.7) * math.cos(a), cB[1] + (r1 + 0.7) * math.sin(a))
    ax.plot(*p, marker="*", ms=11, color=P.edge("highlight"), zorder=10)
bio.label(ax, (cB[0], cB[1]), "host", size="tiny", color=P.muted())
bio.label(ax, (cB[0], 1.0), "red spokes: both routes equally short (6 steps)", size="tiny", color=P.muted())

# winding numbers (theta measured in hours)
idx = [index(float(k), graft) for k in range(12)]
sup = {k: i for k, i in zip(range(12), idx) if i != 0}
txt = "winding number of values around each point:\n" + ", ".join(
    f"{('anterior' if k == 3 else 'posterior' if k == 9 else k)}: {v:+d}" for k, v in sup.items())
txt += f"\ntotal {sum(sup.values()):+d} = deg(host) - deg(graft) = 1 - (-1)"
bio.label(ax, (25.0, 12.6), txt, size="tiny", ha="left")
bio.label(ax, (25.0, 10.9), "stars: complete circles, two supernumerary limbs\n(anterior and posterior, host handedness)",
          size="tiny", ha="left", color=P.edge("highlight"))

# C: cockroach tibia
bio.panel(ax, "C", (25.0, 9.6))
bio.label(ax, (26.2, 9.3), "Cockroach tibia: P-D intercalation", size="small", bold=True, ha="left")


def segs(y, vals, kinds):
    x = 25.4
    for v, k in zip(vals, kinds):
        tok = {"h": "animal", "g": "drug", "i": "highlight"}[k]
        ax.add_patch(FancyBboxPatch((x, y - 0.32), 0.6, 0.64, boxstyle="round,pad=0,rounding_size=0.12",
                                    fc=P.fill(tok), ec=P.edge(tok), lw=LW * 0.7, zorder=6))
        bio.label(ax, (x + 0.3, y), str(v), size="tiny", zorder=8)
        x += 0.66
    return x


bio.label(ax, (25.4, 8.3), "host 1 | graft 5", size="tiny", ha="left")
segs(7.5, [1, 2, 3, 4, 5], "hiiig")
bio.label(ax, (25.4, 6.4), "host 1 2 3 4 | graft 1 2 3 4 5", size="tiny", ha="left")
segs(5.6, [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5], "hhhhiiggggg")
bio.label(ax, (25.4, 4.6), "yellow: intercalated; in the second case\nreversed (bristles point the wrong way)",
          size="tiny", ha="left", color=P.muted())
