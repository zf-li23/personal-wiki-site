"""Industrial melanism in the peppered moth as a deterministic one-locus model. The melanic allele C
(carbonaria) is dominant. A: rise under selection against the light recessive phenotype (fitness of cc
1 - s, s = 0.254, the value that takes the melanic phenotype from 1 % to 98 % in 47 generations, about
1848-1895 near Manchester); allele and phenotype frequencies differ most while C is rare. B: decline
after air pollution fell, with selection s against the melanic phenotype (fitness of C_ 1 - s), from a
melanic frequency of 90 %, for s = 0.1, 0.15 and 0.2; the last melanics persist for a long time as
heterozygotes."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def rise(p, s, T):
    out = [p]
    for _ in range(T):
        q = 1 - p
        q = (q - s * q * q) / (1 - s * q * q)
        p = 1 - q
        out.append(p)
    return np.array(out)


def decline(p, s, T):
    out = [p]
    for _ in range(T):
        q = 1 - p
        wb = (1 - s) * (1 - q * q) + q * q
        p = p * (1 - s) / wb
        out.append(p)
    return np.array(out)


def phen(p):
    return 1 - (1 - p) ** 2


fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.9, wspace=0.25)
a = axs[0]
T = 60
t = np.arange(T + 1)
p0 = 1 - np.sqrt(0.99)
pr = rise(p0, 0.254, T)
a.plot(t, phen(pr), color=charts.line("dna"), lw=2, label="melanic phenotype")
a.plot(t, pr, color=charts.line("enzyme"), lw=2, ls="--", label="allele $C$")
a.scatter([0, 47], [0.01, 0.98], color=P.ink(), s=18, zorder=5)
a.annotate("1848: 1 %", (0, 0.01), xytext=(1, 0.06), fontsize=FT["tiny"], color=P.ink())
a.annotate("1895: 98 %", (47, 0.98), xytext=(30, 0.86), fontsize=FT["tiny"], color=P.ink())
a.set_xlim(0, T)
a.set_ylim(0, 1.02)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(a, "generation (years)", "frequency")
charts.title(a, r"A  Rise of $\it{carbonaria}$, $s = 0.25$ against $\it{typica}$")

b = axs[1]
T = 80
t = np.arange(T + 1)
p0 = 1 - np.sqrt(0.1)
for s, tok in ((0.1, "dna"), (0.15, "enzyme"), (0.2, "negative")):
    b.plot(t, phen(decline(p0, s, T)), color=charts.line(tok), lw=2, label=f"$s = {s}$")
b.axhline(0.1, color=P.muted(), lw=0.8, ls=":")
b.set_xlim(0, T)
b.set_ylim(0, 1.0)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "generation after the decline in pollution", "melanic phenotype frequency")
charts.title(b, r"B  Decline under selection against $\it{carbonaria}$")
