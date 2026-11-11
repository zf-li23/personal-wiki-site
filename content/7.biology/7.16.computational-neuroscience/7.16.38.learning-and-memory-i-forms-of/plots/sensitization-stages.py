"""Short- and long-term sensitization in Aplysia as a two-stage cascade (schematic model).

Each 5-HT pulse (tail shock) raises PKA activity p by 1; p decays with tau_p = 20 min (short-term facilitation).
Nuclear PKA n follows p slowly: dn/dt = (p - n) / tau_n, tau_n = 30 min.
CREB-dependent growth g: dg/dt = k h(n) (1 - g) - g / tau_g, h(n) = n^4 / (n^4 + 1.5^4), k = 0.05 / min,
tau_g = 10 d. Facilitation of the sensory-motor EPSP = 1 + 1.0 p_sat + 1.5 g, p_sat = p / (1 + p).
One pulse versus five pulses spaced by 20 min.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
dt = 0.5  # min
t = np.arange(-30, 5 * 24 * 60, dt)


def run(pulses):
    p = n = g = 0.0
    F = np.empty_like(t)
    pk = set(int(round((x + 30) / dt)) for x in pulses)
    for i in range(len(t)):
        if i in pk:
            p += 1.0
        p += dt * (-p / 20.0)
        n += dt * (p - n) / 30.0
        h = n ** 4 / (n ** 4 + 1.5 ** 4)
        g += dt * (0.05 * h * (1 - g) - g / (10 * 24 * 60))
        F[i] = 1 + p / (1 + p) + 1.5 * g
    return F


fig, ax = plt.subplots(figsize=(7.5, 3.5))
tt = np.maximum(t, 0) + 1
ax.semilogx(tt, 100 * run([0.0]), color=P.edge("dna"), lw=2.2, label="1 pulse of 5-HT")
ax.semilogx(tt, 100 * run([0, 20, 40, 60, 80]), color=P.edge("negative"), lw=2.2, label="5 spaced pulses (20 min apart)")
for x, lab in [(60, "1 h"), (24 * 60, "1 d"), (4 * 24 * 60, "4 d")]:
    ax.axvline(x, color=P.muted(), lw=0.7, ls=":")
    ax.text(x * 1.05, 255, lab, fontsize=8, color=P.muted())
ax.axhline(100, color=P.muted(), lw=0.8)
ax.set_xlabel("Time after the first pulse / min (log scale)")
ax.set_ylabel("EPSP amplitude / % of baseline")
ax.set_ylim(80, 270)
ax.legend(frameon=False, fontsize=8, loc="center left")
ax.grid(True, alpha=0.3, which="both")
fig.tight_layout()
