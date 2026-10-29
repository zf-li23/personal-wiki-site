"""An adhesion-site membrane pulled along a substrate: relaxation to steady sliding.

Linearized site model (text, 8.2.1): tension T = -k (n - n0), friction per site proportional to its
velocity, so that n u = -K dn/ds with K = k / (n_s f); sites are conserved, dn/dt + d(n u)/ds = 0,
which gives the heat equation dn/dt = K d2n/ds2 on a segment whose ends move (a Stefan-type problem).
At t = 0 a segment of length L0 with uniform site density n0 has the tension corresponding to
n1 = n0/2 applied at its right end; the left end stays at n0 (zero tension). Units: L0 = K = n0 = 1.
The problem is solved in the Lagrangian site coordinate m (number of sites to the left), in which
the ends are fixed: dn/dt = K n^2 d2n/dm2, u = -K dn/dm, by explicit finite differences.
A: site density n(s) at t = 0.02, 0.1, 0.3, 1 and 4 (in units of L0^2/K), plotted against position.
B: segment length L(t) and the velocity of the trailing end, approaching the steady sliding solution
L = L0 ln(n0/n1)/(1 - n1/n0) = 1.386 L0 and U = (K/L0)(1 - n1/n0) = 0.5 K/L0 (dashed).
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
M, n0, n1, K = 100, 1.0, 0.5, 1.0
m = np.linspace(0, n0 * 1.0, M + 1)
dm = m[1] - m[0]
n = np.full(M + 1, n0)
n[-1] = n1
dt = 0.2 * dm * dm / K
s0 = 0.0
snap_t = [0.02, 0.1, 0.3, 1.0, 4.0]
snaps, hist = {}, []
t, si = 0.0, 0
tmax = 4.0
nsteps = int(tmax / dt) + 1
for it in range(nsteps):
    u0 = -K * (-3 * n[0] + 4 * n[1] - n[2]) / (2 * dm)
    if it % 20 == 0:
        L = np.trapezoid(1 / n, m)
        hist.append((t, L, u0))
    if si < len(snap_t) and t >= snap_t[si]:
        s = s0 + np.r_[0, np.cumsum(0.5 * (1 / n[1:] + 1 / n[:-1]) * dm)]
        snaps[snap_t[si]] = (s, n.copy())
        si += 1
    lap = (n[2:] - 2 * n[1:-1] + n[:-2]) / dm ** 2
    n[1:-1] += dt * K * n[1:-1] ** 2 * lap
    s0 += dt * u0
    t += dt
s = s0 + np.r_[0, np.cumsum(0.5 * (1 / n[1:] + 1 / n[:-1]) * dm)]
snaps[4.0] = (s, n.copy())
hist = np.array(hist)

fig, ax = bio.canvas(30.0, 10.0)
bio.panel(ax, "A", (0.1, 9.9))
pa = charts.axes_at(ax, (2.0, 1.8, 11.5, 7.0))
toks = ["ectoderm", "positive", "highlight", "drug", "mesoderm"]
for (tt, (s, nn)), tok in zip(sorted(snaps.items()), toks):
    pa.plot(s, nn, color=quant.line_color(tok), lw=2.0, label=f"t = {tt:g}")
pa.plot([0, 1], [1, 1], color=P.muted(), lw=1.0, ls=(0, (3, 2)), label="t = 0")
pa.set_xlim(-0.05, 3.5)
pa.set_ylim(0.4, 1.05)
charts.style_axes(pa, "position s / L0", "site density n / n0")
leg = pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], loc="lower right")
for tx in leg.get_texts():
    tx.set_color(P.ink())
charts.title(pa, "The segment stretches and slides")

bio.panel(ax, "B", (16.0, 9.9))
pb = charts.axes_at(ax, (18.0, 1.8, 11.0, 7.0))
pb.plot(hist[:, 0], hist[:, 1], color=quant.line_color("mesoderm"), lw=2.0, label="length L / L0")
pb.plot(hist[:, 0], hist[:, 2], color=quant.line_color("ectoderm"), lw=2.0, label="trailing-end speed / (K/L0)")
pb.axhline(np.log(2) / 0.5, color=quant.line_color("mesoderm"), lw=0.9, ls=(0, (3, 2)))
pb.axhline(0.5, color=quant.line_color("ectoderm"), lw=0.9, ls=(0, (3, 2)))
pb.set_xscale("log")
pb.set_xlim(1e-3, 4)
pb.set_ylim(0, 1.6)
charts.style_axes(pb, "time t K / L0²", "")
leg = pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], loc="center left")
for tx in leg.get_texts():
    tx.set_color(P.ink())
charts.title(pb, "Relaxation time ~ L0²/K")
