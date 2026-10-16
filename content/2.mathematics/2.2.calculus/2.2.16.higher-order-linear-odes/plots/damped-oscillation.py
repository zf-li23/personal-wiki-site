"""Free damped oscillation x'' + 2k x' + w^2 x = 0, w = 1, x(0) = 1, x'(0) = 0."""

import numpy as np
import matplotlib.pyplot as plt

w = 1.0
t = np.linspace(0, 20, 1000)


def solve(k):
    if k < w:  # underdamped
        wd = np.sqrt(w**2 - k**2)
        return np.exp(-k * t) * (np.cos(wd * t) + k / wd * np.sin(wd * t))
    if k == w:  # critically damped
        return (1 + w * t) * np.exp(-w * t)
    s = np.sqrt(k**2 - w**2)  # overdamped
    l1, l2 = -k + s, -k - s
    c1 = -l2 / (l1 - l2)
    c2 = l1 / (l1 - l2)
    return c1 * np.exp(l1 * t) + c2 * np.exp(l2 * t)


fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(t, solve(0.15), color="C0", lw=1.8, label="underdamped, k = 0.15")
env = np.exp(-0.15 * t) / np.sqrt(1 - 0.15**2)
ax.plot(t, env, color="C0", lw=0.9, ls="--")
ax.plot(t, -env, color="C0", lw=0.9, ls="--")
ax.plot(t, solve(1.0), color="C3", lw=2, label="critically damped, k = 1")
ax.plot(t, solve(2.5), color="C2", lw=2, label="overdamped, k = 2.5")
ax.axhline(0, color="0.5", lw=0.8)
ax.set_xlabel("t")
ax.set_ylabel("x(t)")
ax.set_xlim(0, 20)
ax.set_title("x'' + 2k x' + x = 0,  x(0) = 1, x'(0) = 0")
ax.legend(loc="upper right")
fig.tight_layout()
