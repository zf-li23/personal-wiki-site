"""Convolution models of indirect measures of neural activity. A: a spike train (Poisson, 2 Hz,
with a burst) and the fluorescence of a calcium indicator modeled as a first-order (AR(1)) process,
c_t = gamma c_(t-1) + s_t with decay time constant 0.6 s, F = F0 (1 + a c) + noise, shown as
dF/F. B: nonnegative deconvolution recovers the spike train from dF/F (projected gradient descent
on the squared error with an L1 penalty, which is the convex problem solved by standard methods).
C: the canonical double-gamma hemodynamic response function (peak near 5 s, undershoot near 15 s).
D: a block design (20 s on, 20 s off) and two brief events; the predicted BOLD signal is the
neural activity convolved with the HRF, plus noise."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma as G
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(2)
fig, axs = plt.subplots(2, 2, figsize=(10.0, 5.4))
fig.subplots_adjust(hspace=0.55, wspace=0.28, left=0.08, right=0.98, bottom=0.1, top=0.93)

dt = 1 / 30.0  # 30 Hz imaging
T = 30.0
t = np.arange(0, T, dt)
s = rng.poisson(2.0 * dt, len(t)).astype(float)
s[(t > 12) & (t < 12.4)] += 1  # a burst
g = np.exp(-dt / 0.6)
c = np.zeros_like(t)
for k in range(1, len(t)):
    c[k] = g * c[k - 1] + s[k]
dff = 0.25 * c + rng.normal(0, 0.05, len(t))

ax = axs[0, 0]
ax.plot(t, dff, color=charts.line("ca"), lw=1.0, label="ΔF/F")
st = t[s > 0]
ax.vlines(st, -0.45, -0.25, color=P.ink(), lw=0.8)
ax.text(0.2, -0.2, "spikes", fontsize=FT["tiny"], color=P.ink(), va="bottom")
charts.style_axes(ax, "t / s", "ΔF/F")
charts.title(ax, "A  Spikes and calcium fluorescence")

# nonnegative deconvolution: minimize ||dff - a K s||^2 + lam*sum(s), s >= 0, K = AR(1) kernel
n = len(t)
kern = g ** np.arange(n)
def Kconv(v):
    return np.convolve(v, kern)[:n]
def Kt(v):
    return np.convolve(v[::-1], kern)[:n][::-1]
a = 0.25
est = np.zeros(n)
step = 1.0 / (a * a * (1 / (1 - g)) ** 2)
lam = 0.02
for it in range(1500):
    grad = -a * Kt(dff - a * Kconv(est)) + lam
    est = np.maximum(est - step * grad, 0)
ax = axs[0, 1]
ax.vlines(st, 0, s[s > 0], color=P.muted(), lw=2.2, label="true spikes")
ax.plot(t, est, color=charts.line("ca"), lw=1.0, label="deconvolved")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "t / s", "spikes per frame")
charts.title(ax, "B  Nonnegative deconvolution")

th = np.arange(0, 32, 0.1)
hrf = G.pdf(th, 6) - G.pdf(th, 16) / 6
hrf /= hrf.max()
ax = axs[1, 0]
ax.plot(th, hrf, color=charts.line("blood"), lw=1.7)
ax.axhline(0, color=P.muted(), lw=0.6)
charts.style_axes(ax, "time after a brief neural event / s", "HRF (normalized)")
charts.title(ax, "C  Hemodynamic response function")

dtb = 0.1
tb = np.arange(0, 160, dtb)
x = (((tb % 40) < 20) & (tb < 80)).astype(float)
x[(tb > 100) & (tb < 101)] = 1
x[(tb > 130) & (tb < 131)] = 1
y = np.convolve(x, hrf)[:len(tb)] * dtb / 5.0
TR = 2.0
tr = np.arange(0, 160, TR)
yobs = np.interp(tr, tb, y) + rng.normal(0, 0.05, len(tr))
ax = axs[1, 1]
ax.fill_between(tb, 0, x * 1.1, step="mid", color=P.mix(P.muted(), P.surface(), 0.8), lw=0, label="neural activity")
ax.plot(tb, y, color=charts.line("blood"), lw=1.6, label="predicted BOLD")
ax.plot(tr, yobs, "o", ms=2.5, color=charts.line("dna"), label="samples (TR = 2 s)")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
ax.set_ylim(-0.25, 1.5)
charts.style_axes(ax, "t / s", "signal (a.u.)")
charts.title(ax, "D  Block design and events")
