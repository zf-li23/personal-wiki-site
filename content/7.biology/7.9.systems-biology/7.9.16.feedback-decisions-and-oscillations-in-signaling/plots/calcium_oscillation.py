"""Ca2+ oscillations from fast activation and slow inactivation of the IP3 receptor: the Li-Rinzel
reduction of the De Young-Keizer model, with its standard parameters (Li and Rinzel, 1994).

c = cytosolic Ca2+ (µM), h = fraction of IP3 receptors not inactivated by Ca2+, p = IP3 (µM); the ER
Ca2+ is (c0 - c)/c1 (closed cell).
dc/dt = c1 v1 m^3 n^3 h^3 (c_ER - c) + c1 v2 (c_ER - c) - v3 c^2/(k3^2 + c^2),  m = p/(p + d1), n = c/(c + d5)
dh/dt = a2 [Q2 (1 - h) - c h],  Q2 = d2 (p + d1)/(p + d3)
c0 = 2, c1 = 0.185, v1 = 6 s^-1, v2 = 0.11 s^-1, v3 = 0.9 uM/s, k3 = 0.1, d1 = 0.13, d2 = 1.049, d3 = 0.9434,
d5 = 0.08234 (µM), a2 = 0.2 uM^-1 s^-1.
A: c and h at p = 0.5 uM. B: the (c, h) phase plane: the c-nullcline (N-shaped: Ca2+-induced Ca2+ release is
the fast positive feedback), the h-nullcline (slow inactivation, the negative feedback) and the limit
cycle. C: period and amplitude of the oscillation against p; oscillations exist between about 0.36 and
0.68 uM, bounded by Hopf bifurcations.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks
import wikibio as bio
from wikibio import charts

P = bio.P
c0, c1, v1, v2, v3, k3 = 2.0, 0.185, 6.0, 0.11, 0.9, 0.1
d1, d2, d3, d5, a2 = 0.13, 1.049, 0.9434, 0.08234, 0.2


def flux(c, h, p):
    minf, ninf, cer = p / (p + d1), c / (c + d5), (c0 - c) / c1
    return c1 * v1 * minf ** 3 * ninf ** 3 * h ** 3 * (cer - c) + c1 * v2 * (cer - c) - v3 * c * c / (k3 * k3 + c * c)


def rhs(t, z, p):
    c, h = z
    Q2 = d2 * (p + d1) / (p + d3)
    return [flux(c, h, p), a2 * (Q2 * (1 - h) - c * h)]


def run(p, T=400.0, tr=200.0):
    s = solve_ivp(rhs, (0, T), [0.1, 0.7], args=(p,), method="LSODA", rtol=1e-8, atol=1e-10, dense_output=True)
    t = np.linspace(tr, T, 20000)
    return t, s.sol(t)


fig, axes = plt.subplots(1, 3, figsize=(11, 3.5))
fig.subplots_adjust(left=0.06, right=0.94, bottom=0.16, top=0.86, wspace=0.42)
t, (c, h) = run(0.5)
ax = axes[0]
ax.plot(t - t[0], c, color=charts.line("ca"), lw=1.8, label="cytosolic Ca2+, c (µM)")
ax.plot(t - t[0], h, color=charts.line("receptor"), lw=1.3, ls="--", label="active receptors, h")
ax.set_xlim(0, 60)
ax.set_ylim(0, 1.1)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "time (s)", "level")
charts.title(ax, "A  Oscillations at IP3 = 0.5 µM")

ax = axes[1]
cc = np.linspace(0.01, 0.8, 400)
hh = np.linspace(0.01, 1.0, 400)
C, Hh = np.meshgrid(cc, hh)
ax.contour(C, Hh, flux(C, Hh, 0.5), levels=[0], colors=[charts.line("ca")], linewidths=1.5)
Q2 = d2 * (0.5 + d1) / (0.5 + d3)
ax.plot(cc, Q2 / (Q2 + cc), color=charts.line("receptor"), lw=1.5)
ax.plot(c, h, color=P.ink(), lw=1.0)
ax.text(0.42, 0.53, "dh/dt = 0", fontsize=7, color=charts.line("receptor"))
ax.text(0.45, 0.66, "dc/dt = 0", fontsize=7, color=charts.line("ca"))
ax.set_xlim(0, 0.6)
ax.set_ylim(0.45, 0.85)
charts.style_axes(ax, "c (µM)", "h")
charts.title(ax, "B  Phase plane and limit cycle")

ax = axes[2]
ps = np.linspace(0.3, 0.75, 19)
per, amp = [], []
for p in ps:
    t, (c, h) = run(p)
    a = c.max() - c.min()
    pk, _ = find_peaks(c, prominence=0.1 * max(a, 1e-12))
    if a > 1e-3 and len(pk) > 2:
        per.append(np.mean(np.diff(t[pk])))
        amp.append(a)
    else:
        per.append(np.nan)
        amp.append(0.0)
ax.plot(ps, per, "o-", color=charts.line("ca"), lw=1.5, ms=3.5, label="period")
ax.set_ylim(0, 16)
charts.style_axes(ax, "IP3, p (µM)", "period (s)")
ax2 = ax.twinx()
ax2.plot(ps, amp, "s--", color=charts.line("receptor"), lw=1.2, ms=3, label="amplitude")
ax2.set_ylim(0, 0.45)
charts.style_axes(ax2, None, "amplitude of c (µM)", box=True)
ax2.spines["left"].set_visible(False)
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, fontsize=7, frameon=False, loc="upper right")
charts.title(ax, "C  The oscillatory window")
