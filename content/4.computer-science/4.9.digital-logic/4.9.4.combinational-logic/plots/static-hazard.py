"""Static-1 hazard in F = AB + A'C with B = C = 1. When A falls, the term AB
turns off one gate delay before A'C turns on (the inverter adds a delay), so F
drops to 0 briefly. The consensus term BC stays 1 and removes the glitch."""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 1001)
d = 1.0                      # one gate delay
t0 = 3.0                     # A falls at t0
A = (t < t0).astype(float)
nA = (t >= t0 + d).astype(float)          # inverter output
AB = (t < t0 + d).astype(float)           # AND gate, B = 1
nAC = (t >= t0 + 2 * d).astype(float)     # AND gate after the inverter, C = 1
F = np.maximum(AB, nAC)
F = np.concatenate([np.ones(int(d / (t[1] - t[0]))), F])[:t.size]   # OR gate delay
F2 = np.ones_like(t)                      # with the consensus term BC

rows = [("$A$", A), (r"$\overline{A}$", nA), ("$AB$", AB), (r"$\overline{A}C$", nAC),
        (r"$F = AB + \overline{A}C$", F), ("$F + BC$", F2)]
fig, axes = plt.subplots(len(rows), 1, figsize=(8, 5.4), sharex=True)
for ax, (name, y) in zip(axes, rows):
    color = "C3" if name.startswith("$F =") else "C0"
    ax.plot(t, y, color=color, lw=1.8, drawstyle="steps-post")
    ax.set_ylim(-0.3, 1.3)
    ax.set_yticks([])
    ax.set_ylabel(name, rotation=0, ha="right", va="center", fontsize=9)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    for k in range(4):
        ax.axvline(t0 + k * d, color="gray", lw=0.6, ls=":")
axes[4].annotate("glitch", xy=(t0 + 2.5 * d, 0.05), xytext=(t0 + 4 * d, 0.6),
                 arrowprops=dict(arrowstyle="->", lw=1), fontsize=9)
axes[-1].set_xlabel("time (gate delays)")
fig.tight_layout()
