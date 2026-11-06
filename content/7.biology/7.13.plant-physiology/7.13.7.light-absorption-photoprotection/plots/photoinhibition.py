"""Photoinhibition as a balance of D1 damage and repair: a two-state model of PSII.

The fraction x of functional PSII centres obeys dx/dt = -kd I x + kr (1 - x): damage is first order in the
photon flux I (reciprocity, rate constant kd I) and repair (D1 replacement) is first order in the damaged
fraction. The steady state is x* = kr / (kr + kd I). Fv/Fm is taken as 0.83 x. Illustrative parameters:
kd = 1e-7 m2 umol-1 (damage half-time 58 min at 2000 umol m-2 s-1), kr = 3e-4 s-1 at 25 C (half-time 39 min),
kr = 6e-5 s-1 at 8 C. A: 3 h of 2000 umol m-2 s-1 followed by 3 h of 50 umol m-2 s-1, with normal repair,
with chilling-slowed repair and with repair blocked (lincomycin inhibits chloroplast protein synthesis);
B: steady-state Fv/Fm against photon flux for the two repair rates.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
kd = 1e-7
t = np.linspace(0, 6 * 3600, 2161)
I = np.where(t < 3 * 3600, 2000.0, 50.0)
cases = [("25 °C, repair active", 3e-4, P.edge("plant"), "-"),
         ("8 °C, repair slowed", 6e-5, P.edge("dna"), "--"),
         ("lincomycin, no repair", 0.0, P.edge("negative"), ":")]

fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
for name, kr, col, ls in cases:
    x = np.empty_like(t)
    x[0] = 1.0
    for i in range(1, len(t)):
        dt = t[i] - t[i - 1]
        k = kd * I[i - 1] + kr
        xs = kr / k
        x[i] = xs + (x[i - 1] - xs) * np.exp(-k * dt)
    a.plot(t / 3600, 0.83 * x, color=col, lw=2, ls=ls, label=name)
a.axvspan(0, 3, color=P.mix(P.fill("highlight"), P.surface(), 0.7), lw=0)
a.text(1.5, 0.05, "2000 µmol m$^{-2}$ s$^{-1}$", ha="center", fontsize=8, color=P.muted())
a.text(4.5, 0.05, "50 µmol m$^{-2}$ s$^{-1}$", ha="center", fontsize=8, color=P.muted())
a.set_xlim(0, 6)
a.set_ylim(0, 0.9)
a.set_xlabel("Time $t$ / h")
a.set_ylabel("$F_{\\mathrm{v}}/F_{\\mathrm{m}}$")
a.legend(frameon=False, fontsize=8, loc="lower right", bbox_to_anchor=(1.0, 0.1))
a.set_title("A  Damage and recovery", loc="left", fontsize=10)

Ig = np.linspace(0, 2500, 300)
for name, kr, col, ls in cases[:2]:
    b.plot(Ig, 0.83 * kr / (kr + kd * Ig), color=col, lw=2, ls=ls, label=name)
b.set_xlim(0, 2500)
b.set_ylim(0, 0.9)
b.set_xlabel("PPFD $I$ / µmol m$^{-2}$ s$^{-1}$")
b.set_ylabel("Steady-state $F_{\\mathrm{v}}/F_{\\mathrm{m}}$")
b.legend(frameon=False, fontsize=8, loc="upper right")
b.set_title("B  Steady state $x^* = k_r/(k_r + k_d I)$", loc="left", fontsize=10)
for ax in (a, b):
    ax.grid(True, alpha=0.3)
fig.tight_layout()
