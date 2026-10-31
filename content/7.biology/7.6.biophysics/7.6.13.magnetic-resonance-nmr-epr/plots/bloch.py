# Numerical solution of the Bloch equations in the frame rotating at the radiofrequency.
# Sign convention: dM/dt = gamma M x B with gamma > 0, so a field along x' turns M from z towards +y'.
# A: trajectory of the magnetization M/M0 during a 90 degree x pulse (on resonance: nutation from z to +y in
#    the y-z plane; off resonance by Omega = 0.5 omega1: the effective field is tilted and the vector misses
#    the transverse plane), then free precession at an offset with T2 = 3 and T1 = 6 (a spiral back to z).
# B: components of M after an ideal 90 degree pulse, free evolution at Omega/2pi = 5 Hz with T2 = 0.1 s and
#    T1 = 0.3 s: the transverse components oscillate and decay with T2, Mz recovers with T1.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P


def bloch(t, m, w1, om, r1, r2):
    """dM/dt in the rotating frame: B_eff = (w1, 0, om)/gamma, relaxation towards (0, 0, 1)."""
    mx, my, mz = m
    # dM/dt = M x w_eff with w_eff = gamma B_eff = (w1, 0, om)
    dx = my * om - mz * 0.0
    dy = mz * w1 - mx * om
    dz = -my * w1
    return [dx - r2 * mx, dy - r2 * my, dz - r1 * (mz - 1.0)]


fig = plt.figure(figsize=(11.5, 4.6))
ax = fig.add_subplot(1, 2, 1, projection="3d")
w1 = 2 * np.pi * 1.0          # nutation frequency (arbitrary units, pulse length 0.25)
tp = 0.25
cases = ((0.0, "protein", "on resonance"), (0.5 * w1, "rna", "off resonance, Ω = 0.5 ω₁"))
for om, tok, name in cases:
    s = solve_ivp(bloch, (0, tp), [0, 0, 1], args=(w1, om, 0, 0), max_step=1e-3)
    col = charts.line(tok)
    ax.plot(s.y[0], s.y[1], s.y[2], color=col, lw=2.0, label=name + ", pulse")
    ax.quiver(0, 0, 0, *s.y[:, -1], color=col, lw=1.4, arrow_length_ratio=0.12)
# free evolution after the on-resonance pulse, at an offset of 0.5 cycles per unit time, T2 = 3, T1 = 6
f = solve_ivp(bloch, (0, 14), [0, 1, 0], args=(0.0, 2 * np.pi * 0.5, 1 / 6, 1 / 3), max_step=2e-3)
ax.plot(f.y[0], f.y[1], f.y[2], color=charts.line("protein"), lw=0.9, ls=(0, (3, 1.5)),
        label="then free precession with relaxation")
# axes of the rotating frame
for v, lab in (((1.25, 0, 0), "x′ (B₁)"), ((0, 1.3, 0), "y′"), ((0, 0, 1.25), "z (B₀)")):
    ax.plot([0, v[0]], [0, v[1]], [0, v[2]], color=P.muted(), lw=0.8)
    ax.text(*[1.08 * c for c in v], lab, color=P.ink(), fontsize=8)
u = np.linspace(0, 2 * np.pi, 100)
ax.plot(np.cos(u), np.sin(u), 0 * u, color=P.muted(), lw=0.5, ls=":")
ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-0.2, 1.1)
ax.set_box_aspect((1, 1, 0.65))
ax.view_init(elev=22, azim=-125)
ax.set_axis_off()
ax.legend(fontsize=7.2, frameon=False, loc="upper left", bbox_to_anchor=(0.0, 1.02))
charts.title(ax, "A   Rotating frame: a 90° pulse about x′")

ax = fig.add_subplot(1, 2, 2)
t = np.linspace(0, 0.8, 2000)
om, T2, T1 = 2 * np.pi * 5.0, 0.1, 0.3
mx = np.sin(om * t) * np.exp(-t / T2)        # start at +y after the x pulse: M = (0, 1, 0)
my = np.cos(om * t) * np.exp(-t / T2)
mz = 1 - np.exp(-t / T1)
ax.plot(t, mx, color=charts.line("protein"), lw=1.4, label="Mx")
ax.plot(t, my, color=charts.line("rna"), lw=1.4, label="My")
ax.plot(t, mz, color=charts.line("enzyme"), lw=2.0, label="Mz")
ax.plot(t, np.exp(-t / T2), color=P.muted(), lw=0.9, ls="--", label="exp(−t/T₂)")
ax.plot(t, -np.exp(-t / T2), color=P.muted(), lw=0.9, ls="--")
ax.axhline(0, color=P.muted(), lw=0.5)
ax.axhline(1 - np.exp(-1), color=P.muted(), lw=0.6, ls=":")
ax.text(0.40, 0.53, "Mz = (1 − 1/e) M₀ at t = T₁", fontsize=7.5, color=P.muted())
ax.set_xlim(0, 0.8); ax.set_ylim(-1.05, 1.1)
ax.legend(fontsize=7.5, frameon=False, loc="lower right", ncol=2)
charts.style_axes(ax, "t / s", "M / M₀")
charts.title(ax, "B   Free evolution: T₂ = 0.1 s, T₁ = 0.3 s")
fig.tight_layout()
