"""Detecting density dependence by regressing growth rate on log abundance, and its pitfalls.

All series are simulated (30 years, log abundance X = ln N, process noise u ~ N(0, 0.2^2)).
A: a regulated population (Gompertz model X_{t+1} = X_t + beta0 + beta1 X_t + u_t, beta1 = -0.3,
equilibrium ln N = 4); the regression of r_t = X_{t+1} - X_t on X_t recovers a negative slope.
B: a random walk (beta1 = 0, no regulation) observed with sampling error (counts with log-scale error
SD 0.3): the regression of the observed growth rate on observed log abundance still has a clearly negative
slope, because an overestimate of X_t produces both a high x-value and a low growth rate.
C: sampling distributions of the estimated slope over 2000 replicate series for three cases: random walk
without observation error (the estimate is biased below 0 even then, the small-sample bias known from unit-root tests), the same random walk
with observation error, and the regulated population.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(3)
n = 30


def series(beta1, obs_sd=0.0, sd=0.2, x0=4.0):
    x = np.empty(n)
    x[0] = x0
    for t in range(n - 1):
        x[t + 1] = x[t] + beta1 * (x[t] - 4.0) + rng.normal(0, sd)
    return x + rng.normal(0, obs_sd, n) if obs_sd else x


def slope(x):
    r = np.diff(x)
    b = np.polyfit(x[:-1], r, 1)
    return b


fig, ax = bio.canvas(30.0, 10.0)
for k, (b1, obs, tok, title) in enumerate([(-0.3, 0.0, "enzyme", "Regulated population"),
                                           (0.0, 0.3, "negative", "Random walk + sampling error")]):
    x = series(b1, obs)
    b = slope(x)
    x0 = 2.0 + 10.0 * k
    pa = C.axes_at(ax, (x0, 1.6, 7.0, 6.8))
    pa.plot(x[:-1], np.diff(x), "o", ms=3.4, color=Q.line_color(tok))
    xx = np.linspace(x.min(), x.max(), 10)
    pa.plot(xx, np.polyval(b, xx), color=P.ink(), lw=1.0)
    pa.axhline(0, color=P.muted(), lw=0.6)
    pa.text(0.97, 0.95, f"slope = {b[0]:.2f}", transform=pa.transAxes, ha="right", va="top",
            fontsize=FS["tiny"], color=P.ink())
    C.style_axes(pa, "ln N_t (observed)", "r_t = ln(N_t+1 / N_t)")
    bio.panel(ax, "AB"[k], (x0 - 1.6, 9.6))
    bio.label(ax, (x0, 9.2), title, size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.5, 1.6, 7.0, 6.8))
bins = np.linspace(-1.6, 0.6, 45)
for b1, obs, tok, lab in [(0.0, 0.0, "dna", "random walk"), (0.0, 0.3, "negative", "random walk + error"),
                          (-0.3, 0.0, "enzyme", "regulated (beta1 = -0.3)")]:
    est = np.array([slope(series(b1, obs))[0] for _ in range(2000)])
    pc.hist(est, bins=bins, histtype="step", lw=1.4, color=Q.line_color(tok), label=lab)
pc.axvline(0, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
C.style_axes(pc, "estimated slope", "replicate series")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "C", (21.0, 9.6))
bio.label(ax, (22.5, 9.2), "Sampling distributions", size="small", bold=True, ha="left")
