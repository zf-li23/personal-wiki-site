"""The arithmetic of saturation in a genetic screen. A: expected fraction of genes found against lambda, the
mean number of alleles recovered per gene, for a Poisson model and for gamma-distributed mutabilities.
B: a simulated screen of 120 genes with lambda = 1.5, with the Poisson expectation and the Chao estimate of
the number of genes still missing."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.9))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.88, wspace=0.26)

a = axs[0]
lam = np.linspace(0, 6, 300)
a.plot(lam, 1 - np.exp(-lam), color=charts.line("dna"), lw=2, label="Poisson: $1 - e^{-\\lambda}$")
for k, ls in ((3, "--"), (1, ":")):
    a.plot(lam, 1 - (1 + lam / k) ** (-k), color=charts.line("receptor"), lw=1.5, ls=ls,
           label=f"variable mutability, shape $k$ = {k}")
for y in (0.95, 0.99):
    a.axhline(y, color=P.muted(), lw=0.7, ls=":")
    a.text(0.1, y - 0.055 if y == 0.95 else y + 0.012, f"{y:.0%}", ha="left", fontsize=FT["tiny"], color=P.muted())
a.set_ylim(0, 1.03)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(a, r"$\lambda = N\mu$ (alleles per gene)", "fraction of genes found")
charts.title(a, "A  How saturation approaches 1")

b = axs[1]
G, lam0 = 120, 1.5
counts = rng.poisson(lam0, G)
k = np.arange(0, 7)
obs = np.array([(counts == i).sum() for i in k])
b.bar(k[1:], obs[1:], width=0.62, color=P.fill("dna"), edgecolor=charts.line("dna"), lw=0.9, label="genes found")
b.plot(k[1:], G * stats.poisson.pmf(k[1:], lam0), "o", color=charts.line("receptor"), ms=5,
       label=f"Poisson expectation ($\\lambda$ = {lam0})")
n1, n2 = obs[1], obs[2]
chao = n1**2 / (2 * n2)
b.bar([0], [obs[0]], width=0.62, color=P.fill("neutral"), edgecolor=P.muted(), lw=0.9, label="genes missed (true)")
b.plot([0], [chao], "D", color=charts.line("positive"), ms=6, label=f"Chao estimate $n_1^2/2n_2$ = {chao:.0f}")
b.text(3.1, 0.82 * obs[1], f"$\\hat\\lambda = 2n_2/n_1$ = {2 * n2 / n1:.2f}", fontsize=FT["tiny"], color=P.muted())
b.set_xticks(k)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "alleles recovered per gene", "number of genes")
charts.title(b, "B  One simulated screen of 120 genes")
