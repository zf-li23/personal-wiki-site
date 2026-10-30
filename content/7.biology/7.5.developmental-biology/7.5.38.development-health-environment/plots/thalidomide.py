"""Thalidomide as a molecular glue (SBGN process description, simplified).

Cereblon (CRBN) is the substrate receptor of the cullin-RING ubiquitin ligase CRL4 (CUL4A, DDB1, RBX1).
Thalidomide (or its analogues lenalidomide and pomalidomide) binds a pocket of CRBN and creates a new surface that
recruits proteins the ligase normally ignores ("neosubstrates") through a beta-hairpin zinc-finger degron.
The neosubstrate is polyubiquitinated and degraded by the proteasome. Right: neosubstrates and consequences:
SALL4 (limb, ear, heart and kidney development; its loss-of-function syndromes phenocopy thalidomide embryopathy;
degraded in humans, primates and rabbits but not in mice and rats because of sequence differences in its
second zinc finger), p63 (limbs and ears in zebrafish and chick), PLZF (limb patterning in chick), and in
blood cells IKZF1 and IKZF3 (the therapeutic effect in multiple myeloma).
"""

import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(34.0, 13.0)
d = network.Diagram(ax)
d.macromolecule("cul", (3.0, 8.4), "CUL4A", token="protein", w=3.0, h=1.2)
d.macromolecule("ddb", (3.0, 6.6), "DDB1", token="protein", w=3.0, h=1.2)
d.macromolecule("rbx", (3.0, 10.2), "RBX1", token="protein", w=3.0, h=1.2)
d.macromolecule("crbn", (6.6, 6.6), "CRBN", token="receptor", w=3.0, h=1.2)
d.complex("crl4", ["cul", "ddb", "rbx", "crbn"], text="CRL4-CRBN ubiquitin ligase", token="enzyme")
d.simple_chemical("thal", (6.6, 2.6), "thalidomide", token="drug")
d.macromolecule("sall", (12.0, 2.6), "SALL4", token="protein", w=3.0, h=1.2)
d.macromolecule("sallub", (16.5, 7.4), "SALL4", token="protein", w=3.0, h=1.2, states=["Ub"])
d.unspecified("prot", (21.0, 7.4), "proteasome", token="neutral", w=3.8, h=1.4)
d.empty("deg", (21.0, 3.6))
d.reaction(["sall"], ["sallub"], at=(13.6, 6.0), modifiers=[("crl4", "catalysis"), ("thal", "necessary")])
d.reaction(["sallub"], ["deg"], at=(18.6, 4.6), modifiers=[("prot", "catalysis")])
bio.label(ax, (9.4, 1.2), "binds CRBN, creates a degron-binding surface", size="tiny", color=P.muted())

x0 = 24.0
rows = (("neosubstrate", "where it matters", "effect of degradation"),
        ("SALL4", "limb bud, ear, heart, kidney", "phocomelia, ear and heart defects"),
        ("p63", "apical ectodermal ridge, ear", "fin and ear defects (zebrafish)"),
        ("PLZF", "limb mesenchyme", "limb defects (chick)"),
        ("IKZF1, IKZF3", "myeloma and T cells", "therapy of multiple myeloma"))
for i, r in enumerate(rows):
    y = 11.6 - 1.25 * i
    for j, s in enumerate(r):
        bio.label(ax, (x0 + [0, 3.0, 6.3][j], y), s, size="tiny", ha="left", bold=(i == 0))
bio.label(ax, (x0, 4.6), "Species difference in SALL4 zinc finger 2:", size="tiny", ha="left", bold=True)
bio.label(ax, (x0, 3.8), "human, primates, rabbit: degraded, embryos sensitive", size="tiny", ha="left")
bio.label(ax, (x0, 3.1), "mouse, rat: not degraded, embryos resistant", size="tiny", ha="left")
