"""Group-sequential boundaries for five equally spaced analyses, two-sided overall alpha = 0.05, computed by
numerical integration of the joint distribution of the interim z statistics (Armitage-McPherson-Rowe
recursion on a grid).

A: critical values |z| of the Pocock design (constant), the O'Brien-Fleming design (c / sqrt(t)) and the
Lan-DeMets spending function of O'Brien-Fleming type, together with the unadjusted 1.96; repeated testing
at 1.96 at all five looks has an overall type I error of about 0.14. B: cumulative type I error spent by
each design against the information fraction.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import optimize, stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
x = np.linspace(-9, 9, 1101)
dx = x[1] - x[0]


def crossing(b, t):
    """Probability of first crossing |Z_k| >= b_k at each look under H0 (Brownian motion scale)."""
    out, dens, xin, tprev = [], None, None, 0.0
    for k in range(len(t)):
        sd = np.sqrt(t[k] - tprev)
        f = stats.norm.pdf(x, 0, sd) if dens is None else (stats.norm.pdf(x[:, None] - xin[None, :], 0, sd) * dens).sum(1) * dx
        lim = b[k] * np.sqrt(t[k])
        out.append(f[np.abs(x) >= lim].sum() * dx)
        keep = np.abs(x) < lim
        xin, dens, tprev = x[keep], f[keep], t[k]
    return np.array(out)


K = 5
t = np.arange(1, K + 1) / K
c_poc = optimize.brentq(lambda c: crossing([c] * K, t).sum() - 0.05, 2, 3, xtol=1e-4)
c_obf = optimize.brentq(lambda c: crossing(c / np.sqrt(t), t).sum() - 0.05, 1.8, 2.5, xtol=1e-4)
spend = 2 - 2 * stats.norm.cdf(stats.norm.isf(0.025) / np.sqrt(t))
inc = np.diff(np.r_[0, spend])
b_ld = []
for k in range(K):
    b_ld.append(optimize.brentq(lambda c: crossing(b_ld + [c], t[:k + 1])[-1] - inc[k], 1.0, 8.0, xtol=1e-4))
designs = [("Pocock", [c_poc] * K, "dna"), ("O'Brien-Fleming", list(c_obf / np.sqrt(t)), "rna"),
           ("Lan-DeMets (OBF-type spending)", b_ld, "plant")]
naive = crossing([1.959964] * K, t).sum()

fig, axs = plt.subplots(1, 2, figsize=(10, 3.7))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.87, wspace=0.25)
ax = axs[0]
for name, b, tok in designs:
    ax.plot(t, b, "-o", ms=4, color=charts.line(tok), lw=1.5, label=name)
    ax.plot(t, -np.array(b), "-o", ms=4, color=charts.line(tok), lw=1.5)
ax.axhline(1.96, color=P.muted(), ls="--", lw=0.9)
ax.axhline(-1.96, color=P.muted(), ls="--", lw=0.9)
ax.text(0.6, 1.4, f"unadjusted 1.96 at every look: overall alpha {naive:.2f}", ha="center", fontsize=FT["tiny"], color=P.muted())
ax.fill_between([0.15, 1.05], -1.96, 1.96, color=P.fill("neutral"), alpha=0.15, lw=0)
ax.set_xlim(0.15, 1.05)
ax.set_ylim(-5, 5)
ax.text(0.6, 4.6, "stop: benefit", ha="center", fontsize=FT["tiny"], color=P.ink())
ax.text(0.6, -4.8, "stop: harm", ha="center", fontsize=FT["tiny"], color=P.ink())
charts.style_axes(ax, "information fraction t (events so far / planned)", "critical value of z")
charts.title(ax, "A  Stopping boundaries, 5 analyses")
ax = axs[1]
for name, b, tok in designs:
    ax.plot(np.r_[0, t], np.r_[0, np.cumsum(crossing(b, t))], "-o", ms=4, color=charts.line(tok), lw=1.5, label=name)
ax.plot(np.r_[0, t], np.r_[0, np.cumsum(crossing([1.959964] * K, t))], "--", color=P.muted(), lw=1, label="unadjusted")
ax.axhline(0.05, color=P.ink(), lw=0.7, ls=":")
ax.set_xlim(0, 1.02)
ax.set_ylim(0, 0.15)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "information fraction t", "cumulative type I error")
charts.title(ax, "B  Alpha spent")
