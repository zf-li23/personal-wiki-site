"""The working cycle of systems biology. A biological question fixes the perturbations and the
measurements; omics profiling turns samples into data matrices; statistics and data integration
turn the matrices into lists, signatures and associations; networks are reconstructed from them
and interrogated (topology, key nodes, dynamics); a model makes predictions that are tested by new
experiments, whose results refine the question. The dashed chord: the reconstructed network also suggests
directly which perturbation to make next."""

import wikibio as bio
from wikibio import ecology

fig, ax = bio.canvas(14, 9.4)
steps = [
    dict(text="Question and\nperturbation", token="highlight"),
    dict(text="Omics\nprofiling", token="dna"),
    dict(text="Statistics and\nintegration", token="protein"),
    dict(text="Network\nreconstruction", token="enzyme"),
    dict(text="Model and\nprediction", token="receptor"),
    dict(text="Experimental\nvalidation", token="positive"),
]
ecology.cycle(ax, (7, 4.7), 3.5, steps, start=90, size="small",
              arrow_labels=["samples", "data matrices", "lists, signatures", "interrogation", "hypotheses", "refined question"],
              chords=[(3, 0, dict(dashed=True, text="next perturbation"))])
