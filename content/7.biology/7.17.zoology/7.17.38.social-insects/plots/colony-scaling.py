# Metabolic scaling of insect colonies (schematic). Dashed: slope 1, expected if a colony were a sum of
# independent workers. Solid: slope 3/4, close to whole-colony measurements (Waters and coauthors 2010;
# Hou and coauthors 2010). Intercepts arbitrary; no data points. Inset: per-worker rate ~ M^(-1/4).
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(16, 9.5)
a = charts.axes_at(ax, (1.9, 1.4, 13.3, 7.4))
M = np.logspace(-1, 3, 100)
a.loglog(M, M, color=P.muted(), ls="--", lw=1.4, label="sum of independent workers (slope 1)")
a.loglog(M, M ** 0.75, color=P.edge("positive"), lw=2, label="whole colonies (slope about 3/4)")
a.set_xlabel("Colony mass (relative units)")
a.set_ylabel("Colony metabolic rate (relative units)")
a.legend(fontsize=7, frameon=False, loc="upper left")
ins = charts.axes_at(ax, (10.6, 2.4, 4.2, 2.1))
ins.loglog(M, M ** -0.25, color=P.edge("positive"), lw=1.6)
ins.loglog(M, np.ones_like(M), color=P.muted(), ls="--", lw=1.2)
ins.set_xlabel("colony mass", fontsize=6)
ins.set_ylabel("rate per unit mass", fontsize=6)
ins.tick_params(labelsize=5)
