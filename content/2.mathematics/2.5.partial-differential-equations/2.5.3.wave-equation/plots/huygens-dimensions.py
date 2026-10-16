"""Response at distance R to unit initial velocity on a ball (disk, interval) of radius a, in 3D, 2D, 1D."""

import numpy as np
import matplotlib.pyplot as plt

R, a = 3.0, 1.0  # c = 1
t = np.linspace(0.001, 12, 1500)

# 1D: u = (1/2) |(R - t, R + t) intersected with (-a, a)|
u1 = 0.5 * np.clip(np.minimum(R + t, a) - np.maximum(R - t, -a), 0, None)

# 3D: u = (t/2)(1 - cos theta) while the sphere |y - x| = t cuts the ball
cos_th = (t**2 + R**2 - a**2) / (2 * t * R)
u3 = np.where((t > R - a) & (t < R + a), 0.5 * t * (1 - np.clip(cos_th, -1, 1)), 0.0)


def arc(r):
    """Angular measure of the circle of radius r about the observer lying inside the disk."""
    with np.errstate(divide="ignore", invalid="ignore"):
        q = (r**2 + R**2 - a**2) / (2 * r * R)
    return np.where((r > R - a) & (r < R + a), 2 * np.arccos(np.clip(q, -1, 1)), 0.0)


# 2D: u = (1/2 pi) * integral_0^t arc(sqrt(t^2 - w^2)) dw  (substitution w = sqrt(t^2 - r^2))
u2 = np.empty_like(t)
for i, ti in enumerate(t):
    w = np.linspace(0, ti, 2000)
    u2[i] = np.trapezoid(arc(np.sqrt(np.clip(ti**2 - w**2, 0, None))), w) / (2 * np.pi)

fig, axes = plt.subplots(3, 1, figsize=(7.5, 6.5), sharex=True)
for ax, u, name, col in zip(axes, [u3, u2, u1], ["3D (ball)", "2D (disk)", "1D (interval)"], ["C0", "C1", "C2"]):
    ax.plot(t, u, color=col, lw=1.8)
    ax.axvspan(R - a, R + a, color="0.6", alpha=0.15, lw=0)
    ax.set_ylabel("u(x, t)")
    ax.text(0.98, 0.8, name, transform=ax.transAxes, ha="right", fontsize=10)
    ax.set_ylim(bottom=0)
axes[-1].set_xlabel("t")
axes[0].set_title("Signal at distance R = 3 from a source of radius a = 1 (shaded: R - a < t < R + a)")
axes[0].title.set_fontsize(10)
fig.tight_layout()
