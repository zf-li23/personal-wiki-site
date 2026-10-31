"""An active oscillator poised near a Hopf bifurcation as the amplifier of hearing. Normal form
dz/dt = (mu + i omega_0) z - |z|^2 z + F exp(i omega t); in the steady state the response amplitude r
solves F^2 = r^2 [(mu - r^2)^2 + (omega - omega_0)^2]. A: response at the characteristic frequency
against stimulus force for a passive-like damped system (mu = -0.3), close to the bifurcation
(mu = -0.01) and at it (mu = 0): at the critical point the response grows as F^(1/3) for all forces
(compressive nonlinearity, dashed slope 1/3), so weak stimuli are amplified enormously while strong
ones are compressed. B: gain r/F against frequency detuning for a weak force F = 1e-4: the critical
oscillator is sharply tuned."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.3))
fig.subplots_adjust(wspace=0.32, left=0.09, right=0.98, bottom=0.16, top=0.87)


def amp(F, mu, dw):
    g = lambda r: r ** 2 * ((mu - r ** 2) ** 2 + dw ** 2) - F ** 2
    return brentq(g, 0, max(2.0, F ** (1 / 3) * 2 + 1))


Fs = np.logspace(-6, 0, 80)
ax = axs[0]
for mu, tok in [(-0.3, "neutral"), (-0.01, "dna"), (0.0, "blood")]:
    r = [amp(F, mu, 0.0) for F in Fs]
    ax.loglog(Fs, r, color=charts.line(tok), lw=1.7, label=rf"$\mu = {mu:g}$")
ax.loglog(Fs, 0.6 * Fs ** (1 / 3), "--", color=P.muted(), lw=1.0, label="slope 1/3")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "stimulus force $F$", "response amplitude $r$")
charts.title(ax, "A  Compressive amplification")
ax = axs[1]
dws = np.linspace(-0.5, 0.5, 401)
for mu, tok in [(-0.3, "neutral"), (-0.01, "dna"), (0.0, "blood")]:
    g = [amp(1e-4, mu, dw) / 1e-4 for dw in dws]
    ax.semilogy(dws, g, color=charts.line(tok), lw=1.6, label=rf"$\mu = {mu:g}$")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"detuning $\omega - \omega_0$", "gain $r/F$")
charts.title(ax, "B  Sharp tuning")
