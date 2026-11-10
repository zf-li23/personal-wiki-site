# How balancing selection maintains MHC polymorphism: a Wright-Fisher model of one MHC locus.
# N diploid individuals (2N gene copies); each copy mutates to a brand-new allele with probability u per
# generation (infinite-alleles model). Under symmetric heterozygote advantage, homozygotes have fitness 1 - s
# and heterozygotes 1, so an allele at frequency p has marginal fitness 1 - s p: rare alleles are favoured.
# Under negative frequency-dependent selection (pathogens adapt to the commonest MHC types) the marginal
# fitness of allele i is 1 - c p_i as well, so both mechanisms give the same frequency-dependent push in this
# minimal form. Illustrative parameters: N = 1000, u = 5e-4 (theta = 4Nu = 2), s in {0, 0.02, 0.1}.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(1)
N, U, GENS = 1000, 5e-4, 6000


def run(s, GENS=GENS):
    counts = np.array([2 * N])
    n_alleles, het = [], []
    for _ in range(GENS):
        p = counts / counts.sum()
        w = p * (1 - s * p)
        w /= w.sum()
        counts = rng.multinomial(2 * N, w)
        m = rng.binomial(counts, U)            # mutations leave their allele ...
        counts = counts - m
        counts = np.concatenate([counts[counts > 0], np.ones(m.sum(), int)])  # ... and found new ones
        p = counts / counts.sum()
        n_alleles.append(int(np.sum(p >= 0.01)))
        het.append(1 - np.sum(p ** 2))
    return np.array(n_alleles), np.array(het), np.sort(p)[::-1]


cases = [(0.0, "neutral (s = 0)", "neutral"), (0.02, "s = 0.02", "dna"), (0.1, "s = 0.1", "negative")]
res = [run(s) for s, _, _ in cases]

fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3))
t = np.arange(GENS)
for (s, name, tok), (na, h, _) in zip(cases, res):
    axs[0].plot(t, na, color=charts.line(tok), lw=1.1, label=name)
    axs[1].plot(t, h, color=charts.line(tok), lw=1.1, label=name)
axs[1].axhline(2 / 3, color=P.muted(), lw=0.8, ls="--")
axs[1].text(GENS * 0.98, 2 / 3 + 0.02, "neutral expectation θ/(1+θ)", fontsize=7, color=P.muted(), ha="right", va="bottom")
charts.style_axes(axs[0], "generation", "alleles at frequency ≥ 1%")
charts.style_axes(axs[1], "generation", "heterozygosity H")
axs[1].set_ylim(0, 1)
svals = np.array([0, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2])
ne = []
for sv in svals:
    _, h, _ = run(sv, 3000)
    ne.append(np.mean(1 / (1 - h[1000:])))
axs[2].plot(svals, ne, "o-", ms=3.5, color=charts.line("protein"), lw=1.2)
axs[2].axhline(1 + 2.0, color=P.muted(), lw=0.8, ls="--")
axs[2].text(0.2, 3.15, "neutral: 1 + θ", fontsize=7, color=P.muted(), ha="right", va="bottom")
charts.style_axes(axs[2], "selection coefficient s", "effective number of alleles 1/(1-H)")
axs[0].legend(frameon=False, fontsize=7, labelcolor=P.ink())
for a, letter in zip(axs, "ABC"):
    charts.title(a, letter)
fig.tight_layout()
