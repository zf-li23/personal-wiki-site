# Free cortisol as a function of the CBG dissociation constant.
# Equilibrium binding of total cortisol Ct to CBG (total 700 nM) and, optionally, albumin (a low-affinity,
# effectively unsaturable binder with [Alb]/Kd_alb = 1.5): free F solves
#   Ct = F (1 + 1.5) + 700 F / (Kd + F)        (with albumin)  or   Ct = F + 700 F / (Kd + F).
# Intact CBG: Kd = 30 nM; after neutrophil elastase cleaves the reactive-centre loop: Kd = 320 nM.
# A: free fraction against Kd for Ct = 100 and 400 nM. B: local amplification alpha = F(320) / F(30)
# against total cortisol, compared with the low-saturation approximation (1 + 700/30) / (1 + 700/320) = 7.63.
import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts

P = bio.P
CBG = 700.0
ALB = 1.5


def free(Ct, Kd, alb=True):
    a = 1.0 + (ALB if alb else 0.0)
    return brentq(lambda F: a * F + CBG * F / (Kd + F) - Ct, 0.0, Ct)


fig, ax = bio.canvas(24.0, 9.6)
bio.panel(ax, "A", (0.2, 9.5))
pa = charts.axes_at(ax, (2.2, 1.5, 9.0, 6.9))
Kd = np.logspace(0, 4, 200)
for Ct, tok in ((100.0, "dna"), (400.0, "rna")):
    for alb, ls in ((False, "-"), (True, "--")):
        f = np.array([free(Ct, k, alb) for k in Kd]) / Ct
        pa.plot(Kd, f * 100, color=charts.line(tok), lw=1.6, ls=ls)
    kx, dy, ha = (120.0, 6.0, "right") if Ct > 200 else (1500.0, -8.0, "left")
    pa.text(kx, free(Ct, kx, False) / Ct * 100 + dy, f"total {Ct:.0f} nM", color=charts.line(tok),
            fontsize=7.3, ha=ha, va="center")
for k, lab in ((30, "intact CBG\nKd = 30 nM"), (320, "cleaved CBG\nKd = 320 nM")):
    pa.axvline(k, color=P.muted(), lw=0.8, ls=":")
    pa.text(k * 1.1, 92, lab, fontsize=7.0, color=P.muted(), ha="left", va="top")
pa.text(1.5, 60, "solid: CBG only\ndashed: CBG + albumin", fontsize=7.0, color=P.ink(), ha="left")
pa.set_xscale("log")
pa.set_xlim(1, 1e4)
pa.set_ylim(0, 100)
charts.style_axes(pa, "Kd of cortisol–CBG / nM", "free cortisol / % of total")
charts.title(pa, "Lowering CBG affinity releases cortisol")

bio.panel(ax, "B", (12.6, 9.5))
pb = charts.axes_at(ax, (14.6, 1.5, 8.8, 6.9))
Ct = np.linspace(20, 1200, 200)
for alb, ls, lab in ((False, "-", "CBG only"), (True, "--", "CBG + albumin")):
    al = np.array([free(c, 320, alb) / free(c, 30, alb) for c in Ct])
    pb.plot(Ct, al, color=charts.line("positive"), lw=1.7, ls=ls, label=lab)
approx = (1 + CBG / 30) / (1 + CBG / 320)
pb.axhline(approx, color=P.ink(), lw=0.8, ls=":")
pb.text(1180, approx + 0.15, f"low-saturation formula: {approx:.2f}", fontsize=7.2, color=P.ink(), ha="right",
        va="bottom")
pb.axvspan(150, 550, color=P.mix(P.muted(), P.surface(), 0.8), lw=0, zorder=0)
pb.text(350, 0.4, "usual daytime\nrange", fontsize=7.0, color=P.muted(), ha="center")
leg = pb.legend(loc="upper right", bbox_to_anchor=(1.0, 0.8), fontsize=7.3, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pb.set_xlim(0, 1200)
pb.set_ylim(0, 9)
charts.style_axes(pb, "total cortisol / nM", "amplification α = F(cleaved) / F(intact)")
charts.title(pb, "Local amplification of free cortisol")
