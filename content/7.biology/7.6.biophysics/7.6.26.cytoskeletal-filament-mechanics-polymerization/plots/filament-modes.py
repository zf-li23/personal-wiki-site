"""Flexural rigidity from thermal shapes: the Fourier-mode analysis of Formula 26.1.2.

Two-dimensional filaments with free ends are simulated as chains of 1000 segments whose tangent angle
makes independent Gaussian steps of variance ds/lp (the exact discretization of the bending energy).
Images are mimicked by sampling the contour every 0.5 um and adding 20 nm of localization noise to each
point; the tangent angle theta(s) is recomputed from the noisy points and projected on cos(n pi s/L).
A: five simulated actin filaments (L = 10 um, lp = 17 um). B: mode variances from 400 contours for
actin and for microtubules (L = 20 um, lp = 5 mm): points from the noisy images, lines the theory
L^2/(lp n^2 pi^2), dotted the noise floor estimated from straight rods. C: persistence length estimated
from each mode, lp,n = L^2/(n^2 pi^2 <a_n^2>), relative to the true value; only modes above the noise
floor give the right answer."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(1)
NSEG, DSAMP, SIG = 1000, 0.5, 0.02  # segments, sampling (um), noise (um)
NMODE = 12


def contours(M, L, lp):
    ds = L / NSEG
    dth = rng.normal(0.0, np.sqrt(ds / lp), size=(M, NSEG - 1))
    th = np.concatenate([np.zeros((M, 1)), np.cumsum(dth, axis=1)], axis=1)
    th += rng.uniform(0, 2 * np.pi, size=(M, 1))
    x = np.concatenate([np.zeros((M, 1)), np.cumsum(ds * np.cos(th), axis=1)], axis=1)
    y = np.concatenate([np.zeros((M, 1)), np.cumsum(ds * np.sin(th), axis=1)], axis=1)
    return x, y


def modes(x, y, L):
    k = int(round(DSAMP / (L / NSEG)))
    xs = x[:, ::k] + rng.normal(0, SIG, size=x[:, ::k].shape)
    ys = y[:, ::k] + rng.normal(0, SIG, size=y[:, ::k].shape)
    dx, dy = np.diff(xs, axis=1), np.diff(ys, axis=1)
    th = np.unwrap(np.arctan2(dy, dx), axis=1)
    seg = np.hypot(dx, dy)
    s = np.cumsum(seg, axis=1) - seg / 2
    Lm = seg.sum(axis=1, keepdims=True)
    n = np.arange(1, NMODE + 1)
    a = np.array([np.sqrt(2 / Lm[:, 0]) * np.sum(th * np.cos(m * np.pi * s / Lm) * seg, axis=1) for m in n])
    return n, a.var(axis=1)


fig, axs = plt.subplots(1, 3, figsize=(10.6, 3.4))
fig.subplots_adjust(wspace=0.36, left=0.06, right=0.98, bottom=0.17, top=0.86)

ax = axs[0]
x, y = contours(5, 10.0, 17.0)
for i in range(5):
    xx, yy = x[i] - x[i].mean(), y[i] - y[i].mean()
    ang = np.arctan2(yy[-1] - yy[0], xx[-1] - xx[0])
    c, s = np.cos(-ang), np.sin(-ang)
    ax.plot(c * xx - s * yy, s * xx + c * yy + 1.2 * i, color=charts.line("actin"), lw=1.3)
ax.set_aspect("equal")
ax.set_xlim(-5.5, 5.5)
bio.scale_bar(ax, (-5, -1.2), 2.0, "2 µm")
ax.axis("off")
charts.title(ax, "A  Thermal shapes of actin")

ax2, ax3 = axs[1], axs[2]
for L, lp, tok, nm in ((10.0, 17.0, "actin", "actin, L = 10 µm"), (20.0, 5000.0, "channel", "microtubule, L = 20 µm")):
    x, y = contours(400, L, lp)
    n, var = modes(x, y, L)
    xr, yr = contours(400, L, 1e9)
    _, noise = modes(xr, yr, L)
    th = L ** 2 / (lp * n ** 2 * np.pi ** 2)
    ax2.plot(n, var, "o", color=charts.line(tok), ms=3.5, label=nm)
    ax2.plot(n, th, color=charts.line(tok), lw=1.1)
    ax2.plot(n, noise, ":", color=charts.line(tok), lw=1.0)
    ax3.plot(n, L ** 2 / (n ** 2 * np.pi ** 2 * var) / lp, "o-", color=charts.line(tok), ms=3.5, lw=1.0, label=nm)
ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax2, "mode number n", r"$\langle a_n^2\rangle$ / µm")
charts.title(ax2, "B  Mode variances")
ax3.axhline(1, color=P.muted(), lw=0.7, ls=":")
ax3.set_xscale("log")
ax3.set_yscale("log")
ax3.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax3, "mode number n", r"estimated $\ell_{\mathrm{p}}$ / true $\ell_{\mathrm{p}}$")
charts.title(ax3, "C  Estimate from each mode")
