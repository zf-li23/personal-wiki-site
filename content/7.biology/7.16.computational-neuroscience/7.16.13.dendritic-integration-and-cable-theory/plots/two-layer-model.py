"""The two-layer model of a neuron: dendritic branches as sigmoidal subunits (Poirazi and Mel).

Each of 8 branches sums its synaptic inputs linearly and passes the sum u through a sigmoid
y = 1 / (1 + exp(-(u - theta) / s)) with theta = 10 inputs and s = 1.5 (an NMDA-spike-like
threshold); the soma adds the branch outputs. Inputs are synapses of unit weight.
A: one branch: measured output (normalized sigmoid, solid) against the number of co-active
   synapses, compared with the linear sum expected from a single input (dashed): supralinear
   above threshold, saturating at high drive.
B: total output (sum of branch outputs, in units of branch maxima) when N synapses are active,
   if they are clustered (branches filled one after another) or scattered (spread evenly over
   the 8 branches). For a given N the clustered arrangement is more effective whenever it can
   push branches above threshold; scattered inputs are summed almost linearly and weakly.
C: the same cell as a feature detector: 20 synapses, either 20 on one branch or two groups of 10
   on two branches versus 20 spread over eight branches (2 or 3 per branch). Bars: output.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
theta, s, B = 10.0, 1.5, 8


def sig(u):
    return 1.0 / (1.0 + np.exp(-(u - theta) / s))


def out(counts):
    return sum(sig(c) - sig(0.0) for c in counts)


fig, axs = plt.subplots(1, 3, figsize=(12.5, 3.8), gridspec_kw=dict(width_ratios=[1, 1, 0.8]))
ax = axs[0]
u = np.linspace(0, 25, 300)
y = sig(u) - sig(0.0)
ax.plot(u, y, color=P.edge("positive"), lw=2.2, label="branch output")
ax.plot(u, u * (sig(1) - sig(0)), color=P.muted(), lw=1.2, ls="--", label="linear sum of single inputs")
ax.set_xlabel("Co-active synapses on one branch")
ax.set_ylabel("Branch output")
ax.set_ylim(0, 1.15)
ax.set_title("A  Branch nonlinearity", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper left")

ax = axs[1]
N = np.arange(0, 65)
clustered, scattered = [], []
for n in N:
    c = np.zeros(B, int)
    k = n
    for b in range(B):
        c[b] = min(k, 20)
        k -= c[b]
        if k <= 0:
            break
    clustered.append(out(c))
    sc = np.full(B, n // B)
    sc[: n % B] += 1
    scattered.append(out(sc))
ax.plot(N, clustered, color=P.edge("positive"), lw=2.2, label="clustered")
ax.plot(N, scattered, color=P.edge("negative"), lw=2.2, label="scattered")
ax.set_xlabel("Active synapses $N$")
ax.set_ylabel("Somatic drive (sum of branch outputs)")
ax.set_title("B  Clustered vs scattered", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper left")

ax = axs[2]
cases = [("20 on\n1 branch", [20]), ("10 + 10 on\n2 branches", [10, 10]), ("2-3 on\n8 branches", [3, 3, 3, 3, 2, 2, 2, 2])]
vals = [out(c) for _, c in cases]
ax.bar(range(3), vals, color=[P.fill("positive"), P.fill("protein"), P.fill("negative")],
       edgecolor=[P.edge("positive"), P.edge("protein"), P.edge("negative")])
ax.set_xticks(range(3))
ax.set_xticklabels([c[0] for c in cases], fontsize=8)
ax.set_ylabel("Somatic drive")
ax.set_title("C  20 synapses, three layouts", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3, axis="y")
fig.tight_layout()
