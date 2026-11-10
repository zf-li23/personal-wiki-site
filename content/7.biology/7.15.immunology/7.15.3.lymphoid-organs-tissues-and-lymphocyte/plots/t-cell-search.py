# T cells searching for antigen-presenting dendritic cells in a lymph node, modelled as a persistent
# random walk (speed v, direction persistence tau_p) in a periodic cube of volume 1e8 um^3 with n static
# targets of contact radius a. A: projected trajectories. B: fraction of T cells that have not yet found a
# target, simulation vs the Smoluchowski approximation exp(-k t), k = 4 pi D a rho, D = v^2 tau_p / 3.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(0)
V, A, VEL, TP, DT = 1e8, 20.0, 12.0, 2.0, 0.25       # um^3, um, um/min, min, min
L = V ** (1 / 3)
D = VEL ** 2 * TP / 3
T_END = 720.0
steps = int(T_END / DT)


def unit(n):
    u = rng.normal(size=(n, 3))
    return u / np.linalg.norm(u, axis=1, keepdims=True)


def simulate(n_dc, n_t=400, keep=0):
    dcs = rng.uniform(0, L, (n_dc, 3))
    x = rng.uniform(0, L, (n_t, 3))
    d = unit(n_t)
    found = np.full(n_t, np.inf)
    paths = [x[:keep].copy()]
    p_turn = DT / TP
    for s in range(1, steps + 1):
        turn = rng.random(n_t) < p_turn
        d[turn] = unit(int(turn.sum()))
        x = (x + VEL * DT * d) % L
        if keep:
            paths.append(x[:keep].copy())
        diff = x[:, None, :] - dcs[None, :, :]
        diff -= L * np.round(diff / L)
        hit = (np.einsum("ijk,ijk->ij", diff, diff).min(axis=1) < A * A) & np.isinf(found)
        found[hit] = s * DT
    return dcs, np.array(paths), found


fig, ax = bio.canvas(20.0, 8.6)

# ---- A: trajectories -----------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 8.5))
dcs, paths, found = simulate(20, n_t=3, keep=3)
box = (0.8, 1.2, 6.6, 6.6)
s = box[2] / L
ax.add_patch(__import__("matplotlib").patches.Rectangle(box[:2], box[2], box[3], fill=False, edgecolor=P.muted(), lw=0.8))
for c in dcs:
    ax.add_patch(__import__("matplotlib").patches.Circle((box[0] + c[0] * s, box[1] + c[1] * s), A * s * 1.6,
                                                       facecolor=P.fill("antibody"), edgecolor=P.edge("antibody"),
                                                       lw=0.6, zorder=4))
n_show = int(180 / DT)
for k, tok in enumerate(("dna", "drug", "enzyme")):
    end = n_show if np.isinf(found[k]) else min(n_show, int(found[k] / DT))
    xy = paths[: end + 1, k, :2]
    jumps = np.where(np.abs(np.diff(xy, axis=0)).max(axis=1) > L / 2)[0] + 1
    for seg in np.split(xy, jumps):
        ax.plot(box[0] + seg[:, 0] * s, box[1] + seg[:, 1] * s, color=quant.line_color(tok), lw=0.9, zorder=6)
    if not np.isinf(found[k]) and found[k] <= 180:
        ex, ey = box[0] + xy[-1, 0] * s, box[1] + xy[-1, 1] * s
        bio.label(ax, (ex, ey), "×", size="title", bold=True, color=quant.line_color(tok), zorder=8)
bio.label(ax, (box[0] + box[2] / 2, 0.75), "projection of a 464 µm cube, 3 h", size="tiny")
bio.label(ax, (box[0] + box[2] / 2, 8.15), "T-cell tracks and 20 antigen-bearing DCs", size="small")

# ---- B: survival ---------------------------------------------------------------------------------------
bio.panel(ax, "B", (9.0, 8.5))
pl = quant.Plot(ax, (10.6, 1.4, 8.6, 6.2), xlim=(0, 12), ylim=(0, 1.02), xlabel="time / h",
                ylabel="fraction not yet found", xticks=[0, 3, 6, 9, 12], yticks=[0, 0.25, 0.5, 0.75, 1.0])
tt = np.arange(0, T_END + DT, DT)
for n_dc, tok in ((5, "dna2"), (20, "dna"), (80, "protein")):
    _, _, f = simulate(n_dc)
    surv = np.array([(f > t_).mean() for t_ in tt])
    k = 4 * np.pi * D * A * n_dc / V
    pl.line(tt / 60, surv, tok, lw=2.0)
    pl.line(tt / 60, np.exp(-k * tt), tok, lw=1.0, dashed=True)
    pl.text(tt[len(tt) // 2] / 60 + (2.8 if n_dc == 5 else 0.4), np.exp(-k * T_END / 2) + 0.04,
            f"n = {n_dc}", size="tiny", ha="left", color=quant.line_color(tok))
pl.legend([("simulation", "muted", "-"), ("exp(−kt)", "muted", "--")], at=(16.3, 7.3))
