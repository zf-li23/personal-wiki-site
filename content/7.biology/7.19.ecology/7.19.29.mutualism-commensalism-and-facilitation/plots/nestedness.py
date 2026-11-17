"""Nestedness of a plant-pollinator interaction matrix, measured by NODF (Almeida-Neto et al. 2008).

A simulated network of 12 plants and 20 pollinators: the probability of a link decreases with the sum
of the ranks of the two species (a generalist core and specialists that visit generalists), with 27.5 %
connectance. A: the matrix with rows and columns sorted by degree; filled cells are links; it is
strongly nested (NODF = 74). B: a random matrix with the same size and number of links
(equiprobable null model), sorted in the same way (NODF = 29). C: distribution of NODF in 1000 such random
matrices (bars) and the value of the nested network (line): nestedness is far beyond chance (null mean 29, maximum 43).
All data are simulated.
"""

import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(3)
nr, nc = 12, 20


def nodf(M):
    M = M[np.argsort(-M.sum(1), kind="stable")][:, np.argsort(-M.sum(0), kind="stable")]

    def part(A):
        d = A.sum(1)
        vals = []
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if d[i] > d[j] and d[j] > 0:
                    vals.append((A[i] * A[j]).sum() / d[j])
                else:
                    vals.append(0.0)
        return vals
    v = part(M) + part(M.T)
    return 100 * np.mean(v)


ri = np.arange(nr)[:, None] / nr
cj = np.arange(nc)[None, :] / nc
prob = 1 / (1 + np.exp(12 * (ri + cj - 0.62)))
M = (rng.random((nr, nc)) < prob).astype(int)
M[0, :] = np.maximum(M[0, :], (rng.random(nc) < 0.9))
M[:, 0] = 1
L = M.sum()
Mr = np.zeros(nr * nc, int)
Mr[rng.choice(nr * nc, L, replace=False)] = 1
Mr = Mr.reshape(nr, nc)
null = []
for _ in range(1000):
    R = np.zeros(nr * nc, int)
    R[rng.choice(nr * nc, L, replace=False)] = 1
    null.append(nodf(R.reshape(nr, nc)))
null = np.array(null)
n_obs, n_rand = nodf(M), nodf(Mr)

fig, ax = bio.canvas(33.0, 11.0)


def draw(A, x0, title, letter, val):
    A = A[np.argsort(-A.sum(1), kind="stable")][:, np.argsort(-A.sum(0), kind="stable")]
    cw = 0.42
    for i in range(nr):
        for j in range(nc):
            fc = P.fill("plant") if A[i, j] else P.surface()
            ax.add_patch(Rectangle((x0 + j * cw, 8.6 - (i + 1) * cw), cw, cw, fc=fc,
                                            ec=P.mix(P.muted(), P.surface(), 0.4), lw=0.4))
    bio.panel(ax, letter, (x0 - 1.3, 10.8))
    bio.label(ax, (x0, 10.0), f"{title}: NODF = {val:.0f}", size="small", bold=True, ha="left")
    bio.label(ax, (x0 + nc * cw / 2, 8.6 - nr * cw - 0.5), "pollinators (by degree)", size="small")
    bio.label(ax, (x0 - 0.35, 8.6 - nr * cw / 2), "plants (by degree)", size="small", rotation=90)


draw(M, 1.6, "Simulated pollination network", "A", n_obs)
draw(Mr, 12.4, "Random, same connectance", "B", n_rand)
pc = C.axes_at(ax, (24.2, 2.2, 8.2, 6.6))
pc.hist(null, bins=30, color=P.mix(P.fill("neutral"), P.surface(), 0.2), edgecolor=P.edge("neutral"), lw=0.5)
pc.axvline(n_obs, color=Q.line_color("negative"), lw=1.8)
pc.text(n_obs - 1, pc.get_ylim()[1] * 0.85, "simulated\nnetwork", fontsize=FS["tiny"], color=P.ink(), ha="right")
pc.set_xlim(0, 100)
C.style_axes(pc, "NODF", "random matrices")
bio.panel(ax, "C", (22.7, 10.8))
bio.label(ax, (24.2, 10.0), "Null distribution of NODF", size="small", bold=True, ha="left")
