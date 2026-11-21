"""The Lotka-Volterra predator-prey model, Eq. (25.1): dN/dt = rN - aNP, dP/dt = caNP - mP.

Parameters r = 1, a = 0.1, c = 0.5, m = 0.5, so N* = m/(ca) = 10 and P* = r/a = 10.
A: phase plane. Orbits are level curves of the conserved quantity V (Proposition 25.1.1),
drawn as contours; zero isoclines dashed; arrows show the counterclockwise flow.
B: time series of one orbit (started at N = 25, P = 10) with the cycle averages.
C: period against amplitude (maximum prey density on the orbit); the small-amplitude
limit is 2 pi / sqrt(r m).
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
r, a, c, m = 1.0, 0.1, 0.5, 0.5
Ns, Ps = m / (c * a), r / a
prey, pred = C.line("dna"), C.line("negative")


def rhs(t, z):
    N, Q = z
    return [r * N - a * N * Q, c * a * N * Q - m * Q]


def V(N, Q):
    return c * a * N - m * np.log(N) + a * Q - r * np.log(Q)


fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.3), gridspec_kw=dict(width_ratios=[1.1, 1.3, 1]))

ax = axes[0]
n, q = np.meshgrid(np.linspace(0.3, 60, 500), np.linspace(0.3, 45, 500))
levels = V(np.array([12, 15, 20, 27, 36, 47]), Ps)
ax.contour(n, q, V(n, q), levels=levels, colors=[P.ink()], linewidths=0.9, linestyles="solid")
ax.axhline(Ps, color=prey, ls=(0, (4, 2)), lw=1.1)
ax.axvline(Ns, color=pred, ls=(0, (4, 2)), lw=1.1)
ax.plot(Ns, Ps, "o", color=P.ink(), ms=5)
ax.text(42, Ps + 0.8, "prey isocline P = r/a", color=prey, fontsize=FS["tiny"])
ax.text(Ns + 0.8, 41, "predator isocline N = m/(ca)", color=pred, fontsize=FS["tiny"])
for (x, y) in [(30, 6), (30, 22), (5, 22), (5, 4)]:
    u, v = rhs(0, (x, y))
    s = 3.0 / np.hypot(u / 60, v / 45)
    ax.annotate("", xy=(x + u * s / 60 * 1.6, y + v * s / 45 * 1.2), xytext=(x, y),
                arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=1.0))
ax.set_xlim(0, 60)
ax.set_ylim(0, 45)
C.style_axes(ax, "Prey density N", "Predator density P")
C.title(ax, "A  Closed orbits (level curves of V)")

ax = axes[1]
sol = solve_ivp(rhs, [0, 40], [25, 10], max_step=0.02, rtol=1e-9, atol=1e-9)
ax.plot(sol.t, sol.y[0], color=prey, lw=1.4, label="prey N")
ax.plot(sol.t, sol.y[1], color=pred, lw=1.4, label="predator P")
ax.axhline(Ns, color=P.muted(), lw=0.8, ls=(0, (2, 2)))
ax.text(40.5, Ns + 0.6, "cycle mean of\nN and of P = 10", fontsize=FS["tiny"], color=P.muted(), va="bottom")
ax.set_xlim(0, 52)
ax.legend(fontsize=FS["tiny"], frameon=False, loc="upper right")
C.style_axes(ax, "Time", "Density")
C.title(ax, "B  Predator peaks lag prey peaks")

ax = axes[2]
amps, pers = [], []
for s in np.linspace(1.02, 6.0, 40):
    ev = lambda t, z: z[1] - Ps
    ev.direction = 1.0
    so = solve_ivp(rhs, [0, 200], [Ns * s, Ps], events=ev, rtol=1e-10, atol=1e-10, max_step=0.05)
    te = so.t_events[0]
    pers.append(te[1] - te[0])
    amps.append(so.y[0].max())
ax.plot(amps, pers, color=P.ink(), lw=1.4)
ax.axhline(2 * np.pi / np.sqrt(r * m), color=P.muted(), ls=(0, (3, 2)), lw=0.9)
ax.text(12, 2 * np.pi / np.sqrt(r * m) + 0.15, "2π/√(rm)", fontsize=FS["tiny"], color=P.muted())
C.style_axes(ax, "Maximum prey density on orbit", "Period")
C.title(ax, "C  Period grows with amplitude")
fig.tight_layout()
