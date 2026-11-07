"""Afterdischarge from recurrent excitation terminated by slow negative feedback.

tau_E dE/dt = -E + F(w_EE E - g z + I_stim(t)),  tau_z dz/dt = -z + E,  F(u) = 1/(1 + exp(-(u - 0.5)/0.08)),
tau_E = 10 ms, tau_z = 0.5 s; a 50-ms stimulus (I = 1) starts at t = 0.1 s.
A: activity for several recurrent strengths w_EE (g = 1). Weak recurrence: activity stops with the
stimulus; stronger recurrence: activity outlasts it until the slow variable z shuts it off.
B: duration of the afterdischarge (time E stays above 0.5 after the stimulus ends) against w_EE for
two feedback strengths g. Above a critical w_EE the feedback can no longer terminate the activity
(persistent firing, clipped at the end of the 3-s run).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
T, dt, t0, t1 = 3.0, 2e-4, 0.1, 0.15


def F(u):
    return 1.0 / (1.0 + np.exp(-(u - 0.5) / 0.08))


def simulate(w, g=1.0, tE=0.01, tz=0.5):
    n = int(T / dt)
    E = z = 0.0
    out = np.zeros(n)
    for i in range(n):
        tt = i * dt
        stim = 1.0 if t0 < tt < t1 else 0.0
        E += dt * (-E + F(w * E - g * z + stim)) / tE
        z += dt * (-z + E) / tz
        out[i] = E
    return np.arange(n) * dt, out


def duration(t, E):
    on = t[E > 0.5]
    return max(0.0, on.max() - t1) if len(on) else 0.0


fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.0))
cols = [P.muted(), P.edge("dna"), P.edge("protein"), P.edge("rna")]
for w, c in zip((0.6, 1.0, 1.4, 1.6), cols):
    t, E = simulate(w)
    ax.plot(t, E, color=c, lw=1.8, label=f"$w_{{EE}}$ = {w}")
ax.axvspan(t0, t1, color=P.fill("highlight"), alpha=0.5, lw=0)
ax.text(t1 + 0.02, 1.04, "stimulus", fontsize=8, color=P.muted())
ax.set_xlim(0, 1.4)
ax.set_ylim(0, 1.12)
ax.set_xlabel("Time / s")
ax.set_ylabel("Activity $E$")
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title("A  Activity outlasts the stimulus", loc="left", fontsize=10)

ws = np.linspace(0.6, 2.4, 37)
for g, c in ((1.0, P.edge("protein")), (2.0, P.edge("enzyme"))):
    d = [duration(*simulate(w, g=g)) for w in ws]
    bx.plot(ws, d, "o-", color=c, ms=3, lw=1.6, label=f"g = {g}")
bx.axhline(T - t1, color=P.muted(), lw=0.8, ls=":")
bx.text(0.65, T - t1 - 0.12, "persistent (end of run)", fontsize=8, color=P.muted(), va="top")
bx.set_xlabel("Recurrent excitation $w_{EE}$")
bx.set_ylabel("Afterdischarge duration / s")
bx.legend(frameon=False, fontsize=8, loc="center left")
bx.set_title("B  Duration grows with $w_{EE}$", loc="left", fontsize=10)
for x in (ax, bx):
    x.grid(True, alpha=0.3)
fig.tight_layout()
