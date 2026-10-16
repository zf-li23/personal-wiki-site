"""Difference of two solutions of y' = y - y^3 with nearby initial values, and the Gronwall bound."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

f = lambda x, y: y - y ** 3
x = np.linspace(0, 10, 600)
s1 = solve_ivp(f, [0, 10], [0.010], t_eval=x, rtol=1e-11, atol=1e-14)
s2 = solve_ivp(f, [0, 10], [0.011], t_eval=x, rtol=1e-11, atol=1e-14)
diff = np.abs(s2.y[0] - s1.y[0])

fig, ax = plt.subplots(figsize=(7, 4.6))
ax.semilogy(x, diff, color="C0", lw=2, label="|phi(x; 0.011) - phi(x; 0.010)|")
ax.semilogy(x, 0.001 * np.exp(2 * x), color="C3", ls="--", lw=1.5, label="Gronwall bound 0.001 e^(2x)")
ax.semilogy(x, 0.001 * np.exp(x), color="0.5", ls=":", lw=1.5, label="0.001 e^x (linearization at y = 0)")
ax.set_ylim(1e-4, 10)
ax.set_xlabel("x")
ax.set_ylabel("difference")
ax.set_title("y' = y - y^3: dependence on the initial value")
ax.legend(loc="lower right", fontsize=8)
fig.tight_layout()
