"""Trinucleotide repeat expansion and anticipation in Huntington disease.
(A) Repeat classes of the HTT CAG tract: normal (up to 26), intermediate (27-35, unstable in transmission but not
pathogenic), reduced penetrance (36-39) and full penetrance (40 or more). The curve is the mean age at onset in a
parametric survival model fitted to large patient series (Langbehn and colleagues 2004),
mean onset = 21.54 + exp(9.556 - 0.146 CAG) years, drawn over its range of validity, about 41-56 repeats. (B) Anticipation in a simulated paternal lineage: each transmission through a father adds a random
number of repeats (normal with mean +4, sd 3, illustrative); onset ages fall with each generation."""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)


def onset(c):
    return 21.54 + np.exp(9.556 - 0.146 * c)


fig, ax = bio.canvas(16.0, 7.6)
bio.panel(ax, "A", (0.1, 7.5))
a = charts.axes_at(ax, (1.9, 1.3, 5.6, 5.6))
for lo, hi, tok, name in ((10, 26.5, "positive", "normal"), (26.5, 35.5, "neutral", "intermediate"),
                          (35.5, 39.5, "highlight", "reduced penetrance"), (39.5, 70, "negative", "full penetrance")):
    a.axvspan(lo, hi, color=P.fill(tok), alpha=0.3, lw=0)
    narrow = hi - lo < 12
    a.text((lo + min(hi, 70)) / 2, 92, name, fontsize=FT["tiny"], color=P.ink(), ha="center", va="top",
           rotation=90 if narrow else 0)
c = np.linspace(41, 56, 200)
a.plot(c, onset(c), color=charts.line("negative"), lw=1.8)
a.set_xlim(10, 70)
a.set_ylim(0, 95)
charts.style_axes(a, r"CAG repeats in $\it{HTT}$", "mean age at onset / years")

bio.panel(ax, "B", (8.3, 7.5))
b = charts.axes_at(ax, (10.1, 1.3, 5.6, 5.6))
for rep in range(8):
    cag = [42]
    for _ in range(3):
        cag.append(cag[-1] + max(0, round(rng.normal(4, 3))))
    cag = np.array(cag)
    b.plot(np.arange(1, 5), onset(cag), "o-", color=charts.line("negative"), lw=1.0, ms=3, alpha=0.8)
b.set_xticks([1, 2, 3, 4])
b.set_xticklabels(["I", "II", "III", "IV"])
b.set_xlim(0.7, 4.3)
b.set_ylim(0, 70)
charts.style_axes(b, "generation (paternal transmissions)", "predicted mean onset / years")
