"""The Gram stain in four steps for a Gram-positive coccus cluster and a Gram-negative rod."""
import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(27, 9.6)
POS, NEG, NONE = M.gram_token("+"), M.gram_token("-"), "neutral"
STEPS = [("1. Crystal violet", "about 1 min", POS, POS), ("2. Iodine", "about 1 min; CV–I complex forms", POS, POS),
         ("3. Ethanol", "a few seconds; decolorizes", POS, NONE), ("4. Safranin", "about 1 min; counterstain", POS, NEG)]
bio.label(ax, (0.3, 6.6), "Gram-positive", size="small", bold=True, ha="left")
bio.label(ax, (0.3, 2.9), "Gram-negative", size="small", bold=True, ha="left")
for k, (title, note, cpos, cneg) in enumerate(STEPS):
    x = 4.6 + 6.0 * k
    bio.label(ax, (x, 9.1), title, size="normal", bold=True)
    bio.label(ax, (x, 8.5), note, size="tiny", color=P.muted())
    M.cluster(ax, (x, 6.4), 0.32, n=11, token=cpos)
    for j, dx in enumerate((-1.2, 0.3, 1.5)):
        M.bacillus(ax, (x + dx, 2.7 + 0.35 * (j % 2)), 1.25, 0.45, angle=20 * (j - 1), token=cneg)
    if k < 3:
        bio.arrow(ax, (x + 2.4, 4.6), (x + 3.6, 4.6), kind="process")
bio.label(ax, (22.6, 4.7), "purple", size="tiny", color=P.muted())
bio.label(ax, (22.6, 1.3), "pink", size="tiny", color=P.muted())
bio.label(ax, (16.6, 1.3), "colorless", size="tiny", color=P.muted())
