"""Two-state unfolding N <=> U.
A: thermal melts f_U(T) for T_m = 60 C and three van 't Hoff enthalpies (Delta C_p = 6 kJ/(mol K)).
B: simulated chemical denaturation (CD signal with sloping baselines, Gaussian noise, seed 0),
fitted by nonlinear least squares with the linear extrapolation model
Delta G_U([D]) = Delta G_U(H2O) - m [D]; inset: Delta G_U from the transition-zone points.
C: stability curves Delta G_U(T) from the Gibbs-Helmholtz equation with constant Delta C_p for a
stable protein and a destabilized variant; open circles: heat and cold denaturation (Delta G_U = 0)."""

import numpy as np
from scipy.optimize import brentq, curve_fit
import wikibio as bio
from wikibio import charts

P = bio.P
R = 8.314e-3          # kJ/(mol K)
T0 = 298.15


def dG(T, Tm, dH, dCp):
    return dH * (1 - T / Tm) + dCp * (T - Tm - T * np.log(T / Tm))


def fU(g, T):
    K = np.exp(-g / (R * T))
    return K / (1 + K)


fig, ax = bio.canvas(21.0, 7.6)

# A: thermal melts
bio.panel(ax, "A", (0.1, 7.5))
pa = charts.axes_at(ax, (1.4, 1.3, 5.2, 5.4))
T = np.linspace(273.15 + 20, 273.15 + 90, 400)
for dH, tok in ((150, "neutral"), (350, "protein"), (600, "receptor")):
    pa.plot(T - 273.15, fU(dG(T, 333.15, dH, 0.0), T), color=charts.line(tok), lw=1.7, label=rf"$\Delta_\mathrm{{U}}H_\mathrm{{m}}$ = {dH} kJ/mol")
pa.axhline(0.5, color=P.muted(), lw=0.6, ls=":")
pa.axvline(60, color=P.muted(), lw=0.6, ls=":")
pa.text(61.5, 0.06, r"$T_\mathrm{m}$", fontsize=bio.core.FONT["tiny"], color=P.ink())
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
pa.set_xlim(20, 90)
pa.set_ylim(-0.03, 1.03)
charts.style_axes(pa, "t / °C", r"fraction unfolded $f_\mathrm{U}$")
charts.title(pa, "Thermal denaturation")

# B: chemical denaturation with fit
bio.panel(ax, "B", (7.2, 7.5))
pb = charts.axes_at(ax, (8.5, 1.3, 5.2, 5.4))
rng = np.random.default_rng(0)
true = dict(g0=30.0, m=12.0, yN=-10.0, sN=0.3, yU=-1.5, sU=0.2)


def signal(D, g0, m, yN, sN, yU, sU):
    f = fU(g0 - m * D, T0)
    return (yN + sN * D) * (1 - f) + (yU + sU * D) * f


D = np.linspace(0, 5, 34)
y = signal(D, **true) + rng.normal(0, 0.25, D.size)
popt, pcov = curve_fit(signal, D, y, p0=[20, 8, -10, 0, -1, 0])
perr = np.sqrt(np.diag(pcov))
Dd = np.linspace(0, 5, 300)
pb.plot(D, y, "o", ms=3.4, mfc=charts.line("protein"), mec="none")
pb.plot(Dd, signal(Dd, *popt), color=P.ink(), lw=1.3)
Cm = popt[0] / popt[1]
pb.axvline(Cm, color=P.muted(), lw=0.6, ls=":")
pb.text(2.62, -6.4, f"fit: ΔG(H₂O) = {popt[0]:.1f} ± {perr[0]:.1f} kJ/mol\n"
        f"m = {popt[1]:.1f} ± {perr[1]:.1f} kJ/(mol M)\n" + r"$C_\mathrm{m}$" + f" = {Cm:.2f} M", fontsize=bio.core.FONT["tiny"], color=P.ink(),
        va="top")
charts.style_axes(pb, "[GdnHCl] / M", "CD signal at 222 nm (a.u.)")
charts.title(pb, "Chemical denaturation")
# inset: linear extrapolation
ins = charts.axes_at(ax, (9.35, 4.2, 1.6, 1.5))
yN = popt[2] + popt[3] * D
yU = popt[4] + popt[5] * D
fobs = (y - yN) / (yU - yN)
ok = (fobs > 0.1) & (fobs < 0.9)
gobs = -R * T0 * np.log(fobs[ok] / (1 - fobs[ok]))
ins.plot(D[ok], gobs, "o", ms=2.4, mfc=charts.line("protein"), mec="none")
xx = np.array([0, 3.2])
ins.plot(xx, popt[0] - popt[1] * xx, color=P.ink(), lw=0.9, ls="--")
ins.set_xlim(0, 3.2)
ins.set_ylim(-8, 34)
charts.style_axes(ins, "[D] / M", r"$\Delta_\mathrm{U}G$", size="tiny")

# C: stability curves
bio.panel(ax, "C", (14.3, 7.5))
pc = charts.axes_at(ax, (15.6, 1.3, 5.2, 5.4))
Tc_all = np.linspace(200, 360, 500)
for (Tm, dH, dCp, tok, name) in ((333.15, 350.0, 6.0, "protein", "stable"), (318.15, 220.0, 9.0, "drug", "destabilized")):
    g = dG(Tc_all, Tm, dH, dCp)
    pc.plot(Tc_all - 273.15, g, color=charts.line(tok), lw=1.7, label=name)
    Ts = Tm * np.exp(-dH / (Tm * dCp))
    cold = brentq(lambda t: dG(t, Tm, dH, dCp), 150, Ts)
    for tt in (cold, Tm):
        pc.plot(tt - 273.15, 0, "o", ms=4.5, mfc=P.surface(), mec=charts.line(tok), mew=1.2, zorder=5)
    pc.plot(Ts - 273.15, dG(Ts, Tm, dH, dCp), "^", ms=4.5, color=charts.line(tok), zorder=5)
    pc.annotate(f"{cold - 273.15:.0f} °C".replace("-", "−"), (cold - 273.15, 0), (cold - 273.15 + 3, -8),
                fontsize=bio.core.FONT["tiny"], color=charts.line(tok))
pc.axhline(0, color=P.muted(), lw=0.7)
pc.text(-20, 33, r"▲ maximum stability ($\Delta_\mathrm{U}S = 0$)", fontsize=bio.core.FONT["tiny"], color=P.ink())
pc.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower center")
pc.set_xlim(-70, 85)
pc.set_ylim(-20, 38)
charts.style_axes(pc, "t / °C", r"$\Delta_\mathrm{U}G$ / (kJ/mol)")
charts.title(pc, "Stability curve")
