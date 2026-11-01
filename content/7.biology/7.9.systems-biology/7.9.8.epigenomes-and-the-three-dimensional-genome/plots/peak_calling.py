"""Peak calling for ChIP-seq with a local Poisson background (simulated reads, the logic of MACS). A 2 Mb
region carries 300 binding sites, each giving about 40 fragments (length normal, mean 200 bp, s.d. 25 bp),
on top of 100000 background fragments; a 30 kb stretch has a fourfold higher background in both the ChIP
and the input control (as from an amplified or very open region). Each fragment yields one read, at its
left end on the plus strand or at its right end on the minus strand. A: in a 20 kb window, plus-strand
(above) and minus-strand (below) read starts on either side of the binding sites (dashed), plus starts
upstream and minus starts downstream. B: the strand cross-correlation of read starts over the whole region peaks at the fragment length;
its height relative to the background level is the normalized strand coefficient (NSC). C: after
shifting reads by d/2 toward their 3' ends, the -log10 Poisson p-value of the counts in windows of width
2d, with the genome-wide background lambda_BG (thin) and with the local lambda from the input, the
maximum of lambda_BG and the input rates in 1, 5 and 10 kb around the window (thick); the dotted line is
the threshold p = 1e-5. With the global background the whole biased stretch (shaded) is called as one 30 kb enriched region."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
Lg, nsite, fr_mean = 2_000_000, 300, 200
bias = (1_200_000, 1_230_000)
sites = np.sort(rng.integers(20_000, Lg - 20_000, nsite))
sites[:2] = [1_000_600, 1_006_400]               # two sites in the displayed window
sites = np.sort(sites)


def fragments(n_bg, with_sites):
    starts = [rng.integers(0, Lg, n_bg)]
    nb = int(n_bg * (bias[1] - bias[0]) / Lg * 3)
    starts.append(rng.integers(bias[0], bias[1], nb))
    st = np.concatenate(starts)
    ln = np.clip(rng.normal(fr_mean, 25, st.size), 100, 400).astype(int)
    st = st - ln // 2
    if with_sites:
        k = rng.poisson(40, nsite)
        c = np.repeat(sites, k) + rng.normal(0, 15, k.sum()).astype(int)
        l2 = np.clip(rng.normal(fr_mean, 25, k.sum()), 100, 400).astype(int)
        st = np.concatenate([st, c - l2 // 2]); ln = np.concatenate([ln, l2])
    strand = rng.integers(0, 2, st.size)
    pos = np.where(strand == 0, st, st + ln)
    return pos, strand


cpos, cstr = fragments(100_000, True)
ipos, istr = fragments(100_000, False)

# B: strand cross-correlation
plus = np.bincount(np.clip(cpos[cstr == 0], 0, Lg - 1), minlength=Lg).astype(float)
minus = np.bincount(np.clip(cpos[cstr == 1], 0, Lg - 1), minlength=Lg).astype(float)
shifts = np.arange(0, 601, 5)
pc, mc = plus - plus.mean(), minus - minus.mean()
cc = np.array([np.dot(pc[:Lg - s], mc[s:]) for s in shifts]) / (np.std(plus) * np.std(minus) * Lg)
d = shifts[np.argmax(cc)]
nsc = cc.max() / cc[shifts >= 500].mean()
print("d", d, "NSC", round(nsc, 3), "cc max", cc.max())

# C: shifted tags, windows of 2d, global vs local lambda
step = 50
cent = np.arange(0, Lg, step)
tag = np.where(cstr == 0, cpos + d // 2, cpos - d // 2)
itag = np.where(istr == 0, ipos + d // 2, ipos - d // 2)
cum = np.concatenate([[0], np.cumsum(np.bincount(np.clip(tag, 0, Lg - 1), minlength=Lg))])
icum = np.concatenate([[0], np.cumsum(np.bincount(np.clip(itag, 0, Lg - 1), minlength=Lg))])


def count(cs, c, half):
    lo = np.clip(c - half, 0, Lg); hi = np.clip(c + half, 0, Lg)
    return cs[hi] - cs[lo]


w = 2 * d
k = count(cum, cent, d)
lam_bg = tag.size * w / Lg
lam_loc = np.maximum.reduce([np.full(cent.size, lam_bg)] +
                            [count(icum, cent, h) * w / (2 * h) * tag.size / itag.size for h in (500, 2500, 5000)])
p_bg = stats.poisson.sf(k - 1, lam_bg)
p_loc = stats.poisson.sf(k - 1, lam_loc)


def call(p, thr=1e-5):
    sig = p < thr
    starts = np.flatnonzero(np.diff(np.r_[0, sig.astype(int)]) == 1)
    ends = np.flatnonzero(np.diff(np.r_[sig.astype(int), 0]) == -1)
    mids = cent[(starts + ends) // 2]
    lo_, hi_ = cent[starts] - d, cent[ends] + d
    found = np.array([np.any((lo_ <= x) & (hi_ >= x)) for x in sites])
    width = hi_ - lo_
    false = np.array([not np.any((sites >= a) & (sites <= b)) for a, b in zip(lo_, hi_)])
    return dict(regions=len(mids), sites_found=int(found.sum()), false_regions=int(false.sum()),
                widest_kb=round(width.max() / 1000, 1))


print("lambda_BG", round(lam_bg, 2), "global calls/true/inbias/false", call(p_bg),
      "local", call(p_loc), "sites in bias", np.sum((sites > bias[0]) & (sites < bias[1])))

fig, axs = plt.subplots(1, 3, figsize=(12.8, 3.7), gridspec_kw={"width_ratios": [1.3, 0.8, 1.3]})
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.17, top=0.88, wspace=0.3)
ax = axs[0]
lo, hi = 998_000, 1_009_000
bins = np.arange(lo, hi + 1, 50)
hp, _ = np.histogram(cpos[(cstr == 0)], bins)
hm, _ = np.histogram(cpos[(cstr == 1)], bins)
x = (bins[:-1] - lo) / 1000
ax.bar(x, hp, width=0.05, color=charts.line("negative"), lw=0, label="plus-strand starts")
ax.bar(x, -hm, width=0.05, color=charts.line("dna"), lw=0, label="minus-strand starts")
for sv in sites[(sites > lo) & (sites < hi)]:
    ax.axvline((sv - lo) / 1000, color=P.muted(), lw=0.7, ls="--")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.legend(frameon=False, fontsize=7.5, loc="lower left")
charts.style_axes(ax, f"position (kb, from {lo // 1000} kb)", "reads per 50 bp")
charts.title(ax, "A  Strand-specific read starts")

ax = axs[1]
ax.plot(shifts, cc, color=charts.line("dna"), lw=1.4)
ax.axvline(d, color=P.muted(), lw=0.7, ls="--")
ax.text(d + 15, cc.max() * 0.93, f"d = {d} bp\nNSC = {nsc:.2f}", fontsize=7.5, color=P.ink())
charts.style_axes(ax, "strand shift (bp)", "cross-correlation")
charts.title(ax, "B  Strand cross-correlation")

ax = axs[2]
lo2, hi2 = 1_170_000, 1_260_000
m = (cent >= lo2) & (cent < hi2)
xx = (cent[m] - lo2) / 1000
ax.axvspan((bias[0] - lo2) / 1000, (bias[1] - lo2) / 1000, color=P.fill("neutral"), alpha=0.5, lw=0)
ax.plot(xx, -np.log10(p_bg[m]), color=charts.line("rna"), lw=0.7, label="global lambda_BG")
ax.plot(xx, -np.log10(p_loc[m]), color=charts.line("dna"), lw=1.5, label="local lambda (input)")
ax.axhline(5, color=P.muted(), lw=0.8, ls=":")
for sv in sites[(sites > lo2) & (sites < hi2)]:
    ax.plot((sv - lo2) / 1000, -0.8, "^", color=P.ink(), ms=4)
ax.set_ylim(-1.5, None)
ax.legend(frameon=False, fontsize=7.5, loc="upper right")
charts.style_axes(ax, f"position (kb, from {lo2 // 1000} kb); triangles: true sites", "-log10 p")
charts.title(ax, "C  Global versus local background")
