"""Propagation delay of an inverter driving a capacitive load: the delays are
measured between the 50% points of the input and the output; t_PHL and t_PLH
differ because the pull-down and pull-up resistances differ."""

import numpy as np
import matplotlib.pyplot as plt

VDD = 1.0
t = np.linspace(0, 10, 2001)
t_rise, t_fall = 2.0, 6.0
tau_r, tau_f = 0.85, 0.6        # pull-up is weaker than pull-down
edge = 0.3


def ramp(t, t0, up):
    x = np.clip((t - t0) / edge + 0.5, 0, 1)
    return x if up else 1 - x


vin = np.where(t < 4, ramp(t, t_rise, True), ramp(t, t_fall, False))
vout = np.ones_like(t)
fall = t >= t_rise
vout[fall] = np.exp(-(t[fall] - t_rise) / tau_f)
rise = t >= t_fall
v0 = np.exp(-(t_fall - t_rise) / tau_f)
vout[rise] = 1 - (1 - v0) * np.exp(-(t[rise] - t_fall) / tau_r)

t50_fall = t_rise + tau_f * np.log(2)
t50_rise = t_fall + tau_r * np.log(2)

fig, axes = plt.subplots(2, 1, figsize=(8, 4.6), sharex=True)
for ax, y, name in ((axes[0], vin, "input A"), (axes[1], vout, "output Y")):
    ax.plot(t, y, color="C0" if name.startswith("in") else "C1", lw=2)
    ax.axhline(0.5, color="gray", lw=0.8, ls=":")
    ax.set_ylabel(name)
    ax.set_yticks([0, 0.5, 1])
    ax.set_yticklabels(["0", "50%", "VDD"])
    ax.set_ylim(-0.1, 1.15)
for tt in (t_rise, t_fall):
    for ax in axes:
        ax.axvline(tt, color="gray", lw=0.8, ls="--")
for tt in (t50_fall, t50_rise):
    axes[1].axvline(tt, color="gray", lw=0.8, ls="--")
axes[1].annotate("", xy=(t50_fall, 0.75), xytext=(t_rise, 0.75),
                 arrowprops=dict(arrowstyle="<->", lw=1))
axes[1].text(t50_fall + 0.15, 0.75, r"$t_{\mathrm{PHL}}$", ha="left", va="center", fontsize=10)
axes[1].annotate("", xy=(t50_rise, 0.25), xytext=(t_fall, 0.25),
                 arrowprops=dict(arrowstyle="<->", lw=1))
axes[1].text(t50_rise + 0.15, 0.25, r"$t_{\mathrm{PLH}}$", ha="left", va="center", fontsize=10)
axes[1].set_xlabel("time (arbitrary units)")
fig.tight_layout()
