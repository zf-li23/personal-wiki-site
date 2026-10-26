"""Receptor occupancy and response in the operational model (Black and Leff, 1983).

Occupancy theta = [A]/(KA + [A]); response E/Emax = tau [A]/(KA + (1 + tau)[A]), where the efficacy
tau is the number of receptors times the coupling efficiency of each. Concentrations in units of KA.
A: an agonist with high efficacy (tau = 30) gives the full response at low occupancy: its EC50 is
KA/(1 + tau), thirtyfold below KA ("spare receptors"); lower efficacy (tau = 3) still gives almost the
full response; a partial agonist (tau = 0.5) cannot exceed a third of the maximum even at full occupancy.
B: a competitive antagonist B (dissociation constant KB) shifts the curve of the full agonist to the
right in parallel without lowering the maximum; each tenfold increase in [B]/KB shifts it about tenfold
(the dose ratio is r = 1 + [B]/KB, the Schild relation).
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(20.0, 7.8)
a = np.logspace(-4, 3, 400)


def resp(a, tau):
    return tau * a / (1 + (1 + tau) * a)


bio.panel(ax, "A", (0.1, 7.7))
pa = charts.axes_at(ax, (1.7, 1.4, 7.4, 5.6))
pa.semilogx(a, a / (1 + a), color=P.muted(), lw=1.4, ls=(0, (4, 2.4)), label="occupancy θ")
for tau, tok, name in ((30, "enzyme", "full agonist, τ = 30"), (3, "channel", "agonist, τ = 3"), (0.5, "negative", "partial agonist, τ = 0.5")):
    pa.semilogx(a, resp(a, tau), color=charts.line(tok), lw=1.8, label=name)
    ec = 1 / (1 + tau)
    pa.plot([ec], [resp(ec, tau)], "o", ms=4, mfc=P.fill(tok), mec=charts.line(tok))
pa.axvline(1, color=P.muted(), lw=0.6, ls=(0, (1, 2)))
pa.text(1.15, 0.03, r"$K_\mathrm{A}$", fontsize=bio.core.FONT["tiny"], color=P.muted())
pa.set_xlim(1e-4, 1e3)
pa.set_ylim(0, 1.05)
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pa, r"agonist concentration [A] / $K_\mathrm{A}$", r"response $E/E_{\max}$ (or occupancy)")
charts.title(pa, "Efficacy and spare receptors")

bio.panel(ax, "B", (10.6, 7.7))
pb = charts.axes_at(ax, (12.2, 1.4, 7.2, 5.6))
toks = ["enzyme", "protein", "drug", "negative"]
for b, tok in zip((0, 3, 30, 300), toks):
    pb.semilogx(a, resp(a / (1 + b), 30), color=charts.line(tok), lw=1.8, label=f"[B]/$K_\\mathrm{{B}}$ = {b}")
pb.set_xlim(1e-4, 1e3)
pb.set_ylim(0, 1.05)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pb, r"agonist concentration [A] / $K_\mathrm{A}$", r"response $E/E_{\max}$")
charts.title(pb, "Competitive antagonist (τ = 30)")
