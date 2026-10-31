"""Random walks in two dimensions: steps of length a = 1 in a random direction every tau = 1, so
that D = a^2/(4 tau) = 0.25 in each of the two dimensions combined (<r^2> = 4Dt). A: five walks of
1000 steps from the origin. B: mean squared displacement averaged over 2000 walkers (dots) and the
time-averaged MSD of single 1000-step walks (thin lines), compared with <r^2> = 4Dt = N a^2.
C: distribution of the x coordinate after 10 and 400 steps compared with the Gaussian of variance
N a^2/2 predicted by the central limit theorem."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(1)
M, N = 2000, 1000
theta = rng.uniform(0, 2 * np.pi, (M, N))
steps = np.stack([np.cos(theta), np.sin(theta)], axis=-1)
pos = np.concatenate([np.zeros((M, 1, 2)), np.cumsum(steps, axis=1)], axis=1)

fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.4))
fig.subplots_adjust(wspace=0.38, left=0.06, right=0.98, bottom=0.16, top=0.88)
toks = ("dna", "rna", "enzyme", "protein", "blood")

ax = axs[0]
for k, tok in enumerate(toks):
    ax.plot(pos[k, :, 0], pos[k, :, 1], color=charts.line(tok), lw=0.6)
    ax.plot(*pos[k, -1], "o", color=charts.line(tok), ms=3)
ax.plot(0, 0, "o", color=P.ink(), ms=4)
r = np.sqrt(N)
t = np.linspace(0, 2 * np.pi, 200)
ax.plot(r * np.cos(t), r * np.sin(t), color=P.muted(), lw=0.8, ls="--")
ax.text(0.7 * r, -1.05 * r, r"$\sqrt{N}a$", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_aspect("equal")
charts.style_axes(ax, "x / a", "y / a")
charts.title(ax, "A  Five walks, N = 1000")

ax = axs[1]
n = np.arange(N + 1)
msd = (pos ** 2).sum(axis=2).mean(axis=0)
sel = np.unique(np.logspace(0, 3, 25).astype(int))
for k, tok in enumerate(toks[:3]):
    lags = np.arange(1, 300)
    tamsd = [((pos[k, l:] - pos[k, :-l]) ** 2).sum(axis=1).mean() for l in lags]
    ax.plot(lags, tamsd, color=charts.line(tok), lw=0.7, alpha=0.8)
ax.plot(sel, msd[sel], "o", color=charts.line("neutral"), ms=3.5, label="ensemble average")
ax.plot(n[1:], n[1:], color=P.ink(), lw=1.0, label=r"$\langle r^2\rangle = Na^2 = 4Dt$")
ax.set_xscale("log")
ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"steps $N = t/\tau$", r"$\langle r^2\rangle / a^2$")
charts.title(ax, "B  MSD grows linearly")

ax = axs[2]
for Nk, tok in ((10, "rna"), (400, "dna")):
    x = pos[:, Nk, 0] / np.sqrt(Nk)
    ax.hist(x, bins=40, range=(-3, 3), density=True, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.4, alpha=0.7,
            label=f"N = {Nk}")
xs = np.linspace(-3, 3, 200)
ax.plot(xs, np.exp(-xs ** 2) / np.sqrt(np.pi), color=P.ink(), lw=1.2, label="Gaussian, variance 1/2")
ax.set_ylim(0, 0.8)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"$x/(\sqrt{N}a)$", "probability density")
charts.title(ax, "C  Central limit theorem")
