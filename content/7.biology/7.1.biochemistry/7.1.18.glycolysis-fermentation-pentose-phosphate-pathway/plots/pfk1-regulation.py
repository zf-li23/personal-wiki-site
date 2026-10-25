"""PFK-1 regulation in a four-site concerted (MWC) model, K system (illustrative parameters).
v/vmax = a(1+a)^3 / ((1+a)^4 + L (1+c a)^4), a = [F6P]/K_R, with
L = L0 (1 + [ATP]/K_ATP)^4 / ((1 + [AMP]/K_AMP)^4 (1 + [F26BP]/K_F)^4); ATP binds the T state at a
regulatory site, AMP and fructose 2,6-bisphosphate bind the R state.
L0 = 10, c = 0.01, K_R = 0.05 mM, K_ATP = 0.25 mM, K_AMP = 0.05 mM, K_F = 1e-3 mM."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
KR, c, L0 = 0.05, 0.01, 10.0


def v(F, atp, amp=0.0, f26=0.0):
    a = F / KR
    L = L0 * (1 + atp / 0.25) ** 4 / ((1 + amp / 0.05) ** 4 * (1 + f26 / 1e-3) ** 4)
    return a * (1 + a) ** 3 / ((1 + a) ** 4 + L * (1 + c * a) ** 4)


fig, ax = bio.canvas(14.0, 9.0)
a = charts.axes_at(ax, (1.8, 1.3, 11.4, 6.8))
F = np.linspace(0, 4, 600)
curves = [(0.5, 0, 0, "low ATP (0.5 mM)", "enzyme", "-"), (5.0, 0, 0, "high ATP (5 mM)", "negative", "-"),
          (5.0, 0.1, 0, "high ATP + AMP (0.1 mM)", "positive", "--"),
          (5.0, 0, 1e-3, "high ATP + F2,6BP (1 µM)", "drug", "--")]
for atp, amp, f26, lab, tok, ls in curves:
    a.plot(F, v(F, atp, amp, f26), color=charts.line(tok), lw=2.0, ls=ls, label=lab)
a.set_xlim(0, 4)
a.set_ylim(0, 1.02)
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(a, "[fructose 6-phosphate] / mM", r"$v_0/v_{\max}$")
charts.title(a, "ATP inhibits, AMP and fructose 2,6-bisphosphate activate")
