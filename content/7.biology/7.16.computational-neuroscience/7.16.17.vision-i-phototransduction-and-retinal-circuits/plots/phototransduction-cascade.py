"""Phototransduction as a cascade of first-order stages followed by a saturating nonlinearity.

Linear stage: the single-photon response is the impulse response of n identical first-order stages,
h(t) = (t/tau)^(n-1) exp(-t/tau) / ((n-1)! tau), n = 4, tau = 60 ms (independent-activation model of
Baylor, Hodgkin and Lamb 1974, the shape of a dark-adapted rod response).
Onset: for a step activation of R* the PDE activity rises linearly and cGMP falls quadratically,
F(t) = (1/2) Phi A (t - t_eff)^2 (Lamb and Pugh 1992), drawn for the early phase.
Saturation: the fraction of the dark current suppressed is R = 1 - exp(-Phi k h(t)) (all channels
close for bright flashes), Phi = number of photoisomerizations.
A: single-photon impulse responses for n = 1, 2, 4, 6 (same peak time scale). B: flash family.
C: peak response versus flash strength, with the exponential saturation curve.
"""
import math

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
t = np.linspace(0, 1.2, 1200)
tau = 0.06


def h(t, n, tau):
    return (t / tau) ** (n - 1) * np.exp(-t / tau) / (math.factorial(n - 1) * tau)


cols = [P.edge("dna"), P.edge("rna"), P.edge("positive"), P.edge("negative")]
fig, axs = plt.subplots(1, 3, figsize=(13, 4.0))
ax = axs[0]
for n, c in zip((1, 2, 4, 6), cols):
    tt = tau * 4 / n
    y = h(t, n, tt)
    ax.plot(t * 1000, y / y.max(), color=c, lw=1.8, label=f"n = {n} stages")
ax.set_xlim(0, 800)
ax.set_xlabel("Time after flash / ms")
ax.set_ylabel("Normalized response")
ax.legend(frameon=False, fontsize=8)
ax.set_title("A  More stages: delayed, smoother onset", loc="left", fontsize=10)

bx = axs[1]
k = 0.04 / h(t, 4, tau).max()
for j, Phi in enumerate((1, 5, 25, 125, 625, 3125)):
    R = 1 - np.exp(-Phi * k * h(t, 4, tau))
    bx.plot(t * 1000, R, color=P.mix(P.edge("dna"), P.edge("rna"), j / 5), lw=1.5,
            label=f"{Phi} R*")
bx.set_xlim(0, 1200)
bx.set_ylim(0, 1.05)
bx.set_xlabel("Time after flash / ms")
bx.set_ylabel("Fraction of dark current suppressed")
bx.legend(frameon=False, fontsize=7.5, ncol=2, loc="upper right")
bx.set_title("B  Flash family: saturation and prolonged plateau", loc="left", fontsize=10)

cx = axs[2]
Phis = np.logspace(-0.3, 4, 60)
peak = [np.max(1 - np.exp(-p * k * h(t, 4, tau))) for p in Phis]
cx.plot(Phis, peak, color=P.edge("dna"), lw=2, label="peak of model response")
cx.plot(Phis, np.minimum(0.04 * Phis, 1.2), color=P.muted(), lw=1, ls=":", label="linear extrapolation")
cx.set_xscale("log")
cx.set_ylim(0, 1.05)
cx.set_xlabel("Flash strength / photoisomerizations")
cx.set_ylabel("Peak response")
cx.legend(frameon=False, fontsize=8, loc="lower right")
cx.set_title("C  Intensity-response curve", loc="left", fontsize=10)
fig.tight_layout()
