# Statistical positioning (Kornberg and Stryer 1988) computed exactly. Nucleosomes are hard rods of 147 bp on a
# 1-bp lattice with no sequence preference; a bound factor (a barrier) occupies the left end. The grand partition
# function of a segment obeys Z(i) = Z(i-1) + z Z(i-147), and forward-backward recursion gives the probability
# that a nucleosome is centred (its dyad) on each base pair. Only the barrier and the packing density (fugacity z, chosen so
# that the mean linker is about 40 bp or 20 bp) are imposed, yet nucleosomes next to the barrier are well
# positioned: the dyad density oscillates with the repeat length and the order decays over a few nucleosomes, faster at
# lower density. The profiles are blurred by a 15 bp Gaussian, about the resolution of nucleosome maps. The first peak is the "+1 nucleosome" of a promoter.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
w = 147
L = 6000


def coverage(logz):
    lf = np.full(L + 1, -np.inf)  # log Z of segment [0, i)
    lf[0] = 0.0
    for i in range(1, L + 1):
        lf[i] = np.logaddexp(lf[i - 1], logz + lf[i - w]) if i >= w else lf[i - 1]
    lb = np.full(L + 1, -np.inf)  # log Z of segment [i, L)
    lb[L] = 0.0
    for i in range(L - 1, -1, -1):
        lb[i] = np.logaddexp(lb[i + 1], logz + lb[i + w]) if i + w <= L else lb[i + 1]
    start = np.zeros(L)
    s = np.arange(0, L - w + 1)
    start[s] = np.exp(logz + lf[s] + lb[s + w] - lf[L])
    cov = np.convolve(start, np.ones(w))[:L]
    return start, cov


def mean_linker(cov):
    mid = cov[L // 3: 2 * L // 3].mean()
    return w / mid - w


fig, ax = bio.canvas(19.0, 7.6)
a = C.axes_at(ax, (1.6, 1.3, 16.6, 4.8))
x = np.arange(L)
for logz, tok in [(0.0, "neutral"), (3.0, "chromatin")]:
    st, cov = coverage(logz)
    dyad = np.r_[np.zeros(w // 2), st[:-(w // 2)]] * 100  # nucleosome centres per 100 bp
    k = np.arange(-60, 61)
    g = np.exp(-k ** 2 / (2 * 15.0 ** 2))
    dyad = np.convolve(dyad, g / g.sum(), mode="same")  # 15 bp blur, like the resolution of MNase-seq
    a.plot(x, dyad, color=C.line(tok), lw=1.6, label=f"mean linker ≈ {mean_linker(cov):.0f} bp")
a.axvspan(-60, 0, color=P.fill("receptor"), lw=0)
a.text(-30, 2.05, "barrier", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.annotate("+1 nucleosome", (w / 2 + 12, 1.75), (300, 1.95), fontsize=bio.core.FONT["tiny"], color=P.ink(),
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
a.set_xlim(-60, 1500)
a.set_ylim(0, 2.2)
a.set_xticks([0, 250, 500, 750, 1000, 1250, 1500])
a.set_yticks([0, 0.5, 1.0, 1.5, 2.0])
C.style_axes(a, "distance from barrier / bp", "dyad density / (100 bp)$^{-1}$")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
bio.label(ax, (1.0, 7.1), "Statistical positioning of hard-core nucleosomes next to a barrier", size="normal", bold=True, ha="left")
