"""Removal sampling and distance sampling.

A: Leslie regression for a removal study with six successive catches of equal effort: 42, 31, 27, 18, 16, 12
(illustrative data); catch C_i plotted against the number K_i already removed before catch i; the least-squares
line C = p (N - K) meets the K axis at the estimate of N.
B: line-transect distance sampling: 300 simulated detections, perpendicular distances from a half-normal detection
function g(x) = exp(-x^2 / (2 sigma^2)) with sigma = 20 m; histogram scaled to the fitted detection function
(maximum likelihood sigma_hat = sqrt(mean(x^2))); the effective strip half-width is sigma sqrt(pi/2).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
C = np.array([42, 31, 27, 18, 16, 12])
K = np.concatenate([[0], np.cumsum(C)[:-1]])
slope, icpt = np.polyfit(K, C, 1)
Nhat = -icpt / slope

fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.0, 4.5))
ax.plot(K, C, "o", color=P.fill("dna"), mec=P.edge("dna"), ms=7, zorder=5)
kk = np.linspace(0, Nhat, 50)
ax.plot(kk, icpt + slope * kk, color=P.edge("dna"), lw=1.6)
ax.plot([Nhat], [0], "s", color=P.edge("negative"), ms=7)
ax.annotate(f"$\\hat N$ = {Nhat:.0f}", (Nhat, 0), xytext=(-10, 45), textcoords="offset points", fontsize=9, ha="center",
            color=P.edge("negative"), arrowprops=dict(arrowstyle="-", color=P.edge("negative"), lw=0.8))
ax.text(10, 8, f"slope $-\\hat p$ = {slope:.3f}", fontsize=9, color=P.ink())
for i, (k, c) in enumerate(zip(K, C)):
    ax.annotate(f"{i + 1}", (k, c), xytext=(4, 4), textcoords="offset points", fontsize=7.5, color=P.muted())
ax.set_xlim(0, Nhat * 1.08)
ax.set_ylim(0, 48)
ax.set_xlabel("number already removed, $K_i$")
ax.set_ylabel("catch in removal $i$, $C_i$")
ax.set_title("A  Removal sampling: the Leslie regression", loc="left", fontsize=10)

sigma = 20.0
x = []
while len(x) < 300:
    xx = rng.uniform(0, 80)
    if rng.random() < np.exp(-xx ** 2 / (2 * sigma ** 2)):
        x.append(xx)
x = np.array(x)
sh = np.sqrt((x ** 2).mean())
mu = sh * np.sqrt(np.pi / 2)
counts, edges = np.histogram(x, bins=np.arange(0, 85, 5))
dens = counts / (len(x) * 5)
bx.bar(edges[:-1], dens * mu, width=5, align="edge", color=P.fill("plant"), edgecolor=P.edge("plant"), lw=0.8,
       alpha=0.8, label="detections (scaled)")
xs = np.linspace(0, 80, 200)
bx.plot(xs, np.exp(-xs ** 2 / (2 * sh ** 2)), color=P.ink(), lw=1.8, label="fitted $g(x)$, half-normal")
bx.axvline(mu, color=P.edge("negative"), lw=1.2, ls="--")
bx.text(mu + 1.5, 1.0, f"effective half-width\n$\\mu$ = {mu:.1f} m", fontsize=8, color=P.edge("negative"))
bx.set_xlim(0, 80)
bx.set_ylim(0, 1.4)
bx.set_xlabel("perpendicular distance from the transect $x$ / m")
bx.set_ylabel("detection probability $g(x)$")
bx.legend(frameon=False, fontsize=8, loc="upper right")
bx.set_title("B  Distance sampling: the detection function", loc="left", fontsize=10)
for a in (ax, bx):
    for s in ("top", "right"):
        a.spines[s].set_visible(False)
fig.tight_layout()
