"""Duty ratio and processivity of myosins.

A: probability that at least one of N independent heads is bound to actin, 1 - (1 - r)^N, for the duty
ratio r of skeletal-muscle myosin II (about 0.04), a non-muscle myosin II (0.2) and myosin V (0.7). A
two-headed motor with r = 0.7 almost always has a head attached: it can walk alone (processive);
myosin II needs tens of heads per filament (a thick filament has about 300).
B: simulated sliding velocity of an actin filament driven by N skeletal myosin II heads cycling
independently (step d = 5 nm, attached time t_on = 1 ms, r = 0.04; 200 ms per point): each attached head
moves the filament by d during its attached time, so the filament slides at d / t_on whenever at least
one head is bound and stops when none is (no inertia at low Reynolds number). With enough heads
the velocity saturates at d / t_on = 5 um/s, set by how fast heads detach, not by their number
(Uyeda, Kron and Spudich 1990); below that it falls as attachment becomes intermittent.
C: a simulated trace of myosin V walking hand-over-hand at 1 uM ATP: the centre of the molecule moves in
36 nm steps; a fluorescent label on one head moves 72 nm on every second step (as measured by Yildiz et
al. 2003). Dwell times are exponential, set mainly by ADP release and ATP binding.
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
rng = np.random.default_rng(2)
fig, ax = bio.canvas(27.0, 8.6)

bio.panel(ax, "A", (0.1, 8.5))
pa = charts.axes_at(ax, (1.8, 1.4, 6.6, 6.0))
N = np.arange(1, 101)
for r, tk, name in ((0.04, "actin", "myosin II, muscle (r ≈ 0.04)"), (0.2, "drug", "non-muscle myosin II (0.2)"),
                    (0.7, "protein", "myosin V (0.7)")):
    pa.semilogx(N, 1 - (1 - r) ** N, color=quant.line_color(tk), lw=1.8, label=name)
pa.set_ylim(0, 1.05)
pa.set_xticks([1, 2, 10, 100])
pa.set_xticklabels(["1", "2", "10", "100"])
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(pa, "number of heads N", "P(at least one head bound)")
charts.title(pa, "Duty ratio")

bio.panel(ax, "B", (9.5, 8.5))
pb = charts.axes_at(ax, (11.2, 1.4, 6.6, 6.0))
d, ton, r = 5.0, 1e-3, 0.04
toff = ton * (1 - r) / r
dt, T = 2e-5, 0.2
Ns = np.array([1, 2, 4, 8, 16, 32, 64, 128])
vs = []
for n in Ns:
    bound = rng.uniform(size=n) < r
    x, blocked = 0.0, 0
    for _ in range(int(T / dt)):
        # an attached head moves the filament by d during its attached time t_on: the filament slides at
        # v0 = d / t_on whenever at least one head is bound, and stops (no inertia) when none is
        new = (~bound) & (rng.uniform(size=n) < dt / toff)
        rel = bound & (rng.uniform(size=n) < dt / ton)
        bound = (bound | new) & ~rel
        x += (d / ton) * dt if bound.any() else 0.0
    vs.append(x / T)
vs = np.array(vs) * 1e-3
vmax = d / ton * 1e-3
model = vmax * (1 - (1 - r) ** Ns)
pb.semilogx(Ns, vs, "o", color=quant.line_color("actin"), ms=5, label="simulation")
NN = np.logspace(0, np.log10(128), 100)
pb.semilogx(NN, vmax * (1 - (1 - r) ** NN), color=quant.line_color("muted"), lw=1.2, label="(d/t_on)(1 − (1 − r)^N)")
pb.set_xticks([1, 10, 100])
pb.set_xticklabels(["1", "10", "100"])
pb.set_ylim(0, 6.5)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pb, "number of heads N", "sliding velocity / (µm s⁻¹)")
charts.title(pb, "Many weak motors")

bio.panel(ax, "C", (19.0, 8.5))
pc = charts.axes_at(ax, (20.6, 1.4, 5.8, 6.0))
k_adp, k_atp = 12.0, 0.9 * 1.0  # per s: ADP release, ATP binding at 1 uM (0.9 per uM per s)
t, pos, head = [0.0], [0.0], [0.0]
tt = 0.0
for step in range(14):
    tt += rng.exponential(1 / k_adp) + rng.exponential(1 / k_atp)
    t.append(tt)
    pos.append(pos[-1] + 36)
    head.append(head[-1] + (72 if step % 2 == 0 else 0))
pc.step(t, pos, where="post", color=quant.line_color("protein"), lw=1.6, label="centre of mass (36 nm)")
pc.step(t, head, where="post", color=quant.line_color("highlight"), lw=1.4, ls=(0, (4, 2)), label="labelled head (72 nm)")
pc.set_xlim(0, t[-1])
pc.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pc, "time / s", "position / nm")
charts.title(pc, "Myosin V walks hand over hand")
