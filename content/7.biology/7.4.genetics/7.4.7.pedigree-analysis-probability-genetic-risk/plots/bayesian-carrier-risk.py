"""Bayesian revision of carrier risk. A: a woman whose brother has an X-linked recessive disease (prior
probability of being a carrier 1/2) has k unaffected sons; posterior probability that she is a carrier,
1 / (1 + 2^k), and risk that her next son is affected (half of it). B: an unaffected sibling of a patient with
an autosomal recessive disease (prior 2/3) tests negative on a carrier panel that detects a fraction d of
mutant alleles; posterior carrier probability 2(1 - d) / (2(1 - d) + 1)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.9, wspace=0.28)
a = axs[0]
k = np.arange(0, 7)
post = 1 / (1 + 2.0**k)
a.plot(k, post, "o-", color=charts.line("receptor"), lw=1.8, ms=5, label="P(carrier | k unaffected sons)")
a.plot(k, post / 2, "s--", color=charts.line("dna"), lw=1.4, ms=4, label="risk that the next son is affected")
for kk, pp in zip(k[:4], post[:4]):
    a.annotate(f"{pp:.3f}", (kk, pp), textcoords="offset points", xytext=(6, 4), fontsize=FT["tiny"], color=P.muted())
a.set_ylim(0, 0.55)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(a, "number of unaffected sons k", "probability")
charts.title(a, "A  X-linked recessive: conditioning on sons")
b = axs[1]
d = np.linspace(0, 1, 200)
b.plot(d, 2 * (1 - d) / (2 * (1 - d) + 1), color=charts.line("enzyme"), lw=2)
for dd in (0.9, 0.97):
    pp = 2 * (1 - dd) / (2 * (1 - dd) + 1)
    b.plot([dd], [pp], "o", color=charts.line("enzyme"), ms=5)
    b.annotate(f"d = {dd:g}: {pp:.3f}", (dd, pp), textcoords="offset points", xytext=(-80, 14), fontsize=FT["tiny"],
               color=P.muted())
b.axhline(2 / 3, color=P.muted(), lw=0.8, ls=":")
b.text(0.02, 0.68, "prior 2/3", fontsize=FT["tiny"], color=P.muted())
b.set_ylim(0, 0.75)
charts.style_axes(b, "detection rate d of the carrier test", "P(carrier | negative test)")
charts.title(b, "B  Autosomal recessive: a negative carrier test")
