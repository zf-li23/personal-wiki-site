"""Geometry of one-way ANOVA: y, its projection onto the model space and onto the span of the ones vector."""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7.5, 6))
ax = fig.add_subplot(projection="3d")

# Coordinates: e1 along omega (the ones direction), e2 along Omega minus omega, e3 residual direction.
O = np.array([0.0, 0.0, 0.0])
ybar1 = np.array([3.0, 0.0, 0.0])
yhat = np.array([3.0, 2.0, 0.0])
y = np.array([3.0, 2.0, 1.6])

# The plane Omega (spanned by e1 and e2)
xx, yy = np.meshgrid(np.linspace(-0.5, 4.5, 2), np.linspace(-0.5, 3.0, 2))
ax.plot_surface(xx, yy, 0 * xx, alpha=0.15, color="C0")
ax.plot([-0.5, 4.5], [0, 0], [0, 0], color="C0", lw=1.5)
ax.text(4.5, -0.3, 0, "omega = span{1}", color="C0")
ax.text(0.0, 2.9, 0, "Omega (model space)", color="C0")


def seg(p, q, **kw):
    ax.plot([p[0], q[0]], [p[1], q[1]], [p[2], q[2]], **kw)


seg(O, y, color="k", lw=2)
seg(O, yhat, color="gray", lw=1, ls=":")
seg(ybar1, y, color="C1", lw=2.5, label="y - ybar..1   (SS_T)")
seg(ybar1, yhat, color="C2", lw=2.5, label="yhat - ybar..1   (SS_Tr, a - 1 df)")
seg(yhat, y, color="C3", lw=2.5, label="y - yhat   (SS_E, N - a df)")
for p, name in [(O, "O"), (ybar1, "ybar.. 1"), (yhat, "yhat"), (y, "y")]:
    ax.scatter(*p, color="k", s=15)
    ax.text(p[0] + 0.08, p[1] + 0.08, p[2] + 0.08, name)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_box_aspect((4.5, 3.5, 2.2))
ax.view_init(elev=22, azim=-60)
ax.legend(loc="upper left", frameon=False)
ax.set_title("Orthogonal decomposition: SS_T = SS_Tr + SS_E")
fig.tight_layout()
