"""Chemically active droplets suppress Ostwald ripening. Droplet material is made in the dilute phase
(rate s per volume) and converted back into a soluble form inside droplets (rate k per molecule).
Dimensionless growth law of a droplet of radius R at dilute-phase supersaturation epsilon:
dR/dt = (1/R)(epsilon - 1/R) - k R/3 (radius in units of the capillary length times c0/c_in-type
factors, as in the LSW model). A: dR/dt against R at epsilon = 0.37: a passive droplet (k = 0) has a
single, unstable fixed point at the critical radius 1/epsilon, so larger droplets grow and smaller ones
shrink; with k = 0.02 a second, stable fixed point appears at larger R (filled dot), stable whenever it
exceeds 1.5/epsilon. B, C: 60 droplets with random initial radii coupled through a common dilute phase.
B: passive (s = k = 0): Ostwald ripening, droplets dissolve one after another and the survivors grow.
C: active: the small droplets dissolve, but the remaining ones converge to the same radius and stay.
D: number of droplets against time for both cases."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 4, figsize=(11.4, 3.1))
fig.subplots_adjust(wspace=0.42, left=0.055, right=0.985, bottom=0.17, top=0.87)

K = 0.02
ax = axs[0]
eps = 0.37
R = np.linspace(1.0, 9, 400)
for k, tok, lab in [(0.0, "neutral", "passive"), (K, "blood", "active")]:
    v = (1 / R) * (eps - 1 / R) - k * R / 3
    ax.plot(R, v, color=charts.line(tok), lw=1.6, label=lab)
    sgn = np.sign(v)
    for i in np.where(np.diff(sgn) != 0)[0]:
        r0 = R[i]
        stable = v[i] > 0 > v[i + 1]
        ax.plot([r0], [0], "o", ms=5, mfc=charts.line(tok) if stable else "none", mec=charts.line(tok), mew=1.2)
ax.axhline(0, color=P.muted(), lw=0.7)
ax.set_ylim(-0.06, 0.05)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "radius $R$", r"growth rate $\mathrm{d}R/\mathrm{d}t$")
charts.title(ax, "A  Growth law")


def simulate(k, s, beta=0.05, tmax=6000.0, dt=0.05):
    rng = np.random.default_rng(3)
    u = rng.uniform(2.0, 6.5, 60) ** 3
    e = 0.37
    ts, traj = [], []
    t = 0.0
    nrec = 0
    while t < tmax:
        Rr = np.cbrt(np.maximum(u, 0))
        alive = u > 0
        du = np.where(alive, 3 * (Rr * e - 1) - k * u, 0.0)
        de = s - beta * np.sum(np.where(alive, Rr * e - 1, 0.0))
        u = np.where(alive, u + dt * du, 0.0)
        u[u < 1e-6] = 0.0
        e = e + dt * de
        t += dt
        nrec += 1
        if nrec % 40 == 0:
            ts.append(t)
            traj.append(np.cbrt(u))
    return np.array(ts), np.array(traj)


tp, Rp = simulate(0.0, 0.0)
s_active = 0.05 * (K / 3) * 20 * 5.0 ** 3
ta, Ra = simulate(K, s_active)

for ax, (t, Rt), title, tok in [(axs[1], (tp, Rp), "B  Passive: ripening", "neutral"),
                               (axs[2], (ta, Ra), "C  Active: size selection", "blood")]:
    for j in range(Rt.shape[1]):
        r = Rt[:, j].copy()
        r[r <= 0] = np.nan
        ax.plot(t, r, color=charts.line(tok), lw=0.7, alpha=0.8)
    ax.set_ylim(0, 16)
    charts.style_axes(ax, "time $t$", "droplet radius $R$")
    charts.title(ax, title)

ax = axs[3]
ax.plot(tp, (Rp > 0).sum(axis=1), color=charts.line("neutral"), lw=1.6, label="passive")
ax.plot(ta, (Ra > 0).sum(axis=1), color=charts.line("blood"), lw=1.6, label="active")
ax.set_ylim(0, 62)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "time $t$", "number of droplets")
charts.title(ax, "D  Number of droplets")
