"""Kineses in a humidity gradient: where do undirected walkers accumulate?

Walkers move at speed v and reverse/turn at rate lam in a box 0 <= x <= 1 with humidity h(x) = x.
Orthokinesis: speed falls with humidity, v = v0 (1.2 - h).
Klinokinesis without adaptation: constant speed, turning rate depends on the local humidity.
Klinokinesis with adaptation: turning rate depends on the recent change of humidity
(the walker compares now with a moment ago), lam = lam0 exp(-beta dh/dt).
Theory for a velocity-jump process: the stationary density is proportional to 1/v and
independent of a position-dependent turning rate; only the adaptive (temporal) rule biases it.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(1)


def run(mode, n=1500, steps=6000, dt=0.02, v0=0.25, lam0=2.0, beta=2.5):
    x = rng.random(n)
    if mode == "adapt":
        x[:3] = (0.08, 0.15, 0.1)
    y = rng.random(n)
    th = rng.uniform(0, 2 * np.pi, n)
    track = []
    for k in range(steps):
        h = x
        if mode == "ortho":
            v = v0 * (1.2 - h)
            lam = np.full(n, lam0)
        elif mode == "klino":
            v = np.full(n, v0 * 0.7)
            lam = lam0 * (0.3 + 2.0 * (1 - h))
        else:
            v = np.full(n, v0 * 0.7)
            dhdt = v * np.cos(th)
            lam = lam0 * np.exp(-beta * dhdt)
        x = x + v * np.cos(th) * dt
        y = y + v * np.sin(th) * dt
        # reflecting walls
        for arr, ang in ((x, 0), (y, 1)):
            lo = arr < 0
            hi = arr > 1
            arr[lo] = -arr[lo]
            arr[hi] = 2 - arr[hi]
            if ang == 0:
                th[lo | hi] = np.pi - th[lo | hi]
            else:
                th[lo | hi] = -th[lo | hi]
        turn = rng.random(n) < lam * dt
        th[turn] = rng.uniform(0, 2 * np.pi, turn.sum())
        if mode == "adapt" and k < 1500 and k % 3 == 0:
            track.append((x[:3].copy(), y[:3].copy()))
    return x, track


bins = np.linspace(0, 1, 11)
fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.9), gridspec_kw={"width_ratios": [1.25, 1]})
styles = [("ortho", "orthokinesis (speed falls with humidity)", P.edge("dna"), "-"),
          ("klino", "klinokinesis, turning set by local humidity", P.edge("neutral"), "--"),
          ("adapt", "klinokinesis with adaptation (turning set by change)", P.edge("rna"), "-")]
mid = 0.5 * (bins[1:] + bins[:-1])
for mode, lab, col, ls in styles:
    x, track = run(mode)
    hist, _ = np.histogram(x, bins=bins, density=True)
    a.plot(mid, hist, ls, color=col, lw=2, marker="o", ms=4, label=lab)
    if mode == "adapt":
        tr = track
h = np.linspace(0, 1, 100)
theory = 1 / (1.2 - h)
theory /= np.trapezoid(theory, h)
a.plot(h, theory, ":", color=P.muted(), lw=1.2, label="theory for orthokinesis, density ∝ 1/v")
a.axhline(1, color=P.muted(), lw=0.6)
a.set_xlabel("Position in gradient (dry → humid)")
a.set_ylabel("Density of walkers")
a.set_ylim(0, 5.2)
a.legend(frameon=False, fontsize=7.5, loc="upper left")
a.set_title("A", loc="left", fontweight="bold")
# panel B: humidity background and three tracks
b.imshow(np.tile(np.linspace(0, 1, 200), (50, 1)), extent=(0, 1, 0, 1), origin="lower",
         cmap="Blues", alpha=0.35, aspect="auto", vmin=-0.3, vmax=1.4)
xs = np.array([t[0] for t in tr])
ys = np.array([t[1] for t in tr])
for i, col in enumerate((P.edge("rna"), P.edge("dna"))):
    b.plot(xs[:, i], ys[:, i], color=col, lw=1)
    b.plot(xs[-1, i], ys[-1, i], "o", color=col, ms=5)
b.set_xlim(0, 1); b.set_ylim(0, 1)
b.set_xlabel("dry → humid"); b.set_yticks([])
b.set_title("B", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
