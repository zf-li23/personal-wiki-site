"""Fisher information of a Gaussian-tuned population as a function of tuning width and
stimulus dimension D.

Neurons with Gaussian tuning f(s) = A exp(-|s - c|^2 / (2 sigma^2)) have preferred values c on a
cubic lattice of spacing 0.25 (density eta = 0.25^-D), independent Poisson counts, A = 10.
I_F along one coordinate = sum_i (df_i/ds_1)^2 / f_i, evaluated at s = 0 (points) and compared with
the continuum result eta A (2 pi)^(D/2) sigma^(D-2) (lines).
A: tuning curves of width 0.5 and 1.5 (D = 1). B: Fisher information against sigma for D = 1, 2, 3.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
A, h = 10.0, 0.25


def lattice_info(sigma, D):
    L = 5 * sigma
    ax1 = np.arange(-L, L + 1e-9, h)
    ax1 = ax1 - ax1[np.argmin(np.abs(ax1))]
    grids = np.meshgrid(*([ax1] * D), indexing="ij")
    u2 = sum(g ** 2 for g in grids)
    f = A * np.exp(-u2 / (2 * sigma ** 2))
    df1 = f * (grids[0] / sigma ** 2)
    return np.sum(df1 ** 2 / np.maximum(f, 1e-300))


fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.1), gridspec_kw={"width_ratios": [1, 1.1]})
ax = axs[0]
s = np.linspace(-4, 4, 400)
for sg, c in ((0.5, P.edge("rna")), (1.5, P.edge("dna"))):
    ax.plot(s, A * np.exp(-s ** 2 / (2 * sg ** 2)), color=c, lw=2, label=f"sigma = {sg}")
ax.set_xlabel("Stimulus s - preferred value")
ax.set_ylabel("Mean spike count")
ax.legend(frameon=False, fontsize=8)
ax.set_title("A  Narrow and broad tuning", loc="left", fontsize=10)

ax = axs[1]
sig = np.array([0.5, 0.7, 1.0, 1.4, 2.0, 2.8])
for D, c in ((1, P.edge("rna")), (2, P.edge("protein")), (3, P.edge("dna"))):
    pts = [lattice_info(x, D) for x in sig]
    xx = np.linspace(0.5, 2.8, 100)
    ax.plot(xx, h ** -D * A * (2 * np.pi) ** (D / 2) * xx ** (D - 2), color=c, lw=1.8, label=f"D = {D}")
    ax.plot(sig, pts, "o", color=c, ms=4)
ax.set_yscale("log")
ax.set_xlabel("Tuning width sigma")
ax.set_ylabel("Fisher information I_F")
ax.legend(frameon=False, fontsize=8)
ax.set_title("B  Narrow tuning wins only in one dimension", loc="left", fontsize=10)
fig.tight_layout()
