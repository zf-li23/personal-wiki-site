"""Sensitivity amplification by a substrate cycle (Newsholme and Crabtree).

Forward rate vf, reverse rate vr = r vf, net flux J = vf - vr. An effector that raises vf and lowers vr
by the same fraction a gives J(a)/J(0) = [(1 + a) - r (1 - a)] / (1 - r), i.e.
Delta J / J = a (1 + r) / (1 - r). The cost is the ATP hydrolysed by cycling: vr per unit net flux,
r / (1 - r).
A: J(a)/J(0) against a for r = 0, 0.5, 0.8, 0.9. B: amplification factor (1 + r)/(1 - r) and ATP
cost per unit of net flux r/(1 - r) against the cycling ratio r."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(22.0, 9.0)

a_ = np.linspace(-0.2, 0.2, 200)
A = charts.axes_at(ax, (1.9, 1.3, 8.0, 6.6))
for r, tok in ((0.0, "neutral"), (0.5, "enzyme"), (0.8, "drug"), (0.9, "protein")):
    J = ((1 + a_) - r * (1 - a_)) / (1 - r)
    A.plot(a_ * 100, J, color=charts.line(tok), lw=2.0, label=f"$r = v_{{\\mathrm{{r}}}}/v_{{\\mathrm{{f}}}}$ = {r:g}")
A.axhline(1, color=P.muted(), lw=0.8)
A.axvline(0, color=P.muted(), lw=0.8)
A.set_xlim(-20, 20)
A.set_ylim(-1.2, 3.2)
charts.style_axes(A, "change of both enzyme activities, a / %", "net flux J / J(0)")
A.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.4, 8.6))

r = np.linspace(0, 0.95, 300)
B = charts.axes_at(ax, (13.0, 1.3, 8.0, 6.6))
B.semilogy(r, (1 + r) / (1 - r), color=charts.line("positive"), lw=2.0, label="amplification (1 + r)/(1 − r)")
B.semilogy(r, np.maximum(r / (1 - r), 1e-3), color=charts.line("negative"), lw=2.0, ls="--",
           label="ATP cycled per net flux r/(1 − r)")
B.set_xlim(0, 0.95)
B.set_ylim(0.05, 50)
charts.style_axes(B, r"cycling ratio $r = v_{\mathrm{r}}/v_{\mathrm{f}}$", "factor")
B.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (11.5, 8.6))
