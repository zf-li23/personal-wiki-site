"""Biofilms: development and the gradients inside them.
A: the four stages. Reversible attachment of swimming cells to a surface; irreversible attachment with
pili and adhesins while the flagellum is switched off; growth into microcolonies with a matrix of
exopolysaccharide, protein and extracellular DNA (released by the explosive lysis of a subpopulation);
a mature biofilm with water channels, divided into layers by the gradients of panel B; and dispersal,
in which matrix-degrading enzymes and a fall in c-di-GMP return single cells to the plankton.
B: substrate and oxygen penetration. In a flat biofilm of thickness L, with diffusion coefficient D and
zero-order consumption at rate q per unit volume (concentrations well above the half-saturation
constant), the steady state of D c'' = q with c(L) = c0 at the surface and no flux at the base gives
c(x) = c0 [1 - phi^2 (1 - (x/L)^2)] and a fully penetrated film only if the Thiele modulus
phi = L sqrt(q / (2 D c0)) <= 1. For phi > 1 the substrate runs out at x_c = L(1 - 1/phi); below that
depth the cells are starved and dormant, and above it the profile is c0 ((x - x_c)/(L - x_c))^2, which
meets zero with zero slope.
C: the consequence for antimicrobials: killing in a biofilm, with a tolerant dormant fraction, against
the exponential killing of a planktonic culture."""

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Polygon

import wikibio as bio
from wikibio import charts
from wikibio import microbio as M

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(27.0, 11.6)

# ---------------------------------------------------------------- A: stages
bio.panel(ax, "A", (0.2, 11.5))
base = 6.6
stages = [(2.4, "1 reversible\nattachment"), (7.0, "2 irreversible attachment,\nmatrix starts"),
          (11.6, "3 microcolonies"), (16.6, "4 mature biofilm\nwith water channels"),
          (21.8, "5 dispersal")]
for x, name in stages:
    ax.plot([x - 1.9, x + 1.9], [base, base], color=P.muted(), lw=2.4, solid_capstyle="round", zorder=3)
    bio.label(ax, (x, base - 0.9), name, size="tiny", color=P.muted())

M.bacillus(ax, (2.0, base + 1.3), 0.9, 0.3, angle=20, gram="-", flagella="monotrichous", flagellum_length=0.7)
M.bacillus(ax, (2.9, base + 0.35), 0.9, 0.3, angle=-8, gram="-", flagella="monotrichous", flagellum_length=0.7)
bio.arrow(ax, (2.1, base + 1.0), (2.6, base + 0.65), kind="process", lw=0.8, head=0.12)

for k in range(4):
    M.bacillus(ax, (6.0 + 0.65 * k, base + 0.25), 0.85, 0.3, angle=0, gram="-")
ax.add_patch(FancyBboxPatch((5.6, base), 3.0, 0.55, boxstyle="round,pad=0,rounding_size=0.12",
                            facecolor=P.fill("carbohydrate"), edgecolor="none", alpha=0.5, zorder=4))

for cx in (10.7, 12.5):
    ax.add_patch(Polygon([[cx - 0.95, base], [cx + 0.95, base], [cx + 0.6, base + 1.1], [cx - 0.6, base + 1.1]],
                         closed=True, facecolor=P.fill("carbohydrate"), edgecolor=P.edge("carbohydrate"), lw=1.0,
                         alpha=0.75, zorder=4))
    for _ in range(9):
        M.bacillus(ax, (cx + rng.uniform(-0.6, 0.6), base + rng.uniform(0.15, 0.95)), 0.7, 0.26,
                   angle=rng.uniform(0, 180), gram="-")

for dx, h in ((-1.5, 1.9), (0.0, 2.4), (1.5, 1.8)):
    cx = 16.6 + dx
    ax.add_patch(Polygon([[cx - 0.75, base], [cx + 0.75, base], [cx + 0.45, base + h], [cx - 0.45, base + h]],
                         closed=True, facecolor=P.fill("carbohydrate"), edgecolor=P.edge("carbohydrate"), lw=1.0,
                         alpha=0.75, zorder=4))
    for _ in range(14):
        M.bacillus(ax, (cx + rng.uniform(-0.45, 0.45), base + rng.uniform(0.1, h - 0.15)), 0.6, 0.24,
                   angle=rng.uniform(0, 180), gram="-")
bio.callout(ax, (16.6, base + 2.2), (15.0, base + 3.4), "oxygen and substrate\nonly at the top", size="tiny")
bio.callout(ax, (15.5, base + 0.3), (13.4, base + 2.0), "starved, dormant cells\nat the base", size="tiny")

cx = 21.8
ax.add_patch(Polygon([[cx - 1.1, base], [cx + 1.1, base], [cx + 0.7, base + 1.6], [cx - 0.7, base + 1.6]],
                     closed=True, facecolor=P.fill("carbohydrate"), edgecolor=P.edge("carbohydrate"), lw=1.0,
                     alpha=0.6, zorder=4))
for _ in range(8):
    M.bacillus(ax, (cx + rng.uniform(-0.5, 0.5), base + rng.uniform(0.15, 1.3)), 0.6, 0.24,
               angle=rng.uniform(0, 180), gram="-")
for dx, dy in ((1.4, 1.9), (2.0, 1.2), (1.1, 2.6)):
    M.bacillus(ax, (cx + dx, base + dy), 0.8, 0.28, angle=rng.uniform(0, 60), gram="-",
               flagella="monotrichous", flagellum_length=0.7)
bio.label(ax, (25.3, base + 2.3), "matrix enzymes,\nlow c-di-GMP", size="tiny", color=P.muted())
for k in range(4):
    bio.arrow(ax, (stages[k][0] + 2.0, base + 0.7), (stages[k + 1][0] - 2.0, base + 0.7), kind="process",
              lw=1.0, head=0.16)
bio.label(ax, (2.4, base + 3.3), "planktonic cells", size="tiny", color=P.muted())

# ---------------------------------------------------------------- B: profiles
bio.panel(ax, "B", (0.2, 5.1))
pax = charts.axes_at(ax, (2.2, 1.2, 9.4, 3.6))
x = np.linspace(0, 1, 400)
for phi, ls, tok in ((0.5, "-", "dna"), (1.0, "--", "plant"), (2.0, "-.", "highlight"), (4.0, ":", "negative")):
    if phi <= 1:
        c = 1 - phi ** 2 * (1 - x ** 2)
    else:
        xc = 1 - 1 / phi
        c = np.where(x < xc, 0.0, ((x - xc) / (1 - xc)) ** 2)
    pax.plot(x, c, color=charts.line(tok), lw=1.8, ls=ls, label=f"φ = {phi:g}")
pax.set_xlim(0, 1)
pax.set_ylim(-0.02, 1.05)
pax.set_xticks([0, 0.5, 1], ["base", "", "surface"])
pax.legend(fontsize=6.8, frameon=False, loc="upper left")
charts.style_axes(pax, "position in the film, x/L", "substrate c/c₀")
charts.title(pax, "Diffusion against consumption")

# ---------------------------------------------------------------- C: killing
bio.panel(ax, "C", (12.4, 5.1))
cax = charts.axes_at(ax, (14.6, 1.2, 9.4, 3.6))
t = np.linspace(0, 8, 400)
k_fast = 1.6
cax.plot(t, np.exp(-k_fast * t), color=charts.line("dna"), lw=1.8, label="planktonic culture")
for f, ls, tok in ((0.01, "--", "plant"), (0.1, "-.", "negative")):
    cax.plot(t, (1 - f) * np.exp(-k_fast * t) + f * np.exp(-0.06 * t), color=charts.line(tok), lw=1.8, ls=ls,
             label=f"biofilm, dormant fraction {f:g}")
cax.set_yscale("log")
cax.set_xlim(0, 8)
cax.set_ylim(1e-7, 2)
cax.legend(fontsize=6.8, frameon=False, loc="lower left")
charts.style_axes(cax, "time of exposure (a.u.)", "surviving fraction")
charts.title(cax, "Why biofilms survive antimicrobials")
