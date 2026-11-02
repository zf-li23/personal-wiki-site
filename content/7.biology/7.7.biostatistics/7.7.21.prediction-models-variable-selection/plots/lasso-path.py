"""Lasso logistic regression for low birth weight (189 births, Baystate Medical Center 1986; Hosmer and
Lemeshow; R MASS::birthwt) with 27 candidate predictors: mother's age, weight, race (two indicators),
smoking, previous premature labour, hypertension, uterine irritability and physician visits, the
interactions of smoking with each of the other eight, and ten pure-noise standard normal variables
(seed 0). Predictors standardized; coordinate descent on the penalized likelihood (as in glmnet) for 50
values of lambda. A: coefficient paths; coloured: the clinical main effects, grey dashed: noise
variables. B: 10-fold cross-validated deviance per observation (mean and standard error over folds)
with lambda_min and the one-standard-error lambda_1se.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("birthwt.csv") as fh:
    rows = list(csv.DictReader(fh))
c = {k: np.array([float(r[k]) for r in rows]) for k in ("low", "age", "lwt", "race", "smoke", "ptl", "ht", "ui", "ftv")}
base = {"age": c["age"], "lwt": c["lwt"], "black": (c["race"] == 2) * 1.0, "other": (c["race"] == 3) * 1.0,
        "smoke": c["smoke"], "ptd": (c["ptl"] > 0) * 1.0, "ht": c["ht"], "ui": c["ui"], "ftv": c["ftv"]}
names = list(base)
cols = [base[k] for k in names]
for k in [k for k in base if k != "smoke"]:
    names.append("smoke:" + k)
    cols.append(base["smoke"] * base[k])
rng = np.random.default_rng(0)
for j in range(10):
    names.append(f"noise{j + 1}")
    cols.append(rng.normal(size=len(rows)))
X = np.column_stack(cols)
y = c["low"]
n, p = X.shape


def lasso_logit(Z, y, lams, tol=1e-6):
    nn = len(y)
    b0 = np.log(y.mean() / (1 - y.mean()))
    b = np.zeros(Z.shape[1])
    out = []
    for lam in lams:
        for _ in range(100):
            eta = b0 + Z @ b
            pr = 1 / (1 + np.exp(-eta))
            w = np.clip(pr * (1 - pr), 1e-5, None)
            zt = eta + (y - pr) / w
            bold, b0old = b.copy(), b0
            den = (w[:, None] * Z ** 2).sum(0) / nn
            for _ in range(100):
                b0n = np.sum(w * (zt - Z @ b)) / w.sum()
                maxd = abs(b0n - b0)
                b0 = b0n
                r = zt - b0 - Z @ b
                for j in range(Z.shape[1]):
                    rj = r + Z[:, j] * b[j]
                    num = np.sum(w * Z[:, j] * rj) / nn
                    bj = np.sign(num) * max(abs(num) - lam, 0) / den[j]
                    if bj != b[j]:
                        r = rj - Z[:, j] * bj
                        maxd = max(maxd, abs(bj - b[j]))
                        b[j] = bj
                if maxd < tol:
                    break
            if np.max(np.abs(b - bold)) + abs(b0 - b0old) < tol:
                break
        out.append((b0, b.copy()))
    return out


def deviance(y, eta):
    pr = np.clip(1 / (1 + np.exp(-eta)), 1e-12, 1 - 1e-12)
    return -2 * np.mean(y * np.log(pr) + (1 - y) * np.log(1 - pr))


Z = (X - X.mean(0)) / X.std(0)
lmax = np.max(np.abs(Z.T @ (y - y.mean()))) / n
lams = lmax * np.logspace(0, -2.5, 50)
path = lasso_logit(Z, y, lams)
B = np.array([b for _, b in path])
fold = np.random.default_rng(1).permutation(np.arange(n) % 10)
cvd = np.zeros((10, lams.size))
for k in range(10):
    tr = fold != k
    mu, sd = X[tr].mean(0), X[tr].std(0)
    pk = lasso_logit((X[tr] - mu) / sd, y[tr], lams)
    for i, (b0, b) in enumerate(pk):
        cvd[k, i] = deviance(y[~tr], b0 + ((X[~tr] - mu) / sd) @ b)
mcv = cvd.mean(0)
se = cvd.std(0, ddof=1) / np.sqrt(10)
imin = int(np.argmin(mcv))
i1 = int(np.min(np.where(mcv <= mcv[imin] + se[imin])[0]))
fig, axs = plt.subplots(1, 2, figsize=(10.4, 4.0))
fig.subplots_adjust(left=0.07, right=0.97, bottom=0.14, top=0.88, wspace=0.38)
ax = axs[0]
ll = np.log10(lams)
toks = {"age": "dna", "lwt": "rna", "black": "enzyme", "other": "protein", "smoke": "plant", "ptd": "receptor",
        "ht": "drug", "ui": "lipid", "ftv": "metabolite"}
for j, nm in enumerate(names):
    if nm in toks:
        ax.plot(ll, B[:, j], color=charts.line(toks[nm]), lw=1.4)
    elif nm.startswith("noise"):
        ax.plot(ll, B[:, j], color=P.muted(), lw=0.8, ls="--")
    else:
        ax.plot(ll, B[:, j], color=P.fill("neutral"), lw=0.8)
lab = sorted([(B[-1, j], nm) for j, nm in enumerate(names) if nm in toks])
ys = [v for v, _ in lab]
for k in range(1, len(ys)):
    ys[k] = max(ys[k], ys[k - 1] + 0.045)
for (v, nm), yy in zip(lab, ys):
    ax.annotate(nm, xy=(ll[-1], v), xytext=(ll[-1] - 0.12, yy), fontsize=5.8, color=charts.line(toks[nm]),
                va="center", ha="left", annotation_clip=False,
                arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.4))
for i in (imin, i1):
    ax.axvline(ll[i], color=P.muted(), lw=0.7, ls=":")
ax.set_xlim(ll[0] + 0.05, ll[-1] - 0.05)
charts.style_axes(ax, r"$\log_{10}\lambda$", "standardized coefficient")
charts.title(ax, "A  Coefficient paths (27 candidates)")
ax.plot([], [], color=P.fill("neutral"), lw=0.8, label="smoking interactions")
ax.plot([], [], color=P.muted(), lw=0.8, ls="--", label="noise variables")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
ax = axs[1]
nz = (np.abs(B) > 0).sum(1)
ax.errorbar(ll, mcv, yerr=se, fmt="o", ms=3, color=charts.line("rna"), ecolor=P.muted(), elinewidth=0.6, capsize=1.5)
for i, lab in ((imin, "min"), (i1, "1se")):
    ax.axvline(ll[i], color=P.muted(), lw=0.7, ls=":")
    ax.text(ll[i], mcv.max() + 0.03, f"$\\lambda_{{\\mathrm{{{lab}}}}}$: {nz[i]} variables", rotation=90, fontsize=FT["tiny"],
            color=P.ink(), ha="right", va="top")
ax.invert_xaxis()
charts.style_axes(ax, r"$\log_{10}\lambda$", "cross-validated deviance")
charts.title(ax, "B  10-fold cross-validation")
ax.title.set_position((0, 1.12))
sec = ax.secondary_xaxis("top", functions=(lambda v: v, lambda v: v))
sec.set_xticks(ll[::7])
sec.set_xticklabels([str(v) for v in nz[::7]], fontsize=FT["tiny"], color=P.ink())
sec.tick_params(colors=P.muted())
sec.set_xlabel("nonzero coefficients", fontsize=FT["tiny"], color=P.ink())
