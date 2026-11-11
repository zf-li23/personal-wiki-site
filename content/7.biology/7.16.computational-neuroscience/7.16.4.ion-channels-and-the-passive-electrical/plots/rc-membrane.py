"""The passive single-compartment membrane. A: equivalent circuit (capacitance C, leak conductance
g_L with battery E_L, injected current). B: voltage response to a current step (soma sphere of radius
20 um: c_m = 1 uF/cm2, R_m = 5 kOhm cm2, hence C = 50 pF, R_in = 99 MOhm, tau_m = 5 ms) with the
time constant marked, for the nominal membrane and for the same cell when a synaptic conductance
doubles g_L (shunting: R_in halves, tau_m halves). C: amplitude of the response to sinusoidal
current, |Z|(f) = R_in / sqrt(1 + (2 pi f tau_m)^2): the membrane is a low-pass filter. D: the resting
potential as the conductance-weighted mean of the reversal potentials, V = sum g_i E_i / sum g_i, with
E_K = -89, E_Cl = -69, E_Na = +66 mV and g_K = 1, g_Cl = 0.2, as a function of g_Na / g_K."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts, neuro

P = bio.P
FT = bio.core.FONT
fig = plt.figure(figsize=(10.4, 5.6))

# A: circuit on a canvas-like axes
axc = fig.add_axes([0.02, 0.55, 0.30, 0.4])
axc.set_xlim(0, 6); axc.set_ylim(0, 4.4); axc.set_aspect("equal"); axc.axis("off")
neuro.wire(axc, (0.4, 3.6), (5.4, 3.6)); neuro.wire(axc, (0.4, 0.6), (5.4, 0.6))
neuro.wire(axc, (1.2, 3.6), (1.2, 2.55)); neuro.capacitor(axc, (1.2, 2.55), (1.2, 1.65), text="$C$", text_side=-1)
neuro.wire(axc, (1.2, 1.65), (1.2, 0.6))
neuro.wire(axc, (3.0, 3.6), (3.0, 3.1)); neuro.resistor(axc, (3.0, 3.1), (3.0, 2.2), variable=False, text="$1/g_\\mathrm{L}$", text_side=1)
neuro.wire(axc, (3.0, 2.2), (3.0, 1.8)); neuro.battery(axc, (3.0, 1.8), (3.0, 1.2), text="$E_\\mathrm{L}$", text_side=1)
neuro.wire(axc, (3.0, 1.2), (3.0, 0.6))
neuro.current_source(axc, (4.8, 2.6), (4.8, 1.5), text="$I$", text_side=1)
neuro.wire(axc, (4.8, 3.6), (4.8, 2.6)); neuro.wire(axc, (4.8, 1.5), (4.8, 0.6))
for x in (1.2, 3.0, 4.8):
    neuro.node(axc, (x, 3.6)); neuro.node(axc, (x, 0.6))
axc.text(0.2, 3.9, "inside", fontsize=FT["tiny"], color=P.ink()); axc.text(0.2, 0.2, "outside", fontsize=FT["tiny"], color=P.ink())
axc.set_title("A  Equivalent circuit", fontsize=FT["small"], color=P.ink(), loc="left", weight="bold", pad=0)

c_m, R_m, a = 1.0, 5000.0, 20e-4  # uF/cm2, Ohm cm2, cm
A = 4 * np.pi * a**2
Rin = R_m / A / 1e6  # MOhm
C = c_m * A * 1e6  # pF
tau = R_m * c_m * 1e-3  # ms
I = 0.1  # nA
t = np.linspace(-5, 40, 900)
ax = fig.add_axes([0.42, 0.58, 0.55, 0.34])
on = t >= 0
for gf, tok, lab in [(1, "neuron", "rest"), (2, "negative", "$g_\\mathrm{L}$ doubled")]:
    V = np.where(on, I * Rin / gf * (1 - np.exp(-t / (tau / gf))), 0)
    ax.plot(t, V, color=charts.line(tok), lw=1.8, label=lab)
    ax.plot([tau / gf], [I * Rin / gf * (1 - np.exp(-1))], "o", ms=4, color=charts.line(tok))
ax.axhline(I * Rin, color=P.muted(), lw=0.6, ls=":")
ax.text(40, I * Rin * 1.02, "$R_\\mathrm{in} I$", ha="right", va="bottom", fontsize=FT["tiny"], color=P.muted())
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(ax, "t / ms", "$V - E_\\mathrm{L}$ / mV")
charts.title(ax, f"B  Step response: $R_\\mathrm{{in}}$ = {Rin:.0f} MΩ, $\\tau_\\mathrm{{m}}$ = {tau:.0f} ms, C = {C:.0f} pF")

ax = fig.add_axes([0.08, 0.10, 0.38, 0.30])
f = np.logspace(-0.5, 3.3, 300)
for gf, tok in [(1, "neuron"), (2, "negative")]:
    Z = Rin / gf / np.sqrt(1 + (2 * np.pi * f * tau / gf * 1e-3) ** 2)
    ax.loglog(f, Z, color=charts.line(tok), lw=1.8)
fc = 1e3 / (2 * np.pi * tau)
ax.axvline(fc, color=P.muted(), lw=0.7, ls=":")
ax.text(fc * 1.1, 4, f"$f_\\mathrm{{c}}$ = {fc:.0f} Hz", fontsize=FT["tiny"], color=P.muted())
ax.set_ylim(3, 200)
charts.style_axes(ax, "frequency / Hz", "|Z| / MΩ")
charts.title(ax, "C  Low-pass filter")

ax = fig.add_axes([0.58, 0.10, 0.39, 0.30])
r = np.logspace(-2.5, 1.7, 300)
EK, ECl, ENa = -89, -69, 66
V = (1 * EK + 0.2 * ECl + r * ENa) / (1 + 0.2 + r)
ax.semilogx(r, V, color=charts.line("na"), lw=1.8)
for x, lab in [(0.04, "rest"), (20, "AP peak")]:
    ax.plot([x], [(EK + 0.2 * ECl + x * ENa) / (1.2 + x)], "o", ms=4, color=P.ink())
    ax.text(x, (EK + 0.2 * ECl + x * ENa) / (1.2 + x) + (14 if x < 1 else -14), lab, ha="center", fontsize=FT["tiny"], color=P.ink())
ax.axhline(ENa, color=P.muted(), lw=0.6, ls=":"); ax.axhline(EK, color=P.muted(), lw=0.6, ls=":")
ax.text(0.004, ENa - 8, "$E_\\mathrm{Na}$", fontsize=FT["tiny"], color=P.muted())
ax.text(0.004, EK + 3, "$E_\\mathrm{K}$", fontsize=FT["tiny"], color=P.muted())
charts.style_axes(ax, "$g_\\mathrm{Na}/g_\\mathrm{K}$", "$V_\\mathrm{rest}$ / mV")
charts.title(ax, "D  Conductance-weighted potential")
