"""The linear noise approximation for an autoregulated gene, a one-dimensional birth-death process
with production f(n) and degradation gamma n (gamma = 1). The exact stationary distribution of such
a chain is P(n) ~ prod_{i=1}^{n} f(i - 1)/(gamma i). A: Fano factor against the feedback gain
H = -f'(x*)/gamma at the deterministic steady state x*: exact values (points) for negative
autoregulation f = beta/(1 + (n/20)^4) (H > 0) and positive autoregulation
f = 2 + beta1 n/(40 + n) (H < 0), and the LNA prediction F = 1/(1 + H) (line).
B: exact distributions for strong negative feedback (H = 3.9) and for positive feedback close to
the marginal gain H = -1 (H = -0.6) against Poisson distributions with the same means (lines)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
N = 3000
n = np.arange(N)


def exact(f):
    logp = np.concatenate([[0.0], np.cumsum(np.log(f(n[:-1])) - np.log(n[1:]))])
    p = np.exp(logp - logp.max())
    p /= p.sum()
    mu = (n * p).sum()
    return p, mu, ((n ** 2 * p).sum() - mu ** 2) / mu


def gain(f, lo, hi):
    xs = brentq(lambda x: f(x) - x, lo, hi)
    h = 1e-4 * max(xs, 1)
    return xs, -(f(xs + h) - f(xs - h)) / (2 * h)


fig, axs = plt.subplots(1, 2, figsize=(9.0, 3.4))
fig.subplots_adjust(wspace=0.28, left=0.08, right=0.98, bottom=0.17, top=0.88)
ax = axs[0]
Hs, Fs = [], []
for beta in np.logspace(1.0, 3.6, 14):
    f = lambda x, b=beta: b / (1 + (x / 20.0) ** 4)
    xs, H = gain(f, 0.1, beta)
    Hs.append(H)
    Fs.append(exact(f)[2])
ax.plot(Hs, Fs, "o", ms=4, color=charts.line("protein"), label="exact, negative feedback")
Hp, Fp = [], []
for b1 in np.linspace(0, 38.5, 14):
    f = lambda x, b=b1: 2 + b * x / (40.0 + x)
    xs, H = gain(f, 0.1, 2000)
    Hp.append(H)
    Fp.append(exact(f)[2])
ax.plot(Hp, Fp, "s", ms=4, color=charts.line("blood"), label="exact, positive feedback")
hh = np.linspace(-0.95, 4.2, 300)
ax.plot(hh, 1 / (1 + hh), color=P.ink(), lw=1.2, label="LNA: 1/(1 + H)")
ax.axhline(1, color=P.muted(), lw=0.6, ls=":")
ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, r"feedback gain $H = -f'(x^*)/\gamma$", "Fano factor")
charts.title(ax, "A  Feedback shapes the noise")

ax = axs[1]
f1 = lambda x: 2000 / (1 + (x / 20.0) ** 4)
p1, m1, F1 = exact(f1)
f2 = lambda x: 2 + 37 * x / (40.0 + x)
p2, m2, F2 = exact(f2)
H1 = gain(f1, 0.1, 2000)[1]
H2 = gain(f2, 0.1, 2000)[1]
ax.bar(n[:90], p1[:90], width=1.0, color=P.fill("protein"), lw=0, label=f"negative, H = {H1:.1f}, F = {F1:.2f}")
ax.bar(n[:90], p2[:90], width=1.0, color=P.fill("blood"), lw=0, alpha=0.7, label=f"positive, H = {H2:.1f}, F = {F2:.1f}")
ax.plot(n[:90], stats.poisson.pmf(n[:90], m1), color=charts.line("protein"), lw=1.0)
ax.plot(n[:90], stats.poisson.pmf(n[:90], m2), color=charts.line("blood"), lw=1.0)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, "n", "probability")
charts.title(ax, "B  Sub- and super-Poissonian")
