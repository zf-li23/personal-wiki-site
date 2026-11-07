# Two-compartment model of growth hormone elimination after an intravenous bolus.
# Central compartment (free GH in plasma) x1, peripheral compartment x2 (GH bound to GH-binding protein
# and distributed in the extravascular space):
#   dx1/dt = -(k10 + k12) x1 + k21 x2,   dx2/dt = k12 x1 - k21 x2,
# with elimination (receptor-mediated uptake, renal filtration, hepatic degradation) only from x1.
# Illustrative rate constants (per min): k10 = 0.06, k12 = 0.05, k21 = 0.08, giving a fast phase with
# t1/2 ~ 4 min and a slow phase with t1/2 ~ 23 min (measured GH half-lives are ~ 15-25 min).
# Mean residence time MRT = (1 / k10) (1 + k12 / k21). The dashed curve doubles k12 (more binding).
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P


def solve(k10, k12, k21, t):
    M = np.array([[-(k10 + k12), k21], [k12, -k21]])
    w, V = np.linalg.eig(M)
    c = np.linalg.solve(V, np.array([1.0, 0.0]))
    X = (V * c) @ np.exp(np.outer(w, t))
    return X[0].real, X[1].real, -w.real


fig, ax = bio.canvas(24.0, 9.6)
t = np.linspace(0, 150, 600)

bio.panel(ax, "A", (0.2, 9.5))
pa = charts.axes_at(ax, (2.2, 1.5, 9.0, 6.9))
x1, x2, lam = solve(0.06, 0.05, 0.08, t)
pa.semilogy(t, x1, color=charts.line("dna"), lw=1.8, label="central: free GH in plasma")
pa.semilogy(t, x2, color=charts.line("protein"), lw=1.5, label="peripheral: bound / extravascular")
pa.semilogy(t, x1 + x2, color=P.muted(), lw=1.0, ls=":", label="total in body")
lam_s = lam.min()
A2 = x1[-1] / np.exp(-lam_s * t[-1])
pa.semilogy(t, A2 * np.exp(-lam_s * t), color=charts.line("dna"), lw=0.8, ls="--")
th = np.log(2) / np.sort(lam)[::-1]
pa.text(4, 0.6, f"fast phase: t½ = {th[0]:.1f} min", fontsize=7.3, color=charts.line("dna"))
pa.text(70, 0.13, f"slow phase: t½ = {th[1]:.0f} min", fontsize=7.3, color=charts.line("dna"))
leg = pa.legend(loc="lower left", fontsize=7.2, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pa.set_xlim(0, 150)
pa.set_ylim(5e-3, 1.2)
charts.style_axes(pa, "time after bolus / min", "amount / dose")
charts.title(pa, "Bi-exponential decay of a GH bolus")

bio.panel(ax, "B", (12.6, 9.5))
pb = charts.axes_at(ax, (14.6, 1.5, 8.8, 6.9))
for k12, ls, lab in ((0.05, "-", "k12 = 0.05 /min"), (0.10, "--", "k12 = 0.10 /min (more binding)")):
    y1, y2, lm = solve(0.06, k12, 0.08, t)
    mrt = (1 / 0.06) * (1 + k12 / 0.08)
    pb.semilogy(t, y1, color=charts.line("dna"), lw=1.7, ls=ls, label=f"{lab}; MRT = {mrt:.0f} min")
leg = pb.legend(loc="upper right", fontsize=7.2, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pb.set_xlim(0, 150)
pb.set_ylim(5e-4, 1.2)
charts.style_axes(pb, "time after bolus / min", "plasma free GH / dose")
charts.title(pb, "A reversible binding pool slows elimination")
