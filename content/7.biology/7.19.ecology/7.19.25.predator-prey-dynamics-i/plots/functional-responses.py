"""Holling's three types of functional response (Section 25.4).

A: intake per predator f(N): type I aN (capped at 20), type II aN/(1 + ahN) with a = 0.5, h = 0.05
(asymptote 1/h = 20, half-saturation 1/(ah) = 40), type III bN^2/(1 + bhN^2) with b = 0.01, h = 0.05.
B: per capita risk of a prey individual, f(N)/N, for one predator: constant (type I), decreasing
(type II: inverse density dependence), humped (type III: density dependent at low N).
C: the time budget behind the disc equation: a simulated foraging bout at prey density N = 40,
with exponentially distributed search intervals (mean 1/(aN)) alternating with handling bouts h.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
a, h, b = 0.5, 0.05, 0.01
N = np.linspace(0.01, 200, 600)
f1 = np.minimum(a * N, 20)
f2 = a * N / (1 + a * h * N)
f3 = b * N**2 / (1 + b * h * N**2)
cols = [C.line("positive"), C.line("dna"), C.line("negative")]

fig = plt.figure(figsize=(13.5, 5.6))
gs = fig.add_gridspec(2, 2, height_ratios=[3, 1.1])
ax = fig.add_subplot(gs[0, 0])
for f, col, lab in zip([f1, f2, f3], cols, ["type I", "type II", "type III"]):
    ax.plot(N, f, color=col, lw=1.5, label=lab)
ax.axhline(1 / h, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
ax.text(150, 1 / h + 0.5, "1/h", fontsize=FS["tiny"], color=P.muted())
ax.legend(fontsize=FS["tiny"], frameon=False, loc="lower right")
C.style_axes(ax, "Prey density N", "Prey eaten per predator per day")
C.title(ax, "A  Functional responses")

ax = fig.add_subplot(gs[0, 1])
for f, col, lab in zip([f1, f2, f3], cols, ["type I", "type II", "type III"]):
    ax.plot(N, f / N, color=col, lw=1.5, label=lab)
ax.set_ylim(0, 0.55)
ax.legend(fontsize=FS["tiny"], frameon=False, loc="upper right")
C.style_axes(ax, "Prey density N", "Risk per prey, f(N)/N, per day")
C.title(ax, "B  Per capita predation risk")

ax = fig.add_subplot(gs[1, :])
rng = np.random.default_rng(3)
t, Nd, n_caught = 0.0, 40, 0
while t < 2.0:
    s = rng.exponential(1 / (a * Nd))
    ax.barh(0, min(s, 2 - t), left=t, height=0.5, color=P.light("dna"), edgecolor=P.edge("dna"), lw=0.6)
    t += s
    if t >= 2:
        break
    ax.barh(0, min(h, 2 - t), left=t, height=0.5, color=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.6)
    t += h
    n_caught += 1
ax.set_xlim(0, 2)
ax.set_yticks([])
ax.text(0.0, 0.42, "searching", fontsize=FS["tiny"], color=P.edge("dna"))
ax.text(0.25, 0.42, "handling (h per prey)", fontsize=FS["tiny"], color=P.edge("negative"))
ax.text(2.0, 0.42, f"{n_caught} prey in 2 days; disc equation predicts {2 * a * Nd / (1 + a * h * Nd):.1f}",
        fontsize=FS["tiny"], color=P.ink(), ha="right")
ax.set_ylim(-0.35, 0.6)
C.style_axes(ax, "Time (days)")
ax.spines["left"].set_visible(False)
C.title(ax, "C  Time budget of a searching predator (N = 40)")
fig.tight_layout()
