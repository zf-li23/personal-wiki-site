# Phase contrast of a weak phase object: the same field of particles imaged under different conditions.
# The specimen is a field of 300 x 300 pixels (2 A per pixel) containing six copies of a toy complex
# (a ring of seven Gaussian subunits around a central one, 120 A across) in random orientations; its
# projected potential phi(r) is scaled so that the largest phase shift sigma*phi is 0.1 rad. Images are
# I = 1 + 2 F^-1[F[sigma phi] CTF] (weak-phase-object approximation, 300 kV, Cs = 2.7 mm, A = 0.07,
# envelope B = 100 A^2). Panels: projected potential; in focus (only amplitude contrast: almost no
# contrast); underfocus 1 um and 3 um (particles dark on a light background, with fringes); an ideal phase
# plate at 0.3 um underfocus (strong, nearly faithful contrast); and the 2 um image recorded with
# 25 electrons per square angstrom (Poisson shot noise), which is what a real micrograph looks like.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(1)
lam, Cs, A, B = 0.019687, 2.7e7, 0.07, 100.0
n, px = 300, 2.0
y, x = np.mgrid[0:n, 0:n] * px


def particle(cx, cy, ang):
    out = np.zeros((n, n))
    pts = [(0.0, 0.0, 1.2)] + [(45 * np.cos(ang + 2 * np.pi * j / 7), 45 * np.sin(ang + 2 * np.pi * j / 7), 1.0)
                               for j in range(7)]
    pts += [(28 * np.cos(ang + 0.3), 28 * np.sin(ang + 0.3), 0.6)]
    for dx, dy, w in pts:
        out += w * np.exp(-((x - cx - dx) ** 2 + (y - cy - dy) ** 2) / (2 * 11.0**2))
    return out


phi = np.zeros((n, n))
centers = [(120, 130), (330, 110), (480, 160), (150, 400), (360, 330), (470, 470)]
for cx, cy in centers:
    phi += particle(cx, cy, rng.uniform(0, 2 * np.pi))
phi = 0.1 * phi / phi.max()

f = np.fft.fftfreq(n, d=px)
KX, KY = np.meshgrid(f, f)
K2 = KX**2 + KY**2


def image(df, phase=0.0):
    c = np.pi * lam * df * K2 - 0.5 * np.pi * Cs * lam**3 * K2**2 + phase
    h = -(np.sqrt(1 - A**2) * np.sin(c) + A * np.cos(c)) * np.exp(-B * K2 / 4)
    return 1 + 2 * np.real(np.fft.ifft2(np.fft.fft2(phi) * h))


panels = [("Projected potential σφ", phi, None),
          ("In focus", image(0.0), None),
          ("Δf = 1 µm", image(1.0e4), None),
          ("Δf = 3 µm", image(3.0e4), None),
          ("Phase plate, Δf = 0.3 µm", image(0.3e4, np.pi / 2), None),
          ("Δf = 2 µm, 25 e⁻/Å²", None, 2.0e4)]
fig, axs = plt.subplots(2, 3, figsize=(10.5, 7.4))
ref = image(3.0e4)
span = np.percentile(np.abs(ref - 1), 99.5)
for ax, (name, img, dfn) in zip(axs.ravel(), panels):
    if dfn is not None:
        dose = 25 * px * px
        img = rng.poisson(dose * np.clip(image(dfn), 0, None)) / dose
        lo, hi = np.percentile(img, (0.5, 99.5))
    elif img is phi:
        lo, hi = 0, phi.max()
    else:
        lo, hi = 1 - span, 1 + span
    ax.imshow(img, cmap="gray", vmin=lo, vmax=hi, origin="lower", interpolation="nearest")
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_color(P.muted())
    charts.title(ax, name)
axs[0, 0].plot([20, 70], [15, 15], color="white", lw=3)
axs[0, 0].text(45, 25, "100 Å", color="white", ha="center", fontsize=7)
fig.tight_layout()
