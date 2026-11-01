"""A transcription factor whose activity changes while its mRNA does not (simulation). Expression of
2000 genes is simulated in 20 samples of each of two phenotypes. The factor T is equally expressed in
both, but in phenotype B it is activated post-translationally: its 40 activated targets rise and its
20 repressed targets fall by 0.6 standard deviations on average (target-specific effects). A: the
mRNA of T. B: the signature (genes ranked by the Welch t statistic, B against A), with the positions
of the activated (top) and repressed (bottom) targets, and the two running sums of the two-tailed
enrichment (activated targets from the top of the ranking, repressed targets from the bottom).
C: the activity score of T in each sample, the mean standardized expression of the activated targets
minus that of the repressed targets."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
ng, na = 2000, 20
X = rng.normal(0, 1, (ng, 2 * na))
grp = np.r_[np.zeros(na, bool), np.ones(na, bool)]
pos = rng.choice(np.arange(1, ng), 60, replace=False)
up, down = pos[:40], pos[40:]
X[np.ix_(up, grp)] += rng.gamma(4, 0.15, (40, 1))
X[np.ix_(down, grp)] -= rng.gamma(4, 0.15, (20, 1))
tf = X[0]                                     # gene 0 is the factor T itself: no change
t_tf, p_tf = stats.ttest_ind(tf[grp], tf[~grp], equal_var=False)
t, _ = stats.ttest_ind(X[:, grp], X[:, ~grp], axis=1, equal_var=False)
order = np.argsort(-t)
rank = np.empty(ng, int); rank[order] = np.arange(ng)


def running(members, ranking_stat):
    hit = np.zeros(ng, bool); hit[members] = True
    w = np.where(hit, np.abs(ranking_stat), 0.0)
    return np.cumsum(w / w.sum() - (~hit) / (~hit).sum())


ts = t[order]
run_up = running(rank[up], ts)
run_dn = running(ng - 1 - rank[down], ts[::-1])
es_up, es_dn = run_up.max(), run_dn.max()
null = []
for _ in range(1000):
    perm = rng.permutation(ng)
    null.append(running(perm[:40], ts).max() + running(perm[40:60], ts[::-1]).max())
p_es = (1 + np.sum(np.array(null) >= es_up + es_dn)) / 1001
Z = (X - X.mean(1, keepdims=True)) / X.std(1, keepdims=True)
act = Z[up].mean(0) - Z[down].mean(0)
t_act, p_act = stats.ttest_ind(act[grp], act[~grp], equal_var=False)

fig, (a, b, c) = plt.subplots(1, 3, figsize=(10, 3.4), gridspec_kw=dict(width_ratios=[0.7, 1.6, 0.8]))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.86, wspace=0.42)
cA, cB = charts.line("neutral"), charts.line("highlight")
for k, (vals, col) in enumerate([(tf[~grp], cA), (tf[grp], cB)]):
    a.scatter(k + rng.uniform(-0.15, 0.15, na), vals, s=10, color=col, lw=0)
    a.plot([k - 0.25, k + 0.25], [vals.mean()] * 2, color=P.ink(), lw=1)
a.set_xticks([0, 1]); a.set_xticklabels(["A", "B"]); a.set_xlim(-0.6, 1.6)
charts.style_axes(a, "phenotype", "mRNA of T (z)")
charts.title(a, f"A  T mRNA (p = {p_tf:.2f})")
x = np.arange(ng)
b.plot(x, run_up, color=charts.line("positive"), lw=1.2, label=f"activated targets, ES = {es_up:.2f}")
b.plot(ng - 1 - x, run_dn, color=charts.line("negative"), lw=1.2, label=f"repressed targets, ES = {es_dn:.2f}")
b.vlines(rank[up], 0.92, 1.0, color=charts.line("positive"), lw=0.6)
b.vlines(rank[down], -0.22, -0.14, color=charts.line("negative"), lw=0.6)
b.axhline(0, color=P.muted(), lw=0.6)
b.set_ylim(-0.25, 1.05)
b.legend(fontsize=7, frameon=False, loc="center", bbox_to_anchor=(0.5, 0.2), labelcolor=P.ink())
charts.style_axes(b, "rank in the signature (B up ... B down)", "running sum")
charts.title(b, f"B  Two-tailed enrichment (p = {p_es:.3f})")
for k, (vals, col) in enumerate([(act[~grp], cA), (act[grp], cB)]):
    c.scatter(k + rng.uniform(-0.15, 0.15, na), vals, s=10, color=col, lw=0)
    c.plot([k - 0.25, k + 0.25], [vals.mean()] * 2, color=P.ink(), lw=1)
c.set_xticks([0, 1]); c.set_xticklabels(["A", "B"]); c.set_xlim(-0.6, 1.6)
charts.style_axes(c, "phenotype", "activity score of T")
charts.title(c, f"C  Activity (p = {p_act:.0e})")
