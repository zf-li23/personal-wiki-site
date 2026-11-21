"""Predicting extinctions from habitat loss with the species-area relationship.

A: fraction of species predicted to be lost when a fraction h of habitat is destroyed, from S = c A^z:
1 - (1 - h)^z, for z = 0.15, 0.25 and 0.35; and from the countryside species-area relationship (Pereira and
Daily 2006), S = c (A_native + sigma A_converted)^z with z = 0.25, in which converted land (farmland,
plantations) retains an affinity sigma = 0.2 or 0.4 for the species.
B: a simulated region (unit square) with 200 species; abundances lognormal (median 60 individuals, log-sd
1.3, at least 1); each species' individuals are aggregated (Thomas process: about one cluster per 25
individuals, Gaussian spread sd 0.04 around uniformly placed cluster centers, wrapped at the edges). The
species-area curve of nested squares centered in the region is fitted by a power law (z shown). Habitat is
destroyed either as one contiguous block (a strip from the left edge) or as scattered cells (random cells of a
20 x 20 grid). Species lost = species with no individual left in the remaining habitat (means of 20 regions).
The SAR prediction 1 - (1 - h)^z overestimates the loss even for contiguous destruction (a species is lost only
when all its individuals are in the destroyed area, which for aggregated species requires a larger area than the
SAR implies; cf. He and Hubbell 2011), and scattered loss of the same area removes far fewer species, because
the remnants sample the whole region.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(6)

fig, ax = bio.canvas(30.0, 11.0)
pa = C.axes_at(ax, (2.4, 1.6, 10.8, 7.4))
h = np.linspace(0, 1, 201)
for z, tok in ((0.15, "dna"), (0.25, "plant"), (0.35, "negative")):
    pa.plot(h, 1 - (1 - h) ** z, color=Q.line_color(tok), lw=1.6, label=f"S = cA^z, z = {z}")
for sig, ls in ((0.2, (0, (4, 2))), (0.4, (0, (1, 1.5)))):
    pa.plot(h, 1 - (1 - h + sig * h) ** 0.25, color=Q.line_color("plant"), lw=1.3, ls=ls, label=f"countryside SAR, z = 0.25, sigma = {sig}")
for hh in (0.5, 0.9):
    pa.plot([hh, hh], [0, 1 - (1 - hh) ** 0.25], color=P.muted(), lw=0.7, ls=(0, (2, 2)))
    pa.text(hh + 0.01, 1 - (1 - hh) ** 0.25 + 0.02, f"{100 * (1 - (1 - hh) ** 0.25):.0f} %", fontsize=FS["tiny"], color=Q.line_color("plant"))
pa.set_xlim(0, 1)
pa.set_ylim(0, 1)
C.style_axes(pa, "fraction of habitat destroyed h", "fraction of species lost")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.6, 10.6))
bio.label(ax, (2.4, 10.2), "Species-area predictions", size="small", bold=True, ha="left")


def region(nsp=200):
    pts = []
    for _ in range(nsp):
        n = max(1, int(round(60 * np.exp(1.3 * rng.standard_normal()))))
        k = max(1, int(round(n / 25)))
        cent = rng.random((k, 2))
        xy = cent[rng.integers(0, k, n)] + 0.04 * rng.standard_normal((n, 2))
        pts.append(np.mod(xy, 1.0))
    return pts


hs = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95])
cont, scat, zs = [], [], []
for _ in range(20):
    pts = region()
    sides = np.linspace(0.1, 1.0, 10)
    Sa = [sum(np.any(np.all(np.abs(p - 0.5) <= s / 2, axis=1)) for p in pts) for s in sides]
    zs.append(np.polyfit(np.log(sides ** 2), np.log(Sa), 1)[0])
    c_, s_ = [], []
    for hh in hs:
        c_.append(np.mean([not np.any(p[:, 0] >= hh) for p in pts]))
        cells = rng.random((20, 20)) < hh
        s_.append(np.mean([not np.any(~cells[(p[:, 0] * 20).astype(int), (p[:, 1] * 20).astype(int)]) for p in pts]))
    cont.append(c_)
    scat.append(s_)
z = np.mean(zs)
pb = C.axes_at(ax, (17.6, 1.6, 10.8, 7.4))
pb.plot(h, 1 - (1 - h) ** z, color=P.muted(), lw=1.4, ls=(0, (4, 2)), label=f"SAR prediction, fitted z = {z:.2f}")
pb.plot(hs, np.mean(cont, 0), "o-", color=Q.line_color("negative"), lw=1.5, ms=4, label="contiguous loss (one block)")
pb.plot(hs, np.mean(scat, 0), "s-", color=Q.line_color("dna"), lw=1.5, ms=4, label="scattered loss (random cells)")
pb.set_xlim(0, 1)
pb.set_ylim(0, 1)
C.style_axes(pb, "fraction of habitat destroyed h", "fraction of species lost")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (15.8, 10.6))
bio.label(ax, (17.6, 10.2), "The pattern of loss matters", size="small", bold=True, ha="left")
