"""The main transition of a phospholipid bilayer and the size of the cooperative unit (Formula 8.5.1).

Two-state model for a cooperative unit of n lipids that melt together: per mole of lipid the excess
heat capacity is Delta H_cal Delta H_vH f(1-f)/(R T^2) with Delta H_vH = n Delta H_cal; the peak area
is Delta H_cal = 36 kJ/mol for every n, its height grows as n and its width falls as 1/n
(full width at half height 3.525 R T_m^2 / Delta H_vH). T_m = 41.4 C (DPPC).
A: peaks for n = 20, 100, 500. B: full width at half height against n; points: the width of the main transition of multilamellar
DPPC vesicles (about 0.1 K) and two broadened transitions.
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
R = 8.314e-3
Tm, dHcal = 273.15 + 41.4, 36.0

fig, ax = bio.canvas(20.0, 8.0)
bio.panel(ax, "A", (0.1, 7.9))
pa = charts.axes_at(ax, (1.6, 1.3, 8.0, 5.8))
T = np.linspace(Tm - 4, Tm + 4, 4000)
for n, tok in ((20, "lipid_head"), (100, "lipid"), (500, "protein")):
    dHvH = n * dHcal
    K = np.exp(-dHvH / R * (1 / T - 1 / Tm))
    f = K / (1 + K)
    cp = dHcal * dHvH * f * (1 - f) / (R * T ** 2)
    w = 3.525 * R * Tm ** 2 / dHvH
    pa.plot(T - 273.15, cp, color=charts.line(tok), lw=1.6,
            label=f"n = {n}: height {cp.max():.0f} kJ mol⁻¹ K⁻¹, width {w:.2f} K")
pa.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
pa.set_xlim(Tm - 273.15 - 4, Tm - 273.15 + 4)
pa.set_ylim(-8, 265)
charts.style_axes(pa, "t / °C", r"$C_{p,\mathrm{ex}}$ per mol lipid / (kJ mol$^{-1}$ K$^{-1}$)")
charts.title(pa, "Same enthalpy, different cooperativity")

bio.panel(ax, "B", (10.6, 7.9))
pb = charts.axes_at(ax, (12.1, 1.3, 7.2, 5.8))
nn = np.logspace(0.5, 3.5, 200)
pb.loglog(nn, 3.525 * R * Tm ** 2 / (nn * dHcal), color=P.ink(), lw=1.5)
for w, name in ((0.1, "multilamellar DPPC"), (1.0, "broadened"), (3.0, "strongly broadened")):
    n = 3.525 * R * Tm ** 2 / (w * dHcal)
    pb.plot(n, w, "o", ms=5, mfc=P.fill("lipid_head"), mec=P.edge("lipid_head"))
    left = name.startswith("multi")
    pb.text(n / 1.25 if left else n * 1.3, w / 1.7 if left else w * 1.1, f"{name}: {w:g} K → n ≈ {n:.0f}",
            fontsize=FT["tiny"], color=P.ink(), ha="right" if left else "left")
charts.style_axes(pb, "cooperative unit n (lipids)", "full width at half height / K", box=True)
charts.title(pb, r"$\Delta T_{1/2} = 3.525\,RT_m^2/(n\,\Delta H_\mathrm{cal})$")
