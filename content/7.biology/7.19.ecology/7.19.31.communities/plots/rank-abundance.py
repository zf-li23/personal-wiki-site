"""Species abundance models as rank-abundance diagrams, and Preston's octave plot.

A: expected relative abundance against rank for S = 25 species: geometric series with pre-emption
fraction k = 0.4, p_i = k (1 - k)^(i-1) / (1 - (1 - k)^S); MacArthur's broken stick,
p_i = (1/S) sum_{j=i..S} 1/j; a log-series (Fisher's alpha = 5, N = 1000: species expected at each
abundance n, alpha x^n / n, sorted); and a log-normal (expected order statistics of a log-normal with
log-sd 1.2). Log scale: the geometric series is a straight line, the broken stick the most even.
B, C: Preston's octave plot of samples of N = 500 (B) and N = 20 000 (C) individuals from one simulated
community of 300 species with log-normal abundances (log-sd 1.6): number of species with 1, 2-3, 4-7,
8-15 ... individuals (octaves log2). The small sample truncates the distribution at the "veil line":
most species are unseen or rare, and the mode lies at the left; the large sample uncovers the mode of
the log-normal.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(7)
S = 25
r = np.arange(1, S + 1)
k = 0.4
geo = k * (1 - k) ** (r - 1) / (1 - (1 - k) ** S)
bs = np.array([np.sum(1 / np.arange(i, S + 1)) for i in r]) / S
# log-series: expected number of species with n individuals alpha x^n / n; build abundance vector
alpha, N = 5.0, 1000
x = N / (N + alpha)
ns = np.arange(1, 2000)
expect = alpha * x**ns / ns
cum = np.cumsum(expect[::-1])[::-1]
ls = np.array([ns[np.searchsorted(-cum, -(i - 0.5))] if i - 0.5 <= cum[0] else 1 for i in range(1, int(cum[0]) + 1)])
ls = np.sort(ls)[::-1].astype(float)
ls = ls / ls.sum()
from scipy.stats import norm
q = norm.ppf((S - r + 0.625) / (S + 0.25))
ln = np.exp(1.2 * q)
ln = ln / ln.sum()

fig, ax = bio.canvas(33.0, 11.0)
pa = C.axes_at(ax, (2.0, 1.8, 9.0, 7.5))
pa.semilogy(r, geo, "o-", color=Q.line_color("negative"), ms=3.5, lw=1.4, label="geometric series (k = 0.4)")
pa.semilogy(np.arange(1, len(ls) + 1), ls, "s-", color=Q.line_color("highlight"), ms=3.5, lw=1.4,
            label=f"log-series (alpha = 5, S = {len(ls)})")
pa.semilogy(r, ln, "^-", color=Q.line_color("dna"), ms=3.5, lw=1.4, label="log-normal (log-sd 1.2)")
pa.semilogy(r, bs, "D-", color=Q.line_color("plant"), ms=3.5, lw=1.4, label="broken stick")
pa.set_xlim(0, 32)
C.style_axes(pa, "species rank", "relative abundance p_i")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.3, 10.7))
bio.label(ax, (2.0, 10.0), "Rank-abundance diagrams", size="small", bold=True, ha="left")

pcom = np.exp(rng.normal(0, 1.6, 300))
pcom /= pcom.sum()
for j, (Ns, letter) in enumerate(((500, "B"), (20000, "C"))):
    c = rng.multinomial(Ns, pcom)
    c = c[c > 0]
    octv = np.floor(np.log2(c)).astype(int)
    bins = np.bincount(octv)
    x0 = 14.5 + 9.5 * j
    pb = C.axes_at(ax, (x0, 1.8, 7.5, 7.5))
    pb.bar(np.arange(len(bins)), bins, width=0.85, color=P.fill("plant"), edgecolor=P.edge("plant"), lw=0.6)
    labels = ["1", "2-3", "4-7", "8-15", "16-31", "32-63", "64-127", "128-255", "256-511", "512-1023", "1024+"]
    pb.set_xticks(np.arange(len(bins)), labels[:len(bins)], rotation=60, fontsize=FS["tiny"])
    pb.axvline(-0.5, color=P.ink(), lw=1.2, ls=(0, (4, 2)))
    pb.text(-0.3, bins.max() * 1.02, "veil line", fontsize=FS["tiny"], color=P.ink())
    pb.set_ylim(0, bins.max() * 1.15)
    C.style_axes(pb, "individuals per species (octave)", "number of species")
    bio.panel(ax, letter, (x0 - 1.6, 10.7))
    bio.label(ax, (x0, 10.0), f"N = {Ns}: {len(c)} of 300 species seen", size="small", bold=True, ha="left")
