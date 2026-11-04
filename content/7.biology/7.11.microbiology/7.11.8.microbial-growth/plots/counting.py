# Measuring growth: viable counts, the most probable number and turbidity.
# A: serial tenfold dilution and spread plating of 0.1 mL from each tube (schematic). A sample with 1.6e8
#    CFU per mL gives on average 1600, 160 and 16 colonies on the 1e-4, 1e-5 and 1e-6 plates (colonies drawn
#    as a Poisson sample, seed 5). Only the plate in the countable range is used:
#    about 160 colonies / (0.1 mL x 1e-5) = 1.6e8 CFU per mL.
# B: the counting error of a plate. With randomly placed cells the colony count is Poisson, relative SE
#    1/sqrt(c); on crowded plates colonies merge (a colony of area a on a plate of area A hides a fraction
#    of others: observed = (A/a)(1 - exp(-c a / A)), with A/a = 3000, illustrative), so the observed count
#    underestimates. The total relative error (root sum of squares of the Poisson SE and the crowding bias)
#    is smallest in the conventional countable range of about 30 to 300 colonies.
# C: the most probable number (MPN) from a three-tube series with inocula of 0.1, 0.01 and 0.001 g of
#    sample and the result 3-2-0 positive tubes: the likelihood of the concentration c, a product of
#    binomial terms with P(positive) = 1 - exp(-c v), peaks at c = 93 per g, the tabulated MPN; the
#    interval where the log-likelihood is within 1.92 of its maximum is an approximate 95 % interval.
# D: turbidity. Optical density at 600 nm is proportional to the cell density only at low density
#    (Beer-Lambert regime); at higher densities multiple scattering makes the reading saturate, so a
#    standard curve is made against direct counts and dense cultures are diluted before measuring.
#    The calibration 1 OD unit = 8e8 cells per mL is a common rule of thumb for E. coli; it depends on the
#    instrument and on cell size.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from scipy.optimize import minimize_scalar

import wikibio as bio
from wikibio import charts
from wikibio import stats

P = bio.P
fig = plt.figure(figsize=(14.5, 4.4))
gs = fig.add_gridspec(1, 4, width_ratios=[1.5, 1.0, 1.0, 1.0], wspace=0.42)

# ---- A: dilution and plating ----------------------------------------------------------------------------
ax = fig.add_subplot(gs[0, 0])
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.set_aspect("equal")
ax.axis("off")
charts.title(ax, "A   Serial dilution and plate count")
tubes = stats.dilution_series(ax, (0.6, 4.6), n=6, token="bacterium", dx=1.9, w=0.6, h=1.6, factor="1:10")
for k, (x, y) in enumerate(tubes):
    bio.label(ax, (x, y - 0.35), f"10$^{{-{k + 1}}}$", size="tiny")
rng = np.random.default_rng(5)
mean = {3: 1600, 4: 160, 5: 16}
for k in (3, 4, 5):
    cx, cy = tubes[k][0], 2.0
    R = 0.85
    ax.add_patch(Circle((cx, cy), R, facecolor=P.mix(P.fill("cell_wall"), P.surface(), 0.75), edgecolor=P.muted(), lw=1.1))
    n = rng.poisson(mean[k])
    r = R * 0.92 * np.sqrt(rng.uniform(0, 1, n))
    th = rng.uniform(0, 2 * np.pi, n)
    size = 0.035 if n > 500 else 0.05
    for rr, tt in zip(r, th):
        ax.add_patch(Circle((cx + rr * np.cos(tt), cy + rr * np.sin(tt)), size, color=P.edge("bacterium"), lw=0))
    text = "too many\nto count" if n > 300 else f"{n}" if n >= 30 else f"{n}\n(too few)"
    bio.label(ax, (cx, cy - 1.35), text, size="tiny", color=P.ink() if 30 <= n <= 300 else P.muted(),
              bold=30 <= n <= 300)
    bio.arrow(ax, (cx, tubes[k][1] - 0.6), (cx, cy + R + 0.1), kind="process", lw=0.9, head=0.14, color=P.muted())
bio.label(ax, (2.2, 2.6), "spread 0.1 mL\non each plate", size="tiny", color=P.muted())
bio.label(ax, (2.2, 1.3), "CFU mL$^{-1}$ = colonies\n/ (volume × dilution)", size="tiny")

# ---- B: counting error ----------------------------------------------------------------------------------
ax = fig.add_subplot(gs[0, 1])
c = np.logspace(0.5, 3.6, 300)
Aa = 3000.0
obs = Aa * (1 - np.exp(-c / Aa))
bias = 1 - obs / c
se = 1 / np.sqrt(c)
tot = np.sqrt(se**2 + bias**2)
ax.axvspan(30, 300, color=P.mix(P.fill("positive"), P.surface(), 0.8 if not P.is_dark() else 0.88), lw=0)
ax.text(95, 0.3, "countable\nrange", ha="center", fontsize=6.8, color=charts.line("positive"))
ax.plot(c, se, color=charts.line("dna"), lw=1.6, ls="--", label="Poisson SE $1/\\sqrt{c}$")
ax.plot(c, bias, color=charts.line("negative"), lw=1.6, ls=":", label="crowding loss")
ax.plot(c, tot, color=P.ink(), lw=2.0, label="total relative error")
ax.set_xscale("log")
ax.set_ylim(0, 0.7)
ax.legend(fontsize=6.8, frameon=False, loc="upper right")
charts.style_axes(ax, "colonies on the plate $c$", "relative error")
charts.title(ax, "B   Which plate to count")

# ---- C: MPN -----------------------------------------------------------------------------------------------
ax = fig.add_subplot(gs[0, 2])
v = np.array([0.1, 0.01, 0.001])
pos = np.array([3, 2, 0])


def loglik(conc):
    m = np.outer(conc, v)
    return (pos * np.log(-np.expm1(-m)) - (3 - pos) * m).sum(axis=1)


cc = np.logspace(0.45, 3.3, 500)
ll = loglik(cc)
best = np.exp(minimize_scalar(lambda x: -loglik(np.array([np.exp(x)]))[0], bounds=(0, 9), method="bounded").x)
lmax = loglik(np.array([best]))[0]
ax.plot(cc, ll - lmax, color=charts.line("bacterium"), lw=2.0)
ax.axhline(-1.92, color=P.muted(), lw=0.8, ls="--")
inside = cc[ll - lmax > -1.92]
ax.axvspan(inside[0], inside[-1], color=P.mix(P.fill("highlight"), P.surface(), 0.8 if not P.is_dark() else 0.88), lw=0)
ax.axvline(best, color=P.ink(), lw=0.8)
ax.text(best * 1.18, -0.6, f"MPN = {best:.0f} g$^{{-1}}$", fontsize=7.2, color=P.ink())
ax.text(3.3, -2.05, "approx. 95 %\ninterval", fontsize=6.8, color=P.muted(), va="top")
ax.text(3.3, -5.4, "3 tubes each of\n0.1, 0.01, 0.001 g;\npositive: 3, 2, 0", fontsize=6.8, color=P.ink(), va="bottom")
ax.set_xscale("log")
ax.set_ylim(-6, 0.5)
charts.style_axes(ax, "concentration $c$ / g$^{-1}$", "log-likelihood (relative)")
charts.title(ax, "C   Most probable number")

# ---- D: turbidity ---------------------------------------------------------------------------------------------
ax = fig.add_subplot(gs[0, 3])
cells = np.linspace(0, 3e9, 300)
od_true = cells / 8e8
od_obs = od_true / (1 + (od_true / 1.6) ** 1.3) ** (1 / 1.3)
ax.plot(cells / 1e9, od_true, color=charts.line("neutral"), lw=1.3, ls="--", label="proportional (dilute)")
ax.plot(cells / 1e9, od_obs, color=charts.line("bacterium"), lw=2.0, label="measured")
cal = np.array([0.1, 0.2, 0.3, 0.4, 0.5]) * 8e8
ax.plot(cal / 1e9, cal / 8e8, "o", ms=4, color=charts.line("bacterium"))
ax.axvspan(0, 0.45, color=P.mix(P.fill("positive"), P.surface(), 0.8 if not P.is_dark() else 0.88), lw=0)
ax.text(0.05, 2.3, "linear\nrange", fontsize=6.8, color=charts.line("positive"))
ax.set_xlim(0, 3)
ax.set_ylim(0, 2.6)
ax.legend(fontsize=6.8, frameon=False, loc="lower right")
charts.style_axes(ax, "cells / (10$^9$ mL$^{-1}$)", "OD$_{600}$")
charts.title(ax, "D   Turbidity needs a standard curve")
