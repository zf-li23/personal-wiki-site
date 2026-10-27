"""Rho-family GTPases divide the work of reorganizing the actin cytoskeleton.

A (SBGN activity flow): receptors reach the Rho-family GTPases through GEFs and GAPs. Receptor tyrosine
kinases and Gbeta-gamma of GPCRs make PIP3, which recruits PH-domain GEFs (Vav, Tiam1, P-Rex, beta-PIX) for
Rac and Cdc42; integrins act through FAK, Src and the Crk-p130Cas complex on DOCK180-ELMO (Rac) and on
p190RhoGAP, which keeps Rho low while a cell spreads; G12/13-coupled receptors activate p115-RhoGEF (and LARG,
PDZ-RhoGEF); ephrin-activated Eph receptors activate ephexin (Rho, growth-cone collapse). The GTPases act
through their effectors on actin: Cdc42 through mDia2 and N-WASP (Arp2/3), filopodia; Rac through WAVE
(Arp2/3) and PAK, the lamellipodium; Rho through mDia1 and ROCK, which raises myosin regulatory light-chain
phosphorylation: stress fibers and contraction. Cdc42 activates Rac, and Rac and Rho inhibit each other.
B: mutual inhibition makes a switch. A minimal model dRac/dt = s + a/(1 + (Rho/K)^3) - Rac,
dRho/dt = a/(1 + (Rac/K)^3) - Rho (a = 1.5, K = 0.5, s = 0.05) has two stable states, Rac high and Rho
low (a front) or the reverse (a rear), separated by a saddle: the nullclines (solid: dRac/dt = 0,
dashed: dRho/dt = 0) cross three times.
"""

import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts, network

P = bio.P
FS = bio.core.FONT["tiny"]
fig, ax = bio.canvas(22.0, 11.4)

# A: from receptors to actin structures
bio.panel(ax, "A", (0.1, 11.3))
d = network.Diagram(ax, size="small")
d.activity("i1", (2.6, 10.4), "RTK, GPCR (Gβγ) → PIP₃", token="drug")
d.activity("i2", (7.0, 10.4), "integrins → FAK, Src", token="drug")
d.activity("i3", (10.4, 10.4), "GPCR (G12/13)", token="drug")
d.activity("i4", (13.2, 10.4), "ephrin → Eph", token="drug")
d.activity("g1", (2.6, 8.9), "Vav, Tiam1, P-Rex, β-PIX", token="positive")
d.activity("g2", (5.7, 8.9), "DOCK180–ELMO", token="positive")
d.activity("g3", (8.4, 8.9), "p190RhoGAP", token="negative")
d.activity("g4", (10.7, 8.9), "p115-RhoGEF", token="positive")
d.activity("g5", (13.2, 8.9), "ephexin", token="positive")
d.activity("cdc42", (2.0, 7.2), "Cdc42", token="receptor")
d.activity("rac", (5.6, 7.2), "Rac", token="receptor")
d.activity("rho", (10.4, 7.2), "Rho", token="receptor")
d.activity("mdia2", (0.9, 5.5), "mDia2", token="protein")
d.activity("nwasp", (2.6, 5.5), "N-WASP", token="protein")
d.activity("wave", (4.6, 5.5), "WAVE", token="protein")
d.activity("pak", (6.6, 5.5), "PAK", token="enzyme")
d.activity("mdia1", (9.3, 5.5), "mDia1", token="protein")
d.activity("rock", (11.6, 5.5), "ROCK", token="enzyme")
d.activity("arp", (3.6, 3.8), "Arp2/3", token="channel")
d.activity("myo", (11.6, 3.8), "myosin II (MLC-P)", token="muscle")
d.phenotype("filo", (1.2, 2.0), "filopodia", token="positive")
d.phenotype("lamel", (4.8, 2.0), "lamellipodium", token="positive")
d.phenotype("sf", (10.4, 2.0), "stress fibers, contraction", token="positive")
for a, b, k in (("i1", "g1", "positive"), ("i2", "g2", "positive"), ("i2", "g3", "positive"),
                ("i3", "g4", "positive"), ("i4", "g5", "positive"), ("g1", "cdc42", "positive"),
                ("g1", "rac", "positive"), ("g2", "rac", "positive"), ("g3", "rho", "negative"),
                ("g4", "rho", "positive"), ("g5", "rho", "positive"), ("cdc42", "nwasp", "positive"),
                ("cdc42", "mdia2", "positive"), ("rac", "wave", "positive"), ("rac", "pak", "positive"),
                ("rho", "mdia1", "positive"), ("rho", "rock", "positive"), ("nwasp", "arp", "positive"),
                ("wave", "arp", "positive"), ("arp", "lamel", "positive"), ("mdia2", "filo", "positive"),
                ("mdia1", "sf", "positive"), ("rock", "myo", "positive"), ("myo", "sf", "positive"),
                ("cdc42", "rac", "positive")):
    d.connect(a, b, k)
d.connect("rac", "rho", "negative", bend=0.25)
d.connect("rho", "rac", "negative", bend=0.25)
bio.label(ax, (8.0, 6.05), "mutual inhibition", size="tiny", color=P.muted())

# C: phase plane of the mutual-inhibition switch
bio.panel(ax, "B", (14.9, 11.3))
pc = charts.axes_at(ax, (16.4, 4.0, 5.2, 5.6))
a, K, s, n = 1.5, 0.5, 0.05, 3
r = np.linspace(0, 1.8, 300)
pc.plot(s + a / (1 + (r / K) ** n), r, color=charts.line("receptor"), lw=1.6)  # dRac/dt = 0: Rac as f(Rho)
pc.plot(r, a / (1 + (r / K) ** n), color=charts.line("muscle"), lw=1.6, ls=(0, (4, 2)))
RR, HH = np.meshgrid(np.linspace(0, 1.8, 20), np.linspace(0, 1.8, 20))
U = s + a / (1 + (HH / K) ** n) - RR
V = a / (1 + (RR / K) ** n) - HH
pc.streamplot(RR, HH, U, V, color=P.mix(P.muted(), P.surface(), 0.4), density=0.7, linewidth=0.5, arrowsize=0.6)


def g(x):
    h = a / (1 + (x / K) ** n)
    return s + a / (1 + (h / K) ** n) - x


roots = []
xs = np.linspace(0.001, 1.8, 2000)
vals = g(xs)
for i in range(len(xs) - 1):
    if vals[i] * vals[i + 1] < 0:
        roots.append(brentq(g, xs[i], xs[i + 1]))
for k, x in enumerate(roots):
    h = a / (1 + (x / K) ** n)
    stable = k != 1
    pc.plot(x, h, "o", ms=6, color=P.ink() if stable else P.surface(), mec=P.ink(), zorder=5)
pc.text(1.45, 0.32, "front", fontsize=FS, color=P.ink(), ha="center")
pc.text(0.2, 1.62, "rear", fontsize=FS, color=P.ink())
pc.set_xlim(0, 1.8)
pc.set_ylim(0, 1.8)
charts.style_axes(pc, "Rac activity", "Rho activity")
charts.title(pc, "Mutual inhibition: two states")
bio.label(ax, (19.2, 2.6), "filled: stable states\nopen: saddle (threshold)", size="tiny", color=P.muted())
