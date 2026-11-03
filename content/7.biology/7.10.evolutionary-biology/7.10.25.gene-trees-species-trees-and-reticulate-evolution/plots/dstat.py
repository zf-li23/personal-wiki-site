"""The D statistic (ABBA-BABA test), simulated under the multispecies coalescent with introgression.
Species tree (((P1, P2), P3), O) with P1 and P2 splitting 0.5 and P3 splitting 1.0 coalescent units
ago (the outgroup O far older); at time 0.2 a fraction f of the genome of P2 is replaced by genes from
P3 (backward in time, a P2 lineage moves into P3 with probability f). For each of 20 000 unlinked loci
a gene tree is simulated, and mutations fall on its branches as a Poisson process (theta = 0.5 per
locus); a derived allele on the branch ancestral to P2 and P3 only gives the site pattern ABBA, on
the branch ancestral to P1 and P3 only BABA. A: numbers of ABBA and BABA sites against f; without
introgression they are equal, because incomplete lineage sorting produces the two discordant gene
trees equally often. B: D = (ABBA - BABA)/(ABBA + BABA), with 95 % intervals from a block jackknife
over 20 blocks of 1000 loci; D departs from 0 as soon as f > 0."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(17)
t12, t123, tO, tm = 0.5, 1.0, 4.0, 0.2
L, theta = 20000, 0.5


def coalesce(lins, t0, t1):
    """lins: list of (set_of_tips, birth_time); coalesce within [t0, t1); returns lins and branches."""
    br = []
    t = t0
    while len(lins) > 1:
        k = len(lins)
        w = rng.exponential(2 / (k * (k - 1)))
        if t + w >= t1:
            break
        t += w
        i, j = rng.choice(k, 2, replace=False)
        a, b = lins[i], lins[j]
        br += [(a[0], t - a[1]), (b[0], t - b[1])]
        lins = [x for q, x in enumerate(lins) if q not in (i, j)] + [(a[0] | b[0], t)]
    return lins, br


def locus(f):
    br = []
    p1, p2, p3 = [({"1"}, 0.0)], [({"2"}, 0.0)], [({"3"}, 0.0)]
    if rng.random() < f:
        p3 = p3 + p2
        p2 = []
    p12 = p1 + p2
    p12, b = coalesce(p12, 0.0, t12)
    br += b
    p3, b = coalesce(p3, 0.0, t123)
    br += b
    pool, b = coalesce(p12, t12, t123)
    br += b
    pool, b = coalesce(pool + p3, t123, tO)
    br += b
    pool, b = coalesce(pool + [({"O"}, 0.0)], tO, np.inf)
    br += b
    abba = sum(l for s, l in br if s == {"2", "3"})
    baba = sum(l for s, l in br if s == {"1", "3"})
    return rng.poisson(theta / 2 * abba), rng.poisson(theta / 2 * baba)


fs = [0.0, 0.02, 0.05, 0.1, 0.2, 0.3]
res = []
for f in fs:
    x = np.array([locus(f) for _ in range(L)])
    A, Bv = x[:, 0], x[:, 1]
    D = (A.sum() - Bv.sum()) / (A.sum() + Bv.sum())
    blocks = np.array_split(np.arange(L), 20)
    jk = []
    for bl in blocks:
        m = np.ones(L, bool)
        m[bl] = False
        jk.append((A[m].sum() - Bv[m].sum()) / (A[m].sum() + Bv[m].sum()))
    jk = np.array(jk)
    se = np.sqrt((len(jk) - 1) / len(jk) * ((jk - jk.mean()) ** 2).sum())
    res.append((A.sum(), Bv.sum(), D, se))
res = np.array(res)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.28)
a.plot(fs, res[:, 0], "o-", color=charts.line("rna"), lw=1.5, ms=4, label="ABBA")
a.plot(fs, res[:, 1], "s-", color=charts.line("dna"), lw=1.5, ms=4, label="BABA")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(a, "introgression fraction $f$ (P3 into P2)", "number of sites")
charts.title(a, "A  Discordant site patterns")
b.errorbar(fs, res[:, 2], yerr=1.96 * res[:, 3], fmt="o-", color=charts.line("rna"), ecolor=P.muted(),
           lw=1.5, ms=4, capsize=3)
b.axhline(0, color=P.muted(), lw=0.7, ls="--")
charts.style_axes(b, "introgression fraction $f$", "$D$")
charts.title(b, "B  The D statistic")
