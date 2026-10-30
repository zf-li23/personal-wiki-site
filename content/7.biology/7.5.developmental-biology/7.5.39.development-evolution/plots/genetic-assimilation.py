"""Genetic assimilation in a threshold model (Formula 39.7.1): a simulation of a Waddington-type experiment.

Each fly has a liability Y = G + S + E: G is the sum of allelic effects at 100 unlinked diploid loci (allele
'+' adds 0.1, starting frequency 0.2), S = 1.5 if the embryo is exposed to the stimulus (heat or ether)
and 0 otherwise, E ~ N(0, 0.5^2) a developmental noise term. The phenotype (for example crossveinless wings)
appears when Y > T = 7.0. Each generation 1000 flies are exposed and those showing the phenotype are bred
(selection for the trait, at most the 200 with the phenotype, chosen at random; parents mate at random,
free recombination); in a second line, flies without the phenotype are bred (selection against). Each
generation a sample of 1000 unexposed siblings is scored. Seed 0.
A: percentage of exposed (solid) and unexposed (dashed) flies with the phenotype in the two lines.
B: distribution of the genotypic value G in the line selected for the trait at generations 0, 8 and 16,
with the thresholds T - S (exposed) and T (unexposed) on the G scale.
"""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
L, eff, p0, S, sdE, T = 100, 0.1, 0.2, 1.5, 0.5, 7.0
Npop, Nsel, gens = 1000, 200, 20


def genotypes(pop):
    return pop.sum(axis=(1, 2)) * eff


def offspring(parents, n):
    i = rng.integers(0, len(parents), n)
    j = rng.integers(0, len(parents), n)
    pick_i = rng.integers(0, 2, (n, L))
    pick_j = rng.integers(0, 2, (n, L))
    a = np.take_along_axis(parents[i], pick_i[:, None, :], axis=1)[:, 0, :]
    b = np.take_along_axis(parents[j], pick_j[:, None, :], axis=1)[:, 0, :]
    return np.stack([a, b], axis=1)


def run(select_for):
    pop = (rng.random((Npop, 2, L)) < p0).astype(np.int8)
    exp_frac, unexp_frac, snaps = [], [], {}
    for g in range(gens + 1):
        G = genotypes(pop)
        if g in (0, 8, 16):
            snaps[g] = G.copy()
        aff = G + S + rng.normal(0, sdE, Npop) > T
        test = offspring(pop, Npop)
        unexp = genotypes(test) + rng.normal(0, sdE, Npop) > T
        exp_frac.append(100 * aff.mean())
        unexp_frac.append(100 * unexp.mean())
        chosen = np.flatnonzero(aff if select_for else ~aff)
        if len(chosen) > Nsel:
            chosen = rng.choice(chosen, Nsel, replace=False)
        pop = offspring(pop[chosen], Npop)
    return np.array(exp_frac), np.array(unexp_frac), snaps


up_e, up_u, snaps = run(True)
dn_e, dn_u, _ = run(False)
gg = np.arange(gens + 1)

fig, axs = plt.subplots(1, 2, figsize=(11.0, 3.8))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.86, wspace=0.28)
a = axs[0]
a.plot(gg, up_e, "o-", color=charts.line("drug"), ms=3, lw=1.5, label="selected for, exposed")
a.plot(gg, up_u, "o--", color=charts.line("drug"), ms=3, lw=1.2, mfc="none", label="selected for, unexposed")
a.plot(gg, dn_e, "s-", color=charts.line("dna"), ms=3, lw=1.5, label="selected against, exposed")
a.plot(gg, dn_u, "s--", color=charts.line("dna"), ms=3, lw=1.2, mfc="none", label="selected against, unexposed")
a.set_ylim(-3, 103)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right", bbox_to_anchor=(1.0, 0.84))
charts.style_axes(a, "generation", "flies with the phenotype / %")
charts.title(a, "A  Selection on an induced phenotype")

b = axs[1]
bins = np.arange(-0.1, 10.1, 0.2)
for g, tok in ((0, "neutral"), (8, "highlight"), (16, "drug")):
    b.hist(snaps[g], bins=bins, density=True, histtype="stepfilled", alpha=0.45, color=P.fill(tok),
           edgecolor=P.edge(tok), lw=0.8, label=f"generation {g}")
for x, txt, ha in ((T - S, "threshold\nwith stimulus", "right"), (T, "threshold\nwithout", "left")):
    b.axvline(x, color=P.ink(), lw=0.8, ls=(0, (3, 2)))
    b.text(x + (0.1 if ha == "left" else -0.1), 0.95, txt, fontsize=FT["tiny"], color=P.ink(), va="top", ha=ha)
b.set_ylim(0, 1.0)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left", bbox_to_anchor=(0.0, 0.8))
charts.style_axes(b, "genotypic value G", "density")
charts.title(b, "B  The genotypes move towards the threshold")
