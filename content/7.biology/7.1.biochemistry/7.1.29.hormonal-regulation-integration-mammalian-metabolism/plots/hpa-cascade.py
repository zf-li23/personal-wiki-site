"""The top-down cascade of cortisol release (hypothalamic-pituitary-adrenal axis) and its feedback.
A stress sensed by the central nervous system makes the hypothalamus release corticotropin-releasing hormone
(CRH, nanograms) into the portal vessels of the anterior pituitary, which secretes corticotropin (ACTH,
micrograms) into the general circulation; ACTH makes the adrenal cortex release cortisol (milligrams), an
overall amplification of about a millionfold. Cortisol acts through the glucocorticoid receptor, a nuclear
receptor, on liver (induction of PEP carboxykinase and other gluconeogenic enzymes), muscle (proteolysis,
amino acids exported), adipose tissue (lipolysis) and the immune system (suppression). Dashed bars: cortisol
inhibits the release of ACTH and CRH (negative feedback), as an end product inhibits the first enzyme of a
biosynthetic pathway."""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(19.0, 10.4)
neg, ink = P.edge("negative"), P.ink()

bio.icon(ax, "servier/brain", at=(2.2, 9.0), height=1.6)
bio.label(ax, (2.2, 7.85), "CNS: stress, pain,\nhypoglycemia, infection", size="tiny", color=P.muted())
levels = [(9.0, "Hypothalamus", "CRH", "≈ ng", "neuron"), (6.6, "Anterior pituitary", "ACTH", "≈ µg", "receptor"),
          (4.2, "Adrenal cortex", "cortisol", "≈ mg", "lipid")]
X = 7.0
for y, organ, hormone, amount, tok in levels:
    bio.box(ax, (X, y), 3.6, 0.9, token=tok, text=organ, size="small")
    bio.label(ax, (X + 2.2, y - 1.2), f"{hormone} ({amount})", size="small", bold=True, ha="left")
for (y1, *_), (y2, *_) in zip(levels, levels[1:]):
    bio.arrow(ax, (X, y1 - 0.5), (X, y2 + 0.5), kind="process", color=ink, lw=1.8)
bio.arrow(ax, (3.4, 9.0), (X - 1.85, 9.0), kind="process", color=ink, lw=1.8)
bio.arrow(ax, (X, 3.7), (X, 2.6), kind="process", color=ink, lw=1.8)
# feedback
bio.arrow(ax, (X - 1.9, 3.9), (X - 1.9, 6.4), kind="inhibition", color=neg, dashed=True, bend=0.35, lw=1.4)
bio.arrow(ax, (X - 2.0, 4.1), (X - 1.9, 8.8), kind="inhibition", color=neg, dashed=True, bend=0.5, lw=1.4)
bio.label(ax, (2.6, 5.6), "negative\nfeedback", size="tiny", color=neg, bold=True)
# targets
targets = [("liver", "gluconeogenesis ↑\n(PEPCK induced)"), ("muscle", "proteolysis ↑,\namino acids out"),
           ("adipose", "lipolysis ↑"), ("immune", "inflammation ↓")]
for i, (t, txt) in enumerate(targets):
    x = 3.2 + 2.6 * i
    bio.box(ax, (x, 1.7), 2.4, 0.7, token="enzyme", text=t, size="tiny")
    bio.label(ax, (x, 0.95), txt, size="tiny", color=P.muted(), va="top")
# amplification bar
bio.label(ax, (14.8, 9.7), "amplification", size="small", bold=True)
for y, lab in [(9.0, "10⁻⁹ g"), (6.6, "10⁻⁶ g"), (4.2, "10⁻³ g")]:
    ax.plot([13.4, 16.2], [y, y], color=P.muted(), lw=0.8, ls=":")
    bio.label(ax, (16.4, y), lab, size="small", ha="left")
ax.plot([14.8, 14.8], [4.2, 9.0], color=P.edge("highlight"), lw=6, solid_capstyle="round", alpha=0.6)
bio.label(ax, (14.8, 3.4), "≈ 10⁶-fold", size="small", bold=True, color=P.edge("highlight"))
