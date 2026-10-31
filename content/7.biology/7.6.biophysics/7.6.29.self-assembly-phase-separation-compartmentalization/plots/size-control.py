"""Length control of eukaryotic flagella by a balance point. A: in the balance-point model the
assembly rate falls as 1/L because a fixed number of intraflagellar transport trains, each carrying
a fixed load, must travel the whole length, while disassembly proceeds at a constant rate D; the
steady length is L* = A/D (parameters: A = 10 um^2/min, D = 1 um/min, so L* = 10 um).
B: two flagella sharing a limited precursor pool (assembly rate a P / L, with free pool P = P_tot - L1 - L2; the amputated material is lost and new
precursor synthesis restores P_tot with a 30 min time constant):
when one flagellum is amputated (t = 0) the stump regrows quickly while the intact one transiently
shortens, until both reach the same length, the behavior of Chlamydomonas in the classic
"long-zero" experiment."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(7.6, 3.1))
fig.subplots_adjust(wspace=0.38, left=0.09, right=0.98, bottom=0.17, top=0.87)

ax = axs[0]
L = np.linspace(1, 25, 300)
ax.plot(L, 10 / L, color=charts.line("dna"), lw=1.6, label="assembly $A/L$")
ax.axhline(1.0, color=charts.line("blood"), lw=1.6, label="disassembly $D$")
ax.plot([10], [1], "o", ms=5, color=P.ink())
ax.text(10.6, 1.25, r"$L^* = A/D$", fontsize=FT["tiny"], color=P.ink())
ax.set_ylim(0, 4)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"flagellar length $L$ / $\mu$m", r"rate / $\mu$m min$^{-1}$")
charts.title(ax, "A  Balance point")

ax = axs[1]
a, D = 2.0, 1.0   # steady state L* = 10 um each needs a free pool of 5: a 5/10 = D
L1, L2 = 10.0, 0.05
dt = 0.002
ts, l1, l2 = [], [], []
t = 0.0
while t < 120:
    Ptot = 15.0 + 10.0 * (1 - np.exp(-t / 30.0))  # amputated tubulin lost; new synthesis restores it
    Pf = max(Ptot - L1 - L2, 0.0)
    L1 += dt * (a * Pf / L1 - D)
    L2 += dt * (a * Pf / L2 - D)
    L2 = max(L2, 0.05)
    t += dt
    ts.append(t); l1.append(L1); l2.append(L2)
ax.plot(ts, l1, color=charts.line("dna"), lw=1.6, label="intact flagellum")
ax.plot(ts, l2, color=charts.line("blood"), lw=1.6, label="amputated flagellum")
ax.set_ylim(0, 12)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "time after amputation / min", r"length / $\mu$m")
charts.title(ax, "B  Long-zero experiment")
