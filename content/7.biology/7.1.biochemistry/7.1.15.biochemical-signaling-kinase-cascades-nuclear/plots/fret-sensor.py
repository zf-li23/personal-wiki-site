"""FRET biosensors for signaling.

A: efficiency of Foerster resonance energy transfer against donor-acceptor distance,
E = 1/(1 + (r/R0)^6), for Foerster radii of 4.9 nm (about that of the CFP-YFP pair) and 5.5 nm; E falls
from 90% to 10% between about 0.7 R0 and 1.4 R0, so FRET reports distances of a few nanometres.
B: a unimolecular cAMP sensor of the Epac type: the cAMP-binding domain of Epac1 between CFP (donor)
and YFP (acceptor). Without cAMP the ends are close and excitation of CFP at 433 nm gives YFP emission at
527 nm; cAMP binding changes the conformation, separates the fluorophores and restores CFP emission at
476 nm.
C: the response of such a sensor, the emission ratio CFP/YFP against [cAMP], modelled as a binding
hyperbola with an EC50 of 2.4 uM (the value reported for Epac1-camps, Nikolaev et al., 2004) and a
40% change in ratio; the sensor responds over about 0.3-20 uM; shaded: the approximate range of cytosolic [cAMP] (0.1-10 uM).
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(25.0, 8.0)

bio.panel(ax, "A", (0.1, 7.9))
pa = charts.axes_at(ax, (1.6, 1.4, 6.2, 5.8))
r = np.linspace(0, 12, 400)
for R0, tok in ((4.9, "channel"), (5.5, "positive")):
    pa.plot(r, 1 / (1 + (r / R0) ** 6), color=charts.line(tok), lw=2.0, label=f"R₀ = {R0} nm")
    pa.plot([R0], [0.5], "o", ms=4, mfc=P.fill(tok), mec=charts.line(tok))
pa.axhline(0.5, color=P.muted(), lw=0.6, ls=(0, (1, 2)))
pa.set_xlim(0, 12)
pa.set_ylim(0, 1.05)
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pa, "donor–acceptor distance r / nm", "FRET efficiency E")
charts.title(pa, "E = 1/[1 + (r/R₀)⁶]")

# B: schematic
bio.panel(ax, "B", (8.9, 7.9))


def fp(xy, tok, text):
    bio.protein(ax, xy, 1.05, 0.9, tok, text=text, size="small")


# closed state
fp((10.3, 5.4), "channel", "CFP")
fp((12.2, 5.4), "positive", "YFP")
bio.protein(ax, (11.25, 4.4), 1.4, 0.7, "neutral", text="Epac", size="tiny")
bio.label(ax, (11.25, 6.4), "no cAMP: high FRET", size="small", bold=True)
bio.arrow(ax, (9.3, 6.2), (9.8, 5.75), kind="process", color=P.edge("channel"), head=0.15)
bio.label(ax, (9.2, 6.45), "433 nm", size="tiny", color=P.muted())
bio.arrow(ax, (10.85, 5.5), (11.6, 5.5), kind="process", dashed=True, head=0.13)
bio.arrow(ax, (12.7, 5.9), (13.2, 6.4), kind="process", color=P.edge("positive"), head=0.15)
bio.label(ax, (13.45, 6.6), "527 nm", size="tiny", color=P.edge("positive"))
# open state
fp((9.9, 2.0), "channel", "CFP")
fp((12.8, 2.0), "positive", "YFP")
bio.protein(ax, (11.35, 1.3), 1.5, 0.7, "neutral", text="Epac", size="tiny")
bio.molecule(ax, (11.35, 2.0), token="highlight", text="cAMP", r=0.3, size=4.6, zorder=16)
bio.label(ax, (11.35, 3.05), "cAMP bound: low FRET", size="small", bold=True)
bio.arrow(ax, (9.0, 2.8), (9.45, 2.35), kind="process", color=P.edge("channel"), head=0.15)
bio.arrow(ax, (9.45, 1.55), (8.95, 1.05), kind="process", color=P.edge("channel"), head=0.15)
bio.label(ax, (8.85, 0.75), "476 nm", size="tiny", color=P.edge("channel"))
bio.arrow(ax, (11.3, 3.85), (11.3, 3.35), kind="process")

bio.panel(ax, "C", (15.4, 7.9))
pc = charts.axes_at(ax, (17.4, 1.4, 6.8, 5.8))
c = np.logspace(-2, 3, 400)
ratio = 1 + 0.4 * c / (2.4 + c)
pc.semilogx(c, ratio, color=charts.line("highlight"), lw=2.0)
pc.plot([2.4], [1.2], "o", ms=5, mfc=P.fill("highlight"), mec=charts.line("highlight"))
pc.text(3.0, 1.17, "EC₅₀ = 2.4 µM", fontsize=bio.core.FONT["tiny"], color=P.ink())
pc.axvspan(0.1, 10, color=P.fill("neutral"), alpha=0.35, lw=0)
pc.text(0.12, 1.37, "typical cytosolic\n[cAMP] range", fontsize=bio.core.FONT["tiny"], color=P.muted())
pc.set_xlim(1e-2, 1e3)
pc.set_ylim(0.95, 1.45)
charts.style_axes(pc, "[cAMP] / µM", "emission ratio CFP/YFP (relative)")
charts.title(pc, "Sensor calibration")
