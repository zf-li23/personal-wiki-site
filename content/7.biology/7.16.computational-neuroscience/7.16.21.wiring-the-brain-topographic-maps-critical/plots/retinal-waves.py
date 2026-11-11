"""Retinal waves in a one-dimensional excitable medium and their correlation structure.

A ring of 400 retinal cells per eye. Each cell is resting (0), active for T_a = 3 steps or refractory for T_ref = 150
steps. A resting cell becomes active spontaneously with probability q = 1e-5 per step, or with probability
p = 0.32 per step if at least one cell within radius r = 2 is active (waves spread through coupled neighbors).
Two independent eyes with the same parameters. Activity of cell i is a(i, t) in {0, 1}; correlation between cells at
distance d is the Pearson correlation of their activity binned in 3-step windows, averaged over pairs.
A: raster of one eye (cells vs time); waves appear as oblique bands. B: correlation against distance within an eye and
between the two eyes. C: distribution of the number of simultaneously active cells.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
N, T, Ta, Tref, q, p, r = 400, 8000, 3, 150, 1.0e-5, 0.32, 2


def simulate(seed):
    rng = np.random.default_rng(seed)
    c = np.zeros(N, int)  # 0 resting, 1..Ta active, Ta+1..Ta+Tref refractory
    act = np.zeros((T, N), bool)
    for t in range(T):
        active = (c >= 1) & (c <= Ta)
        near = np.zeros(N, bool)
        for s in range(-r, r + 1):
            near |= np.roll(active, s)
        fire = (c == 0) & ((rng.random(N) < q) | (near & (rng.random(N) < p)))
        c[c > 0] += 1
        c[c > Ta + Tref] = 0
        c[fire] = 1
        act[t] = (c >= 1) & (c <= Ta)
    return act


A1, A2 = simulate(1), simulate(2)


def binned(a, b=3):
    n = a.shape[0] // b
    return a[: n * b].reshape(n, b, N).any(1).astype(float)


b1, b2 = binned(A1), binned(A2)
z1 = (b1 - b1.mean(0)) / (b1.std(0) + 1e-9)
z2 = (b2 - b2.mean(0)) / (b2.std(0) + 1e-9)
C11 = z1.T @ z1 / len(z1)
C12 = z1.T @ z2 / len(z1)
dist = np.abs((np.arange(N)[:, None] - np.arange(N)[None, :] + N // 2) % N - N // 2)
ds = np.arange(0, 60)
within = np.array([C11[dist == d].mean() for d in ds])
between = np.array([C12[dist == d].mean() for d in ds])

fig, axs = plt.subplots(1, 3, figsize=(13, 3.9))
ax = axs[0]
ax.imshow(A1[:3000].T, aspect="auto", cmap="gray_r", interpolation="nearest", origin="lower")
ax.set_xlabel("Time (steps)")
ax.set_ylabel("Cell position")
ax.set_title("A  Waves in one retina", loc="left", fontsize=10)

bx = axs[1]
bx.plot(ds, within, color=P.edge("dna"), lw=2, label="same eye")
bx.plot(ds, between, color=P.edge("rna"), lw=2, label="the other eye")
bx.axhline(0, color=P.muted(), lw=0.7)
bx.set_xlabel("Distance between cells (cell spacings)")
bx.set_ylabel("Correlation of activity")
bx.legend(frameon=False, fontsize=8)
bx.set_title("B  Correlation falls with distance", loc="left", fontsize=10)

cx = axs[2]
sizes = A1.sum(1)
nwaves = (sizes[1:] > 0) & (sizes[:-1] == 0)
cx.hist(sizes[sizes > 0], bins=30, color=P.fill("dna"), edgecolor=P.edge("dna"))
cx.set_xlabel("Number of active cells at one time")
cx.set_ylabel("Time steps")
cx.set_title(f"C  Wave sizes ({nwaves.sum()} events)", loc="left", fontsize=10)
fig.tight_layout()
