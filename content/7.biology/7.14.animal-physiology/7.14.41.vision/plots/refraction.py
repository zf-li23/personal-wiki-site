"""Refractive errors in the reduced eye and the decline of accommodation with age.

A: paraxial ray trace of a reduced eye (one refracting surface of power 60 D, internal index 1.336,
so an emmetropic axial length of 1.336/60 m = 22.3 mm) for a distant object (parallel rays).
Myopic eye: axial length 24.0 mm; hyperopic eye: 20.8 mm (axial ametropia, relaxed accommodation).
Spectacle lenses 12 mm in front of the cornea; their power is computed so the image falls on the retina.
B: amplitude of accommodation versus age, Hofstetter's (1950) minimum, mean and maximum lines
(15 - 0.25 a, 18.5 - 0.3 a, 25 - 0.4 a dioptres), and the corresponding near point of an
emmetrope (100 / A centimetres). Reading at 40 cm needs 2.5 D.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

import wikibio as bio

P = bio.P
n_eye, Pe, vertex = 1.336, 60.0, 0.012


def trace(y0, L, Pl=0.0):
    """Return polyline (x, y) in mm for a ray parallel to the axis at height y0 (mm)."""
    xs, ys = [-30.0], [y0]
    y, u = y0 * 1e-3, 0.0
    if Pl:
        xs.append(-vertex * 1e3)
        ys.append(y * 1e3)
        u = u - y * Pl
        y = y + u * vertex
    xs.append(0.0)
    ys.append(y * 1e3)
    u2 = (u - y * Pe) / n_eye
    y = y + u2 * L
    xs.append(L * 1e3)
    ys.append(y * 1e3)
    return xs, ys


def image_height(L, Pl):
    return trace(1.0, L, Pl)[1][-1]


cases = [("Emmetropia", 0.0223, False), ("Myopia", 0.0240, False), ("Myopia, corrected", 0.0240, True),
         ("Hyperopia", 0.0208, False), ("Hyperopia, corrected", 0.0208, True)]
fig = plt.figure(figsize=(12, 5.2))
gs = fig.add_gridspec(5, 2, width_ratios=[1.25, 1], hspace=0.15)
for k, (name, L, corr) in enumerate(cases):
    ax = fig.add_subplot(gs[k, 0])
    Pl = brentq(lambda p: image_height(L, p), -20, 20) if corr else 0.0
    for y0 in (-1.6, -0.8, 0.8, 1.6):
        xs, ys = trace(y0, L, Pl)
        ax.plot(xs, ys, color=P.edge("highlight"), lw=0.9)
    th = np.linspace(-np.pi / 2, np.pi / 2, 60)
    ax.plot(2.2 * (1 - np.cos(th)) - 2.2 + 0.0, 2.2 * np.sin(th), color=P.edge("dna"), lw=1.6)
    ax.plot([L * 1e3] * 2, [-2.4, 2.4], color=P.edge("rna"), lw=2.2)
    if corr:
        ax.plot([-vertex * 1e3] * 2, [-2.2, 2.2], color=P.edge("enzyme"), lw=2.2)
        ax.text(-vertex * 1e3 - 1, 2.0, f"{Pl:+.1f} D", fontsize=8, ha="right", va="center",
                color=P.edge("enzyme"))
    ax.text(-30, 2.3, name, fontsize=8.5, va="top", color=P.ink())
    ax.set_xlim(-30, 27)
    ax.set_ylim(-2.6, 2.6)
    ax.axis("off")
    if k == 0:
        ax.set_title("A  Distant object, relaxed eye (cornea blue, retina red)", loc="left",
                     fontsize=10)

bx = fig.add_subplot(gs[:, 1])
age = np.linspace(8, 70, 200)
lo, mean, hi = (np.clip(a - b * age, 0, None) for a, b in ((15, 0.25), (18.5, 0.3), (25, 0.4)))
bx.fill_between(age, lo, hi, color=P.fill("dna"), alpha=0.35, lw=0)
bx.plot(age, mean, color=P.edge("dna"), lw=2, label="mean (Hofstetter)")
bx.axhline(2.5, color=P.edge("rna"), lw=1, ls="--")
bx.text(12, 1.2, "2.5 D: reading at 40 cm", fontsize=8, ha="left", color=P.edge("rna"))
bx.set_xlabel("Age / years")
bx.set_ylabel("Amplitude of accommodation / D")
bx.set_ylim(0, 22)
bx.set_xlim(8, 70)
for a in (10, 30, 45, 55):
    A = 18.5 - 0.3 * a
    bx.plot(a, A, "o", color=P.edge("dna"), ms=4)
    bx.text(a + 1, A + 0.6, f"near point {100 / A:.0f} cm", fontsize=7.5, color=P.muted())
bx.legend(frameon=False, fontsize=8, loc="upper right")
bx.set_title("B  Presbyopia: accommodation declines with age", loc="left", fontsize=10)
fig.subplots_adjust(left=0.03, right=0.98, top=0.93, bottom=0.11, wspace=0.18)
