"""Self-thinning and size hierarchies in a zone-of-influence model of plants (Sections 11.4.2, 11.4.3).

Plants sit at random positions in a unit square (periodic). Plant i of mass w_i has a circular zone of
influence of radius rho_i = 0.015 w_i^(1/3), area A_i. Where two zones overlap (area O_ij), the overlap is
divided in proportion to w^p: p = 0 is size-symmetric competition (equal shares), p = 8 strongly
size-asymmetric (light competition, the larger plant takes nearly all). Effective area
E_i = max(0, A_i - sum_j O_ij (1 - s_ij)), s_ij = w_i^p / (w_i^p + w_j^p).
Growth per time step: dw_i = 0.5 (E_i / A_i) w_i^(2/3) - 0.05 w_i (isolated plants approach w = 125 000);
a plant dies after its mass has declined for 5 consecutive steps or falls below 0.5.
Initial masses lognormal (median 1, sigma 0.25).
A: trajectories of log mean mass against log density for three sowing densities (asymmetric competition),
with the least-squares slope of the late (thinning) part of all trajectories and a reference slope of -3/2.
B: Gini coefficient of plant mass over time (sown at 1600) for symmetric and asymmetric competition,
without mortality (solid; suppressed plants persist at minimal size) and with mortality (dashed).
C: distributions of plant mass at t = 60 without mortality.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import cKDTree

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
CR = 0.006


def lens(d, r1, r2):
    """Area of intersection of two circles with centre distance d (vectorized)."""
    out = np.zeros_like(d)
    small = np.minimum(r1, r2)
    inside = d <= np.abs(r1 - r2)
    out[inside] = np.pi * small[inside] ** 2
    m = (~inside) & (d < r1 + r2)
    dd, a, b = d[m], r1[m], r2[m]
    c1 = np.clip((dd ** 2 + a ** 2 - b ** 2) / (2 * dd * a), -1, 1)
    c2 = np.clip((dd ** 2 + b ** 2 - a ** 2) / (2 * dd * b), -1, 1)
    out[m] = (a ** 2 * np.arccos(c1) + b ** 2 * np.arccos(c2)
              - 0.5 * np.sqrt(np.clip((-dd + a + b) * (dd + a - b) * (dd - a + b) * (dd + a + b), 0, None)))
    return out


def gini(w):
    w = np.sort(w)
    n = len(w)
    return (2 * np.arange(1, n + 1) - n - 1).dot(w) / (n * w.sum())


def run(n0, p, steps=260, seed=1, mortality=True):
    rng = np.random.default_rng(seed)
    xy = rng.random((n0, 2))
    w = np.exp(rng.normal(0, 0.25, n0))
    decl = np.zeros(n0, int)
    hist = []
    snap = None
    for t in range(steps):
        rho = CR * w ** (1 / 3)
        A = np.pi * rho ** 2
        tree = cKDTree(xy, boxsize=1.0)
        pairs = tree.query_pairs(2 * rho.max(), output_type="ndarray")
        E = A.copy()
        if len(pairs):
            i, j = pairs[:, 0], pairs[:, 1]
            dvec = np.abs(xy[i] - xy[j])
            dvec = np.minimum(dvec, 1 - dvec)
            d = np.hypot(dvec[:, 0], dvec[:, 1])
            O = lens(d, rho[i], rho[j])
            if p == 0:
                si = np.full_like(O, 0.5)
            else:
                si = w[i] ** p / (w[i] ** p + w[j] ** p)
            np.subtract.at(E, i, O * (1 - si))
            np.subtract.at(E, j, O * si)
        E = np.clip(E, 0, None)
        dw = 0.5 * (E / A) * w ** (2 / 3) - 0.01 * w
        w = w + dw
        decl = np.where(dw < 0, decl + 1, 0)
        alive = (decl < 8) & (w > 0.3) if mortality else np.ones(len(w), bool)
        w = np.maximum(w, 0.3)
        xy, w, decl = xy[alive], w[alive], decl[alive]
        hist.append((len(w), w.mean(), gini(w)))
        if t == 59:
            snap = w.copy()
    return np.array(hist), snap


fig, axes = plt.subplots(1, 3, figsize=(12.8, 3.9))
ax = axes[0]
cols = [C.line("rna"), C.line("positive"), C.line("dna")]
late = []
for n0, col in zip((400, 1600, 6400), cols):
    h, _ = run(n0, 8)
    ld, lw = np.log10(h[:, 0]), np.log10(h[:, 1])
    ax.plot(ld, lw, color=col, lw=1.8, label=f"sown at {n0}")
    ax.annotate("", (ld[-1], lw[-1]), (ld[-8], lw[-8]), arrowprops=dict(arrowstyle="-|>", color=col, lw=1))
    keep = h[:, 0] < 0.6 * n0
    late.append(np.column_stack([ld[keep], lw[keep]]))
late = np.vstack(late)
sl, ic = np.polyfit(late[:, 0], late[:, 1], 1)
xx = np.linspace(late[:, 0].min(), late[:, 0].max(), 10)
ax.plot(xx, sl * xx + ic + 0.35, color=P.muted(), lw=1, ls=(0, (4, 2)))
ax.text(xx[3], sl * xx[3] + ic + 0.5, f"fitted slope {sl:.2f}", fontsize=FS["tiny"], color=P.muted())
C.style_axes(ax, "log₁₀ density (plants per unit area)", "log₁₀ mean plant mass")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
C.title(ax, "A  Self-thinning trajectories")

ax = axes[1]
res = {}
for p, col, name in ((0, C.line("dna"), "symmetric (p = 0)"), (8, C.line("negative"), "asymmetric (p = 8)")):
    h, snap = run(1600, p, steps=150, mortality=False)
    res[p] = snap
    ax.plot(np.arange(len(h)), h[:, 2], color=col, lw=1.8, label=name + ", no deaths")
    h2, _ = run(1600, p, steps=150)
    ax.plot(np.arange(len(h2)), h2[:, 2], color=col, lw=1.3, ls=(0, (4, 2)), label=name + ", with deaths")
ax.axvline(60, color=P.muted(), lw=0.6, ls=(0, (1, 2)))
ax.set_ylim(0, 1)
C.style_axes(ax, "time step", "Gini coefficient of mass")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
C.title(ax, "B  Size inequality")

ax = axes[2]
bins = np.linspace(0, max(res[0].max(), res[8].max()), 30)
ax.hist(res[0], bins=bins, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.5, alpha=0.8, label="symmetric")
ax.hist(res[8], bins=bins, color=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.5, alpha=0.6,
        label="asymmetric")
ax.set_yscale("log")
C.style_axes(ax, "plant mass at t = 60 (no deaths)", "number of plants (log scale)")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "C  Size distributions")
fig.tight_layout()
