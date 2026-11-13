"""Pinhole eye versus lens eye of the same size: why a lens was worth evolving.

An eye of focal length f (here 10 mm, about the size of the eye of Nautilus) with an aperture of
diameter A. Without a lens every point of the scene illuminates a patch of retina as wide as the
aperture, so the angular blur is the geometric term A/f, plus the diffraction blur lambda/A
(lambda = 0.5 um). The blur is smallest at A* = sqrt(lambda f) (about 0.07 mm), but such a pinhole
admits very little light. With a lens the geometric term disappears; the blur is set by diffraction
and by the angle s/f subtended by one receptor (s = 5 um). The light reaching one receptor grows
as (A/f)^2 in both designs. Nautilus uses pupils of about 0.4-2.8 mm (Land 1981), trading
resolution for light; a lens of the same aperture would sharpen the image by one to two orders of
magnitude.
"""

import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
f, lam, s = 10e-3, 0.5e-6, 5e-6
A = np.logspace(-5, np.log10(5e-3), 300)
deg = 180 / np.pi
pin = np.sqrt((A / f) ** 2 + (lam / A) ** 2) * deg
lens = np.sqrt((lam / A) ** 2 + (s / f) ** 2) * deg
sens = (A / f) ** 2

fig, ax = bio.canvas(24.0, 9.6)
yt = [(0.01, "0.01"), (0.1, "0.1"), (1, "1"), (10, "10")]
pa = quant.Plot(ax, (2.3, 1.5, 8.6, 6.6), xlim=(0.01, 5), ylim=(0.01, 20), xlog=True, ylog=True,
                xlabel="aperture A / mm", ylabel="angular blur Δρ / degrees",
                xticks=[(0.01, "0.01"), (0.1, "0.1"), (1, "1")], yticks=yt)
pa.span(0.4, 2.8, "highlight")
pa.text(1.06, 30, "pupil of", ha="right", color=P.muted())
pa.text(1.1, 30, "Nautilus", ha="left", italic=True, color=P.muted())
pa.line(A * 1e3, pin, "negative", lw=2.0, text="pinhole", at=0.86, dx=-0.2, dy=0.35, ha="right", size="small")
pa.line(A * 1e3, lens, "dna", lw=2.0, text="lens", at=0.86, dx=0.0, dy=-0.4, ha="right", size="small")
astar = np.sqrt(lam * f)
pa.points([astar * 1e3], [np.sqrt(2 * lam / f) * deg], "negative", r=0.09)
pa.text(0.012, 0.13, "optimum pinhole (dot):\nA* = (λf)$^{1/2}$ ≈ 0.07 mm", ha="left")
bio.label(ax, (2.3, 9.05), "A  Blur against aperture (f = 10 mm)", size="small", bold=True, ha="left")

pb = quant.Plot(ax, (13.9, 1.5, 8.6, 6.6), xlim=(1e-6, 0.25), ylim=(0.01, 20), xlog=True, ylog=True,
                xlabel="light per receptor ∝ (A/f)$^2$", ylabel="angular blur Δρ / degrees",
                xticks=[(1e-6, "10$^{-6}$"), (1e-4, "10$^{-4}$"), (1e-2, "10$^{-2}$")], yticks=yt)
pb.span((0.4e-3 / f) ** 2, (2.8e-3 / f) ** 2, "highlight")
pb.text(1.4e-2 / 1.8, 30, "Nautilus", italic=True, color=P.muted())
pb.line(sens, pin, "negative", lw=2.0)
pb.line(sens, lens, "dna", lw=2.0)
pb.legend([("pinhole eye", "negative", "-"), ("lens eye", "dna", "-")], at=(14.5, 2.6), size="small", step=0.5)
bio.label(ax, (13.9, 9.05), "B  The trade-off between sharpness and brightness", size="small", bold=True, ha="left")
