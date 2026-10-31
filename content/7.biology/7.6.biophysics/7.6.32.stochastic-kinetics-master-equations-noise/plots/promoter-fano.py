"""The Fano factor as a fingerprint of promoter kinetics. A: simple repression, where a repressor
binding with rate k_on (proportional to its concentration) silences a promoter that otherwise makes
mRNA at r = 0.33 s^-1 (degradation gamma = 0.011 s^-1); the Fano factor against the fold change
FC = k_off/(k_off + k_on) for three operators of different strength (k_off = 1/(7 min), 1/(2.4 min),
1/(0.47 s)): lines from F = 1 + r FC(1 - FC)/(k_off + gamma FC), points from Gillespie simulations.
B: steady-state distributions of the two-state promoter (r/gamma = 20, mean fraction on 0.5) in
three regimes, simulated (bars) against the limiting forms: fast switching gives a Poisson
distribution, slow switching a zero-inflated Poisson, short bursts a negative binomial."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(2)


def telegraph(kp, km, r, g, tmax, burn=0.0):
    """Two-state promoter: off->on kp, on->off km, mRNA made at r when on, degraded at g each.
    Returns the time-weighted distribution of m."""
    t, s, m = 0.0, 1, 0
    w = np.zeros(400)
    while t < tmax:
        a = np.array([kp * (1 - s), km * s, r * s, g * m])
        a0 = a.sum()
        tau = rng.exponential(1 / a0)
        if t > burn:
            w[min(m, 399)] += tau
        t += tau
        j = np.searchsorted(np.cumsum(a), rng.random() * a0)
        if j == 0:
            s = 1
        elif j == 1:
            s = 0
        elif j == 2:
            m += 1
        else:
            m -= 1
    return w / w.sum()


def moments(w):
    n = np.arange(w.size)
    mu = (n * w).sum()
    return mu, ((n ** 2 * w).sum() - mu ** 2) / mu


fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.4), gridspec_kw=dict(width_ratios=(1, 1.5)))
fig.subplots_adjust(wspace=0.25, left=0.07, right=0.98, bottom=0.17, top=0.88)

ax = axs[0]
r, g = 0.33, 0.011
fc = np.linspace(0.005, 1, 300)
ops = [("Oid", 1 / 420, "highlight"), ("O1", 1 / 144, "protein"), ("O3", 1 / 0.47, "dna")]
for name, koff, tok in ops:
    ax.plot(fc, 1 + r * fc * (1 - fc) / (koff + g * fc), color=charts.line(tok), lw=1.6, label=name)
koff = 1 / 144
for f in (0.1, 0.3, 0.6):
    kon = koff * (1 - f) / f
    w = telegraph(koff, kon, r, g, 6e4, burn=2000)
    ax.plot(moments(w)[0] * g / r, moments(w)[1], "o", ms=4, color=charts.line("protein"))
ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), title="operator",
          title_fontsize=bio.core.FONT["tiny"])
charts.style_axes(ax, "fold change", "Fano factor")
charts.title(ax, "A  Simple repression")

ax = axs[1]
ax.axis("off")
regimes = [("fast switching", 50.0, 50.0, 1.0), ("slow switching", 0.02, 0.02, 1.0), ("bursts", 2.0, 2.0 * 19, 1.0)]
for i, (lab, kp, km, gg) in enumerate(regimes):
    sub = ax.inset_axes([0.04 + i * 0.345, 0.0, 0.27, 1.0])
    if lab == "bursts":
        rr = 20 * gg * (kp + km) / kp
    else:
        rr = 40.0
    w = telegraph(kp, km, rr, gg, 3000 if lab != "slow switching" else 60000, burn=20)
    n = np.arange(70)
    sub.bar(n, w[:70], width=0.9, color=P.fill("mrna"), edgecolor=P.edge("mrna"), lw=0.3)
    f_on = kp / (kp + km)
    if lab == "fast switching":
        model = stats.poisson.pmf(n, rr * f_on / gg)
        name = "Poisson"
    elif lab == "slow switching":
        model = f_on * stats.poisson.pmf(n, rr / gg)
        model[0] += 1 - f_on
        name = "zero-inflated Poisson"
    else:
        b = rr / km
        a = kp / gg
        model = stats.nbinom.pmf(n, a, 1 / (1 + b))
        name = "negative binomial"
    sub.plot(n, model, "o", ms=2.2, color=P.ink())
    mu, F = moments(w)
    sub.text(0.97, 0.97, f"{name}\nmean {mu:.1f}\nF = {F:.1f}", transform=sub.transAxes, ha="right", va="top",
             fontsize=bio.core.FONT["tiny"], color=P.ink())
    if lab == "slow switching":
        sub.set_ylim(0, 0.12)
        sub.annotate(f"P(0) = {w[0]:.2f}", (1, 0.118), (8, 0.06), fontsize=bio.core.FONT["tiny"], color=P.ink(),
                     arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
    charts.style_axes(sub, "m", "probability" if i == 0 else None)
    charts.title(sub, ("B  " if i == 0 else "") + lab)
