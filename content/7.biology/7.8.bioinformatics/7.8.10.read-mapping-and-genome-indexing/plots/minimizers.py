# Minimizer sampling. A: the (w, k)-minimizers of a 60-nt stretch of a random sequence with k = 5 and
# w = 6: each window of w consecutive k-mers selects its k-mer of smallest hash value (ticks), and
# consecutive windows usually select the same k-mer, so only a fraction of positions are kept.
# B: density (sampled k-mers per position) on a random 200 kb sequence with k = 15 against the window w,
# for a random hash order and for lexicographic order, with the approximation 2/(w + 1).
import numpy as np
import wikibio as bio
from wikibio import charts as C

rng = np.random.default_rng(0)
MASK = np.uint64((1 << 64) - 1)


def kmer_codes(seq, k):
    v = np.zeros(len(seq) - k + 1, dtype=np.uint64)
    for j in range(k):
        v = v * np.uint64(4) + seq[j:len(seq) - k + 1 + j].astype(np.uint64)
    return v


def mix(x):
    x = x.copy()
    x ^= x >> np.uint64(33)
    x *= np.uint64(0xFF51AFD7ED558CCD)
    x ^= x >> np.uint64(33)
    x *= np.uint64(0xC4CEB9FE1A85EC53)
    x ^= x >> np.uint64(33)
    return x


def minimizer_positions(h, w):
    from numpy.lib.stride_tricks import sliding_window_view
    win = sliding_window_view(h, w)
    return np.unique(np.argmin(win, axis=1) + np.arange(win.shape[0]))


seq = rng.integers(0, 4, 200_000)
k = 15
codes = kmer_codes(seq, k)
hashed = mix(codes)
ws = np.arange(2, 51, 2)
dens_h = [len(minimizer_positions(hashed, w)) / len(codes) for w in ws]
dens_l = [len(minimizer_positions(codes, w)) / len(codes) for w in ws]
print("density w=10 hash", dens_h[4], "lex", dens_l[4], "theory", 2 / 11)

fig, ax = bio.canvas(26.0, 9.5)
short = seq[:60]
kk, ww = 5, 6
h2 = mix(kmer_codes(short, kk))
mins = minimizer_positions(h2, ww)
x0, y0, cw = 0.8, 7.2, 0.19
bio.label(ax, (6.5, 8.9), "A  (w, k) = (6, 5) minimizers of a 60-nt sequence", size="small", bold=True)
for i, b in enumerate(short):
    ch = "ACGT"[b]
    bio.label(ax, (x0 + (i + 0.5) * cw, y0), ch, size="tiny", color=bio.P.NUCLEOTIDE[ch])
for r, m in enumerate(mins):
    y = y0 - 0.55 - 0.32 * (r % 6)
    ax.plot([x0 + m * cw, x0 + (m + kk) * cw], [y, y], color=C.line("dna"), lw=2.2, solid_capstyle="butt")
bio.label(ax, (6.5, 4.4), f"{len(mins)} minimizers for {len(short) - kk + 1} k-mers "
          f"(density {len(mins) / (len(short) - kk + 1):.2f}; 2/(w+1) = {2 / (ww + 1):.2f})", size="small")
bio.label(ax, (6.5, 3.7), "any shared substring of w + k - 1 = 10 nt yields a shared minimizer",
          size="small", color=bio.P.muted())
a = C.axes_at(ax, (15.5, 1.5, 9.5, 6.8))
a.plot(ws, dens_h, "o", ms=4, color=C.line("dna"), label="random hash order")
a.plot(ws, dens_l, "s", ms=4, color=C.line("negative"), label="lexicographic order")
wf = np.linspace(2, 50, 200)
a.plot(wf, 2 / (wf + 1), "-", color=C.line("neutral"), lw=1.0, label="2/(w + 1)")
a.set_yscale("log")
C.style_axes(a, "window w (k-mers)", "density (fraction of k-mers kept)")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=bio.P.ink())
C.title(a, "B  Density on 200 kb, k = 15")
