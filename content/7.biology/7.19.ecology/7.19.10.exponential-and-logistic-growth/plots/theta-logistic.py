"""The theta-logistic model dN/dt = r N [1 - (N/K)^theta] and the Gompertz limit (Section 10.3.1).

The per capita growth rate is scaled so that its value at N = 0 is r = 1 for theta > 0, and the Gompertz
curve dN/dt = r N ln(K/N) is drawn with r = 1 (it is the limit theta -> 0 of the theta-logistic with
r replaced by r/theta). K = 1.
A: per capita growth rate against N/K. B: dN/dt against N/K with the inflection points
N* = K (1 + theta)^(-1/theta) (Gompertz: K/e). C: solutions from N0 = 0.02 (closed form, Proposition 10.3.1).
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
x = np.linspace(1e-4, 1.2, 500)
cases = [(0.3, C.line("rna")), (1.0, C.line("dna")), (4.0, C.line("positive"))]

fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.8))
for th, col in cases:
    axes[0].plot(x, 1 - x ** th, color=col, lw=2, label=f"θ = {th:g}")
    axes[1].plot(x, x * (1 - x ** th), color=col, lw=2)
    ns = (1 + th) ** (-1 / th)
    axes[1].plot([ns], [ns * (1 - ns ** th)], "o", color=col, ms=5)
    t = np.linspace(0, 14, 400)
    N0 = 0.02
    N = (1 + (N0 ** -th - 1) * np.exp(-th * t)) ** (-1 / th)
    axes[2].plot(t, N, color=col, lw=2)
g = C.line("neuron")
axes[0].plot(x, -np.log(x) * 0.25, color=g, lw=1.6, ls=(0, (4, 2)), label="Gompertz (r = 0.25)")
axes[1].plot(x, 0.25 * x * -np.log(x), color=g, lw=1.6, ls=(0, (4, 2)))
axes[1].plot([np.exp(-1)], [0.25 * np.exp(-1)], "o", color=g, ms=5)
t = np.linspace(0, 14, 400)
axes[2].plot(t, np.exp(np.log(0.02) * np.exp(-0.25 * t)), color=g, lw=1.6, ls=(0, (4, 2)))
axes[0].axhline(0, color=P.muted(), lw=0.6)
axes[0].set_ylim(-0.5, 1.4)
C.style_axes(axes[0], "N / K", "(1/N) dN/dt")
axes[0].legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(axes[0], "A  Per capita growth rate")
axes[1].axhline(0, color=P.muted(), lw=0.6)
axes[1].set_xlim(0, 1.2)
axes[1].set_ylim(-0.12, 0.6)
C.style_axes(axes[1], "N / K", "dN/dt  (dots: inflection)")
C.title(axes[1], "B  Growth rate")
axes[2].set_ylim(0, 1.05)
C.style_axes(axes[2], "time (r = 1; Gompertz r = 0.25)", "N / K")
C.title(axes[2], "C  Growth curves")
fig.tight_layout()
