"""Dynamic instability: the two-state model of Dogterom and Leibler (1993).

A microtubule end grows at v_g, switches to shrinkage (catastrophe) at rate f_cat, shrinks at v_s and
switches back to growth (rescue) at rate f_res; a microtubule that shrinks to zero length is renucleated
at once (a centrosome nucleates continuously). Parameters typical of interphase cells: v_g = 10 um/min,
v_s = 20 um/min, f_cat = 0.06 per s, f_res = 0.05 per s (bounded regime, v_s f_cat > v_g f_res).
A: length against time for three microtubules (Monte Carlo, time step 0.05 s).
B: distribution of lengths of 4000 microtubules at steady state (bars) against the exponential with mean
<L> = v_g v_s / (v_s f_cat - v_g f_res) (line).
C: mean length against the rescue rate; it diverges at the transition to unbounded growth,
f_res = v_s f_cat / v_g (dashed), beyond which the mean length grows at J = (v_g f_res - v_s f_cat) /
(f_cat + f_res).
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
rng = np.random.default_rng(4)
vg, vs = 10 / 60, 20 / 60  # um/s
fcat, fres = 0.06, 0.05
dt = 0.05


def simulate(n, T, fres=fres, record=False):
    L = np.zeros(n)
    grow = np.ones(n, bool)
    trace = []
    for i in range(int(T / dt)):
        u = rng.uniform(size=n)
        switch = np.where(grow, u < fcat * dt, u < fres * dt)
        grow = grow ^ switch
        L = L + np.where(grow, vg, -vs) * dt
        dead = L <= 0
        L[dead] = 0
        grow[dead] = True
        if record:
            trace.append(L.copy())
    return L, np.array(trace)


fig, ax = bio.canvas(27.0, 8.4)
bio.panel(ax, "A", (0.1, 8.3))
pa = charts.axes_at(ax, (1.8, 1.4, 7.2, 6.0))
_, tr = simulate(3, 600, record=True)
t = np.arange(tr.shape[0]) * dt / 60
for k, tk in enumerate(("channel", "protein", "enzyme")):
    pa.plot(t, tr[:, k], color=quant.line_color(tk), lw=1.2)
pa.set_xlim(0, 10)
charts.style_axes(pa, "time / min", "length / µm")
charts.title(pa, "Growth, catastrophe, shrinkage, rescue")

bio.panel(ax, "B", (10.2, 8.3))
pb = charts.axes_at(ax, (11.9, 1.4, 6.4, 6.0))
Ls, _ = simulate(4000, 900)
mean = vg * vs / (vs * fcat - vg * fres)
pb.hist(Ls, bins=np.linspace(0, 30, 31), density=True, color=P.fill("channel"), edgecolor=P.edge("channel"), lw=0.5)
x = np.linspace(0, 30, 200)
# lengths in the growing and shrinking states share the same exponential (plus an atom near zero)
pb.plot(x, np.exp(-x / mean) / mean, color=quant.line_color("ink"), lw=1.4, label=f"exponential, ⟨L⟩ = {mean:.1f} µm")
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
pb.text(12, 0.06, f"simulated mean {Ls.mean():.1f} µm", fontsize=bio.core.FONT["tiny"], color=P.muted())
charts.style_axes(pb, "length / µm", "probability density / µm⁻¹")
charts.title(pb, "Steady-state length distribution")

bio.panel(ax, "C", (19.5, 8.3))
pc = charts.axes_at(ax, (21.2, 1.4, 5.4, 6.0))
fr = np.linspace(0.0, 0.115, 200)
crit = vs * fcat / vg
mL = np.where(fr < crit, vg * vs / np.maximum(vs * fcat - vg * fr, 1e-9), np.nan)
pc.plot(fr, mL, color=quant.line_color("channel"), lw=1.8)
pc.axvline(crit, color=quant.line_color("muted"), lw=0.9, ls=(0, (3, 2)))
pc.text(crit + 0.003, 40, "unbounded\ngrowth", fontsize=bio.core.FONT["tiny"], color=P.muted())
pc.plot([fres], [mean], "o", color=quant.line_color("ink"), ms=4)
pc.set_ylim(0, 60)
charts.style_axes(pc, "rescue frequency / s⁻¹", "mean length / µm")
charts.title(pc, "Bounded and unbounded regimes")
