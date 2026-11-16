"""The logistic equation dN/dt = r N (1 - N/K) (Section 10.2), r = 1, K = 100.

A: growth rate dN/dt (left axis) and per capita growth rate (right axis) against N; arrows on the N axis
show the direction of change; maximum rK/4 at N = K/2.
B: solutions N(t) = K / (1 + exp(a - r t)) from N0 = 2, 20, 60, 150; the five conventional phases of the
S-shaped curve from N0 = 2 are separated at N = K(3 - sqrt 3)/6, K/2 and K(3 + sqrt 3)/6, where the
second derivative is extreme or zero, and at 0.99 K.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
r, K = 1.0, 100.0

fig, axes = plt.subplots(1, 2, figsize=(11.0, 3.9))
ax = axes[0]
N = np.linspace(0, 120, 400)
ax.plot(N, r * N * (1 - N / K), color=C.line("dna"), lw=2, label="dN/dt")
ax.axhline(0, color=P.muted(), lw=0.7)
for x0, x1 in ((15, 35), (65, 85)):
    ax.annotate("", (x1, 0), (x0, 0), arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=1.2))
ax.annotate("", (103, 0), (117, 0), arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=1.2))
ax.plot([0], [0], "o", ms=7, mfc=P.surface(), mec=P.ink())
ax.plot([K], [0], "o", ms=7, color=P.ink())
ax.text(1, -3.2, "N = 0\nunstable", fontsize=FS["tiny"], color=P.muted(), va="top")
ax.text(K, -3.2, "N = K\nstable", fontsize=FS["tiny"], color=P.muted(), va="top", ha="center")
ax.plot([K / 2, K / 2], [0, r * K / 4], color=P.muted(), lw=0.7, ls=(0, (3, 2)))
ax.text(K / 2 + 2, r * K / 4 + 0.6, "maximum rK/4 at K/2", fontsize=FS["tiny"], color=P.muted())
ax.set_ylim(-12, 30)
C.style_axes(ax, "population size N", "dN/dt")
ax2 = ax.twinx()
ax2.plot(N, r * (1 - N / K), color=C.line("rna"), lw=1.6, ls=(0, (4, 2)))
ax2.set_ylim(-0.4, 1.0)
C.style_axes(ax2, None, "per capita rate (1/N) dN/dt")
ax2.spines["right"].set_visible(True)
ax2.spines["right"].set_color(P.muted())
ax2.yaxis.label.set_color(C.line("rna"))
C.title(ax, "A  Rate of growth against density")

ax = axes[1]
t = np.linspace(0, 12, 500)
for N0, col in ((2, C.line("dna")), (20, C.line("positive")), (60, P.muted()), (150, C.line("rna"))):
    sol = K / (1 + (K - N0) / N0 * np.exp(-r * t))
    ax.plot(t, sol, color=col, lw=2 if N0 == 2 else 1.3, label=f"N₀ = {N0}")
a = np.log((K - 2) / 2)
levels = [K * (3 - np.sqrt(3)) / 6, K / 2, K * (3 + np.sqrt(3)) / 6, 0.99 * K]
tb = [(a - np.log(K / L - 1)) / r for L in levels]
edges = [0] + tb + [12]
names = ["lag", "acceleration", "inflection", "deceleration", "saturation"]
for i in range(5):
    lo, hi = edges[i], edges[i + 1]
    if i == 2:
        lo, hi = tb[1] - 0.12, tb[1] + 0.12
    ax.axvspan(lo, hi, color=P.fill("highlight") if i % 2 == 0 else P.fill("neutral"), alpha=0.35, lw=0)
    xm = (edges[i] + edges[i + 1]) / 2 if i != 2 else tb[1]
    ax.text(xm, 162, names[i], fontsize=FS["tiny"], color=P.ink(), ha="center", rotation=90 if i in (1, 2, 3) else 0,
            va="top")
ax.axhline(K, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
ax.axhline(K / 2, color=P.muted(), lw=0.5, ls=(0, (1, 2)))
ax.set_ylim(0, 165)
ax.set_xlim(0, 12)
C.style_axes(ax, "time (units of 1/r)", "N")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
C.title(ax, "B  Solutions and the phases of the S curve")
fig.tight_layout()
