"""Transition probabilities under JC69 and K80 and the observed transition/transversion ratio.
A: under K80 with kappa = 5, the probabilities p0 (no difference), p1 (a transitional difference) and
2 p2 (a transversional difference) against the distance d; dashed: the JC69 probabilities of no
difference and of any difference. B: the expected observed ratio E(S)/E(V) = p1/(2 p2) against d for
several values of kappa; it starts at kappa/2 for very similar sequences and falls to 1/2 at saturation."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def k80(d, k):
    e1 = np.exp(-4 * d / (k + 2))
    e2 = np.exp(-2 * d * (k + 1) / (k + 2))
    return 0.25 + 0.25 * e1 + 0.5 * e2, 0.25 + 0.25 * e1 - 0.5 * e2, 0.25 - 0.25 * e1


d = np.linspace(1e-4, 3, 400)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.9))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.9, wspace=0.28)
p0, p1, p2 = k80(d, 5.0)
a.plot(d, p0, color=charts.line("dna"), lw=1.6, label="$p_0$: same nucleotide")
a.plot(d, p1, color=charts.line("rna"), lw=1.6, label="$p_1$: transitional difference")
a.plot(d, 2 * p2, color=charts.line("enzyme"), lw=1.6, label="$2p_2$: transversional difference")
e = np.exp(-4 * d / 3)
a.plot(d, 0.25 + 0.75 * e, color=P.muted(), lw=1.0, ls="--", label="JC69: same / different")
a.plot(d, 0.75 - 0.75 * e, color=P.muted(), lw=1.0, ls="--")
for y in (0.25, 0.5):
    a.axhline(y, color=P.muted(), lw=0.5, ls=":")
a.set_xlim(0, 3)
a.set_ylim(0, 1.02)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(a, "distance $d$ (substitutions per site)", "probability")
charts.title(a, "A  K80 transition probabilities ($\\kappa = 5$)")

for k, tok in ((1, "neutral"), (2, "dna"), (5, "rna"), (10, "enzyme")):
    p0, p1, p2 = k80(d, float(k))
    b.plot(d, p1 / (2 * p2), color=charts.line(tok), lw=1.6, label=f"$\\kappa = {k}$")
    b.plot([0], [k / 2], "o", ms=3.5, color=charts.line(tok), clip_on=False)
b.axhline(0.5, color=P.muted(), lw=0.6, ls=":")
b.set_xlim(0, 3)
b.set_ylim(0, 5.2)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "distance $d$ (substitutions per site)", "$\\mathbb{E}(S)/\\mathbb{E}(V)$")
charts.title(b, "B  Observed transition/transversion ratio")
