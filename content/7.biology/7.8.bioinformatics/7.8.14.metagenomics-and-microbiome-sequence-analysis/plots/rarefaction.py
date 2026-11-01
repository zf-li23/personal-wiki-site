# Rarefaction curves of two simulated communities. Community 1 has 150 taxa and community 2 has 1500, with
# log-normal relative abundances (log-scale SD 1.5 and 1.2); 20 000 reads are drawn from each (multinomial).
# A: the expected number of taxa observed in a random subsample of n reads, E[S_n] = sum_i [1 - C(N - N_i, n)
# / C(N, n)] (Hurlbert 1971), computed exactly from the counts N_i; dashed lines are the true richness, and the
# text gives the observed richness, the Chao1 estimate S_obs + f1^2 / (2 f2) and the Shannon index of each
# sample. B: Hill numbers of order q (q = 0 richness, q = 1 exp(Shannon), q = 2 inverse Simpson) of the two
# full samples: richness is dominated by rare taxa, high orders by the abundant ones.
import numpy as np
from scipy.special import gammaln
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
comms = [(150, 1.5, "dna", "community 1 (150 taxa)"), (1500, 1.2, "rna", "community 2 (1500 taxa)")]
fig, ax = bio.canvas(28.0, 10.6)
a = C.axes_at(ax, (2.2, 1.6, 12.0, 7.8))
b = C.axes_at(ax, (18.2, 1.6, 9.0, 7.8))
ns = np.unique(np.r_[np.linspace(1, 20000, 200).astype(int), 10, 30, 100, 300, 1000, 5000])
qs = np.linspace(0, 3, 61)
for S, sd, tok, name in comms:
    w = np.exp(rng.normal(0, sd, S))
    counts = rng.multinomial(20000, w / w.sum())
    c = counts[counts > 0]
    N = c.sum()
    ES = []
    for n in ns:
        k = N - c
        lc = np.where(k >= n, gammaln(k + 1) - gammaln(n + 1) - gammaln(np.maximum(k - n, 0) + 1), -np.inf)
        ES.append(np.sum(1 - np.exp(lc - (gammaln(N + 1) - gammaln(n + 1) - gammaln(N - n + 1)))))
    a.plot(ns, ES, color=C.line(tok), lw=1.6, label=name)
    a.axhline(S, color=C.line(tok), lw=0.8, ls=(0, (3, 2)))
    f1, f2 = np.sum(c == 1), np.sum(c == 2)
    chao = len(c) + f1 ** 2 / (2 * f2)
    p = c / N
    H = -(p * np.log(p)).sum()
    a.text(20500, ES[-1] - (110 if S == 150 else 0), f" observed {len(c)}\n Chao1 {chao:.0f}\n Shannon {H:.2f}", fontsize=bio.core.FONT["tiny"],
           color=P.ink(), va="center")
    hill = [len(c) if q == 0 else np.exp(H) if abs(q - 1) < 1e-9 else (p ** q).sum() ** (1 / (1 - q)) for q in qs]
    b.semilogy(qs, hill, color=C.line(tok), lw=1.6)
    for q in (0, 1, 2):
        v = hill[int(round(q * 20))]
        b.plot([q], [v], "o", color=C.line(tok), ms=4)
        b.text(q + 0.06, v * 1.12, f"{v:.0f}", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.set_xlim(0, 26000)
a.set_ylim(0, 1600)
a.set_xticks([0, 5000, 10000, 15000, 20000])
C.style_axes(a, "reads subsampled (n)", "expected taxa observed E[S_n]")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="center right",
         bbox_to_anchor=(0.78, 0.45))
b.set_xticks([0, 1, 2, 3])
C.style_axes(b, "order q", "Hill number (effective number of taxa)")
bio.panel(ax, "A", (0.3, 10.2))
bio.panel(ax, "B", (16.4, 10.2))
