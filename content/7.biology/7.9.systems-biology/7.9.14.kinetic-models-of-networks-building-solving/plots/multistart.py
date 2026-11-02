"""Local minima in fitting an oscillation (simulation: 41 measurements over four periods of
y = 2 + sin(2 pi t + 0.5) plus Gaussian noise with standard deviation 0.2; the model is
y = c + a sin(omega t) + b cos(omega t), linear in c, a, b and nonlinear in the angular frequency omega).
A: the data, the global best fit (omega = 6.29) and the fit reached by Levenberg-Marquardt from the
start omega = 4, a local minimum that misses the oscillation. B: the residual sum of squares
minimized over c, a, b for each omega (the profile of omega): one deep global minimum near 2 pi and
six shallow local minima. Below, the frequencies reached by Levenberg-Marquardt from 200 starting
values of omega drawn uniformly between 0.5 and 15: each run ends in the minimum of its own basin
(13 drift to omega near 0 and 10 beyond 15), and 19.5 % reach the global one."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
t = np.linspace(0, 4, 41)
y = 2 + np.sin(2 * np.pi * t + 0.5) + rng.normal(0, 0.2, t.size)


def model(th, tt=t):
    c, a, b, om = th
    return c + a * np.sin(om * tt) + b * np.cos(om * tt)


def linear_part(om):
    X = np.c_[np.ones_like(t), np.sin(om * t), np.cos(om * t)]
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    return np.sum((X @ beta - y) ** 2), beta


def lm(om0):
    return least_squares(lambda th: model(th) - y, [*linear_part(om0)[1], om0], method="lm").x


oms = np.linspace(0.5, 15, 3000)
rss = np.array([linear_part(o)[0] for o in oms])
starts = rng.uniform(0.5, 15, 200)
ends = np.array([lm(o)[3] for o in starts])
glob, loc = lm(7.0), lm(4.0)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 3.5))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.86, wspace=0.3)
tt = np.linspace(0, 4, 400)
ax1.plot(t, y, "o", ms=3.5, color=P.ink())
ax1.plot(tt, model(glob, tt), color=charts.line("positive"), lw=1.6, label=f"global, omega = {glob[3]:.2f}")
ax1.plot(tt, model(loc, tt), color=charts.line("negative"), lw=1.6, label=f"local, omega = {loc[3]:.2f}")
ax1.legend(fontsize=7, frameon=False, loc="upper right", ncol=2)
ax1.set_ylim(0.3, 4.2)
charts.style_axes(ax1, "t", "y")
charts.title(ax1, "A  Data and two fits")
ax2.plot(oms, rss, color=P.ink(), lw=1.2)
ax2.plot(ends, np.full(ends.size, -2.5) + rng.uniform(-0.8, 0.8, ends.size), "|", ms=6,
         color=charts.line("highlight"), alpha=0.7)
ax2.text(15, -0.6, "ends of 200 local fits", fontsize=7, color=charts.line("highlight"), ha="right")
ax2.set_ylim(-4, 32)
charts.style_axes(ax2, "omega", "residual sum of squares")
charts.title(ax2, "B  Profile of omega and multistart")
