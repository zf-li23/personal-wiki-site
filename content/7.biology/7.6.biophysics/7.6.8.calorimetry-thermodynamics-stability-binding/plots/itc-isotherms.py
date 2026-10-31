"""Isothermal titration calorimetry of 1:1 binding (Formulas 8.4.1-8.4.3).

Cell: V0 = 200 uL of macromolecule M; 19 injections of 2 uL ligand L (plus a 0.4 uL first injection,
discarded as usual). Concentrations in the overflow cell follow the standard model
[M]_t = M0 (1 - v/2V0)/(1 + v/2V0), [L]_t = L0 (v/V0)(1 - v/2V0), v = cumulative injected volume;
the bound concentration is the root of the binding quadratic, and the heat of injection i is
dQ_i = Q_i - Q_{i-1} + (dv/V0)(Q_i + Q_{i-1})/2 with Q = V0 Delta H [ML].
A: simulated raw power trace for c = 50 (each injection relaxes with a 12 s instrument time
constant; seed 0 noise). B: normalized isotherms for Wiseman c = n K_a [M]_t from 0.5 to 5000.
C: the c = 50 data with Gaussian noise (0.15 uJ) fitted by nonlinear least squares for n, K_a and
Delta H; and the same experiment at c = 5000, where K_a is not determined.
"""

import numpy as np
from scipy.optimize import curve_fit
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
V0 = 200e-6                 # L
dv = np.r_[0.4e-6, np.full(19, 2.0e-6)]
M0 = 20e-6                  # M
L0 = 220e-6                 # M


def concentrations(M0, L0):
    v = np.cumsum(dv)
    Mt = M0 * (1 - v / (2 * V0)) / (1 + v / (2 * V0))
    Lt = L0 * (v / V0) * (1 - v / (2 * V0))
    return Mt, Lt


def bound(Mt, Lt, n, Ka):
    s = n * Mt + Lt + 1.0 / Ka
    return (s - np.sqrt(s * s - 4 * n * Mt * Lt)) / 2          # [ML] in M (n sites per M)


def heats(n, Ka, dH, M0=M0, L0=L0):
    """Heat of each injection in uJ (dH in kJ/mol)."""
    Mt, Lt = concentrations(M0, L0)
    Q = V0 * dH * 1e3 * bound(Mt, Lt, n, Ka) * 1e6               # uJ
    Qprev = np.r_[0.0, Q[:-1]]
    dvi = dv
    return Q - Qprev + dvi / V0 * (Q + Qprev) / 2


rng = np.random.default_rng(0)
n_true, dH_true = 1.0, -45.0
fig, ax = bio.canvas(24.0, 8.4)

# A: raw thermogram for c = 50
bio.panel(ax, "A", (0.1, 8.3))
pa = charts.axes_at(ax, (1.4, 1.3, 6.0, 5.8))
Ka50 = 50 / (n_true * M0)
q = heats(n_true, Ka50, dH_true)
tau, spacing = 12.0, 150.0
t = np.arange(0, spacing * (len(q) + 1), 0.5)
power = np.zeros_like(t)
for i, qi in enumerate(q):
    t0 = 60 + spacing * i
    m = t >= t0
    power[m] += qi / tau * np.exp(-(t[m] - t0) / tau)
power += rng.normal(0, 0.01, t.size)
pa.plot(t / 60, power, color=charts.line("protein"), lw=0.8)
pa.set_xlim(0, t[-1] / 60)
charts.style_axes(pa, "time / min", "differential power / µW")
charts.title(pa, "Raw data (c = 50): one peak per injection")

# B: isotherms for several c
bio.panel(ax, "B", (8.2, 8.3))
pb = charts.axes_at(ax, (9.5, 1.3, 6.0, 5.8))
Mt, Lt = concentrations(M0, L0)
ratio = Lt / Mt
toks = ["neutral", "channel", "protein", "receptor", "enzyme"]
for c, tok in zip([0.5, 5, 50, 500, 5000], toks):
    Ka = c / (n_true * M0)
    qq = heats(n_true, Ka, dH_true)
    norm = qq / (dv * L0 * 1e6) / 1e3                            # kJ per mol injectant
    pb.plot(ratio[1:], norm[1:], "o-", ms=3, lw=1.0, color=charts.line(tok), label=f"c = {c:g}")
pb.axvline(1.0, color=P.muted(), lw=0.6, ls=":")
pb.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(pb, "molar ratio [L]$_t$/[M]$_t$", "heat per mol injectant / (kJ/mol)")
charts.title(pb, "Wiseman c sets the shape")

# C: fit at c = 50 and at c = 5000
bio.panel(ax, "C", (16.3, 8.3))
pc = charts.axes_at(ax, (17.6, 1.3, 6.0, 5.8))
for c, tok, yoff in ((50, "protein", 0), (5000, "enzyme", 0)):
    Ka = c / (n_true * M0)
    data = heats(n_true, Ka, dH_true) + rng.normal(0, 0.15, len(dv))
    f = lambda _x, n, logK, dH: heats(n, 10 ** logK, dH)[1:]
    popt, pcov = curve_fit(f, np.arange(len(dv) - 1), data[1:], p0=(0.9, np.log10(Ka) - 0.5, -35.0))
    err = np.sqrt(np.diag(pcov))
    norm = 1 / (dv[1:] * L0 * 1e6) / 1e3
    pc.plot(ratio[1:], data[1:] * norm, "o", ms=3.2, mfc=charts.line(tok), mec="none")
    pc.plot(ratio[1:], f(None, *popt) * norm, color=charts.line(tok), lw=1.1)
    Kd = 1e9 / 10 ** popt[0 + 1]
    rel = np.log(10) * err[1] * 100
    label = (f"c = {c}: n = {popt[0]:.3f} ± {err[0]:.3f}\nΔH = {popt[2]:.1f} ± {err[2]:.1f} kJ/mol\n"
             f"K$_d$ = {Kd:.3g} nM ± {rel:.0f} % (true {1e9 / Ka:.3g})")
    pc.text(1.22, -12.0 - (0 if c == 50 else 13.0), label, fontsize=FT["tiny"], color=charts.line(tok), va="top")
pc.set_ylim(-50, 2)
charts.style_axes(pc, "molar ratio [L]$_t$/[M]$_t$", "heat per mol injectant / (kJ/mol)")
charts.title(pc, "Fits: K is determined only at moderate c")
