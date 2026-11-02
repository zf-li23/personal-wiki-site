"""Noise-sustained oscillations of a two-component negative feedback loop (a p53-Mdm2-like circuit).

dx/dt = b/(1 + y^8) - x + noise,  dy/dt = x - y + noise  (x activates y, y represses x; b = 10; time in
units of the removal time). The fixed point (x* = y* = 1.27) is a stable spiral with eigenvalues
-1 +/- 2.64i: without noise, perturbations decay in damped oscillations. Euler-Maruyama simulation,
time step 0.002, independent white noise of intensity sigma on both variables, 3000 time units.
A: a deterministic perturbation (damped) and the stochastic trajectory (sigma = 0.1).
B: distributions of the peak heights above x* and of the intervals between peaks (peaks of the
0.2-smoothed trace with prominence above one standard deviation), each divided by its mean.
C: power spectral density of x (Welch) for sigma = 0.1 and 0.2, divided by sigma^2, and the spectrum of
the linearized system (line): the shape, and hence the period, does not depend on the noise strength.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.signal import find_peaks, welch
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
n, b = 8, 10.0
ys = brentq(lambda y: b / (1 + y ** n) - y, 0, 10)
g = n * ys ** n / (1 + ys ** n)
dt, T = 0.002, 3000.0
N = int(T / dt)
rng = np.random.default_rng(0)


def simulate(s):
    noise = rng.standard_normal((N, 2)) * s * np.sqrt(dt)
    x = np.empty(N)
    y = np.empty(N)
    x[0] = y[0] = ys
    for i in range(1, N):
        xi, yi = x[i - 1], y[i - 1]
        x[i] = max(xi + dt * (b / (1 + yi ** n) - xi) + noise[i, 0], 0.0)
        y[i] = max(yi + dt * (xi - yi) + noise[i, 1], 0.0)
    return x


runs = {s: simulate(s) for s in (0.1, 0.2)}
t = np.arange(N) * dt
fig, axes = plt.subplots(1, 3, figsize=(11, 3.5))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.16, top=0.86, wspace=0.32)
ax = axes[0]
det = solve_ivp(lambda tt, z: [b / (1 + z[1] ** n) - z[0], z[0] - z[1]], (0, 30), [ys + 0.6, ys], max_step=0.01)
ax.plot(t[t < 30], runs[0.1][t < 30], color=charts.line("protein"), lw=1.0, label="with noise")
ax.plot(det.t, det.y[0], color=P.ink(), lw=1.5, label="deterministic")
ax.axhline(ys, color=P.muted(), lw=0.7, ls=":")
ax.legend(fontsize=7, frameon=False, loc="upper right", ncol=2)
ax.set_ylim(0.6, 2.2)
charts.style_axes(ax, "time (1/alpha)", "x (p53-like)")
charts.title(ax, "A  Damped on paper, sustained in noise")

ax = axes[1]
x = runs[0.1]
w = int(0.2 / dt)
xs = np.convolve(x, np.ones(w) / w, "same")
pk, _ = find_peaks(xs, prominence=xs.std())
amp = xs[pk] - ys
per = np.diff(pk) * dt
bins = np.linspace(0, 3, 31)
ax.hist(amp / amp.mean(), bins=bins, color=charts.line("protein"), alpha=0.6,
        label=f"peak height, CV = {amp.std() / amp.mean():.2f}")
ax.hist(per / per.mean(), bins=bins, color=charts.line("enzyme"), alpha=0.6,
        label=f"interval, CV = {per.std() / per.mean():.2f}")
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "value / mean", "number of peaks")
charts.title(ax, "B  Amplitude varies more than period")

ax = axes[2]
for s, tok in [(0.1, "protein"), (0.2, "receptor")]:
    f, Pxx = welch(runs[s] - runs[s].mean(), fs=1 / dt, nperseg=2 ** 15)
    sel = f < 1.5
    ax.plot(f[sel], Pxx[sel] / s ** 2, color=charts.line(tok), lw=1.2, label=f"simulation, sigma = {s}")
om = 2 * np.pi * f[sel]
S = ((om ** 2 + 1) + g ** 2) / np.abs((1j * om + 1) ** 2 + g) ** 2
ax.plot(f[sel], 2 * S, color=P.ink(), lw=1.4, ls="--", label="linear theory")
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "frequency (1/time)", "PSD of x / sigma^2")
charts.title(ax, "C  The spectrum peaks at a fixed period")
