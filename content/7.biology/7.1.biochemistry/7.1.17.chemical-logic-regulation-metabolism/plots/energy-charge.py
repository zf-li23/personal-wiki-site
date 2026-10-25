"""The adenylate system and the energy charge EC = ([ATP] + [ADP]/2)/([ATP] + [ADP] + [AMP]).

A: composition against EC with adenylate kinase at equilibrium, [ATP][AMP]/[ADP]^2 = K' = 1.
B: model responses to EC at a total adenylate pool of 5 mM (illustrative parameters):
   R-type (ATP-regenerating, PFK-like): four-site MWC enzyme at fixed substrate (alpha = S/K_R = 1,
   c = 0.01), L_app = L0 (1 + [ATP]/K_ATP)^4 / (1 + [AMP]/K_AMP)^4, L0 = 0.05, K_ATP = 1 mM,
   K_AMP = 0.1 mM;
   U-type (ATP-using): v = [ATP]/(K_M (1 + [ADP]/K_ADP) + [ATP]), K_M = 1 mM, K_ADP = 0.1 mM.
   Each curve scaled to its maximum.
C: fold increase in [AMP] when [ATP] falls by a fraction delta, total adenylate constant, adenylate
   kinase at equilibrium (K' = 1), for initial [ATP]/[ADP] = 5, 10, 30."""

import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P


def comp(EC, K=1.0):
    """Fractions (ATP, ADP, AMP) at energy charge EC with K' = [ATP][AMP]/[ADP]^2."""
    hi = min(2 * EC, 2 * (1 - EC))
    if hi < 1e-12:
        return (EC, 0.0, 1 - EC)

    def f(d):
        a = EC - d / 2
        return a * (1 - a - d) - K * d * d
    d = brentq(f, 0.0, hi)
    a = EC - d / 2
    return a, d, 1 - a - d


ec = np.linspace(0.0, 1.0, 401)
fr = np.array([comp(e) for e in ec])

fig, ax = bio.canvas(23.0, 8.6)
bio.panel(ax, "A", (0.1, 8.4))
a = charts.axes_at(ax, (1.5, 1.2, 5.6, 6.4))
a.axvspan(0.8, 0.95, color=P.fill("highlight"), alpha=0.35, lw=0)
for k, (name, tok) in enumerate((("ATP", "atp"), ("ADP", "enzyme"), ("AMP", "drug"))):
    a.plot(ec, fr[:, k], color=charts.line(tok), lw=2.0, label=name)
a.set_xlim(0, 1)
a.set_ylim(0, 1.02)
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper center")
charts.style_axes(a, "energy charge", "fraction of adenylate pool")
charts.title(a, "Adenylate kinase at equilibrium")

bio.panel(ax, "B", (8.2, 8.4))
b = charts.axes_at(ax, (9.5, 1.2, 5.6, 6.4))
T = 5.0
atp, adp, amp = fr[:, 0] * T, fr[:, 1] * T, fr[:, 2] * T
alpha, c, L0 = 1.0, 0.01, 0.05
L = L0 * (1 + atp / 1.0) ** 4 / (1 + amp / 0.1) ** 4
vr = alpha * (1 + alpha) ** 3 / ((1 + alpha) ** 4 + L * (1 + c * alpha) ** 4)
vu = atp / (1.0 * (1 + adp / 0.1) + atp)
b.axvspan(0.8, 0.95, color=P.fill("highlight"), alpha=0.35, lw=0)
b.plot(ec, vr / vr.max(), color=charts.line("enzyme"), lw=2.0, label="R-type (regenerates ATP)")
b.plot(ec, vu / vu.max(), color=charts.line("drug"), lw=2.0, label="U-type (uses ATP)")
b.set_xlim(0, 1)
b.set_ylim(0, 1.05)
b.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center left")
charts.style_axes(b, "energy charge", "relative rate")
charts.title(b, "Two types of response")

bio.panel(ax, "C", (16.2, 8.4))
cc = charts.axes_at(ax, (17.5, 1.2, 5.0, 6.4))
dl = np.linspace(0, 0.3, 61)
for r, tok in ((5, "neutral"), (10, "enzyme"), (30, "drug")):
    d0 = 1.0 / r
    m0 = d0 * d0  # [ATP] = 1 (scale), [AMP] = K [ADP]^2/[ATP]
    tot = 1 + d0 + m0
    fold = []
    for x in dl:
        A = 1 - x
        rest = tot - A
        d = (-A + np.sqrt(A * A + 4 * A * rest)) / 2  # A*m = d^2, d + m = rest
        fold.append((rest - d) / m0)
    cc.plot(dl * 100, fold, color=charts.line(tok), lw=2.0, label=f"[ATP]/[ADP] = {r}")
cc.set_yscale("log")
cc.set_xlim(0, 30)
cc.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(cc, "fall in [ATP] / %", "fold increase in [AMP]")
charts.title(cc, "AMP amplifies the signal")
