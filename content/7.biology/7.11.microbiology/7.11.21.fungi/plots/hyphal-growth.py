"""A: the tip of a septate hypha (ascomycete, schematic). Vesicles carrying wall-synthesizing enzymes travel
along microtubules and actin to the Spitzenkoerper, which feeds them to the apical membrane; the wall is
plastic at the apex and rigidifies behind it. Septa with a central pore, plugged by Woronin bodies after injury,
divide the hypha into compartments. B and C: a model of mycelial growth. Every tip extends at a constant rate
v with a small random change of direction, and a hypha branches (at 45 degrees) when the length it has grown
since its last branch exceeds the hyphal growth unit G. Total length L and tip number N then grow exponentially
at the same rate (about ln 2 · v / G), with L/N close to G, while the colony radius grows linearly.
Illustrative parameters: v = 100 um/h, G = 150 um, seed 0."""
import numpy as np
from matplotlib.patches import Ellipse, Circle, Polygon
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(27, 10.4)

# ---------------- A: hyphal tip
bio.panel(ax, "A", (0.2, 10.2))
y0, r = 5.2, 0.9
xs = np.linspace(0.6, 9.0, 200)
th = np.linspace(-np.pi / 2, np.pi / 2, 60)
tipx, tipy = 9.0 + r * 1.3 * np.cos(th), y0 + r * np.sin(th)
outer = np.r_[np.c_[xs, np.full_like(xs, y0 - r)], np.c_[tipx, tipy], np.c_[xs[::-1], np.full_like(xs, y0 + r)]]
ax.add_patch(Polygon(outer, closed=True, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cell_wall"), lw=3.0, zorder=4))
for sx in (2.0, 5.4):
    ax.plot([sx, sx], [y0 - r, y0 - 0.16], color=P.edge("cell_wall"), lw=3.0, zorder=6)
    ax.plot([sx, sx], [y0 + 0.16, y0 + r], color=P.edge("cell_wall"), lw=3.0, zorder=6)
    for dx in (-0.25, 0.25):
        ax.add_patch(Circle((sx + dx, y0 + 0.45), 0.1, facecolor=P.fill("peroxisome"), edgecolor=P.edge("peroxisome"), lw=0.6, zorder=7))
for nx in (1.1, 3.4, 4.5, 6.8):
    ax.add_patch(Ellipse((nx, y0 - 0.25), 0.7, 0.42, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.9, zorder=6))
for mx in (2.7, 6.1, 7.6):
    bio.mitochondrion(ax, (mx, y0 + 0.4), 0.7, 0.26, zorder=6)
rng = np.random.default_rng(2)
for _ in range(28):
    vx = rng.uniform(6.6, 9.3); vy = y0 + rng.uniform(-0.45, 0.45)
    ax.add_patch(Circle((vx, vy), 0.06, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=0.4, zorder=7))
for _ in range(30):
    a = rng.uniform(0, 2 * np.pi); rr = 0.22 * np.sqrt(rng.uniform())
    ax.add_patch(Circle((9.55 + rr * np.cos(a), y0 + rr * np.sin(a)), 0.05, facecolor=P.edge("vesicle"), edgecolor="none", zorder=8))
ax.plot([6.0, 9.3], [y0 + 0.1, y0 + 0.02], color=P.edge("neutral"), lw=0.8, zorder=5)
ax.plot([6.0, 9.3], [y0 - 0.1, y0 - 0.05], color=P.edge("neutral"), lw=0.8, zorder=5)
bio.callout(ax, (9.55, y0), (10.4, 8.4), "Spitzenkörper")
bio.callout(ax, (8.0, y0 + 0.3), (7.6, 7.4), "secretory vesicles")
bio.callout(ax, (5.4, y0 + 0.05), (4.8, 8.4), "septum with pore")
bio.callout(ax, (2.25, y0 + 0.45), (1.9, 7.4), "Woronin bodies")
bio.callout(ax, (4.5, y0 - 0.3), (3.6, 2.2), "nuclei")
bio.callout(ax, (7.6, y0 + 0.4), (7.4, 2.2), "mitochondrion")
bio.callout(ax, (8.6, y0 - r), (9.8, 2.6), "cell wall (chitin, glucans)")
bio.arrow(ax, (10.6, y0), (11.4, y0), kind="process", head=0.18)
bio.label(ax, (11.0, y0 - 0.5), "growth", size="tiny")

# ---------------- model
v, G, dt, T = 100.0, 150.0, 0.02, 13.0
rs = np.random.default_rng(0)
tips = [[0.0, 0.0, 0.0, 0.0, G]]  # x, y, angle, length since last branch, branching threshold
segs, times, Ls, Ns, Rs = [], [], [], [], []
L = 0.0
t = 0.0
while t < T and len(tips) < 6000:
    new = []
    for tp in tips:
        x, y, a, s, g = tp
        a += rs.normal(0, 0.08)
        nx_, ny_ = x + v * dt * np.cos(a), y + v * dt * np.sin(a)
        segs.append((x, y, nx_, ny_, t))
        L += v * dt
        s += v * dt
        if s > g:
            s, g = 0.0, G * rs.uniform(0.5, 1.5)
            new.append([nx_, ny_, a + (np.pi / 4 if rs.uniform() < 0.5 else -np.pi / 4), 0.0, G * rs.uniform(0.5, 1.5)])
        tp[:] = [nx_, ny_, a, s, g]
    tips += new
    t += dt
    times.append(t); Ls.append(L); Ns.append(len(tips))
    Rs.append(max(np.hypot(p[0], p[1]) for p in tips))
times, Ls, Ns, Rs = map(np.array, (times, Ls, Ns, Rs))

bio.panel(ax, "B", (12.2, 10.2))
cx, cy, sc = 15.8, 5.3, 3.6 / max(Rs.max(), 1)
from matplotlib.collections import LineCollection
S = np.array([sg[:4] for sg in segs]) * sc + np.array([cx, cy, cx, cy])
late = np.array([sg[4] > T - 2.0 for sg in segs])
for m, tok in ((~late, "cell_wall"), (late, "rna")):
    ax.add_collection(LineCollection(S[m].reshape(-1, 2, 2), colors=P.edge(tok), linewidths=0.5, zorder=5))
bio.label(ax, (cx, 0.9), f"mycelium after {T:.0f} h (last 2 h in orange)", size="tiny", color=P.muted())

bio.panel(ax, "C", (19.8, 10.2))
pl = quant.Plot(ax, (21.4, 1.8, 5.2, 7.4), xlim=(0, T), ylim=(1, 1e6), ylog=True, xlabel="time (h)",
                xticks=[0, 4, 8, 12], yticks=[(1, "1"), (100, "10²"), (1e4, "10⁴"), (1e6, "10⁶")])
pl.line(times, Ls, token="cell_wall", lw=1.8, text="length L (µm)", at=0.55)
pl.line(times, Ns, token="rna", lw=1.8, text="tips N", at=0.75)
pl.line(times, Rs, token="dna", lw=1.4, dashed=True, text="radius (µm)", at=0.4)
