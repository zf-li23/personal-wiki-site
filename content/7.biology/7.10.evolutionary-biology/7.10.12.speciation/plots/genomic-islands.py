"""Genomic islands of divergence in two populations that exchange genes (N = 1000 per population,
m = 0.002, so that neutral F_ST = 1/(1 + 4 N m) = 0.11 far from selected loci). Barrier loci (in A at 30 and
70 cM) are under divergent selection. A neutral site at recombination fraction r from a barrier locus with
selection s against the immigrant allele escapes into the other genetic background with probability
about r/(r + s), so its effective migration rate is m_e = m prod_i r_i/(r_i + s_i) (Haldane map function
r = (1 - exp(-2d))/2 for map distance d in Morgans), and its expected F_ST is 1/(1 + 4 N m_e).
A: barrier loci with s = 0.2 and s = 0.02. B: a single barrier locus at 50 cM (s = 0.2) with normal
recombination, and with recombination reduced 20-fold in the segment from 40 to 60 cM that contains it (as
in an inversion heterozygote or near a centromere): the island extends over the whole low-recombination
segment. Grey dots: F_ST of
individual SNPs drawn around the expectation (beta distribution, seed 0), illustrating the noisy profile seen
in genome scans."""
import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
N, m = 1000, 0.002


def fst_profile(x, barriers, recomb_rate):
    # x in cM along the chromosome; recomb_rate(x) relative rate per cM
    xs = np.linspace(0, 100, 2001)
    cum = np.concatenate([[0], np.cumsum(recomb_rate((xs[1:] + xs[:-1]) / 2) * np.diff(xs))])
    gen = np.interp(x, xs, cum) / 100  # genetic position in Morgans
    me = np.full_like(x, m)
    for pos, s in barriers:
        d = np.abs(gen - np.interp(pos, xs, cum) / 100)
        r = (1 - np.exp(-2 * d)) / 2
        me = me * r / (r + s)
    return 1 / (1 + 4 * N * me)


x = np.linspace(0, 100, 1000)
rng = np.random.default_rng(0)
fig, axs = plt.subplots(1, 2, figsize=(11, 3.8), sharey=True)
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.9, wspace=0.08)
uniform = lambda xx: np.ones_like(xx)
inv = lambda xx: np.where((xx > 40) & (xx < 60), 0.05, 1.0)
for ax, cases, title in (
    (axs[0], [([(30, 0.2), (70, 0.2)], uniform, "$s = 0.2$", "dna"), ([(30, 0.02), (70, 0.02)], uniform, "$s = 0.02$", "rna")],
     "A  Strong and weak barrier loci"),
    (axs[1], [([(50, 0.2)], uniform, "normal recombination", "dna"),
              ([(50, 0.2)], inv, "recombination reduced 20-fold, 40–60 cM", "plant")], "B  Low recombination widens islands"),
):
    for barriers, rate, lab, tok in cases:
        f = fst_profile(x, barriers, rate)
        snp_x = rng.uniform(0, 100, 600)
        fs = fst_profile(snp_x, barriers, rate)
        k = 40.0
        ax.scatter(snp_x, rng.beta(fs * k + 0.05, (1 - fs) * k + 0.05), s=3, color=P.muted(), alpha=0.5, lw=0)
        ax.plot(x, f, color=charts.line(tok), lw=2, label=lab)
        for pos, _ in barriers:
            ax.axvline(pos, color=charts.line(tok), lw=0.7, ls=":")
    if title.startswith("B"):
        ax.axvspan(40, 60, color=P.fill("neutral"), alpha=0.4, lw=0)
    ax.axhline(1 / (1 + 4 * N * m), color=P.muted(), lw=0.8, ls="--")
    ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper center")
    ax.set_ylim(0, 1.05)
    charts.style_axes(ax, "position along chromosome (cM)", "$F_{\\mathrm{ST}}$" if title.startswith("A") else None)
    charts.title(ax, title)
