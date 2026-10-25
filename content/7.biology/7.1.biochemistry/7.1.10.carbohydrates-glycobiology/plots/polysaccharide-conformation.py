"""How the glycosidic linkage sets the shape of a glucose polymer (schematic, not to scale).
A: amylose, (alpha1-4)-linked: each residue is turned about 60 degrees relative to the previous one, so
the chain coils into a helix of about six residues per turn (V-amylose, pitch about 0.8 nm); the
hydrophobic core of the helix holds polyiodide (I3-, I5-), the basis of the blue starch-iodine test.
Residues on the far side of the helix are drawn paler. B: cellulose, (beta1-4)-linked: each residue is
turned 180 degrees relative to its neighbours (marked by the side on which the C-6 group points), so
the chain is straight; intrachain hydrogen bonds (O3-H...O5') stiffen each chain and interchain
hydrogen bonds join parallel chains into sheets and microfibrils."""

import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Polygon

P = bio.P
fig, ax = bio.canvas(21.0, 8.6)


def ring(c, r=0.32, token="carbohydrate", alpha_mix=0.0, zorder=6):
    t = np.radians(np.arange(6) * 60 + 30)
    v = np.c_[c[0] + r * np.cos(t), c[1] + r * 0.75 * np.sin(t)]
    if alpha_mix > 0:
        ax.add_patch(Polygon(
            v, closed=True, facecolor=P.mix(P.fill(token), P.surface(), alpha_mix),
            edgecolor=P.mix(P.edge(token), P.surface(), alpha_mix), lw=1.0, zorder=zorder))
    else:
        bio.shape(ax, v, token, lw=1.1, zorder=zorder)


# --- A: amylose helix -----------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 8.5))
bio.label(ax, (0.9, 8.15), "Amylose: (α1→4) → helix", bold=True, ha="left")
n = 25
rise, R = 0.32, 1.15
xs = 1.3 + np.arange(n) * rise
th = np.radians(60 * np.arange(n))
ys = 4.5 + R * np.cos(th)
depth = np.sin(th)
tt = np.linspace(0, n - 1, 600)
cx, cy, cd = 1.3 + tt * rise, 4.5 + R * np.cos(np.radians(60 * tt)), np.sin(np.radians(60 * tt))
for k in range(len(tt) - 1):
    back = cd[k] < 0
    ax.plot(cx[k:k + 2], cy[k:k + 2], color=P.mix(P.ink(), P.surface(), 0.6 if back else 0.0), lw=1.2,
            zorder=3 if back else 7, solid_capstyle="round")
for x in np.linspace(xs[0] + 0.2, xs[-1] - 0.2, 16):
    ax.add_patch(Circle((x, 4.5), 0.09, facecolor=P.fill("k"),
                 edgecolor=P.edge("k"), lw=0.6, zorder=4))
for i in np.argsort(depth):
    ring((xs[i], ys[i]), r=0.22 + 0.05 * depth[i], alpha_mix=0.55 if depth[i] < -0.2 else 0.0,
         zorder=5 if depth[i] < 0 else 8)
ax.annotate("", (xs[6], 6.25), (xs[0], 6.25), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.8))
bio.label(ax, ((xs[0] + xs[6]) / 2, 6.6), "one turn ≈ 6 residues (≈ 0.8 nm)", size="small")
bio.callout(ax, (xs[9] + 0.25, 4.5), (6.6, 2.0), "I₃⁻ / I₅⁻ in the core (blue colour)")
bio.label(ax, (5.3, 1.2), "adjacent rings at ≈ 60°: curved chain, compact granules", size="small")

# --- B: cellulose sheet -----------------------------------------------------------------------------------
bio.panel(ax, "B", (10.6, 8.5))
bio.label(ax, (11.4, 8.15), "Cellulose: (β1→4) → straight chains", bold=True, ha="left")
step = 0.95
for row, y in enumerate((6.4, 4.4, 2.4)):
    pts = [(11.6 + k * step, y) for k in range(9)]
    ax.plot([p[0] for p in pts], [y] * len(pts), color=P.ink(), lw=1.2, zorder=3)
    for k, p in enumerate(pts):
        ring(p)
        up = 1 if k % 2 == 0 else -1
        ax.plot([p[0], p[0]], [y + up * 0.24, y + up * 0.46], color=P.edge("carbohydrate"), lw=1.1, zorder=4)
        ax.add_patch(Circle((p[0], y + up * 0.5), 0.06,
                     color=P.edge("carbohydrate"), zorder=4))
        if k < 8:  # intrachain O3-H...O5' hydrogen bond across each linkage
            ax.plot([p[0] + 0.25, p[0] + step - 0.25], [y - up * 0.3, y - up * 0.3], color=P.fill("dna"), lw=1.0,
                    ls=(0, (1.5, 1.5)), zorder=4)
    if row < 2:  # interchain hydrogen bonds to the chain below
        for k in range(0, 9, 2):
            x = 11.6 + k * step
            ax.plot([x, x + 0.2], [y - 0.62, y - 1.45], color=P.fill("negative"), lw=1.0, ls=(0, (1.5, 1.5)), zorder=4)
bio.label(ax, (15.4, 1.2), "residues alternate by 180°: flat ribbons, H-bonded sheets", size="small")
lx = 20.4
ax.plot([lx - 0.25, lx + 0.25], [5.8, 5.8], color=P.fill("dna"), lw=1.2, ls=(0, (1.5, 1.5)))
bio.label(ax, (lx, 5.45), "intrachain", size="tiny")
ax.plot([lx - 0.25, lx + 0.25], [4.8, 4.8], color=P.fill("negative"), lw=1.2, ls=(0, (1.5, 1.5)))
bio.label(ax, (lx, 4.45), "interchain", size="tiny")
bio.label(ax, (lx, 6.4), "H bonds", size="small")
