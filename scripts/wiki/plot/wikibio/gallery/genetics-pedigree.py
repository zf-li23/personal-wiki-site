# Autosomal recessive pedigree with a first-cousin marriage (NSGC symbols)
import wikibio as bio
from wikibio import genetics as G

fig, ax = bio.canvas(15.6, 7.6)
ped = G.Pedigree()
ped.person("I-1", "M", status="carrier", deceased=True)
ped.person("I-2", "F")
ped.person("II-w", "F")
ped.person("II-s", "M")
ped.person("II-d", "F")
ped.person("II-h", "M")
ped.person("II-t1", "M")
ped.person("II-t2", "M")
ped.person("III-1", "F")
ped.person("III-2", "M", status="carrier")
ped.person("III-3", "F", status="carrier")
ped.person("III-4", "U", text="2")
ped.person("III-5", "M", deceased=True, note="d. 2 y")
ped.person("IV-1", "F", status="carrier")
ped.person("IV-2", "M", status="affected", proband=True)
ped.person("IV-3", "F", status="affected")
ped.person("IV-4", "M")
ped.person("IV-5", "U", kind="miscarriage")

ped.union("I-1", "I-2", children=["II-s", "II-d", "II-t1", "II-t2"], twins=[("II-t1", "II-t2", "mz")])
ped.union("II-w", "II-s", children=["III-1", "III-2"])
ped.union("II-d", "II-h", children=["III-3", "III-4", "III-5"])
ped.union("III-2", "III-3", consanguineous=True, children=["IV-1", "IV-2", "IV-3", "IV-4", "IV-5"],
          twins=[("IV-3", "IV-4", "dz")])

G.pedigree(ax, ped, origin=(1.6, 7.0), dx=1.05, dy=1.95, size=0.52, token="protein")

G.pedigree_legend(ax, (10.0, 7.1), [
    ("Unaffected male, female", [dict(sex="M"), dict(sex="F")]),
    ("Affected", dict(sex="M", status="affected")),
    ("Carrier (heterozygote)", dict(sex="F", status="carrier")),
    ("Deceased", dict(sex="M", deceased=True)),
    ("Sex not specified (number)", dict(sex="U", text="2")),
    ("Pregnancy loss", dict(sex="U", kind="miscarriage")),
    ("Proband", dict(sex="M", proband=True)),
    ("Consanguineous union", dict(couple="consanguineous")),
    ("Monozygotic twins", dict(twins="mz")),
    ("Dizygotic twins", dict(twins="dz")),
], size=0.4, spacing=0.66)
