"""Population vector coding of reach direction by cosine-tuned motor cortex neurons.

Each neuron i fires r_i = b + k cos(theta - theta_i) spikes/s (b = 25, k = 20), with Poisson
spike counts in a 0.4 s window. The population vector is
P = sum_i (r_i - b) / k * u_i, where u_i is the unit vector of the preferred direction theta_i.
A: tuning curves of four neurons with their counted rates.
B: one trial per target in a centre-out task (8 targets, N = 60 neurons): weighted preferred
directions (thin) and the population vector (thick).
C: mean absolute angular error of the population vector against the number of neurons.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
b, k, win = 25.0, 20.0, 0.4


def rates(theta, pref):
    return b + k * np.cos(theta - pref)


def popvec(theta, pref):
    counts = rng.poisson(rates(theta, pref) * win)
    w = (counts / win - b) / k
    return w, np.array([np.sum(w * np.cos(pref)), np.sum(w * np.sin(pref))])


fig = plt.figure(figsize=(12, 4.0))
ax = fig.add_subplot(1, 3, 1)
th = np.linspace(0, 2 * np.pi, 361)
cols = [P.edge("dna"), P.edge("rna"), P.edge("enzyme"), P.edge("protein")]
for c, p in zip(cols, (0.3, 1.9, 3.4, 5.0)):
    ax.plot(np.degrees(th), rates(th, p), color=c, lw=1.8)
    td = np.radians(np.arange(0, 360, 45))
    obs = rng.poisson(rates(td, p) * win * 5) / (win * 5)
    ax.plot(np.degrees(td), obs, "o", color=c, ms=4)
ax.set_xlim(0, 360)
ax.set_xticks(range(0, 361, 90))
ax.set_xlabel("Movement direction / deg")
ax.set_ylabel("Firing rate / (spikes/s)")
ax.set_title("A  Cosine tuning", loc="left", fontsize=10)
ax.grid(True, alpha=0.3)

bx = fig.add_subplot(1, 3, 2)
pref = rng.uniform(0, 2 * np.pi, 60)
for j, t in enumerate(np.radians(np.arange(0, 360, 45))):
    c0 = np.array([np.cos(t), np.sin(t)]) * 3.0
    w, pv = popvec(t, pref)
    for wi, pi in zip(w, pref):
        bx.plot([c0[0], c0[0] + 0.35 * wi * np.cos(pi)], [c0[1], c0[1] + 0.35 * wi * np.sin(pi)],
                color=P.muted(), lw=0.6)
    pvn = pv / np.linalg.norm(pv) * 1.0
    bx.annotate("", xy=c0 + pvn, xytext=c0,
                arrowprops=dict(arrowstyle="-|>", color=P.edge("rna"), lw=2))
    bx.plot(*(c0 + np.array([np.cos(t), np.sin(t)]) * 1.0), "x", color=P.edge("dna"), ms=6)
bx.plot(0, 0, "o", color=P.ink(), ms=5)
bx.set_aspect("equal")
bx.set_xlim(-4.6, 4.6)
bx.set_ylim(-4.6, 4.6)
bx.axis("off")
bx.set_title("B  Population vectors (N = 60)", loc="left", fontsize=10)
bx.text(0, -4.5, "x: target direction   arrow: population vector", ha="center", fontsize=8,
        color=P.muted())

cx = fig.add_subplot(1, 3, 3)
ns = np.array([5, 10, 20, 40, 80, 160, 320, 640])
err = []
for n in ns:
    e = []
    for _ in range(300):
        pr = rng.uniform(0, 2 * np.pi, n)
        t = rng.uniform(0, 2 * np.pi)
        _, pv = popvec(t, pr)
        d = np.angle(np.exp(1j * (np.arctan2(pv[1], pv[0]) - t)))
        e.append(abs(np.degrees(d)))
    err.append(np.mean(e))
cx.loglog(ns, err, "o-", color=P.edge("rna"), lw=1.8)
cx.loglog(ns, err[0] * np.sqrt(ns[0] / ns), "--", color=P.muted(), lw=1, label=r"$\propto N^{-1/2}$")
cx.set_xlabel("Number of neurons N")
cx.set_ylabel("Mean angular error / deg")
cx.legend(frameon=False, fontsize=8)
cx.set_title("C  Error falls as more cells vote", loc="left", fontsize=10)
cx.grid(True, which="both", alpha=0.3)
fig.tight_layout()
