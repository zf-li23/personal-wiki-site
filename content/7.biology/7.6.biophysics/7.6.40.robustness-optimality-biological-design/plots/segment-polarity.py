# Parameter robustness of a pattern-maintaining network, in the spirit of von Dassow, Meir, Munro and
# Odell (2000) and Ingolia (2004). A one-dimensional row of 12 cells (three repeats of four) with two
# variables per cell: E (engrailed/hedgehog) and W (wingless). E in cell i is activated by W in its
# anterior neighbour i-1 (Hill function, K_E, n_E); W in cell i is activated by its own W (autoregulation,
# weight a, K_A, n_A) and by E in its posterior neighbour i+1 (K_H, n_H), and repressed by E in the same
# cell (K_R, n_R); both decay with unit rate (E with rate 1/tau). The directional coupling stands for the
# anterior-posterior asymmetry that other segment-polarity genes supply in the embryo.
# Task: from a transient prepattern (easy: W = 1 in cell 0 and E = 1 in cell 1 of each repeat; hard: the
# same with weak expression spilling into neighbouring cells, 0.5 and 0.35) the network must settle into
# and keep the pattern W only in cell 0, E only in cell 1. 10 parameters drawn log-uniformly
# (K in [0.01, 1], n in [1, 6], a in [0.05, 1], tau in [0.2, 5]); 3000 random sets per task.
# A: fraction of random parameter sets that perform each task. B: the successful sets span decades in each
# threshold (distributions of log10 K). C: for 40 successful sets, the factor by which each single
# parameter can be changed (up or down) before the pattern fails (hard task); most tolerate tenfold changes, the two
# activation thresholds K_E and K_H do not.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
np.seterr(over="ignore", under="ignore")
rng = np.random.default_rng(0)
N = 12
names = ["$K_E$", "$n_E$", "$K_A$", "$n_A$", "$a$", "$K_H$", "$n_H$", "$K_R$", "$n_R$", "$\\tau$"]
lo = np.log10([0.01, 1, 0.01, 1, 0.05, 0.01, 1, 0.01, 1, 0.2])
hi = np.log10([1, 6, 1, 6, 1, 1, 6, 1, 6, 5])


def hill(x, K, n):
    r = np.clip(x, 1e-12, None) / K
    return 1.0 / (1.0 + np.power(r, -n))


def run(par, task):
    M = par.shape[0]
    KE, nE, KA, nA, a, KH, nH, KR, nR, tau = [par[:, j:j + 1] for j in range(10)]
    E = np.zeros((M, N)); W = np.zeros((M, N))
    W[:, 0::4] = 1.0; E[:, 1::4] = 1.0
    if task == "hard":
        W[:, 0::4] = 0.5; E[:, 1::4] = 0.5
        W[:, 3::4] = 0.35; E[:, 2::4] = 0.35
    dt = 0.15
    decE = np.exp(-dt / tau)
    decW = np.exp(-dt)
    for _ in range(1000):
        Wa = np.roll(W, 1, axis=1)   # anterior neighbour i-1
        Ep = np.roll(E, -1, axis=1)  # posterior neighbour i+1
        tE = hill(Wa, KE, nE)
        tW = (a * hill(W, KA, nA) + (1 - a) * hill(Ep, KH, nH)) * (1 - hill(E, KR, nR))
        E = tE + (E - tE) * decE  # exact relaxation over dt towards the current target (stable for any tau)
        W = tW + (W - tW) * decW
    want_W = np.zeros(N, bool); want_W[0::4] = True
    want_E = np.zeros(N, bool); want_E[1::4] = True
    ok = (W[:, want_W].min(1) > 0.5) & (W[:, ~want_W].max(1) < 0.2) & (E[:, want_E].min(1) > 0.5) & (E[:, ~want_E].max(1) < 0.2)
    return ok


M = 3000
par = 10 ** (lo + (hi - lo) * rng.random((M, 10)))
ok_easy = run(par, "easy")
ok_hard = run(par, "hard")

fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0), gridspec_kw=dict(width_ratios=[0.7, 1.2, 1.3]))
ax = axs[0]
fr = [ok_easy.mean(), ok_hard.mean()]
ax.bar([0, 1], fr, color=[P.fill("enzyme"), P.fill("protein")], edgecolor=[P.edge("enzyme"), P.edge("protein")])
for i, f in enumerate(fr):
    ax.text(i, f + 0.01, f"{100 * f:.1f} %", ha="center", fontsize=8, color=P.ink())
ax.set_xticks([0, 1], ["keep\npattern", "sharpen\nand keep"])
charts.style_axes(ax, None, "fraction of random parameter sets")
charts.title(ax, "A   Many parameter sets work")

ax = axs[1]
good = par[ok_hard]
bins = np.linspace(-2, 0, 21)
for j, tok in ((0, "dna"), (2, "enzyme"), (5, "rna"), (7, "protein")):
    ax.hist(np.log10(good[:, j]), bins=bins, histtype="step", lw=1.6, color=charts.line(tok), density=True, label=names[j])
ax.legend(fontsize=7.5, frameon=False, ncol=2)
charts.style_axes(ax, "$\\log_{10}$ threshold (successful sets, hard task)", "density")
charts.title(ax, "B   Working thresholds span decades")

ax = axs[2]
base = good[:30]
factors = 10 ** np.linspace(0.25, 2, 8)
tol = np.zeros((30, 10, 2))
for j in range(10):
    for d, sgn in enumerate((-1, 1)):
        trial = np.repeat(base[:, None, :], len(factors), axis=1).copy()
        f = factors ** sgn
        if j in (1, 3, 6, 8):  # Hill coefficients stay >= 1
            trial[:, :, j] = np.maximum(1.0, trial[:, :, j] * f)
        elif j == 4:
            trial[:, :, j] = np.clip(trial[:, :, j] * f, 0, 1)
        else:
            trial[:, :, j] = trial[:, :, j] * f
        okk = run(trial.reshape(-1, 10), "hard").reshape(30, len(factors))
        first_fail = np.argmax(~okk, axis=1)
        allok = okk.all(1)
        val = np.where(allok, np.log10(factors[-1]), np.log10(factors[np.maximum(first_fail - 1, 0)]) * (first_fail > 0))
        tol[:, j, d] = val
med = np.median(tol, axis=0)
q1, q3 = np.percentile(tol, 25, axis=0), np.percentile(tol, 75, axis=0)
y = np.arange(10)
ax.barh(y, med[:, 1], color=P.fill("positive"), edgecolor=P.edge("positive"), height=0.6, label="increase")
ax.barh(y, -med[:, 0], color=P.fill("negative"), edgecolor=P.edge("negative"), height=0.6, label="decrease")
ax.errorbar(med[:, 1], y, xerr=[med[:, 1] - q1[:, 1], q3[:, 1] - med[:, 1]], fmt="none", ecolor=P.muted(), lw=0.8)
ax.errorbar(-med[:, 0], y, xerr=[q3[:, 0] - med[:, 0], med[:, 0] - q1[:, 0]], fmt="none", ecolor=P.muted(), lw=0.8)
ax.axvline(0, color=P.ink(), lw=0.8)
ax.set_yticks(y, names)
ax.set_xlim(-2.1, 2.1)
ax.set_xticks([-2, -1, 0, 1, 2], ["÷100", "÷10", "1", "×10", "×100"])
ax.legend(fontsize=7.5, frameon=False, loc="lower right")
charts.style_axes(ax, "single-parameter change tolerated (median, quartiles)", None)
charts.title(ax, "C   Most parameters tolerate large changes")
fig.tight_layout()
