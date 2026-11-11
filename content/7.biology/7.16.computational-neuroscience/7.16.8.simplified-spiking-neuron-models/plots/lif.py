"""Integrate-and-fire models. LIF: tau_m dV/dt = -(V - E_L) + R I, spike and reset when V reaches V_th,
with E_L = V_reset = -65 mV, V_th = -50 mV, tau_m = 10 ms, R = 10 MOhm (rheobase I_th = 1.5 nA).
A: voltage of the LIF neuron for a 2 nA step (spikes drawn as vertical lines; tau_ref = 2 ms).
B: f-I curve: analytic rate r = 1/(tau_ref + tau_m ln(RI/(RI - (V_th - E_L)))) (lines) and simulation
(dots, Euler, dt = 0.05 ms) for tau_ref = 0 and 5 ms. C: the right-hand side F(V) of tau_m dV/dt = F(V)
at I = 0 for the LIF (linear), the exponential integrate-and-fire model (ExpIF, F = -(V - E_L) +
Delta_T exp((V - V_T)/Delta_T), V_T = -55 mV, Delta_T = 2 mV) and the quadratic model (QIF, F =
(V - E_L)(V - V_c)/(V_c - E_L) with V_c = -52 mV, scaled to the same rest and threshold): in the ExpIF and
QIF the threshold is an unstable equilibrium, not a fixed voltage. D: ExpIF voltage for a 1.8 nA step with
Delta_T = 0.5, 2 and 5 mV (V_T = -55 mV, spike cut at 0 mV and reset to -65 mV): first spike after the step; a smaller Delta_T makes the
spike onset sharper and the model closer to the LIF."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
EL, Vth, Vr, tau, R = -65.0, -50.0, -65.0, 10.0, 10.0


def lif(I, T, dt=0.05, tref=2.0):
    """Euler integration; I may be an array (several runs at once). Returns t, V (with spikes marked)."""
    I = np.atleast_1d(np.asarray(I, float))
    t = np.arange(0, T, dt)
    V = np.full(I.shape, EL); last = np.full(I.shape, -1e9)
    Vt = np.empty((len(t),) + I.shape); count = np.zeros(I.shape)
    for k, tt in enumerate(t):
        active = tt - last >= tref
        V = np.where(active, V + dt / tau * (-(V - EL) + R * I), V)
        spk = V >= Vth
        count += spk
        Vt[k] = np.where(spk, 20.0, V)
        V = np.where(spk, Vr, V); last = np.where(spk, tt, last)
    return t, Vt, count


fig, axs = plt.subplots(2, 2, figsize=(10.0, 5.8))
fig.subplots_adjust(wspace=0.28, hspace=0.5, left=0.07, right=0.99, bottom=0.09, top=0.93)

ax = axs[0, 0]
t, Vt, _ = lif(np.array([2.0]), 100)
Iseries = np.where(t >= 10, 2.0, 0.0)
_, Vt, _ = lif(np.array([0.0]), 10)
t1, V1, _ = lif(np.array([2.0]), 90)
tt = np.concatenate([np.arange(0, 10, 0.05), 10 + t1]); VV = np.concatenate([np.full(200, EL), V1[:, 0]])
ax.plot(tt, VV, color=charts.line("blood"), lw=1.2)
ax.axhline(Vth, color=P.muted(), lw=0.7, ls=":"); ax.text(101, Vth, "$V_\\mathrm{th}$", fontsize=FT["tiny"], color=P.muted(), va="center")
ax.axhline(Vr, color=P.muted(), lw=0.7, ls=":"); ax.text(101, Vr, "$V_\\mathrm{reset}$", fontsize=FT["tiny"], color=P.muted(), va="center")
ax.set_xlim(0, 108)
charts.style_axes(ax, "t / ms", "$V$ / mV")
charts.title(ax, "A  LIF neuron, 2 nA step")

ax = axs[0, 1]
Ig = np.linspace(0, 6, 400)
Is = np.linspace(0.25, 6, 24)
for tref, tok in [(0.0, "dna"), (5.0, "neuron")]:
    with np.errstate(divide="ignore", invalid="ignore"):
        T = tref + tau * np.log(R * Ig / (R * Ig - (Vth - EL)))
        r = np.where(R * Ig > Vth - EL, 1000 / T, 0.0)
    ax.plot(Ig, r, color=charts.line(tok), lw=1.5, label=f"$\\tau_\\mathrm{{ref}} = {tref:g}$ ms")
    _, _, cnt = lif(Is, 1000.0, dt=0.05, tref=tref)
    ax.plot(Is, cnt, "o", ms=3, color=charts.line(tok))
ax.axvline(1.5, color=P.muted(), lw=0.7, ls=":"); ax.text(1.55, 300, "rheobase", fontsize=FT["tiny"], color=P.muted())
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "$I$ / nA", "firing rate / Hz")
charts.title(ax, "B  f-I curve: theory (lines) and simulation (dots)")

ax = axs[1, 0]
V = np.linspace(-75, -45, 300)
VT, DT, Vc = -55.0, 2.0, -52.0
ax.plot(V, -(V - EL), color=charts.line("neutral"), lw=1.5, label="LIF")
ax.plot(V, -(V - EL) + DT * np.exp((V - VT) / DT), color=charts.line("blood"), lw=1.5, label="ExpIF")
ax.plot(V, (V - EL) * (V - Vc) / (Vc - EL), color=charts.line("dna"), lw=1.5, label="QIF")
ax.axhline(0, color=P.muted(), lw=0.7)
ax.set_ylim(-12, 12)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "$V$ / mV", "$F(V)$ / mV")
charts.title(ax, "C  Right-hand side $F(V)$ at $I = 0$")

ax = axs[1, 1]
dt = 0.02
t = np.arange(0, 45, dt)
for DTk, tok in [(0.5, "neutral"), (2.0, "blood"), (5.0, "dna")]:
    Vk = EL; out = np.empty(len(t))
    for k, tt in enumerate(t):
        I = 1.8 if tt >= 10 else 0.0
        Vk = Vk + dt / tau * (-(Vk - EL) + DTk * np.exp(min((Vk - VT) / DTk, 50)) + R * I)
        if Vk >= 0:
            out[k] = 20.0; Vk = Vr
        else:
            out[k] = Vk
    ax.plot(t, out, color=charts.line(tok), lw=1.1, label=f"$\\Delta_T = {DTk:g}$ mV")
ax.set_ylim(-70, 45); ax.set_xlim(5, 45)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left", ncol=3)
charts.style_axes(ax, "t / ms", "$V$ / mV")
charts.title(ax, "D  ExpIF: sharpness of spike initiation")
