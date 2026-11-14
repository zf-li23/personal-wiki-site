"""How fast can a silent mutation spread? Selection on flatwing crickets on Kauai.

Flatwing (fw) is a single-locus, X-linked mutation that erases the sound-producing structures of
the male forewing (Tinghitella 2008). Males that cannot sing escape the parasitoid fly Ormia
ochracea but lose access to females attracted by song. The model treats the male phenotype
frequency with a selection coefficient s (net survival-and-mating advantage of silent males
relative to callers) in discrete generations, starting from 1 %; the observed spread on Kauai
(from rare to over 90 % of males within about 20 generations, Zuk et al. 2006) requires s of
the order of 0.3 or more.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
g = np.arange(0, 41)
fig, ax = plt.subplots(figsize=(8.5, 3.6))
for s_, col in ((0.1, P.edge("neutral")), (0.2, P.edge("dna")), (0.35, P.edge("rna")), (0.5, P.edge("negative"))):
    q = [0.01]
    for _ in g[1:]:
        x = q[-1]
        q.append(x * (1 + s_) / (1 + s_ * x))
    ax.plot(g, q, color=col, lw=2, label=f"s = {s_}")
ax.axhline(0.9, color=P.muted(), lw=0.7, ls=":")
ax.axvspan(0, 20, color=P.light("highlight"), alpha=0.5, lw=0)
ax.text(1, 0.93, "observed: >90 % flatwing within about 20 generations", fontsize=7.5, color=P.ink())
ax.set_xlabel("Generations")
ax.set_ylabel("Frequency of flatwing males")
ax.set_ylim(0, 1.05)
ax.legend(frameon=False, fontsize=8, loc="center right")
for sp in ("top", "right"):
    ax.spines[sp].set_visible(False)
fig.tight_layout()
