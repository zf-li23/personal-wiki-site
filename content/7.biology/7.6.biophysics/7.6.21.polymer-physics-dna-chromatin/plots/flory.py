"""Excluded volume and the Flory exponent.

A: mean squared end-to-end distance of random walks (ideal chains) and of self-avoiding walks on the
simple cubic lattice against the number of steps N (lattice spacing a = 1). Self-avoiding walks are
sampled with the pivot algorithm (random lattice symmetry applied to the part of the chain beyond a
random pivot site, accepted if the chain stays self-avoiding); ideal walks are sampled directly.
The lines show <R^2> = N a^2 (exponent 2 nu = 1) and a fit with 2 nu = 2 x 0.588 = 1.176.
B: the Flory free energy F(R)/kBT = 3R^2/(2Na^2) + v N^2/(2 R^3) (with excluded volume v = a^3) for
N = 100, 300 and 1000; the minimum R* (dots) grows as N^(3/5)."""

import itertools
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(5)

# the 48 symmetries of the cube (signed permutation matrices), without the identity
SYM = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for i, (p, sg) in enumerate(zip(perm, signs)):
            M[i, p] = sg
        if not np.array_equal(M, np.eye(3, dtype=int)):
            SYM.append(M)


def key(x):
    return (x[:, 0] + 512) * 1048576 + (x[:, 1] + 512) * 1024 + (x[:, 2] + 512)


def saw_r2(N, n_attempts):
    x = np.zeros((N + 1, 3), dtype=int)
    x[:, 0] = np.arange(N + 1)
    r2 = []
    for k in range(n_attempts):
        p = rng.integers(1, N)
        M = SYM[rng.integers(len(SYM))]
        new = (x[p + 1:] - x[p]) @ M.T + x[p]
        trial = np.vstack([x[:p + 1], new])
        if np.unique(key(trial)).size == N + 1:
            x = trial
        if k > n_attempts // 4:
            r2.append(((x[-1] - x[0]) ** 2).sum())
    return np.mean(r2)


Ns = np.array([8, 16, 32, 64, 128, 256])
saw = np.array([saw_r2(N, 4000) for N in Ns])
steps = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])
rw = np.array([((steps[rng.integers(6, size=(3000, N))].sum(axis=1)) ** 2).sum(axis=1).mean() for N in Ns])

fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.5))
fig.subplots_adjust(wspace=0.32, left=0.08, right=0.97, bottom=0.16, top=0.88)
ax = axs[0]
ax.plot(Ns, rw, "o", color=charts.line("dna"), ms=4, label="random walk")
ax.plot(Ns, saw, "s", color=charts.line("protein"), ms=4, label="self-avoiding walk")
nn = np.logspace(0.8, 2.5, 50)
ax.plot(nn, nn, color=charts.line("dna"), lw=1.0, label=r"$N^{1}$")
c = np.exp(np.mean(np.log(saw[2:]) - 1.176 * np.log(Ns[2:])))
ax.plot(nn, c * nn ** 1.176, color=charts.line("protein"), lw=1.0, label=r"$N^{2\nu}$, $\nu = 0.588$")
ax.set_xscale("log")
ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "number of steps N", r"$\langle R^2\rangle / a^2$")
charts.title(ax, "A  Swelling by excluded volume")

ax = axs[1]
for N, tok in ((100, "rna"), (300, "dna"), (1000, "protein")):
    R = np.linspace(2, 80, 600)
    F = 1.5 * R ** 2 / N + 0.5 * N ** 2 / R ** 3
    F -= F.min()
    ax.plot(R, F, color=charts.line(tok), lw=1.3, label=f"N = {N}")
    i = np.argmin(F)
    ax.plot(R[i], 0, "o", color=charts.line(tok), ms=4)
ax.set_ylim(-0.5, 30)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "end-to-end distance R / a", r"$[F(R) - F_{\min}]/k_{\mathrm{B}}T$")
charts.title(ax, "B  Flory free energy")
