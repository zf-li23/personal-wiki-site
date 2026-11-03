"""What happens when medicine relaxes selection against a genetic disease (Section 33.6.1), after the
argument of Barton et al. (2007), Fig. 26.15. Mutation rate 10^-5 per generation. A recessive lethal at
mutation-selection balance has allele frequency q = sqrt(mu), about 0.003, carried almost entirely in
heterozygotes; a dominant allele with heterozygote fitness 1 - s (s = 0.1) has frequency p = mu/s.
If selection is removed entirely, each frequency rises by mu per generation. The incidence of the
dominant disease (about 2p) doubles in 10 generations and rises 11-fold in 100; that of the recessive
disease (q^2) rises by about three-quarters in 100 generations."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
mu, s = 1e-5, 0.1
t = np.arange(0, 201)
q = np.sqrt(mu) + mu * t
p = mu / s + mu * t
fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.4))
fig.subplots_adjust(left=0.09, right=0.98, bottom=0.17, top=0.87, wspace=0.3)
a.semilogy(t, q, color=charts.line("dna"), lw=2, label="recessive lethal")
a.semilogy(t, p, color=charts.line("rna"), lw=2, label="dominant, s = 0.1")
charts.style_axes(a, "generations after selection is relaxed", "allele frequency")
charts.title(a, "A  Allele frequency")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
b.plot(t, (q / q[0]) ** 2, color=charts.line("dna"), lw=2)
b.plot(t, p / p[0], color=charts.line("rna"), lw=2)
for x in (10, 100):
    b.axvline(x, color=P.muted(), lw=0.6, ls=":")
charts.style_axes(b, "generations after selection is relaxed", "incidence relative to start")
charts.title(b, "B  Incidence of the disease")
