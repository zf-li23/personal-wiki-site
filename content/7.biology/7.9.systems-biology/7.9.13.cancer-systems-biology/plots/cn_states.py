"""Allele-specific copy number from tumor sequencing (simulation). A genome of six segments carries
the allele-specific states (major, minor) = (1, 1), (2, 1), (1, 0), (2, 0), (2, 2) and (3, 1) in a
tumor sample of purity 0.7 (30 % normal cells); 500 heterozygous SNPs per segment are sequenced at
a depth of 60 reads. A: log ratio of tumor to normal depth, logR = log2[(2(1 - rho) + rho n)/
(2(1 - rho) + rho psi)], with segment means (line); n is the total copy number and psi the average
tumor ploidy. B: B-allele fraction of the heterozygous SNPs, which splits into two bands at
(1 - rho + rho n_B)/(2(1 - rho) + rho n) and its mirror image. Copy-neutral loss of heterozygosity
(2, 0) is visible in B but not in A. C: fit of purity and ploidy: for each pair (rho, psi) every
segment is assigned the nearest integer state and the distance of the observed segment means from
the predicted values is summed; the minimum (cross) lies at the true purity and ploidy (circle)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
states = [(1, 1), (2, 1), (1, 0), (2, 0), (2, 2), (3, 1)]
rho, n_snp, depth = 0.7, 500, 60
n_tot = np.array([a + b for a, b in states])
psi = n_tot.mean()


def predict(r, ps, a, b):
    n = a + b
    logr = np.log2((2 * (1 - r) + r * n) / (2 * (1 - r) + r * ps))
    baf = (1 - r + r * b) / (2 * (1 - r) + r * n)
    return logr, baf


pos, logr, baf, seg_logr, seg_baf = [], [], [], [], []
for s, (a, b) in enumerate(states):
    lr, bf = predict(rho, psi, a, b)
    x = s + np.sort(rng.random(n_snp))
    l = lr + rng.normal(0, 0.18, n_snp)
    flip = rng.random(n_snp) < 0.5
    k = rng.binomial(depth, np.where(flip, 1 - bf, bf))
    f = k / depth
    pos.append(x); logr.append(l); baf.append(f)
    seg_logr.append(l.mean())
    seg_baf.append(np.abs(f - 0.5).mean())       # mirrored distance from 0.5
pos, logr, baf = map(np.concatenate, (pos, logr, baf))
seg_logr, seg_baf = np.array(seg_logr), np.array(seg_baf)
cand = [(a, b) for a in range(0, 6) for b in range(0, a + 1) if a + b > 0]


def mirrored_expect(r, n, b):
    """Mean of |f - 0.5| for binomial read counts at fraction bf (exact over the binomial)."""
    _, bf = predict(r, 2, n - b, b)
    k = np.arange(depth + 1)
    from scipy.stats import binom
    return np.sum(binom.pmf(k, depth, bf) * np.abs(k / depth - 0.5))


rhos = np.linspace(0.3, 1.0, 36)
psis = np.linspace(1.5, 4.5, 41)
expect = {(r, a, b): mirrored_expect(r, a + b, b) for r in rhos for a, b in cand}
D = np.zeros((len(psis), len(rhos)))
for i, ps in enumerate(psis):
    for j, r in enumerate(rhos):
        tot = 0.0
        for lr_o, bf_o in zip(seg_logr, seg_baf):
            tot += min((lr_o - predict(r, ps, a, b)[0]) ** 2 / 0.05 ** 2 +
                       (bf_o - expect[(r, a, b)]) ** 2 / 0.02 ** 2 for a, b in cand)
        D[i, j] = tot
ib, jb = np.unravel_index(np.argmin(D), D.shape)

fig = plt.figure(figsize=(11, 4.4))
axA = fig.add_axes([0.06, 0.58, 0.58, 0.34])
axB = fig.add_axes([0.06, 0.12, 0.58, 0.34])
axC = fig.add_axes([0.74, 0.12, 0.24, 0.8])
axA.plot(pos, logr, ".", ms=1.2, color=charts.line("dna"), alpha=0.5)
for s in range(6):
    axA.plot([s, s + 1], [seg_logr[s]] * 2, color=charts.line("negative"), lw=2)
    axA.text(s + 0.5, 1.05, f"{states[s][0]}+{states[s][1]}", ha="center", fontsize=7, color=P.ink())
    for ax in (axA, axB):
        ax.axvline(s, color=P.muted(), lw=0.5)
axA.set_ylim(-1.45, 1.25)
axA.set_xlim(0, 6)
axA.set_xticks([])
charts.style_axes(axA, None, "logR")
charts.title(axA, "A  Depth ratio (segment states: major+minor)")
axB.plot(pos, baf, ".", ms=1.2, color=charts.line("highlight"), alpha=0.5)
axB.set_xlim(0, 6)
axB.set_ylim(0, 1)
axB.set_xticks([])
charts.style_axes(axB, "position (segments)", "B-allele fraction")
charts.title(axB, "B  B-allele fraction of heterozygous SNPs")
im = axC.pcolormesh(rhos, psis, np.log10(D), cmap="viridis_r", shading="auto")
axC.plot(rhos[jb], psis[ib], "x", color="white", ms=9, mew=2)
axC.plot(rho, psi, "o", mfc="none", mec="white", ms=11, mew=1.2)
charts.style_axes(axC, "purity rho", "ploidy psi", box=True)
charts.title(axC, "C  log10 distance")
cb = fig.colorbar(im, ax=axC, fraction=0.05, pad=0.03)
cb.ax.tick_params(labelsize=7)
