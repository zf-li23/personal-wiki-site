"""Comparison bounds for y' = x^2 + y^2, y(0) = 0 (blow-up near x = 2.003)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def big(x, y):
    return y[0] - 60.0


big.terminal = True
sol = solve_ivp(lambda x, y: [x * x + y[0] ** 2], [0, 3], [0.0], events=big,
                rtol=1e-10, atol=1e-12, dense_output=True)
xe = sol.t[-1]
x = np.linspace(0, xe, 800)
y = sol.sol(x)[0]

x1 = 1.25
xu = np.linspace(0, x1, 400)  # the bound holds on [0, x1]
upper = x1 * np.tan(x1 * xu)

y_at_1 = sol.sol(1.0)[0]
xstar = 1 + np.pi / 2 - np.arctan(y_at_1)
xl = np.linspace(1, xstar - 1e-3, 400)
lower = np.tan(xl - 1 + np.arctan(y_at_1))

fig, ax = plt.subplots(figsize=(7, 4.8))
ax.plot(x, y, color="k", lw=2.4, alpha=0.8, label="solution of y' = x^2 + y^2")
ax.plot(xu, upper, color="C0", lw=1.6, label="upper bound 1.25 tan(1.25 x)")
ax.plot(xl, lower, color="C1", lw=1.6, label="lower bound tan(x - 1 + arctan y(1))")
ax.axvline(np.sqrt(np.pi / 2), color="C0", ls="--", lw=1)
ax.axvline(1 + np.pi / 2 - np.arctan(1 / 3), color="C1", ls="--", lw=1)
ax.set_xlim(0, 2.4)
ax.set_ylim(0, 12)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Second comparison theorem: bounds on the blow-up point")
ax.legend(loc="upper left", fontsize=9)
fig.tight_layout()
