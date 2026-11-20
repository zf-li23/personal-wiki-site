"""Does an umbrella species protect the others? An overlap analysis in a model landscape.

Landscape: 60 x 60 cells; elevation is a fractal surface (spectral synthesis, H = 0.8) rescaled to 0-1; forest
covers cells where an independent fractal surface exceeds its 30 % quantile. Umbrella species: a forest
species of mid elevations, suitability s_U = forest x exp(-(elev - 0.55)^2 / (2 x 0.12^2)). Its reserve network
is the 15 % of cells with the highest s_U. 200 other species: 150 forest species and 50 species of open
(non-forest) habitat, each with an elevation optimum uniform on [0, 1] and a niche width uniform on
[0.05, 0.2]; the range of a species is the set of cells of its habitat type where its Gaussian suitability
exceeds 0.5.
A: elevation (shading), forest boundary (outline) and the umbrella reserve network (red).
B: fraction of each species' range inside the umbrella network against the difference between its elevation
optimum and the umbrella's; forest species (green), open-habitat species (teal). The dashed line is a
representation target of 30 % of the range.
C: number of species meeting the 30 % target with reserves of the same total area (15 %) chosen for the
umbrella and chosen by a greedy complementarity algorithm: species are taken in order of increasing target
size, and for each the cells of its range that also lie in the ranges of the most species still short of
their targets are added until its target is met or the area is used up.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(23)
n = 60


def fractal(H):
    fx = np.fft.fftfreq(n)[:, None]
    fy = np.fft.fftfreq(n)[None, :]
    f = np.sqrt(fx ** 2 + fy ** 2)
    f[0, 0] = 1.0
    amp = f ** (-(H + 1.0))
    amp[0, 0] = 0.0
    z = np.real(np.fft.ifft2(np.fft.fft2(rng.standard_normal((n, n))) * amp))
    return (z - z.min()) / (z.max() - z.min())


elev = fractal(0.8)
fz = fractal(0.6)
forest = fz > np.quantile(fz, 0.3)
sU = forest * np.exp(-(elev - 0.55) ** 2 / (2 * 0.12 ** 2))
area = int(0.15 * n * n)
umb = np.zeros(n * n, bool)
umb[np.argsort(-sU.ravel())[:area]] = True

nsp = 200
kind = np.array([1] * 150 + [0] * 50)
opt = rng.random(nsp)
wid = rng.uniform(0.05, 0.2, nsp)
R = np.zeros((nsp, n * n), bool)
for i in range(nsp):
    hab = forest if kind[i] else ~forest
    R[i] = (hab & (np.exp(-(elev - opt[i]) ** 2 / (2 * wid[i] ** 2)) > 0.5)).ravel()
keep = R.sum(1) >= 5
R, kind, opt = R[keep], kind[keep], opt[keep]
size = R.sum(1)
frac_umb = (R & umb[None, :]).sum(1) / size

target = np.ceil(0.3 * size)
got = np.zeros(len(size))
sel = np.zeros(n * n, bool)
Rf = R.astype(float)
used = 0
for i in np.argsort(target):
    while got[i] < target[i] and used < area:
        unmet = (got < target).astype(float)
        score = unmet @ Rf
        score[~R[i] | sel] = -1
        j = int(np.argmax(score))
        sel[j] = True
        got += Rf[:, j]
        used += 1
met_umb = int(((R & umb[None, :]).sum(1) >= target).sum())
met_greedy = int((got >= target).sum())

fig, ax = bio.canvas(32.0, 11.0)
pa = C.axes_at(ax, (1.2, 1.4, 8.2, 8.2))
pa.imshow(elev, cmap="Greys", origin="lower", extent=[0, n, 0, n], alpha=0.85)
pa.contour(np.arange(n) + 0.5, np.arange(n) + 0.5, forest.astype(float), levels=[0.5], colors=[Q.line_color("plant")], linewidths=0.8)
pa.contourf(np.arange(n) + 0.5, np.arange(n) + 0.5, umb.reshape(n, n).astype(float), levels=[0.5, 1.5], colors=[P.fill("negative")], alpha=0.75)
pa.set_xticks([])
pa.set_yticks([])
bio.panel(ax, "A", (0.3, 10.7))
bio.label(ax, (1.2, 10.3), "Umbrella reserve network (15 % of area)", size="small", bold=True, ha="left")
bio.label(ax, (1.2, 9.8), "gray: elevation; green outline: forest; red: reserves", size="tiny", ha="left")

pb = C.axes_at(ax, (12.6, 1.6, 9.4, 7.6))
d = opt - 0.55
pb.plot(d[kind == 1], frac_umb[kind == 1], "o", ms=3.5, color=Q.line_color("plant"), alpha=0.8, label="forest species")
pb.plot(d[kind == 0], frac_umb[kind == 0], "s", ms=3.5, color=Q.line_color("enzyme"), alpha=0.8, label="open-habitat species")
pb.axhline(0.3, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.set_ylim(-0.02, 1.0)
C.style_axes(pb, "elevation optimum minus umbrella's", "fraction of range in umbrella reserves")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (11.0, 10.7))
bio.label(ax, (12.6, 10.3), "Coverage depends on similarity to the umbrella", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (26.0, 1.6, 5.2, 7.6))
vals = [met_umb, met_greedy]
for x, v, tok in zip((0, 1), vals, ("negative", "dna")):
    pc.bar(x, v, width=0.6, color=P.light(tok), edgecolor=Q.line_color(tok), lw=0.9)
    pc.text(x, v + 2, str(v), ha="center", fontsize=FS["tiny"], color=P.ink())
pc.axhline(len(size), color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pc.set_xticks([0, 1])
pc.set_xticklabels(["umbrella", "complementarity"])
pc.set_ylim(0, len(size) * 1.1)
C.style_axes(pc, None, "species meeting 30 % target")
bio.panel(ax, "C", (24.2, 10.7))
bio.label(ax, (26.0, 10.3), f"Same area, {len(size)} species", size="small", bold=True, ha="left")
