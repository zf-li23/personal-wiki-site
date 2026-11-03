"""Density-dependent selection between two clones.

dN_i/dt = r_i N_i (1 - (N_A + N_B) / K_i); A: r = 1, K = 100; B: r = 0.5, K = 150; N(0) = 1 each.
Integrated with fourth-order Runge-Kutta.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio.quant import odeint_rk4

P = bio.P
FS = bio.core.FONT
r = np.array([1.0, 0.5])
K = np.array([100.0, 150.0])
t = np.linspace(0, 120, 2401)
N = odeint_rk4(lambda _, y: r * y * (1 - y.sum() / K), np.array([1.0, 1.0]), t)
fig, ax = bio.canvas(30.0, 10.0)
pa = C.axes_at(ax, (2.2, 1.6, 11.5, 6.8))
pa.plot(t, N[:, 0], color=C.line("dna"), lw=1.9, label="clone A (r = 1, K = 100)")
pa.plot(t, N[:, 1], color=C.line("rna"), lw=1.9, label="clone B (r = 0.5, K = 150)")
pa.plot(t, N.sum(1), color=P.muted(), lw=1.2, ls=(0, (4, 2)), label="total")
pa.set_xlim(0, 120)
pa.set_ylim(0, 160)
C.style_axes(pa, "time", "number of individuals")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
bio.panel(ax, "A", (0.2, 9.8))
bio.label(ax, (2.2, 9.4), "Fast growth first, persistence under crowding later", size="small", bold=True, ha="left")
pb = C.axes_at(ax, (17.5, 1.6, 11.0, 6.8))
pb.plot(t, N[:, 1] / N.sum(1), color=C.line("rna"), lw=1.9)
pb.set_xlim(0, 120)
pb.set_ylim(0, 1.02)
C.style_axes(pb, "time", "frequency of clone B")
bio.panel(ax, "B", (15.7, 9.8))
bio.label(ax, (17.5, 9.4), "The K-selected clone wins near carrying capacity", size="small", bold=True, ha="left")
