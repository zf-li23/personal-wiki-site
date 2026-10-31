"""Three ways to bud a vesicle from a flat membrane (bending rigidity kappa; the bud is a
spherical cap of fixed area A and opening angle theta, from flat, theta = 0, to a complete bud,
theta = pi; Gaussian-curvature terms neglected). A: a domain of different composition with line
tension gamma along its edge: E / (4 pi kappa) = (1 - cos theta) + lambda sqrt((1 + cos theta)/2)
with lambda = gamma sqrt(A/pi) / (2 kappa); budding lowers the energy for lambda > 2 and becomes
barrier-free for lambda > 4. B: a coat that imposes a spontaneous curvature c0 on the patch:
E = (kappa/2)(2/r - c0)^2 A; the minimum moves from flat to a complete bud as c0 sqrt(A) rises to
4 sqrt(pi) = 7.09. C: a particle of radius R = 50 nm (a virus) adhering with energy mu per area to
a membrane with kappa = 20 kB T and tension 1e-5 N/m: E = (2 kappa / R^2 + sigma - mu) A(theta) is
linear in the wrapped area, so the particle is engulfed completely once mu exceeds
mu* = 2 kappa / R^2 + sigma."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
th = np.linspace(0, np.pi, 300)
c = np.cos(th)
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.2))
fig.subplots_adjust(wspace=0.38, left=0.06, right=0.97, bottom=0.18, top=0.87)

ax = axs[0]
for lam, tok in ((0, "neutral"), (2, "dna"), (4, "bacterium"), (6, "blood")):
    E = (1 - c) + lam * np.sqrt((1 + c) / 2)
    ax.plot(th / np.pi, E - E[0], color=charts.line(tok), lw=1.7, label=rf"$\lambda = {lam}$")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, r"opening angle $\theta/\pi$", r"$[E(\theta) - E(0)]/4\pi\kappa$")
charts.title(ax, "A  Line tension of a domain")

ax = axs[1]
for u, tok in ((0, "neutral"), (3, "dna"), (5, "bacterium"), (4 * np.sqrt(np.pi), "blood")):
    E = 0.5 * (2 * np.sqrt(2 * np.pi * (1 - c)) - u) ** 2
    lab = r"$c_0\sqrt{A} = 4\sqrt{\pi}$" if u > 7 else rf"$c_0\sqrt{{A}} = {u:g}$"
    ax.plot(th / np.pi, (E - E[0]) / (8 * np.pi), color=charts.line(tok), lw=1.7, label=lab)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, r"opening angle $\theta/\pi$", r"$[E(\theta) - E(0)]/8\pi\kappa$")
charts.title(ax, "B  Spontaneous curvature of a coat")

ax = axs[2]
kT = 1.0
kap, R, sig = 20.0, 50.0, 1e-5 / 4.1e-21 * 1e-18  # kB T, nm, kB T/nm^2
mustar = 2 * kap / R**2 + sig
A = 2 * np.pi * R**2 * (1 - c)
for f, tok in ((0.8, "dna"), (1.0, "neutral"), (1.2, "blood")):
    E = (mustar - f * mustar) * A
    ax.plot(th / np.pi, E, color=charts.line(tok), lw=1.7, label=rf"$\mu = {f:g}\,\mu^*$")
ax.text(0.03, -95, rf"$\mu^* = {mustar:.4f}\,k_{{\mathrm{{B}}}}T$/nm$^2$", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"wrapping angle $\theta/\pi$", r"E / $k_{\mathrm{B}}T$")
charts.title(ax, "C  Adhesion of a particle (R = 50 nm)")
