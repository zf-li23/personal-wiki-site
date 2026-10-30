"""Estimating a mitotic field from one synthetic section (Section 31.6).

A synthetic limb-bud section is divided into 30 x 22 squares; the bud occupies a rounded region, each square holds
about 40 nuclei (Poisson), and the true probability of mitosis m(x) is about 0.12, lower in the dense central core
and proximally. Mitotic counts are Poisson with mean m * rho. Estimators: the raw index M / rho; r = 3 passes of
nearest-neighbour averaging (weights 1/4, 1/2, 1/4 in each direction) applied to M and rho separately inside the
tissue (so that the zeros outside do not bias the edge); the Poisson maximum likelihood fit of log m as a
combination of 15 cosine functions cos(i pi u) cos(j pi v), i + j <= 4, with offset log rho, by iteratively
reweighted least squares. Root-mean-square errors inside the tissue are shown.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from matplotlib.colors import LinearSegmentedColormap

P = bio.P
rng = np.random.default_rng(7)
nx, ny = 30, 22
u = (np.arange(nx) + 0.5) / nx          # proximal (0) to distal (1)
v = (np.arange(ny) + 0.5) / ny          # posterior (0) to anterior (1)
U, V = np.meshgrid(u, v)
mask = ((U / 0.98) ** 2.6 + ((V - 0.5) / 0.47) ** 2 <= 1.0) & (U > 0.0)
core = np.exp(-(((U - 0.45) / 0.22) ** 2 + ((V - 0.5) / 0.2) ** 2))
m_true = 0.13 * (1 - 0.5 * core) * (0.75 + 0.25 * U)
rho = rng.poisson(40, size=U.shape) * mask
M = rng.poisson(m_true * rho) * mask


def smooth(A, r):
    B = A.astype(float).copy()
    for _ in range(r):
        B = 0.5 * B + 0.25 * (np.roll(B, 1, 0) + np.roll(B, -1, 0))
        B = 0.5 * B + 0.25 * (np.roll(B, 1, 1) + np.roll(B, -1, 1))
    return B


raw = np.where(mask, M / np.maximum(rho, 1), np.nan)
pad = lambda A: np.pad(A, 4)
sm = smooth(pad(M * mask), 3)[4:-4, 4:-4] / np.maximum(smooth(pad(rho * mask), 3)[4:-4, 4:-4], 1e-9)
sm = np.where(mask, sm, np.nan)

# Poisson GLM by IRLS
ij = [(i, j) for i in range(5) for j in range(5) if i + j <= 4]
Xd = np.stack([np.cos(np.pi * i * U[mask]) * np.cos(np.pi * j * V[mask]) for i, j in ij], axis=1)
y = M[mask].astype(float)
off = np.log(np.maximum(rho[mask], 1))
beta = np.zeros(len(ij))
beta[0] = np.log(max(y.sum(), 1) / np.exp(off).sum())
for _ in range(30):
    eta = Xd @ beta + off
    mu = np.exp(eta)
    z = eta - off + (y - mu) / mu
    W = mu
    A = Xd.T @ (W[:, None] * Xd)
    beta_new = np.linalg.solve(A, Xd.T @ (W * z))
    if np.max(np.abs(beta_new - beta)) < 1e-9:
        beta = beta_new
        break
    beta = beta_new
ml = np.full(U.shape, np.nan)
ml[mask] = np.exp(Xd @ beta)


def rmse(E):
    return np.sqrt(np.nanmean((E[mask] - m_true[mask]) ** 2))


cmap = LinearSegmentedColormap.from_list("w", [P.surface(), P.fill("protein"), P.edge("protein")])
fig, ax = bio.canvas(30.0, 7.4)
panels = [("A", "true field", np.where(mask, m_true, np.nan), None), ("B", "raw index M/ρ", raw, rmse(raw)),
          ("C", "smoothed (r = 3)", sm, rmse(sm)), ("D", "Poisson ML, 15 terms", ml, rmse(ml))]
for k, (lt, title, F, e) in enumerate(panels):
    x0 = 0.8 + 7.3 * k
    pa = C.axes_at(ax, (x0, 1.0, 6.4, 6.4 * ny / nx))
    im = pa.imshow(F, origin="lower", cmap=cmap, vmin=0.03, vmax=0.2, extent=(0, 1, 0, ny / nx), interpolation="nearest")
    pa.set_xticks([])
    pa.set_yticks([])
    for sp in pa.spines.values():
        sp.set_visible(False)
    bio.panel(ax, lt, (x0 - 0.6, 7.2))
    t = title if e is None else f"{title}\nRMSE = {e:.3f}"
    bio.label(ax, (x0 + 3.2, 6.35), t, size="small", va="bottom")
bio.label(ax, (0.9, 0.5), "proximal", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (7.2, 0.5), "distal (AER)", size="tiny", color=P.muted(), ha="right")
cax = C.axes_at(ax, (29.4, 1.0, 0.25, 4.7))
cb = fig.colorbar(im, cax=cax)
cb.outline.set_edgecolor(P.muted())
cb.ax.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=bio.core.FONT["tiny"])
cb.set_label("mitotic index", color=P.ink(), fontsize=bio.core.FONT["tiny"])
