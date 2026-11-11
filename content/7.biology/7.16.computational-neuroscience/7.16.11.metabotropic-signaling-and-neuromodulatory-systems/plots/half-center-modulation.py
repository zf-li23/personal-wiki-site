"""Neuromodulation of a half-center oscillator (rate model with mutual inhibition and adaptation).

Two units with firing rates r1, r2 inhibit each other and adapt (Matsuoka-type oscillator):
tau dr_i/dt = -r_i + f(I_i - w r_j - g a_i),  tau_a da_i/dt = -a_i + r_i,
f(x) = max(x, 0) clipped at 1, tau = 20 ms, w = 2.
Control: I = 1, g = 2, tau_a = 400 ms -> alternation at about 1.2 Hz.
Modulator 1 (e.g. speeds adaptation, tau_a = 150 ms): the same circuit oscillates at about 2.6 Hz.
Modulator 2 (removes adaptation of unit 1, g1 = 0.3; drive to unit 1 raised to 1.2): alternation stops,
unit 1 fires tonically and suppresses unit 2.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
dt, T = 0.5, 3000.0
t = np.arange(0, T, dt)


def f(x):
    return np.clip(x, 0, 1)


def run(I1=1.0, I2=1.0, g1=2.0, g2=2.0, taua=400.0, w=2.0, tau=20.0):
    r = np.array([0.6, 0.0])
    a = np.array([0.0, 0.0])
    I = np.array([I1, I2])
    g = np.array([g1, g2])
    out = np.zeros((len(t), 2))
    for k in range(len(t)):
        inp = I - w * r[::-1] - g * a
        r = r + dt / tau * (-r + f(inp))
        a = a + dt / taua * (-a + r)
        out[k] = r
    return out


cases = [("Control", dict()),
         ("Modulator 1: faster adaptation ($\\tau_a$ 400 -> 150 ms)", dict(taua=150.0)),
         ("Modulator 2: unit 1 loses adaptation and gains drive", dict(g1=0.3, I1=1.2))]
fig, axs = plt.subplots(3, 1, figsize=(10, 5.6), sharex=True)
for ax, (title, kw) in zip(axs, cases):
    o = run(**kw)
    ax.plot(t / 1000, o[:, 0], color=P.edge("dna"), lw=1.8, label="unit 1")
    ax.plot(t / 1000, o[:, 1], color=P.edge("negative"), lw=1.8, label="unit 2")
    ax.set_ylim(-0.05, 1.1)
    ax.set_ylabel("Rate")
    ax.set_title(title, loc="left", fontsize=9.5)
    ax.grid(True, alpha=0.3)
axs[0].legend(frameon=False, fontsize=8, loc="upper right", ncol=2)
axs[-1].set_xlabel("Time / s")
fig.tight_layout()
