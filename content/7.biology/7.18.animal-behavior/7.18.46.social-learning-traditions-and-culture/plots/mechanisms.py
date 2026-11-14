# A classification of the ways in which the presence or behavior of a demonstrator can influence an observer
# (after Whiten and Ham 1992, Heyes 1994, Hoppitt and Laland 2013). Social influence without learning:
# social facilitation. Social learning that does not copy actions: local and stimulus enhancement,
# observational conditioning, social learning of food preferences. Copying of goals or actions: emulation
# (copies the result), imitation (copies the form of the action). Teaching is defined by the demonstrator's
# behavior and can produce any of them. Affordance learning (learning from seeing an object move by itself)
# is shown as the asocial control.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 11.0)


def node(xy, text, tok, w=4.2, h=0.95, sub=None):
    bio.box(ax, xy, w, h, tok, text=text, size="small")
    if sub:
        bio.label(ax, (xy[0], xy[1] - 0.95), sub, size="tiny", color=P.muted())


top = (12.0, 9.8)
node(top, "Social influence on behavior", "neutral", w=5.6)
a = (4.0, 7.4)
b = (12.0, 7.4)
c = (20.0, 7.4)
node(a, "Without learning", "neutral", sub="behavior changes only while\nothers are present")
node(b, "Learning: what, where", "dna", w=4.6, sub="attention or values change;\nactions found by the observer")
node(c, "Learning: how", "rna", sub="the result or the form\nof the action is copied")
for p in (a, b, c):
    bio.arrow(ax, (top[0], top[1] - 0.5), (p[0], p[1] + 0.5), kind="process", color=P.muted())
leaves = [
    ((4.0, 4.2), "social facilitation", "neutral", "eating, yawning, calling\nin chorus with others"),
    ((8.6, 4.2), "local and stimulus\nenhancement", "dna", "attention drawn to a place\nor an object"),
    ((12.6, 4.2), "observational\nconditioning", "dna", "fear of snakes learned from\na frightened companion"),
    ((16.6, 4.2), "emulation", "rna", "copies the goal or the\nchange in the object"),
    ((20.6, 4.2), "imitation", "rna", "copies the form of\nthe action, even if arbitrary"),
]
for xy, t, tok, sub in leaves:
    node(xy, t, tok, w=3.6, h=1.1, sub=sub)
bio.arrow(ax, (a[0], a[1] - 1.45), (4.0, 4.8), kind="process", color=P.muted())
for x in (8.6, 12.6):
    bio.arrow(ax, (b[0], b[1] - 1.45), (x, 4.8), kind="process", color=P.muted())
for x in (16.6, 20.6):
    bio.arrow(ax, (c[0], c[1] - 1.45), (x, 4.8), kind="process", color=P.muted())
node((16.6, 1.3), "teaching", "positive", w=8.0, h=0.9)
bio.label(ax, (16.6, 0.45), "defined by the demonstrator: it changes its behavior for a naive observer, at a cost",
          size="tiny", color=P.muted())
for x in (8.6, 12.6, 16.6, 20.6):
    bio.arrow(ax, (16.6 + (x - 16.6) * 0.45, 1.8), (x, 2.55), kind="activation", color=P.edge("positive"), dashed=True)
bio.box(ax, (4.0, 1.3), 4.4, 0.9, "highlight", text="affordance learning (asocial)", size="small")
bio.label(ax, (4.0, 0.45), "learns what an object does by seeing it move", size="tiny", color=P.muted())
