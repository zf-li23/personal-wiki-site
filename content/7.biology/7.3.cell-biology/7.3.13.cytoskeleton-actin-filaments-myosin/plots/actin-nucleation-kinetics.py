"""Nucleation-elongation kinetics of actin polymerization (the pyrene-actin assay).

Model: nuclei (trimers) form at rate k_n c^3, where c is the free monomer concentration; each filament
grows at both ends with net rate k_on c - k_off (ATP-actin, sum of barbed and pointed ends: k_on = 12.9
per uM per s, k_off = 2.2 per s, Pollard 1986), so that
    dF/dt = k_n c^3,   dM/dt = (k_on c - k_off) F,   c = c_tot - M,
with k_n = 3e-8 per uM^2 per s (chosen to give lags of minutes, as observed).
A: polymer (normalized, as pyrene fluorescence) for three total concentrations without seeds, and for
4 uM with preformed seeds (2 nM filaments), which abolish the lag. The plateau leaves c = C_c free.
B: the half-time of polymerization against c_tot on log-log axes; at early times M ~ t^2 c^4, so the slope
is -3/2 for a trimer nucleus (in general -n/2 for a nucleus of n subunits).
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
kon, koff, kn = 12.9, 2.2, 3e-8
Cc = koff / kon


def run(ctot, F0=0.0, T=1500.0, dt=0.05):
    n = int(T / dt)
    F, M = F0, 0.0
    t = np.arange(n) * dt
    Ms = np.empty(n)
    for i in range(n):
        c = ctot - M
        dF = kn * c**3
        dM = (kon * c - koff) * F
        F += dF * dt
        M = min(M + dM * dt, ctot - Cc * 0.999) if dM > 0 else M + dM * dt
        Ms[i] = M
    return t, Ms


fig, ax = bio.canvas(22.0, 8.0)
bio.panel(ax, "A", (0.1, 7.8))
pa = charts.axes_at(ax, (1.8, 1.3, 8.4, 5.8))
cols = ["drug", "actin", "protein"]
for c0, tk in zip((2.0, 4.0, 8.0), cols):
    t, M = run(c0)
    pa.plot(t / 60, M / (c0 - Cc), color=quant.line_color(tk), lw=1.8, label=f"{c0:g} µM, unseeded")
t, M = run(4.0, F0=0.002)
pa.plot(t / 60, M / (4.0 - Cc), color=quant.line_color("positive"), lw=1.8, ls=(0, (4, 2)), label="4 µM + seeds")
pa.set_xlim(0, 25)
pa.set_ylim(0, 1.08)
pa.text(14, 0.25, "lag phase\n(nucleation)", fontsize=bio.core.FONT["tiny"], color=P.muted())
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(pa, "time / min", "polymer (fraction of final)")
charts.title(pa, "Lag, growth, steady state")

bio.panel(ax, "B", (11.6, 7.8))
pb = charts.axes_at(ax, (13.4, 1.3, 7.8, 5.8))
cs = np.array([1.5, 2, 3, 4, 6, 8, 12])
th = []
for c0 in cs:
    t, M = run(c0, T=4000 if c0 < 2.5 else 1500, dt=0.05 if c0 < 6 else 0.02)
    th.append(t[np.searchsorted(M, 0.5 * (c0 - Cc))])
th = np.array(th)
pb.loglog(cs, th, "o", color=quant.line_color("actin"), ms=5)
ref = th[3] * (cs / cs[3]) ** -1.5
pb.loglog(cs, ref, color=quant.line_color("muted"), lw=1.0, ls=(0, (3, 2)))
pb.text(5.2, ref[3] * 1.45, "slope −3/2", fontsize=bio.core.FONT["tiny"], color=P.muted())
from matplotlib.ticker import NullFormatter
pb.set_xticks([1.5, 2, 3, 4, 6, 8, 12])
pb.set_xticklabels(["1.5", "2", "3", "4", "6", "8", "12"])
pb.xaxis.set_minor_formatter(NullFormatter())
pb.set_yticks([50, 100, 200, 500, 1000])
pb.set_yticklabels(["50", "100", "200", "500", "1000"])
pb.yaxis.set_minor_formatter(NullFormatter())
charts.style_axes(pb, "total actin / µM", "half-time / s")
charts.title(pb, "Half-time reveals the nucleus size")
