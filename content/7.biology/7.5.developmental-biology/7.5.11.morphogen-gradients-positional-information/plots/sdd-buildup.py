"""Building a synthesis-diffusion-degradation gradient.

A morphogen enters at x = 0 with constant flux j from time 0, diffuses (D) and is degraded at rate k; the
domain is long enough (8 decay lengths) to act as semi-infinite. Units: decay length lambda = sqrt(D / k) = 1,
lifetime 1 / k = 1. A: profiles at successive times approach C_inf = (j lambda / D) exp(-x / lambda) from the
source outward. B: the local accumulation time tau(x) = int_0^inf [1 - C(x, t) / C_inf(x)] dt computed from the
simulation (points) agrees with the exact result tau(x) = (1 + x / lambda) / (2 k) (line): the gradient is
established first near the source, and a cell 3 decay lengths away waits four times as long as one at the source.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
Lx, n = 8.0, 401
x = np.linspace(0, Lx, n)
dx = x[1] - x[0]
D, k, j = 1.0, 1.0, 1.0
dt = 0.002
# Crank-Nicolson with flux boundary at 0 and no flux at Lx (ghost-node form)
main = np.full(n, -2.0)
off = np.ones(n - 1)
A = np.diag(main) + np.diag(off, 1) + np.diag(off, -1)
A[0, 1] = 2.0
A[-1, -2] = 2.0
A = D * A / dx**2 - k * np.eye(n)
b = np.zeros(n)
b[0] = 2 * j / dx
I = np.eye(n)
M1 = np.linalg.inv(I - 0.5 * dt * A)
M2 = I + 0.5 * dt * A
Cinf = j / np.sqrt(D * k) * np.exp(-x / np.sqrt(D / k))
c = np.zeros(n)
snap_t = [0.1, 0.3, 1.0, 3.0]
snaps = {}
tau = np.zeros(n)
t = 0.0
Tend = 12.0
while t < Tend - 1e-9:
    tau += dt * (1 - c / Cinf)
    c = M1 @ (M2 @ c + dt * b)
    t += dt
    for s in snap_t:
        if abs(t - s) < dt / 2:
            snaps[s] = c.copy()

fig, ax = bio.canvas(22.0, 9.0)
pa = C.axes_at(ax, (1.6, 1.4, 8.6, 6.4))
pa.plot(x, Cinf, color=P.ink(), lw=2.0, label="steady state")
toks = ["highlight", "na", "protein", "negative"]
for s, tk in zip(snap_t, toks):
    pa.plot(x, snaps[s], color=Q.line_color(tk), lw=1.5, ls=(0, (4, 2)), label=f"t = {s:g} / k")
pa.set_xlim(0, 5)
pa.set_ylim(0, 1.05)
C.style_axes(pa, "x / λ", "C / (jλ/D)")
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
bio.panel(ax, "A", (0.3, 8.6))
bio.label(ax, (1.6, 8.6), "Gradient formation after the source is switched on", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (13.0, 1.4, 8.0, 6.4))
xs = np.linspace(0, 5, 200)
pb.plot(xs, (1 + xs) / 2, color=P.ink(), lw=1.8, label="(1 + x/λ) / 2k")
sel = slice(0, int(5 / dx) + 1, 25)
pb.plot(x[sel], tau[sel], "o", ms=4.5, color=Q.line_color("protein"), label="simulation")
pb.set_xlim(0, 5)
pb.set_ylim(0, 3.2)
C.style_axes(pb, "x / λ", "accumulation time τ · k")
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (11.8, 8.6))
bio.label(ax, (13.0, 8.6), "Local accumulation time", size="small", bold=True, ha="left")
