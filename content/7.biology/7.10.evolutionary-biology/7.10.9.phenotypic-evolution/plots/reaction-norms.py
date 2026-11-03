"""Reaction norms and the evolution of plasticity. A: linear reaction norms z = a + b e of six hypothetical
genotypes over an environmental gradient e; differing slopes are genotype-environment interaction, so that
the ranking of genotypes changes along the gradient. B: evolution of the mean slope b in a quantitative-
genetic model: in each generation the environment of selection e_s ~ N(0, 1) sets the optimum
theta = B e_s (B = 1), while development responds to a cue e_d correlated with e_s (correlation rho);
fitness is Gaussian (V_s = 5) and the means of intercept and slope change by G times their selection
gradients (G = diag(0.05, 0.05)). Lines: mean slope over 3000 generations for rho = 0.9, 0.5 and 0.1
(seed 0); dashed: the predicted optimum b* = rho B."""
import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(10.0, 4.0))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.14, top=0.9, wspace=0.28)
a = axs[0]
e = np.linspace(-1, 1, 2)
rng = np.random.default_rng(3)
for i in range(6):
    ai, bi = rng.normal(0, 0.4), rng.normal(0.4, 0.5)
    a.plot(e, ai + bi * e, color=charts.line(["dna", "rna", "plant", "enzyme", "negative", "animal"][i]), lw=2)
    a.scatter(e, ai + bi * e, s=14, color=charts.line(["dna", "rna", "plant", "enzyme", "negative", "animal"][i]))
a.set_xticks([-1, 1])
a.set_xticklabels(["environment 1", "environment 2"])
charts.style_axes(a, None, "phenotype $z$")
charts.title(a, "A  Reaction norms of six genotypes")

b = axs[1]
B, Vs, Gv, T = 1.0, 5.0, 0.05, 3000
rng = np.random.default_rng(0)
for rho, tok in ((0.9, "plant"), (0.5, "dna"), (0.1, "rna")):
    am, bm = 0.0, 0.0
    tr = []
    for t in range(T):
        es = rng.normal()
        ed = rho * es + np.sqrt(1 - rho**2) * rng.normal()
        dev = B * es - (am + bm * ed)
        am += Gv * dev / Vs
        bm += Gv * ed * dev / Vs
        tr.append(bm)
    b.plot(np.arange(T), tr, color=charts.line(tok), lw=1.2, label=f"$\\rho = {rho}$")
    b.axhline(rho * B, color=charts.line(tok), lw=0.9, ls="--")
b.set_ylim(-0.1, 1.05)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(b, "generation", "mean plasticity $\\bar b$")
charts.title(b, "B  Plasticity evolves to $b^* = \\rho B$")
