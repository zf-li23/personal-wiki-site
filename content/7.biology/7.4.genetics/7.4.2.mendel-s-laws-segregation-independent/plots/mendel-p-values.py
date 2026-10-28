"""Mendel's experiments against the chi-square test (counts from Mendel 1866).

For each experiment, the p-value of the chi-square test of Mendel's own hypothesis is plotted against the
expected p-value of the same rank among uniform order statistics, (i - 0.5)/m. Experiments: the seven F2
monohybrid ratios (3:1), the two seed-trait F3 tests (1:2), the six plant-trait F3 tests (1:2, 100 plants
each, including the repeated pod-color test), the dihybrid F2 (9:3:3:1) and the dihybrid testcross (1:1:1:1).
"""
import numpy as np
from scipy import stats

import wikibio as bio
from wikibio import charts

P = bio.P


def pval(o, ratio):
    o = np.asarray(o, float)
    e = np.asarray(ratio, float) / sum(ratio) * o.sum()
    return stats.chi2.sf(((o - e) ** 2 / e).sum(), len(o) - 1)


groups = {
    "F₂ monohybrid (3:1)": [pval(o, (3, 1)) for o in [(5474, 1850), (6022, 2001), (705, 224), (882, 299),
                                                           (428, 152), (651, 207), (787, 277)]],
    "F₃ progeny tests (1:2)": [pval(o, (1, 2)) for o in [(193, 372), (166, 353), (36, 64), (29, 71), (40, 60),
                                                              (33, 67), (28, 72), (35, 65)]],
    "dihybrid F₂ and testcross": [pval((315, 108, 101, 32), (9, 3, 3, 1)), pval((31, 26, 27, 26), (1, 1, 1, 1))],
}
allp = sorted(p for v in groups.values() for p in v)
m = len(allp)
expected = {p: (i + 0.5) / m for i, p in enumerate(allp)}

fig, ax = bio.canvas(12.0, 10.0)
a = charts.axes_at(ax, (2.0, 1.6, 9.2, 7.8))
a.plot([0, 1], [0, 1], color=P.muted(), lw=1.0, ls=(0, (3, 2)))
for (name, ps), tok in zip(groups.items(), ("dna", "highlight", "negative")):
    a.scatter([expected[p] for p in ps], ps, s=34, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=5,
              label=name)
a.set_xlim(0, 1)
a.set_ylim(0, 1)
a.text(0.62, 0.3, "fit worse than chance", fontsize=bio.core.FONT["tiny"], color=P.muted())
a.text(0.22, 0.66, "fit better than chance", fontsize=bio.core.FONT["tiny"], color=P.muted())
charts.style_axes(a, "expected p-value (uniform order statistic)", "observed p-value", box=True)
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
