"""Linear viscoelastic models built from a spring (modulus E) and a dashpot (viscosity eta),
with relaxation time tau = eta/E. A: creep, the strain after a stress sigma0 is switched on at
t = 0 and off at t = 3 tau: the Voigt (Kelvin-Voigt) solid creeps to sigma0/E and recovers
completely; the Maxwell liquid jumps elastically and then flows without limit, keeping the
flowed strain; the standard linear solid (a spring in series with a Voigt element, E1 = E2 = E)
jumps to sigma0/(2E) and relaxes to sigma0/E. B: storage and loss moduli of a Maxwell liquid in
oscillatory shear: elastic (G' > G'') above the crossover frequency 1/tau, viscous below.
C: the weak power law G' ~ G'' ~ omega^0.2 typical of the cytoplasm and cortex of living cells
(soft glassy rheology), with no single relaxation time."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.2))
fig.subplots_adjust(wspace=0.38, left=0.06, right=0.97, bottom=0.18, top=0.87)

t = np.linspace(-0.5, 7, 800)
on = (t >= 0) & (t < 3)
off = t >= 3
voigt = np.where(on, 1 - np.exp(-t), 0.0) + np.where(off, (1 - np.exp(-3)) * np.exp(-(t - 3)), 0.0)
maxwell = np.where(on, 1 + t, 0.0) + np.where(off, 3.0, 0.0)
sls = np.where(on, 0.5 + 0.5 * (1 - np.exp(-t / 0.5)), 0.0) + np.where(off, 0.5 * (1 - np.exp(-3 / 0.5)) * np.exp(-(t - 3) / 0.5), 0.0)
ax = axs[0]
ax.axvspan(0, 3, color=P.fill("highlight"), alpha=0.25, lw=0)
ax.plot(t, voigt, color=charts.line("dna"), lw=1.7, label="Voigt solid")
ax.plot(t, maxwell, color=charts.line("blood"), lw=1.7, label="Maxwell liquid")
ax.plot(t, sls, color=charts.line("bacterium"), lw=1.7, label="standard linear solid")
ax.text(0.1, 3.7, r"stress $\sigma_0$ on", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(ax, r"time $t/\tau$", r"strain $\varepsilon E/\sigma_0$")
charts.title(ax, "A  Creep and recovery")

ax = axs[1]
w = np.logspace(-2, 2, 300)
Gp = w**2 / (1 + w**2)
Gpp = w / (1 + w**2)
ax.plot(w, Gp, color=charts.line("dna"), lw=1.7, label=r"$G'$ (storage)")
ax.plot(w, Gpp, color=charts.line("blood"), lw=1.7, label=r"$G''$ (loss)")
ax.axvline(1, color=P.muted(), lw=0.7, ls=":")
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_ylim(1e-4, 2)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, r"frequency $\omega\tau$", r"modulus / E")
charts.title(ax, "B  Maxwell liquid")

ax = axs[2]
w = np.logspace(-1, 3, 300)
beta = 0.2
G0 = 300.0  # Pa at 1 rad/s
mag = G0 * w**beta
Gp = mag * np.cos(np.pi * beta / 2) + 0.0
Gpp = mag * np.sin(np.pi * beta / 2) + 1e-3 * 1.0 * w * 1e0
ax.plot(w, Gp, color=charts.line("dna"), lw=1.7, label=r"$G'$")
ax.plot(w, Gpp, color=charts.line("blood"), lw=1.7, label=r"$G''$")
ax.set_xscale("log"); ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"frequency $\omega$ / rad s$^{-1}$", "modulus / Pa")
charts.title(ax, r"C  Cells: $G^* \propto (\mathrm{i}\omega)^{0.2}$")
