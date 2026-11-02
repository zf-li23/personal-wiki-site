"""Frequency tuning with and without positive feedback (after the argument of Tsai and colleagues, 2008).

Negative feedback only: a three-stage Goodwin loop, dx1/dt = 10/(1 + x3^12) - x1, dx2/dt = x1 - x2,
dx3/dt = g (x2 - x3); the frequency is changed through the rate g of the last stage.
Positive plus negative feedback: the activator-repressor relaxation oscillator of 7.6.33,
dA/dt = (100 + 5000 A^2)/(1 + A^2 + R^2) - 30 A, dR/dt = e (120 A^2/(1 + A^2) - R); the frequency is
changed through the rate e of the repressor.
A: time courses (each normalized to its own maximum) for two values of the tuning parameter of each.
B: peak-to-trough amplitude (relative to the largest) against frequency (relative to the lowest) as the
tuning parameter is scanned; the Goodwin loop oscillates only for g between about 0.32 and 3.3, and its amplitude
falls to zero at both ends (Hopf bifurcations), whereas the relaxation oscillator is tuned over two decades
of frequency with nearly constant amplitude.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks
import wikibio as bio
from wikibio import charts

P = bio.P


def goodwin(g):
    return lambda t, z: [10 / (1 + z[2] ** 12) - z[0], z[0] - z[1], g * (z[1] - z[2])]


def relax(e):
    return lambda t, z: [(100 + 5000 * z[0] ** 2) / (1 + z[0] ** 2 + z[1] ** 2) - 30 * z[0],
                         e * (120 * z[0] ** 2 / (1 + z[0] ** 2) - z[1])]


def measure(f, z0, T, tr, var):
    s = solve_ivp(f, (0, T), z0, method="LSODA", rtol=1e-7, atol=1e-9, dense_output=True)
    t = np.linspace(tr, T, 20000)
    x = s.sol(t)[var]
    amp = x.max() - x.min()
    pk, _ = find_peaks(x, prominence=0.05 * max(amp, 1e-12))
    if len(pk) < 3 or amp < 1e-3 * abs(x).max():
        return np.nan, 0.0
    return np.mean(np.diff(t[pk])), amp


gs = np.concatenate([np.linspace(0.32, 0.5, 4), np.linspace(0.7, 3.3, 9)])
G = np.array([measure(goodwin(g), [0.5, 0.5, 0.5], 200 / min(g, 1), 120 / min(g, 1), 2) for g in gs])
es = np.logspace(np.log10(0.02), np.log10(3), 9)
Rx = np.array([measure(relax(e), [1, 1], 150 / e, 90 / e, 0) for e in es])

fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.86, wspace=0.27)
ax = axes[0]
for f, z0, var, par, tok, ls, lab, scale in [
        (goodwin(0.7), [0.5, 0.5, 0.5], 2, 0.7, "protein", "-", "negative only, g = 0.7", 1.0),
        (goodwin(2.5), [0.5, 0.5, 0.5], 2, 2.5, "protein", "--", "negative only, g = 2.5", 1.0),
        (relax(1.0), [1, 1], 0, 1.0, "positive", "-", "positive + negative, e = 1", 1.0),
        (relax(0.3), [1, 1], 0, 0.3, "positive", "--", "positive + negative, e = 0.3", 1.0)]:
    s = solve_ivp(f, (0, 140), z0, method="LSODA", rtol=1e-8, atol=1e-10, dense_output=True)
    t = np.linspace(110, 140, 3000)
    x = s.sol(t)[var]
    off = 1.25 if "positive" in tok else 0.0
    ax.plot(t - 110, x / x.max() + off, color=charts.line(tok), lw=1.4, ls=ls, label=lab)
ax.set_ylim(0, 2.9)
ax.set_yticks([])
ax.legend(fontsize=6.5, frameon=False, loc="upper center", ncol=2)
charts.style_axes(ax, "time", "level (normalized, offset)")
charts.title(ax, "A  Two oscillators at two settings")

ax = axes[1]
ok = ~np.isnan(G[:, 0])
fmin = min(np.nanmin(1 / G[:, 0]), np.nanmin(1 / Rx[:, 0]))
ax.semilogx(1 / G[ok, 0] / fmin, G[ok, 1] / G[ok, 1].max(), "o-", color=charts.line("protein"), lw=1.4, ms=3.5,
            label="negative feedback only")
ok2 = ~np.isnan(Rx[:, 0])
ax.semilogx(1 / Rx[ok2, 0] / fmin, Rx[ok2, 1] / Rx[ok2, 1].max(), "s-", color=charts.line("positive"), lw=1.4,
            ms=3.5, label="positive + negative feedback")
ax.set_ylim(0, 1.15)
ax.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax, "frequency (relative to the lowest)", "amplitude (relative)")
charts.title(ax, "B  Tunable frequency at constant amplitude")
