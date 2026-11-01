"""Two signatures of ATAC-seq data (simulated). A: the length distribution of about 200000 sequenced fragments:
fragments from nucleosome-free DNA (below about 150 bp, with a 10.5 bp modulation from the helical pitch of
DNA on which Tn5 cuts one face), and fragments spanning one, two and three nucleosomes (peaks near 200,
400 and 600 bp), above a smooth background of unphased fragments; the inset is on a linear scale. B: transposase insertions around 1000 binding sites of a
transcription factor, aggregated: within an accessible region the bound factor protects about 20 bp
from insertion (a footprint), for half of the sites (bound) but not for the other half (unbound).
C: the footprint occupancy score FOS = (C + 1)/L + (C + 1)/R of single sites, from the insertions in the
central 20 bp (C) and in 30 bp flanks on each side (L, R): low values indicate a footprint."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)

# A: fragment lengths
n = 200_000
w = np.array([0.44, 0.30, 0.13, 0.05, 0.08])
k = rng.choice(5, n, p=w)
L = np.empty(n)
m0 = k == 0
L[m0] = rng.gamma(4.0, 18.0, m0.sum()) + 25
# helical modulation: thin nucleosome-free fragments by 1 + 0.35 cos(2 pi L / 10.5)
keep = rng.uniform(0, 1, n) < np.where(m0, (1 + 0.35 * np.cos(2 * np.pi * L / 10.5)) / 1.35, 1)
for j, (mu, sd) in enumerate([(195, 22), (390, 32), (585, 42)], start=1):
    mj = k == j
    L[mj] = rng.normal(mu, sd, mj.sum())
m4 = k == 4                                      # unphased background of all lengths
L[m4] = 30 + rng.exponential(250, m4.sum())
L = np.round(L[keep & (L > 30) & (L < 900)]).astype(int)
h = np.bincount(L, minlength=901)[:901]
x = np.arange(901)
seg = h[40:150].astype(float)
seg = seg - np.convolve(seg, np.ones(15) / 15, mode="same")
seg = seg[10:-10] * np.hanning(seg.size - 20)
f = np.fft.rfftfreq(8192)[1:]
spec = np.abs(np.fft.rfft(seg, 8192))[1:]
mask = (1 / f > 6) & (1 / f < 20)
period = 1 / f[mask][np.argmax(spec[mask])]
nfr = np.mean(L < 147)
print("fragments", L.size, "fraction <147", round(nfr, 3), "dominant short period", round(period, 2),
      "modes", [int(np.argmax(h[a:b]) + a) for a, b in [(150, 300), (300, 500), (500, 750)]])

fig, axs = plt.subplots(1, 3, figsize=(12.8, 3.7), gridspec_kw={"width_ratios": [1.3, 1.1, 0.9]})
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.17, top=0.88, wspace=0.3)
ax = axs[0]
ax.semilogy(x[30:], np.maximum(h[30:], 0.5), color=charts.line("dna"), lw=1.0)
for xv, t in [(75, "nucleosome-\nfree"), (205, "1"), (390, "2"), (585, "3")]:
    ax.text(xv, h[xv] * 2.2, t, fontsize=7.5, color=P.ink(), ha="center")
ax.set_ylim(5, h.max() * 6)
charts.style_axes(ax, "fragment length (bp)", "fragments (log scale)")
charts.title(ax, "A  Fragment lengths: a nucleosome ladder")
ins = ax.inset_axes([0.66, 0.55, 0.32, 0.28])
ins.plot(x[40:151], h[40:151], color=charts.line("dna"), lw=0.9)
charts.style_axes(ins)
ins.set_title(f"40-150 bp: period {period:.1f} bp", fontsize=6.5, color=P.ink())
ins.tick_params(labelsize=6)

# B, C: footprints
S, half = 1000, 150
pos = np.arange(-half, half + 1)
rate = 0.2 * np.exp(-(pos / 110.0) ** 2) + 0.03
core = np.abs(pos) <= 10
bound = np.r_[np.ones(S // 2, bool), np.zeros(S // 2, bool)]
R = np.tile(rate, (S, 1))
R[np.ix_(bound, core)] *= 0.15
R *= rng.gamma(4, 0.25, (S, 1))                  # site-to-site accessibility
cuts = rng.poisson(R)
ax = axs[1]
for msk, tok, name in [(bound, "dna", "bound sites"), (~bound, "rna", "unbound sites")]:
    prof = cuts[msk].mean(0)
    ax.plot(pos, np.convolve(prof, np.ones(3) / 3, mode="same"), color=charts.line(tok), lw=1.3, label=name)
ax.axvspan(-10, 10, color=P.fill("neutral"), alpha=0.25, lw=0)
ax.text(0, ax.get_ylim()[1] * 0.97, "motif", ha="center", va="top", fontsize=7.5, color=P.ink())
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
charts.style_axes(ax, "position relative to motif center (bp)", "insertions per site per bp")
charts.title(ax, "B  Aggregate footprint")

C = cuts[:, core].sum(1)
Lf = cuts[:, (pos >= -40) & (pos < -10)].sum(1)
Rf = cuts[:, (pos > 10) & (pos <= 40)].sum(1)
fos = (C + 1) / np.maximum(Lf, 1) + (C + 1) / np.maximum(Rf, 1)
ax = axs[2]
bins = np.linspace(0, 3, 31)
ax.hist(fos[bound], bins=bins, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.4, alpha=0.85, label="bound")
ax.hist(fos[~bound], bins=bins, histtype="step", color=charts.line("rna"), lw=1.4, label="unbound")
thr = 1.0
print("FOS median bound/unbound", np.median(fos[bound]), np.median(fos[~bound]),
      "FOS<1: bound", np.mean(fos[bound] < thr), "unbound", np.mean(fos[~bound] < thr))
ax.axvline(thr, color=P.muted(), lw=0.8, ls="--")
ax.legend(frameon=False, fontsize=7.5, loc="upper right")
charts.style_axes(ax, "footprint occupancy score", "sites")
charts.title(ax, "C  Single-site scores")
