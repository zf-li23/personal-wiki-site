"""Habituation and spontaneous recovery with two time scales (rate sensitivity).

Each stimulus k at time t_k increments two traces that decay exponentially:
x_f (tau_f = 20 s) by 1 and x_s (tau_s = 600 s) by the output of the fast stage, max(1 - 0.5 x_f, 0)
(a cascade, after Staddon and Higa 1996). Response R = max(1 - 0.5 x_f - ws x_s, 0), measured before
the increment. Training: 15 stimuli at interstimulus interval 5 s or 30 s, then a test after a 10-min pause.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
tau_f, tau_s, wf, ws = 20.0, 600.0, 0.5, 0.12


def series(isi, n=15, pause=600.0):
    times = list(np.arange(n) * isi) + [(n - 1) * isi + pause]
    xf = xs = 0.0
    last = 0.0
    R = []
    for tk in times:
        xf *= np.exp(-(tk - last) / tau_f)
        xs *= np.exp(-(tk - last) / tau_s)
        R.append(max(1 - wf * xf - ws * xs, 0.0))
        o1 = max(1 - wf * xf, 0.0)
        xf += 1.0
        xs += o1
        last = tk
    return np.array(R)


fig, ax = plt.subplots(figsize=(7.5, 3.5))
for isi, tok in [(5.0, "negative"), (30.0, "dna")]:
    R = series(isi)
    ax.plot(np.arange(1, 16), R[:15], "o-", color=P.edge(tok), ms=4, lw=1.8, label=f"interstimulus interval {isi:.0f} s")
    ax.plot([15, 18], [R[14], R[15]], ":", color=P.edge(tok), lw=1.2)
    ax.plot([18], [R[15]], "s", color=P.edge(tok), ms=7)
ax.text(18, 1.02, "test after\n10-min pause", ha="center", fontsize=8.5, color=P.muted())
ax.set_xticks(list(range(1, 16, 2)) + [18])
ax.set_xticklabels([str(i) for i in range(1, 16, 2)] + ["test"])
ax.set_xlabel("Stimulus number")
ax.set_ylabel("Response amplitude (rel.)")
ax.set_ylim(0, 1.15)
ax.legend(frameon=False, fontsize=8, loc="lower left")
ax.grid(True, alpha=0.3)
fig.tight_layout()
