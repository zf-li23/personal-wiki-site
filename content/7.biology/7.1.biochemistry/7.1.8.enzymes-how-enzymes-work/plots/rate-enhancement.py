"""Rate enhancements of enzymes (k_cat / k_uncat, values compiled in Lehninger 8e, Table 6-5) on a
logarithmic scale, with the equivalent lowering of the activation Gibbs energy at 25 C on the top
axis: Delta Delta^dagger G = RT ln(k_cat / k_uncat), i.e. 5.71 kJ/mol per factor of ten."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
R, T = 8.314e-3, 298.15
PER_DECADE = R * T * np.log(10)

data = [
    ("Cyclophilin", 5),
    ("Carbonic anhydrase", 7),
    ("Triose phosphate isomerase", 9),
    ("Carboxypeptidase A", 11),
    ("Phosphoglucomutase", 12),
    ("Succinyl-CoA transferase", 13),
    ("Urease", 14),
    ("OMP decarboxylase", 17),
]

fig, ax = bio.canvas(16.0, 8.0)
a = charts.axes_at(ax, (5.4, 0.9, 10.0, 5.9))
y = np.arange(len(data))[::-1]
for yy, (name, n) in zip(y, data):
    a.barh(yy, n, height=0.62, color=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.8)
    a.text(n + 0.2, yy, f"$10^{{{n}}}$", va="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.set_yticks(y, [d[0] for d in data])
a.set_xlim(0, 19.5)
a.set_xticks(range(0, 19, 2))
a.set_ylim(-0.7, len(data) - 0.3)
charts.style_axes(a, r"$\log_{10}(k_{\mathrm{cat}}/k_{\mathrm{uncat}})$", None)
top = a.secondary_xaxis("top", functions=(lambda n: n * PER_DECADE, lambda g: g / PER_DECADE))
top.set_xticks([0, 20, 40, 60, 80, 100])
top.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=bio.core.FONT["tiny"], width=0.7, length=3)
top.spines["top"].set_color(P.muted())
top.set_xlabel(r"$\Delta\Delta^{\ddagger}G$ at 25 °C / (kJ mol$^{-1}$)", fontsize=bio.core.FONT["small"], color=P.ink())
