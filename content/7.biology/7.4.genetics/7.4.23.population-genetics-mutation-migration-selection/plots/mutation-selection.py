"""Mutation-selection balance with mutation rate mu = 1e-5 per generation (from the normal allele to the
deleterious one). A: equilibrium frequency of the deleterious allele against the selection coefficient s
against homozygotes, for complete recessivity (q = sqrt(mu/s)) and for heterozygote effects h = 0.01, 0.05
and 0.5 (q ~ mu/(hs)); dots: the exact equilibria found by iterating the recursion. Even slight
expression in heterozygotes lowers the equilibrium greatly, because heterozygotes are then the main target of
selection. B: approach to the equilibrium q = sqrt(mu) = 0.0032 of a recessive lethal from q = 0, and to
mu/(hs) = 0.0002 for h = 0.05, s = 1."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
mu = 1e-5


def step(q, s, h):
    q = q + mu * (1 - q)
    p = 1 - q
    wb = p * p + 2 * p * q * (1 - h * s) + q * q * (1 - s)
    return (p * q * (1 - h * s) + q * q * (1 - s)) / wb


def equilibrium(s, h, n=200000):
    q = 0.0
    for _ in range(n):
        q2 = step(q, s, h)
        if abs(q2 - q) < 1e-14:
            break
        q = q2
    return q


fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.27)
a = axs[0]
s = np.logspace(-3, 0, 200)
a.loglog(s, np.sqrt(mu / s), color=charts.line("dna"), lw=2, label="$h = 0$: $\\sqrt{\\mu/s}$")
for h, tok in ((0.01, "enzyme"), (0.05, "rna"), (0.5, "negative")):
    a.loglog(s, np.minimum(mu / (h * s), 1), color=charts.line(tok), lw=2, label=f"$h = {h}$: $\\mu/(hs)$")
for sv in (0.01, 0.1, 1.0):
    for h, tok in ((0.0, "dna"), (0.05, "rna"), (0.5, "negative")):
        a.scatter([sv], [equilibrium(sv, h)], s=14, color=P.ink(), zorder=4)
a.set_ylim(1e-5, 0.2)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(a, "selection coefficient $s$", "equilibrium frequency $\\hat q$")
charts.title(a, "A  Equilibrium frequency, $\\mu = 10^{-5}$")
b = axs[1]
T = 4000
qs = {0.0: [0.0], 0.05: [0.0]}
for h in qs:
    for _ in range(T):
        qs[h].append(step(qs[h][-1], 1.0, h))
t = np.arange(T + 1)
b.plot(t, np.array(qs[0.0]) * 1e3, color=charts.line("dna"), lw=2, label="recessive lethal")
b.axhline(np.sqrt(mu) * 1e3, color=charts.line("dna"), lw=0.8, ls="--")
b.plot(t, np.array(qs[0.05]) * 1e3, color=charts.line("rna"), lw=2, label="lethal, $h = 0.05$")
b.axhline(mu / 0.05 * 1e3, color=charts.line("rna"), lw=0.8, ls="--")
b.set_xlim(0, T)
b.set_ylim(0, 3.5)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(b, "generation", "$q \\times 10^3$")
charts.title(b, "B  Approach from $q = 0$")
