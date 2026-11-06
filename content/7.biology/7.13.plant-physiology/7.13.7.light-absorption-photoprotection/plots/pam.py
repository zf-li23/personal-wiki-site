"""Pulse-amplitude-modulated (PAM) chlorophyll fluorescence trace of a dark-adapted leaf, from a kinetic model.

Fluorescence yield F = kF / (kF + kD + kN(t) + kP q(t)), with kF = 1, kD = 4, kP = 24.4 (so that
Fv/Fm = 0.83) and the yield scaled to Fm = 1. q is the fraction of open PSII centres: 1 in the dark,
0 during a 0.8 s saturating pulse; after the actinic light (1000 umol m-2 s-1) is switched on at 60 s it
falls quickly and recovers towards 0.45 as the Calvin cycle is activated (time constant 20 s); after the
light is switched off at 360 s it returns to 1 (5 s). The NPQ rate constant kN builds up with time constant
60 s to 7.5 (NPQ = 1.5) and relaxes in the dark with a fast (60 s, 85 %) and a slow (900 s) component.
A: the trace with the saturating pulses (every 30 s); B: Phi_PSII = (Fm' - Fs)/Fm' and NPQ = (Fm - Fm')/Fm'
computed from the pulses. Illustrative parameters.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
kF, kD, kP = 1.0, 4.0, 24.4
norm = kF + kD                               # scales Fm (dark, no NPQ) to 1
t = np.arange(0, 720, 0.05)
on, off = 60.0, 360.0
pulses = [20.0] + list(np.arange(on + 30, off + 1, 30)) + list(np.arange(off + 30, 720, 45))


def q_of(t):
    if t < on:
        return 1.0
    if t < off:
        return 0.45 - (0.45 - 0.08) * np.exp(-(t - on) / 20.0)
    qoff = 0.45 - (0.45 - 0.08) * np.exp(-(off - on) / 20.0)
    return 1.0 - (1.0 - qoff) * np.exp(-(t - off) / 5.0)


def kn_of(t):
    if t < on:
        return 0.0
    if t < off:
        return 7.5 * (1 - np.exp(-(t - on) / 60.0))
    k0 = 7.5 * (1 - np.exp(-(off - on) / 60.0))
    return k0 * (0.85 * np.exp(-(t - off) / 60.0) + 0.15 * np.exp(-(t - off) / 900.0))


def F(t, pulse):
    q = 0.0 if pulse else q_of(t)
    return norm * kF / (kF + kD + kn_of(t) + kP * q)


inpulse = np.zeros_like(t, bool)
for p in pulses:
    inpulse |= (t >= p) & (t < p + 0.8)
f = np.array([F(x, pp) for x, pp in zip(t, inpulse)])

fig, (a, b) = plt.subplots(1, 2, figsize=(12, 4.2), gridspec_kw={"width_ratios": [1.6, 1]})
a.axvspan(on, off, color=P.mix(P.fill("highlight"), P.surface(), 0.7), lw=0)
a.text((on + off) / 2, 1.04, "actinic light 1000 µmol m$^{-2}$ s$^{-1}$", ha="center", fontsize=8, color=P.muted())
a.plot(t, f, color=P.edge("negative"), lw=1.0)
F0 = F(10, False)
a.annotate("$F_0$", (10, F0), xytext=(2, F0 + 0.12), fontsize=9, color=P.ink())
a.annotate("$F_{\\mathrm{m}}$", (20.4, 1.0), xytext=(28, 0.95), fontsize=9, color=P.ink())
p_late = pulses[[i for i, p in enumerate(pulses) if p < off][-1]]
a.annotate("$F_{\\mathrm{m}}'$", (p_late, F(p_late + 0.4, True)), xytext=(p_late - 55, F(p_late, True) + 0.12),
           fontsize=9, color=P.ink(), arrowprops=dict(arrowstyle="->", color=P.muted()))
a.annotate("$F_{\\mathrm{s}}$", (p_late - 5, F(p_late - 5, False)), xytext=(p_late - 45, F(p_late, False) - 0.12),
           fontsize=9, color=P.ink(), arrowprops=dict(arrowstyle="->", color=P.muted()))
a.annotate("Kautsky peak", (on + 1, F(on + 1, False)), xytext=(on + 25, 0.6), fontsize=8, color=P.ink(),
           arrowprops=dict(arrowstyle="->", color=P.muted()))
a.set_ylim(0, 1.1)
a.set_xlim(0, 720)
a.set_xlabel("Time $t$ / s")
a.set_ylabel("Fluorescence yield (relative to $F_{\\mathrm{m}}$)")
a.set_title("A  Saturating-pulse fluorescence trace", loc="left", fontsize=10)

tp = np.array([p for p in pulses if p > on])
fm1 = np.array([F(p + 0.4, True) for p in tp])
fs = np.array([F(p - 0.1, False) for p in tp])
phi = (fm1 - fs) / fm1
npq = 1.0 / fm1 - 1.0
b.axvspan(on, off, color=P.mix(P.fill("highlight"), P.surface(), 0.7), lw=0)
b.plot(tp, phi, "o-", color=P.edge("plant"), lw=1.5, ms=4, label="$\\Phi_{\\mathrm{PSII}}$")
b2 = b.twinx()
b2.plot(tp, npq, "s-", color=P.edge("dna"), lw=1.5, ms=4, label="NPQ")
b.set_ylim(0, 0.9)
b2.set_ylim(0, 1.8)
b.set_xlabel("Time $t$ / s")
b.set_ylabel("$\\Phi_{\\mathrm{PSII}}$", color=P.edge("plant"))
b2.set_ylabel("NPQ", color=P.edge("dna"))
b.set_title("B  Parameters from the pulses", loc="left", fontsize=10)
h1, l1 = b.get_legend_handles_labels()
h2, l2 = b2.get_legend_handles_labels()
b.legend(h1 + h2, l1 + l2, frameon=False, fontsize=8, loc="center right")
for ax in (a, b):
    ax.grid(True, alpha=0.3)
fig.tight_layout()
