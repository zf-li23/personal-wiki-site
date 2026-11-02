"""Sleep deprivation and reaction time: 18 subjects measured on 10 consecutive days of sleep restriction
(Belenky et al. 2003; R package lme4, data set sleepstudy; 180 observations).

A: every subject's trajectory (spaghetti plot) and the ordinary least-squares line that ignores the subjects.
B: intercepts and slopes of each subject fitted separately (open circles) and the predictions of the
linear mixed model with correlated random intercepts and slopes, fitted by REML (filled dots); the arrows
show how the mixed model pulls the subject-specific lines towards the population line (cross), most
strongly for the subjects whose own fit is least certain or most extreme.
C: six subjects with the separate fit (dashed), the mixed-model fit (solid) and the population line (grey).
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import optimize
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rows = list(csv.DictReader(open("sleepstudy.csv")))
subj = np.array([r["subject"] for r in rows])
days = np.array([float(r["days"]) for r in rows])
y = np.array([float(r["reaction"]) for r in rows])
ids = sorted(set(subj))
Xs = [np.column_stack([np.ones(10), days[subj == s]]) for s in ids]
ys = [y[subj == s] for s in ids]
N, p = len(y), 2


def parts(th):
    L = np.array([[th[0], 0.0], [th[1], th[2]]])
    D = L @ L.T
    A, c, Vis, logdet = np.zeros((2, 2)), np.zeros(2), [], 0.0
    for X, yy in zip(Xs, ys):
        V = np.eye(len(yy)) + X @ D @ X.T
        Vi = np.linalg.inv(V)
        Vis.append(Vi)
        logdet += np.linalg.slogdet(V)[1]
        A += X.T @ Vi @ X
        c += X.T @ Vi @ yy
    b = np.linalg.solve(A, c)
    rss = sum((yy - X @ b) @ Vi @ (yy - X @ b) for X, yy, Vi in zip(Xs, ys, Vis))
    return D, b, rss, logdet, A, Vis


def reml(th):
    D, b, rss, logdet, A, _ = parts(th)
    return logdet + (N - p) * np.log(rss / (N - p)) + np.linalg.slogdet(A)[1]


th = optimize.minimize(reml, [1.0, 0.0, 0.2], method="Nelder-Mead",
                       options=dict(xatol=1e-9, fatol=1e-11, maxiter=20000)).x
D, beta, rss, _, _, Vis = parts(th)
s2 = rss / (N - p)
G = D * s2
blup = np.array([beta + G @ X.T @ (Vi / s2) @ (yy - X @ beta) for X, yy, Vi in zip(Xs, ys, Vis)])
sep = np.array([np.polyfit(X[:, 1], yy, 1)[::-1] for X, yy in zip(Xs, ys)])
ols = np.polyfit(days, y, 1)[::-1]

fig = plt.figure(figsize=(11, 3.9))
axA = fig.add_axes([0.06, 0.15, 0.27, 0.73])
axB = fig.add_axes([0.40, 0.15, 0.25, 0.73])
for s in ids:
    m = subj == s
    axA.plot(days[m], y[m], "-o", ms=2, lw=0.8, color=P.fill("neutral"), mec=charts.line("neutral"), mew=0.4)
xx = np.array([0, 9])
axA.plot(xx, ols[0] + ols[1] * xx, color=charts.line("rna"), lw=2.2, label=f"OLS: {ols[0]:.1f} + {ols[1]:.2f} day")
axA.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(axA, "days of sleep restriction", "mean reaction time / ms")
charts.title(axA, "A  18 subjects")
for (i0, s0), (i1, s1) in zip(sep, blup):
    axB.annotate("", xy=(i1, s1), xytext=(i0, s0),
                 arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=0.7, mutation_scale=7))
axB.plot(sep[:, 0], sep[:, 1], "o", ms=5, mfc="none", mec=charts.line("dna"), mew=1, label="separate fits")
axB.plot(blup[:, 0], blup[:, 1], "o", ms=4, color=charts.line("rna"), label="mixed model (BLUP)")
axB.plot(beta[0], beta[1], "+", ms=12, mew=2, color=P.ink(), label="population")
axB.set_ylim(-5, 31)
axB.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right", ncol=1)
charts.style_axes(axB, "intercept (day 0) / ms", "slope / ms per day")
charts.title(axB, "B  Shrinkage of subject lines")
show = ["308", "309", "330", "335", "337", "350"]
for k, s in enumerate(show):
    ax = fig.add_axes([0.71 + 0.095 * (k % 3), 0.55 - 0.40 * (k // 3), 0.085, 0.33])
    i = ids.index(s)
    m = subj == s
    ax.plot(days[m], y[m], "o", ms=2.5, color=charts.line("neutral"))
    ax.plot(xx, beta[0] + beta[1] * xx, color=P.muted(), lw=0.9)
    ax.plot(xx, sep[i, 0] + sep[i, 1] * xx, color=charts.line("dna"), lw=1.1, ls="--")
    ax.plot(xx, blup[i, 0] + blup[i, 1] * xx, color=charts.line("rna"), lw=1.4)
    ax.set_ylim(180, 470)
    ax.set_xticks([0, 9])
    if k % 3:
        ax.set_yticklabels([])
    charts.style_axes(ax)
    ax.set_title(f"subject {s}", fontsize=FT["tiny"], color=P.ink(), pad=2)
fig.text(0.71, 0.93, "C  Six subjects", fontsize=FT["small"], color=P.ink(), weight="bold")
