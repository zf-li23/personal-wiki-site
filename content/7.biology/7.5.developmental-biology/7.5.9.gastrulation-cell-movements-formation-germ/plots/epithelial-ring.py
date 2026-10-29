"""Invagination of an epithelial ring by apical constriction (a two-dimensional section of a blastula wall,
after the ring model of Percus and Childress, written as a vertex model). Each of 40 cells is a quadrilateral
with an apical (outer) edge, a basal (inner) edge and two lateral edges; apical and basal edges are contractile springs
with a preferred length, lateral edges carry a tension, each cell has an area elasticity and the enclosed
blastocoel a volume (area) elasticity. With
isotropic friction, the dissipation principle δ(dT/dt + Φ/2) = 0 gives overdamped motion of each vertex down
the energy gradient. Shortening the preferred apical length of five cells at the vegetal pole to a quarter (apical
constriction) while their basal surfaces relax (preferred length 1.3 times) turns them into wedges, and the sheet bends inwards: the outer surface dimples and a pit about one cell
height deep forms (deeper invagination needs further forces, as in real embryos). Left: snapshots (the five constricting cells
coloured); right: the depth of the pit and the apical width of the constricting cells over time."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
N = 40
nx = np.roll(np.arange(N), -1)


def cr(a, b):
    return a[..., 0] * b[..., 1] - a[..., 1] * b[..., 0]


def setup():
    th = np.linspace(0, 2 * np.pi, N, endpoint=False) - np.pi / 2 - np.pi / N
    return np.c_[np.cos(th), np.sin(th)], 0.75 * np.c_[np.cos(th), np.sin(th)]


def areas(ap, ba):
    bi, bj, aj, ai = ba, ba[nx], ap[nx], ap
    return 0.5 * (cr(bi, bj) + cr(bj, aj) + cr(aj, ai) + cr(ai, bi))


def grad(ap, ba, ta, tb, tl, K, A0, KL, AL0):
    ga, gb = np.zeros_like(ap), np.zeros_like(ba)
    for Pt, G, (ks, l0) in ((ap, ga, ta), (ba, gb, tb)):
        d = Pt[nx] - Pt
        ln = np.hypot(*d.T)
        u = d / ln[:, None]
        tau = ks * (ln - l0)  # apical and basal edges are contractile springs with a preferred length
        G -= tau[:, None] * u
        np.add.at(G, nx, tau[:, None] * u)
    d = ap - ba
    u = d / np.hypot(*d.T)[:, None]
    ga += tl[:, None] * u
    gb -= tl[:, None] * u
    bi, bj, aj, ai = ba, ba[nx], ap[nx], ap
    f = (K * (areas(ap, ba) - A0))[:, None]
    gb += f * 0.5 * np.c_[bj[:, 1] - ai[:, 1], ai[:, 0] - bj[:, 0]]
    np.add.at(gb, nx, f * 0.5 * np.c_[aj[:, 1] - bi[:, 1], bi[:, 0] - aj[:, 0]])
    np.add.at(ga, nx, f * 0.5 * np.c_[ai[:, 1] - bj[:, 1], bj[:, 0] - ai[:, 0]])
    ga += f * 0.5 * np.c_[bi[:, 1] - aj[:, 1], aj[:, 0] - bi[:, 0]]
    AL = 0.5 * np.sum(cr(ba, ba[nx]))
    gb += KL * (AL - AL0) * 0.5 * np.c_[ba[nx][:, 1] - np.roll(ba, 1, 0)[:, 1], np.roll(ba, 1, 0)[:, 0] - ba[nx][:, 0]]
    return ga, gb


strong = [38, 39, 0, 1, 2]
ap, ba = setup()
A0 = areas(ap, ba)[0]
AL0 = 0.5 * np.sum(cr(ba, ba[nx]))
la, lb = np.hypot(*(ap[1] - ap[0])), np.hypot(*(ba[1] - ba[0]))
l_ap = np.full(N, la)
l_ap[strong] = 0.25 * la
l_ba = np.full(N, lb)
l_ba[strong] = 1.3 * lb
ta, tb, tl = (40.0, l_ap), (40.0, l_ba), np.full(N, 0.3)
dt, T = 1e-4, 6.0
steps = int(T / dt)
snaps, ts, depth, width = [], [], [], []
y_rest = None
for k in range(steps + 1):
    if k % (steps // 3) == 0:
        snaps.append((ap.copy(), ba.copy()))
    if k % 200 == 0:
        ts.append(k * dt)
        rest = np.mean(np.hypot(*ap[10:30].T))  # radius of the unconstricted part
        depth.append(rest - np.hypot(*ap[0]))
        width.append(np.mean(np.hypot(*(ap[nx][strong] - ap[strong]).T)))
    ga, gb = grad(ap, ba, ta, tb, tl, 1000.0, A0, 0.3, AL0)
    ap -= dt * ga
    ba -= dt * gb

fig, ax = bio.canvas(22, 8.6)
for s, (A, B) in enumerate(snaps[:4]):
    cx, cy, sc = 2.4 + 4.3 * s, 4.6, 1.85
    for i in range(N):
        j = nx[i]
        q = np.array([B[i], B[j], A[j], A[i]]) * sc + (cx, cy)
        bio.shape(ax, q, "mesoderm" if i in strong else "ectoderm", lw=0.6, zorder=5)
    bl = B * sc + (cx, cy)
    bio.shape(ax, bl, "vacuole", lw=0, zorder=4)
    bio.label(ax, (cx, 1.9), f"t = {s * T / 3:.0f}", size="small")
bio.label(ax, (0.4, 8.2), "A  Vertex model of a blastula wall", size="small", bold=True, ha="left")
c = charts.axes_at(ax, (17.6, 1.6, 3.8, 5.6))
c.plot(ts, np.array(depth) / 0.25, color=charts.line("mesoderm"), lw=1.7, label="pit depth / cell height")
c.plot(ts, np.array(width) / width[0], color=charts.line("dna"), lw=1.7, label="apical width / initial")
charts.style_axes(c, "time", None)
charts.title(c, "B  Kinetics")
lg = c.legend(fontsize=6.5, frameon=False, loc="center right")
[t.set_color(P.ink()) for t in lg.get_texts()]
