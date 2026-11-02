"""Checking proportional hazards for the Karnofsky score in the veteran trial (137 patients, 128 deaths;
Kalbfleisch and Prentice; R package survival).

A: scaled Schoenfeld residuals of the Karnofsky score from a Cox model with treatment, Karnofsky score and
cell type (Breslow ties), one point per death, against days on a log axis, with a running mean of
25 deaths; the dashed line is the time-constant coefficient. The coefficient is strongly negative early
and drifts towards zero after about 100 days. B: log(-log S) of Kaplan-Meier estimates against log time
in three Karnofsky groups; under proportional hazards the curves would be parallel.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts, stats

P = bio.P
FT = bio.core.FONT
rows = list(csv.DictReader(open("veteran.csv")))
time = np.array([float(r["time"]) for r in rows])
event = np.array([int(r["status"]) for r in rows])
karno = np.array([float(r["karno"]) for r in rows])
cell = np.array([r["celltype"] for r in rows])
X = np.column_stack([np.array([int(r["trt"]) for r in rows]) - 1.0, karno,
                     cell == "smallcell", cell == "adeno", cell == "large"]).astype(float)
p = X.shape[1]
deaths = np.unique(time[event == 1])


def score_info(b):
    U, I = np.zeros(p), np.zeros((p, p))
    w = np.exp(X @ b)
    for t in deaths:
        r = time >= t
        d = (time == t) & (event == 1)
        W = w[r].sum()
        m = (w[r, None] * X[r]).sum(0) / W
        M2 = (w[r, None, None] * X[r, :, None] * X[r, None, :]).sum(0) / W
        U += X[d].sum(0) - d.sum() * m
        I += d.sum() * (M2 - np.outer(m, m))
    return U, I


b = np.zeros(p)
for _ in range(30):
    U, I = score_info(b)
    step = np.linalg.solve(I, U)
    b += step
    if np.abs(step).max() < 1e-10:
        break
V = np.linalg.inv(score_info(b)[1])
w = np.exp(X @ b)
tt, res = [], []
for i in np.flatnonzero(event == 1):
    r = time >= time[i]
    m = (w[r, None] * X[r]).sum(0) / w[r].sum()
    tt.append(time[i])
    res.append(X[i] - m)
tt, res = np.array(tt), np.array(res)
order = np.argsort(tt, kind="stable")
tt, res = tt[order], res[order]
scaled = b + len(tt) * res @ V
k = 1  # karnofsky column

fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.87, wspace=0.28)
ax = axs[0]
ax.plot(tt, scaled[:, k], "o", ms=3, color=P.fill("neutral"), mec=charts.line("neutral"), mew=0.5)
win = 25
sm = np.convolve(scaled[:, k], np.ones(win) / win, mode="valid")
ax.plot(tt[win // 2: win // 2 + len(sm)], sm, color=charts.line("rna"), lw=2, label="running mean (25 deaths)")
ax.axhline(b[k], color=charts.line("dna"), ls="--", lw=1.2, label=f"Cox coefficient {b[k]:.4f}")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_xscale("log")
ax.set_ylim(-0.25, 0.25)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "days (log scale)", "scaled Schoenfeld residual, Karnofsky")
charts.title(ax, "A  Time-varying coefficient of the Karnofsky score")
ax = axs[1]
for lo, hi, tok in [(0, 50, "rna"), (50, 70, "protein"), (70, 101, "dna")]:
    m = (karno >= lo) & (karno < hi)
    km = stats.kaplan_meier(time[m], event[m])
    keep = (km.S > 0) & (km.S < 1)
    lab = f"score {lo}-{hi - 1} (n = {m.sum()})" if hi < 101 else f"score {lo}-99 (n = {m.sum()})"
    ax.step(np.log(km.times[keep]), np.log(-np.log(km.S[keep])), where="post", color=charts.line(tok), lw=1.6,
            label=lab)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "log(days)", "log(-log S(t))")
charts.title(ax, "B  Log-log Kaplan-Meier curves by Karnofsky score")
