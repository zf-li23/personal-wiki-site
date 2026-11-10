# Mutual inhibition of the Th1 and Th2 master regulators as a toggle switch (illustrative model).
# x = T-bet activity, y = GATA3 activity (dimensionless):
#   dx/dt = s1 + a / (1 + y^n) - x      s1: Th1-driving input (IL-12 / IFN-gamma through STAT4 / STAT1)
#   dy/dt = s2 + a / (1 + x^n) - y      s2: Th2-driving input (IL-4 through STAT6)
# a = 3, n = 3 (cooperative repression), both regulators decay with rate 1 (time in units of 1/decay rate).
# A: phase plane at s1 = s2 = 0.05: nullclines, stable fixed points, and basins of attraction
#    (initial states integrated to t = 40 and classified by sign of x - y).
# B: hysteresis. s1 is swept up and then down; each step starts from the previous steady state.
#    Two levels of the opposing input s2 show that IL-4 raises the Th1 threshold.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
A, N = 3.0, 3.0


def rhs(x, y, s1, s2):
    return s1 + A / (1 + y ** N) - x, s2 + A / (1 + x ** N) - y


def integrate(x, y, s1, s2, t_end=40.0, dt=0.02):
    for _ in range(int(t_end / dt)):
        dx, dy = rhs(x, y, s1, s2)
        x = x + dt * dx
        y = y + dt * dy
    return x, y


S1 = S2 = 0.05
fig, axs = plt.subplots(1, 2, figsize=(10, 3.8))

# Panel A: basins and nullclines
g = np.linspace(0, 3.4, 90)
X0, Y0 = np.meshgrid(g, g)
Xf, Yf = integrate(X0.copy(), Y0.copy(), S1, S2)
basin = (Xf > Yf).astype(float)
axs[0].contourf(X0, Y0, basin, levels=[-0.5, 0.5, 1.5], colors=[P.fill("protein"), P.fill("enzyme")], alpha=0.55)
yy = np.linspace(0, 3.4, 400)
axs[0].plot(S1 + A / (1 + yy ** N), yy, color=charts.line("enzyme"), lw=1.4)
axs[0].plot(yy, S2 + A / (1 + yy ** N), color=charts.line("protein"), lw=1.4)
rng = np.random.default_rng(0)
for _ in range(10):
    x, y = rng.uniform(0.05, 3.2, 2)
    path = [(x, y)]
    for _ in range(300):
        dx, dy = rhs(x, y, S1, S2)
        x, y = x + 0.04 * dx, y + 0.04 * dy
        path.append((x, y))
    p = np.array(path)
    axs[0].plot(p[:, 0], p[:, 1], color=P.muted(), lw=0.6, alpha=0.8)
fx = integrate(np.array([3.0, 0.2, 1.0]), np.array([0.2, 3.0, 1.0]), S1, S2, t_end=80)
axs[0].plot(fx[0][:2], fx[1][:2], "o", ms=6, color=P.ink())
axs[0].plot(fx[0][2:], fx[1][2:], "o", ms=6, mfc="none", mec=P.ink())
axs[0].text(2.55, 0.45, "Th1\nstate", fontsize=7, color=P.ink(), ha="center")
axs[0].text(0.55, 2.45, "Th2\nstate", fontsize=7, color=P.ink(), ha="center")
axs[0].text(1.3, 1.0, "saddle", fontsize=7, color=P.ink(), ha="left", va="top")
axs[0].set_xlim(0, 3.4)
axs[0].set_ylim(0, 3.4)
charts.style_axes(axs[0], "T-bet activity x", "GATA3 activity y")
charts.title(axs[0], "A")

# Panel B: hysteresis under a sweep of the Th1 input
s_grid = np.linspace(0, 2.2, 56)
for s2, tok in ((0.05, "protein"), (0.6, "negative")):
    x, y = 0.2, 3.0  # start in the Th2 state
    up = []
    for s in s_grid:
        x, y = integrate(x, y, s, s2, t_end=30)
        up.append(x - y)
    down = []
    for s in s_grid[::-1]:
        x, y = integrate(x, y, s, s2, t_end=30)
        down.append(x - y)
    axs[1].plot(s_grid, up, color=charts.line(tok), lw=1.5, label=f"s2 = {s2}, increasing s1")
    axs[1].plot(s_grid[::-1], down, color=charts.line(tok), lw=1.2, ls="--", label=f"s2 = {s2}, decreasing s1")
axs[1].axhline(0, color=P.muted(), lw=0.6, ls=":")
axs[1].legend(frameon=False, fontsize=6.5, labelcolor=P.ink(), loc="upper left")
charts.style_axes(axs[1], "Th1-driving input s1", "x - y (Th1 positive, Th2 negative)")
charts.title(axs[1], "B")
fig.tight_layout()
