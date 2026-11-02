"""Numerical solution of ordinary differential equations. A: the error at t = 1 of the Euler method,
Heun's method (second-order Runge-Kutta) and the classical fourth-order Runge-Kutta method for
dx/dt = a - b x (a = 20, b = 2, x(0) = 5) against the step size h, on logarithmic axes; the slopes
are the orders 1, 2 and 4. B: Euler solutions of the same equation with three step sizes; for
h b > 2 the iteration diverges although the true solution relaxes to a/b = 10. C: the Lotka-Volterra
system x' = x(1 - 0.1 y), y' = y(-1.5 + 0.075 x) from (10, 5) for 50 time units: the exact orbit is
closed (a level curve of the first integral), the Euler solution with h = 0.01 spirals outward,
the fourth-order Runge-Kutta solution with h = 0.1 stays on the orbit."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
a, b, c = 20.0, 2.0, 5.0
f1 = lambda x: a - b * x
exact = lambda t: a / b - (a / b - c) * np.exp(-b * t)


def integrate(f, x0, h, n, method):
    xs = [np.asarray(x0, float)]
    x = xs[0]
    for _ in range(n):
        if method == "euler":
            x = x + h * f(x)
        elif method == "heun":
            k1 = f(x)
            x = x + h / 2 * (k1 + f(x + h * k1))
        else:
            k1 = f(x); k2 = f(x + h / 2 * k1); k3 = f(x + h / 2 * k2); k4 = f(x + h * k3)
            x = x + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        xs.append(x)
    return np.array(xs)


hs = 0.4 / 2.0 ** np.arange(0, 9)
methods = [("euler", "Euler (order 1)", "negative"), ("heun", "Heun (order 2)", "highlight"),
           ("rk4", "RK4 (order 4)", "positive")]
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(11, 3.5))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.86, wspace=0.38)
for m, name, tok in methods:
    err = [abs(integrate(f1, c, h, round(1 / h), m)[-1] - exact(1.0)) for h in hs]
    ax1.loglog(hs, err, "o-", ms=3, color=charts.line(tok), lw=1.3, label=name)
ax1.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax1, "step size h", "error at t = 1")
charts.title(ax1, "A  Order of accuracy")

tt = np.linspace(0, 6, 300)
for h, tok in [(0.05, "positive"), (0.9, "highlight"), (1.1, "negative")]:
    n = round(6 / h)
    ax2.plot(np.arange(n + 1) * h, integrate(f1, c, h, n, "euler"), "o-" if h > 0.5 else "-", ms=2.5,
             lw=1 if h > 0.5 else 2.4, color=charts.line(tok), label=f"Euler, h = {h}")
ax2.plot(tt, exact(tt), color=P.ink(), lw=1, ls="--", label="exact")
ax2.set_ylim(-15, 35)
ax2.legend(fontsize=7, frameon=False, loc="upper left", ncol=2)
charts.style_axes(ax2, "t", "x")
charts.title(ax2, "B  Stability of the Euler method")

al, be, ga, de = 1.0, 0.1, 1.5, 0.075
flv = lambda z: np.array([z[0] * (al - be * z[1]), z[1] * (-ga + de * z[0])])
z0 = np.array([10.0, 5.0])
ref = integrate(flv, z0, 0.002, round(5.6 / 0.002), "rk4")
eu = integrate(flv, z0, 0.01, 5000, "euler")
rk = integrate(flv, z0, 0.1, 500, "rk4")
ax3.plot(eu[:, 0], eu[:, 1], color=charts.line("negative"), lw=0.8, label="Euler, h = 0.01")
ax3.plot(rk[:, 0], rk[:, 1], color=charts.line("positive"), lw=2.4, alpha=0.7, label="RK4, h = 0.1")
ax3.plot(ref[:, 0], ref[:, 1], color=P.ink(), lw=0.9, ls="--", label="exact orbit")
ax3.plot(*z0, "o", color=P.ink(), ms=3)
ax3.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax3, "prey x", "predator y")
charts.title(ax3, "C  Lotka-Volterra, t = 0 to 50")
