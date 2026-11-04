"""Survival after gamma irradiation in the multi-target model S(D) = 1 - (1 - exp(-D/D0))^n (Formula 18.8.1).
Illustrative parameters chosen to reproduce typical published survival: Escherichia coli (n = 2,
D0 = 0.1 kGy; 10 % survival near 0.25 kGy), endospores of Bacillus (n = 3, D0 = 0.8 kGy; near 2.5 kGy) and
Deinococcus radiodurans (n = 100, D0 = 1.6 kGy; no loss of viability up to about 5 kGy, 10 % survival
near 12 kGy). The dashed line marks about 5 Gy, a dose lethal to most humans."""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = plt.subplots(figsize=(7.2, 4.0))
D = np.linspace(0, 20, 800)
for name, n, D0, tok, xy in [("Escherichia coli", 2, 0.1, "negative", (1.3, 1.5e-4)),
                             ("Bacillus endospores", 3, 0.8, "enzyme", (7.6, 1.5e-3)),
                             ("Deinococcus radiodurans", 100, 1.6, "dna", (13.0, 0.08))]:
    S = 1 - (1 - np.exp(-D / D0)) ** n
    ax.plot(D, np.maximum(S, 1e-9), color=charts.line(tok), lw=1.8)
    ax.text(*xy, name, fontsize=7.5, color=charts.line(tok), style="italic" if "Bacillus" not in name
            else "normal", ha="left")
ax.axvline(0.005, color=P.muted(), ls="--", lw=0.9)
ax.text(0.15, 2e-6, "lethal to humans (about 5 Gy)", fontsize=6.8, color=P.muted(), rotation=90, va="bottom")
ax.set_yscale("log")
ax.set_ylim(1e-6, 2)
ax.set_xlim(0, 20)
charts.style_axes(ax, "dose / kGy", "surviving fraction")
