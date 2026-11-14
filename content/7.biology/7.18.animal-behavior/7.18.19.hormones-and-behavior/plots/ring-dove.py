"""Reciprocal interactions between hormones and behavior in the reproductive cycle of the ring dove (Streptopelia
risoria), after Lehrman (1965) and Silver (1978). Stimuli from the partner and the nest act through the brain on
the pituitary and gonads; the hormones change behavior, and the new behavior provides the stimuli for the next
stage. Boxes: behavior (top row) and hormones (bottom row); arrows: the main causal links."""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(25, 9.6)
beh = [("Male courtship\n(bow-cooing)", 2.4), ("Nest building\n(both sexes)", 7.6), ("Egg laying", 12.4),
       ("Incubation\n(both sexes)", 17.0), ("Feeding squabs\ncrop milk", 22.2)]
hor = [("FSH, LH ->\nestradiol (female)", 4.9), ("progesterone", 10.0), ("prolactin", 19.6)]
yb, yh = 7.0, 2.6
for t, x in beh:
    bio.box(ax, (x, yb), 4.0, 1.5, "neutral", text=t, size="small")
for t, x in hor:
    bio.box(ax, (x, yh), 3.9, 1.5, "drug", text=t, size="small")


def arr(a, b, bend=0.0, kind="activation"):
    bio.arrow(ax, a, b, kind=kind, bend=bend, shrink=0.05)


arr((3.0, 6.2), (4.4, 3.4))       # courtship -> estradiol
arr((5.4, 3.4), (7.0, 6.2))       # estradiol -> nest building
arr((8.2, 6.2), (9.6, 3.4))       # nest building -> progesterone
arr((10.4, 3.4), (12.0, 6.2))     # progesterone -> laying
arr((10.6, 3.4), (16.4, 6.2), bend=-0.1)  # progesterone -> incubation
arr((17.6, 6.2), (19.2, 3.4))     # incubation (sight of partner sitting, eggs) -> prolactin
arr((20.0, 3.4), (21.6, 6.2))     # prolactin -> crop milk, feeding
arr((19.4, 3.4), (17.5, 6.2), bend=0.2)   # prolactin maintains incubation
bio.label(ax, (1.0, 8.9), "Behavior", size="small", bold=True, ha="left")
bio.label(ax, (1.0, 1.5), "Hormones (gonads, pituitary)", size="small", bold=True, ha="left")
bio.label(ax, (14.8, 0.9), "upward arrows: hormones act on behavior; downward arrows: stimuli from partner and nest act via brain and pituitary", size="tiny", color=P.muted())
ax.set_ylim(0.4, 9.4)
