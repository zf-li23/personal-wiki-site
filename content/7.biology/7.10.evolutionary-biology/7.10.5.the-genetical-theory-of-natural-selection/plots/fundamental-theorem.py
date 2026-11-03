"""Mean fitness under selection and mutation. A: change of mean fitness per generation while a favored allele
A2 spreads from frequency 0.01 (additive) or 0.1 (recessive), computed exactly from the one-locus recursion, for additive fitnesses
(1, 1.05, 1.1; solid) and a recessive advantage (1, 1, 1.1; dashed), with the fundamental-theorem prediction
V_A / w_bar, V_A = 2 p q alpha^2, shown as dots every 10 generations. B: genome-wide mutation load
L = 1 - exp(-U) against the rate U of new deleterious mutations per diploid genome per generation, assuming
independent multiplicative effects; the dotted line marks U = 2."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.7), gridspec_kw={"width_ratios": [1.3, 1]})
fig.subplots_adjust(left=0.09, right=0.98, bottom=0.16, top=0.9, wspace=0.3)
for w, tok, ls, lab, T, p in (((1, 1.05, 1.1), "dna", "-", "additive", 400, 0.01), ((1, 1, 1.1), "rna", "--", "recessive", 400, 0.1)):
    dW, pred = [], []
    for t in range(T):
        q = 1 - p
        wb = q * q * w[0] + 2 * p * q * w[1] + p * p * w[2]
        alpha = (p * w[2] + q * w[1]) - (p * w[1] + q * w[0])
        pred.append(2 * p * q * alpha ** 2 / wb)
        p2 = (p * p * w[2] + p * q * w[1]) / wb
        q2 = 1 - p2
        wb2 = q2 * q2 * w[0] + 2 * p2 * q2 * w[1] + p2 * p2 * w[2]
        dW.append(wb2 - wb)
        p = p2
    t = np.arange(T)
    a.plot(t, np.array(dW) * 1e3, color=charts.line(tok), lw=1.6, ls=ls, label=f"$\\Delta\\bar w$, {lab}")
    a.scatter(t[::10], np.array(pred)[::10] * 1e3, s=9, color=charts.line(tok), zorder=4)
a.scatter([], [], s=9, color=P.muted(), label="$V_A/\\bar w$")
a.set_xlim(0, 400)
a.set_ylim(0, None)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(a, "generation", "$\\Delta\\bar w$ per generation ($\\times 10^{-3}$)")
charts.title(a, "A  Fisher's fundamental theorem")
U = np.linspace(0, 5, 200)
b.plot(U, 1 - np.exp(-U), color=charts.line("negative"), lw=1.8)
b.axvline(2, color=P.muted(), lw=0.8, ls=":")
b.scatter([2], [1 - np.exp(-2)], s=24, color=P.ink(), zorder=5)
b.annotate("$U = 2$: $L = 0.86$", (2, 1 - np.exp(-2)), xytext=(2.4, 0.62), fontsize=FT["tiny"], color=P.ink())
b.set_xlim(0, 5)
b.set_ylim(0, 1.02)
charts.style_axes(b, "deleterious mutations per genome $U$", "mutation load $L$")
charts.title(b, "B  $L = 1 - \\mathrm{e}^{-U}$")
