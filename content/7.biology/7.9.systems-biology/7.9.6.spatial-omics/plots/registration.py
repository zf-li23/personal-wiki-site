"""Landmark registration of two images of the same section, using nucleus centroids as matched
points. The moving image (orange) is the fixed one (blue) rotated by 8 degrees, scaled by 1.03 and
0.98 along its axes (uneven tissue shrinkage), sheared, translated, and measured with centroid
noise of 0.8 um. A: before registration. B: the best rigid transform (Kabsch algorithm, rotation
and translation by SVD); residuals magnified 10x. C: the least-squares affine transform; residuals
magnified 10x. D: error at 200 held-out nuclei against the number of landmarks used for fitting:
the rigid model cannot absorb the anisotropic scaling, the affine model approaches the error of the
true transform (dashed), which is set by the centroid noise."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
N = 60
th = np.deg2rad(8)
R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
A_true = R @ np.array([[1.03, 0.02], [0.0, 0.98]])
t_true = np.array([25.0, -15.0])
sigma = 0.8


Ainv = np.linalg.inv(A_true)
floor = sigma * np.sqrt(np.trace(Ainv @ Ainv.T))   # error of the true transform


def moving_of(x):
    return x @ A_true.T + t_true + rng.normal(0, sigma, x.shape)


def kabsch(X, Y):
    """Rotation Rk and translation t minimizing sum |Rk x_i + t - y_i|^2."""
    mx, my = X.mean(0), Y.mean(0)
    H = (X - mx).T @ (Y - my)
    U, _, Vt = np.linalg.svd(H)
    d = np.sign(np.linalg.det(Vt.T @ U.T))
    Rk = Vt.T @ np.diag([1, d]) @ U.T
    return Rk, my - Rk @ mx


def affine(X, Y):
    """Least-squares affine map: Y ~ X A^T + t."""
    Xh = np.hstack([X, np.ones((len(X), 1))])
    M, *_ = np.linalg.lstsq(Xh, Y, rcond=None)
    return M[:2].T, M[2]


def rms(X, Y, A, t):
    return np.sqrt(np.mean(np.sum((X @ A.T + t - Y) ** 2, 1)))


fixed = rng.uniform(0, 300, (N, 2))
moving = moving_of(fixed)
# register the moving image onto the fixed one: fit maps moving -> fixed
Rk, tk = kabsch(moving, fixed)
Aa, ta = affine(moving, fixed)
rms_rigid, rms_aff = rms(moving, fixed, Rk, tk), rms(moving, fixed, Aa, ta)
ang = np.degrees(np.arctan2(Rk[1, 0], Rk[0, 0]))

test_f = rng.uniform(0, 300, (200, 2))
test_m = moving_of(test_f)
floor = rms(test_m, test_f, Ainv, -Ainv @ t_true)   # error of the true transform on the same nuclei
ns = np.array([3, 4, 5, 6, 8, 10, 15, 20, 30, 45, 60])
err_r, err_a = [], []
for k in ns:
    er, ea = [], []
    for rep in range(40):
        idx = rng.choice(N, k, replace=False)
        A1, t1 = kabsch(moving[idx], fixed[idx])
        er.append(rms(test_m, test_f, A1, t1))
        A2, t2 = affine(moving[idx], fixed[idx])
        ea.append(rms(test_m, test_f, A2, t2))
    err_r.append(np.median(er))
    err_a.append(np.median(ea))
RESULT = {"rms_rigid": rms_rigid, "rms_affine": rms_aff, "kabsch_angle": ang, "A_fit": Aa,
          "A_true_inv": np.linalg.inv(A_true), "heldout_rigid60": err_r[-1], "heldout_aff60": err_a[-1],
          "heldout_aff3": err_a[0], "heldout_aff6": err_a[3], "noise_floor": floor}

fig, axs = plt.subplots(1, 4, figsize=(12.6, 3.3), gridspec_kw={"width_ratios": [1, 1, 1, 1.2]})
fig.subplots_adjust(left=0.02, right=0.99, bottom=0.17, top=0.86, wspace=0.25)
cf, cm = charts.line("dna"), charts.line("rna")
axs[0].scatter(*fixed.T, s=10, color=cf, label="fixed")
axs[0].scatter(*moving.T, s=10, color=cm, marker="^", label="moving")
for a, B, t, title_ in [(axs[1], Rk, tk, f"B  Rigid: RMS {rms_rigid:.1f} µm"),
                        (axs[2], Aa, ta, f"C  Affine: RMS {rms_aff:.2f} µm")]:
    mapped = moving @ B.T + t
    a.scatter(*fixed.T, s=10, color=cf)
    for p, q in zip(fixed, mapped):
        a.plot([p[0], p[0] + 10 * (q[0] - p[0])], [p[1], p[1] + 10 * (q[1] - p[1])], color=cm, lw=0.9)
    charts.title(a, title_)
charts.title(axs[0], "A  Matched nuclei, before")
axs[0].legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="lower right", ncol=2)
for a in axs[:3]:
    a.set_aspect("equal")
    a.set_xlim(-20, 350)
    a.set_ylim(-95, 360)
    a.set_xticks([])
    a.set_yticks([])
    for sp in a.spines.values():
        sp.set_color(P.muted())
axs[3].plot(ns, err_r, "o-", ms=3, color=cm, lw=1.4, label="rigid (Kabsch)")
axs[3].plot(ns, err_a, "o-", ms=3, color=cf, lw=1.4, label="affine (least squares)")
axs[3].axhline(floor, color=P.muted(), ls="--", lw=0.8)
axs[3].text(60, floor * 1.08, "true transform", fontsize=7, color=P.muted(), ha="right")
axs[3].set_xscale("log")
axs[3].set_yscale("log")
axs[3].yaxis.set_major_formatter(plt.matplotlib.ticker.ScalarFormatter())
axs[3].yaxis.set_minor_formatter(plt.matplotlib.ticker.NullFormatter())
axs[3].set_yticks([1, 2, 3, 4])
axs[3].xaxis.set_major_formatter(plt.matplotlib.ticker.ScalarFormatter())
axs[3].set_xticks([3, 5, 10, 20, 60])
axs[3].legend(frameon=False, fontsize=7.5, labelcolor=P.ink())
charts.style_axes(axs[3], "landmarks used", "held-out error / µm")
charts.title(axs[3], "D  How many landmarks")
