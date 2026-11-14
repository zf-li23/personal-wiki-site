"""The three roles of the nervous system in behavior, with the escape of a noctuid moth from a bat."""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 11)

# general scheme (top row)
xs = [2.2, 7.4, 12.6, 17.8, 22.0]
names = ["Stimulus", "Sensation", "Integration", "Movement", "Behavior"]
subs = ["environment, body", "receptors transduce", "central circuits select", "motor neurons, muscles", "acts on environment"]
tokens = ["neutral", "receptor", "neuron", "muscle", "positive"]
widths = [3.4, 3.8, 4.2, 4.0, 3.4]
for x, n, s, t, w in zip(xs, names, subs, tokens, widths):
    bio.box(ax, (x, 8.4), w, 1.7, t)
    bio.label(ax, (x, 8.75), n, size="normal", color=P.on_fill())
    bio.label(ax, (x, 8.0), s, size="tiny", color=P.on_fill())
for a, b, wa, wb in zip(xs[:-1], xs[1:], widths[:-1], widths[1:]):
    bio.arrow(ax, (a + wa / 2 + 0.1, 8.4), (b - wb / 2 - 0.1, 8.4), kind="process")
# feedback loop from behavior to stimulus
bio.arrow(ax, (22.0, 9.2), (2.2, 9.2), kind="process", bend=-0.12, dashed=True)
bio.label(ax, (12.1, 10.65), "behavior changes the next input", size="small", color=P.muted())
# internal state modulates integration
bio.box(ax, (12.6, 5.6), 5.6, 1.0, "highlight", text="Internal state: hormones, modulators", size="small")
bio.arrow(ax, (12.6, 6.15), (12.6, 7.5), kind="modulation")
# chapters
for x, c in zip(xs[1:4], ["7.18.9-7.18.12", "7.18.13, 7.18.15", "7.18.14, 7.18.16"]):
    bio.label(ax, (x, 7.05) if x != 12.6 else (12.6, 4.75), c, size="tiny", color=P.muted())

# moth example (bottom row)
bio.label(ax, (0.4, 3.6), "Moth escape", size="normal", ha="left", bold=True)
ex = ["Bat call\n(ultrasound)", "A1, A2 cells of\ntympanal organ", "Thoracic\ninterneurons", "Flight motor\nneurons", "Turn away\nor dive"]
for x, e, t, w in zip(xs, ex, tokens, widths):
    bio.box(ax, (x, 1.7), w, 1.7, t, text=e, size="small")
for a, b, wa, wb in zip(xs[:-1], xs[1:], widths[:-1], widths[1:]):
    bio.arrow(ax, (a + wa / 2 + 0.1, 1.7), (b - wb / 2 - 0.1, 1.7), kind="process")
