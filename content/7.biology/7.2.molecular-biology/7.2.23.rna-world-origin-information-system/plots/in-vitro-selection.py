# In vitro selection (SELEX): one cycle, the enrichment arithmetic and the size of sequence space.
# A: the cycle - a synthetic DNA pool with a random region between constant primer-binding regions is
#    transcribed, the RNA pool is passed through a selection step (affinity chromatography for aptamers, or a
#    self-tagging reaction for ribozymes), survivors are reverse-transcribed and amplified by PCR (optionally
#    mutagenic), and the amplified pool enters the next round.
# B: fraction of functional molecules after r rounds, starting at 1e-10, for per-round enrichment
#    eps = 10, 100, 1000 (Example 23.2.2).
# C: fraction of sequence space covered by a pool of 1e15 molecules against the length of the random region,
#    min(1, 1e15 / 4^n) (Example 23.2.1).
import numpy as np
import wikibio as bio
from wikibio import genetics as G
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(25.0, 9.6)


def pw(v):
    """Tick label 10^k for a power of ten."""
    k = int(round(np.log10(v)))
    return (v, "1" if k == 0 else f"$10^{{{k}}}$")


# ----------------------------------------------------------------- A: the cycle
bio.panel(ax, "A", (0.1, 9.4))
bio.label(ax, (5.9, 9.4), "One round of selection and amplification", size="small", bold=True)

steps = [
    ("DNA pool", "dna", 7.2),
    ("transcription\nT7 RNA polymerase", "rna", 5.5),
    ("RNA pool", "rna", 3.8),
    ("selection:\nbinding or reaction", "highlight", 2.1),
]
for text, token, y in steps:
    bio.box(ax, (3.1, y), 4.0, 1.1, token=token, text=text, size="tiny", radius=0.12, zorder=10)
for y in (7.2, 5.5, 3.8):
    bio.arrow(ax, (3.1, y - 0.58), (3.1, y - 1.12), kind="process")
bio.box(ax, (8.6, 3.8), 3.4, 1.1, token="mrna", text="reverse\ntranscription", size="tiny", radius=0.12, zorder=10)
bio.box(ax, (8.6, 6.4), 3.4, 1.1, token="positive", text="PCR\n(± mutagenesis)", size="tiny", radius=0.12, zorder=10)
bio.arrow(ax, (5.15, 2.1), (8.6, 3.22), kind="process", bend=-0.2)
bio.arrow(ax, (8.6, 4.38), (8.6, 5.82), kind="process")
bio.arrow(ax, (8.6, 6.98), (5.2, 7.42), kind="process", bend=-0.2)
bio.label(ax, (7.0, 8.0), "next round", size="tiny", color=P.muted())
bio.label(ax, (9.9, 2.5), "survivors only;\neverything else\nis washed away", size="tiny", color=P.muted(), ha="left")

G.construct(ax, 1.4, 0.95, [
    {"kind": "promoter", "text": "T7", "width": 1.0},
    {"kind": "cds", "text": "constant", "width": 1.3, "token": "dna"},
    {"kind": "cds", "text": "N$_{25}$", "width": 1.6, "token": "highlight"},
    {"kind": "cds", "text": "constant", "width": 1.3, "token": "dna"},
], unit=0.55)
bio.label(ax, (5.9, 0.2), "fixed primer-binding sites flank the random region, so any survivor can be amplified",
          size="tiny", color=P.muted())

# ----------------------------------------------------------------- B: enrichment
bio.panel(ax, "B", (12.0, 9.4))
rounds = np.arange(0, 13)
pl = Q.Plot(ax, (14.1, 1.6, 4.0, 6.4), xlim=(0, 12), ylim=(1e-11, 3.0), ylog=True,
            xlabel="round $r$", ylabel="functional fraction of the pool",
            xticks=[0, 4, 8, 12], yticks=[pw(v) for v in (1e-10, 1e-8, 1e-6, 1e-4, 1e-2, 1)],
            ylabel_offset=1.25)
for eps, tok, at in ((10, "neutral", 0.78), (100, "rna", 0.42), (1000, "positive", 0.26)):
    odds = 1e-10 * float(eps) ** rounds
    dy = 0.45 if eps == 1000 else -0.5
    dx = -0.45 if eps == 1000 else 0.3
    pl.line(rounds, odds / (1 + odds), tok, text=f"ε = {eps}", at=at, dx=dx, dy=dy)
pl.hline(0.5, text="majority", side="left")
bio.label(ax, (16.1, 9.4), "Enrichment per round decides", size="small", bold=True)
bio.label(ax, (16.1, 0.5), "start: one functional molecule in $10^{10}$", size="tiny", color=P.muted())

# ----------------------------------------------------------------- C: sequence space
bio.panel(ax, "C", (19.4, 9.4))
n = np.arange(10, 61)
cover = np.minimum(1.0, 1e15 / 4.0 ** n)
pl = Q.Plot(ax, (21.3, 1.6, 3.4, 6.4), xlim=(10, 60), ylim=(1e-24, 3.0), ylog=True,
            xlabel="random region / nt", ylabel="fraction of sequence space sampled",
            xticks=[10, 25, 40, 60], yticks=[pw(v) for v in (1e-24, 1e-18, 1e-12, 1e-6, 1)],
            ylabel_offset=1.25)
pl.line(n, cover, "highlight", lw=1.8)
pl.vline(25, text="$4^{25} = 10^{15}$")
pl.points([40], [1e15 / 4.0 ** 40], "negative", r=0.09)
pl.text(44, 1e15 / 4.0 ** 40 * 300, "a 40-mer:\n$10^{-9}$ sampled", size="tiny")
bio.label(ax, (23.0, 9.4), "Sequence space is never exhausted", size="small", bold=True)
bio.label(ax, (23.0, 0.5), "pool of $10^{15}$ molecules", size="tiny", color=P.muted())
