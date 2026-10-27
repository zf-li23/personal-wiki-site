"""Cell sorting by differential adhesion: the cellular Potts model of Graner and Glazier (1992).

Each cell sigma occupies a set of sites of a square lattice (L = 44; cell type tau = dark, light, or the
medium M). The energy is
    H = sum over neighbouring sites (i, j) of J(tau_i, tau_j) (1 - delta(sigma_i, sigma_j))
        + lambda * sum over cells (a_sigma - A)^2,
with contact energies J(d, d) = 2, J(l, l) = 14, J(d, l) = 11, J(d, M) = J(l, M) = 16 (a low J is strong
adhesion: dark cells adhere most strongly to each other), target area A = 16 sites and lambda = 4, the
energy summed over the eight nearest and next-nearest neighbours. A Monte Carlo step (MCS) is L^2 attempts
to copy the cell index of a random site into a random neighbour, accepted with the Metropolis probability
min(1, exp(-dH / T)) at T = 8; cells are not allowed to shrink below two sites. Interfacial tensions gamma(d, l) = J(d, l) - (J(d, d) + J(l, l)) / 2 = 3 > 0 and
gamma(l, M) < gamma(d, M) predict that the cells sort and that the light cells envelop the dark ones.
A: the aggregate at 0, 100 and 3000 MCS (random mixture, clusters, sorted with dark cells inside).
B: the fraction of cell-cell contact length that is heterotypic (dark-light) falls as the cells sort.
"""

import math

import numpy as np
from matplotlib.collections import LineCollection

import wikibio as bio
from wikibio import charts, quant

P = bio.P
rng = np.random.default_rng(3)
L, A_T, LAM, T = 44, 16, 4.0, 8.0
J = np.array([[0.0, 16.0, 16.0], [16.0, 2.0, 11.0], [16.0, 11.0, 14.0]])  # types: 0 medium, 1 dark, 2 light

# initial aggregate: 4x4 square cells inside a disk, types at random (half dark)
sigma = np.zeros((L, L), dtype=int)
ctype = [0]
cid = 0
c = (L - 1) / 2
for by in range(0, L, 4):
    for bx in range(0, L, 4):
        if math.hypot(bx + 1.5 - c, by + 1.5 - c) < 17.5:
            cid += 1
            sigma[by:by + 4, bx:bx + 4] = cid
            ctype.append(0)
ncell = cid
types = rng.permutation([1] * (ncell // 2) + [2] * (ncell - ncell // 2))
for k in range(1, ncell + 1):
    ctype[k] = int(types[k - 1])
ctype = np.array(ctype)
area = np.bincount(sigma.ravel(), minlength=ncell + 1).astype(float)

NB8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
sig = sigma.tolist()
ct = ctype.tolist()
ar = area.tolist()
Jl = J.tolist()


def hetero_fraction(s):
    s = np.asarray(s)
    t = ctype[s]
    tot = het = 0
    for a, b in ((s[:, :-1], s[:, 1:]), (s[:-1, :], s[1:, :])):
        ta, tb = ctype[a], ctype[b]
        m = (a != b) & (ta > 0) & (tb > 0)
        tot += m.sum()
        het += (m & (ta != tb)).sum()
    del t
    return het / max(tot, 1)


def mcs(n):
    """Run n Monte Carlo steps (pure Python inner loop over L^2 copy attempts)."""
    N = L * L
    for _ in range(n):
        ys = rng.integers(1, L - 1, N).tolist()
        xs = rng.integers(1, L - 1, N).tolist()
        nb = rng.integers(0, 8, N).tolist()
        us = rng.random(N).tolist()
        for y, x, k, u in zip(ys, xs, nb, us):
            dy, dx = NB8[k]
            s_new = sig[y + dy][x + dx]
            s_old = sig[y][x]
            if s_new == s_old or (s_old and ar[s_old] <= 2):
                continue
            t_new, t_old = ct[s_new], ct[s_old]
            dH = 0.0
            for oy, ox in NB8:
                yy, xx = y + oy, x + ox
                if 0 <= yy < L and 0 <= xx < L:
                    s2 = sig[yy][xx]
                    t2 = ct[s2]
                    if s2 != s_old:
                        dH -= Jl[t_old][t2]
                    if s2 != s_new:
                        dH += Jl[t_new][t2]
            if s_old:
                dH += LAM * ((ar[s_old] - 1 - A_T) ** 2 - (ar[s_old] - A_T) ** 2)
            if s_new:
                dH += LAM * ((ar[s_new] + 1 - A_T) ** 2 - (ar[s_new] - A_T) ** 2)
            if dH <= 0 or u < math.exp(-dH / T):
                sig[y][x] = s_new
                ar[s_old] -= 1
                ar[s_new] += 1


snaps, curve = {}, []
times = [0, 100, 3000]
t = 0
curve.append((0, hetero_fraction(sig)))
snaps[0] = np.array(sig)
for target in (10, 30, 100, 300, 600, 1000, 2000, 3000):
    mcs(target - t)
    t = target
    curve.append((t, hetero_fraction(sig)))
    if t in times:
        snaps[t] = np.array(sig)

fig, ax = bio.canvas(28.0, 9.6)
cols = {1: P.fill("channel"), 2: P.fill("antibody")}
edge = P.ink()


def draw(s, x0, y0, size):
    k = size / L
    img = np.zeros((L, L, 4))
    from matplotlib.colors import to_rgba
    for tp, col in cols.items():
        img[ctype[s] == tp] = to_rgba(col)
    ax.imshow(img, extent=(x0, x0 + size, y0, y0 + size), origin="lower", interpolation="nearest", zorder=2)
    segs = []
    for yy in range(L):
        for xx in range(L):
            if xx + 1 < L and s[yy, xx] != s[yy, xx + 1] and (s[yy, xx] or s[yy, xx + 1]):
                segs.append([(x0 + (xx + 1) * k, y0 + yy * k), (x0 + (xx + 1) * k, y0 + (yy + 1) * k)])
            if yy + 1 < L and s[yy, xx] != s[yy + 1, xx] and (s[yy, xx] or s[yy + 1, xx]):
                segs.append([(x0 + xx * k, y0 + (yy + 1) * k), (x0 + (xx + 1) * k, y0 + (yy + 1) * k)])
    ax.add_collection(LineCollection(segs, colors=P.on_fill(), linewidths=0.5, alpha=0.55, zorder=3))


bio.panel(ax, "A", (0.1, 9.5))
for k, tt in enumerate(times):
    x0 = 0.5 + k * 6.3
    draw(snaps[tt], x0, 1.4, 6.0)
    bio.label(ax, (x0 + 3.0, 0.8), f"{tt} MCS", size="small")
for k, (tp, name) in enumerate(((1, "Dark cells (strong mutual adhesion)"), (2, "Light cells"))):
    y = 9.0 - 0.55 * k
    bio.box(ax, (7.2, y), 0.4, 0.4, "channel" if tp == 1 else "antibody")
    bio.label(ax, (7.6, y), name, size="tiny", ha="left")

bio.panel(ax, "B", (19.6, 9.5))
pb = charts.axes_at(ax, (21.2, 1.6, 6.3, 6.6))
tt, hf = np.array(curve).T
pb.plot(tt, hf, color=quant.line_color("drug"), lw=2.0, marker="o", ms=3.5)
pb.set_xscale("symlog", linthresh=10)
pb.set_xlim(0, 3500)
pb.set_ylim(0, 0.6)
pb.axhline(0.5, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.text(12, 0.52, "random mixture", fontsize=bio.core.FONT["tiny"], color=P.muted())
charts.style_axes(pb, "time / MCS", "heterotypic fraction of contacts")
charts.title(pb, "Sorting reduces dark–light contacts")
