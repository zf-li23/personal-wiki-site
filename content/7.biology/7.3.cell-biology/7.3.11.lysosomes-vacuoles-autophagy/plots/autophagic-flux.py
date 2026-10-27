"""Measuring autophagic flux with a two-compartment model (illustrative rate constants, per cell and minute).
Autophagosomes A form at rate k_f and fuse with lysosomes with rate constant k_fus; autolysosomes L are
degraded with rate constant k_d:  dA/dt = k_f - k_fus A,  dL/dt = k_fus A - k_d L.  Fed cells k_f = 0.5,
starved cells k_f = 2 (mTORC1 off), fusion-defective cells k_fus = 0.02 instead of 0.1; k_d = 0.08.
Bafilomycin A1 (blocks fusion and lysosomal degradation) is modelled as k_fus = k_d = 0 from t = 0.
(A) Autophagosomes per cell in each steady state (solid) and after bafilomycin is added at t = 0 (dashed):
the slope with bafilomycin equals k_f, the flux. (B) LC3-II (autophagosomes plus autolysosomes, arbitrary units) after 2 h
without and with bafilomycin: starvation and a fusion defect both raise LC3-II, but only starvation raises the
bafilomycin-induced increment. (C) Steady-state numbers of yellow (GFP and mRFP, autophagosomes) and red-only
(mRFP, acidic autolysosomes) puncta of the tandem mRFP-GFP-LC3 reporter."""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
kd = 0.08


def traj(kf, kfus, baf, t):
    a0, l0 = kf / kfus, kf / kd  # steady state of the condition before treatment
    if baf:
        return a0 + kf * t, np.full_like(t, l0)
    a = kf / kfus + (a0 - kf / kfus) * np.exp(-kfus * t)
    # numerical L
    l = np.empty_like(t)
    l[0] = l0
    for i in range(1, len(t)):
        dt = t[i] - t[i - 1]
        l[i] = l[i - 1] + dt * (kfus * a[i - 1] - kd * l[i - 1])
    return a, l


t = np.linspace(0, 120, 1201)
conds = [("fed", 0.5, 0.1, "positive"), ("starved", 2.0, 0.1, "negative"), ("fusion defect", 0.5, 0.02, "channel")]

fig, ax = bio.canvas(22.0, 7.6)
bio.panel(ax, "A", (0.1, 7.5))
a = charts.axes_at(ax, (1.7, 1.3, 5.6, 5.6))
for name, kf, kfus, tok in conds:
    A, L = traj(kf, kfus, False, t)
    a.plot(t, A, color=charts.line(tok), lw=1.8, label=name)
    Ab, _ = traj(kf, kfus, True, t)
    a.plot(t, Ab, color=charts.line(tok), lw=1.5, ls="--")
a.plot([], [], color=P.muted(), ls="--", label="+ bafilomycin")
a.set_xlim(0, 60)
a.set_ylim(0, 130)
a.set_xticks([0, 15, 30, 45, 60])
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "t / min", "autophagosomes per cell")

bio.panel(ax, "B", (8.0, 7.5))
b = charts.axes_at(ax, (9.6, 1.3, 5.2, 5.6))
x = 0
ticks, labels = [], []
for name, kf, kfus, tok in conds:
    A, L = traj(kf, kfus, False, t)
    Ab, Lb = traj(kf, kfus, True, t)
    v0, v1 = A[-1] + L[-1], Ab[-1] + Lb[-1]
    b.bar(x, v0, width=0.8, color=P.fill(tok), edgecolor=P.edge(tok))
    b.bar(x + 0.9, v1, width=0.8, color=P.light(tok), edgecolor=P.edge(tok), hatch="//")
    b.annotate("", xy=(x + 1.45, v1), xytext=(x + 1.45, v0),
               arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.8))
    b.text(x + 1.55, (v0 + v1) / 2, f"Δ = {v1 - v0:.0f}", fontsize=FT["tiny"], color=P.ink(), va="center", rotation=90)
    ticks += [x + 0.45]
    labels += [name]
    x += 2.6
b.set_xticks(ticks)
b.set_xticklabels(labels, fontsize=FT["tiny"])
b.text(0.02, 0.99, "solid: untreated   hatched: + bafilomycin (2 h)", transform=b.transAxes, fontsize=FT["tiny"],
       color=P.ink(), va="top")
b.set_ylim(0, 360)
charts.style_axes(b, None, "LC3-II (A + L)")

bio.panel(ax, "C", (15.6, 7.5))
c = charts.axes_at(ax, (17.2, 1.3, 4.5, 5.6))
for k, (name, kf, kfus, tok) in enumerate(conds):
    A, L = kf / kfus, kf / kd
    c.bar(k - 0.2, A, width=0.38, color=P.fill("highlight"), edgecolor=P.edge("highlight"), label="yellow (A)" if k == 0 else None)
    c.bar(k + 0.2, L, width=0.38, color=P.fill("negative"), edgecolor=P.edge("negative"), label="red only (L)" if k == 0 else None)
c.set_xticks(range(3))
c.set_xticklabels([n for n, *_ in conds], fontsize=FT["tiny"])
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
c.set_ylim(0, 32)
charts.style_axes(c, None, "puncta per cell (steady state)")
