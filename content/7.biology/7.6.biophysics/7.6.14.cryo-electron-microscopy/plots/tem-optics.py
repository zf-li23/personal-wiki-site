# The transmission electron microscope and Abbe's theory of image formation.
# A: the column of a cryo-TEM from the gun to the detector (schematic, not to scale): field-emission gun,
#    condenser lenses C1-C2 with the condenser aperture, the cryo-specimen at liquid-nitrogen temperature,
#    the objective lens with the objective aperture in its back focal plane, the selected-area aperture in
#    the first image plane, intermediate and projector lenses, energy filter and direct electron detector.
# B: ray diagram of an ideal thin lens (object distance U = 3, focal length f = 2, image distance V = 6,
#    magnification -2). Rays leaving three object points in the same direction (same colour) meet at one
#    point of the back focal plane, whose height f tan(theta) depends only on the direction: the back focal
#    plane holds the Fourier transform (diffraction pattern) of the exit wave. Rays from the same object
#    point meet again in the image plane. A second Fourier transform (propagation from the back focal plane
#    to the image) restores the image.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
ink, muted = P.ink(), P.muted()

fig, ax = bio.canvas(25, 12)

# --- A: column ---------------------------------------------------------------------------------
bio.panel(ax, "A", (0.3, 11.5))
cx = 3.6
parts = [
    (10.6, "gun", "Field-emission gun", "highlight"),
    (9.5, "lens", "Condenser lenses C1, C2", "channel"),
    (8.6, "ap", "Condenser aperture", None),
    (7.8, "spec", "Specimen (vitreous ice, ~ -180 °C)", "dna"),
    (7.0, "lens", "Objective lens", "channel"),
    (6.3, "ap", "Objective aperture (back focal plane)", None),
    (5.5, "ap", "Selected-area aperture (image plane)", None),
    (4.6, "lens", "Intermediate lens", "channel"),
    (3.6, "lens", "Projector lens", "channel"),
    (2.6, "box", "Energy filter (zero-loss slit)", "neutral"),
    (1.4, "det", "Direct electron detector", "receptor"),
]
ax.plot([cx, cx], [1.4, 10.6], color=muted, lw=0.8, ls=(0, (2, 2)), zorder=1)
for y, kind, text, tok in parts:
    if kind == "gun":
        bio.shape(ax, [(cx - 0.45, y + 0.35), (cx + 0.45, y + 0.35), (cx, y - 0.35)], token=tok)
    elif kind == "lens":
        for s in (-1, 1):
            bio.box(ax, (cx + s * 0.75, y), 0.7, 0.42, token=tok, radius=0.08)
    elif kind == "ap":
        for s in (-1, 1):
            ax.plot([cx + s * 0.12, cx + s * 0.9], [y, y], color=ink, lw=2.2, solid_capstyle="butt")
    elif kind == "spec":
        bio.box(ax, (cx, y), 1.2, 0.18, token=tok, radius=0.03)
    elif kind == "box":
        bio.box(ax, (cx, y), 1.6, 0.5, token=tok, radius=0.08)
    elif kind == "det":
        bio.box(ax, (cx, y), 2.0, 0.35, token=tok, radius=0.05)
    bio.label(ax, (cx + 1.35, y), text, size="small", ha="left")
# beam envelope
yy = np.linspace(1.6, 10.3, 200)
w = 0.08 + 0.25 * np.abs(np.sin((yy - 1.6) / 8.7 * 3.0 * np.pi)) * (yy > 2.0)
ax.fill_betweenx(yy, cx - w, cx + w, color=P.light("highlight"), zorder=2, lw=0)
bio.label(ax, (cx - 1.2, 9.2), "e⁻ beam", size="small", ha="right", color=muted)
bio.label(ax, (cx - 1.2, 4.0), "imaging\nsystem", size="small", ha="right", color=muted)
bio.label(ax, (cx - 1.2, 7.8), "300 kV", size="small", ha="right", color=muted)

# --- B: Abbe ray diagram -------------------------------------------------------------------------
bio.panel(ax, "B", (11.6, 11.5))
x0, scale, yc = 12.2, 1.25, 6.0
U, f = 3.0, 2.0
V = 1 / (1 / f - 1 / U)
L = U
X = lambda x: x0 + x * scale          # noqa: E731
Y = lambda y: yc + y * scale          # noqa: E731
cols = [charts.line("dna"), charts.line("positive"), charts.line("negative")]
slopes = [0.38, 0.0, -0.38]
for y0 in (-0.6, 0.0, 0.6):
    for s, col in zip(slopes, cols):
        yl = y0 + s * U
        s2 = s - yl / f
        yi = yl + s2 * V
        ax.plot([X(0), X(L), X(L + V)], [Y(y0), Y(yl), Y(yi)], color=col, lw=1.0, alpha=0.85, zorder=4)
# planes and lens
for xp, name in ((0, "object plane\n(exit wave ψ(r))"), (L + f, "back focal plane\nΨ(k) = F[ψ]"),
                 (L + V, "image plane\nψ(r / M), M < 0")):
    ax.plot([X(xp), X(xp)], [Y(-2.6), Y(2.6)], color=muted, lw=1.0, ls=(0, (3, 2)), zorder=3)
    bio.label(ax, (X(xp), Y(-3.3)), name, size="small")
lens = bio.blob((X(L), Y(0)), 0.22, 2.9 * scale, wobble=0.0)
bio.shape(ax, lens, token="channel", zorder=3)
bio.label(ax, (X(L), Y(3.25)), "objective lens", size="small")
for s, col in zip(slopes, cols):
    ax.plot(X(L + f), Y(s * f), "o", color=col, ms=5, zorder=6)
bio.label(ax, (X(L + f) + 0.3, Y(2.2)), "one point\nper direction", size="tiny", ha="left", color=muted)
ax.annotate("", xy=(X(0), Y(-2.1)), xytext=(X(L), Y(-2.1)),
            arrowprops=dict(arrowstyle="<->", color=muted, lw=0.8))
bio.label(ax, (X(L / 2), Y(-1.85)), "U", size="small", color=muted)
ax.annotate("", xy=(X(L), Y(-2.1)), xytext=(X(L + f), Y(-2.1)),
            arrowprops=dict(arrowstyle="<->", color=muted, lw=0.8))
bio.label(ax, (X(L + f / 2), Y(-1.85)), "f", size="small", color=muted)
bio.label(ax, (X(L + V / 2), Y(2.9)), "1/U + 1/V = 1/f,  M = −V/U", size="small", color=muted)
