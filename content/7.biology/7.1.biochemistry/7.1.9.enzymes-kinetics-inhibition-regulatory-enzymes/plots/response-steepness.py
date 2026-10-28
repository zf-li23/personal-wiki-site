"""How steep can a biochemical response be? The input fold change R needed to move a response from
10 % to 90 % of its range, for the mechanisms of this chapter and 7.1.7.

Hill form y = x^n / (1 + x^n) gives R = 81^(1/n): 81 for a Michaelis-Menten enzyme or a single
binding site (n = 1), 9 for n = 2, 3 for n = 4. Hemoglobin (n_H about 2.8) needs about 4.8-fold.
A covalent modification cycle with saturated enzymes (zero-order ultrasensitivity, Formula 9.6.1)
gives R = 81((J + 0.1)/(J + 0.9))^2: 3.2 for J = 0.1 and 1.18 for J = 0.01, with effective Hill
coefficients ln 81 / ln R of 3.7 and 26.
A: normalized responses on a logarithmic input axis, with the 10-90 % windows as bars.
B: R on a logarithmic scale for the different mechanisms."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
tiny = bio.core.FONT["tiny"]

fig, ax = bio.canvas(22.0, 8.6)

bio.panel(ax, "A", (0.1, 8.5))
a = charts.axes_at(ax, (1.5, 1.0, 8.6, 6.6))
x = np.logspace(-2, 2, 500)
curves = [(1, "enzyme", "$n = 1$ (Michaelis–Menten)"), (2, "protein", "$n = 2$"), (4, "negative", "$n = 4$")]
for k, (n, tok, lab) in enumerate(curves):
    a.semilogx(x, x**n / (1 + x**n), color=charts.line(tok), lw=2.0, label=lab)
    lo, hi = (1 / 9) ** (1 / n), 9 ** (1 / n)
    y = -0.06 - 0.055 * k
    a.plot([lo, hi], [y, y], color=charts.line(tok), lw=4, solid_capstyle="butt")
    a.text(hi * 1.25, y - 0.015, f"{81 ** (1 / n):.3g}-fold", fontsize=tiny, color=P.ink())
for th in (0.1, 0.9):
    a.axhline(th, color=P.muted(), lw=0.6, ls=":")
a.set_xlim(1e-2, 1e2)
a.set_ylim(-0.24, 1.02)
a.set_yticks([0, 0.1, 0.5, 0.9, 1])
a.legend(frameon=False, fontsize=tiny, labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "input / $K_{0.5}$", "response (fraction of maximum)")
charts.title(a, "Hill responses and their 10–90 % windows")

bio.panel(ax, "B", (11.4, 8.5))
b = charts.axes_at(ax, (16.3, 1.0, 5.3, 6.6))
J = lambda j: 81 * ((j + 0.1) / (j + 0.9)) ** 2
rows = [
    ("Michaelis–Menten, one site", 81.0, "enzyme"),
    ("Hill $n = 2$", 9.0, "protein"),
    ("hemoglobin, $n_\\mathrm{H} = 2.8$", 81 ** (1 / 2.8), "blood"),
    ("Hill $n = 4$ (the limit of a tetramer)", 3.0, "protein"),
    ("modification cycle, $J = 0.1$", J(0.1), "highlight"),
    ("modification cycle, $J = 0.01$", J(0.01), "negative"),
]
for i, (lab, r, tok) in enumerate(rows):
    yy = len(rows) - 1 - i
    b.barh(yy, r - 1, height=0.62, left=1, color=P.fill(tok), edgecolor=charts.line(tok), lw=0.9)
    b.text(r * 1.12 if r < 30 else r / 1.12, yy, f"{r:.3g}", va="center", ha="left" if r < 30 else "right",
           fontsize=tiny, color=P.ink() if r < 30 else P.on_fill())
b.set_xscale("log")
b.set_xlim(1, 120)
b.set_yticks(range(len(rows)))
b.set_yticklabels([r[0] for r in rows][::-1])
charts.style_axes(b, "$R$ = input fold change for 10 % → 90 %")
charts.title(b, "Steepness of switches", loc="right")
