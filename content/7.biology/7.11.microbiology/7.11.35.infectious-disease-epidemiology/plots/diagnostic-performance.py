# Reading a diagnostic test: predictive values against pre-test probability, a worked case, and the timing
# of nucleic acid, antigen and antibody detection.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(19.0, 7.1)

SE, SP = 0.99, 0.98

# ---------------------------------------------------------------- A: predictive values
bio.panel(ax, "A", (0.1, 6.85))
bio.label(ax, (4.0, 6.8), "Predictive value and prevalence", size="small", bold=True)
pA = quant.Plot(ax, (1.6, 1.0, 4.6, 4.2), xlim=(1e-4, 1.0), ylim=(0, 1.0), xlog=True,
                xlabel="pre-test probability", ylabel="P(result correct)",
                xticks=[(1e-4, "0.01 %"), (1e-2, "1 %"), (1.0, "100 %")],
                yticks=[(0, "0"), (0.5, "50 %"), (1.0, "100 %")], ylabel_offset=1.3)
pi = np.logspace(-4, -0.0001, 400)
ppv = SE * pi / (SE * pi + (1 - SP) * (1 - pi))
npv = SP * (1 - pi) / (SP * (1 - pi) + (1 - SE) * pi)
pA.line(pi, ppv, "negative", text="positive predictive value", at=0.62, size="tiny", dy=-0.35)
pA.line(pi, npv, "positive", text="negative predictive value", at=0.1, size="tiny", dy=-0.35)
pA.hline(0.5, dashed=True)
cross = (1 - SP) / (SE + 1 - SP)
pA.vline(cross, token="muted", dashed=True)
bio.label(ax, (pA.X(cross) + 0.1, pA.Y(0.18)), "below ≈2 %: most\npositives are false",
          size="tiny", ha="left", color=P.muted())
bio.label(ax, (4.0, 6.35), f"sensitivity {SE:.0%}, specificity {SP:.0%}", size="tiny", color=P.muted())

# ---------------------------------------------------------------- B: a worked case, as counts
bio.panel(ax, "B", (6.7, 6.85))
bio.label(ax, (10.5, 6.8), "The same test in two populations", size="small", bold=True)
for j, (pi0, name) in enumerate(((0.005, "screening: prevalence 0.5 %"), (0.30, "symptomatic: prevalence 30 %"))):
    N = 10000
    tp, fn = SE * pi0 * N, (1 - SE) * pi0 * N
    fp, tn = (1 - SP) * (1 - pi0) * N, SP * (1 - pi0) * N
    y = 4.4 - j * 2.5
    bio.label(ax, (7.0, y + 1.0), name, size="tiny", bold=True, ha="left")
    x = 7.0
    total = tp + fp
    for value, tok, lab in ((tp, "positive", "true positives"), (fp, "negative", "false positives")):
        w = 6.2 * value / max(total, 1)
        bio.box(ax, (x + w / 2, y + 0.35), w, 0.7, token=tok, radius=0.1)
        if w > 1.0:
            bio.label(ax, (x + w / 2, y + 0.35), f"{value:.0f}", size="tiny", color=P.on_fill())
        x += w
    bio.label(ax, (7.0, y - 0.3), f"of {tp + fp:.0f} positive results, {100 * tp / (tp + fp):.0f} % are true "
                                  f"(per 10 000 tested)", size="tiny", ha="left", color=P.muted())
bio.label(ax, (7.0, 0.5), "green: true positives   red: false positives", size="tiny", ha="left", color=P.muted())

# ---------------------------------------------------------------- C: what is detectable when
bio.panel(ax, "C", (13.3, 6.85))
bio.label(ax, (16.5, 6.8), "What is detectable, and when", size="small", bold=True)
pC = quant.Plot(ax, (14.3, 1.0, 4.2, 4.2), xlim=(-3, 40), ylim=(0, 1.15),
                xlabel="days from infection", ylabel="signal (arbitrary)",
                xticks=[0, 10, 20, 30, 40], yticks=[])
t = np.linspace(-3, 40, 500)
nucleic = np.exp(-0.5 * ((t - 6) / 4.5) ** 2) * (t > 0)
antigen = 0.85 * np.exp(-0.5 * ((t - 7) / 3.0) ** 2) * (t > 2)
antibody = 1.0 / (1 + np.exp(-(t - 15) / 2.2))
pC.line(t, nucleic, "dna", text="nucleic acid (PCR)", at=0.35, size="tiny", dy=0.3)
pC.line(t, antigen, "enzyme", text="antigen", at=0.3, size="tiny", dy=-0.55)
pC.line(t, antibody, "antibody", text="antibody", at=0.8, size="tiny", dy=0.3)
pC.vline(0, token="muted", dashed=True, text="infection")
bio.label(ax, (16.5, 6.35), "a negative test taken too early means little; antibody\nmeans exposure, not current infection", size="tiny", color=P.muted())
