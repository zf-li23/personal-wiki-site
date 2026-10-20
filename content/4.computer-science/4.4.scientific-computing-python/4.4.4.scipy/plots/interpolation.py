"""Interpolating the same data with different methods. Left: step-like data;
the cubic spline overshoots, PCHIP and modified Akima preserve monotonicity.
Right: Runge's function sampled at 11 equispaced points; the degree-10
interpolating polynomial oscillates near the ends, the cubic spline does not."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = np.arange(8.0)
y = np.array([0, 0, 0.1, 0.2, 1, 1, 1, 1.1])
xx = np.linspace(0, 7, 701)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(xx, np.interp(xx, x, y), color="C7", lw=1, label="linear (np.interp)")
ax1.plot(xx, interpolate.CubicSpline(x, y)(xx), color="C3", label="CubicSpline")
ax1.plot(xx, interpolate.PchipInterpolator(x, y)(xx), color="C0", label="PchipInterpolator")
ax1.plot(xx, interpolate.Akima1DInterpolator(x, y, method="makima")(xx), color="C2",
         ls="--", label="Akima (makima)")
ax1.plot(x, y, "ko", ms=5, label="data")
ax1.set_title("step-like data")
ax1.set_xlabel("x")
ax1.legend(fontsize=8)
ax1.grid(alpha=0.3)

def runge(t):
    return 1 / (1 + 25 * t ** 2)

xs = np.linspace(-1, 1, 11)
tt = np.linspace(-1, 1, 801)
poly = np.polynomial.Polynomial.fit(xs, runge(xs), deg=10)
ax2.plot(tt, runge(tt), color="C7", lw=3, alpha=0.5, label="1 / (1 + 25 x^2)")
ax2.plot(tt, poly(tt), color="C3", label="degree-10 polynomial")
ax2.plot(tt, interpolate.CubicSpline(xs, runge(xs))(tt), color="C0", label="CubicSpline")
ax2.plot(xs, runge(xs), "ko", ms=5, label="11 equispaced nodes")
ax2.set_ylim(-0.5, 2.0)
ax2.set_title("Runge's function")
ax2.set_xlabel("x")
ax2.legend(fontsize=8)
ax2.grid(alpha=0.3)
fig.tight_layout()
