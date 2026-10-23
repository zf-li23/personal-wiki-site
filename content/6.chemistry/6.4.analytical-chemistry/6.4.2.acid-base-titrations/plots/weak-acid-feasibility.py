"""Titration of weak acids HA with NaOH of the same concentration, from the charge balance.
Left: c = 0.1000 mol/L and different pKa; right: pKa = 7 and different concentrations.
The grey band marks +-0.1 % about the stoichiometric point; the jump becomes too small for
a visual end point when c_sp*Ka falls below about 1e-8."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

Kw = 1.0e-14


def pH(a, c, Ka):
    """a = titration fraction; equal concentrations of acid and base, so c_sp = c / 2 at a = 1."""
    ct, na = c / (1 + a), c * a / (1 + a)
    def f(p):
        h = 10.0 ** -p
        return h + na - Kw / h - ct * Ka / (Ka + h)
    return brentq(f, -1.0, 15.0, xtol=1e-11)


a = np.concatenate([np.linspace(0, 0.98, 120), np.linspace(0.98, 1.02, 200), np.linspace(1.02, 1.6, 80)])
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2), sharey=True)
for pKa, col in zip([3, 5, 7, 8, 9], ["C0", "C1", "C2", "C3", "C4"]):
    Ka = 10.0 ** -pKa
    ax1.plot(a, [pH(x, 0.1, Ka) for x in a], color=col, lw=1.5,
             label=rf"p$K_a$ = {pKa}  ($c_{{sp}}K_a = 5\times10^{{{-pKa - 2}}}$)")
for c, col in zip([1.0, 0.1, 0.01, 0.001], ["C0", "C1", "C2", "C3"]):
    ax2.plot(a, [pH(x, c, 1e-7) for x in a], color=col, lw=1.5, label=rf"$c$ = {c:g} M")
for ax in (ax1, ax2):
    ax.axvspan(0.999, 1.001, color="0.5", alpha=0.35, lw=0)
    ax.set_xlabel("titration fraction $a$")
    ax.set_xlim(0, 1.6)
    ax.legend(frameon=False, fontsize=8, loc="upper left")
ax1.set_ylabel("pH")
ax1.set_ylim(0, 14)
ax1.set_title("c = 0.1000 M, different acid strengths", fontsize=10)
ax2.set_title(r"p$K_a$ = 7, different concentrations", fontsize=10)
fig.tight_layout()
