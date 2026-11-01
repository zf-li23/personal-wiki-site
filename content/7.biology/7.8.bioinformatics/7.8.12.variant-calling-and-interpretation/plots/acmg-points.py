# The Bayesian reading of the ACMG/AMP rules (Tavtigian and colleagues, 2018). Each evidence strength is
# worth a number of points (supporting 1, moderate 2, strong 4, very strong 8), the odds of pathogenicity
# of one supporting point are O = 350^(1/8) = 2.08, and combined evidence of P points multiplies the prior
# odds by 350^(P/8). A: the posterior probability that a variant is pathogenic against the summed points
# for three prior probabilities; the horizontal lines are the thresholds of the five classes (0.99
# pathogenic, 0.90 likely pathogenic, 0.10 and 0.001 on the benign side), and with the prior 0.10 used by
# the authors the thresholds fall at +10, +6, -1 and -7 points, which reproduces the combining rules of
# the 2015 guidelines. B: the points of the individual criteria; benign criteria count negative.
import numpy as np
import wikibio as bio
from wikibio import charts as C

ODDS1 = 350.0 ** (1 / 8)
pts = np.linspace(-10, 14, 400)
fig, ax = bio.canvas(25.0, 9.5)
a = C.axes_at(ax, (2.2, 1.5, 10.0, 7.0))
for prior, tok in ((0.02, "neutral"), (0.10, "dna"), (0.30, "negative")):
    odds = ODDS1 ** pts * prior / (1 - prior)
    a.plot(pts, odds / (1 + odds), color=C.line(tok), lw=1.6, label=f"prior {prior}")
for y, name in ((0.99, "pathogenic"), (0.90, "likely pathogenic"),
                (0.10, "likely benign"), (0.001, "benign")):
    a.axhline(y, color=C.line("neutral"), lw=0.6, ls=":")
    a.text(13.8, y, f" {name}", fontsize=bio.core.FONT["tiny"], color=bio.P.muted(), va="center", ha="right")
a.set_yscale("logit")
a.set_xlim(-10, 14)
C.style_axes(a, "summed points of evidence", "P(pathogenic | evidence)")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=bio.P.ink(), loc="upper left")
C.title(a, "A  Points to posterior probability")
b = C.axes_at(ax, (15.5, 1.5, 8.0, 7.0))
items = [("very strong (PVS1)", 8), ("strong (PS1-PS4)", 4), ("moderate (PM1-PM6)", 2),
         ("supporting (PP1-PP5)", 1), ("supporting benign (BP1-BP7)", -1),
         ("strong benign (BS1-BS4)", -4), ("stand-alone benign (BA1)", -8)]
y = np.arange(len(items))[::-1]
vals = [v for _, v in items]
b.barh(y, vals, color=[C.line("negative") if v > 0 else C.line("dna") for v in vals], height=0.6)
for yy, (name, v) in zip(y, items):
    b.text(0.3 if v > 0 else -0.3, yy, f"{v:+d}", va="center", ha="left" if v > 0 else "right",
           fontsize=bio.core.FONT["tiny"], color=bio.P.ink())
b.set_yticks(y)
b.set_yticklabels([n for n, _ in items], fontsize=bio.core.FONT["tiny"])
b.axvline(0, color=bio.P.muted(), lw=0.8)
C.style_axes(b, "points", None)
C.title(b, "B  Strength of the criteria")
for p in (-8, -7, -1, 0, 4, 6, 10):
    o = ODDS1 ** p * 0.1 / 0.9
    print(p, round(o / (1 + o), 5))
