# k-mer spectrum of a simulated diploid genome and a GenomeScope-style fit. Haploid genome G = 100 Mb,
# heterozygosity r = 1 % per base, k = 21, read coverage 30x with 150-nt reads (k-mer coverage 26 per diploid,
# 13 per haplotype), base error rate 0.2 %. Heterozygous k-mers (in one haplotype only) form the peak at 13,
# homozygous k-mers the peak at 26; error k-mers pile up at counts 1-3. The fitted model is a mixture of two
# negative binomials at lambda and 2 lambda with weights 2(1-(1-r)^k) and (1-r)^k per haploid position;
# fitting counts >= 6 recovers G, r and lambda, and G is also estimated as (k-mer instances)/(2 lambda).
import numpy as np
from scipy import optimize, stats
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
G, r, k, lam, size, err = 100e6, 0.01, 21, 13.0, 60.0, 0.002
x = np.arange(1, 121)


def nb(xs, mean, size):
    p = size / (size + mean)
    return stats.nbinom.pmf(xs, size, p)


def genomic(xs, G, r, lam, size):
    hom = (1 - r) ** k
    return G * (2 * (1 - hom) * nb(xs, lam, size) + hom * nb(xs, 2 * lam, size))


true_gen = genomic(x, G, r, lam, size)
inst = 2 * lam * G                      # k-mer instances from the genome
n_err = inst * (1 - (1 - err) ** k)     # error k-mer instances, mostly unique
err_h = n_err * stats.geom.pmf(x, 0.85) / x * 0.9
counts = rng.poisson(true_gen + err_h)
mask = x >= 6
popt, _ = optimize.curve_fit(lambda xs, G, r, lam, size: genomic(xs, G, r, lam, size), x[mask], counts[mask],
                             p0=(80e6, 0.005, 12.0, 30.0), bounds=([1e6, 1e-5, 2, 1], [1e9, 0.1, 60, 1e3]))
Gf, rf, lf, sf = popt
G_inst = (counts[mask] * x[mask]).sum() / (2 * lf)

fig, ax = bio.canvas(18.0, 9.5)
a = C.axes_at(ax, (1.8, 1.4, 14.6, 7.2))
a.bar(x, counts / 1e6, width=1.0, color=P.light("dna"), edgecolor=P.edge("dna"), lw=0.3, label="simulated spectrum")
a.plot(x, genomic(x, *popt) / 1e6, color=C.line("negative"), lw=1.8, label="fitted model (counts >= 6)")
hom = (1 - rf) ** k
a.plot(x, Gf * 2 * (1 - hom) * nb(x, lf, sf) / 1e6, color=C.line("protein"), lw=1.0, ls=(0, (3, 2)),
       label="heterozygous k-mers")
a.plot(x, Gf * hom * nb(x, 2 * lf, sf) / 1e6, color=C.line("enzyme"), lw=1.0, ls=(0, (3, 2)), label="homozygous k-mers")
a.set_xlim(0, 70)
a.set_ylim(0, 8)
a.text(2.5, 7.5, "errors", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.text(lf - 5.5, 4.45, f"het peak ~{lf:.1f}", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.text(2 * lf, 5.75, f"hom peak ~{2 * lf:.1f}", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.text(38, 4.2, f"fit: G = {Gf / 1e6:.1f} Mb, r = {100 * rf:.2f} %\n"
                   f"from instances / (2 lambda): G = {G_inst / 1e6:.1f} Mb\n(simulated: G = 100 Mb, r = 1.00 %)",
       fontsize=bio.core.FONT["tiny"], color=P.ink(), va="top")
C.style_axes(a, "k-mer count (times a 21-mer occurs in the reads)", "distinct 21-mers (millions)")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")

