"""How much carbon C3 photosynthesis loses to photorespiration, as a function of leaf temperature and CO2.

Gamma*(T) = 42.75 exp[37830 (T - 25) / (298.15 R (T + 273.15))] umol mol-1 (Bernacchi et al. 2001), the
oxygenation/carboxylation ratio phi = 2 Gamma*/ci with ci = 0.7 ca (C3 leaf, mesophyll resistance ignored);
each oxygenation releases half a CO2, so the fraction of carboxylated carbon lost is 0.5 phi.
A: contours of 0.5 phi over temperature and atmospheric CO2, with the CO2 levels of the last glacial maximum
(180), pre-industrial (280), today (about 420) and a high-emission future (700 umol mol-1). The thick line is
where the ATP cost of net C3 fixation, (3 + 3.5 phi)/(1 - 0.5 phi), equals that of C4 photosynthesis with
20 % bundle-sheath leakage, 3 + 2/(1 - 0.2) = 5.5 ATP; to its right (warmer, lower CO2) C4 is cheaper.
B: the lost fraction against temperature at the four CO2 levels.
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

import wikibio as bio

P = bio.P
R = 8.314


def gstar(T):
    return 42.75 * np.exp(37830 * (T - 25) / (298.15 * R * (T + 273.15)))


T = np.linspace(5, 45, 161)
ca = np.linspace(150, 1000, 171)
TT, CC = np.meshgrid(T, ca)
phi = 2 * gstar(TT) / (0.7 * CC)
loss = 0.5 * phi
cost = np.where(loss < 0.8, (3 + 3.5 * phi) / (1 - 0.5 * phi), np.nan)
cmap = LinearSegmentedColormap.from_list("loss", [P.surface(), P.fill("highlight"), P.fill("rna"), P.edge("negative")])

fig, (a, b) = plt.subplots(1, 2, figsize=(11.5, 4.4))
lev = [0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5]
cf = a.contourf(TT, CC, loss, levels=[0] + lev + [1.0], cmap=cmap)
cs = a.contour(TT, CC, loss, levels=lev, colors=[P.ink()], linewidths=0.6)
a.clabel(cs, fmt=lambda v: f"{v:.0%}", fontsize=7)
a.contour(TT, CC, cost, levels=[5.5], colors=[P.edge("plant")], linewidths=2.6)
a.text(36.5, 330, "C4 cheaper", fontsize=9, color=P.edge("plant"), weight="bold")
a.text(9, 820, "C3 cheaper", fontsize=9, color=P.edge("plant"), weight="bold")
for c, name in ((180, "glacial"), (280, "pre-industrial"), (420, "today"), (700, "future")):
    a.axhline(c, color=P.edge("dna"), lw=0.9, ls="--")
    a.text(5.5, c + 12, name, fontsize=7, color=P.edge("dna"))
a.set_xlabel("Leaf temperature $T$ / °C")
a.set_ylabel("Atmospheric CO$_2$ $c_{\\mathrm{a}}$ / µmol mol$^{-1}$")
a.set_title("A  Carbon lost to photorespiration (C3)", loc="left", fontsize=10)

cols = [P.edge("negative"), P.edge("rna"), P.edge("dna"), P.edge("plant")]
for (c, name), col in zip(((180, "180"), (280, "280"), (420, "420"), (700, "700")), cols):
    b.plot(T, 0.5 * 2 * gstar(T) / (0.7 * c), color=col, lw=2, label=f"$c_{{\\mathrm{{a}}}}$ = {name} µmol mol$^{{-1}}$")
b.set_xlim(5, 45)
b.set_ylim(0, 0.8)
b.set_xlabel("Leaf temperature $T$ / °C")
b.set_ylabel("Fraction of fixed carbon lost, $0.5\\phi$")
b.legend(frameon=False, fontsize=8, loc="upper left")
b.grid(True, alpha=0.3)
b.set_title("B  Temperature dependence", loc="left", fontsize=10)
fig.tight_layout()
