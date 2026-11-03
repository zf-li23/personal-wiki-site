"""Simulated F_ST scan. 5000 SNPs with ancestral frequencies p ~ U(0.05, 0.95); in each of two populations
the frequency is drawn from Beta(p(1 - F)/F, (1 - p)(1 - F)/F) (Balding-Nichols) with F = 0.05 for neutral
SNPs and F = 0.5 at five selected sites; SNPs within 5 positions of a selected site get an intermediate F
that decays with distance. 100 chromosomes are sampled per population and Hudson's estimator
N/D = [(p1 - p2)^2 - p1(1 - p1)/(n1 - 1) - p2(1 - p2)/(n2 - 1)] / [p1(1 - p2) + p2(1 - p1)] is computed
per SNP. A: F_ST along the SNP index (dashed: 99.9th percentile of neutral SNPs). B: distribution for
neutral SNPs (log scale) and values at the selected sites."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(41)
m, nsamp = 5000, 100
p = rng.uniform(0.05, 0.95, m)
F = np.full(m, 0.05)
sites = np.array([700, 1650, 2400, 3500, 4300])
for c in sites:
    for d in range(-5, 6):
        F[c + d] = max(F[c + d], 0.5 * np.exp(-abs(d) / 2))
a_ = p * (1 - F) / F
b_ = (1 - p) * (1 - F) / F
p1, p2 = rng.beta(a_, b_), rng.beta(a_, b_)
h1, h2 = rng.binomial(nsamp, p1) / nsamp, rng.binomial(nsamp, p2) / nsamp
num = (h1 - h2) ** 2 - h1 * (1 - h1) / (nsamp - 1) - h2 * (1 - h2) / (nsamp - 1)
den = h1 * (1 - h2) + h2 * (1 - h1)
fst = np.where(den > 0, num / np.where(den > 0, den, 1), 0)
neutral = F == 0.05
thr = np.quantile(fst[neutral], 0.999)
fig, (a, b) = plt.subplots(1, 2, figsize=(11.0, 3.7), gridspec_kw={"width_ratios": [2, 1]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.9, wspace=0.25)
a.scatter(np.where(neutral)[0], fst[neutral], s=3, color=P.mix(P.muted(), P.surface(), 0.2), lw=0)
a.scatter(np.where(~neutral)[0], fst[~neutral], s=10, color=charts.line("rna"), lw=0, zorder=3)
a.axhline(thr, color=P.ink(), lw=0.8, ls="--")
a.set_xlim(0, m)
a.set_ylim(-0.05, 1)
charts.style_axes(a, "SNP position (index along the genome)", "$F_{\\mathrm{ST}}$ (Hudson)")
charts.title(a, "A  Scan of 5000 SNPs, five selected regions")
b.hist(fst[neutral], bins=np.linspace(-0.05, 1, 43), color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.4,
       label="neutral SNPs")
for v in fst[sites]:
    b.axvline(v, color=charts.line("rna"), lw=1.2)
b.plot([], [], color=charts.line("rna"), lw=1.2, label="selected sites")
b.axvline(thr, color=P.ink(), lw=0.8, ls="--")
b.set_yscale("log")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(b, "$F_{\\mathrm{ST}}$", "number of SNPs")
charts.title(b, "B  Neutral distribution")
