"""Typical pedigrees of four single-gene modes of inheritance (NSGC symbols: squares males, circles females,
filled affected, central dot carrier). A: autosomal dominant. B: autosomal recessive with a consanguineous
mating (double line). C: X-linked recessive. D: X-linked dominant."""
import wikibio as bio
from wikibio import genetics as G

fig, ax = bio.canvas(25.0, 16.0)


def ped_ad():
    p = G.Pedigree()
    p.person("I1", "M", "affected"); p.person("I2", "F")
    for i, (s, st) in enumerate((("F", "affected"), ("M", "unaffected"), ("M", "affected"), ("F", "unaffected"))):
        p.person(f"II{i}", s, st)
    p.person("IIs", "M")
    p.person("IIw", "F")
    p.union("I1", "I2", children=["II0", "II1", "II2", "II3"])
    p.person("III0", "M", "affected"); p.person("III1", "F"); p.person("III2", "F", "affected")
    p.person("III3", "M"); p.person("III4", "F", "affected")
    p.union("II0", "IIs", children=["III0", "III1", "III2"])
    p.union("II2", "IIw", children=["III3", "III4"])
    return p


def ped_ar():
    p = G.Pedigree()
    p.person("I1", "M"); p.person("I2", "F")
    p.person("II1", "F"); p.person("II2", "M"); p.person("IIa", "F"); p.person("IIb", "M")
    p.union("I1", "I2", children=["II1", "II2"])
    p.person("III1", "M"); p.person("III2", "F")
    p.union("II1", "IIb", children=["III1"])
    p.union("IIa", "II2", children=["III2"])
    for i, st in enumerate(("unaffected", "affected", "unaffected", "affected")):
        p.person(f"IV{i}", "MFFM"[i], st)
    p.union("III1", "III2", children=["IV0", "IV1", "IV2", "IV3"], consanguineous=True)
    return p


def ped_xr():
    p = G.Pedigree()
    p.person("I1", "M", "affected"); p.person("I2", "F")
    p.person("II1", "F", "carrier"); p.person("II2", "M"); p.person("II3", "F", "carrier"); p.person("IIh", "M")
    p.person("IIh2", "M")
    p.union("I1", "I2", children=["II1", "II2", "II3"])
    p.person("III1", "M", "affected"); p.person("III2", "F"); p.person("III3", "M")
    p.union("IIh", "II1", children=["III1", "III2", "III3"])
    p.person("III4", "M"); p.person("III5", "M", "affected"); p.person("III6", "F", "carrier")
    p.union("II3", "IIh2", children=["III4", "III5", "III6"])
    return p


def ped_xd():
    p = G.Pedigree()
    p.person("I1", "M", "affected"); p.person("I2", "F")
    p.person("II1", "F", "affected"); p.person("II2", "M"); p.person("II3", "F", "affected"); p.person("IIh", "M")
    p.union("I1", "I2", children=["II1", "II2", "II3"])
    p.person("III1", "M", "affected"); p.person("III2", "F"); p.person("III3", "F", "affected"); p.person("III4", "M")
    p.union("IIh", "II1", children=["III1", "III2", "III3", "III4"])
    return p


panels = [("A", "Autosomal dominant", ped_ad(), (1.6, 14.0)), ("B", "Autosomal recessive", ped_ar(), (14.6, 14.4)),
          ("C", "X-linked recessive", ped_xr(), (1.6, 6.0)), ("D", "X-linked dominant", ped_xd(), (14.6, 6.0))]
for letter, title, ped, origin in panels:
    bio.panel(ax, letter, (origin[0] - 1.5, origin[1] + 1.6 if letter != "B" else origin[1] + 1.2))
    bio.label(ax, (origin[0] + 3.0, origin[1] + 1.25 if letter != "B" else origin[1] + 0.85), title, size="small", bold=True)
    G.pedigree(ax, ped, origin=origin, dx=1.15, dy=1.55 if letter != "B" else 1.25, size=0.5)
G.pedigree_legend(ax, (19.5, 1.6), [("affected", dict(sex="M", status="affected")),
                                    ("carrier (heterozygote)", dict(sex="F", status="carrier"))], columns=2, column_width=3.2)
