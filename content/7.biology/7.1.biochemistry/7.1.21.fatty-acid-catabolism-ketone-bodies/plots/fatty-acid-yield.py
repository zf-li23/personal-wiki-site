"""ATP from the complete oxidation of saturated even-chain fatty acids, compared with glucose.

ATP(n) = (n/2 - 1)(1.5 + 2.5) + (n/2) * 10 - 2 (beta-oxidation turns give FADH2 and NADH; each acetyl-CoA gives
10 ATP in the citric acid cycle and oxidative phosphorylation; activation costs 2 ATP equivalents).
Molar mass of CnH2nO2 = 14.027 n + 31.999 g/mol. Glucose: 32 ATP, 180.16 g/mol, 6 carbons.
A: ATP per molecule. B: ATP per carbon atom. C: ATP per gram of fuel, and per gram of stored fuel when
glycogen is stored with about 2 g of water per g (triacylglycerol is stored anhydrous)."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
n = np.arange(4, 26, 2)
atp = (n / 2 - 1) * 4 + (n / 2) * 10 - 2
mass = 14.027 * n + 31.999
G_ATP, G_M = 32, 180.16

fig, ax = bio.canvas(26.0, 9.0)
panels = [("A", atp, G_ATP, "ATP per molecule"), ("B", atp / n, G_ATP / 6, "ATP per carbon atom"),
          ("C", atp / mass, G_ATP / G_M, "ATP per gram")]
for k, (letter, y, gy, lab) in enumerate(panels):
    x0 = 1.9 + k * 8.4
    a = charts.axes_at(ax, (x0, 1.3, 6.2, 6.6))
    a.plot(n, y, "o-", color=charts.line("lipid"), lw=2.0, ms=4, label="saturated fatty acid")
    a.axhline(gy, color=charts.line("carbohydrate"), lw=1.6, ls="--", label="glucose")
    if letter == "C":
        a.axhline(G_ATP / G_M / 3, color=charts.line("carbohydrate"), lw=1.2, ls=":", label="glycogen, hydrated")
        a.set_ylim(0, 0.5)
    a.axvline(16, color=P.muted(), lw=0.7)
    a.set_xticks([4, 8, 12, 16, 20, 24])
    charts.style_axes(a, "carbon atoms, n", lab)
    if letter == "A":
        a.text(16.4, 40, "palmitate: 106", fontsize=bio.core.FONT["tiny"], color=P.ink())
    a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc={"A": "upper left", "B": "center right", "C": "center right"}[letter])
    bio.panel(ax, letter, (x0 - 1.5, 8.6))
