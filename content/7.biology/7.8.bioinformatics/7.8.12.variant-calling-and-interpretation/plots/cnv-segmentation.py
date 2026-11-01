# Copy number from read depth (simulated). Read counts in 1 kb windows along 2 Mb of a diploid genome
# at a mean of 30 reads per window (Poisson, with window-to-window variation of 10 % in mappability and
# GC bias), carrying a heterozygous deletion (copy number 1) of 150 kb and a duplication (copy number 3)
# of 300 kb. A: log2 ratios of the counts to the diploid mean. Binary segmentation finds the change
# points: it splits a segment where the two-sample t statistic of the means on either side is largest,
# keeps the split if that statistic exceeds 6, and recurses (red lines: segment means). B: the segment
# means converted to copy number, 2 x 2^(log2 ratio), recover 1, 2 and 3.
import numpy as np
import wikibio as bio
from wikibio import charts as C

rng = np.random.default_rng(0)
NW = 2000
cn = np.full(NW, 2.0)
cn[500:650] = 1.0
cn[1200:1500] = 3.0
bias = rng.lognormal(0.0, 0.10, NW)
counts = rng.poisson(30.0 * cn / 2 * bias)
lr = np.log2(np.maximum(counts, 0.5) / 30.0)


def best_split(x):
    n = len(x)
    if n < 20:
        return None, 0.0
    cs = np.cumsum(x)
    css = np.cumsum(x * x)
    i = np.arange(10, n - 10)
    m1 = cs[i - 1] / i
    m2 = (cs[-1] - cs[i - 1]) / (n - i)
    var = (css[-1] - i * m1 ** 2 - (n - i) * m2 ** 2) / (n - 2)
    t = np.abs(m1 - m2) / np.sqrt(var * (1.0 / i + 1.0 / (n - i)))
    j = int(np.argmax(t))
    return int(i[j]), float(t[j])


def segment(x, lo, hi, out, thr=6.0):
    k, t = best_split(x[lo:hi])
    if k is None or t < thr:
        out.append((lo, hi))
        return
    segment(x, lo, lo + k, out, thr)
    segment(x, lo + k, hi, out, thr)


segs = []
segment(lr, 0, NW, segs)
segs.sort()
print([(a, b, round(float(lr[a:b].mean()), 3), round(2 * 2 ** float(lr[a:b].mean()), 2)) for a, b in segs])
fig, ax = bio.canvas(24.0, 10.0)
pos = np.arange(NW) / 1000.0
a = C.axes_at(ax, (2.0, 5.8, 21.0, 3.4))
a.plot(pos, lr, ".", ms=1.5, color=C.line("neutral"))
for s, e in segs:
    a.plot([pos[s], pos[e - 1]], [lr[s:e].mean()] * 2, color=C.line("negative"), lw=2.0)
a.set_ylim(-2.2, 1.8)
C.style_axes(a, None, "log2 ratio")
C.title(a, "A  Depth in 1 kb windows and segmentation")
b = C.axes_at(ax, (2.0, 1.2, 21.0, 3.0))
b.step(pos, cn, where="post", color=C.line("dna"), lw=1.0, ls="--", label="true copy number")
for s, e in segs:
    b.plot([pos[s], pos[e - 1]], [2 * 2 ** lr[s:e].mean()] * 2, color=C.line("negative"), lw=2.0)
b.plot([], [], color=C.line("negative"), lw=2.0, label="estimated from segment means")
b.set_ylim(0.5, 3.6)
C.style_axes(b, "position (Mb)", "copy number")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=bio.P.ink(), loc="upper left")
C.title(b, "B  Copy number")
