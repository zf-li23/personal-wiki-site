"""First and second pain: arrival times of A-delta and C fibre volleys.

A: conduction time t = L / v against path length L for A-delta fibres (6-30 m/s, band; line at
15 m/s) and C fibres (0.5-2 m/s; line at 1 m/s). Marks: about 0.7 m from the hand and 1.0 m from
the foot to the spinal cord.
B: volley reaching the spinal cord after a brief noxious stimulus to the foot (L = 1.0 m):
1000 A-delta fibres with log-normal velocities (median 15 m/s) and 3000 C fibres (median 1 m/s);
histogram of arrival times (10-ms bins; counts per fibre type normalised to the peak).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.0))

L = np.linspace(0.05, 2.0, 200)
ad, cc = P.edge("dna"), P.edge("rna")
ax.fill_between(L, L / 30, L / 6, color=ad, alpha=0.25, lw=0)
ax.plot(L, L / 15, color=ad, lw=2, label=r"A$\delta$ (6-30 m/s)")
ax.fill_between(L, L / 2, L / 0.5, color=cc, alpha=0.25, lw=0)
ax.plot(L, L / 1, color=cc, lw=2, label="C (0.5-2 m/s)")
for x, name in ((0.7, "hand"), (1.0, "foot")):
    ax.axvline(x, color=P.muted(), lw=0.7, ls=":")
    ax.text(x + 0.02, 3.0, name, fontsize=8, color=P.muted())
ax.set_yscale("log")
ax.set_ylim(1e-3, 5)
ax.set_xlim(0, 2)
ax.set_xlabel("Path length to the spinal cord / m")
ax.set_ylabel("Conduction time / s")
ax.legend(frameon=False, fontsize=8, loc="lower right")
ax.set_title("A  Conduction time grows with distance", loc="left", fontsize=10)

va = np.exp(rng.normal(np.log(15), 0.35, 1000))
vc = np.exp(rng.normal(np.log(1.0), 0.3, 3000))
bins = np.arange(0, 3.0, 0.01)
for v, c, lab in ((va, ad, r"A$\delta$ volley: first pain"), (vc, cc, "C volley: second pain")):
    h, e = np.histogram(1.0 / v, bins=bins)
    bx.step(e[:-1], h / h.max(), where="post", color=c, lw=1.6, label=lab)
bx.set_xlim(0, 3)
bx.set_ylim(0, 1.15)
bx.set_xlabel("Time after stimulus to the foot / s")
bx.set_ylabel("Arrivals (normalised)")
bx.legend(frameon=False, fontsize=8, loc="upper right")
bx.set_title("B  Two volleys, two pains", loc="left", fontsize=10)
for a in (ax, bx):
    a.grid(True, alpha=0.3)
fig.tight_layout()
