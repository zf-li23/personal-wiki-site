"""The bicyclic cascade that controls bacterial glutamine synthetase (GS), and its input-output response.

A (SBGN activity flow): the bifunctional uridylyltransferase/uridylyl-removing enzyme (UT/UR, GlnD) adds UMP to
the regulatory protein PII when alpha-ketoglutarate and ATP are high and removes it when glutamine and Pi are
high. PII-UMP stimulates the deadenylylating activity of adenylyltransferase (AT, GlnE), which activates GS;
unmodified PII stimulates its adenylylating activity, which inactivates GS (adenylylated Tyr397 makes GS
sensitive to its eight cumulative feedback inhibitors). PII-UMP also activates transcription of glnA
through the NtrB/NtrC two-component system.
B: steady-state fraction of active (deadenylylated) GS as a function of the [glutamine]/[alpha-ketoglutarate]
ratio. Each covalent-modification cycle is modelled with Michaelis-Menten converter enzymes
(Goldbeter-Koshland function G(v1, v2, J1, J2)); the ratio of the forward to the reverse converter activity in
the first cycle is proportional to [alpha-KG]/[Gln]; in the second cycle the deadenylylation/adenylylation
ratio is proportional to u/(1 - u), where u is the fraction of PII uridylylated. A single cycle with
unsaturated enzymes (J = 1) responds hyperbolically; two cycles in series are steeper, and saturation of
the converter enzymes (J = 0.2, zero-order ultrasensitivity) makes the response switch-like. Apparent Hill
coefficients nH = log 81 / log(x90/x10) are given in the legend. Parameters are illustrative.
"""

import numpy as np

import wikibio as bio
from wikibio import charts, network

P = bio.P
fig, ax = bio.canvas(27.0, 11.0, scale=0.42)
bio.panel(ax, "A", (0.2, 10.8))
d = network.Diagram(ax, size="small")
d.simple_chemical("akg", (1.8, 9.4), "α-KG,\nATP", r=0.85, token="metabolite")
d.simple_chemical("gln", (1.8, 6.4), "Gln, Pᵢ", r=0.85, token="metabolite")
d.activity("ut", (5.2, 9.4), "UT activity\n(GlnD)", token="enzyme", w=2.8, h=1.2)
d.activity("ur", (5.2, 6.4), "UR activity\n(GlnD)", token="enzyme", w=2.8, h=1.2)
d.activity("piiu", (8.9, 9.4), "PII–UMP", token="protein", w=2.4)
d.activity("pii", (8.9, 6.4), "PII", token="protein", w=2.4)
d.activity("dead", (12.9, 9.4), "AT: deadenylylation", token="positive", w=3.8)
d.activity("adn", (12.9, 6.4), "AT: adenylylation", token="negative", w=3.8)
d.activity("gs", (12.9, 3.0), "GS activity", token="highlight", w=3.2)
d.activity("fb", (7.4, 3.0), "8 feedback inhibitors\n(cumulative)", token="drug", w=4.2, h=1.2)
d.connect("akg", "ut", "positive")
d.connect("gln", "ur", "positive")
d.connect("ut", "piiu", "positive")
d.connect("ur", "pii", "positive")
d.connect("piiu", "dead", "positive")
d.connect("pii", "adn", "positive")
d.connect("adn", "gs", "negative")
d.connect("dead", "gs", "positive", via=[(15.3, 9.4), (15.3, 3.0)])
d.connect("fb", "gs", "negative")
d.connect("piiu", "pii", "unknown", text="interconversion", text_offset=(0.9, 0.0))
bio.label(ax, (7.4, 1.4), "adenylylated GS is more sensitive to the feedback inhibitors", size="tiny",
          color=P.muted())

bio.panel(ax, "B", (16.4, 10.8))


def gk(v1, v2, j1, j2):
    b = v2 - v1 + j1 * v2 + j2 * v1
    return 2 * v1 * j2 / (b + np.sqrt(b * b - 4 * (v2 - v1) * v1 * j2))


x = np.logspace(-2, 2, 801)  # [Gln]/[alpha-KG]
c = charts.axes_at(ax, (18.0, 1.6, 8.4, 8.2))
for name, j, two, tok in (("one cycle, J = 1", 1.0, False, "neutral"), ("two cycles, J = 1", 1.0, True, "dna"),
                          ("two cycles, J = 0.2", 0.2, True, "negative")):
    u = gk(1 / x, 1.0, j, j)
    a = gk(u, 1 - u + 1e-9, j, j) if two else u
    lo, hi = np.interp(0.1, a[::-1], x[::-1]), np.interp(0.9, a[::-1], x[::-1])
    nh = np.log(81) / np.log(lo / hi)
    c.semilogx(x, a, color=charts.line(tok), lw=2.0, label=f"{name} (nH ≈ {nh:.1f})")
c.set_xlim(1e-2, 1e2)
c.set_ylim(-0.02, 1.05)
charts.style_axes(c, "[glutamine] / [α-ketoglutarate] (relative)", "fraction of GS active")
c.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
