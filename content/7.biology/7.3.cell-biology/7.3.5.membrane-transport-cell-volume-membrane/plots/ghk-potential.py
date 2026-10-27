"""Resting membrane potential from the Goldman-Hodgkin-Katz voltage equation (37 C).

Inside: Na 12, K 140, Cl 8 mM. Outside: K varied with Na + K = 150 mM, Cl 110 mM.
A: V_m against [K+]_o (log axis) for P_Na : P_K = 0.05 and P_Cl : P_K = 0.4, compared with the
Nernst potential E_K; the GHK curve follows E_K at high [K+]_o and bends away at low [K+]_o, where
the small Na+ permeability dominates. Dotted: with the electrogenic pump (Mullins-Noda form, r = 3/2).
B: V_m against P_Na / P_K (log axis) at normal concentrations: raising the relative Na+ permeability
moves the potential from near E_K towards E_Na, the change that produces an action potential.
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
RTF = 8.314 * 310 / 96485 * 1e3  # mV
Nai, Ki, Cli, Clo = 12.0, 140.0, 8.0, 110.0


def ghk(Ko, Nao, pna=0.05, pcl=0.4, r=1.0):
    return RTF * np.log((r * Ko + pna * Nao + pcl * Cli) / (r * Ki + pna * Nai + pcl * Clo))


fig, ax = bio.canvas(22.0, 8.0)
bio.panel(ax, "A", (0.1, 7.8))
pa = charts.axes_at(ax, (1.7, 1.3, 8.2, 5.8))
Ko = np.logspace(0, np.log10(150), 300)
Nao = 150 - Ko
pa.semilogx(Ko, RTF * np.log(Ko / Ki), color=charts.line("neutral"), lw=1.6, ls=(0, (4, 2)), label=r"Nernst potential $E_{\mathrm{K}}$")
pa.semilogx(Ko, ghk(Ko, Nao), color=charts.line("k"), lw=2.0, label=r"GHK, $P_{\mathrm{Na}} : P_{\mathrm{K}} = 0.05$")
pa.semilogx(Ko, ghk(Ko, Nao, r=1.5), color=charts.line("negative"), lw=1.3, ls=(0, (1, 1.6)), label="GHK with pump (r = 3/2)")
pa.axvline(5, color=P.muted(), lw=0.6, ls=(0, (1, 2)))
pa.text(5.3, 10, "normal [K⁺]ₒ", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="left")
pa.set_xlim(1, 150)
pa.set_ylim(-140, 20)
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(pa, "[K⁺]ₒ / mM", r"$V_{\mathrm{m}}$ / mV")
charts.title(pa, "Dependence on external K⁺")

bio.panel(ax, "B", (11.3, 7.8))
pb = charts.axes_at(ax, (12.9, 1.3, 7.6, 5.8))
ratio = np.logspace(-3, 2, 300)
pb.semilogx(ratio, ghk(5.0, 145.0, pna=ratio), color=charts.line("na"), lw=2.0)
ENa = RTF * np.log(145 / Nai)
EK = RTF * np.log(5 / Ki)
for E, name, dy in ((ENa, r"$E_{\mathrm{Na}}$", 3), (EK, r"$E_{\mathrm{K}}$", -10)):
    pb.axhline(E, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
    pb.text(1.2e-3, E + dy, f"{name} = {E:.0f} mV", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="left")
for r, name in ((0.05, "rest"), (20, "peak of action potential")):
    pb.plot([r], [ghk(5.0, 145.0, pna=r)], "o", color=charts.line("na"), ms=5)
    pb.text(r * (1.3 if r < 1 else 0.75), ghk(5.0, 145.0, pna=r) - 8, name, fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="left" if r < 1 else "right")
pb.set_xlim(1e-3, 100)
pb.set_ylim(-110, 80)
charts.style_axes(pb, r"$P_{\mathrm{Na}} / P_{\mathrm{K}}$", r"$V_{\mathrm{m}}$ / mV")
charts.title(pb, r"Relative permeability sets $V_{\mathrm{m}}$")
