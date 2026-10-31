"""Sedimentation velocity: the Lamm equation solved numerically (Definition 8.8.2).

A: forces on a particle in a sector-shaped cell of an analytical ultracentrifuge.
B: concentration profiles c(r, t) every 10 min for a mixture of a monomer (s = 4.4 S,
D = 6.0e-7 cm^2/s, 70 % of the mass) and a dimer (s = 6.7 S, D = 4.7e-7 cm^2/s, 30 %) at
50 000 rpm, meniscus 6.0 cm, bottom 7.2 cm. Finite volumes in the radial coordinate (central fluxes,
no-flux walls), explicit time steps of 0.4 s; the plateau falls by radial dilution exp(-2 s w^2 t).
C: the apparent distribution g(s*) = dc/ds* obtained from one profile (t = 60 min) by the change of
variable s* = ln(r/r_m)/(w^2 t), which separates the two species; diffusion broadens the peaks.
"""

import numpy as np
import matplotlib.patches as mpatches
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

rpm = 50000
w = 2 * np.pi * rpm / 60.0                 # rad/s
rm, rb = 6.0, 7.2                          # cm
N = 1200
edges = np.linspace(rm, rb, N + 1)
r = 0.5 * (edges[1:] + edges[:-1])
dr = edges[1] - edges[0]
species = [(4.4e-13, 6.0e-7, 0.7), (6.7e-13, 4.7e-7, 0.3)]    # s (s), D (cm^2/s), mass fraction
dt = 0.4
t_end = 100 * 60.0
snap_times = np.arange(10, 101, 10) * 60.0


def solve(s, D, c0):
    c = np.full(N, c0)
    out = []
    t = 0.0
    k = 0
    while t < t_end - 1e-9:
        # flux J at interior edges: J = s w^2 r c - D dc/dr (positive outward)
        ce = 0.5 * (c[1:] + c[:-1])
        re = edges[1:-1]
        J = s * w ** 2 * re * ce - D * (c[1:] - c[:-1]) / dr
        flux = np.zeros(N + 1)
        flux[1:-1] = re * J
        c = c - dt * (flux[1:] - flux[:-1]) / (r * dr)
        t += dt
        if k < len(snap_times) and t >= snap_times[k] - 1e-9:
            out.append(c.copy())
            k += 1
    return np.array(out)


profiles = [solve(s, D, f) for s, D, f in species]
total = profiles[0] + profiles[1]

fig, ax = bio.canvas(25.0, 8.6)
# A: sector cell schematic
bio.panel(ax, "A", (0.1, 8.5))
cx, cy = 0.9, 4.2
ang = np.radians(6)
R0, R1 = 2.2, 5.6
wedge = mpatches.Wedge((cx, cy), R1, -np.degrees(ang), np.degrees(ang), width=R1 - R0,
                       facecolor=P.light("cytoplasm"), edgecolor=P.edge("neutral"), lw=1.0)
ax.add_patch(wedge)
ax.plot([cx, cx + R1 + 0.4], [cy, cy], color=P.muted(), lw=0.6, ls=":")
ax.add_patch(mpatches.Circle((cx, cy), 0.12, color=P.ink()))
bio.label(ax, (cx, cy - 0.55), "rotor\naxis", size="tiny", color=P.muted())
# particle and forces
px, py = cx + 4.0, cy
ax.add_patch(mpatches.Circle((px, py), 0.22, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.8, zorder=5))
bio.arrow(ax, (px + 0.25, py + 0.05), (px + 1.5, py + 0.05), kind="process", color=P.edge("negative"))
bio.label(ax, (px + 1.0, py + 0.65), r"$m\omega^2 r$", size="tiny")
bio.arrow(ax, (px - 0.25, py + 0.05), (px - 1.1, py + 0.05), kind="process", color=P.edge("channel"))
bio.label(ax, (px - 0.8, py + 0.65), r"$m\bar v\rho\,\omega^2 r$", size="tiny")
bio.arrow(ax, (px - 0.25, py - 0.25), (px - 1.4, py - 0.25), kind="process", color=P.edge("enzyme"))
bio.label(ax, (px - 0.9, py - 0.75), r"$f\,\mathrm{d}r/\mathrm{d}t$", size="tiny")
bio.label(ax, (cx + R0 - 0.05, cy + 1.05), "meniscus $r_m$", size="tiny", color=P.muted())
bio.label(ax, (cx + R1, cy + 1.05), "bottom $r_b$", size="tiny", color=P.muted())
bio.label(ax, (cx + 3.4, 1.4), "centrifugal = buoyancy + friction\n" + r"$s = \dfrac{\mathrm{d}r/\mathrm{d}t}{\omega^2 r} = \dfrac{M(1-\bar v\rho)}{N_\mathrm{A} f}$",
          size="tiny")
bio.label(ax, (cx + 3.4, 7.6), "sector-shaped cell", size="small", bold=True)

# B: profiles
bio.panel(ax, "B", (7.7, 8.5))
pb = charts.axes_at(ax, (9.0, 1.3, 7.2, 6.4))
for i, c in enumerate(total):
    tone = P.mix(P.edge("protein"), P.light("protein"), i / (len(total) - 1))
    pb.plot(r, c, color=tone, lw=1.2)
pb.text(6.03, 1.03, "10 min", fontsize=FT["tiny"], color=P.ink())
pb.text(6.9, 0.5, "100 min", fontsize=FT["tiny"], color=P.ink())
plateau = [sum(f * np.exp(-2 * s * w ** 2 * t) for s, D, f in species) for t in snap_times]
pb.plot([7.05] * len(plateau), plateau, "_", ms=8, color=P.muted())
pb.text(6.5, 1.05, "plateau falls by radial dilution", fontsize=FT["tiny"], color=P.muted())
pb.set_xlim(rm, rb)
pb.set_ylim(0, 1.15)
charts.style_axes(pb, "radius r / cm", "concentration / initial")
charts.title(pb, "Boundaries move out and spread (50 000 rpm)")

# C: g(s*)
bio.panel(ax, "C", (17.0, 8.5))
pc = charts.axes_at(ax, (18.3, 1.3, 6.2, 6.4))
k60 = 5                                    # index of t = 60 min
t60 = snap_times[k60]
sstar = np.log(r / rm) / (w ** 2 * t60) * 1e13
for comp, tok, name in ((profiles[0][k60], "protein", "monomer"), (profiles[1][k60], "receptor", "dimer"), (total[k60], "neutral", "total")):
    g = np.gradient(comp, sstar)
    keep = r < 7.0                         # exclude the pile-up at the cell bottom
    pc.plot(sstar[keep], g[keep], color=charts.line(tok), lw=1.8 if name == "total" else 1.0,
            ls="-" if name == "total" else "--", label=name)
for s, D, f in species:
    pc.axvline(s * 1e13, color=P.muted(), lw=0.6, ls=":")
pc.set_xlim(2, 9)
pc.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pc, "apparent sedimentation coefficient s* / S", "g(s*) = dc/ds* (per S)")
charts.title(pc, "Two species resolved by s")
