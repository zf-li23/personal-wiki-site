"""The semicircular canal as an overdamped torsion pendulum (Steinhausen model).

Cupula-endolymph deflection theta for head angular velocity Omega:
  theta / Omega = G tau1 s / ((1 + tau1 s)(1 + tau2 s)),  tau1 = 5 s (long), tau2 = 4 ms (short).
Between 1/(2 pi tau1) = 0.03 Hz and 1/(2 pi tau2) = 40 Hz the cupula signals head velocity.
A: gain and phase (relative to head velocity). B: response to a 60 deg/s rotation lasting 45 s:
the afferent (cupula) signal decays with tau1 and reverses when rotation stops; the central
"velocity storage" prolongs the VOR slow-phase velocity to a time constant of about 15 s
(modelled here as a first-order process with tau_c = 15 s driven by the same step).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
t1, t2, tc = 5.0, 4e-3, 15.0
f = np.logspace(-3, 3, 600)
s = 2j * np.pi * f
H = t1 * s / ((1 + t1 * s) * (1 + t2 * s))

fig, axs = plt.subplots(1, 2, figsize=(12, 4.2))
ax = axs[0]
ax.plot(f, 20 * np.log10(np.abs(H)), color=P.edge("dna"), lw=2, label="gain")
ax.set_xscale("log")
ax.set_ylabel("Gain re head velocity / dB", color=P.edge("dna"))
ax.set_xlabel("Frequency / Hz")
ax.set_ylim(-45, 5)
ax.axvspan(0.5, 20, color=P.fill("highlight"), alpha=0.25, lw=0)
ax.text(3.2, -40, "natural head\nmovements", fontsize=8, ha="center", color=P.muted())
ax2 = ax.twinx()
ax2.plot(f, np.degrees(np.angle(H)), color=P.edge("rna"), lw=1.6, ls="--", label="phase")
ax2.set_ylabel("Phase / degrees", color=P.edge("rna"))
ax2.set_ylim(-95, 95)
ax.set_title("A  Velocity transducer between 0.03 and 40 Hz", loc="left", fontsize=10)

dt = 0.01
t = np.arange(-5, 100, dt)
omega = np.where((t >= 0) & (t < 45), 60.0, 0.0)
# cupula: high-pass with tau1 (tau2 negligible at this time scale)
cup = np.zeros_like(t)
vs = np.zeros_like(t)
for k in range(1, len(t)):
    d_om = omega[k] - omega[k - 1]
    cup[k] = cup[k - 1] + d_om - dt * cup[k - 1] / t1
    vs[k] = vs[k - 1] + d_om - dt * vs[k - 1] / tc
bx = axs[1]
bx.plot(t, omega, color=P.muted(), lw=1.2, label="head velocity")
bx.plot(t, cup, color=P.edge("dna"), lw=2, label="cupula / afferent signal (τ = 5 s)")
bx.plot(t, vs, color=P.edge("rna"), lw=2, ls="--", label="VOR slow phase (velocity storage, τ ≈ 15 s)")
bx.axhline(0, color=P.muted(), lw=0.5)
bx.set_xlabel("Time / s")
bx.set_ylabel("Angular velocity / (deg/s)")
bx.text(50, -45, "post-rotatory response:\nsensation of turning the other way", fontsize=8,
        color=P.muted())
bx.legend(frameon=False, fontsize=8, loc="upper right")
bx.set_ylim(-70, 90)
bx.set_title("B  Constant rotation, then stop", loc="left", fontsize=10)
fig.tight_layout()
