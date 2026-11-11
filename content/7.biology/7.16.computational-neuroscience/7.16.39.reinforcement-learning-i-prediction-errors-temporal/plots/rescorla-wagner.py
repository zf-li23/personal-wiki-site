"""Rescorla-Wagner rule: acquisition, extinction and blocking (Definition 39.1.1).

V_i <- V_i + alpha_i beta (lambda - sum_j V_j) for every CS i present; alpha beta = 0.2, lambda = 1 with US.
A: acquisition (30 trials A+) then extinction (30 trials A-).
B: blocking. Blocking group: 20 trials A+, then 20 trials AX+. Control group: 20 trials B+, then 20 AX+.
Bars: V_X after phase 2.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
ab = 0.2


def train(V, present, lam, n, record=None):
    out = []
    for _ in range(n):
        pred = sum(V[c] for c in present)
        for c in present:
            V[c] += ab * (lam - pred)
        out.append(dict(V))
    return out


fig, axs = plt.subplots(1, 2, figsize=(10, 3.6), gridspec_kw=dict(width_ratios=[1.6, 1]))
V = dict(A=0.0)
h = [dict(V)] + train(V, ["A"], 1.0, 30) + train(V, ["A"], 0.0, 30)
axs[0].plot([x["A"] for x in h], "o-", color=P.edge("dna"), ms=3, lw=1.6)
axs[0].axvspan(0, 30, color=P.light("highlight"), zorder=0)
axs[0].text(15, 1.06, "A + US", ha="center", fontsize=8.5, color=P.muted())
axs[0].text(45, 1.06, "A alone", ha="center", fontsize=8.5, color=P.muted())
axs[0].set_ylim(-0.03, 1.15)
axs[0].set_xlabel("Trial")
axs[0].set_ylabel("Associative strength $V_A$")
axs[0].set_title("A  Acquisition and extinction", loc="left", fontsize=10)

Vb = dict(A=0.0, X=0.0)
train(Vb, ["A"], 1.0, 20)
train(Vb, ["A", "X"], 1.0, 20)
Vc = dict(A=0.0, B=0.0, X=0.0)
train(Vc, ["B"], 1.0, 20)
train(Vc, ["A", "X"], 1.0, 20)
axs[1].bar([0, 1], [Vb["X"], Vc["X"]], 0.55, color=[P.fill("negative"), P.fill("dna")],
           edgecolor=[P.edge("negative"), P.edge("dna")])
axs[1].set_xticks([0, 1])
axs[1].set_xticklabels(["Blocking\n(A+ then AX+)", "Control\n(B+ then AX+)"])
axs[1].set_ylabel("$V_X$ after phase 2")
axs[1].set_ylim(0, 0.6)
axs[1].set_title("B  Blocking", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
