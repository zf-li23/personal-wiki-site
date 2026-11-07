# Simple diffusion versus carrier-mediated (facilitated) diffusion.
# A: influx against the outside concentration A (inside kept near zero). Simple diffusion through the
#    bilayer is linear, J = P A_m A. A carrier saturates: J = k3 R0 A / (A + Kd), with maximal rate k3 R0
#    reached when A >> Kd, and slope k3 R0 / Kd when A << Kd. Curves: GLUT1-like (Kd = 1.5 mM) and
#    GLUT2-like (Kd = 17 mM) carriers with the same maximal rate, and a diffusion line for comparison.
#    Shading: the normal range of blood glucose, 4-8 mM.
# B: three ways to regulate carrier flux at a fixed A = 5 mM: more carriers (R0 doubled, as when insulin
#    moves GLUT4 to the membrane), higher affinity (Kd halved), or faster turnover (k3 doubled).
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(24.0, 9.4)

bio.panel(ax, "A", (0.2, 9.3))
pa = charts.axes_at(ax, (2.2, 1.5, 8.8, 6.7))
A = np.linspace(0, 40, 400)
pa.axvspan(4, 8, color=P.mix(P.muted(), P.surface(), 0.85), lw=0)
pa.text(6, 1.08, "blood glucose", fontsize=7.5, color=P.ink(), ha="center")
pa.plot(A, A / (A + 1.5), color=charts.line("dna"), lw=1.8, label="carrier, Kd = 1.5 mM (GLUT1-like)")
pa.plot(A, A / (A + 17), color=charts.line("rna"), lw=1.8, label="carrier, Kd = 17 mM (GLUT2-like)")
pa.plot(A, A / 40, color=charts.line("neutral"), lw=1.6, ls="--", label="simple diffusion, J ∝ A")
pa.axhline(1, color=P.muted(), lw=0.7, ls=":")
pa.text(20, 1.015, "Jmax = k₃R₀", fontsize=7.5, color=P.muted(), ha="center", va="bottom")
leg = pa.legend(loc="lower right", fontsize=7.5, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pa.set_xlim(0, 40)
pa.set_ylim(0, 1.15)
charts.style_axes(pa, "outside concentration A / mM", "influx J / Jmax")
charts.title(pa, "Saturation distinguishes carriers")

bio.panel(ax, "B", (12.6, 9.3))
pb = charts.axes_at(ax, (14.6, 1.5, 8.8, 6.7))
base = 5 / (5 + 5)
vals = [base, 2 * base, 5 / (5 + 2.5), 2 * base]
labels = ["control\n(Kd = 5 mM)", "R₀ × 2\n(more carriers)", "Kd ÷ 2\n(higher affinity)", "k₃ × 2\n(faster cycle)"]
toks = ["neutral", "dna", "protein", "rna"]
pb.bar(range(4), vals, color=[P.fill(t) for t in toks], edgecolor=[P.edge(t) for t in toks], lw=1.0, width=0.6)
for i, v in enumerate(vals):
    pb.text(i, v + 0.02, f"{v / base:.2f}×", ha="center", fontsize=7.5, color=P.ink())
pb.set_xticks(range(4))
pb.set_xticklabels(labels, fontsize=7)
pb.set_ylim(0, 1.2)
charts.style_axes(pb, None, "flux at A = 5 mM (relative units)")
charts.title(pb, "Regulating a carrier")
