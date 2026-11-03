"""Estimating selection gradients by regression (Lande and Arnold 1983), on simulated data.
A: 500 individuals with a standardized trait z; survival is a Bernoulli draw with probability
0.7 exp(0.35 z - 0.25 z^2) (capped at 1), i.e. directional plus stabilizing selection. Relative fitness
(survival divided by mean survival) is regressed on z (linear fit: slope beta) and on z and z^2/2
(quadratic fit: coefficient gamma). Points are jittered vertically for visibility; open circles give the
mean relative fitness in bins of 0.5 SD. B: a fitness surface with stabilizing and correlational selection,
w = exp[(gamma_11 z1^2 + 2 gamma_12 z1 z2 + gamma_22 z2^2) / 2] with gamma_11 = gamma_22 = -0.4 and
gamma_12 = 0.3 (contours of relative fitness): fitness falls off slowly along a ridge on which high z1 goes
with high z2 and low with low, and steeply across it, as for stripe pattern and escape
behaviour in garter snakes. The ellipse is the 95 % contour of the phenotype distribution."""
import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts
from wikibio import evolution as evo

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
n = 500
z = rng.normal(0, 1, n)
p = np.minimum(1, 0.7 * np.exp(0.35 * z - 0.25 * z**2))
alive = (rng.random(n) < p).astype(float)
la = evo.lande_arnold(z, alive)
zs = (z - z.mean()) / z.std()
w = alive / alive.mean()

fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.2), gridspec_kw={"width_ratios": [1.25, 1]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.13, top=0.9, wspace=0.25)
a = axs[0]
a.scatter(zs, w + rng.uniform(-0.06, 0.06, n), s=5, color=P.fill("neutral"), edgecolor=P.muted(), lw=0.3)
edges = np.arange(-2.5, 2.51, 0.5)
for lo, hi in zip(edges[:-1], edges[1:]):
    m = (zs >= lo) & (zs < hi)
    if m.sum() >= 8:
        a.scatter([(lo + hi) / 2], [w[m].mean()], s=28, facecolor="none", edgecolor=P.ink(), lw=1.1, zorder=4)
X1 = np.c_[np.ones(n), zs]
c1 = np.linalg.lstsq(X1, w, rcond=None)[0]
X2 = np.c_[np.ones(n), zs, zs**2 / 2]
c2 = np.linalg.lstsq(X2, w, rcond=None)[0]
g = np.linspace(-3, 3, 200)
a.plot(g, c1[0] + c1[1] * g, color=charts.line("dna"), lw=2, label=f"linear: $\\beta = {la['beta']:.2f} \\pm {la['beta_se']:.2f}$")
a.plot(g, c2[0] + c2[1] * g + c2[2] * g**2 / 2, color=charts.line("rna"), lw=2, ls="--",
       label=f"quadratic: $\\gamma = {la['gamma']:.2f} \\pm {la['gamma_se']:.2f}$".replace("-", "−"))
a.set_ylim(-0.3, 2.2)
a.set_xlim(-3, 3)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "trait $z$ (standardized)", "relative fitness $w$")
charts.title(a, "A  Directional and stabilizing selection")

b = axs[1]
x = np.linspace(-3, 3, 201)
Z1, Z2 = np.meshgrid(x, x)
W = np.exp(0.5 * (-0.4 * Z1**2 + 2 * 0.3 * Z1 * Z2 - 0.4 * Z2**2))
W = W / W[100, 100]
cs = b.contour(Z1, Z2, W, levels=[0.1, 0.3, 0.5, 0.7, 0.9], colors=[charts.line("enzyme")], linewidths=1.1)
b.clabel(cs, fontsize=FT["tiny"], fmt="%.2g", colors=P.ink())
t = np.linspace(0, 2 * np.pi, 200)
r = np.sqrt(5.99)
b.plot(r * np.cos(t), r * np.sin(t), color=P.muted(), lw=1, ls=":")
b.set_aspect("equal")
b.set_xlim(-3, 3)
b.set_ylim(-3, 3)
charts.style_axes(b, "trait $z_1$", "trait $z_2$")
charts.title(b, "B  Correlational selection, $\\gamma_{12} > 0$")
