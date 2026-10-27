"""Hop diffusion in the picket-fence model: a random walk on a square lattice divided into compartments.

Lattice spacing a = 5 nm, microscopic diffusion coefficient D_mu = 5 um^2/s (time step a^2/(4 D_mu)),
square compartments of side L = 100 nm whose walls are crossed with probability p = 0.003 per attempt.
A: one 50 ms trajectory, colored by time, over the compartment grid.
B: apparent diffusion coefficient MSD/(4t) for 400 walkers, with D_mu at short times and the
long-time value of Formula 4.5.1, 1/D_M = 1/D_mu + 1/(kappa L) with kappa = p D_mu / a (dashed);
free diffusion (p = 1) for comparison.
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(22.0, 8.4)

a = 5.0            # nm
Dmu = 5e6          # nm^2/s
dt = a * a / (4 * Dmu)
n = 20             # sites per compartment (L = 100 nm)
L = n * a
p = 0.003
rng = np.random.default_rng(0)
STEPS = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])


def walk(nw, nsteps, p, record):
    pos = np.zeros((nw, 2), dtype=np.int64) + n // 2
    start = pos.copy()
    out = []
    rec = set(record)
    traj = []
    for k in range(1, nsteps + 1):
        d = STEPS[rng.integers(0, 4, nw)]
        new = pos + d
        cross = (np.floor_divide(new, n) != np.floor_divide(pos, n)).any(axis=1)
        ok = ~cross | (rng.random(nw) < p)
        pos = np.where(ok[:, None], new, pos)
        if k in rec:
            out.append(((pos - start) ** 2).sum(axis=1).mean() * a * a)
        if nw == 1 and k % 20 == 0:
            traj.append(pos[0].copy())
    return np.array(out), np.array(traj)


nsteps = int(0.2 / dt)
rec = np.unique(np.geomspace(4, nsteps, 60).astype(int))
t = rec * dt
msd, _ = walk(400, nsteps, p, rec)
msd_free, _ = walk(400, nsteps, 1.0, rec)

kappa = p * Dmu / a
DM = 1 / (1 / Dmu + 1 / (kappa * L))

# ---- A: trajectory
bio.panel(ax, "A", (0.1, 8.2))
_, tr = walk(1, int(0.05 / dt), p, [])
tr = tr * a  # nm
pa = charts.axes_at(ax, (1.3, 1.2, 6.4, 6.4))
lim = max(np.abs(tr - n // 2 * a).max() + 30, 160)
c0 = n // 2 * a
for g in np.arange(-10, 11) * L:
    pa.axvline(g, color=P.edge("muscle"), lw=1.1, alpha=0.6)
    pa.axhline(g, color=P.edge("muscle"), lw=1.1, alpha=0.6)
import matplotlib.cm as cm
from matplotlib.collections import LineCollection
segs = np.stack([tr[:-1], tr[1:]], axis=1)
lc = LineCollection(segs, cmap="viridis", lw=0.7)
lc.set_array(np.linspace(0, 50, len(segs)))
pa.add_collection(lc)
pa.set_xlim(c0 - lim, c0 + lim)
pa.set_ylim(c0 - lim, c0 + lim)
pa.set_aspect("equal")
charts.style_axes(pa, "x / nm", "y / nm")
charts.title(pa, "50 ms trajectory (color: time)")

# ---- B: apparent D
bio.panel(ax, "B", (9.6, 8.2))
pb = charts.axes_at(ax, (11.4, 1.2, 9.8, 6.4))
pb.loglog(t * 1e3, msd / (4 * t) / 1e6, "o", ms=3.2, color=charts.line("protein"), label="picket fence, p = 0.003")
pb.loglog(t * 1e3, msd_free / (4 * t) / 1e6, "o", ms=3.2, color=charts.line("neutral"), label="free diffusion")
pb.axhline(DM / 1e6, color=charts.line("negative"), lw=1.2, ls=(0, (4, 2)), label=f"Formula 4.5.1: {DM / 1e6:.2f} µm² s⁻¹")
pb.axhline(Dmu / 1e6, color=P.muted(), lw=0.7, ls=(0, (1, 2)))
tc = L * L / (4 * Dmu) * 1e3
pb.axvline(tc, color=P.muted(), lw=0.7, ls=(0, (1, 2)))
pb.text(tc * 1.1, 0.12, "L²/4Dµ", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="left")
pb.set_ylim(0.1, 10)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(pb, "time lag t / ms", "MSD / 4t  /  (µm² s⁻¹)")
charts.title(pb, "Two regimes of diffusion")
