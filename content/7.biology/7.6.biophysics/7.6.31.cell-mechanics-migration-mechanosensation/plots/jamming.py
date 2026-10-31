"""Jamming of self-propelled soft disks, a minimal model of cell monolayers. N = 120 bidisperse disks
(radii 1 and 1.4) in a periodic box, overdamped dynamics with harmonic repulsion (stiffness 1),
self-propulsion speed v0 = 0.02 along a polarity that diffuses with rotational diffusion coefficient
D_r = 0.1 (persistence time 10). A: final positions at packing fraction 0.62 (fluid) and 0.88 (jammed),
colored by the distance moved in the run (center-of-mass drift removed). B: mean squared displacement against lag time at five packing
fractions: with increasing density cells are increasingly hindered by their neighbors and the MSD
becomes subdiffusive (caging) near 0.84, the random close packing of disks in two dimensions. C: long-time effective
diffusion coefficient, normalized by that of a free cell D0 = v0^2/(2 D_r), against packing fraction:
it falls by more than an order of magnitude on approaching jamming. (A small system and short runs:
the transition is smeared.)"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
N, v0, Dr, dt, steps = 120, 0.02, 0.1, 0.5, 3500
rad = np.where(np.arange(N) < N // 2, 1.0, 1.4)


def run(phi, seed=0):
    rng = np.random.default_rng(seed)
    L = np.sqrt(np.pi * np.sum(rad ** 2) / phi)
    x = rng.uniform(0, L, (N, 2))
    th = rng.uniform(0, 2 * np.pi, N)
    # relax overlaps first
    for _ in range(400):
        d = x[:, None, :] - x[None, :, :]
        d -= L * np.round(d / L)
        r = np.sqrt((d ** 2).sum(-1)) + np.eye(N)
        ov = np.clip(rad[:, None] + rad[None, :] - r, 0, None)
        np.fill_diagonal(ov, 0)
        x = (x + 0.5 * (ov / r)[:, :, None].__mul__(d).sum(1)) % L
    unw = x.copy()
    traj = [unw.copy()]
    for s in range(steps):
        d = x[:, None, :] - x[None, :, :]
        d -= L * np.round(d / L)
        r = np.sqrt((d ** 2).sum(-1)) + np.eye(N)
        ov = np.clip(rad[:, None] + rad[None, :] - r, 0, None)
        np.fill_diagonal(ov, 0)
        f = ((ov / r)[:, :, None] * d).sum(1)
        vel = f + v0 * np.stack([np.cos(th), np.sin(th)], 1)
        x = (x + dt * vel) % L
        unw = unw + dt * vel
        th = th + np.sqrt(2 * Dr * dt) * rng.standard_normal(N)
        if s % 10 == 9:
            traj.append(unw.copy())
    traj = np.array(traj)
    traj = traj - traj.mean(axis=1, keepdims=True)  # remove the drift of the center of mass
    return L, x, traj


phis = [0.62, 0.70, 0.78, 0.84, 0.88]
out = {p: run(p) for p in phis}
fig = plt.figure(figsize=(11.0, 3.3))
gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1.2, 1.2], wspace=0.4, left=0.03, right=0.98, bottom=0.17, top=0.87)
for i, p in enumerate([0.62, 0.88]):
    ax = fig.add_subplot(gs[i])
    L, x, traj = out[p]
    disp = np.sqrt(((traj[-1] - traj[0]) ** 2).sum(1))
    cmap = plt.get_cmap("viridis")
    for j in range(N):
        ax.add_patch(Circle(x[j], rad[j], facecolor=cmap(min(disp[j] / 6.0, 1.0)), edgecolor=P.ink(), lw=0.3))
    ax.set_xlim(0, L); ax.set_ylim(0, L); ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    charts.title(ax, f"{'A' if i == 0 else ' '}  packing {p:.2f}")
ax = fig.add_subplot(gs[2])
toks = ["dna", "bacterium", "lipid_head", "blood", "neutral"]
Deff = []
for p, tok in zip(phis, toks):
    L, x, traj = out[p]
    lags = np.unique(np.logspace(0, np.log10(len(traj) // 3), 15).astype(int))
    msd = np.array([np.mean(((traj[l:] - traj[:-l]) ** 2).sum(-1)) for l in lags])
    t = lags * 10 * dt
    ax.loglog(t, msd, "o-", ms=2.5, lw=1.1, color=charts.line(tok), label=rf"$\phi = {p:.2f}$")
    Deff.append(msd[-1] / (4 * t[-1]))
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "lag time", "MSD")
charts.title(ax, "B  Caging")
ax = fig.add_subplot(gs[3])
D0 = v0 ** 2 / (2 * Dr)
ax.semilogy(phis, np.array(Deff) / D0, "o-", color=charts.line("protein"), lw=1.5)
ax.axvline(0.84, color=P.muted(), lw=0.8, ls=":")
ax.text(0.845, 0.9, r"$\phi_J \approx 0.84$", transform=ax.get_xaxis_transform(), fontsize=FT["tiny"], color=P.ink())
charts.style_axes(ax, r"packing fraction $\phi$", r"$D_{\mathrm{eff}}/D_0$")
charts.title(ax, "C  Jamming transition")
