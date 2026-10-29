"""Calcium at fertilization: a travelling wave in the sea urchin egg, oscillations in the mammalian egg.

A, B: calcium-induced calcium release as a bistable reaction-diffusion system across the egg diameter
(L = 80 um, no-flux ends):  dc/dt = D d2c/dx2 + k c (c - a)(1 - c), with c the free Ca2+ scaled from rest (0)
to the released state (1), effective (buffered) diffusion coefficient D = 20 um^2/s, k = 10 /s and threshold
a = 0.25. A local release at the sperm entry point (x = 0) starts a front that crosses the egg at the constant
speed v = sqrt(D k / 2)(1 - 2a) = 5 um/s. A: kymograph (position against time, colour = c); B: profiles every
3 s. Removal of calcium (re-uptake into the endoplasmic reticulum, a slow recovery) is left out.
C: a minimal model of calcium oscillations (Goldbeter, Dupont and Berridge 1990): cytosolic Ca2+ Z and Ca2+ in
the stores Y, with constant influx v0 + v1 beta, where beta is the saturation of the IP3 receptor by IP3:
    dZ/dt = v0 + v1 beta - v2 + v3 + kf Y - k Z,   dY/dt = v2 - v3 - kf Y,
    v2 = VM2 Z^2 / (K2^2 + Z^2),   v3 = VM3 Y^2 / (KR^2 + Y^2) * Z^4 / (KA^4 + Z^4),
with v0 = 1, v1 = 7.3, VM2 = 65, VM3 = 500 (uM/s), K2 = 1, KR = 2, KA = 0.9 (uM), kf = 1, k = 10 (/s). A sustained
IP3 level (as made by sperm PLCzeta) gives repetitive spikes rather than one wave, and their frequency rises with
beta. The model's spikes recur every few seconds; in mouse eggs they recur every 10-20 min, because the stores
refill slowly and IP3 production is itself modulated, but the frequency coding is the same.
"""

import numpy as np
from matplotlib.colors import LinearSegmentedColormap

import wikibio as bio
from wikibio import charts, quant

P = bio.P
fig, ax = bio.canvas(30, 10.4)

# ---------------------------------------------------------------- bistable front
L, D, k, a = 80.0, 20.0, 10.0, 0.25
nx = 161
x = np.linspace(0, L, nx)
dx = x[1] - x[0]
dt = 0.2 * dx * dx / D
c = np.where(x < 6, 1.0, 0.0)
times, snaps = [], []
t, Tend = 0.0, 18.0
nsteps = int(Tend / dt)
rec_every = max(1, nsteps // 180)
for i in range(nsteps):
    lap = np.empty_like(c)
    lap[1:-1] = c[2:] - 2 * c[1:-1] + c[:-2]
    lap[0] = 2 * (c[1] - c[0])
    lap[-1] = 2 * (c[-2] - c[-1])
    c = c + dt * (D * lap / dx**2 + k * c * (c - a) * (1 - c))
    t += dt
    if i % rec_every == 0:
        times.append(t)
        snaps.append(c.copy())
snaps = np.array(snaps)
v = np.sqrt(D * k / 2) * (1 - 2 * a)

bio.panel(ax, "A", (0.2, 10.2))
ka = charts.axes_at(ax, (1.9, 1.6, 7.0, 7.6))
ka.imshow(snaps.T, origin="lower", aspect="auto", extent=(0, times[-1], 0, L), cmap=LinearSegmentedColormap.from_list("ca", [P.mix(P.surface(), P.muted(), 0.15), P.fill("ca"), P.edge("drug")]), vmin=0, vmax=1)
tt = np.linspace(0, times[-1], 10)
ka.plot(tt, np.clip(6 + v * (tt - 0.6), 0, L), color=P.ink(), lw=0.9, ls=(0, (3, 2)))
charts.style_axes(ka, "time / s", "position x / µm")
ka.text(1.0, 55, f"front: v = {v:.0f} µm/s", color=P.ink(), fontsize=8)

bio.panel(ax, "B", (10.3, 10.2))
pb = quant.Plot(ax, (12.0, 1.6, 7.0, 7.6), xlim=(0, 80), ylim=(0, 1.1), xlabel="position x / µm", ylabel="free Ca²⁺ (scaled)",
                xticks=[0, 20, 40, 60, 80], yticks=[0, 0.5, 1])
for j, ts in enumerate(np.arange(0, 18, 3)):
    idx = int(np.argmin(np.abs(np.array(times) - ts)))
    pb.line(x, snaps[idx], "ca" if j % 2 == 0 else "drug", lw=1.3, text=f"{ts:g} s", at=min(0.95, (6 + v * ts) / 80 + 0.02),
            dx=0.05, dy=0.08 + 0.0 * j)

# ---------------------------------------------------------------- oscillations
bio.panel(ax, "C", (20.3, 10.2))
v0, v1, VM2, VM3, K2, KR, KA, kf, kk = 1.0, 7.3, 65.0, 500.0, 1.0, 2.0, 0.9, 1.0, 10.0


def rhs(_, y, beta):
    Z, Y = y
    v2 = VM2 * Z**2 / (K2**2 + Z**2)
    v3 = VM3 * Y**2 / (KR**2 + Y**2) * Z**4 / (KA**4 + Z**4)
    return np.array([v0 + v1 * beta - v2 + v3 + kf * Y - kk * Z, v2 - v3 - kf * Y])


tg = np.linspace(0, 12, 12001)
pc = quant.Plot(ax, (22.0, 1.6, 7.4, 7.6), xlim=(0, 12), ylim=(0, 1.7), xlabel="time / s", ylabel="cytosolic Ca²⁺ / µM",
                xticks=[0, 4, 8, 12], yticks=[0, 0.5, 1, 1.5])
for beta, tok, dy in ((0.3, "dna", 0.0), (0.5, "drug", 0.0)):
    sol = quant.odeint_rk4(lambda t_, y_: rhs(t_, y_, beta), np.array([0.3, 1.5]), tg)
    pc.line(tg, sol[:, 0], tok, lw=1.2)
pc.text(0.3, 1.6, "β = 0.3", token="dna", ha="left")
pc.text(3.0, 1.6, "β = 0.5: faster spikes", token="drug", ha="left")
