"""Harvest strategies in a fluctuating environment (Section 53.2.4).

Annual surplus-production model, dimensionless stock x = N/K:
    x' = x + r x (1 - x / k_t) - H_t,  r = 0.5,
with a carrying capacity k_t that fluctuates (lognormal, mean 1, CV 0.3, lag-1 autocorrelation 0.5).
The deterministic MSY is rK/4 = 0.125 per year at x = 0.5 with harvest rate F_MSY = r/2.
Strategies: (1) fixed quota H = 0.9 MSY; (2) fixed effort H = F_MSY x; (3) a precautionary
harvest control rule: F = 0.8 F_MSY above x = 0.4, falling linearly to 0 at x = 0.1.
The harvest cannot exceed the stock available after production. 400 replicate runs of 100 years.
A: one run (same environment for all strategies); B: mean annual yield relative to the MSY and the
coefficient of variation of the yield among years; C: probability that the stock falls below 5% of K.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
cols = [C.line("negative"), C.line("dna"), C.line("positive")]
names = ["fixed quota\n0.9 MSY", "fixed effort\nF_MSY", "control rule\n0.8 F_MSY"]

r, T, R = 0.5, 100, 400
msy = r / 4
rng = np.random.default_rng(0)


def environment():
    z = np.zeros(T)
    for t in range(1, T):
        z[t] = 0.5 * z[t - 1] + np.sqrt(1 - 0.25) * rng.standard_normal()
    s = np.sqrt(np.log(1 + 0.3 ** 2))
    return np.exp(s * z - s * s / 2)


def run(k, strategy):
    x = np.empty(T + 1)
    y = np.zeros(T)
    x[0] = 0.5
    for t in range(T):
        avail = max(x[t] + r * x[t] * (1 - x[t] / k[t]), 0.0)
        if strategy == 0:
            h = 0.9 * msy
        elif strategy == 1:
            h = (r / 2) * x[t]
        else:
            f = 0.8 * r / 2 * np.clip((x[t] - 0.1) / 0.3, 0, 1)
            h = f * x[t]
        h = min(h, avail)
        y[t] = h
        x[t + 1] = avail - h
    return x, y


envs = [environment() for _ in range(R)]
res = [[run(k, s) for k in envs] for s in range(3)]

fig, axes = plt.subplots(1, 3, figsize=(13, 3.9), gridspec_kw={"width_ratios": [1.7, 1, 1]})
ax = axes[0]
pick = next(i for i in range(R) if res[0][i][0].min() < 0.02 and res[0][i][0].argmin() > 40)
for s in range(3):
    ax.plot(np.arange(T + 1), res[s][pick][0], color=cols[s], lw=1.8, label=names[s].replace("\n", " "))
ax.axhline(0.5, color=P.muted(), lw=0.6, ls=":")
ax.set_xlim(0, T)
ax.set_ylim(0, 1.25)
C.style_axes(ax, "year", "stock x = N / K")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right", ncol=3)
C.title(ax, "A  One environment, three strategies")

ax = axes[1]
pos = np.arange(3)
mean_y = [np.mean([y.mean() for _, y in res[s]]) / msy for s in range(3)]
cv_y = [np.mean([y.std() / max(y.mean(), 1e-9) for _, y in res[s]]) for s in range(3)]
w = 0.38
ax.bar(pos - w / 2, mean_y, w, color=[P.mix(c, P.surface(), 0.35) for c in cols], edgecolor=cols)
ax.bar(pos + w / 2, cv_y, w, color=P.surface(), edgecolor=cols, hatch="///")
for i in range(3):
    ax.text(pos[i] - w / 2, mean_y[i] + 0.02, f"{mean_y[i]:.2f}", ha="center", fontsize=FS["tiny"], color=P.ink())
    ax.text(pos[i] + w / 2, cv_y[i] + 0.02, f"{cv_y[i]:.2f}", ha="center", fontsize=FS["tiny"], color=P.ink())
ax.set_xticks(pos, names)
ax.set_ylim(0, 1.38)
C.style_axes(ax, None, "mean yield / MSY (solid); CV of yield (hatched)")
C.title(ax, "B  Yield and its variability")

ax = axes[2]
pc = [np.mean([x.min() < 0.05 for x, _ in res[s]]) for s in range(3)]
ax.bar(pos, pc, 0.6, color=[P.mix(c, P.surface(), 0.35) for c in cols], edgecolor=cols)
for i in range(3):
    ax.text(pos[i], pc[i] + 0.02, f"{pc[i]:.2f}", ha="center", fontsize=FS["tiny"], color=P.ink())
ax.set_xticks(pos, names)
ax.set_ylim(0, 1.05)
C.style_axes(ax, None, "P(stock < 0.05 K within 100 years)")
C.title(ax, "C  Risk of collapse")
fig.tight_layout()
