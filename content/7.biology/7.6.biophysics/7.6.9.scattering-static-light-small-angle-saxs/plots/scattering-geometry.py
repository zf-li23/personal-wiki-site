# Geometry of elastic scattering and the angular pattern of a small (dipole) scatterer.
# A: a plane wave with wave vector k_i is scattered by two volume elements, at the origin O and at r,
#    towards the detector direction k_s (|k_s| = |k_i| = 2 pi / lambda for elastic scattering). The path
#    difference between the two rays is (s1 - s0) . r, the phase difference q . r with the scattering
#    vector q = k_s - k_i, of length q = 4 pi sin(theta/2) / lambda.
# B: angular distribution (in the scattering plane) of light scattered by a particle much smaller than
#    the wavelength: incident light polarized perpendicular to the scattering plane (isotropic, sin^2 phi = 1),
#    polarized in the plane (cos^2 theta, zero at 90 degrees), and unpolarized ((1 + cos^2 theta) / 2).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P

fig = plt.figure(figsize=(11.5, 4.6))
ax = fig.add_axes([0.02, 0.04, 0.52, 0.86])
ax.set_xlim(-0.6, 10.4)
ax.set_ylim(-1.2, 5.6)
ax.set_aspect("equal")
ax.axis("off")

ink, muted = P.ink(), P.muted()
cin, cout, cq = charts.line("dna"), charts.line("rna"), charts.line("negative")


def vec(a, b, color, lw=1.8, text=None, off=(0, 0), size=9):
    ax.annotate("", xy=b, xytext=a, arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                                    mutation_scale=13, shrinkA=0, shrinkB=0))
    if text:
        mx, my = (a[0] + b[0]) / 2 + off[0], (a[1] + b[1]) / 2 + off[1]
        ax.text(mx, my, text, color=color, fontsize=size, ha="center", va="center")


# incident plane wave: wavefronts and rays
O = np.array([3.0, 0.6])
R = np.array([4.6, 2.3])
for x in np.arange(-0.3, 2.2, 0.45):
    ax.plot([x, x], [-0.3, 3.3], color=P.mix(cin, P.surface(), 0.55), lw=0.9)
for p in (O, R):
    ax.plot([-0.4, p[0]], [p[1], p[1]], color=cin, lw=1.0, ls=(0, (3, 2)))
th = np.radians(32)
s1 = np.array([np.cos(th), np.sin(th)])
for p in (O, R):
    ax.plot([p[0], p[0] + 4.6 * s1[0]], [p[1], p[1] + 4.6 * s1[1]], color=cout, lw=1.0, ls=(0, (3, 2)))
ax.text(9.0, 4.95, "to detector", color=muted, fontsize=8, ha="center")
for p, name in ((O, "O"), (R, "")):
    ax.add_patch(plt.Circle(p, 0.2, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=1.2, zorder=5))
    ax.text(p[0] - 0.05, p[1] - 0.48, name, color=ink, fontsize=9, ha="center", style="italic")
vec(O, R, ink, lw=1.3)
ax.text(3.55, 1.75, "r", color=ink, fontsize=10, weight="bold", style="italic")

# path difference: projections
foot1 = np.array([R[0], O[1]])
ax.plot([R[0], R[0]], [O[1], R[1]], color=muted, lw=0.7, ls=":")
d2 = np.dot(R - O, s1)
foot2 = O + d2 * s1
ax.plot([R[0], foot2[0]], [R[1], foot2[1]], color=muted, lw=0.7, ls=":")
ax.plot([O[0], foot1[0]], [O[1] - 0.06, foot1[1] - 0.06], color=cin, lw=3.2, alpha=0.45, solid_capstyle="butt")
ax.plot([O[0], foot2[0]], [O[1], foot2[1]], color=cout, lw=3.2, alpha=0.45, solid_capstyle="butt")
ax.text(3.8, 0.15, "s0 . r", color=cin, fontsize=8, ha="center")
ax.text(4.0, 1.25, "s1 . r", color=cout, fontsize=8, ha="center", rotation=32)
ax.text(5.3, -0.55, "path difference (s1 - s0) . r,  phase difference q . r", color=ink, fontsize=8.5, ha="center")

# vector triangle q = k_s - k_i
T = np.array([7.4, 0.3])
L = 2.2
ki = np.array([L, 0.0])
ks = L * s1
vec(T, T + ki, cin, text="k_i", off=(0, -0.28))
vec(T, T + ks, cout, text="k_s", off=(-0.3, 0.25))
vec(T + ki, T + ks, cq, lw=2.0, text="q", off=(0.3, 0.1), size=10)
arc = np.linspace(0, th, 30)
ax.plot(T[0] + 0.8 * np.cos(arc), T[1] + 0.8 * np.sin(arc), color=muted, lw=0.8)
ax.text(T[0] + 1.0, T[1] + 0.22, "θ", color=ink, fontsize=9)
ax.text(8.5, 3.1, "|k_i| = |k_s| = 2π/λ\nq = 4π sin(θ/2) / λ", color=ink, fontsize=8.5, ha="center")
ax.text(-0.5, 5.35, "A   Interference of two scattering elements", color=ink, fontsize=9.5, weight="bold")

# B: polar diagrams
pax = fig.add_axes([0.6, 0.1, 0.36, 0.76], projection="polar")
t = np.linspace(0, 2 * np.pi, 721)
curves = (
    (np.ones_like(t), "polarized normal to plane", charts.line("dna"), "-"),
    (np.cos(t) ** 2, "polarized in plane", charts.line("rna"), "--"),
    ((1 + np.cos(t) ** 2) / 2, "unpolarized", charts.line("negative"), "-"),
)
for r, lab, col, ls in curves:
    pax.plot(t, r, color=col, lw=1.8, ls=ls, label=lab)
pax.set_rticks([0.5, 1.0])
pax.set_rlim(0, 1.08)
pax.set_thetagrids([0, 45, 90, 135, 180, 225, 270, 315])
pax.tick_params(colors=muted, labelcolor=ink, labelsize=7)
pax.grid(color=P.mix(muted, P.surface(), 0.55), lw=0.5)
pax.spines["polar"].set_color(muted)
pax.annotate("", xy=(np.pi, 0.0), xytext=(np.pi, 1.0),
             arrowprops=dict(arrowstyle="-|>", color=ink, lw=1.0, mutation_scale=10))
pax.text(np.pi * 1.06, 0.62, "incident", color=ink, fontsize=7.5, ha="center")
pax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=3, fontsize=7, frameon=False)
fig.text(0.6, 0.93, "B   Scattered intensity I(θ) / I(0) of a dipole", color=ink, fontsize=9.5, weight="bold")
