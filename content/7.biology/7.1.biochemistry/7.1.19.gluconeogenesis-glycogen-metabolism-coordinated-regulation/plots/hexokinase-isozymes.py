"""Hexokinase I (Michaelis-Menten, K_M = 0.1 mM) and hexokinase IV / glucokinase (Hill equation,
K_0.5 = 8 mM, n_H = 1.7) against the glucose concentration (liver: GLUT2 equilibrates cytosol and blood).
A: relative rate v/Vmax. B: elasticity (d ln v / d ln [glucose]), the fractional change of rate per
fractional change of glucose: n_H (1 - theta) for a Hill enzyme, K_M / (K_M + S) for a Michaelis-Menten one.
Shaded bands: blood glucose after an overnight fast (about 4-5.5 mM) and portal-vein glucose after a
carbohydrate meal (up to about 10-15 mM)."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
S = np.linspace(0.001, 20, 800)
KM1 = 0.1
K05, NH = 8.0, 1.7
hk1 = S / (KM1 + S)
gk = S**NH / (K05**NH + S**NH)
e_hk1 = KM1 / (KM1 + S)
e_gk = NH * (1 - gk)

fig, ax = bio.canvas(22.0, 9.0)
for k, (x0, title) in enumerate(((1.8, "Rate"), (13.0, "Sensitivity to glucose"))):
    a = charts.axes_at(ax, (x0, 1.3, 8.2, 6.6))
    for lo, hi, txt in ((4, 5.5, "fasting"), (8, 15, "after a meal\n(portal blood)")):
        a.axvspan(lo, hi, color=P.fill("highlight"), alpha=0.35, lw=0)
        a.text((lo + hi) / 2, 0.03 if k == 0 else 1.83, txt, ha="center", va="bottom" if k == 0 else "top", fontsize=bio.core.FONT["tiny"],
               color=P.muted())
    if k == 0:
        a.plot(S, hk1, color=charts.line("enzyme"), lw=2.0, label=r"hexokinase I ($K_{\mathrm{M}}$ = 0.1 mM)")
        a.plot(S, gk, color=charts.line("drug"), lw=2.0, label=r"glucokinase ($K_{0.5}$ = 8 mM, $n_{\mathrm{H}}$ = 1.7)")
        a.set_ylim(0, 1.05)
        charts.style_axes(a, "[glucose] / mM", r"$v_0/v_{\max}$")
        a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right")
    else:
        a.plot(S, e_hk1, color=charts.line("enzyme"), lw=2.0)
        a.plot(S, e_gk, color=charts.line("drug"), lw=2.0)
        a.set_ylim(0, 1.9)
        charts.style_axes(a, "[glucose] / mM", r"elasticity $\partial \ln v/\partial \ln[\mathrm{glucose}]$")
    a.set_xlim(0, 20)
    a.set_xticks([0, 5, 10, 15, 20])
    bio.panel(ax, "AB"[k], (x0 - 1.4, 8.6))
