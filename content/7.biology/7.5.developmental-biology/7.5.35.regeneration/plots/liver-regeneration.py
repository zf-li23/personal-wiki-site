"""Liver regeneration after partial hepatectomy in the mouse: a growth model (Formula 35.6.1).

A: liver mass M (fraction of the original) after removal of one third or two thirds of the liver. Model: no growth
during a priming phase of 1 day, then logistic growth dM/dt = r M (1 - M / M*) with r = 0.45 per day and the
set point M* = 1 fixed by body size; points are simulated measurements (model plus 4 % noise, seed 0), not data.
Dashed: 90 % of the original mass, reached after t90 = t_lag + ln(9 (1 - m0) / m0) / r (Example 35.6.1).
B: the order of events (schematic, shapes not fitted): hepatocytes enter S phase synchronously with a peak about
36-40 h after a two-thirds hepatectomy in the mouse; non-parenchymal cells (biliary, endothelial, stellate,
Kupffer cells) follow about a day later; the growth signals subside as the mass approaches the set point.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)
r, lag = 0.45, 1.0
t = np.linspace(0, 14, 400)


def mass(t, m0):
    tt = np.clip(t - lag, 0, None)
    return 1.0 / (1.0 + (1.0 - m0) / m0 * np.exp(-r * tt))


pa = C.axes_at(ax, (2.0, 1.6, 11.5, 6.6))
rng = np.random.default_rng(0)
td = np.array([0.5, 1, 2, 3, 4, 5, 7, 10, 14])
for m0, tok, lab in ((2 / 3, "protein", "one third removed"), (1 / 3, "negative", "two thirds removed")):
    pa.plot(t, mass(t, m0), color=Q.line_color(tok), lw=1.7, label=lab)
    pa.plot(td, mass(td, m0) * (1 + 0.04 * rng.standard_normal(len(td))), "o", ms=3.5, color=Q.line_color(tok))
    t90 = lag + np.log(9 * (1 - m0) / m0) / r
    pa.plot([t90], [0.9], marker="|", ms=10, color=Q.line_color(tok))
    pa.text(t90 + 0.2, 0.86, f"t90 = {t90:.1f} d", color=Q.line_color(tok), fontsize=FS["tiny"], va="top")
pa.axhline(0.9, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pa.set_xlim(0, 14)
pa.set_ylim(0.2, 1.1)
C.style_axes(pa, "time after hepatectomy / d", "liver mass / original")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "A", (0.2, 9.8))
bio.label(ax, (2.0, 9.4), "Logistic recovery to a set point", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (17.5, 1.6, 11.5, 6.6))
th = np.linspace(0, 168, 400)


def bump(t, peak, width):
    return np.exp(-0.5 * ((t - peak) / width) ** 2)


pb.plot(th, bump(th, 38, 9), color=Q.line_color("protein"), lw=1.7, label="hepatocytes in S phase")
pb.plot(th, 0.6 * bump(th, 64, 16), color=Q.line_color("enzyme"), lw=1.5, ls=(0, (4, 2)),
        label="non-parenchymal cells in S phase")
pb.plot(th, mass(th / 24.0, 1 / 3) * 1.0 - 1 / 3, color=Q.line_color("muted") if False else P.muted(), lw=1.0,
        label="mass gained (scaled)")
pb.axvspan(0, 24, color=P.fill("highlight"), alpha=0.35, lw=0)
pb.text(2, 1.02, "priming:\nIL-6, TNF, HGF", fontsize=FS["tiny"], color=P.ink(), va="top")
pb.set_xlim(0, 168)
pb.set_ylim(0, 1.1)
pb.set_yticks([])
C.style_axes(pb, "time after two-thirds hepatectomy / h", "relative level (schematic)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
bio.panel(ax, "B", (15.7, 9.8))
bio.label(ax, (17.5, 9.4), "Order of events", size="small", bold=True, ha="left")
