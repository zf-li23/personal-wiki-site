"""Temporal and spatial summation of postsynaptic potentials (phenomenological alpha-function model).

Each PSP at the soma is an alpha function V(t) = A (t/tau) exp(1 - t/tau) that peaks at t = tau,
added linearly on a resting potential of -65 mV; threshold is drawn at -50 mV. tau = 3 ms gives a
PSP lasting about 15 ms.
A: temporal summation. The same input (a synchronous volley giving 5 mV at the soma) arrives
three times at 20 ms intervals (no summation) or at 4 ms intervals (summation reaches threshold).
B: spatial summation with passive attenuation. Inputs at electrotonic distance x/lambda reach the
soma with amplitude A0 exp(-x/lambda) and a slower time course (tau grows with distance; a
schematic stand-in for the cable filtering of 7.6.30). Proximal inputs dominate.
C: an IPSP (-4 mV, at the soma) arriving 2 ms after a suprathreshold summed EPSP cancels it.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
VR, VT = -65.0, -50.0
t = np.linspace(0, 60, 1201)


def alpha(t0, amp, tau=3.0):
    s = np.clip(t - t0, 0, None)
    return amp * (s / tau) * np.exp(1 - s / tau)


fig, axs = plt.subplots(1, 3, figsize=(12, 3.9), sharey=True)
exc, inh = P.edge("positive"), P.edge("negative")

ax = axs[0]
slow = VR + sum(alpha(t0, 5.0) for t0 in (5, 25, 45))
fast = VR + sum(alpha(t0, 5.0) for t0 in (5, 9, 13))
ax.plot(t, slow, color=P.muted(), lw=1.8, label="interval 20 ms")
ax.plot(t, fast, color=exc, lw=2.0, label="interval 4 ms")
ax.set_title("A  Temporal summation", loc="left", fontsize=10)

ax = axs[1]
cols = [P.edge("dna"), P.edge("rna"), P.edge("protein")]
total = np.zeros_like(t)
for (x, c) in zip((0.2, 0.8, 1.6), cols):
    v = alpha(5, 9.0 * np.exp(-x), tau=3.0 * (1 + 0.8 * x))
    total += v
    ax.plot(t, VR + v, color=c, lw=1.3, ls="--", label=f"input at x/$\\lambda$ = {x}")
ax.plot(t, VR + total, color=exc, lw=2.0, label="sum of the three")
ax.set_title("B  Spatial summation", loc="left", fontsize=10)

ax = axs[2]
e = sum(alpha(t0, 6.0) for t0 in (5, 7, 9))
i = alpha(9, -4.0, tau=5.0) + alpha(11, -4.0, tau=5.0)
ax.plot(t, VR + e, color=exc, lw=2.0, label="EPSPs alone")
ax.plot(t, VR + i, color=inh, lw=1.5, ls="--", label="IPSPs alone")
ax.plot(t, VR + e + i, color=P.ink(), lw=2.0, label="EPSPs + IPSPs")
ax.set_title("C  Excitation cancelled by inhibition", loc="left", fontsize=10)

for ax in axs:
    ax.axhline(VT, color=P.muted(), lw=1, ls=":")
    ax.text(59, VT + 0.4, "threshold", ha="right", va="bottom", fontsize=8, color=P.muted())
    ax.set_xlim(0, 60)
    ax.set_ylim(-75, -44)
    ax.set_xlabel("Time / ms")
    ax.legend(frameon=False, fontsize=7.5, loc="lower right")
    ax.grid(True, alpha=0.3)
axs[0].set_ylabel("Somatic membrane potential / mV")
fig.tight_layout()
