"""Transmission ratio distortion, Eq. (19.4). A: an allele that heterozygotes transmit with probability t,
starting rare, for several values of t and a cost s in homozygotes only. B: equilibrium frequencies as a
function of the cost, when heterozygotes also pay a fraction h of it."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def step(q, t, s, h):
    wbar = 1 - s * q**2 - 2 * h * s * q * (1 - q)
    return (q**2 * (1 - s) + 2 * t * q * (1 - q) * (1 - h * s)) / wbar


fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.9))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.88, wspace=0.26)

a = axs[0]
T = 60
for t, tok in ((0.5, "neutral"), (0.6, "dna"), (0.75, "receptor"), (0.9, "positive")):
    q = [0.02]
    for _ in range(T):
        q.append(step(q[-1], t, 0.2, 0.0))
    a.plot(np.arange(T + 1), q, color=charts.line(tok), lw=1.8,
           label=("Mendelian, $t$ = 0.5" if t == 0.5 else f"$t$ = {t}"))
a.set_ylim(-0.02, 1.02)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(a, "generation", "allele frequency $q$")
charts.title(a, "A  Spread of a distorter ($s$ = 0.2, $h$ = 0)")

b = axs[1]
ss = np.linspace(0, 1, 101)
for t, tok in ((0.75, "dna"), (0.9, "receptor")):
    eq = []
    for s in ss:
        q = 0.05
        for _ in range(3000):
            q = min(max(step(q, t, s, 0.2), 0.0), 1.0)
        eq.append(q)
    b.plot(ss, eq, color=charts.line(tok), lw=1.9, label=f"$t$ = {t}")
b.axhline(1.0, color=P.muted(), lw=0.7, ls=":")
b.text(0.02, 0.93, "fixation", fontsize=FT["tiny"], color=P.muted())
b.set_ylim(-0.02, 1.08)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(b, "cost $s$ in homozygotes ($h$ = 0.2)", "equilibrium frequency")
charts.title(b, "B  Equilibrium: fixation or polymorphism")
