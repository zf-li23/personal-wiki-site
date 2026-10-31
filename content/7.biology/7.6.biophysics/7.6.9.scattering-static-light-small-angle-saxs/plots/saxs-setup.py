# Schematic of a solution SAXS experiment (transmission geometry), not to scale.
# X-rays from a synchrotron undulator (or a laboratory source) are monochromatized and collimated by slits;
# the sample flows through a quartz capillary (about 1 mm, 10-50 uL, often directly from a size-exclusion
# column); the scattered rays travel through an evacuated flight tube to a photon-counting area detector,
# while the direct beam is blocked by a beamstop carrying a photodiode (transmitted intensity).
# The isotropic pattern of rings is averaged azimuthally into the one-dimensional curve I(q).
# Numbers: wavelength 1.0 A, sample-detector distance L = 3 m; a beamstop of radius 5 mm and a detector
# edge at 200 mm from the beam give q_min = 0.010 A^-1 and q_max = 0.42 A^-1 through
# q = 4 pi sin(theta/2) / lambda with tan(theta) = radius / L.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Rectangle

import wikibio as bio
from wikibio import charts

P = bio.P
ink, muted = P.ink(), P.muted()
fig = plt.figure(figsize=(12.0, 4.4))
ax = fig.add_axes([0.0, 0.0, 0.74, 1.0])
ax.set_xlim(0, 17.9)
ax.set_ylim(-2.6, 3.6)
ax.set_aspect("equal")
ax.axis("off")
beam = charts.line("negative")

# source
ax.add_patch(FancyBboxPatch((0.2, -0.45), 1.6, 0.9, boxstyle="round,pad=0.05", facecolor=P.fill("neutral"),
                            edgecolor=P.edge("neutral"), lw=1.2))
ax.text(1.0, 0.0, "undulator", ha="center", va="center", fontsize=8, color=P.on_fill())
ax.text(1.0, -0.85, "source", ha="center", fontsize=8, color=ink)
# monochromator and slits
ax.add_patch(Rectangle((2.5, -0.5), 0.25, 1.0, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1))
ax.text(2.62, -0.85, "monochromator", ha="center", fontsize=7.5, color=ink)
for xs in (3.8, 4.8):
    ax.add_patch(Rectangle((xs, 0.12), 0.12, 0.6, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral")))
    ax.add_patch(Rectangle((xs, -0.72), 0.12, 0.6, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral")))
ax.text(4.36, -1.1, "collimating slits", ha="center", fontsize=7.5, color=ink)
ax.plot([1.8, 6.2], [0, 0], color=beam, lw=2.2)
# sample capillary
ax.add_patch(Rectangle((6.05, -0.9), 0.36, 1.8, facecolor=P.light("protein"), edgecolor=P.edge("protein"), lw=1.2))
for k, (yy) in enumerate(np.linspace(-0.7, 0.7, 5)):
    ax.add_patch(Circle((6.23, yy), 0.07, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.6))
ax.annotate("", xy=(6.23, 1.45), xytext=(6.23, 0.95), arrowprops=dict(arrowstyle="<-", color=muted, lw=0.9))
ax.text(6.23, 1.6, "sample flow\n(from SEC column)", ha="center", va="bottom", fontsize=7.5, color=ink)
ax.text(6.23, -1.25, "capillary\n~1 mm", ha="center", va="top", fontsize=7.5, color=ink)
# flight tube
ax.add_patch(Polygon([(6.8, -0.45), (13.6, -2.1), (13.6, 2.1), (6.8, 0.45)], closed=True, facecolor="none",
                     edgecolor=muted, lw=0.9, ls=(0, (4, 2))))
ax.text(10.2, -2.2, "evacuated flight tube, L = 1-5 m", ha="center", fontsize=7.5, color=ink)
ax.plot([6.41, 13.3], [0, 0], color=beam, lw=2.2)
for ang in (6, 12):
    t = np.radians(ang)
    for sgn in (1, -1):
        ax.plot([6.23, 13.8], [0, sgn * 7.57 * np.tan(t)], color=charts.line("dna"), lw=1.0)
ax.add_patch(Circle((13.4, 0), 0.22, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=1.1, zorder=6))
ax.text(13.4, -0.62, "beamstop", ha="center", fontsize=7.5, color=ink)
arc = np.linspace(0, np.radians(12), 30)
ax.plot(6.23 + 2.2 * np.cos(arc), 2.2 * np.sin(arc), color=muted, lw=0.8)
ax.text(8.6, 0.25, "θ", fontsize=9, color=ink)
# detector (side view)
ax.add_patch(Rectangle((13.8, -2.0), 0.3, 4.0, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=1.2))
ax.text(13.95, 2.25, "area detector", ha="center", fontsize=8, color=ink)
# detector face with rings
cx, cy = 15.9, 0.3
for rr, a in zip((0.35, 0.6, 0.9, 1.25), (0.95, 0.7, 0.5, 0.35)):
    ax.add_patch(Circle((cx, cy), rr, facecolor="none", edgecolor=charts.line("dna"), lw=2.4 * a + 0.4))
ax.add_patch(Circle((cx, cy), 0.13, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral")))
ax.add_patch(Rectangle((cx - 1.4, cy - 1.4), 2.8, 2.8, facecolor="none", edgecolor=muted, lw=0.9))
ax.text(cx, cy - 1.75, "isotropic rings", ha="center", fontsize=7.5, color=ink)
ax.annotate("", xy=(cx + 1.95, cy - 2.2), xytext=(cx - 0.4, cy - 2.2),
            arrowprops=dict(arrowstyle="-|>", color=muted, lw=0.8))
ax.text(cx + 0.75, cy - 2.6, "radial average", ha="center", fontsize=7.5, color=ink)

# I(q) inset
iax = fig.add_axes([0.8, 0.2, 0.18, 0.62])
q = np.linspace(0.01, 0.42, 300)
x = q * 18.0
I = (3 * (np.sin(x) - x * np.cos(x)) / x**3) ** 2
iax.semilogy(q, I + 2e-4, color=charts.line("dna"), lw=1.6)
iax.set_xlim(0, 0.42)
charts.style_axes(iax, "q / Å⁻¹", "I(q)  (log)")
iax.set_yticklabels([])
iax.text(0.21, 3e-1, "q_min = 0.010 Å⁻¹\nq_max = 0.42 Å⁻¹\n(λ = 1 Å, L = 3 m)", fontsize=7, color=ink, ha="left",
         va="top")
