"""Calibration densities for node ages. A: four ways of turning fossil information into a prior on the
age t of a node (in Myr): a soft minimum bound (t > 50 Myr with 2.5 % of the probability below,
the rest in a heavy-tailed decline above), soft minimum and maximum bounds (flat between 50 and
70 Myr with 2.5 % in each tail), a gamma density whose 95 % interval is (50, 70), and a soft maximum
bound (t < 70 Myr, 2.5 % above). B: the effective prior. Independent gamma calibrations are specified
for a node (mean 60, sd 8) and its daughter node (mean 55, sd 8); because a node must be older than
its daughter, the program samples only from the region t1 > t2, and the marginal priors actually used
(lines; Monte Carlo, 200 000 draws) differ from the specified ones (dashed)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(2)
t = np.linspace(0.5, 110, 800)
tL, tU = 50.0, 70.0


def soft_min(t, s=10.0):
    right = 0.975 * 2 / (np.pi * s * (1 + ((t - tL) / s) ** 2))
    th = (0.975 * 2 / (np.pi * s)) * tL / 0.025
    left = 0.025 * th / tL * (t / tL) ** (th - 1)
    return np.where(t >= tL, right, left)


def soft_both(t):
    c = 0.95 / (tU - tL)
    th = c * tL / 0.025
    lam = c / 0.025
    return np.where(t < tL, 0.025 * th / tL * (t / tL) ** (th - 1),
                    np.where(t <= tU, c, c * np.exp(-lam * (t - tU))))


def soft_max(t):
    c = 0.975 / tU
    lam = c / 0.025
    return np.where(t <= tU, c, c * np.exp(-lam * (t - tU)))


from scipy.optimize import brentq
k = brentq(lambda a: stats.gamma.ppf(0.975, a, scale=60 / a) / stats.gamma.ppf(0.025, a, scale=60 / a) - tU / tL, 5, 2000)
sc = (tL + tU) / 2 / k
g = stats.gamma(k, scale=sc)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.9, wspace=0.25)
a.plot(t, soft_min(t), color=charts.line("dna"), lw=1.5, label="soft minimum ($t > 50$)")
a.plot(t, soft_both(t), color=charts.line("rna"), lw=1.5, label="soft minimum and maximum")
a.plot(t, g.pdf(t), color=charts.line("positive"), lw=1.5, label="gamma, 95 % in (50, 70)")
a.plot(t, soft_max(t), color=P.muted(), lw=1.3, ls="--", label="soft maximum ($t < 70$)")
for v in (tL, tU):
    a.axvline(v, color=P.muted(), lw=0.6, ls=":")
a.set_xlim(0, 110)
a.set_ylim(0, 0.09)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "node age $t$ (Myr)", "prior density")
charts.title(a, "A  Calibration densities")
n = 200000
g1 = stats.gamma(a=(60 / 8) ** 2, scale=8 ** 2 / 60)
g2 = stats.gamma(a=(55 / 8) ** 2, scale=8 ** 2 / 55)
t1, t2 = g1.rvs(n, random_state=rng), g2.rvs(n, random_state=rng)
ok = t1 > t2
x = np.linspace(25, 95, 300)
for dist, sample, tok, name in ((g1, t1[ok], "dna", "$t_1$ (node)"), (g2, t2[ok], "rna", "$t_2$ (daughter)")):
    b.plot(x, dist.pdf(x), color=charts.line(tok), lw=1.0, ls="--")
    kde = stats.gaussian_kde(sample[:20000])
    b.plot(x, kde(x), color=charts.line(tok), lw=1.8, label=f"{name}: effective")
b.plot([], [], color=P.muted(), ls="--", label="specified")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "node age (Myr)", "prior density")
charts.title(b, f"B  Truncation by $t_1 > t_2$ (kept {ok.mean():.0%} of draws)")
