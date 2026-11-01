"""Comparing network-inference methods on a simulated network with known edges. Ten transcription
factors (with four regulatory edges among them) regulate 50 target genes, each target receiving one
to three inputs, activating or repressing, through saturating (tanh) responses plus noise; expression
is simulated in n = 200 samples. Every method ranks the 590 candidate edges from a factor to another
gene, of which 118 are true. A: precision-recall curves. B: area under the precision-recall curve
(average precision); the dashed line is the precision of a random ranking, 118/590 = 0.2. Methods:
absolute Pearson correlation; absolute partial correlation given all other genes; mutual information
(k-nearest-neighbor estimator) after ARACNe pruning (edges removed by the DPI ranked after the kept
ones); CLR; GENIE3-style random-forest importance; and the community ranking, the average of the
five ranks."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree
from scipy.special import digamma
from scipy.stats import rankdata
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import average_precision_score, precision_recall_curve
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
nt, ng, n = 10, 60, 200
W = np.zeros((ng, ng))                          # W[i, j]: effect of factor i on gene j
for i, j in [(0, 1), (2, 3), (4, 5), (6, 7)]:
    W[i, j] = rng.choice([-1, 1]) * rng.uniform(0.8, 1.4)
for j in range(nt, ng):
    for i in rng.choice(nt, rng.integers(1, 4), replace=False):
        W[i, j] = rng.choice([-1, 1]) * rng.uniform(0.6, 1.4)
X = np.zeros((n, ng))
for j in range(ng):                             # factors 0-9 precede the targets; edges go forward
    X[:, j] = 1.5 * np.tanh(X @ W[:, j]) + rng.normal(0, 0.5, n) if W[:, j].any() else rng.normal(0, 1, n)
X = (X - X.mean(0)) / X.std(0)
cand = [(i, j) for i in range(nt) for j in range(ng) if i != j]
truth = np.array([W[i, j] != 0 for i, j in cand])


def ksg(x, y, k=4):
    pts = np.column_stack([x, y]) + rng.normal(0, 1e-10, (len(x), 2))
    d, _ = cKDTree(pts).query(pts, k + 1, p=np.inf)
    e = d[:, k]
    xs, ys = np.sort(pts[:, 0]), np.sort(pts[:, 1])
    nx = np.searchsorted(xs, pts[:, 0] + e) - np.searchsorted(xs, pts[:, 0] - e, "right") - 1
    ny = np.searchsorted(ys, pts[:, 1] + e) - np.searchsorted(ys, pts[:, 1] - e, "right") - 1
    return max(0.0, digamma(k) + digamma(len(x)) - np.mean(digamma(nx + 1) + digamma(ny + 1)))


C = np.corrcoef(X.T)
Om = np.linalg.inv(C + 0.05 * np.eye(ng))
PC = -Om / np.sqrt(np.outer(np.diag(Om), np.diag(Om)))
MI = np.zeros((ng, ng))
for i in range(ng):
    for j in range(i + 1, ng):
        MI[i, j] = MI[j, i] = ksg(X[:, i], X[:, j])
# ARACNe: remove the weakest edge of every triangle (tolerance 0)
keep = np.ones((ng, ng), bool)
for i in range(ng):
    for j in range(i + 1, ng):
        others = [k for k in range(ng) if k not in (i, j)]
        if any(MI[i, j] < min(MI[i, k], MI[j, k]) for k in others):
            keep[i, j] = keep[j, i] = False
aracne = MI + 10 * keep
mu, sd = MI.mean(1), MI.std(1)
z = np.maximum(0, (MI - mu[:, None]) / sd[:, None])
clr = np.sqrt(z**2 + z.T**2)
imp = np.zeros((ng, ng))
for j in range(ng):
    feats = [i for i in range(nt) if i != j]
    rf = RandomForestRegressor(n_estimators=100, max_features="sqrt", min_samples_leaf=2, random_state=0)
    rf.fit(X[:, feats], X[:, j])
    imp[feats, j] = rf.feature_importances_
scores = {"Pearson |r|": np.abs(C), "partial correlation": np.abs(PC), "MI + DPI (ARACNe)": aracne,
          "CLR": clr, "random forest (GENIE3)": imp}
S = {k: np.array([v[i, j] for i, j in cand]) for k, v in scores.items()}
S["community (mean rank)"] = np.mean([rankdata(s) for s in S.values()], axis=0)
ap = {k: average_precision_score(truth, s) for k, s in S.items()}
base = truth.mean()

fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.8), gridspec_kw=dict(width_ratios=[1.1, 1]))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.14, top=0.9, wspace=0.55)
cols = [P.edge(P.protein(i)) for i in range(5)] + [P.ink()]
for (k, s), col in zip(S.items(), cols):
    pr, rc, _ = precision_recall_curve(truth, s)
    a.plot(rc, pr, color=col, lw=2.0 if k.startswith("community") else 1.1, label=k)
a.axhline(base, ls="--", color=P.muted(), lw=0.8)
a.set_xlim(0, 1); a.set_ylim(0, 1.02)
a.legend(fontsize=6.5, frameon=False, loc="lower left", bbox_to_anchor=(0.02, 0.28), labelcolor=P.ink())
charts.style_axes(a, "recall", "precision")
charts.title(a, "A  Precision-recall curves")
names = list(S)
b.barh(range(len(names)), [ap[k] for k in names], color=cols, height=0.6)
for y, k in enumerate(names):
    b.text(ap[k] + 0.01, y, f"{ap[k]:.2f}", va="center", fontsize=7, color=P.ink())
b.axvline(base, ls="--", color=P.muted(), lw=0.8)
b.set_yticks(range(len(names))); b.set_yticklabels(names, fontsize=7)
b.invert_yaxis(); b.set_xlim(0, 1)
charts.style_axes(b, "average precision", None)
charts.title(b, "B  Area under the PR curve")
