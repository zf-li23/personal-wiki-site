"""An autosomal dominant disease (fully penetrant) segregating with a two-allele SNP marker (G/T). The
affected father in generation II is G/T and received the disease allele with G from his affected father
(phase known: disease with G). His children are scored as parental (P) or recombinant (R) from the allele
they received from him; the mother is T/T and uninformative, so every child's paternal allele is known."""
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(19, 7.4)
ped = G.Pedigree()
ped.person("I-1", "M", "affected", note="G/T")
ped.person("I-2", "F", note="T/T")
ped.person("II-1", "M", "affected", note="G/T")
ped.person("II-2", "F", note="T/T")
kids = [("M", "affected", "G/T", "P"), ("F", "affected", "G/T", "P"), ("F", "unaffected", "T/T", "P"),
        ("M", "affected", "G/T", "P"), ("M", "unaffected", "T/T", "P"), ("F", "affected", "G/T", "P"),
        ("F", "unaffected", "T/T", "P"), ("M", "unaffected", "G/T", "R")]
ids = []
for k, (sx, st, gt, pr) in enumerate(kids):
    pid = f"III-{k + 1}"
    ped.person(pid, sx, st, note=f"{gt}  {pr}")
    ids.append(pid)
ped.union("I-1", "I-2", children=["II-1"])
ped.union("II-1", "II-2", children=ids)
G.pedigree(ax, ped, origin=(2.0, 6.3), dx=1.95, dy=2.3, size=0.55, token="protein")
bio.label(ax, (17.8, 6.3), "disease allele on the G", size="tiny", ha="right", color=P.muted())
bio.label(ax, (17.8, 5.9), "chromosome of II-1", size="tiny", ha="right", color=P.muted())
bio.label(ax, (17.8, 4.0), "7 P, 1 R: Z(0.125) = 1.10", size="small", ha="right")
