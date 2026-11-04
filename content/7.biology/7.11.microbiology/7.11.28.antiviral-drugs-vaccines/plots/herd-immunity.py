# Herd immunity.
# A: the critical immune fraction 1 - 1/R0 with the ranges estimated for several pathogens.
# B: an SIR epidemic (dS/dt = -beta S I, dI/dt = beta S I - gamma I) started in a population with a
#    fraction p already immune, for several values of p around the threshold of a virus with R0 = 5.
# C: clustering. The same mean coverage distributed unevenly over communities (a beta distribution
#    with the same mean and increasing variance) leaves a growing fraction of communities below the
#    threshold, where the local reproduction number exceeds one.
import numpy as np
from scipy.integrate import solve_ivp
from scipy.stats import beta as beta_dist

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(17.6, 7.4)

# --- A  the threshold -------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 7.2))
bio.label(ax, (3.4, 7.05), "Critical immune fraction", size="title", bold=True)

R = np.linspace(1.02, 20, 400)
pl = quant.Plot(ax, (1.9, 2.15, 4.0, 4.2), xlim=(0, 20), ylim=(0, 1.0),
                xlabel="basic reproduction number $R_0$", ylabel="immune fraction needed, $1 - 1/R_0$",
                xticks=[0, 5, 10, 15, 20], yticks=[0, 0.5, 1])
pl.line(R, 1 - 1 / R, "virus", lw=2.0)
DIS = [("seasonal influenza", 1.3, 1.8, -0.09), ("SARS-CoV-2 (ancestral)", 2.0, 3.0, 0.07),
       ("smallpox", 5.0, 7.0, -0.13), ("polio", 5.0, 7.0, 0.07),
       ("measles", 12.0, 18.0, 0.05), ("pertussis", 12.0, 17.0, -0.10)]
for name, lo, hi, dy in DIS:
    mid = 0.5 * (lo + hi)
    pl.points(np.array([mid]), np.array([1 - 1 / mid]), "negative", r=0.075)
    pl.text(mid + 0.4, 1 - 1 / mid + dy, name, size="tiny", ha="left", color=P.muted())
bio.label(ax, (3.4, 0.6), "measles needs 92–95 % immunity;\n$R_0 = 3$ needs about two thirds", size="tiny", color=P.muted())

# --- B  epidemics at several coverages ---------------------------------------------------------------
bio.panel(ax, "B", (6.2, 7.2))
bio.label(ax, (9.9, 7.05), "Four levels of coverage", size="title", bold=True)

R0, GAMMA = 5.0, 0.2            # per day; beta = R0 * gamma
BETA = R0 * GAMMA


def sir(t, y):
    S, I, _ = y
    return [-BETA * S * I, BETA * S * I - GAMMA * I, GAMMA * I]


t_eval = np.linspace(0, 180, 900)
pl2 = quant.Plot(ax, (7.5, 2.15, 4.3, 4.2), xlim=(0, 180), ylim=(0, 0.26),
                 xlabel="days", ylabel="fraction of the population infectious",
                 xticks=[0, 60, 120, 180], yticks=[0, 0.1, 0.2])
for p, tok, tx, ty in ((0.0, "negative", 22, 0.245), (0.5, "virus", 40, 0.135),
                       (0.7, "enzyme", 78, 0.045), (0.82, "bacterium", 120, 0.015)):
    sol = solve_ivp(sir, (0, 180), [1 - p - 1e-4, 1e-4, p], t_eval=t_eval, rtol=1e-9, atol=1e-12)
    pl2.line(sol.t, sol.y[1], tok)
    pl2.text(tx, ty, "%d %% immune" % round(p * 100), size="tiny", color=quant.line_color(tok))
pl2.text(96, 0.215, "threshold $p_{\\mathrm{c}} = 1 - 1/5 = 0.8$", size="tiny")
bio.label(ax, (9.7, 0.6), "below the threshold the epidemic is smaller but still occurs;\n"
                          "above it, an introduction does not spread", size="tiny", color=P.muted())

# --- C  clustering ------------------------------------------------------------------------------------
bio.panel(ax, "C", (12.3, 7.2))
bio.label(ax, (15.5, 7.05), "Why clustering matters", size="title", bold=True)

MEAN = 0.88
kappa = np.linspace(2.0, 200.0, 300)          # concentration: large = uniform coverage
frac_below = np.array([1 - beta_dist.cdf(1 - 1 / R0, MEAN * k, (1 - MEAN) * k) for k in kappa])
frac_below = 1 - frac_below                   # fraction of communities below the threshold
sd = np.sqrt(MEAN * (1 - MEAN) / (kappa + 1))
pl3 = quant.Plot(ax, (13.8, 2.15, 3.1, 4.2), xlim=(0, 0.16), ylim=(0, 0.6),
                 xlabel="s.d. of coverage between communities",
                 ylabel="fraction of communities below $p_{\\mathrm{c}}$",
                 xticks=[0, 0.05, 0.10, 0.15], yticks=[0, 0.2, 0.4, 0.6])
pl3.line(sd, frac_below, "virus", lw=2.0)
pl3.text(0.085, 0.12, "mean coverage 88 %,\nthreshold 80 %", size="tiny")
bio.label(ax, (15.3, 0.6), "unevenly distributed coverage leaves pockets\n"
                           "in which the local $R$ exceeds one", size="tiny", color=P.muted())
