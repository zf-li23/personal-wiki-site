"""The double-negative logic of four plant hormone pathways (SBGN activity flow; open arrows activate,
bars inhibit).
Auxin: auxin acts as a molecular glue between the F-box protein TIR1 (part of an SCF ubiquitin ligase)
and the Aux/IAA repressors, which are ubiquitinated and degraded, releasing the ARF transcription factors.
Gibberellin: GA bound to its soluble receptor GID1 binds the DELLA repressors and recruits the ubiquitin
ligase SCF-SLY1 (GID2 in rice), which marks them for degradation by the proteasome; growth-promoting
transcription factors such as the PIFs are released.
Abscisic acid: ABA bound to a PYR/PYL/RCAR receptor binds and inhibits clade A protein phosphatases 2C
(ABI1, ABI2), which otherwise keep the SnRK2 kinases inactive; active SnRK2 phosphorylates ABF/AREB
transcription factors and the anion channel SLAC1 (stomatal closure).
Brassinosteroid: BR binds the receptor kinase BRI1 with its co-receptor BAK1; the activated receptors
inhibit, through BSK kinases and the phosphatase BSU1, the GSK3-like kinase BIN2, which otherwise
phosphorylates and inactivates the transcription factors BZR1/BES1.
In every case the hormone inhibits an inhibitor: the pathway is OFF by default and ON by derepression.
"""

import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(25.0, 10.5)
d = network.Diagram(ax, size="small")
cols = [
    ("Auxin", [("auxin", "drug"), ("TIR1 (SCF)", "receptor"), ("Aux/IAA", "negative"), ("ARF", "metabolite")], ["positive", "negative", "negative"],
     "auxin-responsive genes"),
    ("Gibberellin", [("GA", "drug"), ("GID1 + SCF-SLY1", "receptor"), ("DELLA", "negative"), ("PIFs and others", "metabolite")],
     ["positive", "negative", "negative"], "stem growth, germination"),
    ("Abscisic acid", [("ABA", "drug"), ("PYR/PYL/RCAR", "receptor"), ("PP2C (ABI1)", "negative"), ("SnRK2 (OST1)", "enzyme")],
     ["positive", "negative", "negative"], "stomatal closure, stress genes"),
    ("Brassinosteroid", [("BR", "drug"), ("BRI1–BAK1", "receptor"), ("BIN2 (GSK3-like)", "negative"), ("BZR1 / BES1", "metabolite")],
     ["positive", "negative", "negative"], "growth genes"),
]
for k, (title, nodes, arcs, out) in enumerate(cols):
    x = 3.1 + 6.2 * k
    bio.label(ax, (x, 10.0), title, size="normal", bold=True)
    ids = []
    for i, (text, tok) in enumerate(nodes):
        nid = f"n{k}{i}"
        d.activity(nid, (x, 8.7 - 1.75 * i), text, token=tok)
        ids.append(nid)
    pid = f"p{k}"
    d.phenotype(pid, (x, 8.7 - 1.75 * 4), out, size="tiny")
    for i, kind in enumerate(arcs):
        d.connect(ids[i], ids[i + 1], kind)
    d.connect(ids[-1], pid, "positive")
bio.label(ax, (12.5, 0.45), "hormone ⟶ receptor ⊣ repressor ⊣ effector ⟶ response: activation by inhibiting an inhibitor",
          size="small", color=P.muted())
