"""Copy-number dynamics of a transposable element (Formula 17.6.1). A: the mean copy number per genome n
under dn/dt = n (u - v - a - b n), with transposition rate u, excision rate v and selection against
copies with log fitness -a n - b n^2/2 (synergistic epistasis b > 0), from several starting values; and
with self-regulation, u(n) = u0 / (1 + n/n_r), as by host piRNAs that become more abundant with the
number of copies. B: the equilibrium n* = (u - v - a)/b as a function of u for two strengths of epistasis."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts, quant

P = bio.P
u, v, a, b = 0.01, 0.001, 0.001, 1e-4
t = np.linspace(0, 3000, 1501)
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.9, wspace=0.28)
ax = axs[0]
for n0 in (1, 20, 150):
    y = quant.odeint_rk4(lambda tt, n: n * (u - v - a - b * n), [n0], t)[:, 0]
    ax.plot(t, y, color=charts.line("dna"), lw=1.4, label="constant u" if n0 == 1 else None)
for n0 in (1, 150):
    y = quant.odeint_rk4(lambda tt, n: n * (u / (1 + n / 20) - v - a - b * n), [n0], t)[:, 0]
    ax.plot(t, y, color=charts.line("receptor"), lw=1.4, ls="--", label="self-regulated u" if n0 == 1 else None)
ax.axhline((u - v - a) / b, color=P.muted(), lw=0.6, ls=":")
ax.text(1600, (u - v - a) / b + 3, "n* = (u − v − a)/b", ha="left", va="bottom", fontsize=bio.core.FONT["tiny"], color=P.muted())
charts.style_axes(ax, "generations", "copies per genome n")
charts.title(ax, "A  Approach to equilibrium")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
ax = axs[1]
us = np.linspace(0, 0.02, 200)
for bb, tok in ((1e-4, "dna"), (4e-4, "enzyme")):
    ax.plot(us * 1e3, np.maximum((us - v - a) / bb, 0), color=charts.line(tok), lw=1.5, label=f"b = {bb:g}")
charts.style_axes(ax, "transposition rate u / 10⁻³ per copy per generation", "equilibrium copies n*")
charts.title(ax, "B  Equilibrium copy number")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
