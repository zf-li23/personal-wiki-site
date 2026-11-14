"""Wind direction from four cosine-tuned giant interneurons (cockroach cercal system).

Four ventral giant interneurons have preferred wind directions at 45, 135, 225 and 315 deg
(0 deg = from the front, clockwise; right side positive) and rectified cosine tuning; each
response carries multiplicative noise (CV 20 %). The population vector sum of preferred
directions weighted by responses recovers the wind direction; the cockroach turns away from it.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(4)
pref = np.radians([45, 135, 225, 315])
names = ["right front", "right rear", "left rear", "left front"]
cols = [P.edge("dna"), P.edge("rna"), P.edge("positive"), P.edge("negative")]
th = np.radians(np.linspace(0, 360, 361))
fig = plt.figure(figsize=(10.5, 3.9))
a = fig.add_subplot(1, 2, 1)
for p, n, c in zip(pref, names, cols):
    r = np.maximum(0, np.cos(th - p))
    a.plot(np.degrees(th), r, color=c, lw=2, label=n)
a.set_xticks([0, 90, 180, 270, 360]); a.set_xticklabels(["front", "right", "rear", "left", "front"])
a.set_xlabel("Wind direction")
a.set_ylabel("Response (normalized)")
a.legend(frameon=False, fontsize=7.5, loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.18))
a.text(0, 0.5, "A", transform=a.transAxes, fontweight="bold", fontsize=11, va="bottom", ha="left",
       position=(-0.12, 1.08))
for s in ("top", "right"):
    a.spines[s].set_visible(False)
b = fig.add_subplot(1, 2, 2)
true = np.radians(np.repeat(np.arange(0, 360, 15), 20))
resp = np.maximum(0, np.cos(true[:, None] - pref[None, :])) * (1 + 0.2 * rng.normal(size=(len(true), 4)))
resp = np.maximum(resp, 0)
vx = (resp * np.sin(pref)).sum(1)
vy = (resp * np.cos(pref)).sum(1)
est = np.arctan2(vx, vy) % (2 * np.pi)
b.plot(np.degrees(true), np.degrees(est), "o", ms=2, color=P.edge("dna"), alpha=0.5)
b.plot([0, 360], [0, 360], color=P.muted(), lw=0.8)
err = np.degrees(np.angle(np.exp(1j * (est - true))))
b.text(10, 330, f"mean absolute error {np.mean(np.abs(err)):.0f}°", fontsize=8, color=P.ink())
b.set_xticks([0, 90, 180, 270, 360]); b.set_yticks([0, 90, 180, 270, 360])
b.set_xlabel("True wind direction / deg"); b.set_ylabel("Population-vector estimate / deg")
b.set_title("B", loc="left", fontweight="bold")
for s in ("top", "right"):
    b.spines[s].set_visible(False)
fig.tight_layout()
