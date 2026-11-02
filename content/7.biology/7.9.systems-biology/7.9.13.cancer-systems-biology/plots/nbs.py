"""Network-based stratification on a toy example (simulation). A: an interaction network of 36 genes:
two pathways of 12 genes (blue and amber; pairs within a pathway interact with probability 0.35)
joined by a few edges, and 12 other genes. Each of 40 tumors carries one or two mutations in a gene of
one pathway (20 tumors per pathway, a different subtype each) and one or two passenger mutations
anywhere; thick red outlines show the mutated genes of two tumors of the same subtype, which share no
mutated gene (one of the outlined genes is a passenger in the other pathway). B: cosine similarity between the tumors' binary mutation profiles, ordered by true
subtype. C: the same after network propagation of each profile (random walk with restart, restart
probability 0.3). Below each panel: the agreement of a rank-2 non-negative matrix factorization
(each tumor assigned to its larger factor) with the true subtypes."""

import numpy as np
import matplotlib.pyplot as plt
import wikigraph as G
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(3)
n, m = 36, 12
mod = np.r_[np.zeros(m, int), np.ones(m, int), np.full(m, 2)]
A = np.zeros((n, n))
for i in range(n):
    for j in range(i + 1, n):
        p = 0.35 if mod[i] == mod[j] < 2 else (0.12 if mod[i] == mod[j] == 2 else 0.02)
        if rng.random() < p:
            A[i, j] = A[j, i] = 1
for i in range(n):                                   # no isolated genes
    if A[i].sum() == 0:
        j = rng.choice([k for k in range(n) if k != i])
        A[i, j] = A[j, i] = 1
W = A / A.sum(0)
r = 0.3
K = r * np.linalg.inv(np.eye(n) - (1 - r) * W)

n_pat = 40
sub = np.r_[np.zeros(20, int), np.ones(20, int)]
X = np.zeros((n_pat, n))
for k in range(n_pat):
    X[k, rng.choice(np.where(mod == sub[k])[0], rng.integers(1, 3), replace=False)] = 1
    X[k, rng.choice(n, rng.integers(1, 3), replace=False)] = 1
Xp = X @ K.T                                          # propagated profiles (rows: tumors)
Xp = Xp / Xp.sum(1, keepdims=True)


def cosine(M):
    U = M / np.linalg.norm(M, axis=1, keepdims=True)
    return U @ U.T


def nmf2(M, seed):
    rr = np.random.default_rng(seed)
    Wf, H = rr.random((M.shape[0], 2)) + 0.1, rr.random((2, M.shape[1])) + 0.1
    for _ in range(500):
        H *= (Wf.T @ M) / (Wf.T @ Wf @ H + 1e-12)
        Wf *= (M @ H.T) / (Wf @ H @ H.T + 1e-12)
    return Wf, np.linalg.norm(M - Wf @ H)


def accuracy(M):
    Wf = min((nmf2(M, s) for s in range(10)), key=lambda f: f[1])[0]
    lab = np.argmax(Wf, 1)
    return max(np.mean(lab == sub), np.mean(lab != sub))


acc_raw, acc_prop = accuracy(X), accuracy(Xp)
k1 = 0
k2 = next(k for k in range(1, 20) if not (X[k] * X[k1]).any())

fig = plt.figure(figsize=(11, 4.0))
axA = fig.add_axes([0.0, 0.05, 0.36, 0.85])
axB = fig.add_axes([0.42, 0.2, 0.24, 0.68])
axC = fig.add_axes([0.72, 0.2, 0.24, 0.68])
ang = np.linspace(0, 2 * np.pi, m, endpoint=False)
pos = {}
for i in range(n):
    c = [(-2.2, 1.4), (2.2, 1.4), (0, -2.0)][mod[i]]
    a = ang[i % m]
    rad = 1.3 if mod[i] < 2 else 1.6
    pos[str(i)] = (c[0] + rad * np.cos(a), c[1] + rad * np.sin(a))
edges = [(str(i), str(j)) for i in range(n) for j in range(i + 1, n) if A[i, j]]
fill = {str(i): [G.BLUE, G.AMBER, G.GREY][mod[i]] for i in range(n)}
hl = {str(i): G.RED for i in np.where(X[k1] + X[k2] > 0)[0]}
axA.set_xlim(-4.2, 4.2)
axA.set_ylim(-4.0, 3.3)
axA.set_aspect("equal")
axA.axis("off")
G.draw(axA, pos, edges, labels=False, vertex_color=fill, highlight=hl, radius=0.22)
axA.text(-4.0, 3.2, "A  Network and two tumors of one subtype", fontsize=9, weight="bold", color=P.ink(), va="top")
for ax, M, title, acc in [(axB, X, "B  Raw mutation profiles", acc_raw), (axC, Xp, "C  After propagation", acc_prop)]:
    im = ax.imshow(cosine(M), cmap="viridis", vmin=0, vmax=1)
    ax.axhline(19.5, color="white", lw=0.8)
    ax.axvline(19.5, color="white", lw=0.8)
    ax.set_xticks([9.5, 29.5])
    ax.set_xticklabels(["subtype 1", "subtype 2"])
    ax.set_yticks([9.5, 29.5])
    ax.set_yticklabels(["subtype 1", "subtype 2"], rotation=90, va="center")
    charts.style_axes(ax, f"NMF agreement: {acc:.0%}", None, box=True)
    charts.title(ax, title)
cb = fig.colorbar(im, ax=axC, fraction=0.05, pad=0.03)
cb.ax.tick_params(labelsize=7)
