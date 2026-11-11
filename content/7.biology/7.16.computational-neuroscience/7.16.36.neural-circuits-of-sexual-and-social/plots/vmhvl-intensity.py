"""Schematic of behaviors evoked by graded optogenetic activation of VMHvl Esr1+ neurons in male mice.

Qualitative shape of Lee et al. 2014 (Nature): weak activation evokes investigation and mating behavior,
strong activation evokes attack. Curves are illustrative logistic functions, not data.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
x = np.linspace(0, 1, 300)


def sig(x, x0, k):
    return 1 / (1 + np.exp(-(x - x0) / k))


attack = sig(x, 0.62, 0.06)
mount = sig(x, 0.25, 0.05) * (1 - attack)
invest = sig(x, 0.08, 0.04) * (1 - sig(x, 0.3, 0.06)) * 0.8 + 0.05

fig, ax = plt.subplots(figsize=(7.5, 3.4))
ax.plot(x, invest, color=P.edge("neutral"), lw=2.2, label="social investigation")
ax.plot(x, mount, color=P.edge("dna"), lw=2.2, label="mating behavior")
ax.plot(x, attack, color=P.edge("negative"), lw=2.2, label="attack")
ax.set_xlabel("Strength of activation of VMHvl Esr1$^+$ neurons (light intensity, schematic)")
ax.set_ylabel("Probability of behavior")
ax.set_xticks([0, 0.5, 1])
ax.set_xticklabels(["none", "intermediate", "strong"])
ax.set_ylim(0, 1.05)
ax.grid(True, alpha=0.3)
ax.legend(frameon=False, fontsize=8.5, loc="center right")
fig.tight_layout()
