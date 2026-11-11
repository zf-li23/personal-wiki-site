"""The liability-threshold model of a polygenic disorder.

Liability = polygenic score G + environment E, standardized N(0, 1), with heritability h2 = Var(G);
individuals with liability above the threshold T are affected, T set by the prevalence K
(K = 1 %, T = 2.33, the approximate prevalence of schizophrenia).
A: liability distribution of the population and of full siblings of affected individuals
   (h2 = 0.8, sibling liability correlation h2 / 2, ignoring shared environment).
B: recurrence risk in relatives against heritability for K = 1 % (bivariate normal with correlation
   r = h2 for monozygotic twins, h2 / 2 for first-degree relatives, h2 / 8 for first cousins).
C: a simulated polygenic score from 1000 variants of small effect (allele frequencies U(0.05, 0.5),
   effects N(0, 1), score scaled to explain 10 % of liability in a population of 50 000):
   risk by decile of the score.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multivariate_normal, norm

import wikibio as bio

P = bio.P
K = 0.01
T = norm.isf(K)
h2 = 0.8

fig, axs = plt.subplots(1, 3, figsize=(13.5, 3.9))
ax = axs[0]
x = np.linspace(-4, 5, 500)
ax.plot(x, norm.pdf(x), color=P.edge("dna"), lw=1.8, label="population")
# conditional liability of siblings of affected: mean r * E[L | L > T], variance 1 - r^2 * (...) (approx.)
r = h2 / 2
mu_aff = norm.pdf(T) / K
var_aff = 1 + T * mu_aff - mu_aff ** 2
mu_s = r * mu_aff
var_s = 1 - r ** 2 * (1 - var_aff)
ax.plot(x, norm.pdf(x, mu_s, np.sqrt(var_s)), color=P.edge("negative"), lw=1.8, label="siblings of affected")
ax.fill_between(x[x >= T], norm.pdf(x[x >= T]), color=P.fill("dna"), alpha=0.8)
ax.fill_between(x[x >= T], norm.pdf(x[x >= T], mu_s, np.sqrt(var_s)), color=P.fill("negative"), alpha=0.5)
ax.axvline(T, color=P.muted(), lw=1.0, ls="--")
ax.text(T + 0.1, 0.36, f"threshold\n(prevalence {100 * K:g} %)", fontsize=8, color=P.muted())
ax.set_xlabel("Liability (standard units)")
ax.set_ylabel("Density")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.set_title("A  Liability and threshold", loc="left", fontsize=10)

ax = axs[1]
hs = np.linspace(0, 1, 21)


def recur(rr):
    if rr <= 0:
        return K
    rr = min(rr, 0.999)
    mvn = multivariate_normal(mean=[0, 0], cov=[[1, rr], [rr, 1]])
    both = 1 - 2 * norm.cdf(T) + mvn.cdf([T, T])
    return both / K


for fac, lab, col in ((1.0, "monozygotic twin", P.edge("negative")), (0.5, "sibling, parent, child", P.edge("protein")), (0.125, "first cousin", P.edge("dna"))):
    ax.plot(hs, [100 * recur(fac * h) for h in hs], color=col, lw=1.8, label=lab)
ax.axhline(100 * K, color=P.muted(), lw=0.8, ls=":")
ax.text(0.55, 100 * K * 0.8, "population", fontsize=8, color=P.muted())
ax.set_yscale("log")
ax.set_xlabel("Heritability of liability $h^2$")
ax.set_ylabel("Risk in relative of an affected person / %")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.set_title("B  Recurrence risk", loc="left", fontsize=10)
ax.grid(True, alpha=0.3, which="both")

ax = axs[2]
rng = np.random.default_rng(0)
nsnp, nind = 1000, 50000
p = rng.uniform(0.05, 0.5, nsnp)
beta = rng.normal(size=nsnp)
geno_mean = 2 * p @ beta
geno_var = np.sum(2 * p * (1 - p) * beta ** 2)
# draw scores in chunks to limit memory: genotype counts ~ Bin(2, p)
score = np.empty(nind)
for i in range(0, nind, 10000):
    gch = rng.binomial(2, p, size=(min(10000, nind - i), nsnp)).astype(float)
    score[i:i + len(gch)] = (gch @ beta - geno_mean) / np.sqrt(geno_var)
r2 = 0.10
liab = np.sqrt(r2) * score + np.sqrt(1 - r2) * rng.normal(size=nind)
aff = liab > T
dec = np.digitize(score, np.quantile(score, np.linspace(0, 1, 11)[1:-1]))
risk = [100 * aff[dec == d].mean() for d in range(10)]
ax.bar(np.arange(1, 11), risk, color=P.fill("protein"), edgecolor=P.edge("protein"))
ax.axhline(100 * K, color=P.muted(), lw=0.8, ls=":")
ax.set_xticks(range(1, 11))
ax.set_xlabel("Decile of polygenic score")
ax.set_ylabel("Prevalence / %")
ax.set_title("C  Risk by polygenic score (10 % variance)", loc="left", fontsize=10)
fig.tight_layout()
