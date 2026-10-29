"""Selection of a single neural precursor from a proneural cluster by lateral inhibition (the Delta-Notch model of
Collier et al. 1996, Formula 19.5.1, on a hexagonal sheet of cells). Cells of the cluster (outlined) express
proneural genes and can make Delta, with competence highest in the centre; the surrounding cells make a low, constant level of
Delta and cannot be selected. Each cell's Notch activity n rises with the mean Delta of its six neighbours, and high Notch
represses its own Delta d. Starting from small random differences (left), feedback amplifies them; the central cell
wins, keeps high Delta and low Notch and becomes the neuroblast or sensory organ precursor, and its neighbours are
inhibited (middle). Right: Delta levels of all cluster cells over time; the winner is drawn in bold."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
nx, ny = 11, 9
cells = [(i, j) for j in range(ny) for i in range(nx)]
xy = np.array([(i + 0.5 * (j % 2), j * np.sqrt(3) / 2) for i, j in cells])
idx = {c: k for k, c in enumerate(cells)}


def neighbours(i, j):
    if j % 2 == 0:
        d = [(-1, 0), (1, 0), (-1, -1), (0, -1), (-1, 1), (0, 1)]
    else:
        d = [(-1, 0), (1, 0), (0, -1), (1, -1), (0, 1), (1, 1)]
    return [idx[(i + a, j + b)] for a, b in d if (i + a, j + b) in idx]


nb = [neighbours(i, j) for i, j in cells]
centre = xy[idx[(5, 4)]]
r = np.hypot(*(xy - centre).T)
cluster = r < 1.1
comp = np.where(cluster, 1.0 - 0.15 * r, 0.0)
d_out = 0.3                 # surrounding cells make a constant, low level of Delta

a_, b_, k_, h_, v = 0.01, 100.0, 2, 2, 1.0
n = 0.5 + 0.02 * rng.standard_normal(len(cells))
d = np.where(cluster, 0.5 + 0.05 * rng.standard_normal(len(cells)), d_out)
d0 = d.copy()
dt, T = 0.02, 30.0
trace = []
for step in range(int(T / dt)):
    dm = np.array([d[m].mean() for m in nb])
    n += dt * (dm ** k_ / (a_ + dm ** k_) - n)
    d += dt * v * (comp / (1 + b_ * n ** h_) - d)
    d[~cluster] = d_out
    if step % 10 == 0:
        trace.append(d[cluster].copy())
trace = np.array(trace)

fig = plt.figure(figsize=(11.0, 3.8))
axs = [fig.add_axes([0.0, 0.05, 0.3, 0.85]), fig.add_axes([0.31, 0.05, 0.3, 0.85]), fig.add_axes([0.69, 0.16, 0.29, 0.72])]


def sheet(ax, dv, title):
    vmax = 1.0
    for k, (x, y) in enumerate(xy):
        t = float(np.clip(dv[k] / vmax, 0, 1))
        face = P_.mix(P_.light("protein"), P_.edge("negative"), t) if cluster[k] else P_.light("neutral")
        ax.add_patch(RegularPolygon((x, y), 6, radius=0.56, orientation=0, facecolor=face,
                                    edgecolor=P_.edge("protein") if cluster[k] else P_.edge("neutral"), lw=1.2 if cluster[k] else 0.5))
    ax.set_xlim(-0.8, nx + 0.3)
    ax.set_ylim(-0.8, ny * 0.87 + 0.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=FT["small"], color=P_.ink(), loc="left", weight="bold")


sheet(axs[0], d0, "A  Start: small differences")
sheet(axs[1], d, "B  Final: one precursor")
win = np.argmax(trace[-1])
tt = np.arange(len(trace)) * 10 * dt
for k in range(trace.shape[1]):
    axs[2].plot(tt, trace[:, k], color=charts.line("negative") if k == win else P_.muted(), lw=2.0 if k == win else 0.7)
charts.style_axes(axs[2], "time", "Delta level")
charts.title(axs[2], "C  Delta in the cluster")
