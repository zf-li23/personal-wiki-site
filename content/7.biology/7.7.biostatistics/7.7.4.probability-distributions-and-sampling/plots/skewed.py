"""Two right-skewed distributions of times. A: the log-normal distribution of the incubation period of
COVID-19 estimated by Lauer et al. (2020, Ann Intern Med; log-scale mean 1.621, SD 0.418): median 5.1 days,
97.5 % of cases have symptoms by day 11.5, and only 0.7 % after day 14. B: survival in the Veterans
Administration lung cancer trial (137 patients, 128 deaths; Kalbfleisch and Prentice; R package survival):
the Kaplan-Meier estimate (steps) against an exponential model (constant hazard, rate = deaths / total
follow-up time) and a Weibull model fitted by maximum likelihood; the Weibull shape below 1 says the
hazard falls with time.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from scipy import optimize, stats
from wikibio import charts
from wikibio import stats as wstats

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.5))
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.16, top=0.87, wspace=0.22)

ax = axs[0]
m, s = 1.621, 0.418
d = stats.lognorm(s, scale=np.exp(m))
x = np.linspace(0.01, 18, 500)
ax.plot(x, d.pdf(x), color=charts.line("rna"), lw=1.8)
ax.fill_between(x[x >= 14], d.pdf(x[x >= 14]), color=P.fill("rna"), alpha=0.6, lw=0)
for v, lab, ls in [(d.median(), f"median {d.median():.1f} d", "--"), (d.mean(), f"mean {d.mean():.1f} d", ":"),
                   (d.ppf(0.975), f"97.5 % by {d.ppf(0.975):.1f} d", "-.")]:
    ax.plot([v, v], [0, d.pdf(v)], color=P.muted(), lw=1.0, ls=ls)
    ax.text(v + 0.2, d.pdf(v) + (0.005 if ls != ":" else -0.03), lab, fontsize=FT["tiny"], color=P.ink())
ax.text(14.1, 0.03, f"after day 14:\n{100 * d.sf(14):.1f} %", fontsize=FT["tiny"], color=P.ink())
charts.style_axes(ax, "incubation period (days)", "density")
charts.title(ax, "A  Log-normal incubation period")

ax = axs[1]
rows = list(csv.DictReader(open("veteran.csv")))
t = np.array([float(r["time"]) for r in rows])
e = np.array([int(r["status"]) for r in rows])
km = wstats.kaplan_meier(t, e)
tt = np.concatenate([km.times, [t.max()]])
ss = np.concatenate([km.S, [km.S[-1]]])
ax.step(tt, ss, where="post", color=charts.line("dna"), lw=1.6, label=f"Kaplan-Meier (median {km.median:.0f} d)")
lam = e.sum() / t.sum()
g = np.linspace(0, 1000, 400)
ax.plot(g, np.exp(-lam * g), color=charts.line("enzyme"), lw=1.4, ls="--",
        label=f"exponential, rate {lam * 1000:.2f} per 1000 d (median {np.log(2) / lam:.0f} d)")


def nll(par):
    k, sc = np.exp(par)
    z = t / sc
    return -(np.sum(e * (np.log(k) - np.log(sc) + (k - 1) * np.log(z))) - np.sum(z ** k))


k, sc = np.exp(optimize.minimize(nll, [0.0, np.log(130.0)]).x)
ax.plot(g, np.exp(-(g / sc) ** k), color=charts.line("protein"), lw=1.4, ls=":",
        label=f"Weibull, shape {k:.2f} (median {sc * np.log(2) ** (1 / k):.0f} d)")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1.02)
charts.style_axes(ax, "days since randomization", "proportion surviving")
charts.title(ax, "B  Survival times in a lung cancer trial")
