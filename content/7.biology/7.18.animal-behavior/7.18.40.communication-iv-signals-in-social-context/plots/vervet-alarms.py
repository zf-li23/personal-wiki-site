"""Schematic call-by-response matrix for vervet alarm call playbacks (illustrative values, after Seyfarth,
Cheney and Marler 1980)."""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
calls = ["leopard alarm", "eagle alarm", "snake alarm"]
resp = ["run into trees", "look up,\nrun into bushes", "stand up,\nlook down"]
M = np.array([[0.85, 0.15, 0.10], [0.15, 0.80, 0.10], [0.10, 0.10, 0.85]])
fig, ax = plt.subplots(figsize=(6.4, 3.6))
im = ax.imshow(M, cmap="Blues", vmin=0, vmax=1)
ax.set_xticks(range(3)); ax.set_xticklabels(resp, fontsize=8.5)
ax.set_yticks(range(3)); ax.set_yticklabels(calls, fontsize=8.5)
ax.set_xlabel("Response of listeners"); ax.set_ylabel("Call played back")
for i in range(3):
    for j in range(3):
        ax.text(j, i, "high" if M[i, j] > 0.5 else "low", ha="center", va="center", fontsize=8,
                color="white" if M[i, j] > 0.5 else P.on_fill())
cb = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.03)
cb.set_label("Relative frequency (schematic)", fontsize=8)
fig.tight_layout()
