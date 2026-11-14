"""Model: path integration in the desert ant Cataglyphis (wikibehav simulation of Wehner's experiments). A: a
forager searches along a tortuous path (blue) from the nest, finds food (star), and runs home along the
integrated home vector (orange) on a straight line. B: an ant captured at the feeder and displaced to unfamiliar
ground runs off the same home vector to a fictive nest position and then searches in expanding loops around it.
C: errors accumulate: 40 ants that made the same outward trip but registered each step with a heading error
(10 deg s.d. per step, plus an individual compass bias of 4 deg s.d. and a distance error of 8 %) end their home runs in a cloud around the nest whose spread grows with the length of the path; near the nest ants switch to landmarks and
odors."""
import numpy as np

import wikibio as bio
import wikibehav as wb

P = bio.P
fig, ax = bio.canvas(27, 10.6)
pi = wb.path_integration(steps=240, seed=3, error=0.0)
bio.panel(ax, "A", (0.3, 10.3))
bio.label(ax, (1.3, 10.0), "Foraging trip", size="small", bold=True, ha="left")
to = wb.fit([pi["outbound"], pi["homing"]], (0.8, 1.2, 7.6, 8.2))
wb.trail(ax, to(pi["outbound"]), token="dna", lw=1.0, arrows=3, start="o")
wb.trail(ax, to(pi["homing"]), token="rna", lw=1.6, fade=False, arrows=1, end="*")
n = to(pi["nest"])
bio.label(ax, (n[0], n[1] - 0.4), "nest", size="tiny", va="top")
f = to(pi["outbound"][-1:])[0]
bio.label(ax, (f[0], f[1] + 0.4), "food", size="tiny")
pi2 = wb.path_integration(steps=240, seed=3, error=0.0, displace=(16, -8))
bio.panel(ax, "B", (9.3, 10.3))
bio.label(ax, (10.3, 10.0), "Displaced at the feeder", size="small", bold=True, ha="left")
to2 = wb.fit([pi2["outbound"], pi2["homing"], pi2["search"]], (9.8, 1.2, 7.6, 8.2))
wb.trail(ax, to2(pi2["outbound"]), token="dna", lw=0.8, arrows=2, start="o")
wb.trail(ax, to2(pi2["homing"]), token="rna", lw=1.6, fade=False, arrows=1)
wb.trail(ax, to2(pi2["search"]), token="rna", lw=0.7, fade=False)
for key, name in (("nest", "real nest"), ("fictive", "fictive nest"), ("release", "release")):
    q = to2(np.atleast_2d(pi2[key]))[0]
    bio.label(ax, (q[0], q[1] - 0.4), name, size="tiny", va="top")
bio.panel(ax, "C", (18.3, 10.3))
bio.label(ax, (19.3, 10.0), "Error accumulates", size="small", bold=True, ha="left")
out = pi["outbound"]
steps = np.diff(out, axis=0)
rng = np.random.default_rng(1)
ends = []
for s in range(40):
    # each step is registered with a heading error of 6 deg (s.d.); the ant runs home along the summed estimate
    th = np.radians(rng.normal(0, 10.0, len(steps)) + rng.normal(0, 4.0))   # step noise + individual compass bias
    c, si = np.cos(th), np.sin(th)
    est = np.column_stack([c * steps[:, 0] - si * steps[:, 1], si * steps[:, 0] + c * steps[:, 1]]).sum(0)
    ends.append(out[-1] - est * rng.normal(1.0, 0.08))   # odometer scale error
ends = np.array(ends)
to3 = wb.fit([out, ends], (18.8, 1.2, 7.8, 8.2))
wb.trail(ax, to3(out), token="dna", lw=0.8, arrows=2, start="o")
e = to3(ends)
f3 = to3(out[-1:])[0]
for q in e:
    ax.plot([f3[0], q[0]], [f3[1], q[1]], color=P.edge("rna"), lw=0.4, alpha=0.6, zorder=5)
ax.scatter(e[:, 0], e[:, 1], s=10, color=P.edge("rna"), zorder=6)
n3 = to3(np.zeros((1, 2)))[0]
ax.scatter([n3[0]], [n3[1]], s=40, color=P.ink(), zorder=7)
bio.label(ax, (n3[0] - 0.5, n3[1]), "nest", size="tiny", ha="right")
