"""pH dependence of enzyme activity in the two-pKa model: only the form EH, with group 1
deprotonated and group 2 protonated, is active, so v / v_lim = 1 / (1 + [H+]/K1 + K2/[H+]).

A: pepsin-like (pK1 = 0.8, pK2 = 2.4; optimum near 1.6, the pH of gastric juice) and chymotrypsin-like
(pK1 = 7.0 for His57, pK2 = 9.0 for the alpha-amino group of Ile16; optimum 8.0) profiles. The pKa
values are illustrative, chosen to reproduce the observed optima. B: the same model on a log scale
for well-separated pKa values (5 and 9): the limbs have slopes +1 and -1, and the asymptotes meet
the plateau at the two pKa values (Dixon's construction)."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P


def frac(pH, pk1, pk2):
    h = 10.0 ** (-pH)
    return 1.0 / (1.0 + h / 10.0 ** (-pk1) + 10.0 ** (-pk2) / h)


fig, ax = bio.canvas(20.0, 8.0)
pH = np.linspace(-1, 13, 800)

bio.panel(ax, "A", (0.1, 7.9))
a = charts.axes_at(ax, (1.3, 1.0, 8.0, 6.0))
for name, pk1, pk2, tok in (("pepsin-like", 0.8, 2.4, "drug"), ("chymotrypsin-like", 7.0, 9.0, "enzyme")):
    f = frac(pH, pk1, pk2)
    a.plot(pH, f, color=charts.line(tok), lw=2.0, label=f"{name} (p$K_1$ {pk1}, p$K_2$ {pk2})")
    opt = (pk1 + pk2) / 2
    a.plot([opt, opt], [0, frac(opt, pk1, pk2)], color=charts.line(tok), lw=0.8, ls=":")
    a.text(opt, frac(opt, pk1, pk2) + 0.03, f"pH {opt:.1f}", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.set_xlim(-0.5, 12.5)
a.set_ylim(0, 1.08)
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(a, "pH", r"$v/v_{\mathrm{lim}}$")
charts.title(a, "Bell-shaped pH–activity profiles")

bio.panel(ax, "B", (10.6, 7.9))
b = charts.axes_at(ax, (11.8, 1.0, 7.8, 6.0))
pk1, pk2 = 5.0, 9.0
b.plot(pH, np.log10(frac(pH, pk1, pk2)), color=charts.line("protein"), lw=2.0)
b.plot(pH, pH - pk1, color=P.muted(), lw=0.9, ls="--")
b.plot(pH, pk2 - pH, color=P.muted(), lw=0.9, ls="--")
b.axhline(0, color=P.muted(), lw=0.9, ls="--")
for pk in (pk1, pk2):
    b.plot([pk], [0], "o", ms=4, color=P.ink())
    b.text(pk, 0.12, f"p$K$ = {pk:.0f}", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
b.text(2.2, -1.2, "slope +1", fontsize=bio.core.FONT["tiny"], color=P.ink(), rotation=0)
b.text(10.6, -0.95, "slope −1", fontsize=bio.core.FONT["tiny"], color=P.ink())
b.set_xlim(1, 13)
b.set_ylim(-3, 0.5)
charts.style_axes(b, "pH", r"$\log_{10}(v/v_{\mathrm{lim}})$")
charts.title(b, "Reading p$K$ values from the limbs")
