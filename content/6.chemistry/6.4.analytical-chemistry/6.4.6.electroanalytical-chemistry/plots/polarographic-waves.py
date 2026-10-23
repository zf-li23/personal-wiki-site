"""Reversible polarographic waves (2-electron reductions, 25 C) of two metal ions with
half-wave potentials -0.64 V and -1.00 V vs SCE (Cd2+ and Zn2+ in 1 mol/L KCl), equal
diffusion currents, plus a small residual (charging) current; and the corresponding
differential pulse voltammogram (pulse amplitude -50 mV, i.e. towards negative potentials), whose peaks lie at
E1/2 - dE/2 = E1/2 + 25 mV."""

import numpy as np
import matplotlib.pyplot as plt

f = 96485.33212 / (8.314462618 * 298.15)
z = 2
E = np.linspace(-0.3, -1.3, 800)
waves = [(-0.64, 5.0), (-1.00, 5.0)]


def wave(E, E12, Id):
    return Id / (1 + np.exp(z * f * (E - E12)))


I = 0.4 + 0.8 * (-0.3 - E)  # residual current, rising slowly
for E12, Id in waves:
    I = I + wave(E, E12, Id)

dEp = -0.050
dI = np.zeros_like(E)
for E12, Id in waves:
    dI += wave(E + dEp, E12, Id) - wave(E, E12, Id)

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))
ax = axes[0]
ax.plot(E, I, color="k", lw=1.7)
for E12, Id in waves:
    ax.axvline(E12, color="0.6", lw=0.7, ls=":")
ax.annotate("", xy=(-0.80, 0.4 + 0.8 * 0.5 + 5.0), xytext=(-0.80, 0.4 + 0.8 * 0.5),
            arrowprops=dict(arrowstyle="<->", color="C0"))
ax.text(-0.785, 3.4, r"$I_{\mathrm{d}}$", color="C0", ha="right")
for E12, Id in waves:
    ax.text(E12 + 0.01, 11.5, r"$E_{1/2}$", fontsize=9, ha="right")
ax.text(-0.33, 1.2, "residual current", fontsize=9)
ax.invert_xaxis()
ax.set_ylim(0, 12)
ax.set_xlabel(r"$E$ / V vs SCE")
ax.set_ylabel(r"cathodic current / $\mu$A")
ax.set_title("DC polarogram (two reversible waves)", fontsize=10)

ax = axes[1]
ax.plot(E, dI, color="C3", lw=1.7)
for E12, Id in waves:
    ax.axvline(E12 - dEp / 2, color="0.6", lw=0.7, ls=":")
ax.invert_xaxis()
ax.set_xlabel(r"$E$ (base potential) / V vs SCE")
ax.set_ylabel(r"$\Delta I$ / $\mu$A")
ax.set_title(r"differential pulse, $\Delta E$ = -50 mV: peaks at $E_{1/2} - \Delta E/2$", fontsize=10)
fig.tight_layout()
