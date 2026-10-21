"""Wavefronts emitted by a source moving to the right: subsonic and supersonic."""

import numpy as np
import matplotlib.pyplot as plt

u = 1.0
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.4))
th = np.linspace(0, 2 * np.pi, 300)

for ax, ma in zip(axes, [0.6, 2.0]):
    vs = ma * u
    t_now = 6.0
    for te in np.arange(0, t_now, 0.75):
        r = u * (t_now - te)
        xe = vs * te
        ax.plot(xe + r * np.cos(th), r * np.sin(th), color="C0", lw=1.0)
        ax.plot([xe], [0], ".", color="0.5", ms=3)
    xs = vs * t_now
    ax.plot([xs], [0], "o", color="C3", ms=6)
    ax.annotate("", xy=(xs + 1.2, 0), xytext=(xs, 0), arrowprops=dict(arrowstyle="->", color="C3", lw=1.5))
    if ma > 1:
        alpha = np.arcsin(1 / ma)
        lgt = 10.0
        for sgn in [1, -1]:
            ax.plot([xs, xs - lgt * np.cos(alpha)], [0, sgn * lgt * np.sin(alpha)], color="C1", lw=1.6)
        ax.text(xs - 3.2, 0.35, "α", fontsize=11)
        ax.set_title("Ma = 2: Mach cone, sin α = 1/Ma")
    else:
        ax.set_title("Ma = 0.6: wavefronts crowd ahead")
    ax.set_aspect("equal")
    ax.set_xlim(-6.5, max(vs * t_now + 2.0, 6.5))
    ax.set_ylim(-6.5, 6.5)
    ax.set_xticks([])
    ax.set_yticks([])

fig.tight_layout()
