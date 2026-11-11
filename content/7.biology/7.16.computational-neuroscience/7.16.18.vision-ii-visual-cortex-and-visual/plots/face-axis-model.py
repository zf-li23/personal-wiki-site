"""The axis model of face cells (in the spirit of Chang and Tsao 2017), with synthetic data.

Faces are points x in a 50-dimensional face space (25 shape + 25 appearance dimensions), each
dimension standard normal across faces. Model cell i: r_i = [b + g a_i . x]_+ + noise, with a random
unit preferred axis a_i, b = 20 Hz, g = 8 Hz per SD; trial noise Poisson in a 0.3 s window.
A: response of one cell to faces lying along its preferred axis and along an orthogonal axis.
B: response map of the same cell (axis model) and of an exemplar (Gaussian-tuned) cell in the plane
spanned by the two axes: parallel iso-response lines versus closed contours.
C: linear decoding: 2000 faces, half for fitting a linear map from responses to face features and
half for testing; correlation between true and decoded features against the number of cells.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(5)
d, b, g, T = 50, 20.0, 8.0, 0.3


def axis_cells(n):
    a = rng.normal(size=(n, d))
    return a / np.linalg.norm(a, axis=1, keepdims=True)


fig, axs = plt.subplots(1, 3, figsize=(13, 4.0))
a = axis_cells(1)[0]
o = rng.normal(size=d)
o -= (o @ a) * a
o /= np.linalg.norm(o)
z = np.linspace(-3, 3, 13)
ax = axs[0]
for u, lab, col in ((a, "along preferred axis", P.edge("dna")), (o, "along orthogonal axis", P.edge("rna"))):
    mean = np.maximum(b + g * z * (u @ a), 0)
    trials = rng.poisson(np.repeat(mean[None, :] * T, 8, axis=0)) / T
    ax.errorbar(z, trials.mean(0), yerr=trials.std(0) / np.sqrt(8), fmt="o-", color=col, ms=4, lw=1.4,
                capsize=2, label=lab)
ax.set_xlabel("Distance from average face / SD")
ax.set_ylabel("Firing rate / Hz")
ax.set_ylim(0, 50)
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("A  Ramp along one axis, flat orthogonally", loc="left", fontsize=10)

bx = axs[1]
u1, u2 = np.meshgrid(np.linspace(-3, 3, 121), np.linspace(-3, 3, 121))
axis_map = np.maximum(b + g * u1, 0)
ex_map = 45 * np.exp(-((u1 - 1.5) ** 2 + (u2 - 0.5) ** 2) / (2 * 0.8**2))
c1 = bx.contour(u1, u2, axis_map, levels=[5, 15, 25, 35], colors=P.edge("dna"), linewidths=1.3)
c2 = bx.contour(u1, u2, ex_map, levels=[5, 15, 25, 35], colors=P.edge("rna"), linewidths=1.3)
bx.clabel(c1, fontsize=7, fmt="%d")
bx.clabel(c2, fontsize=7, fmt="%d")
bx.plot([], [], color=P.edge("dna"), label="axis model")
bx.plot([], [], color=P.edge("rna"), label="exemplar model")
bx.set_xlabel("Preferred axis / SD")
bx.set_ylabel("Orthogonal axis / SD")
bx.set_aspect("equal")
bx.legend(frameon=False, fontsize=8, loc="lower left")
bx.set_title("B  Iso-response contours (Hz)", loc="left", fontsize=10)

cx = axs[2]
F = rng.normal(size=(2000, d))
Ns = [10, 25, 50, 100, 200, 400]
Acells = axis_cells(max(Ns))
R = rng.poisson(np.maximum(b + g * F @ Acells.T, 0) * T) / T
corr = []
for n in Ns:
    Xr = np.hstack([R[:, :n], np.ones((2000, 1))])
    W, *_ = np.linalg.lstsq(Xr[:1000], F[:1000], rcond=None)
    Fh = Xr[1000:] @ W
    corr.append(np.mean([np.corrcoef(F[1000:, j], Fh[:, j])[0, 1] for j in range(d)]))
cx.plot(Ns, corr, "o-", color=P.edge("positive"), lw=1.8, ms=5)
cx.set_xscale("log")
cx.set_ylim(0, 1)
cx.set_xlabel("Number of cells")
cx.set_ylabel("Correlation of decoded and true features")
cx.set_title("C  Linear decoding of 50 face dimensions", loc="left", fontsize=10)
fig.tight_layout()
