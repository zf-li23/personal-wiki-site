"""Under-, exact and overcompensating density dependence (Section 11.2.2).

Survivors A from an initial number B under the Maynard Smith-Slatkin mortality function
A = B / (1 + (a B)^b), a = 0.01, for b = 0.5 (undercompensation), 1 (exact compensation),
2 and 5 (overcompensation), and b = 0 (density independence: A = B/2).
A: survivors against initial density. B: k = log10 B - log10 A = log10(1 + (aB)^b) against log10 B;
the slope approaches b at high density. C: the per capita mortality rate -ln(A/B) against B.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
a = 0.01
B = np.geomspace(1, 1e4, 400)
cases = [(0, P.muted(), "b = 0: density independent"), (0.5, C.line("dna"), "b = 0.5: undercompensating"),
         (1, C.line("positive"), "b = 1: exact (contest)"), (2, C.line("rna"), "b = 2: overcompensating"),
         (5, C.line("negative"), "b = 5: towards scramble")]

fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.9))
for b, col, name in cases:
    A = B / 2 if b == 0 else B / (1 + (a * B) ** b)
    axes[0].plot(B, A, color=col, lw=2, label=name)
    axes[1].plot(np.log10(B), np.log10(B) - np.log10(A), color=col, lw=2)
    axes[2].plot(B, np.log(B / A), color=col, lw=2)
axes[0].set_xlim(0, 1000)
axes[0].set_ylim(0, 260)
C.style_axes(axes[0], "initial density B", "survivors A")
axes[0].legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
C.title(axes[0], "A  Survivors")
axes[1].set_ylim(0, 4)
for s, x0 in ((0.5, 3.0), (1, 3.0), (2, 2.6)):
    axes[1].text(x0 + 0.5, s * (x0 + 0.5 - 2) + 0.05 + (0.15 if s == 1 else 0), f"slope → {s:g}", fontsize=FS["tiny"],
                 color=P.muted())
C.style_axes(axes[1], "log₁₀ B", "k = log₁₀ B − log₁₀ A")
C.title(axes[1], "B  k against log density")
axes[2].set_xscale("log")
axes[2].set_ylim(0, 8)
C.style_axes(axes[2], "initial density B (log scale)", "mortality rate −ln(A/B)")
C.title(axes[2], "C  Per capita mortality")
fig.tight_layout()
