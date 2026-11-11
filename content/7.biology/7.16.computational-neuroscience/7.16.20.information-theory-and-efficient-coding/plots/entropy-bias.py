"""Direct estimation of spike-train entropy: bias of the plug-in estimate and its correction (Strong et al. 1998).

A spike train is simulated as independent bins with spike probability p = 0.2 per bin (a Poisson train of 100 Hz in 2 ms
bins), so the true entropy per bin is h(p) = 0.722 bits. Words of L bins are read from the train; the entropy of the
word distribution is estimated from N words by the plug-in estimate, by the Miller-Madow correction
H_MM = H_plugin + (K - 1)/(2 N ln 2) with K the number of observed words, and by extrapolation in 1/N (fit of the
plug-in estimate at N, N/2, N/4, N/8 to a + b/N, taking a).
A: entropy per bin against word length L for N = 2000 words: the plug-in estimate falls below the true value h(p)
once 2^(L h(p)) words approach N; the corrections delay the failure. B: estimated entropy per bin against 1/N for L = 16 (strongly undersampled: the bias is not yet linear in 1/N).
"""
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
p = 0.2
hp = -(p * np.log2(p) + (1 - p) * np.log2(1 - p))
train = rng.random(2_000_000) < p


def words(L, n):
    idx = rng.integers(0, len(train) - L, n)
    w = np.zeros(n, dtype=np.int64)
    for j in range(L):
        w = (w << 1) | train[idx + j]
    return w


def plugin(w):
    c = np.array(list(Counter(w.tolist()).values()), float)
    q = c / c.sum()
    return -(q * np.log2(q)).sum(), len(c)


def estimates(L, n):
    h, K = plugin(words(L, n))
    mm = h + (K - 1) / (2 * n * np.log(2))
    ns = [n, n // 2, n // 4, n // 8]
    hs = []
    w = words(L, n)
    for m in ns:
        hs.append(plugin(w[:m])[0])
    b, a = np.polyfit(1 / np.array(ns), hs, 1)
    return h, mm, a


Ls = np.arange(2, 31, 2)
res = np.array([np.mean([estimates(L, 2000) for _ in range(5)], axis=0) for L in Ls])
fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.0))
ax = axs[0]
ax.axhline(hp, color=P.ink(), lw=1, ls=":", label=f"true h(p) = {hp:.3f}")
ax.plot(Ls, res[:, 0] / Ls, "o-", ms=4, color=P.edge("rna"), lw=1.6, label="plug-in")
ax.plot(Ls, res[:, 1] / Ls, "o-", ms=4, color=P.edge("dna"), lw=1.6, label="Miller-Madow")
ax.plot(Ls, res[:, 2] / Ls, "o-", ms=4, color=P.edge("positive"), lw=1.6, label="1/N extrapolation")
ax.set_xlabel("Word length L (bins)")
ax.set_ylabel("Estimated entropy per bin (bits)")
ax.set_ylim(0.3, 0.8)
ax.legend(frameon=False, fontsize=8, loc="lower left")
ax.set_title("A  N = 2000 words", loc="left", fontsize=10)

bx = axs[1]
L = 16
Ns = np.array([250, 500, 1000, 2000, 4000, 8000, 16000])
r2 = np.array([np.mean([estimates(L, n)[:2] for _ in range(5)], axis=0) for n in Ns])
bx.axhline(hp, color=P.ink(), lw=1, ls=":")
bx.plot(1 / Ns, r2[:, 0] / L, "o-", ms=4, color=P.edge("rna"), lw=1.6, label="plug-in")
bx.plot(1 / Ns, r2[:, 1] / L, "o-", ms=4, color=P.edge("dna"), lw=1.6, label="Miller-Madow")
bx.set_xlabel("1 / N")
bx.set_ylabel("Estimated entropy per bin (bits)")
bx.legend(frameon=False, fontsize=8, loc="lower left")
bx.set_title("B  Undersampling bias, L = 16", loc="left", fontsize=10)
fig.tight_layout()
