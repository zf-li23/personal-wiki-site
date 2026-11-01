# Scanning with a position weight matrix: score distributions and thresholds. The PWM of the CTCF matrix
# (MA0139.1, weights of the previous figure, rounded to 0.01 bit) gives every 19-bp window a score. A: the
# exact distribution of the score of a random window (background q = 0.295/0.205/0.205/0.295) and of a
# window drawn from the motif model, both computed by convolution over positions (Algorithm 8.3.1), on a
# log scale; vertical lines are the thresholds with background p-values 1e-4, 1e-5 and 1e-6. B: the
# trade-off as the threshold moves: the expected number of chance matches in a genome of 3.1 Gb scanned
# on both strands (left axis, log scale) and the fraction of motif-model sites above the threshold
# (right axis). Even at p = 1e-6 thousands of chance matches remain, of the order of the number of
# true binding sites.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
CTCF = np.array([[87, 291, 76, 459], [167, 145, 414, 187], [281, 49, 449, 134], [56, 800, 21, 36],
                 [8, 903, 0, 2], [744, 13, 65, 91], [40, 528, 334, 11], [107, 433, 48, 324],
                 [851, 11, 32, 18], [5, 0, 903, 3], [333, 3, 566, 9], [54, 12, 504, 341], [12, 0, 890, 8],
                 [56, 8, 775, 71], [104, 733, 5, 67], [372, 13, 507, 17], [82, 482, 307, 37],
                 [117, 322, 73, 396], [402, 181, 266, 59]], float)
q = np.array([0.295, 0.205, 0.205, 0.295])
N = CTCF.sum(1, keepdims=True)
pm = (CTCF + 0.8 * q) / (N + 0.8)
Wi = np.round(np.log2(pm / q) * 100).astype(int)


def distribution(probs):
    vec, low = np.ones(1), 0
    for j in range(len(Wi)):
        lo = Wi[j].min()
        new = np.zeros(len(vec) + Wi[j].max() - lo)
        for b in range(4):
            s = Wi[j, b] - lo
            new[s:s + len(vec)] += vec * probs[j][b]
        vec, low = new, low + lo
    return low, vec


low, bgd = distribution([q] * len(Wi))
_, mot = distribution(pm)
score = (np.arange(len(bgd)) + low) / 100
sf_b = bgd[::-1].cumsum()[::-1]
sf_m = mot[::-1].cumsum()[::-1]
fig, ax = bio.canvas(24.0, 9.0)
a = C.axes_at(ax, (1.9, 1.5, 9.0, 6.8))
b = C.axes_at(ax, (13.6, 1.5, 8.0, 6.8))
k = 50  # pool 0.5-bit bins for display
nb = len(score) // k
sc = score[:nb * k].reshape(nb, k).mean(1)
a.semilogy(sc, bgd[:nb * k].reshape(nb, k).sum(1) / 0.5, color=C.line("neutral"), lw=1.4, label="random window")
a.semilogy(sc, mot[:nb * k].reshape(nb, k).sum(1) / 0.5, color=C.line("dna"), lw=1.4, label="motif-model site")
for pv in (1e-4, 1e-5, 1e-6):
    t = score[np.argmax(sf_b <= pv)]
    a.axvline(t, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
    a.text(t + 0.3, 2e-9, f"p = {pv:g}", rotation=90, fontsize=bio.core.FONT["tiny"], color=P.muted())
a.set_xlim(-60, 30)
a.set_ylim(1e-10, 1)
C.style_axes(a, "PWM score (bits)", "density")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
ts = np.linspace(0, 28, 200)
idx = np.searchsorted(score, ts)
b.semilogy(ts, 2 * 3.1e9 * sf_b[idx], color=C.line("negative"), lw=1.5)
b.set_ylim(1, 1e9)
C.style_axes(b, "threshold (bits)", "expected chance matches in 3.1 Gb")
b2 = b.twinx()
b2.plot(ts, sf_m[idx], color=C.line("positive"), lw=1.5)
b2.set_ylim(0, 1.05)
C.style_axes(b2, None, "sensitivity (motif-model sites)", box=False)
b2.spines["right"].set_visible(True)
b2.spines["right"].set_color(P.muted())
b.text(1, 3e7, "chance matches", color=C.line("negative"), fontsize=bio.core.FONT["tiny"])
b.text(15, 2e7, "sensitivity", color=C.line("positive"), fontsize=bio.core.FONT["tiny"])
bio.panel(ax, "A", (0.2, 8.7))
bio.panel(ax, "B", (12.0, 8.7))
