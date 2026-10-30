"""Chance in development: random X inactivation in a small precursor pool (Formula 38.2.1).

A carrier female has one wild-type and one mutant X. If a tissue descends from N precursor cells at the time
of X inactivation, each inactivating either X with probability 1/2, the number K of precursors that keep the
wild-type X active is Binomial(N, 1/2), and the fraction of wild-type-expressing cells in the tissue is f = K/N.
A: distribution of f for N = 8, 16 and 64. B: probability that f <= 0.4 (for a clotting factor, a plasma level
in the range of mild hemophilia) and that f <= 0.1 (severe deficiency), as a function of N (exact binomial).
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

fig, axs = plt.subplots(1, 2, figsize=(11.0, 3.6))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.86, wspace=0.3)

a = axs[0]
for N, tok, dx in ((8, "drug", -0.012), (16, "dna", 0.0), (64, "positive", 0.012)):
    k = np.arange(N + 1)
    pk = stats.binom.pmf(k, N, 0.5)
    a.vlines(k / N + dx, 0, pk, color=charts.line(tok), lw=1.6, label=f"N = {N}")
    a.plot(k / N + dx, pk, "o", color=charts.line(tok), ms=2.6)
a.axvspan(0, 0.4, color=P.light("negative"), lw=0)
a.text(0.02, 0.255, "f <= 0.4", fontsize=FT["tiny"], color=P.ink())
a.set_xlim(-0.03, 1.03)
a.set_ylim(0, 0.29)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(a, "fraction f of cells with the wild-type X active", "probability")
charts.title(a, "A  Random X inactivation in N precursors")

b = axs[1]
Ns = np.arange(2, 101)
p40 = stats.binom.cdf(np.floor(0.4 * Ns + 1e-9), Ns, 0.5)
p10 = stats.binom.cdf(np.floor(0.1 * Ns + 1e-9), Ns, 0.5)
b.semilogy(Ns, p40, "o-", color=charts.line("drug"), ms=2.2, lw=1.0, label="f <= 0.4")
b.semilogy(Ns, p10, "o-", color=charts.line("negative"), ms=2.2, lw=1.0, label="f <= 0.1")
for N in (8, 16):
    v = stats.binom.cdf(np.floor(0.4 * N + 1e-9), N, 0.5)
    b.text(N + 3, v * 0.3, f"N = {N}: {100 * v:.0f} %", fontsize=FT["tiny"], color=P.ink())
b.set_ylim(1e-12, 1.5)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(b, "number of precursor cells N", "probability")
charts.title(b, "B  Skewed inactivation becomes rare in large pools")
