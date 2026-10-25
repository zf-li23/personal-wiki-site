# Regulatory logic of the lac operon, the trp operon and the lambda switch as SBGN Activity Flow maps.
# A: lac: lactose enters through LacY and LacZ makes allolactose, which inactivates LacI; transcription of
#    lacZYA needs CAP-cAMP AND NOT LacI; glucose transport inhibits adenylate cyclase (CyaA) and, by inducer
#    exclusion, LacY; LacY and LacZ are products of the operon (positive feedback).
# B: trp: Trp activates the TrpR repressor and, as charged tRNA-Trp, favors termination at the attenuator;
#    both inhibit trpEDCBA, whose enzymes make Trp (negative feedback by two routes).
# C: lambda: DNA damage activates RecA, which induces CI cleavage; CIII inhibits the protease FtsH, which
#    degrades CII; CII activates cI (from PRE); CI activates its own PRM (positive autoregulation) and represses
#    it at high concentration (dashed); CI and Cro repress each other; CI represses PL (N); N (antitermination)
#    allows CIII and Q, Q the late genes; CI maintains lysogeny, the late genes lead to lysis.
import wikibio as bio
from wikibio import network

fig, ax = bio.canvas(20.0, 25.5)
d = network.Diagram(ax)
P = bio.P

# ----------------------------------------------------------------- A: lac (y 17.2 .. 25.2)
bio.panel(ax, "A", (0.1, 25.35))
o = 16.9
d.compartment("cell", (3.4, o + 0.3, 19.6, o + 8.2), "Cytoplasm", token="cytoplasm", label_pos="tr")
bio.label(ax, (1.75, o + 7.9), "Medium", size="small", bold=True, color=network.container_edge("extracellular"))
y1, y2, y3, y4 = o + 6.9, o + 5.0, o + 3.3, o + 1.4
d.activity("lac_out", (1.75, y1), "Lactose", token="carbohydrate")
d.activity("glc", (1.75, y4), "Glucose", token="carbohydrate")
d.activity("lac_in", (6.6, y1), "Lactose", token="carbohydrate")
d.activity("allo", (11.0, y1), "Allolactose", token="carbohydrate")
d.activity("laci", (16.8, y1), "LacI", token="negative")
d.activity("lacy", (6.6, y2), "LacY", token="channel")
d.activity("lacz", (11.0, y2), "LacZ", token="enzyme")
d.activity("operon", (11.0, y3), "lacZYA", token="dna", italic=True, units=[("ct:gene", "nucleic", "bl")])
d.activity("cya", (6.6, y4), "CyaA", token="protein")
d.activity("camp", (11.0, y4), "cAMP", token="metabolite")
d.activity("cap", (16.8, y4), "CAP", token="positive")
d.logic("not", (16.8, y2), "NOT", angle=-90)
d.logic("and", (15.0, y3), "AND", angle=180)
d.connect("lac_out", "lac_in", "positive")
d.connect("lacy", "lac_in", "necessary")
d.connect("lac_in", "allo", "positive")
d.connect("lacz", "allo", "necessary")
d.connect("allo", "laci", "negative")
d.connect("laci", "not", "logic")
d.connect("not", "and", "logic", via=[(16.8, y3)])
d.connect("cap", "and", "logic", via=[(16.8, y3)])
d.connect("and", "operon", "positive")
d.connect("glc", "cya", "negative")
d.connect("cya", "camp", "positive")
d.connect("camp", "cap", "positive")
d.connect("operon", "lacz", "positive")
d.connect("operon", "lacy", "positive", via=[(6.6, y3)])
d.connect("glc", "lacy", "negative", dashed=True, via=[(1.75, y2)])
bio.label(ax, (4.6, y2 + 0.3), "inducer exclusion", size="tiny", color=P.muted())

# ----------------------------------------------------------------- B: trp (y 9.0 .. 16.2)
bio.panel(ax, "B", (0.1, 16.45))
o = 9.0
d.compartment("cell2", (0.6, o + 0.3, 19.6, o + 7.0), "Cytoplasm", token="cytoplasm", label_pos="tr")
yt, ym, yb = o + 5.6, o + 3.6, o + 1.5
d.activity("trp", (4.0, ym), "Tryptophan", token="metabolite")
d.activity("trpr", (10.0, yt), "TrpR", token="negative")
d.activity("trna", (10.0, yb), "Trp-tRNA(Trp)", token="trna")
d.activity("trpop", (15.8, ym), "trpEDCBA", token="dna", italic=True, units=[("ct:gene", "nucleic", "bl")])
d.connect("trp", "trpr", "positive")
d.connect("trp", "trna", "positive")
d.connect("trpr", "trpop", "negative")
d.connect("trna", "trpop", "negative")
d.connect("trpop", "trp", "positive", bend=0.0, via=[(15.8, o + 0.95), (4.0, o + 0.95)])
bio.label(ax, (13.4, yt + 0.25), "repression (~70×)", size="tiny", color=P.muted())
bio.label(ax, (14.3, yb + 0.95), "attenuation (~10×)", size="tiny", color=P.muted())
bio.label(ax, (8.0, o + 0.7), "Trp biosynthetic enzymes", size="tiny", color=P.muted())

# ----------------------------------------------------------------- C: lambda (y 0.2 .. 8.2)
bio.panel(ax, "C", (0.1, 8.45))
d.compartment("cell3", (0.6, 0.3, 19.6, 8.0), "Infected cell", token="cytoplasm", label_pos="tr")
r1, r2, r3 = 6.6, 4.2, 1.5
d.activity("dmg", (2.4, r1), "DNA damage", token="negative")
d.activity("reca", (2.4, r2), "RecA*", token="protein")
d.activity("cii", (9.2, r1), "CII", token="positive")
d.activity("ftsh", (13.0, r1), "FtsH", token="enzyme")
d.activity("ciii", (16.8, r1), "CIII", token="protein")
d.activity("ci", (6.0, r2), "CI", token="negative")
d.activity("cro", (10.4, r2), "Cro", token="highlight")
d.activity("n", (14.4, r2), "N", token="protein")
d.activity("q", (17.6, r2), "Q", token="protein")
d.phenotype("lyso", (6.0, r3), "Lysogeny")
d.phenotype("lysis", (17.6, r3), "Lysis")
d.connect("dmg", "reca", "positive")
d.connect("reca", "ci", "negative")
d.connect("ciii", "ftsh", "negative")
d.connect("ftsh", "cii", "negative")
d.connect("cii", "ci", "positive")
d.connect("ci", "ci", "positive", loop=120)
d.connect("ci", "ci", "negative", loop=190, dashed=True)
d.connect("ci", "cro", "negative", bend=0.25)
d.connect("cro", "ci", "negative", bend=0.25)
d.connect("ci", "n", "negative", via=[(7.4, 3.0), (14.4, 3.0)])
d.connect("n", "ciii", "positive")
d.connect("n", "q", "positive")
d.connect("q", "lysis", "positive")
d.connect("ci", "lyso", "positive")
bio.label(ax, (11.0, 2.7), "CI represses PL (N) and PR", size="tiny", color=P.muted())
