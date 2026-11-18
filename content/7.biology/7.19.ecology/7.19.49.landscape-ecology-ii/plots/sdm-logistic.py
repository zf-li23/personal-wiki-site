"""A species distribution model fitted by logistic regression to a virtual species.

Landscape: a 120 x 120 grid of 1-km cells. Elevation (km) is a fractal surface (spectral synthesis,
H = 0.8) scaled to 0.2-3.2 km; mean annual temperature T = 24 - 6.5 x elevation (deg C); annual precipitation
Pr (mm) rises from 600 mm in the west to 1800 mm in the east plus a fractal component.
Virtual species: true probability of occurrence pi = logistic(eta) with a Gaussian (unimodal) niche,
eta = 2.0 - (T - 14)^2 / (2 x 3^2) - (Pr - 1300)^2 / (2 x 250^2).
Data: 300 survey cells chosen at random, each recorded present or absent by a Bernoulli draw from pi.
Model: logit(pi) = b0 + b1 T + b2 T^2 + b3 Pr + b4 Pr^2 (predictors standardized), fitted by maximum
likelihood (iteratively reweighted least squares).
A: true probability of occurrence and survey cells (filled: present, open: absent).
B, C: response curves (probability against one predictor with the other at its fitted optimum): true
(dashed) and fitted (solid), with the fitted optimum u = -b1 / (2 b2) and tolerance t = (-2 b2)^(-1/2).
D: predicted map; AUC computed on 1000 further independent survey cells.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(8)
n = 120


def fractal(H):
    fx = np.fft.fftfreq(n)[:, None]
    fy = np.fft.fftfreq(n)[None, :]
    f = np.sqrt(fx ** 2 + fy ** 2)
    f[0, 0] = 1.0
    amp = f ** (-(H + 1.0))
    amp[0, 0] = 0.0
    z = np.real(np.fft.ifft2(np.fft.fft2(rng.standard_normal((n, n))) * amp))
    return (z - z.min()) / (z.max() - z.min())


elev = 0.2 + 3.0 * fractal(0.8)
T = 24 - 6.5 * elev
Pr = 600 + 1200 * np.linspace(0, 1, n)[None, :] + 400 * (fractal(0.6) - 0.5)


def eta_true(t, p):
    return 2.0 - (t - 14) ** 2 / (2 * 3.0 ** 2) - (p - 1300) ** 2 / (2 * 250.0 ** 2)


pi = 1 / (1 + np.exp(-eta_true(T, Pr)))
mT, sT, mP, sP = T.mean(), T.std(), Pr.mean(), Pr.std()


def design(t, p):
    zt, zp = (t - mT) / sT, (p - mP) / sP
    return np.column_stack([np.ones_like(zt), zt, zt ** 2, zp, zp ** 2])


def survey(k):
    cells = rng.choice(n * n, k, replace=False)
    t, p = T.ravel()[cells], Pr.ravel()[cells]
    y = (rng.random(k) < pi.ravel()[cells]).astype(float)
    return cells, t, p, y


cells, t, p, y = survey(300)
X = design(t, p)
b = np.zeros(X.shape[1])
for _ in range(50):
    mu = 1 / (1 + np.exp(-X @ b))
    W = mu * (1 - mu)
    b = b + np.linalg.solve(X.T @ (W[:, None] * X) + 1e-9 * np.eye(5), X.T @ (y - mu))
pred = 1 / (1 + np.exp(-(design(T.ravel(), Pr.ravel()) @ b))).reshape(n, n)

_, t2, p2, y2 = survey(1000)
s2 = design(t2, p2) @ b
pos, neg = s2[y2 == 1], s2[y2 == 0]
auc = (pos[:, None] > neg[None, :]).mean() + 0.5 * (pos[:, None] == neg[None, :]).mean()

uT = mT - b[1] / (2 * b[2]) * sT
tT = sT / np.sqrt(-2 * b[2])
uP = mP - b[3] / (2 * b[4]) * sP
tP = sP / np.sqrt(-2 * b[4])

fig, ax = bio.canvas(32.0, 11.5)
pa = C.axes_at(ax, (1.0, 1.4, 7.6, 7.6))
im = pa.imshow(pi, cmap="viridis", vmin=0, vmax=1, interpolation="nearest")
r_, c_ = np.unravel_index(cells, (n, n))
pa.scatter(c_[y == 1], r_[y == 1], s=7, c=P.fill("negative"), edgecolors=P.edge("negative"), linewidths=0.5)
pa.scatter(c_[y == 0], r_[y == 0], s=7, facecolors="none", edgecolors="#ffffff", linewidths=0.5)
pa.set_xticks([])
pa.set_yticks([])
bio.panel(ax, "A", (0.2, 11.1))
bio.label(ax, (1.0, 10.7), "True occurrence probability", size="small", bold=True, ha="left")
bio.label(ax, (1.0, 10.0), "300 surveys: filled present, open absent", size="tiny", ha="left")

tt = np.linspace(T.min(), T.max(), 200)
pb = C.axes_at(ax, (10.8, 1.6, 6.0, 7.0))
pb.plot(tt, 1 / (1 + np.exp(-eta_true(tt, 1300))), color=P.muted(), lw=1.3, ls=(0, (4, 2)), label="true")
pb.plot(tt, 1 / (1 + np.exp(-(design(tt, np.full_like(tt, uP)) @ b))), color=Q.line_color("dna"), lw=1.7, label="fitted")
pb.set_ylim(0, 1)
C.style_axes(pb, "mean annual temperature (deg C)", "probability of occurrence")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
pb.text(0.98, 0.9, f"optimum {uT:.1f}\ntolerance {tT:.1f}", transform=pb.transAxes, ha="right", va="top", fontsize=FS["tiny"], color=P.ink())
bio.panel(ax, "B", (9.6, 11.1))
bio.label(ax, (10.8, 10.7), "Response to temperature", size="small", bold=True, ha="left")

pp = np.linspace(Pr.min(), Pr.max(), 200)
pc = C.axes_at(ax, (19.0, 1.6, 6.0, 7.0))
pc.plot(pp, 1 / (1 + np.exp(-eta_true(14, pp))), color=P.muted(), lw=1.3, ls=(0, (4, 2)), label="true")
pc.plot(pp, 1 / (1 + np.exp(-(design(np.full_like(pp, uT), pp) @ b))), color=Q.line_color("plant"), lw=1.7, label="fitted")
pc.set_ylim(0, 1)
C.style_axes(pc, "annual precipitation (mm)", None)
pc.text(0.98, 0.9, f"optimum {uP:.0f}\ntolerance {tP:.0f}", transform=pc.transAxes, ha="right", va="top", fontsize=FS["tiny"], color=P.ink())
bio.panel(ax, "C", (17.8, 11.1))
bio.label(ax, (19.0, 10.7), "Response to precipitation", size="small", bold=True, ha="left")

pd_ = C.axes_at(ax, (26.4, 1.4, 5.6, 5.6))
pd_.imshow(pred, cmap="viridis", vmin=0, vmax=1, interpolation="nearest")
pd_.set_xticks([])
pd_.set_yticks([])
bio.panel(ax, "D", (25.6, 11.1))
bio.label(ax, (26.4, 10.7), "Predicted map", size="small", bold=True, ha="left")
bio.label(ax, (26.4, 10.0), f"AUC on 1000 new surveys = {auc:.2f}", size="tiny", ha="left")
