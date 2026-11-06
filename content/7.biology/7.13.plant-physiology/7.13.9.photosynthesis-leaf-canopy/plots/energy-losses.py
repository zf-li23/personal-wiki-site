"""Where the energy of sunlight goes: the theoretical maximum efficiency of converting solar energy into
biomass, after Zhu, Long and Ort (2008), for 30 C and 380 umol mol-1 CO2.

Starting from 100 % of the solar energy intercepted by a leaf canopy, successive losses: radiation outside
400-700 nm (51.3 %), reflection and transmission (4.9 %), photochemical inefficiency (thermal relaxation of
photons above the reaction-centre energy, 6.6 %), carbohydrate synthesis (24.6 % in C3, 28.8 % in C4, the
latter including the C4 cycle), photorespiration (6.1 % in C3, none in C4) and respiration (1.9 % and 2.5 %).
The remainder is the maximum conversion efficiency: 4.6 % for C3 and 6.0 % for C4. Bars show the energy left
after each step (waterfall).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
steps = ["Total\nsolar", "Outside\nPAR", "Reflected,\ntransmitted", "Photochem.\ninefficiency",
         "Carbohydrate\nsynthesis", "Photo-\nrespiration", "Respiration", "Biomass"]
loss = {"C3": [51.3, 4.9, 6.6, 24.6, 6.1, 1.9], "C4": [51.3, 4.9, 6.6, 28.8, 0.0, 2.5]}

fig, axs = plt.subplots(1, 2, figsize=(13, 4.6), sharey=True)
for ax, (name, ls) in zip(axs, loss.items()):
    left = 100.0
    x = np.arange(len(steps))
    ax.bar(0, 100, color=P.fill("highlight"), edgecolor=P.edge("highlight"))
    for i, l in enumerate(ls, start=1):
        ax.bar(i, l, bottom=left - l, color=P.fill("negative"), edgecolor=P.edge("negative"))
        ax.text(i, left + 1.5, f"−{l:.1f}", ha="center", fontsize=8, color=P.ink())
        left -= l
    ax.bar(len(steps) - 1, left, color=P.fill("plant"), edgecolor=P.edge("plant"))
    ax.text(len(steps) - 1, left + 1.5, f"{left:.1f} %", ha="center", fontsize=9, weight="bold", color=P.ink())
    ax.set_xticks(x)
    ax.set_xticklabels(steps, fontsize=7, rotation=0)
    ax.set_ylim(0, 108)
    ax.set_title(f"{'A' if name == 'C3' else 'B'}  {name} crop", loc="left", fontsize=10)
    ax.grid(True, axis="y", alpha=0.3)
axs[0].set_ylabel("Energy remaining / % of incident solar energy")
fig.tight_layout()
