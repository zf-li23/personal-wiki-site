"""Three spatial point patterns and Ripley's L function.

All patterns on the unit square with periodic boundaries (a torus), so that no edge correction is needed.
Regular: simple sequential inhibition (points added at random, rejected if closer than 0.055 to an existing point),
150 points. Random: homogeneous Poisson process with 150 points. Clumped: Thomas process, 20 parents (Poisson),
on average 7.5 offspring each displaced by isotropic normal deviations with SD 0.03 (150 points kept).
K(r) estimated as (area / n^2) * number of ordered pairs closer than r; L(r) = sqrt(K/pi).
Envelope: pointwise minimum and maximum of L(r) - r over 99 Poisson patterns with the same number of points.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
n = 150


def ssi(n, rmin):
    pts = []
    while len(pts) < n:
        p = rng.random(2)
        if pts:
            d = np.abs(np.array(pts) - p)
            d = np.minimum(d, 1 - d)
            if (np.hypot(d[:, 0], d[:, 1]) < rmin).any():
                continue
        pts.append(p)
    return np.array(pts)


def thomas(n, parents, sd):
    par = rng.random((parents, 2))
    pts = []
    while len(pts) < n:
        c = par[rng.integers(parents)]
        pts.append((c + rng.normal(0, sd, 2)) % 1.0)
    return np.array(pts)


r = np.linspace(0.005, 0.25, 50)


def lfun(pts):
    d = np.abs(pts[:, None, :] - pts[None, :, :])
    d = np.minimum(d, 1 - d)
    dist = np.hypot(d[..., 0], d[..., 1])[np.triu_indices(len(pts), 1)]
    k = np.array([2 * (dist < rr).sum() for rr in r]) / len(pts) ** 2
    return np.sqrt(k / np.pi) - r


patterns = [("Regular", ssi(n, 0.055), "plant"), ("Random", rng.random((n, 2)), "dna"),
            ("Clumped", thomas(n, 20, 0.03), "rna")]
env = np.array([lfun(rng.random((n, 2))) for _ in range(99)])
lo, hi = env.min(axis=0), env.max(axis=0)

fig = plt.figure(figsize=(14.0, 4.4))
gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1, 1.5])
for i, (name, pts, tok) in enumerate(patterns):
    ax = fig.add_subplot(gs[0, i])
    ax.scatter(pts[:, 0], pts[:, 1], s=9, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color(P.muted())
    ax.set_title(f"{'ABC'[i]}  {name}", loc="left", fontsize=10)
lx = fig.add_subplot(gs[0, 3])
lx.fill_between(r, lo, hi, color=P.fill("neutral"), alpha=0.4, lw=0, label="CSR envelope (99 simulations)")
for name, pts, tok in patterns:
    lx.plot(r, lfun(pts), color=P.edge(tok), lw=2.0, label=name.lower())
lx.axhline(0, color=P.muted(), lw=0.8)
lx.set_xlim(0, 0.25)
lx.set_xlabel("distance $r$")
lx.set_ylabel("$L(r) - r$")
lx.legend(frameon=False, fontsize=8, loc="upper right")
lx.set_title("D  Ripley's $L$ function", loc="left", fontsize=10)
for s in ("top", "right"):
    lx.spines[s].set_visible(False)
fig.tight_layout()
