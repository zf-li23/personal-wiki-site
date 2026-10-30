"""The fastest region of the heart tube becomes its pacemaker (Formula 28.4.1). A chain of 80 FitzHugh-Nagumo
cells from the venous pole (sinus venosus, x = 0) to the arterial pole, whose intrinsic rate falls along the tube
(epsilon from 0.10 to 0.05). A: beating frequency of each cell, uncoupled (each beats at its own rate) and coupled
through gap junctions (D = 1): the whole tube beats at nearly the rate of the fastest, inflow end. B: membrane
variable v of the coupled chain in space and time: each beat starts at the venous pole and travels to the arterial
pole as a wave, the slow peristaltic contraction of the early tube."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
n, a, b, I = 80, 0.7, 0.8, 0.5
eps = np.linspace(0.10, 0.05, n)


def run(D, T=900.0, dt=0.04, keep=False):
    v = -1.0 + 0.1 * np.random.default_rng(1).standard_normal(n)
    w = -0.5 * np.ones(n)
    steps = int(T / dt)
    first = np.full(n, np.nan)
    last = np.full(n, np.nan)
    cnt = np.zeros(n)
    above = v > 1.0
    rec = []
    for k in range(steps):
        lap = np.zeros(n)
        lap[1:-1] = v[2:] - 2 * v[1:-1] + v[:-2]
        lap[0] = v[1] - v[0]
        lap[-1] = v[-2] - v[-1]
        v, w = v + dt * (v - v**3 / 3 - w + I + D * lap), w + dt * eps * (v + a - b * w)
        now = v > 1.0
        up = now & ~above
        if k * dt > 300 and up.any():
            tt = k * dt
            first[up & np.isnan(first)] = tt
            last[up] = tt
            cnt[up] += 1
        above = now
        if keep and k % 10 == 0 and k * dt > 600:
            rec.append(v.copy())
    return (cnt - 1) / (last - first), np.array(rec)


f0, _ = run(0.0)
f1, R = run(1.0, keep=True)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.4, 3.8))
fig.subplots_adjust(left=0.08, right=0.97, bottom=0.16, top=0.88, wspace=0.28)
x = np.arange(n)
ax1.plot(x, 1000 * f0, color=charts.line("neutral"), lw=1.6, label="uncoupled (intrinsic rate)")
ax1.plot(x, 1000 * f1, color=charts.line("muscle"), lw=1.9, label="coupled, D = 1")
ax1.set_ylim(0, 1000 * f0.max() * 1.25)
ax1.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="lower left")
charts.style_axes(ax1, "position (venous pole 0, arterial pole 79)", "beats per 1000 time units")
charts.title(ax1, "A  Entrainment by the fastest region")
t = 600 + 0.4 * np.arange(len(R))
ax2.imshow(R.T, aspect="auto", origin="lower", extent=(t[0], t[-1], 0, n - 1), cmap="magma" if P_.is_dark() else "Reds",
           vmin=-2, vmax=2)
charts.style_axes(ax2, "time", "position")
charts.title(ax2, "B  Waves start at the venous pole")
