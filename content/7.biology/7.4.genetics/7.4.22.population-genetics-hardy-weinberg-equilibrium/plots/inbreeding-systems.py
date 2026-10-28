"""Loss of heterozygosity under regular systems of inbreeding, as the panmictic index 1 - F (heterozygosity
relative to a random-mating population with the same allele frequencies). Self-fertilization halves it
every generation; full-sib mating, F_t = (1 + 2F_(t-1) + F_(t-2))/4, reduces it asymptotically by the factor
0.809 per generation; half-sib mating, F_t = (1 + 6F_(t-1) + F_(t-2))/8, by 0.890; drift alone in a
random-mating population of N = 50 by 1 - 1/(2N) = 0.99 (Chapter 7.4.23). Dashed: the 20 generations of
full-sib mating that define an inbred mouse strain (F = 0.986)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
T = 30


def recur(c0, c1, c2):
    F = [0.0, 0.0]
    for _ in range(T):
        F.append((c0 + c1 * F[-1] + c2 * F[-2]))
    return np.array(F[1:])


t = np.arange(T + 1)
series = [
    ("selfing", 1 - (0.5) ** t * 1.0, "negative"),
    ("full sibs", recur(0.25, 0.5, 0.25), "rna"),
    ("half sibs", recur(0.125, 0.75, 0.125), "enzyme"),
    ("random mating, $N = 50$", 1 - (1 - 1 / 100) ** t, "dna"),
]
fig, ax = plt.subplots(figsize=(6.6, 3.8))
fig.subplots_adjust(left=0.12, right=0.97, bottom=0.15, top=0.9)
for lab, F, tok in series:
    ax.semilogy(t, 1 - F, "o-", ms=2.5, color=charts.line(tok), lw=1.6, label=lab)
ax.axvline(20, color=P.muted(), lw=0.8, ls="--")
ax.text(20.4, 0.4, "inbred strain:\n20 sib generations", fontsize=FT["tiny"], color=P.muted(), va="top")
ax.set_ylim(1e-4, 1.3)
ax.set_xlim(0, T)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "generations of inbreeding", "heterozygosity  $1 - F$")
charts.title(ax, "Regular systems of inbreeding")
