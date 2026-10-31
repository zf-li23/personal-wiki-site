# A kinetic model of the torque-speed curve of the bacterial flagellar motor (Formula 28.4.1). Each of N = 8
# stators advances the rotor by delta = 2 pi/26 per cycle of two transitions: a load-independent proton
# transfer (rate scale k_c) that releases (1 - s) of the free energy dmu = 2 e dp (two protons, dp = 150 mV,
# dmu = 48 pN nm), and a power stroke (rate scale k_m = 1e5 /s) that releases s dmu - tau delta / N against the
# share of the load torque tau carried by one stator (s = 0.85); rates split the free-energy change
# symmetrically between forward and backward directions, so that detailed balance holds for each transition.
# A: torque against speed for k_c = 3000 /s, with load lines of beads (rotational drag 8 pi eta r^3 plus a hook
# term); the motor runs where the line meets the curve. B: the same motor with proton transfer slowed 1.6-fold
# (as by D2O or cooling): the high-load plateau, set by thermodynamics, is unchanged; the knee and the zero-load
# speed, set by kinetics, move. C: torque for 1 to 8 stators: the stall torque scales with N, the zero-load
# speed does not.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts

P = bio.P
kT, dl, dmu, s, km = 4.1, 2 * np.pi / 26, 48.0, 0.85, 1e5


def omega(tau, kc, N=8):
    ts = tau / N
    u1, w0 = km * np.exp((s * dmu - ts * dl) / (2 * kT)), km * np.exp(-(s * dmu - ts * dl) / (2 * kT))
    u0, w1 = kc * np.exp((1 - s) * dmu / (2 * kT)), kc * np.exp(-(1 - s) * dmu / (2 * kT))
    return dl * (u0 * u1 - w0 * w1) / (u0 + u1 + w0 + w1) / (2 * np.pi)  # Hz


taus = np.linspace(0, 8 * dmu / dl, 400)
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0))
ax = axs[0]
f = omega(taus, 3000)
ax.plot(f, taus, color=charts.line("bacterium"), lw=2.0)
eta = 1e-3
for r, lab in ((0.5e-6, "1 µm bead"), (0.25e-6, "0.5 µm"), (0.15e-6, "0.3 µm"), (30e-9, "60 nm gold")):
    zeta = (8 * np.pi * eta * r**3 + 2e-22) * 1e21  # pN nm s
    ff = np.linspace(0, 330, 50)
    ax.plot(ff, zeta * 2 * np.pi * ff, color=P.muted(), lw=0.8, ls="--")
    fx = brentq(lambda x: omega(zeta * 2 * np.pi * x, 3000) - x, 0, 330)
    ax.plot(fx, zeta * 2 * np.pi * fx, "o", color=charts.line("negative"), ms=4)
    ax.text(fx + 5, zeta * 2 * np.pi * fx + 40, lab, fontsize=7.5, color=P.ink())
ax.set_xlim(0, 330); ax.set_ylim(0, 1800)
charts.style_axes(ax, "speed / Hz", "torque / pN nm")
charts.title(ax, "A   Plateau, knee, steep fall")

ax = axs[1]
for kc, tok, lab in ((3000, "bacterium", "H$_2$O, $k_\\mathrm{c}$ = 3000 s$^{-1}$"), (3000 / 1.6, "dna", "proton transfer 1.6× slower")):
    ax.plot(omega(taus, kc), taus, color=charts.line(tok), lw=2.0, label=lab)
ax.set_xlim(0, 330); ax.set_ylim(0, 1800)
ax.legend(fontsize=7.5, frameon=False, loc="lower left")
charts.style_axes(ax, "speed / Hz", "torque / pN nm")
charts.title(ax, "B   Kinetics moves only the knee")

ax = axs[2]
for N, tok in ((1, "neutral"), (2, "dna"), (4, "enzyme"), (8, "bacterium")):
    tt = np.linspace(0, N * dmu / dl, 300)
    ax.plot(omega(tt, 3000, N), tt, color=charts.line(tok), lw=1.8, label=f"N = {N}")
ax.set_xlim(0, 330); ax.set_ylim(0, 1800)
ax.legend(fontsize=7.5, frameon=False, loc="upper right", title="stators", title_fontsize=7.5)
charts.style_axes(ax, "speed / Hz", "torque / pN nm")
charts.title(ax, "C   Stators add torque, not speed")
fig.tight_layout()
