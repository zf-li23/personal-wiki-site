# Three in vitro assays of translational motors (schematics, not to scale).
# A: gliding (motility) assay: motors fixed to glass move a filament; the filament glides with its
#    minus end leading when the motors walk toward the plus end.
# B: bead assay in an optical trap: one kinesin carries a bead; the trap (stiffness kappa) measures
#    the displacement and applies the load F = -kappa dx.
# C: single-fluorophore tracking of myosin V (one head labeled): simulated position of the label,
#    74 nm steps separated by two dwells (the label moves only on every second step of the molecule).
import numpy as np
from matplotlib.patches import Circle, Rectangle

import wikibio as bio
from wikibio import cytoskel as C
from wikibio import physiology as phys
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(27, 9.2)
rng = np.random.default_rng(4)


def glass(x0, x1, y):
    ax.add_patch(Rectangle((x0, y - 0.45), x1 - x0, 0.45, facecolor=P.light("vacuole"), edgecolor=P.edge("vacuole"),
                           lw=0.8, zorder=3))
    bio.label(ax, (x0 + 0.15, y - 0.23), "Glass", size="tiny", ha="left", zorder=5)


# ---- A: gliding assay -----------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 9.1))
gy = 1.3
glass(0.4, 8.4, gy)
mt_y = gy + 2.35
for i, x in enumerate(np.linspace(1.1, 7.6, 6)):
    top = (x + 0.25 * (-1) ** i, mt_y - 0.42)
    phys.coiled_coil(ax, (x, gy + 0.02), (x + 0.1, top[1] - 0.25), token="enzyme")
    phys.motor_head(ax, (top[0] - 0.12, top[1] - 0.12), 0.42, seed=i)
    phys.motor_head(ax, (top[0] + 0.22, top[1] - 0.2), 0.42, seed=i + 7)
C.tube(ax, (7.9, mt_y), (0.6, mt_y), width=0.42)
bio.label(ax, (8.15, mt_y), "−", size="title", ha="left", bold=True)
bio.label(ax, (0.3, mt_y), "+", size="title", ha="right", bold=True)
bio.arrow(ax, (4.5, mt_y + 0.75), (7.2, mt_y + 0.75), kind="process", lw=1.6)
bio.label(ax, (4.3, mt_y + 0.75), "filament glides", size="small", ha="right")
bio.label(ax, (4.4, 8.6), "Gliding assay", size="title", bold=True)
bio.label(ax, (4.4, 8.05), "many motors, no load: unloaded velocity", size="tiny")
bio.callout(ax, (1.15, gy + 0.8), (2.4, 0.35), "Motors on the surface", size="tiny")

# ---- B: bead assay --------------------------------------------------------------------------------------
X0 = 9.3
bio.panel(ax, "B", (X0 - 0.2, 9.1))
glass(X0 + 0.2, X0 + 8.4, gy)
trap = (X0 + 4.6, 4.55)
phys.optical_trap(ax, trap, half_height=2.9, spread=1.6, token="h")
mty = gy + 0.3
C.tube(ax, (X0 + 0.3, mty), (X0 + 8.3, mty), width=0.42)
bio.label(ax, (X0 + 0.35, mty + 0.45), "−", size="title", ha="left", bold=True)
bio.label(ax, (X0 + 8.25, mty + 0.45), "+", size="title", ha="right", bold=True)
head_y = mty + 0.42
bead_c, bead_r = (trap[0] + 0.7, trap[1]), 1.45
neck = phys.kinesin(ax, (X0 + 4.6, head_y), (X0 + 5.35, head_y), (bead_c[0] - 0.1, bead_c[1] - bead_r + 0.05), head=0.55)
phys.bead(ax, bead_c, bead_r)
for d in ((-0.13, 0), (0, -0.13)):
    ax.plot([trap[0] + d[0], trap[0] - d[0]], [trap[1] + d[1], trap[1] - d[1]], color=P.on_fill(), lw=1.0, zorder=14)
bio.arrow(ax, (bead_c[0] - 0.1, bead_c[1] + 0.3), (bead_c[0] - 1.2, bead_c[1] + 0.3), kind="process", lw=1.5,
          color=P.on_fill(), zorder=16)
bio.label(ax, (bead_c[0] - 0.65, bead_c[1] + 0.68), "$F$", size="normal", color=P.on_fill(), zorder=16)
quant.bracket(ax, (trap[0], trap[1] + bead_r + 0.35), (bead_c[0], trap[1] + bead_r + 0.35), "$\\Delta x$", side=-1)
bio.label(ax, (X0 + 4.4, 8.6), "Bead assay in an optical trap", size="title", bold=True)
bio.label(ax, (X0 + 4.4, 8.05), "one motor, load $F = -\\kappa\\,\\Delta x$ or clamped", size="tiny")
bio.callout(ax, neck, (X0 + 1.6, 3.9), "Kinesin-1", size="tiny")
bio.callout(ax, (bead_c[0] + 1.0, bead_c[1] - 1.0), (X0 + 7.9, 2.9), "Bead", size="tiny")
bio.callout(ax, (trap[0] - 0.9, trap[1] + 2.2), (X0 + 1.4, 6.6), "Focused laser beam", size="tiny")

# ---- C: single-fluorophore tracking of myosin V --------------------------------------------------------
X1 = 18.6
bio.panel(ax, "C", (X1 - 0.2, 9.1))
ay = 5.75
C.actin_filament(ax, (X1 + 0.3, ay), (X1 + 8.2, ay), r=0.13, ends=True)
rear, front = (X1 + 2.6, ay + 0.16), (X1 + 5.4, ay + 0.16)
neck = C.myosin_v(ax, rear, front, (X1 + 4.0, ay + 2.6), head=0.5)
ax.add_patch(Circle((rear[0] - 0.05, rear[1] + 0.62), 0.14, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=20))
bio.callout(ax, (rear[0] - 0.12, rear[1] + 0.7), (X1 + 1.0, ay + 2.0), "Fluorophore", size="tiny")
bio.label(ax, (X1 + 4.4, 8.6), "Single-fluorophore tracking", size="title", bold=True)

# simulated trace: the molecule steps 37 nm; the labeled head moves 74 nm on every other step
k = 2.0  # steps per second at low ATP
t_step = np.cumsum(rng.exponential(1 / k, 40))
t = np.linspace(0, 8, 1600)
nmol = np.searchsorted(t_step, t)
label_pos = 74.0 * ((nmol + 1) // 2)
noisy = label_pos + rng.normal(0, 4.0, t.size)
pc = quant.Plot(ax, (X1 + 1.2, 0.9, 6.6, 3.3), (0, 8), (-20, 600), xlabel="$t$ / s", ylabel="Label / nm",
                xticks=[0, 2, 4, 6, 8], yticks=[0, 200, 400, 600], grid=True)
pc.line(t, noisy, "neutral", lw=0.5)
pc.line(t, label_pos, "negative", lw=1.3)
pc.text(0.2, 540, "74 nm steps of one head:\nhand over hand, not inchworm", ha="left", va="top", size="tiny")
