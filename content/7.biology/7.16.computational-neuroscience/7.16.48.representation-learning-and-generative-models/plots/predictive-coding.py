"""Rao-Ballard predictive coding in a two-level linear model, and end-stopping of error units.

Input x (15 pixels) is a bar of length L segments centred on the middle; level 1 has 5 units,
each predicting a 3-pixel segment (columns of U, unit gain); level 2 has one "line" unit whose
top-down prediction is the same for all five level-1 units (U2 = 1).
Generative model: x = U r1 + noise (variance s0), r1 = U2 r2 + noise (variance s1),
r2 ~ N(0, sp). Inference is gradient descent on the prediction errors:
  tau dr1/dt = U^T e0 / s0 - e1 / s1,   e0 = x - U r1,
  tau dr2/dt = U2^T e1 / s1 - r2 / sp,  e1 = r1 - U2 r2,
which settles at the MAP estimate. The level-1 error unit e1 of the centre segment is the
"extra-classical" response: it is large for a short bar and suppressed for a long bar that the
higher level can explain (end-stopping).
A: time course of the centre representation r1 and error e1 for bars of length 1 and 5.
B: steady-state centre responses against bar length (classical receptive field = 1 segment).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
nseg, w = 5, 3
U = np.zeros((nseg * w, nseg))
for j in range(nseg):
    U[j * w:(j + 1) * w, j] = 1.0
U2 = np.ones((nseg, 1))
s0, s1, sp = 1.0, 0.15, 4.0
tau, dt, T = 10.0, 0.05, 40.0


def bar(L):
    x = np.zeros(nseg * w)
    c = nseg // 2
    for j in range(c - (L - 1) // 2, c + L // 2 + 1):
        x[j * w:(j + 1) * w] = 1.0
    return x


def run(x):
    r1 = np.zeros(nseg)
    r2 = np.zeros(1)
    n = int(T / dt)
    out = np.zeros((n, 3))
    for k in range(n):
        e0 = x - U @ r1
        e1 = r1 - U2 @ r2
        r1 = r1 + dt / tau * (U.T @ e0 / s0 - e1 / s1)
        r2 = r2 + dt / tau * (U2.T @ e1 / s1 - r2 / sp)
        out[k] = r1[nseg // 2], e1[nseg // 2], r2[0]
    return out


t = np.arange(int(T / dt)) * dt
fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9))
ax = axs[0]
for L, ls in ((1, "-"), (5, "--")):
    o = run(bar(L))
    ax.plot(t, o[:, 0], color=P.edge("dna"), ls=ls, lw=1.8, label=f"$r_1$ (centre), length {L}")
    ax.plot(t, o[:, 1], color=P.edge("negative"), ls=ls, lw=1.8, label=f"error $e_1$ (centre), length {L}")
ax.set_xlabel("Time / ms")
ax.set_ylabel("Activity (a.u.)")
ax.set_ylim(-0.05, 1.35)
ax.legend(frameon=False, fontsize=7.5, loc="upper right", ncol=2)
ax.set_title("A  Inference dynamics", loc="left", fontsize=10)

ax = axs[1]
Ls = [1, 2, 3, 4, 5]
res = np.array([run(bar(L))[-1] for L in Ls])
ax.plot(Ls, res[:, 0], "o-", color=P.edge("dna"), lw=1.8, label="representation $r_1$ (centre)")
ax.plot(Ls, res[:, 1], "s-", color=P.edge("negative"), lw=1.8, label="error unit $e_1$ (centre)")
ax.plot(Ls, res[:, 2], "^-", color=P.edge("protein"), lw=1.8, label="level-2 'line' unit $r_2$")
ax.axhline(0, color=P.muted(), lw=0.7)
ax.set_xticks(Ls)
ax.set_xlabel("Bar length / segments")
ax.set_ylabel("Steady-state activity (a.u.)")
ax.legend(frameon=False, fontsize=7.5, loc="center right")
ax.set_title("B  End-stopping of error units", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
