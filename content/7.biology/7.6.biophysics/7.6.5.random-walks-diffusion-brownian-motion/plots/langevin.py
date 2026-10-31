"""Langevin dynamics of a Brownian particle (overdamped, dimensionless units: gamma = kBT = 1, so
D = 1). A: trajectories of a free particle and of a particle in a harmonic trap of stiffness
kappa = 1 (relaxation time tau = gamma/kappa = 1). B: mean squared displacement from x(0) = 0 over 1000
particles (dots) against theory: 2Dt for the free particle and (kBT/kappa)(1 - e^{-2t/tau}) in
the trap, which starts diffusively and saturates at the equipartition value kBT/kappa. C: with inertia,
m dv/dt = -gamma v + xi(t), the mean kinetic energy of particles started at rest approaches kBT/2
only if the noise strength is 2 gamma kBT (fluctuation-dissipation theorem); noise of half or twice
that strength gives the wrong temperature."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(2)
dt, nsteps, M = 0.01, 2000, 1000
t = np.arange(nsteps + 1) * dt

xf = np.zeros((M, nsteps + 1))
xt = np.zeros((M, nsteps + 1))
kick = rng.normal(0, np.sqrt(2 * dt), (M, nsteps))
for i in range(nsteps):
    xf[:, i + 1] = xf[:, i] + kick[:, i]
    xt[:, i + 1] = xt[:, i] - xt[:, i] * dt + kick[:, i]

fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3))
fig.subplots_adjust(wspace=0.38, left=0.06, right=0.98, bottom=0.17, top=0.88)

ax = axs[0]
ax.plot(t, xf[0], color=charts.line("dna"), lw=0.8, label="free")
ax.plot(t, xt[0], color=charts.line("blood"), lw=0.8, label=r"trap, $\kappa = 1$")
ax.axhspan(-1, 1, color=P.mix(P.fill("blood"), P.surface(), 0.8), lw=0, zorder=0)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, r"$t$ / ($\gamma/\kappa$)", r"$x$ / $\sqrt{k_\mathrm{B}T/\kappa}$")
charts.title(ax, "A  Free and trapped")

ax = axs[1]
sel = np.unique(np.logspace(0, np.log10(nsteps), 22).astype(int))
ax.plot(t[sel], (xf[:, sel] ** 2).mean(0), "o", color=charts.line("dna"), ms=3.5)
ax.plot(t[sel], (xt[:, sel] ** 2).mean(0), "o", color=charts.line("blood"), ms=3.5)
tt = t[1:]
ax.plot(tt, 2 * tt, color=charts.line("dna"), lw=1.2, label=r"$2Dt$")
ax.plot(tt, 1 - np.exp(-2 * tt), color=charts.line("blood"), lw=1.2,
        label=r"$\frac{k_\mathrm{B}T}{\kappa}(1 - \mathrm{e}^{-2t/\tau})$")
ax.axhline(1.0, color=P.muted(), lw=0.6, ls=":")
ax.text(0.012, 1.25, r"equipartition $k_\mathrm{B}T/\kappa$", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_xscale("log")
ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, r"$t$", r"$\langle x^2\rangle$")
charts.title(ax, r"B  $\langle x^2\rangle$ from $x(0) = 0$")

ax = axs[2]
m, gamma = 1.0, 1.0
dt2, n2 = 0.01, 600
t2 = np.arange(n2 + 1) * dt2
for fac, tok, lab in ((0.5, "neutral", r"noise $\gamma k_\mathrm{B}T$"), (1.0, "enzyme", r"noise $2\gamma k_\mathrm{B}T$"),
                      (2.0, "drug", r"noise $4\gamma k_\mathrm{B}T$")):
    v = np.zeros(M)
    ke = [0.0]
    for i in range(n2):
        v = v - gamma / m * v * dt2 + np.sqrt(2 * fac * gamma * dt2) / m * rng.normal(size=M)
        ke.append(0.5 * m * (v ** 2).mean())
    ax.plot(t2, ke, color=charts.line(tok), lw=1.4, label=lab)
    ax.plot(t2, 0.5 * fac * (1 - np.exp(-2 * gamma * t2 / m)), color=charts.line(tok), lw=0.7, ls="--")
ax.axhline(0.5, color=P.muted(), lw=0.6, ls=":")
ax.text(3.2, 0.53, r"$k_\mathrm{B}T/2$", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right", bbox_to_anchor=(1.0, 0.68))
charts.style_axes(ax, r"$t$ / ($m/\gamma$)", r"$\langle mv^2\rangle/2$ / $k_\mathrm{B}T$")
charts.title(ax, "C  Fluctuation-dissipation")
