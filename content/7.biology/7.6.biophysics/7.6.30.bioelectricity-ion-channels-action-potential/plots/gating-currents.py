"""Gating charge and gating currents in a model voltage-gated K+ channel with four independent voltage
sensors (each a two-state system carrying 3.25 e, midpoint -40 mV; total 13 e per channel) and a pore
that is open only when all four are activated (open probability n^4, as in the Hodgkin-Huxley model).
A: normalized charge-voltage (Q-V, proportional to n) and conductance-voltage (G-V, n^4) curves at
20 C: the G-V curve is steeper and shifted to depolarized potentials; a single Boltzmann fit to the
G-V curve (dashed) gives an apparent charge of only about 4 e, far below the 13 e actually moved.
B: gating currents after voltage steps from -100 mV to -60, -30 and 0 mV (sensor rate constants
k = k0 exp(+-z e (V - V_half)/2 k_B T), k0 = 1/ms): fast outward transients whose time integrals are the
moved charge. C: the corresponding ionic K+ currents (driving force V - E_K with E_K = -90 mV) rise
with the sigmoidal delay of n^4, after the gating current is mostly over."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.2))
fig.subplots_adjust(wspace=0.38, left=0.07, right=0.98, bottom=0.17, top=0.87)
kT_e = 25.3  # mV at 20 C
z, Vh, k0 = 3.25, -40.0, 1.0

V = np.linspace(-120, 20, 300)
ninf = 1 / (1 + np.exp(-z * (V - Vh) / kT_e))
G = ninf ** 4
boltz = lambda V, zz, V0: 1 / (1 + np.exp(-zz * (V - V0) / kT_e))
(zfit, V0fit), _ = curve_fit(boltz, V, G, p0=(4, -20))
ax = axs[0]
ax.plot(V, ninf, color=charts.line("k"), lw=1.7, label="Q-V (sensor charge)")
ax.plot(V, G, color=charts.line("blood"), lw=1.7, label="G-V (open probability)")
ax.plot(V, boltz(V, zfit, V0fit), "--", color=P.muted(), lw=1.0, label=f"Boltzmann fit, z = {zfit:.1f}")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "V / mV", "normalized")
charts.title(ax, "A  Charge moves before the pore opens")

t = np.linspace(0, 6, 600)
n0 = 1 / (1 + np.exp(-z * (-100 - Vh) / kT_e))
for (ax_i, kind) in [(1, "gating"), (2, "ionic")]:
    ax = axs[ax_i]
    for Vs, tok in [(-60, "dna"), (-30, "bacterium"), (0, "blood")]:
        a = k0 * np.exp(z * (Vs - Vh) / (2 * kT_e))
        b = k0 * np.exp(-z * (Vs - Vh) / (2 * kT_e))
        ni = a / (a + b)
        n = ni + (n0 - ni) * np.exp(-(a + b) * t)
        if kind == "gating":
            y = 4 * z * (ni - n0) * (a + b) * np.exp(-(a + b) * t)
        else:
            y = n ** 4 * (Vs + 90)
        ax.plot(t, y, color=charts.line(tok), lw=1.6, label=f"step to {Vs} mV")
    ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
    if kind == "gating":
        ax.set_xlim(0, 3)
        charts.style_axes(ax, "time / ms", r"gating current $I_g$ (e ms$^{-1}$ per channel)")
        charts.title(ax, "B  Gating currents")
    else:
        charts.style_axes(ax, "time / ms", "ionic current (a.u.)")
        charts.title(ax, "C  Ionic currents")
