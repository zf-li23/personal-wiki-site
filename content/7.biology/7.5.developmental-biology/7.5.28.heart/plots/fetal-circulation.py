"""Fetal circulation and its change at birth. A: the fetal circuit (oxygen saturation from high, red, to low,
blue). Oxygenated blood from the placenta returns in the umbilical vein; about half bypasses the liver in the
ductus venosus; in the right atrium the stream from the inferior vena cava is directed through the foramen ovale
into the left atrium, so the best-oxygenated blood reaches the heart and brain; most of the right-ventricular
output passes from the pulmonary trunk through the ductus arteriosus into the descending aorta, because the
resistance of the fluid-filled lungs is high. B: a resistor model (Formula 28.9.1): the fraction of the
combined output that flows through the lungs, and the flow through the ductus, against the ratio of pulmonary to
systemic resistance. With the ductus open, flow through it reverses (left to right) when the pulmonary resistance
falls below the systemic one, as after the first breaths, before the ductus closes."""
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(25, 11)
bio.panel(ax, "A", (0.2, 10.8))
nodes = {"Placenta": (2.0, 1.4, "positive"), "Umbilical vein": (2.0, 3.6, "positive"), "Ductus venosus": (2.0, 5.6, "positive"),
         "Liver": (4.4, 2.9, "highlight"), "IVC": (2.0, 7.6, "lipid_head"), "RA": (5.0, 8.8, "neutral"), "LA": (9.6, 8.8, "neutral"),
         "RV": (5.0, 6.8, "neutral"), "LV": (9.6, 6.8, "neutral"), "Pulmonary trunk": (5.0, 4.8, "dna"), "Lungs": (7.3, 3.4, "dna2"),
         "Aorta": (9.6, 4.8, "receptor"), "Body": (9.6, 2.6, "receptor"), "Umbilical arteries": (5.6, 1.4, "dna"), "SVC": (2.4, 9.9, "dna")}
for k, (x, y, tk) in nodes.items():
    bio.box(ax, (x, y), 2.4 if len(k) > 5 else 1.4, 0.75, tk, k, size="tiny")
E = [("Placenta", "Umbilical vein", ""), ("Umbilical vein", "Ductus venosus", ""), ("Umbilical vein", "Liver", ""), ("Ductus venosus", "IVC", ""),
     ("Liver", "IVC", ""), ("IVC", "RA", ""), ("SVC", "RA", ""), ("RA", "LA", "foramen ovale"), ("RA", "RV", ""), ("LA", "LV", ""),
     ("RV", "Pulmonary trunk", ""), ("Pulmonary trunk", "Aorta", "ductus arteriosus"), ("Pulmonary trunk", "Lungs", ""), ("Lungs", "LA", ""),
     ("LV", "Aorta", ""), ("Aorta", "Body", ""), ("Body", "Umbilical arteries", ""), ("Umbilical arteries", "Placenta", "")]
for a_, b_, t in E:
    pa, pb = np.array(nodes[a_][:2]), np.array(nodes[b_][:2])
    bend = {("Lungs", "LA"): 0.25, ("Liver", "IVC"): -0.25}.get((a_, b_), 0.0)
    bio.arrow(ax, tuple(pa), tuple(pb), kind="process", shrink=0.6, bend=bend, lw=1.6 if t else 1.0,
              color=P.edge("highlight") if t else P.ink())
    if t:
        m = (pa + pb) / 2
        bio.label(ax, (m[0], m[1] + 0.35), t, size="tiny", color=P.edge("highlight"))

bio.panel(ax, "B", (12.6, 10.8))
QR, QL, Rs, Rd = 0.6, 0.4, 1.0, 0.05
ratio = np.logspace(-1.3, 1.3, 200)
lung_open, duct_open, lung_closed = [], [], []
for r in ratio:
    Rp = r * Rs
    M = np.array([[1 / Rp + 1 / Rd, -1 / Rd], [-1 / Rd, 1 / Rd + 1 / Rs]])
    P1, P2 = np.linalg.solve(M, [QR, QL])
    lung_open.append(P1 / Rp)
    duct_open.append((P1 - P2) / Rd)
    lung_closed.append(QR)
pl = quant.Plot(ax, (14.6, 1.6, 9.6, 7.8), xlim=(-1.3, 1.3), ylim=(-0.45, 1.0), xlabel="log10 (pulmonary / systemic resistance)",
                ylabel="flow (fraction of combined output)", xticks=[-1, 0, 1], yticks=[-0.4, 0, 0.4, 0.8])
x = np.log10(ratio)
pl.line(x, np.array(lung_open), "dna", text="lungs, ductus open", at=0.15)
pl.line(x, np.array(duct_open), "highlight", text="ductus (+: right to left)", at=0.7)
pl.line(x, np.array(lung_closed), "muted", dashed=True, text="lungs, ductus closed", at=0.5)
pl.hline(0, dashed=False, lw=0.5)
pl.vline(np.log10(8.0), text="fetus", size="tiny")
pl.vline(np.log10(0.12), text="after birth", size="tiny")
