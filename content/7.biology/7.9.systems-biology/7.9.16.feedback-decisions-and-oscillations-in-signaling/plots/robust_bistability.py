"""Two positive feedback loops make bistability robust (after Ferrell, 2008).

a = fraction of Cdk1 that is active. Activation by the phosphatase Cdc25 at rate (0.01 + H(a))(1 - a),
with H(a) = a^3/(0.3^3 + a^3): active Cdk1 activates Cdc25 (loop 1). Inactivation by the kinase Wee1 at
rate w (k2 + k2f (1 - H(a))) a, with overall Wee1 level w. One loop: k2 = 1, k2f = 0 (Wee1 constant).
Two loops: k2 = 0.01, k2f = 1 (active Cdk1 also inhibits Wee1, loop 2).
A, B: rate plots at three Wee1 levels: activation (solid) and inactivation (dashed); fixed points are
their intersections. With one loop the inactivation lines are straight and cross the hump-shaped
activation curve three times only in a narrow range of w; with two loops both curves are humped.
C: active Cdk1 at the fixed points against w (log scale). Bistability: 0.277 < w < 1.19 (4.3-fold) with
one loop, 0.275 < w < 4.99 (18-fold) with two loops.
"""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
a = np.linspace(1e-4, 1 - 1e-4, 4001)
H = a ** 3 / (0.3 ** 3 + a ** 3)
act = (0.01 + H) * (1 - a)
designs = {"one loop": (1.0, 0.0), "two loops": (0.01, 1.0)}
fig, axes = plt.subplots(1, 3, figsize=(11, 3.5))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.16, top=0.86, wspace=0.32)
for ax, (name, (k2, k2f)), ws in [(axes[0], list(designs.items())[0], [0.2, 0.6, 1.5]),
                                  (axes[1], list(designs.items())[1], [0.5, 1.5, 3.0])]:
    ax.plot(a, act, color=charts.line("positive"), lw=1.8, label="activation (Cdc25)")
    for j, w in enumerate(ws):
        inh = w * (k2 + k2f * (1 - H)) * a
        ax.plot(a, inh, color=charts.line("negative"), lw=1.2, ls="--", alpha=0.5 + 0.25 * j,
                label=f"inactivation, w = {w:g}")
    ax.set_ylim(0, 0.75)
    ax.legend(fontsize=7, frameon=False, loc="upper right")
    charts.style_axes(ax, "active Cdk1, a", "rate")
    charts.title(ax, ("A  " if name == "one loop" else "B  ") + name)

ax = axes[2]
for (name, (k2, k2f)), tok in zip(designs.items(), ["enzyme", "protein"]):
    w = act / ((k2 + k2f * (1 - H)) * a)
    dw = np.gradient(w)
    st = dw < 0
    seg = np.split(np.arange(len(a)), np.where(np.diff(st.astype(int)) != 0)[0] + 1)
    for j, idx in enumerate(seg):
        ax.semilogx(w[idx], a[idx], color=charts.line(tok), lw=1.8 if st[idx[0]] else 1.0,
                    ls="-" if st[idx[0]] else "--", label=name if j == 0 else None)
ax.set_xlim(0.05, 50)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "Wee1 level w", "active Cdk1 at steady state")
charts.title(ax, "C  Width of the bistable range")
