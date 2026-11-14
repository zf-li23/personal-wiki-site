"""A motor performance limit on trilled song (after Podos 1997; simulated data). Each point is one trill type:
its syllable repetition rate and frequency bandwidth. Fast trills cannot also sweep wide frequency ranges, because
the beak gape and the syrinx must be moved through the whole range in every syllable. The upper-bound regression
(fitted to the maxima of rate bins) describes the limit; the distance of a trill below the line (Podos's
'vocal deviation' uses the orthogonal distance) is a measure of performance that females of swamp sparrows attend to (Ballentine et al.
2004). Points are simulated below a bound of bandwidth = 7.6 - 0.21 * rate (kHz, rate in syllables per second)."""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(4)
rate = rng.uniform(3, 32, 160)
bound = 7.6 - 0.21 * rate
bw = np.clip(bound * (1 - rng.beta(1.4, 3.5, rate.size)), 0.3, None)
bins = np.linspace(3, 32, 9)
mx, my = [], []
for a, b in zip(bins[:-1], bins[1:]):
    k = (rate >= a) & (rate < b)
    if k.any():
        i = np.argmax(np.where(k, bw, -1)); mx.append(rate[i]); my.append(bw[i])
slope, icpt = np.polyfit(mx, my, 1)
fig, ax = bio.canvas(16, 10.4)
p = quant.Plot(ax, (2.2, 1.8, 12.6, 7.8), xlim=(0, 34), ylim=(0, 8), xlabel="Trill rate / syllables per second",
               ylabel="Frequency bandwidth / kHz", xticks=[0, 10, 20, 30], yticks=[0, 2, 4, 6, 8])
p.points(rate, bw, "neutral", r=0.06)
p.points(mx, my, "dna", r=0.11)
xx = np.linspace(2, 34, 50)
p.line(xx, icpt + slope * xx, "dna", lw=1.6, text="upper-bound regression", at=0.1)
# two example trills and their deviations (vertical distance below the bound, in kHz)
for (r0, b0, name, tok, lab) in [(20, 3.0, "high performance", "positive", (24, 5.2)),
                                 (12, 1.6, "low performance", "negative", (2.5, 0.8))]:
    top = icpt + slope * r0
    p.points([r0], [b0], tok, r=0.16)
    ax.plot(*zip(p.xy(r0, b0), p.xy(r0, top)), color=P.edge(tok), lw=1.4, ls=(0, (3, 2)), zorder=8)
    bio.label(ax, p.xy(*lab), f"{name}: {top - b0:.1f} kHz below the bound", size="tiny", ha="left",
              color=P.edge(tok))
    ax.plot(*zip(p.xy(lab[0] + (0 if lab[0] > 20 else 4), lab[1] + (-0.25 if lab[0] > 20 else 0.25)), p.xy(r0, b0)),
            color=P.edge(tok), lw=0.6, zorder=7)
ax.set_ylim(0.3, 10.2)
