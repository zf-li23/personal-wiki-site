"""Light and photosynthesis inside a canopy (big-leaf layers, Beer's law).

Photon flux on a horizontal plane at cumulative leaf area index L below the top: I(L) = I0 exp(-k L), with
I0 = 1800 umol m-2 s-1 and extinction coefficient k = 0.4 (erect leaves, e.g. modern rice and wheat) or 0.8
(more horizontal leaves). Light absorbed per unit leaf area at depth L is k I(L); each layer follows the
non-rectangular hyperbola (phi = 0.05, Amax = 30, theta = 0.7, Rd = 1.5 umol m-2 s-1; in the canopy, leaf
respiration and Amax are not reduced with depth, a simplification). Canopy net photosynthesis is the integral
over L from 0 to LAI, minus non-leaf respiration of 1 umol m-2 s-1 per unit LAI (stems, roots).
A: relative light and leaf net photosynthesis against depth; B: canopy net photosynthesis against LAI.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
I0, phi, amax, th, rd = 1800.0, 0.05, 30.0, 0.7, 1.5


def leaf(i):
    s = phi * i + amax
    return (s - np.sqrt(s * s - 4 * th * phi * i * amax)) / (2 * th) - rd


L = np.linspace(0, 10, 1001)
fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.3))
for k, col, name in ((0.4, P.edge("plant"), "erect leaves, $k$ = 0.4"), (0.8, P.edge("rna"), "horizontal leaves, $k$ = 0.8")):
    I = I0 * np.exp(-k * L)
    a.plot(I / I0, L, color=col, lw=1.4, ls="--")
    a.plot(leaf(k * I) / amax, L, color=col, lw=2, label=name)
    lai = np.linspace(0, 10, 201)
    cum = np.array([np.trapezoid(leaf(k * I0 * np.exp(-k * L[L <= x])), L[L <= x]) if x > 0 else 0 for x in lai])
    net = cum - 1.0 * lai
    b.plot(lai, net, color=col, lw=2, label=name)
    j = np.argmax(net)
    b.plot([lai[j]], [net[j]], "o", color=col, ms=6)
    b.text(lai[j], net[j] + 1.2, f"LAI$_{{\\mathrm{{opt}}}}$ ≈ {lai[j]:.1f}", ha="center", fontsize=8, color=col)
a.axvline(0, color=P.muted(), lw=0.8)
a.invert_yaxis()
a.set_xlim(-0.15, 1.05)
a.set_xlabel("Relative value (dashed: $I/I_0$; solid: leaf $A/A_{\\max}$)")
a.set_ylabel("Cumulative leaf area index from the top $L$")
a.legend(frameon=False, fontsize=8, loc="lower right")
a.set_title("A  Down through the canopy", loc="left", fontsize=10)
b.set_xlim(0, 10)
b.set_ylim(0, 56)
b.set_xlabel("Leaf area index LAI")
b.set_ylabel("Canopy net photosynthesis / µmol m$^{-2}$ s$^{-1}$")
b.legend(frameon=False, fontsize=8, loc="lower right")
b.set_title("B  Canopy photosynthesis and LAI", loc="left", fontsize=10)
for x in (a, b):
    x.grid(True, alpha=0.3)
fig.tight_layout()
