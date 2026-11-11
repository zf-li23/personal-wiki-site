"""Marr's three levels of analysis, applied to sound localization in the barn owl (left column of
examples) and mapped onto the parts of this course (right column)."""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(20, 9.4)
levels = [
    ("Computational theory", "What is the goal, and why is\nit the right one?", "highlight",
     "Estimate sound azimuth from the\ninteraural time difference (ITD)",
     "coding, information, Bayesian\ninference, reinforcement learning"),
    ("Representation and algorithm", "How are input and output\nrepresented; what procedure?", "receptor",
     "Delay lines + coincidence detection\n(Jeffress); a place code for ITD",
     "network dynamics, attractors,\nlearning rules, population codes"),
    ("Implementation", "How is it realized physically?", "neuron",
     "Axons of nucleus magnocellularis,\ncoincidence detectors in n. laminaris",
     "channels, action potentials,\nsynapses, dendrites, cell types"),
]
bio.label(ax, (3.6, 8.9), "Level", size="title", bold=True)
bio.label(ax, (10.1, 8.9), "Barn owl sound localization", size="title", bold=True)
bio.label(ax, (16.6, 8.9), "Where in this course", size="title", bold=True)
for k, (name, q, tok, ex, course) in enumerate(levels):
    y = 7.2 - k * 2.75
    bio.box(ax, (3.6, y), 6.6, 2.2, token=tok, text=None)
    bio.label(ax, (3.6, y + 0.45), name, size="normal", bold=True, color=P.on_fill())
    bio.label(ax, (3.6, y - 0.4), q, size="small", color=P.on_fill())
    bio.box(ax, (10.1, y), 5.9, 2.2, token="neutral", text=None)
    bio.label(ax, (10.1, y), ex, size="small", color=P.on_fill())
    bio.box(ax, (16.6, y), 6.0, 2.2, token="neutral", text=None)
    bio.label(ax, (16.6, y), course, size="small", color=P.on_fill())
    if k < 2:
        bio.arrow(ax, (3.6, y - 1.15), (3.6, y - 1.6), kind="link", color=P.muted())
bio.label(ax, (0.15, 4.45), "constrains  ↕  constrains", size="tiny", color=P.muted(), rotation=90)
