"""A, B and Z duplexes built from their helical parameters (twist, rise, x-displacement, inclination).

Each base pair is drawn as a rod 10.5 A long (the C1'-C1' distance), displaced from the helix axis by
the x-displacement along its short axis, tilted by the inclination about that axis, then rotated by
the cumulative twist and raised by the cumulative rise. Top row: one turn viewed down the axis
(darker rods nearer the viewer; dashed circle: radius of the phosphates, about 9 A). Bottom row:
one turn viewed from the side (darker rods nearer the viewer). Z-DNA alternates the twist of its CpG and GpC steps.
"""

import numpy as np
import wikibio as bio

P = bio.P
FT = bio.core.FONT

FORMS = [
    ("A-DNA", dict(twist=[32.7], rise=2.56, dx=-4.5, incl=20.0, handed="right")),
    ("B-DNA", dict(twist=[34.3], rise=3.38, dx=0.0, incl=-6.0, handed="right")),
    ("Z-DNA", dict(twist=[-9.0, -51.0], rise=3.72, dx=3.0, incl=-6.2, handed="left")),
]
HALF = 5.25       # half the C1'-C1' distance, A


def rods(par, n):
    out = []
    theta, z = 0.0, 0.0
    for k in range(n):
        eta = np.radians(par["incl"])
        ends = np.array([[par["dx"], -HALF * np.cos(eta), -HALF * np.sin(eta)],
                         [par["dx"], HALF * np.cos(eta), HALF * np.sin(eta)]])
        c, s = np.cos(np.radians(theta)), np.sin(np.radians(theta))
        Rz = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
        e = ends @ Rz.T
        e[:, 2] += z
        out.append(e)
        theta += par["twist"][k % len(par["twist"])]
        z += par["rise"]
    return np.array(out)


fig, ax = bio.canvas(22.0, 17.2)
sc = 0.24                     # canvas units per angstrom
for j, (name, par) in enumerate(FORMS):
    cx = 3.7 + 7.3 * j
    # top view: one turn
    turn = 360.0 / abs(np.mean(par["twist"]))
    n_top = int(round(turn))
    R = rods(par, n_top)
    cy = 13.4
    circ = np.linspace(0, 2 * np.pi, 200)
    ax.plot(cx + sc * 9.0 * np.cos(circ), cy + sc * 9.0 * np.sin(circ), color=P.muted(), lw=0.7, ls="--")
    ax.plot(cx, cy, "+", color=P.muted(), ms=6, mew=0.8)
    zmax = R[:, :, 2].max()
    for k, e in enumerate(R):
        depth = e[:, 2].mean() / max(zmax, 1e-9)        # 1 = top (nearest the viewer)
        col = P.mix(P.mix(P.edge("dna"), P.surface(), 0.7), P.edge("dna"), depth)
        ax.plot(cx + sc * e[:, 0], cy + sc * e[:, 1], color=col, lw=3.0, solid_capstyle="round", zorder=5 + depth)
    bio.label(ax, (cx, 16.6), name, size="normal", bold=True)
    tw = "/".join(f"{t:g}" for t in par["twist"])
    bio.label(ax, (cx, 10.75), f"twist {tw}°  ·  {turn:.1f} bp/turn", size="tiny", color=P.muted())
    bio.label(ax, (cx, 10.3), f"x-displacement {par['dx']:+.1f} Å", size="tiny", color=P.muted())
    # side view: one turn, smaller scale
    ss = 0.19
    n_side = n_top + 1
    R = rods(par, n_side)
    base = 0.9
    for e in R:
        y = e[:, 1].mean() / 6.0                         # -1 (front) .. 1 (back)
        t = float(np.clip((1 - y) / 2, 0, 1))
        col = P.mix(P.mix(P.edge("dna"), P.surface(), 0.7), P.edge("dna"), t)
        ax.plot(cx + ss * e[:, 0], base + ss * e[:, 2], color=col, lw=1.6 + 1.2 * t,
                solid_capstyle="round", zorder=4 + 2 * t)
    top = base + ss * R[:, :, 2].max()
    ax.plot([cx, cx], [base - 0.2, top + 0.2], color=P.muted(), lw=0.6, ls=":", zorder=2)
    pitch = abs(turn) * par["rise"]
    bio.label(ax, (cx + 2.9, base + ss * pitch / 2), f"pitch\n{pitch:.0f} Å", size="tiny", color=P.ink())
    ax.annotate("", xy=(cx + 2.0, base), xytext=(cx + 2.0, base + ss * pitch),
                arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.8))
    bio.label(ax, (cx - 2.9, base + ss * pitch / 2), f"rise\n{par['rise']:.2f} Å\nincl. {par['incl']:+.0f}°", size="tiny", color=P.muted())
bio.scale_bar(ax, (19.0, 11.5), sc * 10, "1 nm (top views)", size="tiny")
bio.scale_bar(ax, (19.0, 0.5), 0.19 * 10, "1 nm (side views)", size="tiny")
