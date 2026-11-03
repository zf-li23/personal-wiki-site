"""Migration-selection balance and gene swamping.
A: an island receives a fraction m of its genes each generation from a continent fixed for allele A1, while
A2 is favoured on the island (s = 0.05). Equilibrium frequency of A2 (iterating selection then migration
from p = 1) against m/s for additive fitnesses 1 : 1 + s : 1 + 2s (A1A1 : A1A2 : A2A2), for A2 dominant
(1 : 1 + 2s : 1 + 2s) and for A2 recessive (1 : 1 : 1 + 2s); the dashed line is the approximation
1 - m/s. In the additive case A2 is lost when m exceeds about s.
B: a patch of width L in which A2 has advantage s, embedded in a habitat where it has disadvantage s
(genic selection, continuous space): steady state of dp/dt = (sigma^2/2) p'' + s(x) p(1 - p), solved
numerically, with distance in units of the characteristic length l = sqrt(sigma^2/(2s)). Curves: frequency
profiles for several patch widths, labelled with the maximum frequency. Patches narrower than
L_c = (pi/2) l (from the linearized equation) cannot maintain the locally favoured allele."""
import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.0))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.14, top=0.9, wspace=0.28)

a = axs[0]
s = 0.05
ratios = np.linspace(0.01, 1.6, 160)
for (w12, w22), lab, tok in (((1 + s, 1 + 2 * s), "additive", "dna"), ((1 + 2 * s, 1 + 2 * s), "$A_2$ dominant", "plant"),
                             ((1.0, 1 + 2 * s), "$A_2$ recessive", "rna")):
    eq = []
    for r in ratios:
        m = r * s
        p = 1.0
        for _ in range(6000):
            q = 1 - p
            wbar = q * q + 2 * p * q * w12 + p * p * w22
            p = (p * q * w12 + p * p * w22) / wbar
            p = (1 - m) * p
        eq.append(p)
    a.plot(ratios, eq, color=charts.line(tok), lw=2, label=lab)
a.plot(ratios, np.clip(1 - ratios, 0, 1), color=P.muted(), lw=1, ls="--", label="$1 - m/s$")
a.set_ylim(-0.02, 1.02)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(a, "migration rate / selection coefficient, $m/s$", "equilibrium frequency of $A_2$")
charts.title(a, "A  Island receiving migrants from a continent")

b = axs[1]
x = np.arange(-15, 15.0001, 0.1)
dx, dt = 0.1, 0.004
widths = np.array([1.5, 2.0, 2.4, 3.0, 4.0, 6.0, 10.0])
sx = np.where(np.abs(x)[None, :] < widths[:, None] / 2, 1.0, -1.0)
p = np.where(np.abs(x)[None, :] < widths[:, None] / 2, 0.9, 0.05)
for _ in range(60000):
    lap = np.zeros_like(p)
    lap[:, 1:-1] = (p[:, 2:] - 2 * p[:, 1:-1] + p[:, :-2]) / dx**2
    lap[:, 0] = lap[:, 1]
    lap[:, -1] = lap[:, -2]
    p = np.clip(p + dt * (lap + sx * p * (1 - p)), 0, 1)
cols = ["negative", "rna", "enzyme", "plant", "dna", "animal", "neutral"]
for k, L in enumerate(widths):
    col = P.muted() if cols[k] == "neutral" else charts.line(cols[k])
    b.plot(x, p[k], color=col, lw=1.6)
    b.text(0, p[k].max() + 0.015, f"$L = {L:g}$: {p[k].max():.2f}", fontsize=FT["tiny"], color=col, ha="center",
           va="bottom")
b.set_xlim(-10, 10)
b.set_ylim(0, 1.12)
charts.style_axes(b, "position $x/l$", "frequency of $A_2$")
charts.title(b, "B  Gene swamping in small patches")
