"""Tinbergen's four questions as a 2 x 2 table (proximate/ultimate x static/dynamic), with gull mobbing as the example."""

from matplotlib.patches import FancyBboxPatch
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24.0, 12.0)


def cell(x, y, w, h, token, title, lines):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.3",
                                facecolor=P.mix(P.fill(token), P.surface(), 0.7), edgecolor=P.edge(token), lw=1.2, zorder=5))
    bio.label(ax, (x + 0.4, y + h - 0.55), title, size="normal", bold=True, ha="left", va="center")
    for i, t in enumerate(lines):
        bio.label(ax, (x + 0.4, y + h - 1.45 - 0.72 * i), t, size="small", ha="left", va="center")


x0, y0, w, h, g = 4.4, 0.6, 9.4, 4.9, 0.4
bio.label(ax, (x0 + w / 2, 11.4), "Static: the behavior as it is now", size="normal", bold=True)
bio.label(ax, (x0 + w + g + w / 2, 11.4), "Dynamic: how the behavior came to be", size="normal", bold=True)
bio.label(ax, (1.7, y0 + h + g + h / 2 + 0.4), "Proximate", size="normal", bold=True)
bio.label(ax, (1.7, y0 + h + g + h / 2 - 0.4), "(individual)", size="small", color=P.muted())
bio.label(ax, (1.7, y0 + h / 2 + 0.4), "Ultimate", size="normal", bold=True)
bio.label(ax, (1.7, y0 + h / 2 - 0.4), "(lineage)", size="small", color=P.muted())

ytop = y0 + h + g
cell(x0, ytop, w, h, "neuron", "1. Mechanism",
     ["How does it work?", "Sight of a crow or fox near the nest",
      "triggers alarm calls and diving attacks;", "hormonal state of breeding adults", "lowers the threshold"])
cell(x0 + w + g, ytop, w, h, "protein", "2. Development",
     ["How did it develop in the individual?", "Mobbing appears in adults at the",
      "breeding colony; young birds learn", "which animals are dangerous", "from the alarm of others"])
cell(x0, y0, w, h, "positive", "3. Function",
     ["What is it for?", "Mobbing distracts egg predators,",
      "so fewer eggs and chicks are taken", "(Kruuk's eggs inside versus", "outside the colony)"])
cell(x0 + w + g, y0, w, h, "rna", "4. Evolution",
     ["How did it evolve in the lineage?", "Inherited from a ground-nesting",
      "ancestral gull; lost in cliff-nesting", "kittiwakes; evolved convergently", "in colonial swallows"])

for a, b in [((x0 + w / 2, ytop - 0.05), (x0 + w / 2, y0 + h + 0.05)),
             ((x0 + w + g + w / 2, ytop - 0.05), (x0 + w + g + w / 2, y0 + h + 0.05))]:
    bio.arrow(ax, a, b, kind="link", color=P.muted())
