"""wikibio: the figure system of the biology courses (see BIO_FIGURES.md).

    import wikibio as bio
    fig, ax = bio.canvas(12, 6)
    bio.cell(ax, (6, 3), 5, 2.6)
    bio.nucleus(ax, (6, 3), 1.2)
    bio.arrow(ax, (1, 1), (3, 1), kind="activation")
    bio.icon(ax, "servier/heart", at=(10, 4), height=1.5)

Colours come from tokens (``bio.P.fill("nucleus")``); every figure works in the light and dark themes.
"""

from . import palette as P
from .cell import bilayer, cell, chloroplast, er, golgi, lysosome, membrane, mitochondrion, nucleus, vacuole, vesicle
from .core import arrow, blob, box, callout, canvas, label, panel, polyline, reaction, scale_bar, shape, smooth_closed
from .icons import icon
from .molecules import dna, domains, ion, molecule, protein, receptor, strand
from .structures import actin, antibody, microtubule, neuron, ribosome, synapse, virus

__all__ = [
    "P", "canvas", "label", "callout", "panel", "scale_bar", "arrow", "reaction", "box", "shape", "blob", "smooth_closed",
    "polyline", "bilayer", "membrane", "cell", "nucleus", "mitochondrion", "er", "golgi", "vesicle", "lysosome",
    "chloroplast", "vacuole", "dna", "strand", "protein", "domains", "receptor", "ion", "molecule", "icon",
    "ribosome", "actin", "microtubule", "antibody", "virus", "neuron", "synapse",
]
