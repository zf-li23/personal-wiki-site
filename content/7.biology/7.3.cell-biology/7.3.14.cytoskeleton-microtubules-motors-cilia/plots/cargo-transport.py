"""Why cells need motors, and why cargoes carry several.

A: time to move a cargo over a distance L by diffusion (t = L^2 / 2D) compared with transport by motors at
1 um/s (t = L / v), for a small protein (D = 10 um^2/s in cytoplasm), a vesicle (D = 0.01 um^2/s, hindered by
the cytoskeleton) and kinesin-driven transport; vertical lines: a fibroblast (20 um), a neuron's dendrite
(500 um) and the sciatic nerve (1 m). Diffusion of a vesicle down a 1 m axon would take thousands of years.
B: mean run length of a cargo carried by N kinesins (Klumpp and Lipowsky 2005): each motor unbinds at rate
eps = 1 per s (single-motor run 1 um at v = 1 um/s) and rebinds at pi = 5 per s while the cargo is attached;
the cargo detaches only when all motors are unbound. Gillespie simulations (points, 2000 runs) against
<x> = (v / (N pi)) [(1 + pi/eps)^N - 1] (line).
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
rng = np.random.default_rng(6)
fig, ax = bio.canvas(22.0, 8.4)

bio.panel(ax, "A", (0.1, 8.3))
pa = charts.axes_at(ax, (1.9, 1.4, 7.8, 6.0))
L = np.logspace(-6, 0, 200)  # m
for D, tk, name in ((10e-12, "metabolite", "protein, diffusion"), (0.01e-12, "vesicle", "vesicle, diffusion")):
    pa.loglog(L * 1e6, L**2 / (2 * D), color=quant.line_color(tk), lw=1.8, label=name)
pa.loglog(L * 1e6, L / 1e-6, color=quant.line_color("enzyme"), lw=1.8, label="motor, 1 µm s⁻¹")
for x, name in ((20, "cell"), (500, "dendrite"), (1e6, "1 m axon")):
    pa.axvline(x, color=quant.line_color("muted"), lw=0.7, ls=(0, (3, 2)))
    pa.text(x * 1.15, 3e-6, name, fontsize=bio.core.FONT["tiny"], color=P.muted(), rotation=90)
for yv, name in ((60, "1 min"), (86400, "1 day"), (3.15e7, "1 year")):
    pa.axhline(yv, color=quant.line_color("muted"), lw=0.5)
    pa.text(1.2, yv * 1.4, name, fontsize=bio.core.FONT["tiny"], color=P.muted())
pa.set_xlim(1, 1e6)
pa.set_ylim(1e-6, 1e14)
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pa, "distance / µm", "time / s")
charts.title(pa, "Diffusion versus transport")

bio.panel(ax, "B", (11.6, 8.3))
pb = charts.axes_at(ax, (13.5, 1.4, 7.6, 6.0))
v, eps, pi = 1.0, 1.0, 5.0
Ns = np.arange(1, 6)
means = []
for N in Ns:
    runs = []
    for _ in range(2000):
        n, t = 1, 0.0
        while n > 0:
            off, on = n * eps, (N - n) * pi
            dt = rng.exponential(1 / (off + on))
            t += dt
            n += -1 if rng.uniform() < off / (off + on) else 1
        runs.append(v * t)
    means.append(np.mean(runs))
NN = np.arange(1, 6)
pb.semilogy(Ns, means, "o", color=quant.line_color("enzyme"), ms=6, label="simulation")
pb.semilogy(NN, v / (NN * pi) * ((1 + pi / eps) ** NN - 1), color=quant.line_color("ink"), lw=1.2, label="Klumpp–Lipowsky")
pb.set_xticks(Ns)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pb, "number of motors N", "mean run length / µm")
charts.title(pb, "Teams of motors")
