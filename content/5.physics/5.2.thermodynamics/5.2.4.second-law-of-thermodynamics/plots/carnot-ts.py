"""T-S diagrams: the Carnot cycle is a rectangle; an arbitrary reversible cycle lies between T_min and T_max."""

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

T1, T2, S1, S2 = 500, 300, 1.0, 2.0
ax1.fill_between([S1, S2], T2, T1, color="C0", alpha=0.15)
ax1.fill_between([S1, S2], 0, T2, color="C1", alpha=0.12)
ax1.plot([S1, S2, S2, S1, S1], [T1, T1, T2, T2, T1], color="C0", lw=1.8)
for (a, b), (c, d) in [((S1, T1), (S2, T1)), ((S2, T1), (S2, T2)), ((S2, T2), (S1, T2)), ((S1, T2), (S1, T1))]:
    ax1.annotate("", xy=((a + 3 * c) / 4, (b + 3 * d) / 4), xytext=((3 * a + c) / 4, (3 * b + d) / 4),
                 arrowprops=dict(arrowstyle="->", color="C0", lw=1.4))
ax1.annotate(r"net work $-W$", (1.32, 400), fontsize=10)
ax1.annotate(r"heat rejected $|Q_2| = T_2 \Delta S$", (1.05, 150), fontsize=10)
ax1.set_xlim(0.6, 2.4)
ax1.set_ylim(0, 600)
ax1.set_xlabel("S (arbitrary units)")
ax1.set_ylabel("T / K")
ax1.set_title("Carnot cycle")

t = np.linspace(0, 2 * np.pi, 400)
S = 1.5 + 0.5 * np.cos(t)
T = 400 + 80 * np.sin(t) + 25 * np.sin(2 * t)
ax2.plot(S, T, color="C0", lw=1.8)
ax2.fill(S, T, color="C0", alpha=0.15)
ax2.axhline(T.max(), color="C3", ls="--", lw=1)
ax2.axhline(T.min(), color="C2", ls="--", lw=1)
ax2.annotate(r"$T_{\max}$", (0.7, T.max() + 8), color="C3", fontsize=10)
ax2.annotate(r"$T_{\min}$", (0.7, T.min() - 25), color="C2", fontsize=10)
ax2.set_xlim(0.6, 2.4)
ax2.set_ylim(0, 600)
ax2.set_xlabel("S (arbitrary units)")
ax2.set_ylabel("T / K")
ax2.set_title("Any reversible cycle fits inside a Carnot rectangle")
fig.tight_layout()
