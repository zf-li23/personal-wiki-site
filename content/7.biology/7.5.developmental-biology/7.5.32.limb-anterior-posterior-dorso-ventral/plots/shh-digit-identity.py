"""Digit identity from the time and the concentration of Shh exposure (Section 32.2; a temporal-expansion model
after Harfe et al. 2004).

Antero-posterior coordinate x (0 = posterior margin). Shh is made by cells within x < 0.15 (the ZPA) until t = 1;
growth stretches the tissue uniformly, x = x0 exp(0.9 t), so the cells that start nearest the margin stay longest in
the source. Paracrine Shh outside the source decays as exp(-(x - 0.15) / 0.12). Each cell's exposure is
E = (time spent in the source) + (time integral of the paracrine level outside it). A: trajectories coloured by
the digit assigned (thresholds below), over the paracrine field. B: exposure against final position with the
thresholds for digits 2 to 5; digit 1 forms without Shh.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
g, xs, lam, T = 0.9, 0.15, 0.12, 1.0
dt = 0.002
t = np.arange(0, T + dt, dt)
x0 = np.linspace(0.005, 0.41, 160)
X = x0[None, :] * np.exp(g * t[:, None])
inside = X < xs
para = np.where(inside, 0.0, np.exp(-(X - xs) / lam))
E = inside.sum(0) * dt + para.sum(0) * dt
th = [0.075, 0.2, 0.45, 0.82]   # digit 2, 3, 4, 5 above these
digit = 1 + np.searchsorted(th, E)
TOK = {1: "neutral", 2: "channel", 3: "positive", 4: "highlight", 5: "protein"}

fig, ax = bio.canvas(24.0, 9.6)
pa = C.axes_at(ax, (1.8, 1.4, 8.6, 6.8))
xx = np.linspace(0, X.max(), 200)
tt = np.linspace(0, T, 100)
XX, TT = np.meshgrid(xx, tt)
field = np.where(XX < xs, 1.0, np.exp(-(XX - xs) / lam))
from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list("s", [P.surface(), P.light("protein"), P.fill("protein")])
pa.pcolormesh(XX, TT, field, cmap=cmap, shading="auto", vmin=0, vmax=1.1)
for j in range(0, len(x0), 6):
    pa.plot(X[:, j], t, color=Q.line_color(TOK[digit[j]]), lw=1.2)
pa.axvline(xs, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.text(xs * 0.5, 1.02, "ZPA", fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="center", va="bottom")
pa.set_xlim(0, X.max())
pa.set_ylim(0, T)
C.style_axes(pa, "position x (posterior → anterior)", "time t")
bio.panel(ax, "A", (0.3, 9.4))
bio.label(ax, (1.8, 9.2), "Cell trajectories in the Shh field", size="small", bold=True, ha="left", va="top")

pb = C.axes_at(ax, (14.0, 1.4, 8.6, 6.8))
for d in range(1, 6):
    k = digit == d
    pb.plot(X[-1, k], E[k], "o", ms=3.5, color=Q.line_color(TOK[d]), label=f"digit {d}")
for v in th:
    pb.axhline(v, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pb.set_yscale("log")
pb.set_ylim(1e-3, 2)
C.style_axes(pb, "final position x", "Shh exposure E")
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (12.5, 9.4))
bio.label(ax, (14.0, 9.2), "Exposure sets identity", size="small", bold=True, ha="left", va="top")
