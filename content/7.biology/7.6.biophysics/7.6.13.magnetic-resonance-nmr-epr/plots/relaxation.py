# Relaxation rates as functions of the rotational correlation time (rigid isotropic tumbling unless stated).
# A: BPP theory for a pair of protons 1.8 A apart at 600 MHz: T1 has a minimum at omega0 tau_c = 0.616,
#    T2 falls monotonically; top axis: molar mass of a globular protein at tau_c = 0.5 ns per kDa (25 C).
# B: 15N R1 and R2 of a backbone amide (N-H 1.02 A, 15N CSA -170 ppm) at 600 MHz and 1 GHz.
# C: the 1H-15N heteronuclear NOE (steady-state intensity ratio) for the same cases.
# D: Lipari-Szabo model: internal correlation function C_I(t) = S^2 + (1 - S^2) exp(-t/tau_e) for three order
#    parameters (tau_e = 0.2 ns) and the total C(t) = C_I(t) exp(-t/tau_m) for tau_m = 5 ns.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
hb, mu0 = 1.054571817e-34, 1.25663706e-6
gH, gN = 2.6752218744e8, -2.71261804e7
tc = np.logspace(-12, -6.5, 400)


def J(w, tc, s2=1.0, te=0.0):
    j = s2 * tc / (1 + (w * tc) ** 2)
    if te > 0:
        t = 1 / (1 / tc + 1 / te)
        j = j + (1 - s2) * t / (1 + (w * t) ** 2)
    return 0.4 * j


def n15(tc, B0):
    wH, wN = gH * B0, gN * B0
    d = mu0 * hb * gH * gN / (4 * np.pi * 1.02e-10**3)
    c = wN * -170e-6 / np.sqrt(3)
    r1 = d**2 / 4 * (J(wH - wN, tc) + 3 * J(wN, tc) + 6 * J(wH + wN, tc)) + c**2 * J(wN, tc)
    r2 = (d**2 / 8 * (4 * J(0, tc) + J(wH - wN, tc) + 3 * J(wN, tc) + 6 * J(wH, tc) + 6 * J(wH + wN, tc))
          + c**2 / 6 * (4 * J(0, tc) + 3 * J(wN, tc)))
    noe = 1 + gH / gN * d**2 / 4 * (6 * J(wH + wN, tc) - J(wH - wN, tc)) / r1
    return r1, r2, noe


fig, axs = plt.subplots(2, 2, figsize=(11.0, 7.4))

ax = axs[0, 0]
w0 = gH * 14.09
b = mu0 / (4 * np.pi) * gH**2 * hb / 1.8e-10**3
x = tc
r1 = 0.3 * b**2 * (x / (1 + (w0 * x) ** 2) + 4 * x / (1 + 4 * (w0 * x) ** 2))
r2 = 0.15 * b**2 * (3 * x + 5 * x / (1 + (w0 * x) ** 2) + 2 * x / (1 + 4 * (w0 * x) ** 2))
ax.loglog(tc, 1 / r1, color=charts.line("protein"), lw=2.0, label="T₁")
ax.loglog(tc, 1 / r2, color=charts.line("rna"), lw=2.0, label="T₂")
tmin = 0.616 / w0
ax.axvline(tmin, color=P.muted(), lw=0.7, ls=":")
ax.text(tmin * 1.15, 3e2, "ω₀τc = 0.62", fontsize=7.5, color=P.muted())
ax.axvspan(1e-12, 0.1 / w0, color=P.light("highlight"), lw=0)
ax.text(1.5e-12, 1e-3, "extreme narrowing\nT₁ = T₂", fontsize=7.5, color=P.ink())
ax.set_xlim(1e-12, 3e-7)
ax.legend(fontsize=8, frameon=False, loc="upper right")
charts.style_axes(ax, "τc / s", "relaxation time / s")
top = ax.secondary_xaxis("top", functions=(lambda t: t / 0.5e-9, lambda m: m * 0.5e-9))
top.set_xlabel("protein mass / kDa", fontsize=8, color=P.ink())
top.tick_params(labelsize=7.5, colors=P.muted())
charts.title(ax, "A   BPP: ¹H pair, 600 MHz")

ax = axs[0, 1]
for B0, ls, name in ((14.09, "-", "600 MHz"), (23.49, "--", "1 GHz")):
    r1, r2, noe = n15(tc, B0)
    ax.loglog(tc, r1, color=charts.line("protein"), lw=1.8, ls=ls, label=f"R₁, {name}")
    ax.loglog(tc, r2, color=charts.line("rna"), lw=1.8, ls=ls, label=f"R₂, {name}")
ax.set_xlim(1e-11, 1e-7)
ax.set_ylim(0.05, 400)
ax.legend(fontsize=7.5, frameon=False, loc="upper left", ncol=2)
charts.style_axes(ax, "τc / s", "¹⁵N relaxation rate / s⁻¹")
charts.title(ax, "B   ¹⁵N R₁ and R₂ of a backbone amide")

ax = axs[1, 0]
for B0, ls, name in ((14.09, "-", "600 MHz"), (23.49, "--", "1 GHz")):
    r1, r2, noe = n15(tc, B0)
    ax.semilogx(tc, noe, color=charts.line("enzyme"), lw=1.8, ls=ls, label=name)
ax.axhline(0, color=P.muted(), lw=0.5)
ax.set_xlim(1e-12, 1e-7)
ax.legend(fontsize=8, frameon=False, loc="lower right")
charts.style_axes(ax, "τc / s", "{¹H}–¹⁵N NOE")
charts.title(ax, "C   Heteronuclear NOE: sensitive to fast motion")

ax = axs[1, 1]
t = np.linspace(0, 6, 600)                     # ns
for s2, tok in ((0.85, "protein"), (0.5, "enzyme"), (0.1, "rna")):
    ci = s2 + (1 - s2) * np.exp(-t / 0.2)
    ax.plot(t, ci, color=charts.line(tok), lw=1.8, label=f"$C_I(t)$, S² = {s2}")
    ax.plot(t, ci * np.exp(-t / 5.0), color=charts.line(tok), lw=0.9, ls="--")
    ax.axhline(s2, color=charts.line(tok), lw=0.5, ls=":")
ax.plot([], [], color=P.muted(), lw=0.9, ls="--", label="× exp(−t/τm), τm = 5 ns")
ax.set_xlim(0, 6)
ax.set_ylim(0, 1.02)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "t / ns", "correlation function")
charts.title(ax, "D   Model-free: plateau S², internal time τe = 0.2 ns")
fig.tight_layout()
