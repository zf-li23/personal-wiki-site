"""Pedigree signatures of genomic imprinting. The same family structure, with a loss-of-function mutation
entering through generation I, for a paternally expressed gene (A: the allele is expressed only after
transmission by a male) and a maternally expressed gene (B: only after transmission by a female)."""
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(19.0, 8.6)


def family(source_sex, son_children, daughter_children):
    ped = G.Pedigree()
    ped.person("I-1", "M", status="carrier" if source_sex == "M" else "unaffected")
    ped.person("I-2", "F", status="carrier" if source_sex == "F" else "unaffected")
    ped.person("II-1", "F")
    ped.person("II-2", "M", status="carrier")
    ped.person("II-3", "F")
    ped.person("II-4", "F", status="carrier")
    ped.person("II-5", "M")
    kids_a, kids_b = [], []
    for k, (sex, st) in enumerate(son_children):
        pid = f"III-a{k}"
        ped.person(pid, sex, status=st)
        kids_a.append(pid)
    for k, (sex, st) in enumerate(daughter_children):
        pid = f"III-b{k}"
        ped.person(pid, sex, status=st)
        kids_b.append(pid)
    ped.union("I-1", "I-2", children=["II-2", "II-3", "II-4"])
    ped.union("II-1", "II-2", children=kids_a)
    ped.union("II-4", "II-5", children=kids_b)
    return ped


A = family("F", [("M", "affected"), ("F", "unaffected"), ("F", "affected")],
           [("M", "unaffected"), ("M", "carrier"), ("F", "carrier")])
B = family("M", [("M", "carrier"), ("F", "unaffected"), ("F", "carrier")],
           [("M", "unaffected"), ("M", "affected"), ("F", "affected")])

for ped, x0, letter, title, note in ((A, 1.4, "A", "Paternally expressed gene", "expressed after passage through a male"),
                                     (B, 10.9, "B", "Maternally expressed gene", "expressed after passage through a female")):
    bio.panel(ax, letter, (x0 - 1.2, 8.45))
    bio.label(ax, (x0 - 0.6, 8.2), title, size="title", ha="left", va="center")
    bio.label(ax, (x0 - 0.6, 7.65), note, size="small", ha="left", color=P.muted())
    G.pedigree(ax, ped, origin=(x0, 6.4), dx=1.05, dy=2.25, size=0.5, token="protein", gen_x=x0 - 1.0)

G.pedigree_legend(ax, (4.6, 0.45), [
    ("Affected (mutant allele expressed)", dict(sex="M", status="affected")),
    ("Carrier (mutant allele silent)", dict(sex="F", status="carrier")),
], size=0.38, spacing=0.6, columns=2, column_width=6.2)
