"""Logistic equation P' = k P (1 - P / K) with k = 1, K = 1: direction field and solutions."""

import numpy as np
import matplotlib.pyplot as plt

k, K = 1.0, 1.0
ts = np.linspace(0, 8, 23)
ps = np.linspace(0, 1.6, 17)
T, P = np.meshgrid(ts, ps)
S = k * P * (1 - P / K)
L = np.sqrt(1 + S**2)

fig, ax = plt.subplots(figsize=(7.5, 4.8))
ax.quiver(T, P, 1 / L, S / L, angles="xy", headwidth=0, headlength=0, headaxislength=0,
          pivot="middle", scale=40, width=0.003, color="0.6")
t = np.linspace(0, 8, 400)
for P0 in [0.02, 0.08, 0.25, 0.5, 0.75, 1.3, 1.6]:
    A = (K - P0) / P0
    ax.plot(t, K / (1 + A * np.exp(-k * t)), color="C0", lw=1.6)
ax.axhline(K, color="C3", lw=2, label="equilibrium P = K")
ax.axhline(0, color="C2", lw=2, label="equilibrium P = 0")
ax.axhline(K / 2, color="0.4", lw=1, ls="--", label="P = K/2 (fastest growth)")
ax.set_xlim(0, 8)
ax.set_ylim(-0.05, 1.65)
ax.set_xlabel("t")
ax.set_ylabel("P")
ax.set_title("Logistic equation P' = kP(1 - P/K), k = 1, K = 1")
ax.legend(loc="lower right", fontsize=9)
fig.tight_layout()
