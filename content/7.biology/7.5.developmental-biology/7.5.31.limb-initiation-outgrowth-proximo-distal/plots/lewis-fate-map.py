"""Lewis's reconstruction of the fate map (Formula 31.8.1) in a model limb bud.

Distance x from the AER; cell density and cross-section constant. Division rate k(x, t) = 0.058 per hour
(12 h cycle) within the zone of AER influence (x < 300 um) and k = 0.02 exp(-t / 48 h) per hour proximally. Five progenitors, one for each segment, start at
300 um x 2^-(j + 0.6) from the AER and are followed forward with Eq. (31.12) for 96 h. A: trajectories (log scale; the band is the
zone of influence). B: the number of cell cycles each boundary cell spends in the zone, k/ln 2 integrated over its
time inside it, against the segment it bounds.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
X, kd = 300.0, np.log(2) / 12.0


def k(x, t):
    return np.where(x < X, kd, 0.02 * np.exp(-t / 48.0))


def velocity(x, t):
    # dx/dt = integral_0^x k(x', t) dx'
    inside = np.minimum(x, X) * kd
    outside = np.maximum(x - X, 0.0) * 0.02 * np.exp(-t / 48.0)
    return inside + outside


T, dt = 96.0, 0.01
times = np.arange(0, T + dt, dt)
# start positions chosen so that the trajectories leave the zone in sequence
x0 = X * 2.0 ** (-np.array([0.6, 1.6, 2.6, 3.6, 4.6]))
traj = np.zeros((len(times), len(x0)))
x = x0.copy()
cycles = np.zeros(len(x0))
for i, t in enumerate(times):
    traj[i] = x
    cycles += np.where(x < X, kd, 0) * dt / np.log(2)
    x = x + velocity(x, t) * dt

fig, ax = bio.canvas(24.0, 9.5)
pa = C.axes_at(ax, (1.8, 1.5, 8.6, 6.6))
pa.axhspan(1, X, color=P.mix(P.fill("highlight"), P.surface(), 0.6 if P.is_dark() else 0.55), lw=0)
names = ["stylopod", "zeugopod", "wrist", "metacarpals", "phalanges"]
toks = ["humerus", "radius", "carpals", "metacarpals", "phalanges"]
for j in range(len(x0)):
    pa.plot(times, traj[:, j], color=Q.line_color(toks[j]), lw=1.7, label=names[j])
pa.set_yscale("log")
pa.set_ylim(5, 4000)
pa.set_xlim(0, T)
pa.set_xticks([0, 24, 48, 72, 96])
C.style_axes(pa, "t / h", "distance from AER / µm")
pa.text(60, 150, "zone of AER\ninfluence (< 300 µm)", fontsize=bio.core.FONT["tiny"], color=P.muted(), va="center")
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "A", (0.3, 9.3))
bio.label(ax, (1.8, 9.1), "Progenitor trajectories", size="small", bold=True, ha="left", va="top")

pb = C.axes_at(ax, (14.0, 1.5, 8.6, 6.6))
pb.bar(np.arange(5), cycles, color=[Q.line_color(t) for t in toks], width=0.6)
for i, c in enumerate(cycles):
    pb.text(i, c + 0.08, f"{c:.2f}", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
pb.set_xticks(np.arange(5))
pb.set_xticklabels(names, rotation=20)
pb.set_ylim(0, 5.5)
C.style_axes(pb, None, "cell cycles spent in the zone")
bio.panel(ax, "B", (12.5, 9.3))
bio.label(ax, (14.0, 9.1), "One more division per segment", size="small", bold=True, ha="left", va="top")
