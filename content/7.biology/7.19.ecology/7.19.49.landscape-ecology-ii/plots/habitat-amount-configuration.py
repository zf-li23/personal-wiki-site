"""Habitat amount and configuration in a lattice metapopulation.

Landscape: an 80 x 80 periodic grid in which a proportion h of the cells is habitat, either placed at
random or clumped (a spectrally synthesized fractal surface, H = 0.5, thresholded at its h-quantile).
Population: each habitat cell is occupied or empty (a contact process). An occupied cell becomes empty
at rate e = 1; an empty habitat cell is colonized at rate (lambda / 4) k, where k is the number of its four
neighbors that are occupied; propagules landing on non-habitat cells are lost. lambda = 3. Simulated in
steps dt = 0.1 from full occupancy for t = 120; occupancy is averaged over t = 80-120 and over 4 landscapes.
A: equilibrium proportion of the habitat that is occupied against habitat amount h, for random and
clumped habitat, with the mean-field (Levins) prediction 1 - e / (lambda h) for comparison. The mean field
ignores configuration; with local dispersal the random landscape loses the population well above the
mean-field threshold, near the habitat amount at which habitat stops percolating, whereas clumped
habitat of the same amount supports it.
B, C: snapshots at h = 0.45 (random: extinct or nearly so; clumped: persisting). Gray: habitat; green:
occupied.
"""

import numpy as np
from matplotlib.colors import ListedColormap

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(11)
L, dt, lam = 80, 0.1, 3.0


def fractal(H=0.5):
    fx = np.fft.fftfreq(L)[:, None]
    fy = np.fft.fftfreq(L)[None, :]
    f = np.sqrt(fx ** 2 + fy ** 2)
    f[0, 0] = 1.0
    amp = f ** (-(H + 1.0))
    amp[0, 0] = 0.0
    return np.real(np.fft.ifft2(np.fft.fft2(rng.standard_normal((L, L))) * amp))


def landscape(h, kind):
    if kind == "random":
        return rng.random((L, L)) < h
    z = fractal()
    return z < np.quantile(z, h)


def run(hab, T=120.0, tavg=80.0):
    s = hab.copy()
    pd = 1 - np.exp(-dt)
    acc = []
    for i in range(int(T / dt)):
        k = (np.roll(s, 1, 0).astype(int) + np.roll(s, -1, 0) + np.roll(s, 1, 1) + np.roll(s, -1, 1))
        pb = 1 - np.exp(-lam * dt * k / 4)
        r = rng.random((L, L))
        s = np.where(s, r > pd, (r < pb) & hab)
        if i * dt >= tavg:
            acc.append(s.sum() / hab.sum())
    return s, np.mean(acc)


hs = np.array([0.30, 0.40, 0.50, 0.55, 0.60, 0.65, 0.70, 0.80, 1.0])
res = {}
for kind in ("random", "clumped"):
    res[kind] = [np.mean([run(landscape(h, kind))[1] for _ in range(4)]) for h in hs]

fig, ax = bio.canvas(32.0, 10.5)
pa = C.axes_at(ax, (2.4, 1.6, 11.5, 7.2))
hh = np.linspace(0.3, 1.0, 200)
pa.plot(hh, np.maximum(1 - 1 / (lam * hh), 0), color=P.muted(), lw=1.2, ls=(0, (4, 2)), label="mean field (Levins)")
pa.plot(hs, res["random"], "o-", color=Q.line_color("plant"), lw=1.5, ms=4, label="random habitat")
pa.plot(hs, res["clumped"], "s-", color=Q.line_color("negative"), lw=1.5, ms=4, label="clumped habitat")
pa.set_xlim(0.28, 1.02)
pa.set_ylim(-0.02, 0.8)
C.style_axes(pa, "habitat amount h (proportion of cells)", "proportion of habitat occupied")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.6, 10.1))
bio.label(ax, (2.4, 9.7), "Same amount, different configuration", size="small", bold=True, ha="left")

cmap = ListedColormap([P.surface(), P.mix(P.muted(), P.surface(), 0.55), P.edge("plant")])
for j, kind in enumerate(("random", "clumped")):
    hab = landscape(0.45, kind)
    s, occ = run(hab)
    img = hab.astype(int) + s.astype(int)
    x0 = 17.0 + 7.6 * j
    pb = C.axes_at(ax, (x0, 1.6, 6.6, 6.6))
    pb.imshow(img, cmap=cmap, vmin=0, vmax=2, interpolation="nearest")
    pb.set_xticks([])
    pb.set_yticks([])
    for sp in pb.spines.values():
        sp.set_color(P.muted())
    bio.panel(ax, "BC"[j], (x0 - 0.8, 10.1))
    bio.label(ax, (x0, 9.7), f"h = 0.45, {kind}", size="small", bold=True, ha="left")
    bio.label(ax, (x0, 8.9), f"occupancy {occ:.2f}", size="tiny", ha="left")
