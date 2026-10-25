"""Cumulative free-energy profile of glycolysis per glucose. Standard values (Lehninger 8e) and actual
values in human erythrocytes (Minakami and Yoshikawa 1965, as tabulated in Lehninger 8e Table 14-2
and Berg et al.). Steps 6-10 count twice; steps 6 and 7 combined. The DHAP -> GAP step (5) counts once."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
labels = ["Glc", "G6P", "F6P", "F1,6BP", "DHAP + GAP", "2 GAP", "2 3PG", "2 2PG", "2 PEP", "2 Pyr"]
std = [-16.7, 1.7, -14.2, 23.8, 7.5, 2 * (6.3 - 18.5), 2 * 4.4, 2 * 7.5, 2 * -31.4]
act = [-33.4, -2.5, -22.2, -1.3, 2.5, 2 * -1.7, 2 * 0.8, 2 * -3.3, 2 * -16.7]
enz = ["HK", "PGI", "PFK-1", "Ald", "TPI", "GAPDH+PGK", "PGM", "Eno", "PK"]
cs, ca = np.concatenate([[0], np.cumsum(std)]), np.concatenate([[0], np.cumsum(act)])

fig, ax = bio.canvas(18.0, 9.4)
a = charts.axes_at(ax, (2.0, 1.8, 15.0, 6.8))
x = np.arange(len(labels))
a.step(x, cs, where="post", color=charts.line("neutral"), lw=1.8, ls="--", label=r"standard, $\Delta_{\mathrm{r}}G'^{\circ}$")
a.step(x, ca, where="post", color=charts.line("drug"), lw=2.2, label=r"erythrocyte, $\Delta_{\mathrm{r}}G$")
for k in range(len(enz)):
    a.text(k + 1, 28, enz[k], ha="center", fontsize=bio.core.FONT["tiny"], color=P.muted())
for k in (0, 2, 8):
    a.annotate("", (k + 1, ca[k + 1]), (k + 1, ca[k]), arrowprops=dict(arrowstyle="->", color=P.edge("negative"), lw=1.4))
a.set_xticks(x)
a.set_xticklabels(labels, rotation=0)
a.set_xlim(-0.3, len(labels) - 0.5)
a.set_ylim(-115, 40)
a.axhline(0, color=P.muted(), lw=0.6)
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(a, "intermediate (per glucose)", r"cumulative $\Delta G$ / (kJ mol$^{-1}$)")
charts.title(a, "Three large drops in the cell: hexokinase, PFK-1, pyruvate kinase")
