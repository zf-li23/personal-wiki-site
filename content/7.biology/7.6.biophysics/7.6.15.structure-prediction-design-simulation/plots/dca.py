# Contacts from coevolution: mutual information versus direct coupling analysis on a toy Potts model.
# A "protein" of L = 30 sites with an alphabet of q = 4 residue types has a known set of 36 contacts
# (pairs with |i - j| >= 5). Sequences are drawn from the Potts model
# P(s) ~ exp[ sum_i h_i(s_i) + sum_{i<j} J_ij(s_i, s_j) ], with random fields h (s.d. 0.3) and, for each
# contact, a coupling that rewards complementary pairs (J = 2.2 if s_i + s_j = 3, -0.7 otherwise);
# 800 independent Gibbs-sampling chains of 200 sweeps give the "multiple sequence alignment".
# Mutual information (with the average-product correction, APC) and mean-field DCA (couplings from the
# inverse of the covariance matrix of the one-hot encoded alignment, pseudocount 0.5, Frobenius norm in
# the zero-sum gauge, APC) score every pair.
# A: true contacts (grey squares) and the 36 top-scoring pairs by DCA (upper triangle) and by MI (lower
#    triangle); true positives filled, false positives open. MI is confused by indirect correlations
#    transmitted along chains of contacts (i-j and j-k make i and k correlated without contact).
# B: precision (fraction of true contacts) among the top-ranked pairs against their number.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(8)
L, q, M, sweeps = 30, 4, 800, 200
pairs = [(i, j) for i in range(L) for j in range(i + 5, L)]
idx = rng.choice(len(pairs), 36, replace=False)
contacts = {pairs[k] for k in idx}
h = rng.normal(0, 0.3, (L, q))
J = np.zeros((L, L, q, q))
comp = np.where(np.add.outer(np.arange(q), np.arange(q)) == q - 1, 2.2, -0.7)
for i, j in contacts:
    J[i, j] = comp
    J[j, i] = comp.T

s = rng.integers(0, q, (M, L))
cols = np.arange(L)
for _ in range(sweeps):
    for i in range(L):
        Ji = J[i]                                   # (L, q, q): J[i, j, a, b]
        field = h[i][None, :] + Ji[cols[None, :], :, s].sum(axis=1)   # (M, q)
        p = np.exp(field - field.max(1, keepdims=True))
        p /= p.sum(1, keepdims=True)
        u = rng.random((M, 1))
        s[:, i] = (p.cumsum(1) < u).sum(1)

onehot = np.zeros((M, L, q))
onehot[np.arange(M)[:, None], cols[None, :], s] = 1
lam = 0.5
fi = (1 - lam) * onehot.mean(0) + lam / q
fij = (1 - lam) * np.einsum("mia,mjb->ijab", onehot, onehot) / M + lam / q**2
for i in range(L):
    fij[i, i] = np.diag(fi[i])
# mutual information
MI = np.zeros((L, L))
for i in range(L):
    for j in range(i + 1, L):
        pij = fij[i, j]
        MI[i, j] = MI[j, i] = np.sum(pij * np.log(pij / np.outer(fi[i], fi[j])))


def apc(S):
    S = S.copy()
    np.fill_diagonal(S, 0)
    m = S.sum(1) / (L - 1)
    out = S - np.outer(m, m) / (S.sum() / (L * (L - 1)))
    np.fill_diagonal(out, 0)
    return out


C = (fij[:, :, :q - 1, :q - 1] - np.einsum("ia,jb->ijab", fi[:, :q - 1], fi[:, :q - 1]))
C = C.transpose(0, 2, 1, 3).reshape(L * (q - 1), L * (q - 1))
Jmf = -np.linalg.inv(C).reshape(L, q - 1, L, q - 1).transpose(0, 2, 1, 3)
Jfull = np.zeros((L, L, q, q))
Jfull[:, :, :q - 1, :q - 1] = Jmf
Jz = Jfull - Jfull.mean(2, keepdims=True) - Jfull.mean(3, keepdims=True) + Jfull.mean((2, 3), keepdims=True)
FN = np.sqrt((Jz**2).sum((2, 3)))
scores = {"DCA": apc(FN), "MI": apc(MI)}


def ranked(S):
    cand = [(S[i, j], i, j) for i, j in pairs]
    cand.sort(reverse=True)
    return [(i, j) for _, i, j in cand]


fig, axs = plt.subplots(1, 2, figsize=(11, 4.8), gridspec_kw={"width_ratios": [1, 1.2]})
ax = axs[0]
for i, j in contacts:
    for a, b in ((i, j), (j, i)):
        ax.add_patch(plt.Rectangle((b - 0.5, a - 0.5), 1, 1, color=P.light("neutral"), lw=0))
for name, tok, upper in (("DCA", "dna", True), ("MI", "negative", False)):
    top = ranked(scores[name])[:36]
    for i, j in top:
        a, b = (i, j) if upper else (j, i)
        hit = (i, j) in contacts
        ax.plot(b, a, "o", ms=5, color=charts.line(tok), mfc=charts.line(tok) if hit else "none", mew=1.1)
ax.plot([-0.5, L - 0.5], [-0.5, L - 0.5], color=P.muted(), lw=0.6)
ax.set_xlim(-0.5, L - 0.5)
ax.set_ylim(L - 0.5, -0.5)
ax.set_aspect("equal")
ax.text(L - 1, 1, "DCA", ha="right", fontsize=8, color=charts.line("dna"), weight="bold")
ax.text(1, L - 2, "MI", ha="left", fontsize=8, color=charts.line("negative"), weight="bold")
charts.style_axes(ax, "residue j", "residue i", box=True)
charts.title(ax, "A   Predicted contacts (top 36)")

ax = axs[1]
ks = np.arange(1, 73)
for name, tok in (("DCA", "dna"), ("MI", "negative")):
    r = ranked(scores[name])
    prec = [np.mean([(p in contacts) for p in r[:k]]) for k in ks]
    ax.plot(ks, prec, color=charts.line(tok), lw=1.8, label=name)
ax.axvline(36, color=P.muted(), lw=0.6, ls=":")
ax.text(37, 0.05, "number of true contacts", fontsize=7, color=P.muted())
ax.axhline(len(contacts) / len(pairs), color=P.muted(), lw=0.6, ls="--")
ax.text(70, len(contacts) / len(pairs) + 0.02, "random", ha="right", fontsize=7, color=P.muted())
ax.set_ylim(0, 1.05)
ax.legend(fontsize=8, frameon=False)
charts.style_axes(ax, "number of top-ranked pairs", "precision")
charts.title(ax, "B   Precision of contact prediction")
fig.tight_layout()
