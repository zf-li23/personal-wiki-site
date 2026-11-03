"""The serial founder model of human expansion (Section 33.3.3). A chain of 25 populations is founded
one after another, each by 50 individuals drawn from the previous one, which then grow to 2000 and
exchange migrants with their neighbours (m = 0.002 per generation); 300 unlinked neutral loci with
initial heterozygosity of about 0.3 in the source population. A: expected heterozygosity in each
population after the expansion falls almost linearly with distance from the source, as observed in
human populations with distance from East Africa. B: for pairs of populations at increasing distance
along the chain, the proportion of the total genetic variation found within populations remains high;
differences increase gradually with distance (a cline), without discrete groups."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(9)
L, D, F, Nmax, m = 300, 25, 50, 2000, 0.002
p0 = rng.beta(0.6, 0.6, L)
p0 = np.clip(p0, 0.02, 0.98)
pops = [p0.copy()]
for d in range(1, D):
    # founding from previous population
    pf = rng.binomial(2 * F, pops[-1]) / (2 * F)
    pops.append(pf)
    # all populations drift and migrate for 40 generations between foundings
    for g in range(40):
        arr = np.array(pops)
        new = arr.copy()
        for i in range(len(pops)):
            nb = [j for j in (i - 1, i + 1) if 0 <= j < len(pops)]
            mix = (1 - m * len(nb)) * arr[i] + m * sum(arr[j] for j in nb)
            N = Nmax if i < len(pops) - 1 else min(Nmax, F * 2 ** (g // 4 + 1))
            new[i] = rng.binomial(2 * N, np.clip(mix, 0, 1)) / (2 * N)
        pops = list(new)
arr = np.array(pops)
H = 2 * arr * (1 - arr)
fig, (a, b) = plt.subplots(1, 2, figsize=(9.8, 3.4))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.87, wspace=0.3)
a.plot(np.arange(D), H.mean(axis=1), "o-", ms=4, color=charts.line("dna"), lw=1.4)
charts.style_axes(a, "order of founding (distance from source)", "heterozygosity")
charts.title(a, "A  Diversity declines with distance")
within = []
dist = np.arange(1, D)
for k in dist:
    w = []
    for i in range(0, D - k):
        pa, pb = arr[i], arr[i + k]
        hs = (2 * pa * (1 - pa) + 2 * pb * (1 - pb)) / 2
        pbar = (pa + pb) / 2
        ht = 2 * pbar * (1 - pbar)
        w.append(hs.sum() / ht.sum())
    within.append(np.mean(w))
b.plot(dist, within, "o-", ms=4, color=charts.line("plant"), lw=1.4)
b.set_ylim(0, 1.02)
charts.style_axes(b, "distance between two populations (steps)", "fraction of variation within populations")
charts.title(b, "B  Most variation is within populations")
