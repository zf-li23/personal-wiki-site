"""Four modes of the pentose phosphate pathway (after Berg et al.). Nodes: glucose 6-phosphate,
ribulose 5-phosphate (oxidative phase: 2 NADPH + CO2), ribose 5-phosphate, fructose 6-phosphate +
glyceraldehyde 3-phosphate (nonoxidative phase, reversible) and pyruvate (glycolysis). Active routes
coloured, inactive ones dashed gray."""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22.0, 15.0)
modes = [
    ("Mode 1: ribose 5-P ≫ NADPH", {"glyc", "nonox_rev"}, "5 G6P + ATP → 6 R5P"),
    ("Mode 2: balanced", {"ox", "iso"}, "G6P + 2 NADP⁺ → R5P + 2 NADPH + CO₂"),
    ("Mode 3: NADPH ≫ ribose 5-P", {"ox", "iso", "nonox", "recycle"}, "G6P + 12 NADP⁺ → 6 CO₂ + 12 NADPH + Pᵢ"),
    ("Mode 4: NADPH and ATP", {"ox", "iso", "nonox", "topyr"}, "3 G6P → 5 pyruvate + 3 CO₂ + 6 NADPH + 5 NADH + 8 ATP"),
]
for k, (title, act, net) in enumerate(modes):
    ox0 = 0.4 + (k % 2) * 11.0
    oy0 = 7.6 if k < 2 else 0.2
    def at(x, y):
        return (ox0 + x, oy0 + y)
    bio.label(ax, at(5.2, 6.8), title, size="small", bold=True)
    nodes = {"g6p": (2.0, 5.4, "Glucose 6-P"), "ru5p": (8.0, 5.4, "Ribulose 5-P"), "r5p": (8.0, 3.2, "Ribose 5-P"),
             "fg": (2.0, 3.2, "F6P + GAP"), "pyr": (2.0, 1.0, "Pyruvate")}
    for key, (x, y, t) in nodes.items():
        bio.box(ax, at(x, y), 2.8, 0.75, "highlight" if key in ("g6p", "r5p") else "metabolite", t, size="small")
    def edge(name, a, b, bend=0.0, text=None, tx=None):
        on = name in act
        bio.arrow(ax, at(*a), at(*b), kind="process", bend=bend, dashed=not on,
                  color=P.edge("positive") if on else P.muted())
        if text and tx:
            bio.label(ax, at(*tx), text, size="tiny", color=P.ink() if on else P.muted())
    edge("ox", (3.5, 5.4), (6.5, 5.4), text="oxidative: 2 NADPH, CO₂", tx=(5.0, 5.85))
    edge("iso", (8.0, 4.95), (8.0, 3.65))
    edge("nonox", (6.55, 3.05), (3.45, 3.05), text="nonoxidative", tx=(5.0, 2.65))
    edge("nonox_rev", (3.45, 3.4), (6.55, 3.4), text="(reverse)", tx=(5.0, 3.8))
    edge("glyc", (1.4, 4.95), (1.4, 3.65), text="glycolytic\nenzymes", tx=(0.0, 4.3))
    edge("recycle", (2.6, 3.65), (2.6, 4.95), text="gluconeogenic\nenzymes", tx=(4.0, 4.3))
    edge("topyr", (2.0, 2.75), (2.0, 1.45), text="glycolysis:\nATP, NADH", tx=(3.6, 2.0))
    bio.label(ax, at(5.2, 0.15), net, size="tiny", color=P.ink())
