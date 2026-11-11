"""The calcium control hypothesis: plasticity as a function of spine Ca2+.

Weight dynamics  tau_w dw/dt = Omega(c) - w  with the target
  Omega(c) = 0.5 - 0.5 S(c - 0.35) + S(c - 0.55),   S(x) = 1 / (1 + exp(-x / 0.03)),
so that Omega = 0.5 (the resting weight w_0, no change) below 0.35 uM, Omega = 0 (depression)
between 0.35 and 0.55 uM and Omega = 1 (potentiation) above 0.55 uM; tau_w = 40 s.
Spine Ca2+: baseline 0.05 uM, each presynaptic pulse (paired with a fixed postsynaptic
depolarization) adds A uM that decays with tau_Ca = 50 ms (a coarse stand-in for NMDA-receptor
Ca2+ entry).
A: Omega(c) with the two thresholds.
B: Ca2+ traces for 1, 10 and 50 Hz stimulation (A = 0.45 uM), with the thresholds.
C: relative weight change after 900 pulses against stimulation frequency, for two Ca2+ amplitudes
   per pulse (A = 0.45 and 0.7 uM; a stronger postsynaptic depolarization or NMDA drive shifts the
   crossover from depression to potentiation to lower frequencies, a sliding-threshold effect).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
cb, tauCa, tauw = 0.05, 50.0, 40000.0  # uM, ms, ms
a1, a2, sw = 0.35, 0.55, 0.03


def S(x):
    return 1.0 / (1.0 + np.exp(-x / sw))


def omega(c):
    return 0.5 - 0.5 * S(c - a1) + S(c - a2)


def trace(f, A, npulse, dt=1.0):
    T = npulse * 1000.0 / f
    n = int(T / dt)
    c = np.empty(n)
    x = 0.0
    nxt = 0.0
    period = 1000.0 / f
    dec = np.exp(-dt / tauCa)
    for k in range(n):
        t = k * dt
        if t >= nxt - 1e-9:
            x += A
            nxt += period
        c[k] = cb + x
        x *= dec
    return c


def final_w(f, A, npulse=900):
    c = trace(f, A, npulse)
    # exact update of tau_w dw/dt = Omega - w with Omega piecewise constant over dt = 1 ms
    w = 0.5
    om = omega(c)
    decay = np.exp(-1.0 / tauw)
    for o in om:
        w = o + (w - o) * decay
    return w


fig, axs = plt.subplots(1, 3, figsize=(13, 3.8))
ax = axs[0]
c = np.linspace(0, 1.2, 400)
ax.plot(c, omega(c), color=P.edge("protein"), lw=2.2)
ax.axvline(a1, color=P.edge("negative"), lw=1.0, ls="--")
ax.axvline(a2, color=P.edge("positive"), lw=1.0, ls="--")
ax.text(a1 - 0.02, 0.95, "$\\theta_{\\mathrm{d}}$", ha="right", fontsize=9, color=P.edge("negative"))
ax.text(a2 + 0.02, 0.2, "$\\theta_{\\mathrm{p}}$", ha="left", fontsize=9, color=P.edge("positive"))
ax.axhline(0.5, color=P.muted(), lw=0.6)
ax.text(1.18, 0.52, "resting weight", ha="right", fontsize=8, color=P.muted())
ax.set_xlabel("Spine $[\\mathrm{Ca^{2+}}]$ / $\\mu$M")
ax.set_ylabel("Target weight $\\Omega$")
ax.set_title("A  Plasticity function", loc="left", fontsize=10)

ax = axs[1]
for f, col in ((1.0, P.edge("negative")), (10.0, P.edge("protein")), (50.0, P.edge("positive"))):
    tr = trace(f, 0.45, int(max(3, f * 1.5)))
    ax.plot(np.arange(len(tr)) / 1000.0, tr, color=col, lw=1.3, label=f"{f:g} Hz")
ax.axhline(a1, color=P.edge("negative"), lw=0.9, ls="--")
ax.axhline(a2, color=P.edge("positive"), lw=0.9, ls="--")
ax.set_xlim(0, 1.5)
ax.set_ylim(0, 1.8)
ax.set_xlabel("Time / s")
ax.set_ylabel("$[\\mathrm{Ca^{2+}}]$ / $\\mu$M")
ax.set_title("B  Ca$^{2+}$ at three frequencies", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper center", ncol=3)

ax = axs[2]
fs = np.array([0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30, 50, 100])
for A, col in ((0.45, P.edge("dna")), (0.7, P.edge("negative"))):
    dw = [100 * (final_w(f, A) / 0.5 - 1) for f in fs]
    ax.semilogx(fs, dw, "o-", ms=4, lw=1.6, color=col, label=f"{A:g} $\\mu$M per pulse")
ax.axhline(0, color=P.muted(), lw=0.8)
ax.set_xlabel("Stimulation frequency / Hz")
ax.set_ylabel("Weight change after 900 pulses / %")
ax.set_title("C  Frequency dependence", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper left")
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
