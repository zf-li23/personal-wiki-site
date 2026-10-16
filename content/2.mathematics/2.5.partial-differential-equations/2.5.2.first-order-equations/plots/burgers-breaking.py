"""Burgers' equation with u(x, 0) = exp(-x^2): crossing characteristics and wave breaking."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import fsolve


def f(x):
    return np.exp(-x**2)


tstar = np.sqrt(np.e / 2)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.4))

ts = np.array([0.0, 3.0])
for x0 in np.arange(-2.5, 3.01, 0.15):
    ax1.plot(x0 + f(x0) * ts, ts, color="C0", lw=0.8)
ax1.axhline(tstar, color="C3", ls="--", lw=1.2, label="breaking time T* = 1.17")
ax1.set_xlim(-2, 4)
ax1.set_ylim(0, 3)
ax1.set_xlabel("x")
ax1.set_ylabel("t")
ax1.set_title("Characteristics x = x0 + f(x0) t")
ax1.legend(loc="upper left", fontsize=9)


def shock(t):
    """Equal-area rule: find x0 values a < b joined by the shock at time t."""

    def eqs(v):
        a, b = v
        e1 = (a + f(a) * t) - (b + f(b) * t)
        e2 = quad(f, a, b)[0] - 0.5 * (f(a) + f(b)) * (b - a)
        return [e1, e2]

    a, b = fsolve(eqs, [0.0, 2.0])
    return a, b


x0 = np.linspace(-4, 6, 2000)
for i, t in enumerate([0.0, 0.6, tstar, 2.0, 3.0]):
    xs = x0 + f(x0) * t
    if t <= tstar:
        ax2.plot(xs, f(x0), color=f"C{i}", lw=1.8, label=f"t = {t:.2f}")
    else:
        ax2.plot(xs, f(x0), color=f"C{i}", lw=1.0, ls=":")
        a, b = shock(t)
        s, ul, ur = a + f(a) * t, f(a), f(b)
        left = x0 <= a
        ax2.plot(np.where(left, xs, np.nan), np.where(left, f(x0), np.nan), color=f"C{i}", lw=1.8,
                 label=f"t = {t:.2f}")
        right = x0 >= b
        ax2.plot(np.where(right, xs, np.nan), np.where(right, f(x0), np.nan), color=f"C{i}", lw=1.8)
        ax2.plot([s, s], [ur, ul], color=f"C{i}", lw=1.8, ls="--")
ax2.set_xlim(-2, 4)
ax2.set_ylim(0, 1.1)
ax2.set_xlabel("x")
ax2.set_ylabel("u")
ax2.set_title("Profiles: steepening, overturning, shock")
ax2.legend(loc="upper left", fontsize=9)

fig.tight_layout()
