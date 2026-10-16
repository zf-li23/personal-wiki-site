"""Real spherical harmonics on the unit sphere for degrees n = 0, 1, 2, 3."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.special import lpmv

theta = np.linspace(0, np.pi, 61)
phi = np.linspace(0, 2 * np.pi, 121)
TH, PH = np.meshgrid(theta, phi)
X = np.sin(TH) * np.cos(PH)
Y = np.sin(TH) * np.sin(PH)
Z = np.cos(TH)

cases = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (3, 0), (3, 2)]
fig = plt.figure(figsize=(10, 5.4))
for i, (n, m) in enumerate(cases):
    ax = fig.add_subplot(2, 4, i + 1, projection="3d")
    F = lpmv(m, n, np.cos(TH)) * np.cos(m * PH)
    mx = np.max(np.abs(F))
    F = F / mx if mx > 0 else F
    colors = cm.RdBu_r(0.5 + 0.42 * F)
    ax.plot_surface(X, Y, Z, facecolors=colors, rstride=2, cstride=2, linewidth=0, antialiased=False, shade=False)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=20, azim=35)
    ax.set_axis_off()
    ax.set_title(f"n = {n}, m = {m}", fontsize=10)
fig.suptitle("Real spherical harmonics P_n^m(cos theta) cos(m phi): red positive, blue negative")
fig.tight_layout()
