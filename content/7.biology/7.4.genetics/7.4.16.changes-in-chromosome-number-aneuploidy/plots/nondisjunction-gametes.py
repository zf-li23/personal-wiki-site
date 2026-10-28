"""Nondisjunction of one chromosome pair in meiosis I and in meiosis II, with the two homologues of the
parent distinguished (alleles A and a near the centromere, no crossing over), and trisomy rescue: loss of
one of the three copies from a trisomic zygote gives uniparental disomy with probability 1/3."""
import wikibio as bio
from wikibio import cytogenetics as C

P = bio.P
fig, ax = bio.canvas(30, 8.2)
names = [("A", "a")]
for k, (nd, title, note) in enumerate(((("I", 0), "Nondisjunction in meiosis I", "disomic eggs carry A and a (heterodisomy)"),
                                       (("II", 0, 0), "Nondisjunction in meiosis II", "disomic egg carries A and A (isodisomy)"))):
    x0 = 1.2 + k * 8.6
    bio.panel(ax, "AB"[k], (x0 - 1.0, 8.0))
    bio.label(ax, (x0 + 2.8, 7.65), title, size="small")
    C.meiosis_lineage(ax, (x0, 4.2), [("dna", "receptor")], nondisjunction=nd, names=names)
    bio.label(ax, (x0 + 2.8, 0.7), note, size="tiny", color=P.muted())
# trisomy rescue
bio.panel(ax, "C", (18.4, 8.0))
bio.label(ax, (23.6, 7.65), "Trisomy rescue", size="small")
C.round_cell(ax, (20.2, 4.2), 0.95)
C.chromosome_set(ax, (20.2, 4.2), [("dna", False), ("receptor", False), ("enzyme", False)], length=0.8, width=0.26)
bio.label(ax, (20.2, 2.9), "trisomic zygote", size="tiny", color=P.muted())
bio.label(ax, (20.2, 2.5), "A, a (egg) + b (sperm)", size="tiny", color=P.muted())
outs = [(("dna", "receptor"), "lose b: maternal UPD", "negative", 6.2),
        (("receptor", "enzyme"), "lose A: biparental", "positive", 4.2),
        (("dna", "enzyme"), "lose a: biparental", "positive", 2.2)]
for toks, text, tok, yy in outs:
    bio.arrow(ax, (21.3, 4.2 + (yy - 4.2) * 0.25), (23.3, yy), kind="process", head=0.16)
    C.round_cell(ax, (24.2, yy), 0.75)
    C.chromosome_set(ax, (24.2, yy), [(toks[0], False), (toks[1], False)], length=0.7, width=0.24)
    bio.label(ax, (25.2, yy), text, size="small", ha="left", color=P.edge(tok))
    bio.label(ax, (25.2, yy - 0.42), "probability 1/3", size="tiny", ha="left", color=P.muted())
