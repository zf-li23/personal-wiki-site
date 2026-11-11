"""Action selection by the basal ganglia: a reduced multi-channel rate model (after Gurney, Prescott and Redgrave 2001).

N = 5 action channels with cortical salience c_i; F(u) = max(u, 0); dopamine level d.
Direct-pathway (D1) MSNs:   x1_i = F((1 + d) c_i - theta)
Indirect-pathway (D2) MSNs: x2_i = F((1 - d) c_i - theta)
STN (GPe folded into the indirect pathway, which disinhibits STN): s_i = F(0.2 + 0.5 c_i + 0.6 x2_i)
Output GPi/SNr: o_i = F(0.6 + 0.8 mean(s) + 0.3 s_i - 1.5 x1_i)  (diffuse STN excitation, focused D1 inhibition)
theta = 0.35. Outputs are normalized to the resting output (all c_i = 0.1, d = 0.2).
Salience c = [0.3, 0.7, 0.45, 0.2, 0.1]; d = -0.4 (depleted), 0.2 (normal), 0.6 (excess).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
c = np.array([0.2, 0.6, 0.35, 0.1, 0.0]) + 0.1
N = len(c)


def F(u):
    return np.maximum(u, 0.0)


def steady(c, d, th=0.35):
    x1 = F((1 + d) * c - th)
    x2 = F((1 - d) * c - th)
    stn = F(0.2 + 0.5 * c + 0.6 * x2)
    return F(0.6 + 0.8 * stn.mean() + 0.3 * stn - 1.5 * x1)


rest = steady(np.full(N, 0.1), 0.2).mean()
fig, axs = plt.subplots(1, 2, figsize=(10, 3.6), gridspec_kw=dict(width_ratios=[1, 1.4]))
axs[0].bar(np.arange(1, N + 1), c, color=P.fill("neutral"), edgecolor=P.edge("neutral"))
axs[0].set_xlabel("Action channel")
axs[0].set_ylabel("Cortical salience $c_i$")
axs[0].set_title("A  Input", loc="left", fontsize=10)
w = 0.26
for k, (d, lab, tok) in enumerate([(-0.4, "dopamine depleted ($d = -0.4$)", "neutral"),
                                   (0.2, "normal ($d = 0.2$)", "dna"),
                                   (0.6, "excess ($d = 0.6$)", "negative")]):
    gpi = steady(c, d)
    axs[1].bar(np.arange(1, N + 1) + (k - 1) * w, gpi / rest, w, color=P.fill(tok), edgecolor=P.edge(tok), label=lab)
axs[1].axhline(1, color=P.muted(), lw=0.8, ls=":")
axs[1].text(5.45, 1.03, "rest", fontsize=8, color=P.muted(), ha="right")
axs[1].set_xlabel("Action channel")
axs[1].set_ylabel("GPi/SNr output (rel. to rest)")
axs[1].set_title("B  Output: low = selected (disinhibited)", loc="left", fontsize=10)
axs[1].legend(frameon=False, fontsize=7.5, loc="upper center", ncol=3)
axs[1].set_ylim(0, 1.7)
for a in axs:
    a.grid(True, alpha=0.3, axis="y")
fig.tight_layout()
