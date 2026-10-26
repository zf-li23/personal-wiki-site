"""Statins: competitive inhibition of HMG-CoA reductase, and how SREBP feedback turns it into lower plasma LDL.

A: fractional activity of HMG-CoA reductase, v/v0 = (KM + [S]) / (KM (1 + [I]/KI) + [S]), at [S] = KM, for
inhibition constants KI = 0.2, 2 and 20 nM (the range of the clinically used statins; KM for HMG-CoA is
about 4 uM). B: a minimal feedback model of a hepatocyte (illustrative parameters). SREBP activity
s = 1 / (1 + (C/K)^4) (K = 0.8) falls with cellular cholesterol C; the amounts of reductase E and of LDL receptor R
are proportional to s. Cholesterol balance: E f + U = C, where f = v/v0 is the fraction of reductase activity
left by the statin and U = 0.5 is the uptake from LDL (at steady state equal to the constant production of
LDL); plasma LDL is L = P / (kc R). As f decreases, C falls much less than f, SREBP rises, reductase protein
and LDL receptors increase, the synthesis flux E f falls less than f, and plasma LDL falls in proportion to
1/R. Values are relative to the untreated state (f = 1).
"""

import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(25.0, 9.6)

a = charts.axes_at(ax, (1.9, 1.4, 9.0, 7.0))
i = np.logspace(-2, 3, 400)
for ki, tok in ((0.2, "positive"), (2.0, "dna"), (20.0, "negative")):
    a.semilogx(i, 2 / ((1 + i / ki) + 1), color=charts.line(tok), lw=2.0, label=rf"$K_\mathrm{{I}}$ = {ki:g} nM")
a.set_ylim(0, 1.05)
a.set_xlim(1e-2, 1e3)
charts.style_axes(a, "[statin] / nM", r"$v/v_0$ (HMG-CoA at $[\mathrm{S}] = K_\mathrm{M}$)")
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "A", (0.3, 9.4))

U, K = 0.5, 0.8


def s_of(c):
    return 1 / (1 + (c / K) ** 4)


def state(f):
    c = brentq(lambda c: s_of(c) * f + U - c, 1e-6, 10)
    return c, s_of(c)


c0, s0 = state(1.0)
f = np.linspace(1.0, 0.2, 200)
C, S = np.array([state(x) for x in f]).T
b = charts.axes_at(ax, (14.4, 1.4, 9.8, 7.0))
b.plot(f, C / c0, color=charts.line("lipid"), lw=2.0, label="cellular cholesterol")
b.plot(f, S / s0, color=charts.line("dna"), lw=2.0, label="reductase protein, LDL receptors")
b.plot(f, S * f / (s0 * 1.0), color=charts.line("enzyme"), lw=2.0, ls="--", label="cholesterol synthesis flux")
b.plot(f, s0 / S, color=charts.line("negative"), lw=2.0, label="plasma LDL")
b.plot(f, f, color=P.muted(), lw=1.0, ls=":", label="direct inhibition f")
b.set_xlim(1.0, 0.2)
b.set_ylim(0, 2.2)
charts.style_axes(b, "fraction of reductase activity left by the statin, f", "relative to untreated")
b.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (12.8, 9.4))
