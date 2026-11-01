# Seeds for DNA search. A: probability that a seed hits somewhere in a homologous region of 64 bases whose
# positions are identical independently with probability p (Monte Carlo, 40000 regions per point): contiguous
# seeds of weight 8, 11 and 28 (BLASTN word sizes) and the spaced seed 111010010100110111 of PatternHunter
# (weight 11, length 18). At p = 0.7 the spaced seed hits with probability 0.47, the contiguous seed of the
# same weight with 0.30. B: expected number of chance seed hits of weight W for a 1-kb query against both
# strands of a 3.1-Gb genome, mn 4^-W: a seed of weight 11 gives 1.5 million chance hits to extend, one of
# weight 28 almost none.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
L, R = 64, 40000
seeds = [("1" * 8, "contiguous, W = 8", "neutral"), ("1" * 11, "contiguous, W = 11", "dna"),
         ("111010010100110111", "spaced, weight 11", "negative"), ("1" * 28, "contiguous, W = 28", "protein")]
ps = np.linspace(0.5, 1.0, 21)
fig, ax = bio.canvas(24.0, 9.6)
a = C.axes_at(ax, (2.0, 1.5, 9.2, 7.0))
for seed, lab, tok in seeds:
    care = np.array([c == "1" for c in seed])
    w = len(seed)
    out = []
    for p in ps:
        X = rng.random((R, L)) < p
        hit = np.zeros(R, bool)
        for s in range(L - w + 1):
            hit |= X[:, s:s + w][:, care].all(axis=1)
        out.append(hit.mean())
    a.plot(ps, out, color=C.line(tok), lw=1.6, label=lab)
a.axvline(0.7, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
a.set_xlim(0.5, 1.0)
a.set_ylim(0, 1.02)
C.style_axes(a, "identity p of the homologous region", "P(at least one seed hit in 64 bases)")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
b = C.axes_at(ax, (14.6, 1.5, 9.0, 7.0))
Ws = np.arange(8, 29)
mn = 1e3 * 2 * 3.1e9
b.semilogy(Ws, mn * 4.0 ** (-Ws), "o-", color=C.line("dna"), ms=3, lw=1.0)
b.axhline(1, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
for W in (11, 28):
    b.annotate(f"W = {W}: {mn * 4.0 ** -W:.2g}", xy=(W, mn * 4.0 ** -W), xytext=(W + (1 if W == 11 else -9), mn * 4.0 ** -W * 20),
               fontsize=bio.core.FONT["tiny"], color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
b.set_xticks(range(8, 29, 4))
C.style_axes(b, "seed weight W", "expected chance hits")
bio.panel(ax, "A", (0.2, 9.3))
bio.panel(ax, "B", (12.9, 9.3))
