"""Unequal crossing over in the X-linked opsin gene array (schematic).
Top: a typical array on Xq28, one long-wavelength (L, 'red') opsin gene followed by one or more nearly identical
middle-wavelength (M, 'green') genes. Middle: in meiosis two arrays pair out of register. (1) A crossover between
genes yields one chromosome that has lost its M gene (no M opsin: deuteranopia) and one with an extra M gene.
(2) A crossover within misaligned L and M genes yields hybrid L/M genes, whose spectral sensitivity is shifted
(anomalous trichromacy, or dichromacy if the hybrid is the first gene expressed)."""

import wikibio as bio

P = bio.P

fig, ax = bio.canvas(18.0, 10.0)


def gene(x, y, kind, w=1.6):
    if kind == "L":
        bio.box(ax, (x, y), w, 0.55, token="negative", text="L", size="small")
    elif kind == "M":
        bio.box(ax, (x, y), w, 0.55, token="positive", text="M", size="small")
    else:  # hybrid "A/B": 5' part from A, 3' part from B
        left, right = kind.split("/")
        tok = {"L": "negative", "M": "positive"}
        bio.box(ax, (x - w / 4, y), w / 2, 0.55, token=tok[left], radius=0.08)
        bio.box(ax, (x + w / 4, y), w / 2, 0.55, token=tok[right], radius=0.08)
        bio.label(ax, (x, y), kind, size="tiny", color=P.on_fill())


def array(x, y, kinds, label=None):
    ax.plot([x - 1.2, x + 2.1 * len(kinds) + 0.2], [y, y], color=P.edge("dna"), lw=1.6, zorder=1)
    for k, kd in enumerate(kinds):
        gene(x + 2.1 * k + 0.5, y, kd)
    if label:
        bio.label(ax, (x + 2.1 * len(kinds) + 0.6, y), label, size="tiny", ha="left")


bio.label(ax, (0.4, 9.4), "Normal array (Xq28)", size="small", ha="left", bold=True)
array(1.6, 8.7, ["L", "M"], "normal color vision")

bio.label(ax, (0.4, 7.6), "(1) Misaligned pairing, crossover between genes", size="small", ha="left", bold=True)
array(1.6, 6.9, ["L", "M"])
array(3.7, 6.2, ["L", "M"])
ax.plot([5.0, 5.5], [6.95, 6.15], color=P.edge("highlight"), lw=2.0)
ax.plot([5.0, 5.5], [6.15, 6.95], color=P.edge("highlight"), lw=2.0)
bio.arrow(ax, (9.0, 6.55), (10.2, 6.55))
array(11.2, 6.9, ["L"], "no M gene: deuteranopia")
array(11.2, 6.2, ["L", "M", "M"], "extra M gene: normal")

bio.label(ax, (0.4, 4.9), "(2) Misaligned pairing, crossover within genes", size="small", ha="left", bold=True)
array(1.6, 4.2, ["L", "M"])
array(3.7, 3.5, ["L", "M"])
ax.plot([3.95, 4.45], [4.25, 3.45], color=P.edge("highlight"), lw=2.0)
ax.plot([3.95, 4.45], [3.45, 4.25], color=P.edge("highlight"), lw=2.0)
bio.arrow(ax, (9.0, 3.85), (10.2, 3.85))
array(11.2, 4.2, ["L/M"], "hybrid gene only: dichromacy")
array(11.2, 3.5, ["L", "M/L", "M"], "hybrid in the array")
bio.label(ax, (9.0, 1.5), "L and M genes are 96% identical, so arrays pair out of register in female meiosis",
          size="small")
bio.label(ax, (9.0, 0.8), "red: L (long-wavelength) sequence    green: M (middle-wavelength) sequence", size="tiny",
          color=P.muted())
