"""Sample sizes computed in the chapters (7.7.n), all instances of one formula.

n = (z_{alpha/2} + z_beta)^2 v / delta^2 (Formula 18.4.1), with (z_{0.025} + z_{0.2})^2 = 7.85 for 80 % power
and 10.51 for 90 %. Bars give the total number of units (or of events) on a logarithmic axis; the numbers
are those of the examples: estimating mean birth weight to +/- 100 g (7.7.5); a one-sample test of body
weight at 90 % power (7.7.6); a paired and an independent design for a 10 mmHg fall in blood pressure
(7.7.7); a 200 g difference in birth weight between two groups (7.7.7); one-way ANOVA with three groups and
f = 0.25 (7.7.12); low birth weight 0.25 vs 0.40 (7.7.9); the events of the veteran trial, which give 80 %
power for a hazard ratio of 1.64 (7.7.16); a prediction model for low birth weight with expected shrinkage
0.9 (7.7.21); and a 25 % relative reduction of myocardial infarction from 2.2 % (Physicians' Health Study,
7.7.18).
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

rows = [("one-sample test, 90 % power", 42, "dna", "42"),
        ("paired BP design, rho = 0.5", 32, "dna", "32 pairs"),
        ("independent BP design", 126, "dna", "2 x 63"),
        ("veteran: events for HR 1.64", 128, "protein", "128 events"),
        ("ANOVA, 3 groups, f = 0.25", 159, "enzyme", "3 x 53"),
        ("estimate mean birth weight +/- 100 g", 205, "neutral", "205"),
        ("low birth weight 0.25 vs 0.40", 304, "rna", "2 x 152"),
        ("prediction model, shrinkage 0.9", 332, "highlight", "332"),
        ("birth weight, 200 g difference", 408, "dna", "2 x 204"),
        ("PHS: 25 % fewer infarctions", 19600, "rna", "2 x 9800")]

fig = plt.figure(figsize=(10.0, 4.6))
ax = fig.add_axes([0.33, 0.13, 0.62, 0.80])
y = np.arange(len(rows))[::-1]
for yy, (name, n, tok, txt) in zip(y, rows):
    ax.barh(yy, n, color=P.fill(tok), edgecolor=charts.line(tok), height=0.62)
    ax.text(-0.02, yy, name, ha="right", va="center", fontsize=FT["tiny"], color=P.ink(),
            transform=ax.get_yaxis_transform())
    ax.text(n * 1.1, yy, txt, va="center", fontsize=FT["tiny"], color=P.ink())
ax.set_xscale("log")
ax.set_xlim(10, 1e5)
ax.set_yticks([])
ax.set_ylim(-0.6, len(rows) - 0.4)
charts.style_axes(ax, "total units (or events)")
charts.title(ax, r"$n = (z_{\alpha/2} + z_\beta)^2\,v/\delta^2$: the design sets $v$, the question sets $\delta$", loc="right")
