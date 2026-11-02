"""Bet hedging in an environment that is good with probability p and stressful with probability 1 - p,
independently in each period. A growing phenotype multiplies by 4 in a good period and by 0.02 in a
stressful one; a dormant phenotype by 1 and 0.8. Every cell gives a fraction q of its offspring the
growing phenotype, without sensing the environment.
A: long-term growth rate Lambda(q) = p ln(4q + 1 - q) + (1 - p) ln(0.02q + 0.8(1 - q)) for several p;
the maxima (dots) lie inside the interval for intermediate p.
B: optimal fraction q* against p (solid) with the Kelly limit q* = p (dotted) that holds when each
phenotype survives only in its own environment; outside 0.245 < p < 0.981 a pure strategy is best.
C: one random sequence of 60 periods with p = 0.8: log population size for q = 1 (all grow),
q = q* = 0.754 and q = 0 (all dormant)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
import wikibio as bio
from wikibio import charts

P = bio.P
a1, a2, b1, b2 = 4.0, 0.02, 1.0, 0.8


def lam(q, p):
    return p * np.log(q * a1 + (1 - q) * b1) + (1 - p) * np.log(q * a2 + (1 - q) * b2)


def qopt(p):
    r = minimize_scalar(lambda q: -lam(q, p), bounds=(0, 1), method="bounded", options={"xatol": 1e-6})
    cands = [0.0, r.x, 1.0]
    return max(cands, key=lambda q: lam(q, p))


fig, axs = plt.subplots(1, 3, figsize=(11, 3.4))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.86, wspace=0.36)

ax = axs[0]
q = np.linspace(0, 0.999, 400)
for p, tok in [(0.5, "negative"), (0.7, "highlight"), (0.8, "protein"), (0.9, "positive")]:
    ax.plot(q, lam(q, p), lw=1.4, color=charts.line(tok), label=f"p = {p:g}")
    qs = qopt(p)
    ax.plot([qs], [lam(qs, p)], "o", ms=4.5, color=charts.line(tok))
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_ylim(-1.0, 1.1)
ax.legend(fontsize=7, frameon=False, loc="lower left")
charts.style_axes(ax, "fraction q of growing offspring", r"$\Lambda(q)$ per period")
charts.title(ax, "A  Long-term growth rate")

ax = axs[1]
ps = np.linspace(0.01, 0.999, 300)
ax.plot(ps, [qopt(p) for p in ps], color=charts.line("protein"), lw=1.6, label="q* (this model)")
ax.plot(ps, ps, ":", color=P.ink(), lw=1.2, label="q* = p (Kelly)")
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "probability p of a good period", "optimal fraction q*")
charts.title(ax, "B  Optimal diversification")

ax = axs[2]
rng = np.random.default_rng(3)
good = rng.random(60) < 0.8
qs = qopt(0.8)
for qq, tok, lab in [(1.0, "negative", "q = 1"), (qs, "protein", f"q = {qs:.3f}"), (0.0, "neutral", "q = 0")]:
    w = np.where(good, qq * a1 + (1 - qq) * b1, qq * a2 + (1 - qq) * b2)
    ax.plot(np.arange(61), np.concatenate([[0], np.cumsum(np.log10(w))]), lw=1.4, color=charts.line(tok), label=lab)
for i in np.flatnonzero(~good):
    ax.axvspan(i, i + 1, color=P.fill("negative"), alpha=0.3, lw=0)
ax.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax, "period (shaded: stress)", "log10 population size")
charts.title(ax, "C  p = 0.8, one realization")
