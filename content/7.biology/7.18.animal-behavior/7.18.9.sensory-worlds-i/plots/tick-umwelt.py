# The Umwelt of a female tick as a chain of three functional cycles (after von Uexkull 1934).
# Each cycle: a perceptual cue (receptor) releases an action; the action changes the situation so that
# the next cue becomes effective. Everything else in the mammal is outside the tick's world.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22, 10.6)

# The mammal (right) and the tick on a twig (left)
bio.icon(ax, "phylopic/deer", at=(18.6, 5.6), height=5.6, color="animal")
bio.label(ax, (18.6, 0.75), "Mammal: shape, color, sound, size", size="tiny", color=P.muted())
bio.label(ax, (18.6, 0.3), "(not part of the tick's world)", size="tiny", color=P.muted())
bio.icon(ax, "phylopic/tick", at=(1.6, 5.3), height=1.5, color="drug")
bio.label(ax, (1.6, 4.1), "Tick", size="small", bold=True)

rows = [
    (8.6, "1", "Butyric acid", "olfactory receptors\n(Haller's organ)", "Let go of the twig,\ndrop", "positive"),
    (5.4, "2", "Touch of hair", "mechanoreceptors\nof the legs", "Run about until\nskin is reached", "channel"),
    (2.2, "3", "Warmth (about 37 °C)", "thermoreceptors", "Bore into the skin,\nsuck blood", "receptor"),
]
xc, xa = 6.4, 11.4
for y, n, cue, rec, act, tok in rows:
    bio.box(ax, (xc, y), 3.6, 1.55, token="highlight")
    bio.label(ax, (xc, y + 0.32), cue, size="small", bold=True, color=P.on_fill())
    bio.label(ax, (xc, y - 0.32), rec, size="tiny", color=P.on_fill())
    bio.box(ax, (xa, y), 3.6, 1.55, token=tok)
    bio.label(ax, (xa, y), act, size="small", color=P.on_fill())
    bio.arrow(ax, (xc + 1.85, y), (xa - 1.85, y), kind="activation")
    # cue arrives from the mammal; the action acts back on it (the functional cycle)
    bio.arrow(ax, (15.6, y + 0.35), (xc + 0.2, y + 0.85), kind="process", bend=-0.12, dashed=True,
              color=P.muted())
    bio.arrow(ax, (xa + 1.85, y - 0.2), (15.6, y - 0.4), kind="process", color=P.muted())
    bio.label(ax, (4.05, y), n, size="title", bold=True)

for (y1, _, _, _, _, _), (y2, _, _, _, _, _) in zip(rows[:-1], rows[1:]):
    bio.arrow(ax, (xa, y1 - 0.8), (xc + 0.4, y2 + 0.8), kind="process", bend=0.15, color=P.ink())

bio.label(ax, (xc, 10.15), "Perceptual cue (receptor)", size="small", bold=True)
bio.label(ax, (xa, 10.15), "Action (effector)", size="small", bold=True)
bio.label(ax, (18.6, 10.15), "Mammal", size="small", bold=True)
