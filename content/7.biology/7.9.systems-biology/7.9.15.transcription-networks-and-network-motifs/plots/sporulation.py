"""Three waves of gene expression from interlocked feed-forward loops (the mother-cell network of
Bacillus subtilis sporulation, after Eichenberger and colleagues, 2004), with logic input functions.

At t = 0 starvation activates X1 (sigma-E). X1 activates its targets Z1 and the repressor Y1 (SpoIIID),
which shuts Z1 off (I1-FFL: a pulse). X1 AND Y1 activate X2 (sigma-K; C1-FFL with an AND gate: a delay).
X2 activates targets Z2 and the repressor Y2 (GerE), which shuts Z2 off (a second pulse), and X2 AND Y2
activate the late genes Z3. All production and removal rates are 1, all thresholds 0.5 (time in units of
the removal time of the proteins). Panel B shows the regulators.
"""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
dt, K = 1e-3, 0.5
t = np.arange(0, 8, dt)
v = {k: np.zeros_like(t) for k in ["Y1", "Z1", "X2", "Y2", "Z2", "Z3"]}
for i in range(1, len(t)):
    g = {k: v[k][i - 1] for k in v}
    prod = {
        "Y1": 1.0,
        "Z1": float(g["Y1"] < K),
        "X2": float(g["Y1"] > K),
        "Y2": float(g["X2"] > K),
        "Z2": float(g["X2"] > K and g["Y2"] < K),
        "Z3": float(g["X2"] > K and g["Y2"] > K),
    }
    for k in v:
        v[k][i] = g[k] + dt * (prod[k] - g[k])

fig, axes = plt.subplots(1, 2, figsize=(10, 3.4), gridspec_kw={"width_ratios": [1.4, 1]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.86, wspace=0.25)
ax = axes[0]
for k, tok in [("Z1", "dna"), ("Z2", "positive"), ("Z3", "rna")]:
    ax.plot(t, v[k], color=charts.line(tok), lw=1.8, label=k)
ax.set_ylim(0, 1.25)
ax.legend(fontsize=7, frameon=False, loc="upper right", ncol=3)
charts.style_axes(ax, "time after onset of sigma-E activity (1/alpha)", "target expression")
charts.title(ax, "A  Early, middle and late genes")
ax = axes[1]
ax.plot(t, np.ones_like(t), color=P.ink(), lw=1.4, label="X1 (sigma-E)")
for k, tok, lab in [("Y1", "protein", "Y1 (SpoIIID)"), ("X2", "enzyme", "X2 (sigma-K)"), ("Y2", "receptor", "Y2 (GerE)")]:
    ax.plot(t, v[k], color=charts.line(tok), lw=1.4, label=lab)
ax.axhline(K, color=P.muted(), lw=0.7, ls=":")
ax.set_ylim(0, 1.4)
ax.legend(fontsize=7, frameon=False, loc="upper left", ncol=2)
charts.style_axes(ax, "time (1/alpha)", "regulator level")
charts.title(ax, "B  The regulators")
