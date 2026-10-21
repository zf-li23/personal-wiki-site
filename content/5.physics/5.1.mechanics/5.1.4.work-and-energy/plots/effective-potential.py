"""Effective potential in a 1/r field and the orbit families (G M = m = 1)."""

import numpy as np
import matplotlib.pyplot as plt

r0 = 1.0
# launch from r0 with speed v perpendicular to the radius: L = r0 v, E = v^2/2 - 1/r0
cases = [
    ("circle", 1.0, "C0"),
    ("ellipse", 0.8, "C2"),
    ("parabola (E = 0)", np.sqrt(2.0), "C1"),
    ("hyperbola", 1.6, "C3"),
]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8))

# left: effective potential for the ellipse case and its energy level, plus other levels
L = r0 * 0.8
r = np.linspace(0.15, 6, 800)
Veff = L**2 / (2 * r**2) - 1 / r
ax1.plot(r, Veff, color="k", lw=2, label="E_eff(r), fixed L")
ax1.plot(r, L**2 / (2 * r**2), color="0.6", lw=1, ls="--", label="L^2/(2 m r^2)")
ax1.plot(r, -1 / r, color="0.6", lw=1, ls=":", label="-G M m / r")
rc = L**2
Emin = -1 / (2 * L**2)
levels = [(Emin, "E = E_eff,min (circle)", "C0"), (0.6 * Emin, "E < 0 (ellipse)", "C2"),
          (0.0, "E = 0 (parabola)", "C1"), (0.4, "E > 0 (hyperbola)", "C3")]
for E, lab, c in levels:
    inside = Veff <= E + 1e-12
    if E == Emin:
        ax1.plot([rc], [E], "o", color=c, label=lab)
    else:
        rr = r[inside]
        ax1.plot([rr.min(), rr.max() if E < 0 else 6], [E, E], color=c, lw=1.6, label=lab)
ax1.set_ylim(-1.2, 1.0)
ax1.set_xlim(0, 6)
ax1.set_xlabel("r")
ax1.set_ylabel("energy")
ax1.set_title("Effective potential (G M = m = 1)")
ax1.legend(fontsize=8, loc="upper right")

# right: orbits from the same point, r(theta) = p / (1 + e cos theta) with perihelion or aphelion at r0
th = np.linspace(-np.pi, np.pi, 2000)
for lab, v, c in cases:
    Lc = r0 * v
    p = Lc**2
    e = p / r0 - 1  # r(0) = r0 if launch point is the perihelion (e >= 0) or aphelion (e < 0)
    ee = abs(e)
    if e >= 0:
        rr = p / (1 + ee * np.cos(th))
        x, y = rr * np.cos(th), rr * np.sin(th)
    else:
        rr = p / (1 + ee * np.cos(th - np.pi))
        x, y = rr * np.cos(th), rr * np.sin(th)
    ok = (rr > 0) & (rr < 8) & (1 + ee * np.cos(th if e >= 0 else th - np.pi) > 1e-3)
    x, y = np.where(ok, x, np.nan), np.where(ok, y, np.nan)
    ax2.plot(x, y, color=c, lw=1.8, label=lab)
ax2.plot([0], [0], "*", color="k", ms=12, label="force center")
ax2.plot([r0], [0], "o", color="k", ms=5)
ax2.set_xlim(-3.5, 2.0)
ax2.set_ylim(-3, 3)
ax2.set_aspect("equal")
ax2.set_title("Orbits launched from the same point")
ax2.legend(fontsize=8, loc="lower left")
fig.tight_layout()
