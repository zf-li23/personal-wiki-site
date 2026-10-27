"""Pathways switched by receptor kinases and nucleocytoplasmic shuttling (A, B: SBGN activity flow).

A TGF-beta/Smad: the ligand brings together type II and type I receptor serine/threonine kinases; the type II
kinase phosphorylates the GS region of the type I receptor, which phosphorylates the receptor-regulated
Smads (Smad2/3; Smad1/5/8 for BMPs), presented by SARA on early endosomes. Phospho-R-Smads bind Smad4 and
accumulate in the nucleus, where they regulate target genes with cofactors; the inhibitory Smad7 is a target
and feeds back on the receptor (dashed).
B Hippo-YAP/TAZ: cell-cell contact, apicobasal polarity (Merlin/NF2) and soft substrates activate the
kinase cascade MST1/2 (with SAV1) -> LATS1/2 (with MOB1), which phosphorylates YAP and TAZ; phosphorylated YAP
is held in the cytoplasm by 14-3-3 or degraded. Unphosphorylated YAP/TAZ enter the nucleus and with TEAD
activate proliferation and survival genes. Stiff matrix, cell spreading and G12/13-coupled receptors act
through Rho and F-actin to inhibit LATS and to promote YAP nuclear entry.
C A four-state shuttling model of Smad2: unphosphorylated Smad shuttles freely (import = export = 0.3/min);
the receptor phosphorylates it in the cytoplasm at 0.2 R per min; phospho-Smad complexes are imported at
the same rate but exported ten times more slowly (0.03/min) and are dephosphorylated in the nucleus
(0.1/min), which returns Smad to the free pool. TGF-beta (R = 1) is added at t = 0; at 60 min the receptor
kinase is blocked (R = 0, as with the inhibitor SB-431542), and Smad leaves the nucleus within about half an
hour: the nuclear level reports current receptor activity, not past exposure (after Inman and colleagues,
2002, and Schmierer and Hill, 2005).
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts, network

P = bio.P
FS = bio.core.FONT["tiny"]
fig, ax = bio.canvas(22.0, 10.6)
d = network.Diagram(ax, size="small")
Y = [9.5, 8.1, 6.7, 5.3, 3.9, 2.5, 1.1]
W = 4.3

# A TGF-beta
x = 2.8
bio.panel(ax, "A", (0.1, 10.5))
bio.label(ax, (x, 10.4), "TGF-β / Smad", size="small", bold=True)
items = [("t0", "TGF-β, activin, BMP", "drug"), ("t1", "type II receptor kinase", "receptor"),
         ("t2", "type I receptor (P on GS region)", "receptor"), ("t3", "R-Smad (Smad2/3) ~P", "highlight"),
         ("t4", "R-Smad–Smad4 complex", "highlight"), ("t5", "nuclear cofactors, DNA", "dna"),
         ("t6", "p15, p21, Smad7, ECM genes", "positive")]
for (id_, text, tok), y in zip(items, Y):
    d.activity(id_, (x, y), text, token=tok, w=W)
for a, b in zip([i[0] for i in items[:-1]], [i[0] for i in items[1:]]):
    d.connect(a, b, "positive")
d.connect("t6", "t2", "negative", dashed=True, via=[(x + 2.4, Y[6]), (x + 2.4, Y[2])])
bio.label(ax, (x + 2.6, 4.6), "Smad7", size="tiny", color=P.muted(), rotation=90)

# B Hippo
x = 9.1
bio.panel(ax, "B", (6.5, 10.5))
bio.label(ax, (x, 10.4), "Hippo–YAP/TAZ", size="small", bold=True)
d.activity("h0", (x - 1.1, Y[0]), "contact, polarity (NF2), soft matrix", token="neutral", w=W + 0.6)
d.activity("h1", (x - 1.1, Y[1]), "MST1/2 + SAV1", token="enzyme", w=3.2)
d.activity("h2", (x - 1.1, Y[2]), "LATS1/2 + MOB1", token="enzyme", w=3.2)
d.activity("h3", (x, Y[3]), "YAP / TAZ", token="highlight", w=3.2)
d.activity("h4", (x, Y[4]), "TEAD", token="dna", w=3.2)
d.activity("h5", (x, Y[5]), "CTGF, CYR61, Myc …", token="positive", w=3.2)
d.phenotype("h6", (x, Y[6]), "proliferation, survival", token="positive")
d.activity("m0", (x + 3.0, Y[1]), "stiff ECM, GPCR (G12/13)", token="drug", w=3.4)
d.activity("m1", (x + 3.0, Y[2]), "Rho, F-actin", token="receptor", w=2.0)
d.connect("h0", "h1", "positive")
d.connect("h1", "h2", "positive")
d.connect("h2", "h3", "negative")
d.connect("h3", "h4", "positive")
d.connect("h4", "h5", "positive")
d.connect("h5", "h6", "positive")
d.connect("m0", "m1", "positive")
d.connect("m1", "h2", "negative")
d.connect("m1", "h3", "positive")

# C Smad shuttling model
bio.panel(ax, "C", (13.6, 10.5))
pc = charts.axes_at(ax, (15.0, 1.4, 6.5, 8.2))
ki, ke, kep, kd, kp = 0.3, 0.3, 0.03, 0.1, 0.2


def R(t):
    return 1.0 if 0 <= t < 60 else 0.0


def f(t, y):
    sc, sn, pc_, pn = y
    return [-ki * sc + ke * sn - kp * R(t) * sc + 0.0,
            ki * sc - ke * sn + kd * pn,
            kp * R(t) * sc - ki * pc_ + kep * pn,
            ki * pc_ - kep * pn - kd * pn]


t = np.linspace(-20, 150, 1701)
s = solve_ivp(f, (-20, 150), [0.5, 0.5, 0.0, 0.0], t_eval=t, max_step=0.2)
nuc = s.y[1] + s.y[3]
pc.axvspan(0, 60, color=P.fill("drug"), alpha=0.18, lw=0)
pc.text(30, 0.97, "TGF-β", fontsize=FS, color=P.muted(), ha="center")
pc.text(100, 0.97, "receptor inhibitor", fontsize=FS, color=P.muted(), ha="center")
pc.plot(t, nuc, color=charts.line("highlight"), lw=2.0, label="total nuclear Smad2")
pc.plot(t, s.y[3], color=charts.line("receptor"), lw=1.3, ls=(0, (4, 2)), label="nuclear phospho-Smad2")
pc.set_xlim(-20, 150)
pc.set_ylim(0, 1.05)
pc.legend(frameon=False, fontsize=FS, labelcolor=P.ink(), loc="lower right", bbox_to_anchor=(1.0, 0.26))
charts.style_axes(pc, "time / min", "fraction of Smad2")
charts.title(pc, "The nucleus reports receptor activity")
