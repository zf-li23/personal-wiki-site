"""The budding-yeast cell cycle as a hysteresis loop driven by growth (Tyson and Novak, 2001).
Variables: cyclin B (CycB), active Cdh1, total and active Cdc20, an intermediary enzyme IEP and the
cell mass m, which grows logistically and is halved when CycB falls below 0.1 (division); time in
minutes. A: steady states of the CycB-Cdh1 module alone (Cdc20 inactive) against m: an S-shaped
curve with a G1 branch (low CycB, Cdh1 on; solid lower) and an S/G2/M branch (high CycB, Cdh1 off;
solid upper) joined by an unstable branch (dashed); the full model (red) creeps along the G1 branch
as the cell grows, jumps up when m passes the saddle-node point (Start), and is reset to G1 by
Cdc20, which re-activates Cdh1 at the end of mitosis. B: time courses over three cycles: mass,
CycB and Cdh1."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
q = dict(k1=0.04, k2a=0.04, k2b=1.0, k3a=1.0, k3b=10.0, k4=35.0, J3=0.04, J4=0.04, k5a=0.005, k5b=0.2,
         k6=0.1, J5=0.3, n=4, k7=1.0, k8=0.5, J7=1e-3, J8=1e-3, Mad=1.0, k9=0.1, k10=0.02, mu=0.005, ms=10.0)


def rhs(t, y):
    B, H, Ct, Ca, I, m = y
    s = (m * B / q["J5"]) ** q["n"]
    return [q["k1"] - (q["k2a"] + q["k2b"] * H) * B,
            (q["k3a"] + q["k3b"] * Ca) * (1 - H) / (q["J3"] + 1 - H) - q["k4"] * m * B * H / (q["J4"] + H),
            q["k5a"] + q["k5b"] * s / (1 + s) - q["k6"] * Ct,
            q["k7"] * I * (Ct - Ca) / (q["J7"] + Ct - Ca) - q["k8"] * q["Mad"] * Ca / (q["J8"] + Ca) - q["k6"] * Ca,
            q["k9"] * m * B * (1 - I) - q["k10"] * I,
            q["mu"] * m * (1 - m / q["ms"])]


y = np.array([0.05, 0.9, 0.1, 0.05, 0.05, 0.6])
t, dt = 0.0, 0.5
ts, ys = [], []
for i in range(int(1500 / dt)):
    yn = solve_ivp(rhs, (t, t + dt), y, method="LSODA", rtol=1e-6, atol=1e-9).y[:, -1]
    if y[0] >= 0.1 and yn[0] < 0.1:
        yn[5] /= 2
    y = yn
    t += dt
    ts.append(t)
    ys.append(y.copy())
ts = np.array(ts)
ys = np.array(ys).T

fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.5))
fig.subplots_adjust(wspace=0.3, left=0.08, right=0.98, bottom=0.16, top=0.88)
ax = axs[0]
H = np.linspace(1e-4, 1 - 1e-4, 4000)
B = q["k1"] / (q["k2a"] + q["k2b"] * H)
m = q["k3a"] * (1 - H) * (q["J4"] + H) / ((q["J3"] + 1 - H) * q["k4"] * B * H)


def stable(Hh, Bb, mm):
    """Eigenvalues of the CycB-Cdh1 module (Cdc20 inactive) at a steady state."""
    k2 = q["k2a"] + q["k2b"] * Hh
    dHdH = -q["k3a"] * q["J3"] / (q["J3"] + 1 - Hh) ** 2 - q["k4"] * mm * Bb * q["J4"] / (q["J4"] + Hh) ** 2
    J = np.array([[-k2, -q["k2b"] * Bb], [-q["k4"] * mm * Hh / (q["J4"] + Hh), dHdH]])
    return np.all(np.linalg.eigvals(J).real < 0)


st = np.array([stable(h, b, mm) for h, b, mm in zip(H, B, m)])
for mask, ls in ((st, "-"), (~st, "--")):
    mm = np.where(mask, m, np.nan)
    ax.plot(mm, B, color=charts.line("protein") if ls == "-" else P.muted(), lw=1.6, ls=ls)
sel = ts > 700
ax.plot(ys[5, sel], ys[0, sel], color=charts.line("blood"), lw=0.9)
ax.set_xlim(0, 1.2)
ax.set_ylim(0.025, 1.5)
ax.set_yscale("log")
ax.text(0.05, 0.03, "G1 (Cdh1 on)", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.text(0.75, 1.1, "S/G2/M (Cdh1 off)", fontsize=bio.core.FONT["tiny"], color=P.ink())
charts.style_axes(ax, "cell mass m", "CycB")
charts.title(ax, "A  Growth drives a hysteresis loop")

ax = axs[1]
sel = (ts > 800) & (ts < 1250)
ax.plot(ts[sel], ys[5, sel], color=charts.line("plant"), lw=1.3, label="mass m")
ax.plot(ts[sel], ys[0, sel], color=charts.line("blood"), lw=1.3, label="CycB")
ax.plot(ts[sel], ys[1, sel], color=charts.line("dna"), lw=1.3, label="Cdh1")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), ncol=3, loc="upper center")
ax.set_ylim(0, 1.15)
charts.style_axes(ax, "time / min", "level")
charts.title(ax, "B  Three cycles")
