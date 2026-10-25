"""Near-equilibrium and far-from-equilibrium steps.

A: flux-force relation J-/J+ = exp(dG/RT) and net fraction J/J+ = 1 - exp(dG/RT) at 37 C.
B: actual Gibbs energies of glycolytic steps in heart muscle (Lehninger 8e, Table 13-10, data of
Newsholme and Start 1973)."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
RT = 8.314462618e-3 * 310.15
fig, ax = bio.canvas(22.0, 8.6)

bio.panel(ax, "A", (0.1, 8.4))
a = charts.axes_at(ax, (1.6, 1.2, 8.6, 6.4))
g = np.linspace(0, 30, 400)
a.axvspan(0, 6, color=P.fill("highlight"), alpha=0.35, lw=0)
a.plot(g, np.exp(-g / RT), color=charts.line("drug"), lw=2.0, label=r"backward / forward, $J_-/J_+$")
a.plot(g, 1 - np.exp(-g / RT), color=charts.line("enzyme"), lw=2.0, label=r"net / forward, $J/J_+$")
a.text(3, 0.9, "near\nequilibrium", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.set_xlim(0, 30)
a.set_ylim(0, 1.02)
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(a, r"$-\Delta_{\mathrm{r}}G$ / (kJ mol$^{-1}$)", "fraction")
charts.title(a, "One-way fluxes at 37 °C")

bio.panel(ax, "B", (11.4, 8.4))
b = charts.axes_at(ax, (15.6, 1.2, 6.0, 6.4))
steps = [("hexokinase", -27), ("phosphohexose isomerase", -1.4), ("PFK-1", -23), ("aldolase", -6.0),
         ("triose phosphate isomerase", 3.8), ("GAPDH + PGK", 3.5), ("phosphoglycerate mutase", 0.6),
         ("enolase", -0.5), ("pyruvate kinase", -17)]
y = np.arange(len(steps))[::-1]
vals = [v for _, v in steps]
far = [v < -10 for v in vals]
b.axvspan(-6, 6, color=P.fill("highlight"), alpha=0.35, lw=0)
b.barh(y, vals, color=[P.fill("negative" if f else "neutral") for f in far],
       edgecolor=[P.edge("negative" if f else "neutral") for f in far], lw=0.8)
b.axvline(0, color=P.muted(), lw=0.8)
b.set_yticks(y)
b.set_yticklabels([n for n, _ in steps])
b.set_xlim(-30, 8)
charts.style_axes(b, r"$\Delta_{\mathrm{r}}G$ in heart / (kJ mol$^{-1}$)")
charts.title(b, "Glycolysis in heart muscle")
