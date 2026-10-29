"""The two-layer lubrication model of neural plate shaping (Percus and Childress, after Jacobson and Gordon).
(A) The neural plate (initially a disc, anterior left) rides on a viscous layer of mesoderm whose upper surface
moves with u = h0 grad T, where T is the interfacial tension; T is carried with the flow (T_t + h0 |grad T|^2 = 0),
so q = 2 u obeys pressureless flow and is constant along straight characteristics. With an initial tension that
rises posteriorly along the notochord (from about x = -0.1) and a uniform shrinkage of the plate cells, the
disc becomes a keyhole: broad in front (brain), narrow and elongated behind (spinal cord). Outlines at equal time
steps; the dashed line is the notochord. (B) Thickness of the lower layer across the notochord from
h_t = -(h0^2/2) Laplacian(T), for a tension that is lowest along the notochord: a midline groove flanked by two
folds deepens linearly in time."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
h0, a, sw, xt, gamma = 1.0, 0.5, 0.35, -0.1, 0.0


def q0(p):
    """Initial characteristic velocity q0 = 2 h0 grad T0 for T0 = (a/2) sigma(x) ((x - xt)^2 - y^2), where the
    logistic switch sigma turns the tension field on behind the notochord tip (a strain flow: posterior extension,
    medio-lateral convergence)."""
    x, y = p[..., 0], p[..., 1]
    s_ = 1 / (1 + np.exp(-(x - xt) / sw))
    ds = s_ * (1 - s_) / sw
    f = (x - xt) ** 2 - y ** 2
    return np.stack([2 * h0 * 0.5 * a * (ds * f + 2 * s_ * (x - xt)), 2 * h0 * 0.5 * a * (-2 * s_ * y)], axis=-1)


def q_at(x, t, guess):
    """q(x, t) = q0(x0) with x = x0 + t q0(x0): solve for x0 by Newton iteration (before characteristics cross)."""
    x0 = guess.copy()
    eps = 1e-6
    for _ in range(12):
        f = x0 + t * q0(x0) - x
        J = np.zeros(x0.shape + (2,))
        for j in range(2):
            d = np.zeros(2)
            d[j] = eps
            J[..., :, j] = (x0 + d + t * q0(x0 + d) - (x0 + t * q0(x0))) / eps
        x0 = x0 - np.linalg.solve(J, f[..., None])[..., 0]
    return q0(x0), x0


th = np.linspace(0, 2 * np.pi, 241)
X = np.c_[0.9 * np.cos(th), 0.9 * np.sin(th)]
x0g = X.copy()
dt, nsteps = 0.0025, 360
snaps = {0: X.copy()}
for n in range(1, nsteps + 1):
    t = n * dt
    q, x0g = q_at(X, t, x0g)
    c = X.mean(axis=0)
    X = X + dt * (0.5 * q - gamma * (X - c))
    if n % 90 == 0:
        snaps[n] = X.copy()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.0, 3.9), gridspec_kw={"width_ratios": [1.45, 1]})
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.17, top=0.88, wspace=0.25)
toks = ["neutral", "dna", "protein", "k", "receptor"]
for k, (n, Xs) in enumerate(sorted(snaps.items())):
    ax1.plot(Xs[:, 0], Xs[:, 1], color=charts.line(toks[k]), lw=1.5, label=f"t = {n * dt:.2f}")
ax1.plot([xt, 1.8], [0, 0], color=P.muted(), lw=1.0, ls="--")
ax1.text(xt - 0.05, 0.08, "notochord tip", fontsize=FT["tiny"], color=P.muted(), ha="right")
ax1.set_aspect("equal")
ax1.set_xlim(-1.2, 1.8)
ax1.set_ylim(-1.15, 1.15)
ax1.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right", ncol=5, handlelength=1.2,
           columnspacing=0.8, bbox_to_anchor=(1.0, 1.12))
charts.style_axes(ax1, "x (anterior-posterior)", "y")
charts.title(ax1, "A  Neural plate outline")

y = np.linspace(-1.5, 1.5, 301)
b, wv = 1.0, 0.45
g = np.exp(-y ** 2 / wv ** 2)
lap = -b * (4 * y ** 2 / wv ** 4 - 2 / wv ** 2) * g     # Laplacian of T0 = -b exp(-y^2 / wv^2)
for k, t in enumerate((0.0, 0.03, 0.06, 0.09)):
    ax2.plot(y, h0 - 0.5 * h0 ** 2 * t * lap, color=charts.line(toks[k + 1] if k else "neutral"), lw=1.5, label=f"t = {t:.2f}")
ax2.axvline(0, color=P.muted(), lw=0.6, ls=":")
ax2.text(0.05, 0.6, "groove", fontsize=FT["tiny"], color=P.ink())
ax2.text(0.62, 1.07, "fold", fontsize=FT["tiny"], color=P.ink())
ax2.set_ylim(0.5, 1.15)
ax2.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax2, "y (across the notochord)", "h / h0")
charts.title(ax2, "B  Groove and folds")
