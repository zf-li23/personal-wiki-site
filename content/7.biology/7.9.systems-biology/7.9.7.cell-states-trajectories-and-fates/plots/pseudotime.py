"""Pseudotime and fate probabilities on a simulated branching differentiation. 900 cells progress from a
progenitor state (true time 0) through a branch point (time 0.35) into one of two fates; 80 genes follow
smooth programs of the true time (falling progenitor genes, rising common genes, and genes specific to
each branch), counts are Poisson. Counts were normalized (shifted log), reduced to 10 principal
components, and joined in a 15-nearest-neighbor graph with Gaussian kernels of adaptive width. A: cells in
the first two principal components colored by diffusion pseudotime from a root cell, with the minimum
spanning tree of 12 k-means centroids (the trajectory skeleton of Monocle-type methods). B: diffusion
pseudotime against the true time, by branch. C: the probability of reaching the terminal cells of fate A,
computed as absorption probabilities of a random walk on the graph that may not step backward in
pseudotime by more than a small tolerance (the forward bias that CellRank derives from RNA velocity)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.cluster.vq import kmeans2
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)

# --- simulate a branching trajectory
N, G, tb = 900, 80, 0.35
t = rng.uniform(0, 1, N)
branch = np.where(t < tb, 0, rng.integers(1, 3, N))            # 0 progenitor, 1 fate A, 2 fate B
s = np.clip((t - tb) / (1 - tb), 0, 1)                          # progress after the branch point


def sig(z, c, w=0.08):
    return 1 / (1 + np.exp(-(z - c) / w))


L = np.zeros((N, G))
for g in range(G):
    c = rng.uniform(0.1, 0.9)
    amp = rng.uniform(1.5, 3.0)
    if g < 20:                                    # progenitor genes, falling
        L[:, g] = amp * (1 - sig(t, c * 0.6))
    elif g < 35:                                  # common late genes
        L[:, g] = amp * sig(t, c)
    elif g < 55:                                  # fate A genes
        L[:, g] = amp * sig(s, c * 0.7) * (branch == 1)
    elif g < 75:                                  # fate B genes
        L[:, g] = amp * sig(s, c * 0.7) * (branch == 2)
    else:                                         # housekeeping
        L[:, g] = amp
X = rng.poisson(np.exp(L - 0.5) * rng.lognormal(0, 0.25, (N, 1)))
tot = X.sum(1, keepdims=True)
Y = np.log1p(X / tot * np.median(tot))
Y -= Y.mean(0)
U, sv, Vt = np.linalg.svd(Y, full_matrices=False)
Z = U[:, :10] * sv[:10]

# --- kNN graph with adaptive Gaussian kernel (Haghverdi et al. 2016)
k = 15
D = np.sqrt(((Z[:, None, :] - Z[None, :, :]) ** 2).sum(-1))
nn = np.argsort(D, 1)[:, 1:k + 1]
sigma = D[np.arange(N), nn[:, -1]]
W = np.zeros((N, N))
for i in range(N):
    j = nn[i]
    W[i, j] = np.sqrt(2 * sigma[i] * sigma[j] / (sigma[i] ** 2 + sigma[j] ** 2)) * np.exp(
        -D[i, j] ** 2 / (sigma[i] ** 2 + sigma[j] ** 2))
W = np.maximum(W, W.T)
d = W.sum(1)
Ms = W / np.sqrt(np.outer(d, d))                  # symmetric conjugate of T = D^-1 W
lam, phi = np.linalg.eigh(Ms)
order = np.argsort(lam)[::-1]
lam, phi = lam[order], phi[:, order]
psi = phi / phi[:, [0]]                           # right eigenvectors of T
nc = 10
w = lam[1:nc + 1] / (1 - lam[1:nc + 1])
root = int(np.argmin(t))
dpt = np.sqrt((((psi[:, 1:nc + 1] - psi[root, 1:nc + 1]) * w) ** 2).sum(1))
dpt = dpt / dpt.max()
rho = stats.spearmanr(dpt, t).correlation
print("Spearman rho(DPT, true time)", round(rho, 3), "eigenvalues", np.round(lam[1:4], 4))

# --- MST on k-means centroids
cent, lab = kmeans2(Z, 12, seed=1, minit="++")
Dc = np.sqrt(((cent[:, None] - cent[None]) ** 2).sum(-1))
mst = minimum_spanning_tree(Dc).toarray()

# --- fate probabilities by absorption of a forward-biased random walk
T = np.zeros((N, N))
for i in range(N):
    for j in nn[i]:
        if dpt[j] >= dpt[i] - 0.02:
            T[i, j] = W[i, j]
T[T.sum(1) == 0, root] = 1
T = T / T.sum(1, keepdims=True)
termA = np.where(branch == 1)[0][np.argsort(-dpt[branch == 1])[:25]]
termB = np.where(branch == 2)[0][np.argsort(-dpt[branch == 2])[:25]]
term = np.r_[termA, termB]
trans = np.setdiff1d(np.arange(N), term)
Q = T[np.ix_(trans, trans)]
R = np.c_[T[np.ix_(trans, termA)].sum(1), T[np.ix_(trans, termB)].sum(1)]
Bm = np.linalg.solve(np.eye(len(trans)) - Q, R)
pA = np.zeros(N)
pA[trans] = Bm[:, 0] / Bm.sum(1)
pA[termA] = 1
prog = branch == 0
acc = np.mean(((pA > 0.5) & (branch == 1)) | ((pA < 0.5) & (branch == 2))) / np.mean(branch > 0)
late = (s > 0.3)
acc_late = np.mean(np.where(branch[late] == 1, pA[late] > 0.5, pA[late] < 0.5))
print("progenitor pA mean, sd", round(pA[prog].mean(), 3), round(pA[prog].std(), 3),
      "accuracy branch cells", round(acc, 3), "accuracy late branch cells", round(acc_late, 3),
      "branch cells s<0.1 accuracy", round(np.mean(np.where(branch[(branch > 0) & (s < 0.1)] == 1,
                                                          pA[(branch > 0) & (s < 0.1)] > 0.5,
                                                          pA[(branch > 0) & (s < 0.1)] < 0.5)), 3))

fig, axs = plt.subplots(1, 3, figsize=(12.6, 3.9))
fig.subplots_adjust(left=0.05, right=0.97, bottom=0.15, top=0.88, wspace=0.3)
ax = axs[0]
sc = ax.scatter(Z[:, 0], Z[:, 1], c=dpt, cmap="viridis", s=6, lw=0)
for i in range(12):
    for j in range(12):
        if mst[i, j] > 0:
            ax.plot(cent[[i, j], 0], cent[[i, j], 1], color=P.ink(), lw=1.2)
ax.scatter(cent[:, 0], cent[:, 1], s=22, color=P.ink(), zorder=3)
ax.scatter(Z[root, 0], Z[root, 1], marker="*", s=120, color=charts.line("negative"), zorder=4)
ax.text(Z[root, 0], Z[root, 1] + 0.6, "root", fontsize=7.5, color=P.ink(), ha="center")
cb = fig.colorbar(sc, ax=ax, fraction=0.046, pad=0.02)
cb.ax.tick_params(labelsize=7, colors=P.muted(), labelcolor=P.ink())
charts.style_axes(ax, "PC 1", "PC 2")
charts.title(ax, "A  Diffusion pseudotime and MST")

ax = axs[1]
for b, tok, name in [(0, "neutral", "progenitor"), (1, "rna", "fate A"), (2, "dna", "fate B")]:
    m = branch == b
    ax.scatter(t[m], dpt[m], s=5, color=charts.line(tok), lw=0, label=name)
ax.text(0.03, 0.92, f"Spearman rho = {rho:.3f}", transform=ax.transAxes, fontsize=7.5, color=P.ink())
ax.legend(frameon=False, fontsize=7.5, loc="lower right", markerscale=2.5)
charts.style_axes(ax, "true time", "diffusion pseudotime")
charts.title(ax, "B  Pseudotime recovers order")

ax = axs[2]
sc = ax.scatter(Z[:, 0], Z[:, 1], c=pA, cmap="coolwarm", vmin=0, vmax=1, s=6, lw=0)
ax.scatter(Z[termA, 0], Z[termA, 1], s=10, facecolor="none", edgecolor=P.ink(), lw=0.5)
ax.scatter(Z[termB, 0], Z[termB, 1], s=10, facecolor="none", edgecolor=P.ink(), lw=0.5)
cb = fig.colorbar(sc, ax=ax, fraction=0.046, pad=0.02)
cb.ax.tick_params(labelsize=7, colors=P.muted(), labelcolor=P.ink())
cb.set_label("P(reach fate A)", fontsize=7.5, color=P.ink())
charts.style_axes(ax, "PC 1", "PC 2")
charts.title(ax, "C  Fate probabilities")
