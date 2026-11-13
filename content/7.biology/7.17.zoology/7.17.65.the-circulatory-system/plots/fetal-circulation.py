# The fetal circulation of a mammal as a flow diagram: boxes are organs and chambers, arrows vessels
# coloured by oxygenation; the three shunts that close at birth are highlighted. Schematic.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(20, 11)
OX, DE, MX = P.edge("negative"), P.edge("dna"), P.edge("protein")
nodes = {
    "head": ((10, 10.2), "head, forelimbs", "neutral"),
    "svc": ((6.2, 8.3), "anterior vena cava", "dna"),
    "ra": ((6.2, 6.4), "right atrium", "dna"),
    "rv": ((6.2, 4.4), "right ventricle", "dna"),
    "pt": ((6.2, 2.5), "pulmonary trunk", "dna"),
    "lungs": ((2.2, 2.5), "lungs (collapsed)", "er"),
    "la": ((13.8, 6.4), "left atrium", "negative"),
    "lv": ((13.8, 4.4), "left ventricle", "negative"),
    "aorta": ((13.8, 2.5), "aorta", "protein"),
    "body": ((13.8, 0.6), "trunk, hindlimbs", "neutral"),
    "ivc": ((10.0, 5.6), "posterior vena cava", "protein"),
    "liver": ((10.0, 4.4), "liver", "mitochondrion"),
    "plac": ((18.2, 4.4), "placenta", "negative"),
}
P_ = {}
for k, (c, t, tok) in nodes.items():
    bio.box(ax, c, 3.0 if k not in ("lungs", "plac") else 2.8, 0.9, token=tok, text=t, size="tiny")
    P_[k] = c


def link(a, b, col, lw=1.6, bend=0.0, text=None, at=None, shunt=False):
    bio.arrow(ax, a, b, kind="process", color=col, lw=lw * (1.6 if shunt else 1.0), bend=bend)
    if text:
        bio.label(ax, at, text, size="tiny", color=P.ink(), bold=shunt)


link((8.5, 10.2), (6.6, 8.8), DE)
link((6.2, 7.85), (6.2, 6.85), DE)
link((6.2, 5.95), (6.2, 4.85), DE)
link((6.2, 3.95), (6.2, 2.95), DE)
link((4.7, 2.5), (3.6, 2.5), DE, lw=1.0, text="little flow", at=(4.15, 2.15))
link((7.7, 2.3), (12.3, 2.3), DE, text="ductus arteriosus", at=(10.0, 1.95), shunt=True)
link((7.7, 6.6), (12.3, 6.6), MX, text="foramen ovale", at=(10.0, 7.0), shunt=True, bend=-0.15)
link((8.5, 5.7), (7.7, 6.2), MX)
link((13.8, 5.95), (13.8, 4.85), OX)
link((13.8, 3.95), (13.8, 2.95), MX)
link((15.3, 2.7), (11.6, 9.8), MX, bend=-0.45)
link((13.8, 2.05), (13.8, 1.05), MX)
link((15.3, 0.6), (18.2, 3.95), DE, bend=0.2, text="umbilical arteries", at=(17.6, 1.6))
link((16.9, 4.1), (11.4, 4.1), OX, bend=0.25, text="umbilical vein", at=(16.6, 3.3))
link((10.0, 4.85), (10.0, 5.15), OX, text="ductus venosus", at=(8.4, 5.0), shunt=True)
link((1.0, 3.0), (5.0, 6.3), OX, lw=0.9, bend=-0.2, text="pulmonary veins", at=(2.0, 5.2))
bio.label(ax, (1.0, 10.4), "red: oxygenated   purple: mixed   blue: deoxygenated", size="tiny", ha="left", color=P.muted())
