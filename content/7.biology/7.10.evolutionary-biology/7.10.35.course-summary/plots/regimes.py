"""The three scaled parameters of population genetics. A: fixation probability of a new mutation
relative to a neutral one, 2N u(1/2N) = 2N (1 - exp(-2s)) / (1 - exp(-4 N s)) (Kimura, genic selection,
N_e = N = 1000), against the scaled selection coefficient N_e s; the band |N_e s| < 1 is the nearly neutral
zone. B: neutral differentiation among many demes of the island model, F_ST = 1 / (1 + 4 N_e m), against
the number of migrants N_e m. C: expected heterozygosity at mutation-drift equilibrium under the
infinite-alleles model, H = theta / (1 + theta), and the expected number of segregating sites in a sample
of n = 10, E[S] = theta a_n (per locus), against theta = 4 N_e mu. Dotted vertical lines mark the scaled
parameter equal to 1."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, (a, b, c) = plt.subplots(1, 3, figsize=(12.0, 3.7))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.88, wspace=0.34)

N = 1000
x = np.linspace(-6, 6, 601)
s = x / N
with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
    u = np.where(np.abs(s) < 1e-12, 1 / (2 * N), (1 - np.exp(-2 * s)) / (1 - np.exp(-4 * N * s)))
a.axvspan(-1, 1, color=P.fill("highlight"), alpha=0.35, lw=0)
a.semilogy(x, 2 * N * u, color=charts.line("dna"), lw=1.8)
a.axhline(1, color=P.muted(), lw=0.8, ls=":")
a.text(0, 3e-3, "drift\ndominates", ha="center", fontsize=FT["tiny"], color=P.ink())
a.text(4.0, 1e-3, "selection\ndominates", ha="center", fontsize=FT["tiny"], color=P.ink())
a.text(-4.6, 1e-3, "purged", ha="center", fontsize=FT["tiny"], color=P.ink())
a.set_xlim(-6, 6)
a.set_ylim(1e-9, 50)
charts.style_axes(a, "scaled selection $N_{\\mathrm{e}}s$", "fixation probability / neutral")
charts.title(a, "A  Selection vs drift")

nm = np.logspace(-2, 2, 300)
b.semilogx(nm, 1 / (1 + 4 * nm), color=charts.line("rna"), lw=1.8)
b.axvline(1, color=P.muted(), lw=0.8, ls=":")
b.text(0.03, 0.12, "demes diverge\nby drift", fontsize=FT["tiny"], color=P.ink())
b.text(4, 0.55, "gene flow\nhomogenizes", fontsize=FT["tiny"], color=P.ink())
b.set_ylim(0, 1)
charts.style_axes(b, "migrants per generation $N_{\\mathrm{e}}m$", "$F_{\\mathrm{ST}}$")
charts.title(b, "B  Migration vs drift")

th = np.logspace(-3, 2, 300)
an = sum(1 / i for i in range(1, 10))
c.semilogx(th, th / (1 + th), color=charts.line("enzyme"), lw=1.8, label="heterozygosity $H$")
c2 = c.twinx()
c2.loglog(th, th * an, color=charts.line("plant"), lw=1.5, ls="--", label="segregating sites $\\mathbb{E}[S]$, $n = 10$")
c.axvline(1, color=P.muted(), lw=0.8, ls=":")
c.set_ylim(0, 1)
charts.style_axes(c, "$\\theta = 4N_{\\mathrm{e}}\\mu$", "$H = \\theta/(1+\\theta)$")
charts.style_axes(c2, None, "$\\mathbb{E}[S] = \\theta a_n$", box=True)
c2.spines["top"].set_visible(False)
h1, l1 = c.get_legend_handles_labels()
h2, l2 = c2.get_legend_handles_labels()
c.legend(h1 + h2, l1 + l2, frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.title(c, "C  Mutation vs drift")
