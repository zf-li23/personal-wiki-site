"""Hopf bifurcation of the Brusselator (a = 1): extrema of x on the attractor and the
oscillation period versus b; the linear prediction 2 pi / a holds at the Hopf point b_c = 2."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

a = 1.0
bc = 1 + a * a


def rhs(t, u, b):
    x, y = u
    return [a - (b + 1) * x + x * x * y, b * x - x * x * y]


bs = np.linspace(1.2, 4.0, 57)
xmax, xmin, period = [], [], []
for b in bs:
    sol = solve_ivp(rhs, (0, 300), [a + 0.1, b / a], args=(b,), max_step=0.05, rtol=1e-8, atol=1e-10)
    m = sol.t > 220
    x = sol.y[0][m]
    t = sol.t[m]
    xmax.append(x.max())
    xmin.append(x.min())
    if x.max() - x.min() > 1e-3:
        # period from successive upward crossings of the mean
        c = x - x.mean()
        idx = np.where((c[:-1] < 0) & (c[1:] >= 0))[0]
        tc = t[idx] - c[idx] * (t[idx + 1] - t[idx]) / (c[idx + 1] - c[idx])
        period.append(np.mean(np.diff(tc)))
    else:
        period.append(np.nan)

fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))
ax = axes[0]
ax.plot(bs, xmax, color="C0", lw=2, label="max x")
ax.plot(bs, xmin, color="C1", lw=2, label="min x")
ax.axhline(a, color="0.5", ls="--", lw=1, label="steady state x = a")
ax.axvline(bc, color="C3", ls=":", lw=1.5)
ax.text(bc + 0.05, 3.6, "Hopf point\nb = 1 + a²", color="C3")
ax.set_xlabel("b")
ax.set_ylabel("x on the attractor")
ax.set_title("bifurcation diagram (a = 1)")
ax.legend(loc="upper left")

ax = axes[1]
ax.plot(bs, period, "o-", color="C0", ms=3)
ax.axhline(2 * np.pi / a, color="0.5", ls="--", lw=1, label="2π/a (linear theory)")
ax.axvline(bc, color="C3", ls=":", lw=1.5)
ax.set_xlabel("b")
ax.set_ylabel("period")
ax.set_title("period of the limit cycle")
ax.legend(loc="upper left")
fig.tight_layout()
