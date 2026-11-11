"""Discriminant analysis and independent component analysis versus PCA.

A: two classes of 2-D population responses (500 points each) with means (+-0.75, -+0.75) apart
along the minor axis of strongly correlated noise (covariance with s.d. 3.0 along (1,1)/sqrt2 and
0.5 along (1,-1)/sqrt2, correlation 0.95..): PC1 (dashed) follows the noise, the Fisher discriminant
axis (solid) the signal direction. B: histograms of the two classes projected on PC1 and on the
discriminant axis (area under the ROC curve in the legend).
C: ICA. Two independent sparse (Laplace) sources of 2000 samples are mixed by a fixed 2 x 2 matrix;
PCA axes (dashed, orthogonal) and ICA axes (solid, from FastICA) in the plane of the mixtures; ICA
recovers the mixing directions.
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import FastICA
from scipy.stats import rankdata

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
n = 500
R = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
noise = lambda m: (rng.normal(size=(m, 2)) * [3.0, 0.5]) @ R.T
mu = np.array([0.75, -0.75])
X1, X2 = noise(n) + mu, noise(n) - mu
X = np.vstack([X1, X2])
C = np.cov(np.vstack([X1 - X1.mean(0), X2 - X2.mean(0)]).T)
Sw = C
w_lda = np.linalg.solve(Sw, X1.mean(0) - X2.mean(0))
w_lda /= np.linalg.norm(w_lda)
Xc = X - X.mean(0)
w_pc = np.linalg.svd(Xc, full_matrices=False)[2][0]


def auc(a, b):
    r = rankdata(np.r_[a, b])
    return (r[:len(a)].sum() - len(a) * (len(a) + 1) / 2) / (len(a) * len(b))


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1))
ax = axs[0]
ax.scatter(*X1.T, s=4, color=P.fill("dna"))
ax.scatter(*X2.T, s=4, color=P.fill("rna"))
for w, ls, lab in ((w_pc, "--", "PC1"), (w_lda, "-", "discriminant axis")):
    ax.plot([-9 * w[0], 9 * w[0]], [-9 * w[1], 9 * w[1]], color=P.ink(), ls=ls, lw=1.8, label=lab)
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)
ax.set_aspect("equal")
ax.set_xlabel("Neuron 1")
ax.set_ylabel("Neuron 2")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("A  Signal and noise directions", loc="left", fontsize=10)

ax = axs[1]
bins = np.linspace(-9, 9, 50)
for w, a_, lab in ((w_pc, 0.5, "PC1"), (w_lda, 1.0, "discriminant")):
    p1, p2 = X1 @ w, X2 @ w
    if lab == "PC1" and p1.mean() < p2.mean():
        p1, p2 = -p1, -p2
    ax.hist(p1, bins=bins, histtype="step", color=P.edge("dna"), lw=2, alpha=a_)
    ax.hist(p2, bins=bins, histtype="step", color=P.edge("rna"), lw=2, alpha=a_)
    ax.plot([], [], color=P.ink(), alpha=a_, lw=2, label=f"{lab}: AUC {max(auc(X1 @ w, X2 @ w), 1 - auc(X1 @ w, X2 @ w)):.2f}")
ax.set_xlabel("Projection")
ax.set_ylabel("Number of trials")
ax.set_ylim(0, 215)
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("B  Separation of the classes", loc="left", fontsize=10)

ax = axs[2]
S = rng.laplace(size=(2000, 2))
A_mix = np.array([[1.0, 0.6], [0.3, 1.0]])
M = S @ A_mix.T
ica = FastICA(2, whiten="unit-variance", random_state=0, max_iter=1000).fit(M)
Wc = np.linalg.pinv(ica.mixing_)     # unmixing
dirs = ica.mixing_ / np.linalg.norm(ica.mixing_, axis=0)
pcs = np.linalg.svd(M - M.mean(0), full_matrices=False)[2]
ax.scatter(*M.T, s=3, color=P.fill("dna"), alpha=0.6)
for v in pcs:
    ax.plot([-9 * v[0], 9 * v[0]], [-9 * v[1], 9 * v[1]], color=P.ink(), ls="--", lw=1.6)
for v in dirs.T:
    ax.plot([-9 * v[0], 9 * v[0]], [-9 * v[1], 9 * v[1]], color=P.edge("rna"), lw=2)
ax.plot([], [], color=P.ink(), ls="--", label="PCA axes (orthogonal)")
ax.plot([], [], color=P.edge("rna"), label="ICA axes (mixing directions)")
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)
ax.set_aspect("equal")
ax.set_xlabel("Mixture 1")
ax.set_ylabel("Mixture 2")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("C  Sparse sources mixed linearly", loc="left", fontsize=10)
fig.tight_layout()
