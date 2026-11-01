"""The usual hierarchy of evidence for questions about the effect of an exposure or a treatment
(schematic). Designs higher in the pyramid control bias better: randomization in trials removes
confounding, and systematic reviews combine trials. The ranking is a rule of thumb, not a law: a large,
well-conducted cohort study can be more informative than a small, biased trial.
"""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(16, 9.2)
levels = [
    ("Meta-analysis", "highlight"),
    ("Randomized controlled trial", "positive"),
    ("Cohort study", "dna"),
    ("Case-control study", "dna2"),
    ("Cross-sectional study", "neutral"),
    ("Case series and case reports", "neutral"),
    ("Expert opinion, mechanistic reasoning", "neutral"),
]
n = len(levels)
base, top, h = 13.0, 1.6, 1.15
x0 = 1.2
for i, (name, tok) in enumerate(levels):
    y0 = 0.4 + (n - 1 - i) * h
    w_lo = base - (base - top) * (n - 1 - i) / n
    w_hi = base - (base - top) * (n - i) / n
    cx = x0 + base / 2
    verts = [(cx - w_lo / 2, y0), (cx + w_lo / 2, y0), (cx + w_hi / 2, y0 + h * 0.92), (cx - w_hi / 2, y0 + h * 0.92)]
    bio.core.shape(ax, verts, token=tok)
    bio.label(ax, (cx, y0 + h * 0.46), name, size="small", color=P.on_fill())
ax.annotate("", xy=(15.2, 0.6 + (n - 0.3) * h), xytext=(15.2, 0.6), arrowprops=dict(arrowstyle="->", color=P.muted(), lw=1.0))
bio.label(ax, (15.55, 0.4 + n * h / 2), "less bias, stronger causal evidence", size="tiny", color=P.muted(), rotation=90)
def bracket(i_top, i_bot, text, vertical=True):
    y_hi = 0.4 + (n - i_top) * h - 0.12
    y_lo = 0.4 + (n - 1 - i_bot) * h + 0.06
    ax.plot([1.0, 0.8, 0.8, 1.0], [y_hi, y_hi, y_lo, y_lo], color=P.muted(), lw=0.9)
    if vertical:
        bio.label(ax, (0.45, (y_hi + y_lo) / 2), text, size="tiny", color=P.muted(), rotation=90)
    else:
        bio.label(ax, (1.25, (y_hi + y_lo) / 2), text, size="tiny", color=P.muted(), ha="left")


bracket(0, 0, "synthesis of trials", vertical=False)
bracket(1, 1, "experiment", vertical=False)
bracket(2, 5, "observational studies")
