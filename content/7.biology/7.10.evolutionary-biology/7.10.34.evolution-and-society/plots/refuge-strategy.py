"""The high-dose/refuge strategy for delaying resistance to Bt crops (Section 34.4.2). A pest with one
resistance locus mates at random across Bt and non-Bt (refuge) fields. On Bt plants the fitness of
susceptible homozygotes SS is 0.01 and that of resistant homozygotes RR is 1; in the refuge all
genotypes have fitness 1. Initial frequency of R is 0.001. A: frequency of R over generations for
refuge fractions 0, 5 %, 20 % and 50 %, with resistance recessive (fitness of RS on Bt plants 0.01,
the "high dose" that kills heterozygotes). B: generations until R exceeds 0.5 as a function of the
refuge fraction, for recessive resistance and for partly dominant resistance (fitness of RS on Bt
plants 0.5). A refuge delays resistance by orders of magnitude only when resistance is recessive:
the rare R alleles are then carried in heterozygotes, which die on Bt plants, and resistant
homozygotes emerging from Bt fields mate mostly with susceptible insects from the refuge."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def run(refuge, h_fit, p0=1e-3, gmax=3000):
    p = p0
    traj = [p]
    for g in range(gmax):
        q = 1 - p
        f = np.array([p * p, 2 * p * q, q * q])  # RR, RS, SS
        w_bt = np.array([1.0, h_fit, 0.01])
        w = refuge * 1.0 + (1 - refuge) * w_bt
        nw = f * w
        p = (nw[0] + nw[1] / 2) / nw.sum()
        traj.append(p)
        if p > 0.999:
            break
    return np.array(traj)


fig, (a, b) = plt.subplots(1, 2, figsize=(9.8, 3.5))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.87, wspace=0.3)
for r, tok in ((0.0, "negative"), (0.05, "rna"), (0.2, "dna"), (0.5, "plant")):
    tr = run(r, 0.01, gmax=400)
    a.plot(np.arange(tr.size), tr, color=charts.line(tok), lw=2, label=f"refuge {int(r * 100)} %")
a.set_xlim(0, 400)
charts.style_axes(a, "generations", "frequency of resistance allele")
charts.title(a, "A  Recessive resistance")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
rs = np.linspace(0, 0.6, 25)
for h, tok, lab in ((0.01, "dna", "recessive (RS fitness 0.01)"), (0.5, "rna", "partly dominant (RS fitness 0.5)")):
    gens = []
    for r in rs:
        tr = run(r, h)
        hit = np.argmax(tr > 0.5) if (tr > 0.5).any() else np.nan
        gens.append(hit)
    b.semilogy(rs * 100, gens, "o-", ms=3.5, lw=1.5, color=charts.line(tok), label=lab)
charts.style_axes(b, "refuge (% of fields)", "generations to 50 % resistance")
charts.title(b, "B  Effect of the refuge")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
