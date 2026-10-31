# A toy version of ab initio bead modelling (in the spirit of DAMMIN), reduced to a flat particle.
# Search volume: the beads of a square grid (spacing 1 unit = 5 A) inside a disc of diameter Dmax = 15 units.
# Each bead is either particle (1) or solvent (0). The particle is flat (all beads in one plane), but it
# tumbles in three dimensions, so its scattering is given by the Debye formula
#   I(q) = sum_j sum_k x_j x_k sin(q r_jk) / (q r_jk).
# Target: a two-lobed, L-shaped particle of 59 beads; its curve on 40 points, 0.05 <= q <= 1.8 unit^-1
# (0.01 to 0.36 A^-1), with 2 % noise, serves as the "data".
# Energy: E = chi^2 (with the best scale factor) + 3 * looseness + 2 * (number of disconnected pieces - 1),
# looseness = 1 - (mean number of occupied neighbours of occupied beads) / 4.
# Simulated annealing: single-bead flips accepted with the Metropolis probability min(1, exp(-dE / T)),
# T lowered by a factor 0.88 every 700 steps from T0 = 2; the scattering is updated incrementally
# (O(N) per flip) through g_m(q) = sum_k x_k S_mk(q).
# Top: the target and the final models of three independent runs (different random seeds); each fits the
# data equally well (chi^2 below 1) but differs in detail and in orientation (rotations and mirror images
# have the same curve): the data fix the overall shape, not the individual beads.
# Bottom left: data and fits; bottom right: energy during annealing.
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

import wikibio as bio
from wikibio import charts

P = bio.P
R = 7.5
g = np.arange(-7, 8)
X, Y = np.meshgrid(g, g, indexing="ij")
inside = X**2 + Y**2 <= R**2
idx = np.argwhere(inside)
xy = np.column_stack([X[inside], Y[inside]]).astype(float)
N = len(xy)
D = np.sqrt(((xy[:, None, :] - xy[None, :, :]) ** 2).sum(-1))
q = np.linspace(0.05, 1.8, 40)
S = np.sinc(q[:, None, None] * D[None] / np.pi)      # S[q, j, k]

target = ((X + 2.5) ** 2 + (Y + 1.5) ** 2 <= 3.2**2) | ((X - 3) ** 2 + (Y - 3) ** 2 <= 2.0**2) \
    | ((np.abs(X - 1) <= 3) & (np.abs(Y + 1) <= 1) & (X >= -1)) | ((np.abs(X - 3) <= 1) & (Y >= -1) & (Y <= 3))
target &= inside
xt = target[inside].astype(float)
It = np.einsum("j,qjk,k->q", xt, S, xt)
rng_d = np.random.default_rng(7)
sig = 0.02 * It
Id = It + sig * rng_d.normal(size=q.size)
w = 1 / sig**2


def chi2(I):
    k = (w * I * Id).sum() / (w * I * I).sum()
    return (w * (k * I - Id) ** 2).mean()


def penalties(grid):
    occ = grid.astype(int)
    nn = sum(np.roll(occ, s, axis=a) for a in (0, 1) for s in (1, -1))
    n = occ.sum()
    loose = 1 - (nn * occ).sum() / (4 * max(n, 1))
    pieces = ndimage.label(occ)[1]
    return 3 * loose + 2 * max(pieces - 1, 0)


def anneal(seed, steps_per_t=700, n_t=40):
    rng = np.random.default_rng(seed)
    x = np.ones(N)
    grid = np.zeros_like(inside, dtype=bool)
    grid[inside] = True
    gq = np.einsum("qjk,k->qj", S, x)
    I = (gq * x).sum(axis=1)
    E = chi2(I) + penalties(grid)
    T = 2.0
    trace = []
    for _ in range(n_t):
        for _ in range(steps_per_t):
            m = rng.integers(N)
            i, j = idx[m]
            if x[m] == 1:
                In = I - 2 * gq[:, m] + 1
            else:
                In = I + 2 * gq[:, m] + 1
            if In[0] < 4:
                continue
            grid[i, j] = not grid[i, j]
            En = chi2(In) + penalties(grid)
            if En <= E or rng.random() < np.exp(-(En - E) / T):
                sgn = -1 if x[m] == 1 else 1
                x[m] += sgn
                gq += sgn * S[:, :, m]
                I, E = In, En
            else:
                grid[i, j] = not grid[i, j]
            trace.append(E)
        T *= 0.88
    return x, I, np.array(trace)


runs = [anneal(s) for s in (11, 12, 13)]

fig = plt.figure(figsize=(12.5, 6.2))
gs = fig.add_gridspec(2, 4, height_ratios=[1.0, 1.0], hspace=0.25, wspace=0.25)
cells = [("target (data)", xt, "highlight")] + [(f"run {k + 1}", r[0], "protein") for k, r in enumerate(runs)]
for c, (lab, xv, tok) in enumerate(cells):
    ax = fig.add_subplot(gs[0, c])
    t = np.linspace(0, 2 * np.pi, 200)
    ax.plot(R * np.cos(t), R * np.sin(t), color=P.muted(), lw=0.7, ls=(0, (3, 2)))
    ax.scatter(xy[xv == 0, 0], xy[xv == 0, 1], s=6, color=P.light("neutral"), edgecolors="none")
    ax.scatter(xy[xv == 1, 0], xy[xv == 1, 1], s=46, color=P.fill(tok), edgecolors=P.edge(tok), linewidths=0.6)
    ax.set_aspect("equal")
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    ax.axis("off")
    n_on = int(xv.sum())
    ax.set_title(f"{lab}: {n_on} beads", fontsize=8.5, color=P.ink())
ax = fig.add_subplot(gs[1, :2])
ax.errorbar(q / 5, Id / Id[0], yerr=sig / Id[0], fmt="o", ms=2.5, color=P.muted(), elinewidth=0.6, label="data")
for k, (xv, I, tr) in enumerate(runs):
    kk = (w * I * Id).sum() / (w * I * I).sum()
    ax.plot(q / 5, kk * I / Id[0], color=charts.line(("dna", "negative", "positive")[k]), lw=1.3,
            label=f"run {k + 1}: χ²/N = {chi2(I):.2f}")
ax.set_yscale("log")
ax.legend(fontsize=7.5, frameon=False, loc="lower left")
charts.style_axes(ax, "q / Å⁻¹", "I(q) / I(0)")
charts.title(ax, "Fits to the scattering curve")
ax = fig.add_subplot(gs[1, 2:])
for k, (xv, I, tr) in enumerate(runs):
    ax.semilogy(np.arange(len(tr)) / 1000, tr, color=charts.line(("dna", "negative", "positive")[k]), lw=1.0,
                label=f"run {k + 1}")
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "accepted and rejected steps  /  1000", "energy E")
charts.title(ax, "Simulated annealing")
