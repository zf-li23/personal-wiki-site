"""Paired-pulse ratio as a function of release probability (depletion plus residual-Ca2+ facilitation).

A site releases with probability p on the first spike. Between spikes the vesicle pool recovers
with time constant tau_rec = 500 ms and the release probability is raised by facilitation,
p2 = p + f (1 - p) exp(-dt / tau_F), with f = 0.3 and tau_F = 50 ms. The expected ratio of the
second to the first response is PPR = x2 p2 / p, where x2 = 1 - p exp(-dt / tau_rec) is the
fraction of the pool available at the second spike.
A: PPR against p for intervals of 20, 50 and 200 ms: low-p synapses facilitate, high-p synapses
depress, and the crossover moves with the interval.
B: lowering extracellular [Ca2+] converts a depressing synapse into a facilitating one. The first
release probability follows p = p_max c^4 / (c^4 + K^4) with p_max = 0.9 and K = 1.5 mM
(dt = 20 ms). The inset shows simulated responses (arbitrary units) at 0.75 and 2.5 mM.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
f, tauF, taurec = 0.3, 50.0, 500.0


def ppr(p, dt):
    p2 = p + f * (1 - p) * np.exp(-dt / tauF)
    x2 = 1 - p * np.exp(-dt / taurec)
    return x2 * p2 / p


fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9))
ax = axs[0]
p = np.linspace(0.02, 0.95, 300)
for dt, c in zip((20, 50, 200), (P.edge("negative"), P.edge("protein"), P.edge("dna"))):
    ax.plot(p, ppr(p, dt), color=c, lw=2.0, label=f"interval {dt} ms")
ax.axhline(1, color=P.muted(), lw=1, ls=":")
ax.text(0.05, 1.04, "facilitation", fontsize=8, color=P.ink())
ax.text(0.7, 0.86, "depression", fontsize=8, color=P.ink())
ax.set_xscale("log")
ax.set_xticks([0.02, 0.05, 0.1, 0.2, 0.5, 0.9])
ax.set_xticklabels(["0.02", "0.05", "0.1", "0.2", "0.5", "0.9"])
ax.set_xlabel("Release probability of the first spike, p")
ax.set_ylabel("Paired-pulse ratio")
ax.set_title("A  PPR falls as p rises", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper right")

ax = axs[1]
c = np.linspace(0.4, 4.0, 300)
K, pmax = 1.5, 0.9
pc = pmax * c**4 / (c**4 + K**4)
ax.plot(c, ppr(pc, 20), color=P.edge("ca"), lw=2.2)
ax.axhline(1, color=P.muted(), lw=1, ls=":")
ax.set_xlabel("Extracellular [Ca$^{2+}$] / mM")
ax.set_ylabel("Paired-pulse ratio (interval 20 ms)")
ax.set_title("B  Ca$^{2+}$ sets the sign", loc="left", fontsize=10)
ins = ax.inset_axes([0.55, 0.5, 0.42, 0.42])
for cc, col, off in ((0.75, P.edge("dna"), 0.0), (2.5, P.edge("negative"), 0.0)):
    p1 = pmax * cc**4 / (cc**4 + K**4)
    amps = np.array([p1, p1 * ppr(p1, 20)])
    amps = amps / amps[0]
    tt = np.linspace(0, 60, 600)
    tr = np.zeros_like(tt)
    for t0, a in zip((5, 25), amps):
        s = np.clip(tt - t0, 0, None)
        tr += a * (np.exp(-s / 6) - np.exp(-s / 1)) * (tt >= t0)
    ins.plot(tt, tr, color=col, lw=1.4, label=f"{cc} mM")
ins.set_xticks([])
ins.set_yticks([])
ins.legend(frameon=False, fontsize=7, loc="upper right")
ins.set_title("normalized to the first", fontsize=7)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
