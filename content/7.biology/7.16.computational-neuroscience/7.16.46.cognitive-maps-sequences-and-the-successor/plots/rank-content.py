"""Conjunctive coding of rank and content: a model of the geometry of sequence working memory.

A population of N = 120 neurons holds a sequence of three spatial locations, each chosen from
six locations on a circle (angles k * 60 deg). The code is the sum of three rank-specific parts:
the item at rank r (r = 1, 2, 3) is written as (cos theta_r, sin theta_r) into a random
two-dimensional plane of the population space, scaled by g_r = 1, 0.7, 0.5 (later items are
represented more weakly), plus independent Gaussian noise (s.d. 0.08 per neuron). All
6^3 = 216 sequences, 4 noisy repetitions each.
The rank-r plane is recovered from the data by linear regression of the population activity
on (cos theta_r, sin theta_r); each sequence is projected onto it.
A-C: projections onto the planes of ranks 1, 2 and 3, colored by the location of the item at
     that rank: each rank has its own ring of locations, smaller for later ranks.
D: the rank-1 plane colored by the item at rank 2: no structure, because the planes are nearly
   orthogonal (principal angles between the recovered planes are given in the title).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
N, gains, noise = 120, (1.0, 0.7, 0.5), 0.08
planes = [np.linalg.qr(rng.standard_normal((N, 2)))[0] for _ in range(3)]
locs = np.arange(6) * np.pi / 3
seqs = np.array([(i, j, k) for i in range(6) for j in range(6) for k in range(6)])
seqs = np.repeat(seqs, 4, axis=0)
X = np.zeros((len(seqs), N))
for r in range(3):
    th = locs[seqs[:, r]]
    X += gains[r] * np.c_[np.cos(th), np.sin(th)] @ planes[r].T
X += noise * rng.standard_normal(X.shape)
Xc = X - X.mean(axis=0)

est = []
for r in range(3):
    th = locs[seqs[:, r]]
    D = np.c_[np.cos(th), np.sin(th)]
    B, *_ = np.linalg.lstsq(D, Xc, rcond=None)  # 2 x N regression weights
    Q, _ = np.linalg.qr(B.T)
    est.append(Q)


def angle(A, B):
    s = np.linalg.svd(A.T @ B, compute_uv=False)
    return np.degrees(np.arccos(np.clip(s.max(), -1, 1)))


cols = [P.edge(t) for t in ("dna", "positive", "highlight", "negative", "rna", "neutral")]
fig, axs = plt.subplots(1, 4, figsize=(14, 3.7))
for r in range(3):
    Z = Xc @ est[r]
    for k in range(6):
        m = seqs[:, r] == k
        axs[r].scatter(Z[m, 0], Z[m, 1], s=6, color=cols[k], alpha=0.6, lw=0)
    axs[r].set_title(f"{'ABC'[r]}  Rank-{r + 1} plane, colored by item {r + 1}", loc="left", fontsize=10)
Z = Xc @ est[0]
for k in range(6):
    m = seqs[:, 1] == k
    axs[3].scatter(Z[m, 0], Z[m, 1], s=6, color=cols[k], alpha=0.6, lw=0)
ang = min(angle(est[0], est[1]), angle(est[0], est[2]), angle(est[1], est[2]))
axs[3].set_title(f"D  Rank-1 plane, colored by item 2", loc="left", fontsize=10)
axs[3].text(0.02, 0.02, f"smallest angle between planes: {ang:.0f} deg",
            transform=axs[3].transAxes, fontsize=8, color=P.muted())
lim = 1.6
for a in axs:
    a.set_xlim(-lim, lim)
    a.set_ylim(-lim, lim)
    a.set_aspect("equal")
    a.set_xticks([])
    a.set_yticks([])
    a.set_xlabel("Axis 1")
    a.set_ylabel("Axis 2")
for k in range(6):
    axs[0].plot([], [], "o", ms=5, color=cols[k], label=f"{60 * k} deg")
axs[0].legend(frameon=False, fontsize=7, loc="upper left", ncol=2, handletextpad=0.2, columnspacing=0.6)
fig.tight_layout()
