"""The Wright-Fisher chain for Buri's design: 2N = 32 gene copies starting from 16 copies of an allele.
A: exact distribution of the number of copies after 1, 5, 10 and 19 generations from powers of the binomial
transition matrix; the absorbed states 0 and 32 are drawn as wider bars at the ends. B: variance of the allele
frequency among replicate populations, p0 q0 [1 - (1 - 1/2N)^t], for N = 16 and N = 11.5 (solid), and the
fraction of populations absorbed (fixed or lost), from the exact chain (dashed; for N = 11.5 the chain with
23 gene copies is used)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.8), gridspec_kw={"width_ratios": [1.3, 1]})
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.28)


def chain(M):
    i = np.arange(M + 1)
    return binom.pmf(i[None, :], M, i[:, None] / M)


M = 32
T = chain(M)
v = np.zeros(M + 1)
v[16] = 1
dist = {}
for t in range(1, 20):
    v = v @ T
    if t in (1, 5, 10, 19):
        dist[t] = v.copy()
cols = {1: "dna", 5: "enzyme", 10: "protein", 19: "rna"}
x = np.arange(M + 1)
for k, (t, d) in enumerate(dist.items()):
    off = (k - 1.5) * 0.2
    a.bar(x[1:-1] + off, d[1:-1], width=0.2, color=P.fill(cols[t]), edgecolor=P.edge(cols[t]), lw=0.4,
          label=f"generation {t}")
    a.bar([-1.2 + off * 2, M + 1.2 + off * 2], [d[0], d[-1]], width=0.38, color=P.fill(cols[t]),
          edgecolor=P.edge(cols[t]), lw=0.6)
a.axvline(-0.5, color=P.muted(), lw=0.6, ls=":")
a.axvline(M + 0.5, color=P.muted(), lw=0.6, ls=":")
a.set_ylim(0, 0.15)
a.text(-1.2, 0.124, "lost", ha="center", fontsize=FT["tiny"], color=P.muted())
a.text(M + 1.2, 0.124, "fixed", ha="center", fontsize=FT["tiny"], color=P.muted())
a.set_xlim(-2.5, M + 2.5)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left", bbox_to_anchor=(0.06, 1.0))
charts.style_axes(a, "copies of the allele (of 32)", "fraction of populations")
charts.title(a, "A  Exact distribution, $2N = 32$")

t = np.arange(0, 41)
for N, tok, M in ((16, "dna", 32), (11.5, "rna", 23)):
    b.plot(t, 0.25 * (1 - (1 - 1 / (2 * N)) ** t) / 0.25, color=charts.line(tok), lw=1.8,
           label=f"$F_{{\\mathrm{{ST}}}}$ among populations, $N = {N}$")
    Tm = chain(M)
    v = np.zeros(M + 1)
    if M % 2 == 0:
        v[M // 2] = 1
    else:
        v[M // 2] = v[M // 2 + 1] = 0.5
    ab = [0.0]
    for _ in t[1:]:
        v = v @ Tm
        ab.append(v[0] + v[-1])
    b.plot(t, ab, color=charts.line(tok), lw=1.3, ls="--", label=f"fraction absorbed, $N = {N}$")
b.axvline(19, color=P.muted(), lw=0.7, ls=":")
b.set_xlim(0, 40)
b.set_ylim(0, 1)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "generation", "variance / $p_0q_0$, or fraction")
charts.title(b, "B  Divergence among replicates")
