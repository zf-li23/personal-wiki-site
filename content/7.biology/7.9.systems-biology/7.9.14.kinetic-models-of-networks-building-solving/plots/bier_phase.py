"""The Bier model of yeast glycolytic oscillations, dG/dt = V_in - k1 G T, dT/dt = 2 k1 G T -
k_p T/(T + K_m), with glucose G and ATP T (V_in = 0.36, k1 = 0.02, k_p = 6; model units).
A: phase plane for K_m = 13 with the two nullclines (dG/dt = 0: G = V_in/(k1 T); dT/dt = 0:
G = k_p/(2 k1 (T + K_m))), the direction field, and a trajectory started next to the fixed point
(dot): the fixed point is an unstable focus and the trajectory winds out onto a stable limit cycle.
B: the same for K_m = 20: a trajectory started far away spirals into the stable focus.
C: bifurcation diagram, the minimum and maximum of G on the attractor against K_m; the oscillation
appears at the supercritical Hopf bifurcation K_m = 15.24, where the trace of the Jacobian vanishes;
below it the dashed line is the unstable fixed point."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
Vin, k1, kp = 0.36, 0.02, 6.0


def f(t, z, Km):
    G, T = z
    return [Vin - k1 * G * T, 2 * k1 * G * T - kp * T / (T + Km)]


def fixed(Km):
    T = 2 * Vin * Km / (kp - 2 * Vin)
    return Vin / (k1 * T), T


Kc = np.sqrt(kp / k1) / (1 + 2 * Vin / (kp - 2 * Vin))
fig, axes = plt.subplots(1, 3, figsize=(11, 3.6))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.17, top=0.86, wspace=0.32)
Tg, Gg = np.meshgrid(np.linspace(0.3, 13, 15), np.linspace(1, 19, 15))
for ax, Km, z0, tend, lab in [(axes[0], 13.0, None, 1500, "A  K_m = 13: limit cycle"),
                              (axes[1], 20.0, [16.0, 0.5], 1200, "B  K_m = 20: stable focus")]:
    Gs, Ts = fixed(Km)
    if z0 is None:
        z0 = [Gs + 0.3, Ts]
    U, V = f(0, [Gg, Tg], Km)
    ux, uy = V / 13, U / 19
    nrm = np.hypot(ux, uy) + 1e-12
    ax.quiver(Tg, Gg, 0.03 * 13 * ux / nrm, 0.03 * 19 * uy / nrm, color=P.muted(), alpha=0.7,
              angles="xy", scale_units="xy", scale=1, width=0.004, headwidth=4, headlength=4, pivot="mid")
    T = np.linspace(0.05, 13, 400)
    ax.plot(T, Vin / (k1 * T), color=charts.line("metabolite"), lw=1.4, label="dG/dt = 0")
    ax.plot(T, kp / (2 * k1 * (T + Km)), color=charts.line("atp"), lw=1.4, label="dT/dt = 0")
    s = solve_ivp(f, (0, tend), z0, args=(Km,), rtol=1e-9, atol=1e-11, max_step=0.5)
    ax.plot(s.y[1], s.y[0], color=P.ink(), lw=0.9)
    ax.plot(Ts, Gs, "o", color=P.ink(), ms=4, mfc="none" if Km < Kc else P.ink())
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 19)
    ax.legend(fontsize=7, frameon=False, loc="upper right")
    charts.style_axes(ax, "ATP, T", "glucose, G")
    charts.title(ax, lab)

ax = axes[2]
Ks = np.linspace(10, 25, 61)
lo, hi = [], []
for Km in Ks:
    Gs, Ts = fixed(Km)
    if Km >= Kc:
        lo.append(Gs); hi.append(Gs)
        continue
    s = solve_ivp(f, (0, 6000), [Gs + 0.3, Ts], args=(Km,), rtol=1e-8, atol=1e-10, method="LSODA",
                  dense_output=True)
    G = s.sol(np.linspace(5000, 6000, 20001))[0]
    lo.append(G.min()); hi.append(G.max())
lo, hi = np.array(lo), np.array(hi)
osc = Ks < Kc
fp = np.array([fixed(k)[0] for k in Ks])
ax.plot(Ks[osc], hi[osc], color=charts.line("metabolite"), lw=1.8, label="max G (limit cycle)")
ax.plot(Ks[osc], lo[osc], color=charts.line("metabolite"), lw=1.8, ls="-.", label="min G (limit cycle)")
ax.plot(Ks[~osc], fp[~osc], color=P.ink(), lw=1.8, label="stable fixed point")
ax.plot(Ks[osc], fp[osc], color=P.ink(), lw=1.0, ls="--", label="unstable fixed point")
ax.axvline(Kc, color=P.muted(), lw=0.8, ls=":")
ax.text(Kc + 0.3, 25, f"Hopf, K_m = {Kc:.2f}", fontsize=7, color=P.ink())
ax.set_ylim(0, 27)
ax.legend(fontsize=7, frameon=False, loc="upper right", bbox_to_anchor=(1.0, 0.9))
charts.style_axes(ax, "K_m", "G on the attractor")
charts.title(ax, "C  Bifurcation diagram")
