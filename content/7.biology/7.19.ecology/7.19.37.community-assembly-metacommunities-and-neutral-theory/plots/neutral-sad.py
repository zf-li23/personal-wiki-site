"""Species abundance distributions of the neutral theory.

Expected number of species with n individuals in a local community of J = 21 000 trees (the size of
the Barro Colorado Island 50 ha plot) with fundamental biodiversity number theta = 50 and immigration
probability m, computed exactly from
    E[S_n] = int_0^1 theta x^-1 (1 - x)^(theta - 1) BetaBinomial(n; J, I x, I (1 - x)) dx,
    I = m (J - 1) / (1 - m),
i.e. metacommunity relative abundances x with the log-series density of the Ewens sampling formula,
each turned into a local abundance by the stationary distribution of a Moran process with immigration.
A: Preston plot (octaves 1, 2-3, 4-7, ...). m = 0.1 (bars; total 235 species) is the value fitted to
BCI by Hubbell; the dashed curve is a normal distribution in log2 abundance fitted by least squares to
those bars (a lognormal). Without dispersal limitation (m -> 1) the local sample is a log-series
(302 species, mode in the first octave); strong dispersal limitation (m = 0.01) lowers richness and
removes rare species. B: the same three distributions as rank-abundance curves.
"""

import numpy as np
from scipy.optimize import curve_fit
from scipy.special import betaln, gammaln

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)

J, theta = 21000, 50.0


def sad(m, nx=1600):
    I = m * (J - 1) / (1 - m)
    u = np.linspace(np.log(1e-12), np.log(1 - 1e-9), nx)
    x = np.exp(u)
    w = theta * (1 - x) ** (theta - 1) * np.gradient(u)  # density in u = ln x
    a, b = I * x, I * (1 - x)
    out = np.zeros(J)
    n = np.arange(1, J + 1)
    for k in range(0, J, 1500):
        nn = n[k:k + 1500][:, None]
        lp = gammaln(J + 1) - gammaln(nn + 1) - gammaln(J - nn + 1) + betaln(nn + a, J - nn + b) - betaln(a, b)
        out[k:k + 1500] = (np.exp(lp) * w).sum(1)
    return out


cases = [(0.1, "m = 0.1", "dna"), (1 - 1e-7, "m = 1 (log-series)", "rna"), (0.01, "m = 0.01", "positive")]
sads = {lab: sad(m) for m, lab, _ in cases}

octs = int(np.log2(J)) + 1
n = np.arange(1, J + 1)
oc = np.floor(np.log2(n)).astype(int)


def octaves(s):
    return np.bincount(oc, weights=s, minlength=octs)


pa = C.axes_at(ax, (2.6, 1.9, 11.6, 8.4))
k = np.arange(octs)
s01 = octaves(sads["m = 0.1"])
pa.bar(k, s01, width=0.8, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.8,
       label=f"m = 0.1 (S = {sads['m = 0.1'].sum():.0f})")
for m, lab, tok in cases[1:]:
    pa.plot(k, octaves(sads[lab]), "o-", ms=3, color=Q.line_color(tok), lw=1.3, label=f"{lab} (S = {sads[lab].sum():.0f})")
f = lambda r, s0, r0, sd: s0 * np.exp(-((r - r0) ** 2) / (2 * sd ** 2))
pp, _ = curve_fit(f, k, s01, p0=(30, 5, 3))
kk = np.linspace(0, octs - 1, 200)
pa.plot(kk, f(kk, *pp), color=P.ink(), lw=1.2, ls="--", label="lognormal fit to m = 0.1")
pa.set_xticks(k[::2])
pa.set_xticklabels([str(2 ** int(i)) for i in k[::2]])
pa.set_xlim(-0.7, octs - 0.3)
C.style_axes(pa, "abundance class (octave lower bound, individuals)", "number of species")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.5, 11.6))
bio.label(ax, (2.6, 11.2), "Preston plot: J = 21 000, theta = 50", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (18.0, 1.9, 11.0, 8.4))
for m, lab, tok in cases:
    s = sads[lab]
    tail = np.cumsum(s[::-1])[::-1]  # expected number of species with abundance >= n
    S = s.sum()
    ranks = np.arange(1, int(S) + 1)
    ab = np.interp(ranks, tail[::-1], n[::-1])  # abundance at which tail count equals rank
    pb.semilogy(ranks, ab, color=Q.line_color(tok), lw=1.5, label=lab)
pb.set_xlim(0, 310)
pb.set_ylim(0.8, 3e3)
C.style_axes(pb, "species rank", "abundance (individuals)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (15.8, 11.6))
bio.label(ax, (18.0, 11.2), "Rank-abundance curves", size="small", bold=True, ha="left")
