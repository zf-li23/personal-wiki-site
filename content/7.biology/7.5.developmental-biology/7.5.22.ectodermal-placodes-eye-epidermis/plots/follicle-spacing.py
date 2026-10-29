"""Spacing of skin appendage primordia by an activator-inhibitor mechanism (a Gierer-Meinhardt model standing for
the WNT-DKK system of Sick et al. 2006; Formula 22.5.1), on a field of skin 100 x 80 grid units. Activator and
inhibitor diffuse with a ratio of diffusion coefficients of 25; activator maxima mark placodes. (A) Competence spreads as a front from the left (the dorsal midline), as in chick feather tracts, where rows of
primordia are added one after another; each new row forms in register with the last, giving a fairly regular array.
(B) The whole field becomes competent at once, as in the hair fields of the mouse: spots appear simultaneously,
with irregular packing and a closer spacing, near the fastest-growing wavelength of the linear theory. Such patterns
are multistable, so spacing depends on how the pattern was laid down as well as on the diffusion coefficients and
reaction rates; it does not depend on the size of the field."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT


def lap(u):
    out = np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1) - 4 * u
    out[:, 0] = u[:, 1] - u[:, 0]
    out[:, -1] = u[:, -2] - u[:, -1]
    return out


def run(front, nx=100, ny=80, steps=25000, dt=0.045, seed=0, v=0.08):
    rng = np.random.default_rng(seed)
    Da, Dh, rho, mu, nu, sig = 0.2, 5.0, 1.0, 1.0, 1.4, 0.01
    a = 1 + 0.01 * rng.standard_normal((ny, nx))
    h = np.ones((ny, nx))
    X = np.arange(nx)[None, :]
    for k in range(steps):
        m = (X < 3 + v * k * dt).astype(float) if front else 1.0
        a = a + dt * (Da * lap(a) + m * (rho * a * a / h + sig) - mu * a)
        h = h + dt * (Dh * lap(h) + m * rho * a * a - nu * h)
    return a


A = run(True)
B = run(False, steps=8000)
cmap = LinearSegmentedColormap.from_list("skin", [P_.mix(P_.fill("ectoderm"), P_.surface(), 0.7), P_.edge("ectoderm")])
fig, axs = plt.subplots(1, 2, figsize=(10.0, 4.3))
fig.subplots_adjust(left=0.03, right=0.99, bottom=0.04, top=0.9, wspace=0.06)
for ax, a, title in ((axs[0], A, "A  Competence spreads as a front (feather rows)"), (axs[1], B, "B  Simultaneous (hair field)")):
    ax.imshow(np.clip(a, 0, 4), cmap=cmap, origin="lower", interpolation="bilinear")
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_color(P_.muted())
    charts.title(ax, title)
axs[0].annotate("", xy=(30, -6), xytext=(2, -6), arrowprops=dict(arrowstyle="->", color=P_.ink(), lw=1.0), annotation_clip=False)
