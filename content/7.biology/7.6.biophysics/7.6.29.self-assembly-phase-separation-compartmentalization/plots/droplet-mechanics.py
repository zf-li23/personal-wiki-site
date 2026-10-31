"""Mechanics of liquid condensates. A: fusion of two touching spherical droplets of radius R: the aspect
ratio (long axis over short axis) relaxes from 2 to 1 roughly exponentially, with the visco-capillary
time tau = eta R / gamma (curves for R = 0.5, 1 and 2 um at eta/gamma = 1 s/um). B: tau against
droplet radius for inverse capillary velocities eta/gamma from 0.1 to 1000 s/um, the range spanned by
protein droplets in vitro, P granules and nucleoli (order-of-magnitude, illustrative): measuring tau for
droplets of several sizes and fitting a line through the origin gives eta/gamma. C: micropipette
aspiration: at the threshold where the aspirated tongue becomes a hemisphere of the pipette radius
R_p, the suction pressure is Delta p = 2 gamma (1/R_p - 1/R_d); synthetic measurements on droplets of
radius R_d = 10 um with three pipettes, fitted to recover gamma = 1 uN/m. D: wetting of one
condensate phase (1) by another (2) in the nucleoplasm (0): complete engulfment when
gamma_01 > gamma_02 + gamma_12, partial engulfment when no tension exceeds the sum of the other two,
separate droplets when gamma_12 > gamma_01 + gamma_02."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig = plt.figure(figsize=(11.4, 3.2))
gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1, 1.5], wspace=0.45, left=0.05, right=0.99, bottom=0.17, top=0.87)

ax = fig.add_subplot(gs[0])
t = np.linspace(0, 6, 300)
for R, tok in [(0.5, "dna"), (1.0, "bacterium"), (2.0, "blood")]:
    tau = 1.0 * R
    ax.plot(t, 1 + np.exp(-t / tau), color=charts.line(tok), lw=1.6, label=rf"$R = {R:g}\ \mu\mathrm{{m}}$")
ax.set_ylim(0.95, 2.05)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "time / s", "aspect ratio")
charts.title(ax, "A  Fusion")

ax = fig.add_subplot(gs[1])
R = np.logspace(-1, 1, 50)
for ratio, tok in [(0.1, "dna"), (1.0, "bacterium"), (10.0, "blood"), (1000.0, "neutral")]:
    ax.loglog(R, ratio * R, color=charts.line(tok), lw=1.6, label=rf"$\eta/\gamma = {ratio:g}\ \mathrm{{s\,\mu m^{{-1}}}}$")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"droplet radius $R$ / $\mu$m", r"fusion time $\tau$ / s")
charts.title(ax, "B  Visco-capillary scaling")

ax = fig.add_subplot(gs[2])
gamma = 1.0e-6
Rd = 10e-6
Rp = np.array([1.5e-6, 2.5e-6, 4e-6])
xv = 1 / Rp - 1 / Rd
rng = np.random.default_rng(0)
dp = 2 * gamma * xv * (1 + 0.06 * rng.standard_normal(3))
xx = np.linspace(0, 7e5, 50)
slope = np.sum(dp * xv) / np.sum(xv ** 2)
ax.plot(xv / 1e6, dp, "o", color=charts.line("protein"), ms=5)
ax.plot(xx / 1e6, slope * xx, color=P.muted(), lw=1.0)
ax.text(0.05, 1.15, rf"fit: $\gamma = {slope / 2 * 1e6:.2f}\ \mu\mathrm{{N\,m^{{-1}}}}$", fontsize=FT["tiny"],
        color=P.ink())
charts.style_axes(ax, r"$1/R_{\mathrm{p}} - 1/R_{\mathrm{d}}$ / $\mu$m$^{-1}$", r"$\Delta p$ / Pa")
charts.title(ax, "C  Micropipette aspiration")

ax = fig.add_subplot(gs[3])
ax.set_xlim(0, 12)
ax.set_ylim(-0.8, 5)
ax.set_aspect("equal")
ax.axis("off")
c1, c2 = P.fill("rrna"), P.fill("protein")
e1, e2 = P.edge("rrna"), P.edge("protein")
# complete engulfment
ax.add_patch(Circle((2, 2.6), 1.35, facecolor=c2, edgecolor=e2, lw=1))
ax.add_patch(Circle((2, 2.6), 0.75, facecolor=c1, edgecolor=e1, lw=1))
# partial engulfment
ax.add_patch(Circle((5.6, 2.6), 1.0, facecolor=c2, edgecolor=e2, lw=1))
ax.add_patch(Circle((6.4, 2.6), 0.85, facecolor=c1, edgecolor=e1, lw=1))
# separate
ax.add_patch(Circle((9.3, 2.6), 0.85, facecolor=c2, edgecolor=e2, lw=1))
ax.add_patch(Circle((11.1, 2.6), 0.75, facecolor=c1, edgecolor=e1, lw=1))
for x, txt in [(2, r"$\gamma_{01} > \gamma_{02} + \gamma_{12}$"), (6.0, "no tension exceeds\nthe other two"),
               (10.2, r"$\gamma_{12} > \gamma_{01} + \gamma_{02}$")]:
    ax.text(x, 0.75, txt, ha="center", va="center", fontsize=FT["tiny"], color=P.ink())
for x, txt in [(2, "engulfed"), (6.0, "partial"), (10.2, "separate")]:
    ax.text(x, 4.55, txt, ha="center", va="center", fontsize=FT["small"], color=P.ink())
ax.add_patch(Circle((0.5, -0.35), 0.16, facecolor=c1, edgecolor=e1, lw=0.8))
ax.text(0.8, -0.35, "phase 1", fontsize=FT["tiny"], color=P.ink(), va="center")
ax.add_patch(Circle((3.4, -0.35), 0.16, facecolor=c2, edgecolor=e2, lw=0.8))
ax.text(3.7, -0.35, "phase 2", fontsize=FT["tiny"], color=P.ink(), va="center")
ax.text(6.3, -0.35, "medium 0 around both", fontsize=FT["tiny"], color=P.muted(), va="center")
charts.title(ax, "D  Wetting of two phases")
