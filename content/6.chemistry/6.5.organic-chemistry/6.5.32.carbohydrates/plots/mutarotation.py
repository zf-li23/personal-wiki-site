"""Mutarotation of D-glucose as a reversible first-order reaction alpha <=> beta (the open chain
is a steady-state intermediate present at about 0.003%). Starting from either pure anomer, the
specific rotation relaxes exponentially to the same equilibrium value with the rate constant
k = k1 + k-1. Rotations: alpha +112.2, beta +18.7 deg; the equilibrium fraction of beta,
x = 0.636, follows from the measured equilibrium rotation +52.7 deg. The rate constant
(0.015 per minute, uncatalysed, near room temperature) only sets the time axis; acid and base
both catalyse the reaction strongly."""

import numpy as np
import matplotlib.pyplot as plt

A, B, EQ = 112.2, 18.7, 52.7
x_beta = (A - EQ) / (A - B)
k = 0.015  # 1/min, k1 + k-1
t = np.linspace(0, 300, 400)

fig, ax = plt.subplots(figsize=(7.5, 3.8))
for start, label, colour in ((A, r"start: pure $\alpha$ anomer", "#2563eb"), (B, r"start: pure $\beta$ anomer", "#dc2626")):
    ax.plot(t, EQ + (start - EQ) * np.exp(-k * t), color=colour, lw=2, label=label)
ax.axhline(EQ, color="0.5", ls="--", lw=1)
ax.text(295, EQ - 9, rf"equilibrium $+{EQ}^\circ$: $x_\beta = {x_beta:.3f}$", ha="right", fontsize=9, color="0.4")
ax.set_xlabel(r"$t$ / min")
ax.set_ylabel(r"$[\alpha]_{\mathrm{D}}$ / deg")
ax.set_xlim(0, 300)
ax.set_ylim(0, 120)
ax.legend(frameon=False, loc="upper right", bbox_to_anchor=(1.0, 0.92))
