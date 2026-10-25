# Speed and accuracy of the three general transfers of the central dogma, as order-of-magnitude ranges
# (log scale; typical values from E. coli and human cells, compiled from the course textbooks and
# reviews). A: elongation rates in nucleotides (or amino acids) added per second. B: error frequency per
# nucleotide or residue; for replication the three steps of the fidelity cascade are shown separately:
# base selection by the polymerase, with 3'->5' exonuclease proofreading, and with post-replicative
# mismatch repair (7.2.7, 7.2.8).
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(19, 8.6)

speed = [
    ("Replication, $\\mathit{E.\\ coli}$", 500, 1000, "dna"),
    ("Replication, human", 15, 50, "dna"),
    ("Transcription, $\\mathit{E.\\ coli}$", 20, 80, "rna"),
    ("Transcription, human (Pol II)", 15, 70, "rna"),
    ("Translation, $\\mathit{E.\\ coli}$", 10, 20, "protein"),
    ("Translation, human", 3, 8, "protein"),
]
error = [
    ("Replication: base selection", 1e-5, 1e-4, "dna"),
    ("  + proofreading", 1e-7, 1e-6, "dna"),
    ("  + mismatch repair", 1e-10, 1e-9, "dna"),
    ("Transcription", 1e-6, 1e-5, "rna"),
    ("Aminoacylation of tRNA", 1e-5, 1e-4, "protein"),
    ("Translation (decoding)", 1e-4, 1e-3, "protein"),
]


def panel(rect, rows, xlim, ticks, xlabel, letter, title):
    a = C.axes_at(ax, rect)
    a.set_xscale("log")
    n = len(rows)
    for k, (name, lo, hi, tok) in enumerate(rows):
        y = n - 1 - k
        a.barh(y, hi - lo, left=lo, height=0.55, color=P.fill(tok), edgecolor=C.line(tok), lw=0.9)
    a.set_yticks(range(n), [r[0] for r in rows][::-1])
    a.set_ylim(-0.6, n - 0.4)
    a.set_xlim(*xlim)
    a.set_xticks(*ticks)
    a.minorticks_off()
    C.style_axes(a, xlabel, None)
    a.tick_params(axis="y", length=0)
    bio.panel(ax, letter, (rect[0] - 4.6, 8.3))
    bio.label(ax, (rect[0] - 4.2, 8.3), title, size="normal", bold=True, ha="left")


panel((4.9, 1.4, 4.4, 6.2), speed, (1, 3000), ([1, 10, 100, 1000], ["1", "10", "100", "1000"]),
      "Rate / (nt or aa per s)", "A", "Elongation rate")
panel((14.4, 1.4, 4.4, 6.2), error, (1e-11, 1e-2), ([1e-10, 1e-8, 1e-6, 1e-4, 1e-2],
      ["10⁻¹⁰", "10⁻⁸", "10⁻⁶", "10⁻⁴", "10⁻²"]), "Errors per nt or residue", "B", "Error frequency")
