"""Tsodyks-Markram model of short-term plasticity: responses to regular spike trains.

Between spikes u relaxes to 0 with tau_f and x recovers to 1 with tau_d; at a spike u jumps by
U (1 - u), then a fraction u x of the resources is released (the response) and x drops by u x.
Depressing synapse: U = 0.5, tau_d = 800 ms, tau_f = 20 ms.
Facilitating synapse: U = 0.1, tau_d = 200 ms, tau_f = 1500 ms.
Each panel shows the response amplitude u x per spike (bars, normalized to the first response of
the depressing synapse) for 10 spikes at 20 Hz and at 50 Hz, followed by a test spike 500 ms later
(recovery), and the PSC trace (exponential, 3 ms) underneath.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P


def train(U, td, tf, times):
    u, x, last, out = 0.0, 1.0, None, []
    for ts in times:
        if last is not None:
            d = ts - last
            u = u * np.exp(-d / tf)
            x = 1 + (x - 1) * np.exp(-d / td)
        u = u + U * (1 - u)
        r = u * x
        x -= r
        out.append(r)
        last = ts
    return np.array(out)


syn = [("Depressing (U = 0.5, $\\tau_d$ = 800 ms, $\\tau_f$ = 20 ms)", 0.5, 800.0, 20.0, P.edge("negative")),
       ("Facilitating (U = 0.1, $\\tau_d$ = 200 ms, $\\tau_f$ = 1500 ms)", 0.1, 200.0, 1500.0, P.edge("dna"))]
fig, axs = plt.subplots(2, 2, figsize=(11.5, 5.4), sharey=True)
ref = train(0.5, 800, 20, [0.0])[0]
for i, (nm, U, td, tf, c) in enumerate(syn):
    for j, f in enumerate((20.0, 50.0)):
        ax = axs[i, j]
        times = list(np.arange(10) * 1000 / f + 20) + [20 + 9 * 1000 / f + 500]
        r = train(U, td, tf, times) / ref
        tt = np.arange(0, times[-1] + 60, 0.1)
        tr = np.zeros_like(tt)
        for ts, a in zip(times, r):
            s = tt - ts
            tr += a * np.exp(-np.clip(s, 0, None) / 3.0) * (s >= 0)
        ax.plot(tt, tr, color=c, lw=1.2)
        ax.plot(times, r, "o", color=c, ms=4)
        ax.set_title(f"{nm.split(' (')[0]}, {f:.0f} Hz", loc="left", fontsize=9.5)
        ax.grid(True, alpha=0.3)
        if j == 0:
            ax.set_ylabel("Response / first (depr.)")
        if i == 1:
            ax.set_xlabel("Time / ms")
        ax.text(times[-1], r[-1] + 0.08, "test +500 ms", fontsize=7, ha="center", color=P.muted())
fig.text(0.5, 0.995, "Depressing: $U$ = 0.5, $\\tau_{\\mathrm{d}}$ = 800 ms, $\\tau_{\\mathrm{f}}$ = 20 ms;   facilitating: $U$ = 0.1, $\\tau_{\\mathrm{d}}$ = 200 ms, $\\tau_{\\mathrm{f}}$ = 1500 ms",
         ha="center", va="top", fontsize=8, color=P.muted())
fig.tight_layout(rect=(0, 0, 1, 0.96))
