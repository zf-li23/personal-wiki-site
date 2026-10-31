# Enhanced sampling of a barrier by umbrella sampling and WHAM (weighted histogram analysis).
# A particle performs overdamped Brownian dynamics (Euler-Maruyama, D = 1, dt = 2.5e-4, energies in k_B T)
# in a double well U(x) = 6 (x^2 - 1)^2 + 0.5 x with a barrier of about 6 k_B T.
# A: an unbiased run of 40 000 steps (time 10) started in the left well stays there; the histogram estimate of the
#    free energy -ln p(x) (grey) covers only that well. Fifteen umbrella windows with harmonic biases
#    w_i(x) = (k/2)(x - x_i)^2 (k = 40, x_i from -1.6 to 1.6), each sampled for 80 000 steps (time 20), are combined
#    by WHAM; the reconstructed free-energy profile (dots) matches the exact U(x) (line) across the
#    barrier. Curves are shifted to zero at their minima.
# B: the histograms of the fifteen biased windows, which must overlap for WHAM to connect them.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(5)


def U(x):
    return 6 * (x**2 - 1) ** 2 + 0.5 * x


def dU(x):
    return 24 * x * (x**2 - 1) + 0.5


dt, D = 2.5e-4, 1.0
centers = np.linspace(-1.6, 1.6, 15)
k = 40.0


def simulate(x0, steps, kspring=0.0, c=0.0):
    x = np.array(x0, float)
    out = np.empty((steps, x.size))
    for s in range(steps):
        f = -dU(x) - kspring * (x - c)
        x = x + D * f * dt + np.sqrt(2 * D * dt) * rng.standard_normal(x.size)
        out[s] = x
    return out


free = simulate([-1.0], 40000)[:, 0]
win = simulate(centers.copy(), 80000, k, centers)[8000:]          # discard equilibration

edges = np.linspace(-1.9, 1.9, 77)
xc = 0.5 * (edges[1:] + edges[:-1])
H = np.array([np.histogram(win[:, i], edges)[0] for i in range(len(centers))], float)
Nw = H.sum(1)
bias = 0.5 * k * (xc[None, :] - centers[:, None]) ** 2
f = np.zeros(len(centers))
for _ in range(2000):
    denom = (Nw[:, None] * np.exp(f[:, None] - bias)).sum(0)
    p = H.sum(0) / denom
    fn = -np.log((p[None, :] * np.exp(-bias)).sum(1))
    if np.max(abs(fn - f)) < 1e-8:
        break
    f = fn - fn[0]
G = -np.log(np.where(p > 0, p, np.nan))
G -= np.nanmin(G)

fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.2))
ax = axs[0]
xx = np.linspace(-1.9, 1.9, 300)
ax.plot(xx, U(xx) - U(xx).min(), color=charts.line("protein"), lw=1.6, label="exact U(x)")
hf, _ = np.histogram(free, edges)
Gf = -np.log(np.where(hf > 0, hf, np.nan))
ax.plot(xc, Gf - np.nanmin(Gf), "s", color=charts.line("neutral"), ms=3.5, label="unbiased run (left well only)")
ax.plot(xc, G, "o", color=charts.line("negative"), ms=3.5, label="umbrella sampling + WHAM")
ax.set_ylim(-0.5, 12)
ax.legend(fontsize=7.5, frameon=False, loc="upper center")
charts.style_axes(ax, "reaction coordinate x", "free energy / k_B T")
charts.title(ax, "A   Free-energy profile across a 6 k_B T barrier")

ax = axs[1]
for i in range(len(centers)):
    ax.plot(xc, H[i] / Nw[i], color=charts.line("dna" if i % 2 else "positive"), lw=1.0)
charts.style_axes(ax, "reaction coordinate x", "fraction of samples")
charts.title(ax, "B   Histograms of the 15 biased windows")
fig.tight_layout()
