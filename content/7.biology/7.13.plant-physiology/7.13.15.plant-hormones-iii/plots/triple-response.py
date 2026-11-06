# Dose-response of the triple response (schematic): dark-grown Arabidopsis seedlings, 3 d.
# Hypocotyl length L(C) = Lmin + (L0 - Lmin) K^n / (K^n + C^n) (Eq. 15.3), K = 0.15 uL/L, n = 1.2;
# apical hook angle rises from ~180 to ~280 degrees. Right: seedling shapes in air, ethylene, ein2 + ethylene.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

C = np.logspace(-3, 2, 300)
K, n = 0.15, 1.2
frac = K ** n / (K ** n + C ** n)
L = 2 + 8 * frac
hook = 180 + 100 * (1 - frac)

fig = plt.figure(figsize=(11, 4.3))
a = fig.add_axes([0.07, 0.15, 0.42, 0.78])
a.plot(C, L, color="#2f6fb5", lw=2.4, label="hypocotyl length")
a.set_xscale("log")
a.set_xlabel("Ethylene / (µL L⁻¹)")
a.set_ylabel("Hypocotyl length / mm", color="#2f6fb5")
a.set_ylim(0, 11)
a.axvline(K, color="0.5", lw=0.8, ls=":")
a.text(K * 1.15, 0.5, "K ≈ 0.15 µL/L", fontsize=8.5)
a2 = a.twinx()
a2.plot(C, hook, color="#c0504d", lw=2.0, ls="--", label="hook angle")
a2.set_ylabel("Apical hook angle / °", color="#c0504d")
a2.set_ylim(150, 300)
for ax_ in (a, a2):
    ax_.spines["top"].set_visible(False)
a.text(0.0013, 10.4, "A", fontsize=12, fontweight="bold")

# B: seedling sketches
b = fig.add_axes([0.6, 0.05, 0.38, 0.9])
b.set_xlim(0, 9)
b.set_ylim(-0.6, 10)
b.set_aspect("equal")
b.axis("off")
green, stem, root = "#7cb86a", "#c9b27c", "#b08d57"


def seedling(x, hyp, thick, hook_deg, rootlen, label):
    # hypocotyl from soil line (y=1.5) upward, then a hook bending by hook_deg - 180 extra
    y0 = 1.5
    b.plot([x, x], [y0, y0 + hyp], color=stem, lw=thick, solid_capstyle="round")
    ang = np.radians(np.linspace(0, hook_deg, 40))
    r = 0.45
    cx, cy = x - r, y0 + hyp
    hx, hy = cx + r * np.cos(ang), cy + r * np.sin(ang)
    b.plot(hx, hy, color=stem, lw=thick, solid_capstyle="round")
    b.add_patch(Ellipse((hx[-1], hy[-1] - 0.18), 0.35, 0.55, angle=np.degrees(ang[-1]), color=green))
    b.plot([x, x], [y0, y0 - rootlen], color=root, lw=thick * 0.6, solid_capstyle="round")
    b.text(x, -0.5, label, ha="center", fontsize=8.5)


seedling(1.5, 6.5, 2.2, 180, 3.0 * 0 + 1.4, "air")
seedling(4.5, 1.6, 5.5, 280, 0.5, "10 µL/L ethylene")
seedling(7.5, 6.3, 2.2, 180, 1.4, "ein2 + ethylene")
b.plot([0.2, 8.8], [1.5, 1.5], color="0.6", lw=0.6, ls=":")
b.text(0.1, 9.6, "B", fontsize=12, fontweight="bold")
