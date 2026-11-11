"""Kinetic scheme of an AMPA-type receptor with deactivation and desensitization.

States: C0 (unbound), C1 (one agonist), C2 (two agonists, closed), O (open), D (desensitized,
reached from C2). Rates (per ms; binding per mM per ms): C0->C1 2 kon T, C1->C0 koff,
C1->C2 kon T, C2->C1 2 koff, C2->O beta, O->C2 alpha, C2->D kd, D->C2 kr, with kon = 5,
koff = 4, beta = 8, alpha = 2, kd = 0.8, kr = 0.015. T is the glutamate concentration.
A: open probability for a 1 ms pulse of 1 mM glutamate (synaptic-like: decay = deactivation)
and for a 100 ms pulse (decay = desensitization to a small steady state).
B: paired 1 ms pulses: the second response recovers from desensitization with the slow rate kr.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
kon, koff, beta, alpha, kd, kr = 5.0, 4.0, 8.0, 2.0, 0.8, 0.015
dt = 0.005


def run(Tfun, tmax):
    n = int(tmax / dt)
    s = np.array([1.0, 0, 0, 0, 0])  # C0 C1 C2 O D
    out = np.empty(n)
    for k in range(n):
        T = Tfun(k * dt)
        c0, c1, c2, o, d = s
        ds = np.array([
            -2 * kon * T * c0 + koff * c1,
            2 * kon * T * c0 - koff * c1 - kon * T * c1 + 2 * koff * c2,
            kon * T * c1 - 2 * koff * c2 - beta * c2 + alpha * o - kd * c2 + kr * d,
            beta * c2 - alpha * o,
            kd * c2 - kr * d,
        ])
        s = s + dt * ds
        out[k] = s[3]
    return np.arange(n) * dt, out


fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9))
ax = axs[0]
t1, o1 = run(lambda t: 1.0 if 1 <= t < 2 else 0.0, 60)
t2, o2 = run(lambda t: 1.0 if 1 <= t < 101 else 0.0, 60)
ax.plot(t2, o2, color=P.edge("negative"), lw=2.0, label="100 ms pulse: desensitization")
ax.plot(t1, o1, color=P.edge("positive"), lw=2.0, label="1 ms pulse: deactivation")
ax.axvspan(1, 2, color=P.light("highlight"), zorder=0)
ax.set_xlabel("Time / ms")
ax.set_ylabel("Open probability")
ax.set_title("A  Deactivation and desensitization", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper right")

ax = axs[1]
ivals = np.array([5, 10, 20, 40, 80, 150, 300])
ratio = []
for iv in ivals:
    tt, oo = run(lambda t, iv=iv: 1.0 if (1 <= t < 2 or 1 + iv <= t < 2 + iv) else 0.0, iv + 15)
    first = oo[tt < 1 + min(iv, 8)].max()
    second = oo[tt >= 1 + iv].max()
    ratio.append(second / first)
ax.plot(ivals, ratio, "o-", color=P.edge("receptor"), lw=1.8)
ax.axhline(1, color=P.muted(), lw=0.8, ls=":")
ax.set_xscale("log")
ax.set_xlabel("Interval between two 1 ms pulses / ms")
ax.set_ylabel("Second / first peak")
ax.set_title("B  Recovery from desensitization", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
