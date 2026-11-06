# The Nernst equation as a test for active transport: pea root tissue in a dilute nutrient solution
# (data of Higinbotham, Etherton and Foster 1967, as tabulated in Taiz et al. 2015, Table 6.1). Measured membrane
# potential -110 mV. For each ion the internal concentration expected at electrochemical equilibrium,
# c_in = c_out 10^(-z V_m / 59 mV), is compared with the measured one (log scale). Only K+ is near equilibrium;
# all anions are far above (active uptake); Na+, Mg2+ and Ca2+ are far below (passive entry, active extrusion).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
Vm = -110.0
k = 59.16
ions = [("K$^+$", 1, 1.0, 75), ("Na$^+$", 1, 1.0, 8), ("Mg$^{2+}$", 2, 0.25, 3), ("Ca$^{2+}$", 2, 1.0, 2),
        ("NO$_3^-$", -1, 2.0, 28), ("Cl$^-$", -1, 1.0, 7), ("H$_2$PO$_4^-$", -1, 1.0, 21), ("SO$_4^{2-}$", -2, 0.25, 19)]
x = np.arange(len(ions))
pred = np.array([co * 10 ** (-z * Vm / k) for _, z, co, ci in ions])
obs = np.array([ci for *_, ci in ions])
ext = np.array([co for _, z, co, ci in ions])

fig, ax = plt.subplots(figsize=(9.5, 4.6))
w = 0.36
ax.bar(x - w / 2, pred, w, color=P.fill("neutral"), edgecolor=P.edge("neutral"), label="predicted (equilibrium)")
ax.bar(x + w / 2, obs, w, color=P.fill("k"), edgecolor=P.edge("k"), label="measured")
ax.scatter(x, ext, marker="_", s=260, color=P.ink(), zorder=5, label="external concentration")
for i, (_, z, co, ci) in enumerate(ions):
    r = obs[i] / pred[i]
    if 0.5 < r < 2:
        lab, tok = "≈ equilibrium", "positive"
    elif r > 1:
        lab, tok = "active uptake", "dna"
    else:
        lab, tok = "active efflux", "negative"
    ax.text(i, 2.6e4, lab, ha="center", fontsize=6.8, color=charts.line(tok), rotation=0)
ax.set_yscale("log")
ax.set_ylim(1e-5, 1e5)
ax.set_xticks(x)
ax.set_xticklabels([n for n, *_ in ions])
ax.legend(fontsize=7, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.09), ncol=3)
charts.style_axes(ax, None, "internal concentration / (mmol L$^{-1}$)")
ax.set_title("pea root, $V_{\\mathrm{m}}$ = −110 mV", fontsize=8, color=P.ink(), loc="right")
