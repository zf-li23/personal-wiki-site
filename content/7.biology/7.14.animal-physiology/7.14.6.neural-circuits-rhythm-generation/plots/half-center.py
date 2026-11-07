"""A half-centre oscillator: two rate units with mutual inhibition and slow self-adaptation.

tau_x dx_A/dt = -x_A + F(I0 - w_I x_B - g a_A),  tau_a da_A/dt = -a_A + x_A  (and the same with A <-> B),
F(u) = max(0, u); I0 = 1 (tonic drive), w_I = 2, tau_x = 50 ms, tau_a = 0.6 s; A starts slightly ahead.
A: g = 2: the active half fatigues, releases the other, and the two alternate (like flexor and extensor).
B: period and peak-to-peak amplitude of x_A against the adaptation strength g. Without enough
adaptation (g below about 1.1) mutual inhibition alone gives a winner-take-all steady state.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P


def simulate(g, wI=2.0, I0=1.0, tx=0.05, ta=0.6, T=8.0, dt=1e-3):
    n = int(T / dt)
    s = np.zeros((n, 4))
    xa, xb, aa, ab = 0.1, 0.0, 0.0, 0.0
    for i in range(n):
        fa = max(0.0, I0 - wI * xb - g * aa)
        fb = max(0.0, I0 - wI * xa - g * ab)
        xa, xb, aa, ab = (xa + dt * (-xa + fa) / tx, xb + dt * (-xb + fb) / tx,
                          aa + dt * (-aa + xa) / ta, ab + dt * (-ab + xb) / ta)
        s[i] = xa, xb, aa, ab
    return np.arange(n) * dt, s


fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.5, 4.0), gridspec_kw={"width_ratios": [1.5, 1]})
t, s = simulate(2.0)
ax.plot(t, s[:, 0], color=P.edge("dna"), lw=2, label="$x_A$ (e.g. flexor half-centre)")
ax.plot(t, s[:, 1], color=P.edge("rna"), lw=2, label="$x_B$ (extensor half-centre)")
ax.plot(t, s[:, 2], color=P.edge("dna"), lw=1, ls="--", label="$a_A$ (adaptation of A)")
ax.set_xlim(0, 6)
ax.set_ylim(0, 1.25)
ax.set_xlabel("Time / s")
ax.set_ylabel("Activity (rate, arbitrary units)")
ax.legend(frameon=False, fontsize=8, ncol=3, loc="upper center")
ax.set_title("A  Alternation, g = 2", loc="left", fontsize=10)

gs = np.linspace(0, 6, 49)
per, amp = [], []
for g in gs:
    t, s = simulate(g)
    x = s[len(t) // 2:, 0]
    up = np.where((x[1:] > 0.05) & (x[:-1] <= 0.05))[0]
    per.append(np.diff(up).mean() * 1e-3 if len(up) > 1 else np.nan)
    amp.append(x.max() - x.min())
bx.plot(gs, per, "o-", color=P.edge("protein"), ms=3, lw=1.6, label="period")
bx.set_xlabel("Adaptation strength $g$")
bx.set_ylabel("Period / s", color=P.edge("protein"))
bx.set_ylim(0, 2.5)
cx = bx.twinx()
cx.plot(gs, amp, color=P.edge("enzyme"), lw=1.6, ls="--", label="amplitude")
cx.set_ylabel("Amplitude of $x_A$", color=P.edge("enzyme"))
cx.set_ylim(0, 1)
bx.axvspan(0, 1.1, color=P.fill("neutral"), alpha=0.25, lw=0)
bx.text(0.6, 2.25, "winner\ntakes all", ha="center", fontsize=8, color=P.muted())
bx.set_title("B  Rhythm needs adaptation", loc="left", fontsize=10)
for x in (ax, bx):
    x.grid(True, alpha=0.3)
fig.tight_layout()
