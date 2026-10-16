"""Characteristics and transported profiles for u_t + u_x = 0 and u_t + x u_x = 0."""

import numpy as np
import matplotlib.pyplot as plt


def bump(x):
    return np.exp(-4 * (x - 1.0) ** 2)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.4))
x = np.linspace(-1, 6, 800)
times = [0, 1, 2]
scale = 0.6  # vertical scale of the profiles drawn in the (x, t)-plane

# constant speed c = 1
for x0 in np.arange(-3, 6.01, 0.5):
    ax1.plot([x0, x0 + 2.5], [0, 2.5], color="0.65", lw=0.8)
for i, t in enumerate(times):
    ax1.plot(x, t + scale * bump(x - t), color=f"C{i}", lw=1.8, label=f"u(x, {t})")
ax1.set_xlim(-1, 5)
ax1.set_ylim(0, 2.8)
ax1.set_xlabel("x")
ax1.set_ylabel("t")
ax1.set_title("u_t + u_x = 0: lines x - t = const")
ax1.legend(loc="upper left", fontsize=9)

# speed a(x, t) = x
ts = np.linspace(0, 2.5, 200)
for x0 in np.arange(0.1, 2.01, 0.15):
    ax2.plot(x0 * np.exp(ts), ts, color="0.65", lw=0.8)
for i, t in enumerate(times):
    ax2.plot(x, t + scale * bump(x * np.exp(-t)), color=f"C{i}", lw=1.8, label=f"u(x, {t})")
ax2.set_xlim(-1, 5)
ax2.set_ylim(0, 2.8)
ax2.set_xlabel("x")
ax2.set_ylabel("t")
ax2.set_title("u_t + x u_x = 0: curves x = x0 exp(t)")
ax2.legend(loc="upper left", fontsize=9)

fig.tight_layout()
