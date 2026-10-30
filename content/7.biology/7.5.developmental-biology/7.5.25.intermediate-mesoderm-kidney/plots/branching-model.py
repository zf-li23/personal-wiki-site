"""Branching-annihilating random walk in 2D: tips move with persistence, branch at random and terminate near ducts."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(3)
dt, v, sig, rb, dkill = 0.1, 1.0, 0.25, 0.12, 0.7
tips = [[0.0, 0.0, 2 * np.pi * k / 3] for k in range(3)]   # x, y, angle
segs, pts, ages = [], [], []
active, dead, times = [], [], []
nd = 0
K = int(2.5 * dkill / (v * dt)) + 1
for step in range(420):
    old = [q for q, g in zip(pts, ages) if g < step - K]
    tree = cKDTree(np.array(old)) if len(old) > 0 else None
    new = []
    for (x, y, a) in tips:
        pts.append((x, y))
        ages.append(step)
        a = a + sig * np.sqrt(dt) * rng.standard_normal()
        x2, y2 = x + v * dt * np.cos(a), y + v * dt * np.sin(a)
        segs.append(((x, y), (x2, y2)))
        if tree is not None and tree.query_ball_point((x2, y2), dkill):
            nd += 1
            continue
        if rng.random() < rb * dt:
            new.append([x2, y2, a + 0.6])
            new.append([x2, y2, a - 0.6])
        else:
            new.append([x2, y2, a])
    tips = new[:4000]
    active.append(len(tips))
    dead.append(nd)
    times.append(step * dt)
    if not tips:
        break
fig, axs = plt.subplots(1, 2, figsize=(10.4, 4.6), gridspec_kw={"width_ratios": [1.1, 1]})
fig.subplots_adjust(left=0.03, right=0.98, bottom=0.13, top=0.9, wspace=0.25)
a = axs[0]
from matplotlib.collections import LineCollection
a.add_collection(LineCollection(segs, colors=charts.line("dna"), linewidths=0.8))
if tips:
    t = np.array(tips)
    a.plot(t[:, 0], t[:, 1], "o", color=charts.line("positive"), ms=2.5)
a.set_aspect("equal")
a.autoscale()
a.axis("off")
charts.title(a, "A  Branching and termination")
b = axs[1]
b.plot(times, active, color=charts.line("positive"), lw=1.6, label="active tips")
b.plot(times, dead, color=charts.line("dna"), lw=1.6, label="terminated tips")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper left")
charts.style_axes(b, "time", "number")
charts.title(b, "B  Tip numbers")
