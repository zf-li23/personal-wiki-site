"""Stochastic branching of the pancreatic epithelium as a branching-annihilating random walk (Algorithm
30.8.1). A: a tree grown in two dimensions from one tip: tips advance with persistent random turning, split in two
at a constant rate, and stop (terminate) when they come within a fixed distance of an existing duct; active tips
are gold, terminated tips red. B: the number of active tips rises exponentially at first; once the tree becomes
crowded, tips terminate as fast as new ones are made inside, only tips at the advancing front keep branching, and
the number of terminated tips rises to match the active ones: termination by crowding balances branching, so the tree fills space
uniformly without any global instruction. Such a process
describes lineage-traced clones in the developing mouse pancreas (and kidney and mammary gland), in which
progenitors at the tips are fate-restricted and branching and termination are random."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from scipy.spatial import cKDTree
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(4)
v, rb, Ra, th, noise, T, lag = 1.0, 0.12, 1.6, np.radians(40), 0.2, 150, 4
P = np.zeros((1, 2))
B = np.zeros(1, int)
tp = np.zeros((1, 2))
ta = np.array([np.pi / 2])
segs, dead, t_act, t_dead = [], [], [], []
for step in range(1, T + 1):
    ta = ta + noise * rng.standard_normal(len(ta))
    q = tp + v * np.c_[np.cos(ta), np.sin(ta)]
    old = P[B < step - lag]
    if len(old):
        d, _ = cKDTree(old).query(q)
        alive = d >= Ra
    else:
        alive = np.ones(len(q), bool)
    dead += list(q[~alive])
    for p0, p1 in zip(tp[alive], q[alive]):
        segs.append((p0, p1, step))
    tp, ta, q = tp[alive], ta[alive], q[alive]
    P = np.vstack([P, q])
    B = np.r_[B, np.full(len(q), step)]
    br = rng.random(len(q)) < rb
    tp = np.vstack([q[~br], q[br], q[br]])
    ta = np.r_[ta[~br], ta[br] + th, ta[br] - th]
    t_act.append(len(tp))
    t_dead.append(len(dead))
    if len(tp) > 220:
        break
tips = [(p_, None) for p_ in tp]
fig, (a, b) = plt.subplots(1, 2, figsize=(10.2, 4.4), gridspec_kw={"width_ratios": [1.2, 1]})
fig.subplots_adjust(left=0.02, right=0.97, bottom=0.14, top=0.9, wspace=0.18)
a.add_collection(LineCollection([[p, q] for p, q, _ in segs], colors=charts.line("k"), linewidths=0.9, capstyle="round"))
a.autoscale()
if dead:
    d = np.array(dead)
    a.plot(d[:, 0], d[:, 1], "o", ms=1.8, color=charts.line("negative"))
if tips:
    e = np.array([p for p, _ in tips])
    a.plot(e[:, 0], e[:, 1], "o", ms=2.4, color=charts.line("atp"))
a.set_aspect("equal")
a.set_axis_off()
charts.title(a, "A  Branching and annihilation")
ts = np.arange(1, len(t_act) + 1)
b.plot(ts, t_act, color=charts.line("atp"), lw=1.8, label="active tips")
b.plot(ts, t_dead, color=charts.line("negative"), lw=1.8, label="terminated tips")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper left")
charts.style_axes(b, "time (steps)", "number of tips")
charts.title(b, "B  Termination catches up with branching")
