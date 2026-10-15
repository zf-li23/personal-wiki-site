import numpy as np
import matplotlib.pyplot as plt

# Folium of Descartes x^3 + y^3 - 3 a x y = 0 with a = 1
a = 1.0
g = np.linspace(-2.5, 2.5, 801)
X, Y = np.meshgrid(g, g)
F = X**3 + Y**3 - 3 * a * X * Y

fig, ax = plt.subplots(figsize=(6.5, 6))
ax.contour(X, Y, F, levels=[0], colors="tab:blue", linewidths=2)
ax.plot([], [], color="tab:blue", lw=2, label="x^3 + y^3 = 3xy")

# Points with F_y = 3y^2 - 3ax = 0 on the curve: y^2 = a x, x^3 + y^3 = 3 a x y
# Besides the origin: x = 4^(1/3) a, y = 2^(1/3) a (vertical tangent)
xv, yv = 4 ** (1 / 3) * a, 2 ** (1 / 3) * a
ax.plot([0, xv], [0, yv], "s", color="tab:orange", ms=8, label="F_y = 0 (theorem fails)")
ax.plot([xv, xv], [yv - 0.6, yv + 0.6], "--", color="tab:orange", lw=1)

# Local maximum of the implicit function y(x): x = 2^(1/3) a, y = 4^(1/3) a
xm, ym = 2 ** (1 / 3) * a, 4 ** (1 / 3) * a
ax.plot([xm], [ym], "o", color="tab:red", ms=8, label="local maximum of y(x)")
ax.plot([xm - 0.6, xm + 0.6], [ym, ym], "--", color="tab:red", lw=1)

# Asymptote x + y + a = 0
ax.plot(g, -g - a, ":", color="gray", lw=1, label="asymptote x + y + 1 = 0")
ax.axhline(0, color="gray", lw=0.6)
ax.axvline(0, color="gray", lw=0.6)
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Folium of Descartes (a = 1)")
ax.legend(loc="lower left", fontsize=8)
fig.tight_layout()
