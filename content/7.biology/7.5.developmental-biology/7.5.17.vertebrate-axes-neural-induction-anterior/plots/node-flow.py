# Leftward flow at the mouse node from tilted rotating cilia (Formula 17.4.1). A: ventral view of the node (anterior
# up; viewed from the ventral side the embryo's left is on the viewer's right): each pit cell bears one motile cilium
# that rotates clockwise as seen from its tip, and the fluid moves to the left. B: side view of one cilium (posterior
# to the right): its rotation axis is tilted posteriorly, so the cilium sweeps leftward far from the cell surface and
# rightward close to it, where the no-slip wall impedes the fluid. C: net pumping, proportional to the time average of
# the leftward force times its height above the wall, against the tilt for three cone half-angles; it vanishes for
# an upright cilium and is limited by the requirement that the cilium not hit the wall (tilt + cone <= 90 degrees).
import numpy as np
import wikibio as bio
from wikibio import bodyaxes as BA
from wikibio import charts as C

fig, ax = bio.canvas(24.0, 8.4)
P = bio.P
bio.panel(ax, "A", (0.2, 8.2))
n = BA.node_pit(ax, (4.2, 4.0), 5.6)
bio.label(ax, n["left"], "L", size="normal", bold=True, ha="left")
bio.label(ax, n["right"], "R", size="normal", bold=True, ha="right")
bio.label(ax, (n["anterior"][0], n["anterior"][1] + 0.3), "anterior", size="tiny", color=P.muted())
bio.label(ax, (n["posterior"][0], n["posterior"][1] - 0.3), "posterior", size="tiny", color=P.muted())
bio.label(ax, (4.2, 7.6), "ventral view", size="small", bold=True)

bio.panel(ax, "B", (8.8, 8.2))
c = BA.cilium_cone(ax, (12.2, 2.0), 2.6, tilt=35, cone=30, wall=3.0)
bio.label(ax, (12.2, 7.6), "side view", size="small", bold=True)
bio.label(ax, (15.0, 1.6), "posterior →", size="tiny", color=P.muted())
bio.label(ax, (c["tip_high"][0] + 0.2, c["tip_high"][1] + 0.4), "leftward sweep,\nfar from wall", size="tiny", ha="left")
bio.label(ax, (c["tip_low"][0] + 0.3, c["tip_low"][1] - 0.45), "rightward sweep,\nnear wall", size="tiny", ha="left")
bio.label(ax, (12.2, 1.2), "cell surface (no-slip wall)", size="tiny", color=P.muted())

bio.panel(ax, "C", (17.0, 8.2))
pa = C.axes_at(ax, (18.6, 1.4, 5.0, 5.6))
th = np.linspace(0, 90, 300)
for psi, t in [(20, 0.6), (30, 0.3), (45, 0.0)]:
    ok = th + psi <= 90
    q = np.sin(np.radians(psi)) ** 2 * np.sin(np.radians(th))
    pa.plot(th[ok], q[ok], color=P.mix(C.line("dna"), P.surface(), t), lw=2.0, label=f"cone {psi}°")
    pa.plot(th[~ok], q[~ok], color=P.mix(C.line("dna"), P.surface(), t), lw=0.8, ls=(0, (2, 2)))
pa.axvline(40, color=P.muted(), lw=0.8, ls=(0, (1, 2)))
pa.text(41, 0.47, "measured\ntilt ≈ 40°", fontsize=bio.core.FONT["tiny"], color=P.muted())
pa.set_xlim(0, 90)
pa.set_ylim(0, 0.55)
C.style_axes(pa, "tilt θ / degrees", "net leftward pumping\n∝ sin²ψ sin θ")
pa.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
