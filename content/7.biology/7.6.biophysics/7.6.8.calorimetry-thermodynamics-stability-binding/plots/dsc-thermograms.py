"""Excess heat capacity of protein unfolding (Formulas 8.2.1 and 8.2.2).

A: a two-state protein (T_m = 60 C, Delta H_m = 350 kJ/mol, Delta C_p = 6 kJ/(mol K)); the excess
heat capacity over the native baseline is the transition peak f(1-f) Delta H^2/(R T^2) plus the
progress baseline f Delta C_p, which interpolates between the native and unfolded baselines.
B: three proteins with the same calorimetric enthalpy per mole of polypeptide chains, analysed the
same way: one two-state domain, two independent two-state domains (T_m = 55 and 65 C) and a dimer
that dissociates on unfolding (N2 <=> 2U, 50 uM chains). The van 't Hoff enthalpy from the peak height, 4 R T_max^2 C_max / Delta H_cal,
divided by the calorimetric enthalpy (peak area) is 1, < 1 and > 1. C: a simulated noisy scan with
sloping baselines fitted by the two-state model with Delta C_p (nonlinear least squares).
"""

import numpy as np
from scipy.optimize import brentq, curve_fit
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
R = 8.314e-3            # kJ/(mol K)


def dH_of(T, Tm, dH, dCp):
    return dH + dCp * (T - Tm)


def dG_of(T, Tm, dH, dCp):
    return dH * (1 - T / Tm) + dCp * (T - Tm - T * np.log(T / Tm))


def two_state(T, Tm, dH, dCp):
    K = np.exp(-dG_of(T, Tm, dH, dCp) / (R * T))
    f = K / (1 + K)
    h = dH_of(T, Tm, dH, dCp)
    peak = f * (1 - f) * h ** 2 / (R * T ** 2)
    return f, peak, f * dCp


T = np.linspace(273.15 + 30, 273.15 + 90, 1200)
t = T - 273.15
fig, ax = bio.canvas(24.0, 8.0)

# A
bio.panel(ax, "A", (0.1, 7.9))
pa = charts.axes_at(ax, (1.4, 1.3, 6.0, 5.6))
f, peak, prog = two_state(T, 333.15, 350.0, 6.0)
pa.plot(t, peak + prog, color=charts.line("protein"), lw=1.8, label="excess C$_p$")
pa.plot(t, prog, color=P.muted(), lw=1.0, ls="--", label=r"progress baseline $f\,\Delta C_p$")
pa.plot(t, np.zeros_like(t), color=P.muted(), lw=0.8, ls=":")
pa.plot(t, np.full_like(t, 6.0), color=P.muted(), lw=0.8, ls=":")
pa.fill_between(t, prog, peak + prog, color=P.light("protein"), lw=0)
pa.annotate(r"$\Delta C_p$", xy=(86, 3.0), ha="center", fontsize=FT["tiny"], color=P.ink())
pa.annotate("", xy=(84, 0), xytext=(84, 6), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.7))
area = np.trapezoid(peak, T)
pa.text(33, 37, "shaded area = $\\Delta H_\\mathrm{cal}$\n" + f"= {area:.0f} kJ/mol", fontsize=FT["tiny"], color=P.ink(), va="top")
pa.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
pa.set_xlim(30, 90)
pa.set_ylim(-2, 40)
charts.style_axes(pa, "t / °C", r"$C_{p,\mathrm{ex}}$ / (kJ mol$^{-1}$ K$^{-1}$)")
charts.title(pa, "Two-state unfolding")

# B
bio.panel(ax, "B", (8.2, 7.9))
pb = charts.axes_at(ax, (9.5, 1.3, 6.0, 5.6))
cases = []
_, p1, _ = two_state(T, 333.15, 400.0, 0.0)
cases.append(("one domain", p1, "protein"))
_, pa_, _ = two_state(T, 328.15, 200.0, 0.0)
_, pb_, _ = two_state(T, 338.15, 200.0, 0.0)
cases.append(("two domains", pa_ + pb_, "enzyme"))
# dimer N2 <=> 2U at total monomer concentration Ct: K = [U]^2/[N2], f = [U]/Ct, K = 2 Ct f^2/(1-f)
Ct = 50e-6
dHd = 800.0             # per mol of dimer, 400 per mol of chains
Tmd = 333.15


def frac_dimer(TT):
    out = []
    for x in TT:
        K = Ct * np.exp(-dHd * (1 - x / Tmd) / (R * x))    # K = Ct where f = 1/2
        g = lambda fr: 2 * Ct * fr ** 2 / (1 - fr) - K
        out.append(brentq(g, 1e-12, 1 - 1e-12))
    return np.array(out)


fd = frac_dimer(T)
Hd = fd * dHd / 2               # enthalpy per mol of chains relative to N2
pd = np.gradient(Hd, T)
cases.append(("dimer, N$_2$ ⇌ 2U", pd, "receptor"))
for name, pk, tok in cases:
    i = np.argmax(pk)
    Hcal = np.trapezoid(pk, T)
    HvH = 4 * R * T[i] ** 2 * pk[i] / Hcal
    pb.plot(t, pk, color=charts.line(tok), lw=1.6, label=f"{name}: ΔH$_\\mathrm{{vH}}$/ΔH$_\\mathrm{{cal}}$ = {HvH / Hcal:.2f}")
pb.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
pb.set_xlim(40, 80)
pb.set_ylim(0, 60)
charts.style_axes(pb, "t / °C", r"$C_{p,\mathrm{ex}}$ − baseline / (kJ mol$^{-1}$ K$^{-1}$)")
charts.title(pb, r"Same $\Delta H_\mathrm{cal}$ = 400 kJ per mol of chains")

# C: fit of a simulated scan
bio.panel(ax, "C", (16.3, 7.9))
pc = charts.axes_at(ax, (17.6, 1.3, 6.0, 5.6))
rng = np.random.default_rng(0)
Tg = np.linspace(273.15 + 35, 273.15 + 85, 140)


def model(TT, Tm, dH, dCp, a, b):
    f, pk, pr = two_state(TT, Tm, dH, dCp)
    return a + b * (TT - 333.15) + pk + pr


true = (334.0, 420.0, 7.0, 18.0, 0.10)
y = model(Tg, *true) + rng.normal(0, 0.6, Tg.size)
popt, pcov = curve_fit(model, Tg, y, p0=(330, 300, 4, 17, 0.0))
err = np.sqrt(np.diag(pcov))
pc.plot(Tg - 273.15, y, "o", ms=2.6, mfc=charts.line("protein"), mec="none")
pc.plot(Tg - 273.15, model(Tg, *popt), color=P.ink(), lw=1.2)
pc.text(36, 59, f"fit: T$_m$ = {popt[0] - 273.15:.2f} ± {err[0]:.2f} °C\nΔH$_m$ = {popt[1]:.0f} ± {err[1]:.0f} kJ/mol\n"
        f"ΔC$_p$ = {popt[2]:.1f} ± {err[2]:.1f} kJ/(mol K)", fontsize=FT["tiny"], color=P.ink(), va="top")
pc.text(36, 44, "true: 60.85 °C, 420, 7.0", fontsize=FT["tiny"], color=P.muted(), va="top")
pc.set_xlim(35, 85)
charts.style_axes(pc, "t / °C", r"$C_p$ of protein / (kJ mol$^{-1}$ K$^{-1}$)")
charts.title(pc, "Fitting a scan")
