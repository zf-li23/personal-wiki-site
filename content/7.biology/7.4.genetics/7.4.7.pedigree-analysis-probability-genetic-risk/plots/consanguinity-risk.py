"""Consanguinity and recessive disease. A: probability that a child is homozygous for a recessive allele of
frequency q, q^2 (1 - F) + q F, relative to the probability q^2 for unrelated parents, for the children of
first cousins (F = 1/16), second cousins (F = 1/64) and full siblings or parent-offspring (F = 1/4). B: fraction
of all affected children who come from first-cousin marriages, when a fraction c of marriages are between
first cousins."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
q = np.logspace(-4, -0.5, 300)
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.9, wspace=0.28)
a = axs[0]
for F, lab, tok in ((1 / 4, "F = 1/4", "negative"), (1 / 16, "F = 1/16 (first cousins)", "receptor"), (1 / 64, "F = 1/64 (second cousins)", "dna")):
    a.loglog(q, (q**2 * (1 - F) + q * F) / q**2, color=charts.line(tok), lw=2, label=lab)
a.axhline(1, color=P.muted(), lw=0.8, ls=":")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(a, "allele frequency q", "relative risk")
charts.title(a, "A  Relative risk of a homozygous child")
b = axs[1]
F = 1 / 16
for c, tok in ((0.01, "dna"), (0.05, "enzyme"), (0.3, "negative")):
    pf = q**2 * (1 - F) + q * F
    frac = c * pf / (c * pf + (1 - c) * q**2)
    b.semilogx(q, frac, color=charts.line(tok), lw=2, label=f"c = {c:g}")
b.set_ylim(0, 1)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "allele frequency q", "affected from first-cousin marriages")
charts.title(b, "B  Rare recessive diseases concentrate in consanguineous families")
