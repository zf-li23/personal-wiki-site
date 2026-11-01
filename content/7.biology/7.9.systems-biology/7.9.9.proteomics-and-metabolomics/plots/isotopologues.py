"""Mass isotopomer distributions (MIDs) of citrate, C6H8O7, and their correction for natural isotope
abundance (13C 1.07%, 2H 0.0115%, 17O 0.038%, 18O 0.205%). A: the MID of unlabeled citrate is not
pure M+0: 6.3% of the molecules are M+1 and 1.5% M+2. B: a labeling experiment (synthetic true
MID of citrate after growth on [U-13C]glucose, chosen for illustration); the measured MID is the
true one convolved with the natural isotopes of the unlabeled carbons, hydrogens and oxygens
(Eq. (9.9)), and the corrected MID is recovered by non-negative least squares. C: the correction
matrix, column j being the measured distribution of a molecule with exactly j labeled carbons (each column
renormalized over M+0 to M+6, which is why the last entry is 1)."""

import numpy as np
import matplotlib.pyplot as plt
from math import comb
from scipy.optimize import nnls
import wikibio as bio
from wikibio import charts

P = bio.P
nC, nH, nO = 6, 8, 7
pC = 0.0107


def conv(*ds):
    out = np.array([1.0])
    for d in ds:
        out = np.convolve(out, d)
    return out


def binom_dist(n, p):
    return np.array([comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)])


H = np.array([0.999885, 0.000115])
O = np.array([0.99757, 0.00038, 0.00205])
other = conv(*([H] * nH + [O] * nO))
K = nC + 1
A = np.zeros((K, K))
for j in range(K):
    d = conv(np.r_[np.zeros(j), 1.0], binom_dist(nC - j, pC), other)[:K]
    A[:, j] = d
A_norm = A / A.sum(axis=0)

true = np.array([0.35, 0.04, 0.33, 0.06, 0.14, 0.03, 0.05])
meas = A_norm @ true
meas = meas / meas.sum()
corr, _ = nnls(A_norm, meas)
corr = corr / corr.sum()
unl = A_norm[:, 0] / A_norm[:, 0].sum()
FE = {k: (np.arange(K) * v).sum() / nC for k, v in [("true", true), ("measured", meas), ("corrected", corr)]}

fig, (a, b, c) = plt.subplots(1, 3, figsize=(10.5, 3.4), gridspec_kw=dict(width_ratios=[1, 1.4, 1.1]))
fig.subplots_adjust(left=0.06, right=0.97, bottom=0.17, top=0.86, wspace=0.35)
x = np.arange(K)
a.bar(x, unl * 100, color=P.fill("metabolite"), edgecolor=P.edge("metabolite"))
for i in range(3):
    a.text(i, unl[i] * 100 + 2, f"{unl[i] * 100:.1f}", ha="center", fontsize=7, color=P.ink())
a.set_xticks(x, [f"M+{i}" for i in x], fontsize=7)
charts.style_axes(a, None, "fraction (%)")
charts.title(a, "A  Unlabeled citrate")

w = 0.27
for k, (lab, v, tok) in enumerate([("true", true, "neutral"), ("measured", meas, "rna"), ("corrected", corr, "dna")]):
    b.bar(x + (k - 1) * w, v * 100, w, color=P.fill(tok), edgecolor=P.edge(tok), label=f"{lab} (FE {FE[lab] * 100:.1f}%)")
b.set_xticks(x, [f"M+{i}" for i in x], fontsize=7)
b.legend(frameon=False, fontsize=7)
charts.style_axes(b, None, "fraction (%)")
charts.title(b, "B  [U-13C]glucose labeling")

from matplotlib.patches import Rectangle
for i in range(K):
    for j in range(K):
        v = A_norm[i, j]
        if v > 0.0005:
            c.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, facecolor=P.fill("dna"), alpha=min(0.95, 0.15 + v), lw=0))
            c.text(j, i, f"{v:.3f}", ha="center", va="center", fontsize=5.5,
                   color=P.on_fill() if v > 0.5 else P.ink())
c.set_xlim(-0.5, K - 0.5)
c.set_ylim(K - 0.5, -0.5)
c.set_aspect("equal")
c.set_xticks(x, x, fontsize=7)
c.set_yticks(x, [f"M+{i}" for i in x], fontsize=7)
charts.style_axes(c, "labeled carbons j", None, box=True)
charts.title(c, "C  Correction matrix")
