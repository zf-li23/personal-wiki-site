"""Graphite furnace temperature program (drying, pyrolysis, atomization, cleaning) and the
transient absorbance during atomization. Lower panel: the tube wall heats at about
2000 C/s, a L'vov platform heated mainly by radiation lags behind, so the analyte leaves
the platform later, into a gas that is already near its final temperature."""

import numpy as np
import matplotlib.pyplot as plt

# step program: (target C, ramp s, hold s)
steps = [(110, 10, 20), (800, 10, 20), (2300, 0.0, 4), (2600, 1, 3)]
names = ["drying", "pyrolysis", "atomize", "clean"]
t, T = [0.0], [25.0]
bounds = []
for target, ramp, hold in steps:
    t0 = t[-1]
    if ramp > 0:
        t.append(t0 + ramp)
        T.append(target)
    else:
        t.append(t0 + 1.0)  # maximum-power heating, about 1 s
        T.append(target)
    t.append(t[-1] + hold)
    T.append(target)
    bounds.append((t0, t[-1]))

fig, axes = plt.subplots(2, 1, figsize=(7.5, 6.4))
ax = axes[0]
ax.plot(t, T, color="k", lw=1.8)
for (a, b), name in zip(bounds, names):
    ax.axvspan(a, b, color="0.9" if names.index(name) % 2 == 0 else "0.97", lw=0)
    ypos = 2750 if name != "clean" else 1900
    ax.text((a + b) / 2, ypos, name, ha="center", fontsize=8)
ax.set_ylim(0, 2950)
ax.set_xlim(0, t[-1])
ax.set_xlabel("time / s")
ax.set_ylabel(r"temperature / $^\circ$C")
ax.set_title("Temperature program (Ar flow stopped during atomization)", fontsize=10)

ax = axes[1]
tt = np.linspace(0, 4, 2000)
T0, Ta = 800.0, 2300.0
wall = Ta - (Ta - T0) * np.exp(-tt / 0.35)
tau1, tau2 = 0.8, 0.35  # radiative heating of the platform: a two-stage lag
platform = Ta - (Ta - T0) * (tau1 * np.exp(-tt / tau1) - tau2 * np.exp(-tt / tau2)) / (tau1 - tau2)


def signal(Ts, Tapp=1500.0, width=60.0, tau=0.35):
    released = 1 / (1 + np.exp(-(Ts - Tapp) / width))
    rate = np.gradient(released, tt)
    dt = tt[1] - tt[0]
    kernel = np.exp(-tt / tau)
    return np.convolve(rate, kernel)[: len(tt)] * dt


aw, ap = signal(wall), signal(platform)
scale = 0.35 / max(aw.max(), ap.max())
ax2 = ax.twinx()
ax.plot(tt, wall, color="0.5", lw=1.3, ls="--", label="tube wall temperature")
ax.plot(tt, platform, color="0.5", lw=1.3, ls=":", label="platform temperature")
ax2.plot(tt, aw * scale, color="C0", lw=1.8, label="absorbance, wall atomization")
ax2.plot(tt, ap * scale, color="C3", lw=1.8, label="absorbance, platform atomization")
ax.set_xlabel("time after start of atomization / s")
ax.set_ylabel(r"temperature / $^\circ$C")
ax2.set_ylabel("absorbance")
ax.set_ylim(700, 2500)
ax2.set_ylim(0, 0.45)
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, fontsize=8, frameon=False, loc="lower right")
ax.set_title("Atomization step: transient signals (illustrative)", fontsize=10)
fig.tight_layout()
