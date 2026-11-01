# Calibration of base quality scores (simulated). A: reported quality against empirical quality
# -10 log10((mismatches + 1)/(observations + 2)), computed from bases at sites known not to vary (for example, not
# in dbSNP). Here the base caller is overconfident above Q25 and its error rate also depends on the cycle and on
# the preceding base, so empirical quality falls below the diagonal and differs between contexts. B: after
# recalibration (as in GATK BQSR), each reported quality in each context is replaced by its empirical value.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
Q = np.arange(6, 41, 2)
ctx = [("early cycles, after A", 0.0, "dna"), ("late cycles, after A", 2.5, "rna"), ("late cycles, after G", 5.0, "negative")]
fig, ax = bio.canvas(22.0, 9.0)
a = C.axes_at(ax, (1.8, 1.4, 8.2, 6.8))
b = C.axes_at(ax, (12.8, 1.4, 8.2, 6.8))
for name, extra, tok in ctx:
    true_q = Q - 0.25 * np.clip(Q - 25, 0, None) - extra * (Q / 40)
    nobs = rng.integers(2e5, 2e6, len(Q))
    mis = rng.binomial(nobs, 10 ** (-true_q / 10))
    emp = -10 * np.log10((mis + 1) / (nobs + 2))
    a.plot(Q, emp, "o-", color=C.line(tok), ms=3.5, lw=1.2, label=name)
    # recalibrated: bases now carry their empirical quality; re-estimate on independent data
    mis2 = rng.binomial(nobs, 10 ** (-true_q / 10))
    emp2 = -10 * np.log10((mis2 + 1) / (nobs + 2))
    b.plot(emp, emp2, "o", color=C.line(tok), ms=3.5, label=name)
for x in (a, b):
    x.plot([0, 42], [0, 42], color=P.muted(), lw=0.9, ls=(0, (3, 2)))
    x.set_xlim(4, 42)
    x.set_ylim(4, 42)
C.style_axes(a, "reported quality", "empirical quality")
C.style_axes(b, "recalibrated quality", "empirical quality (new data)")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.1, 8.9))
bio.panel(ax, "B", (11.1, 8.9))
