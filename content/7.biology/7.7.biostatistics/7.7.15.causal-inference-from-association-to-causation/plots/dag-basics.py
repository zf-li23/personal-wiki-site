"""Causal diagrams (schematic). A-C: the three elementary structures between an exposure A and an outcome
Y through a third variable: a confounder L (fork, A <- L -> Y), a mediator M (chain, A -> M -> Y) and a
collider C (A -> C <- Y). Adjusting for L removes bias; adjusting for M removes part of the effect;
adjusting for C creates an association where there was none. D: a causal diagram for smoking and FEV in
children: age and sex affect smoking, height and FEV; height lies partly on the path from smoking to FEV.
"""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(19, 9.6)


def node(xy, text, tok="neutral", w=1.7):
    bio.box(ax, xy, w, 0.85, token=tok, text=text, size="small")


def edge(a, b, bend=0.0, dashed=False):
    bio.arrow(ax, a, b, kind="process", color=P.ink(), shrink=0.62, bend=bend, dashed=dashed, lw=1.3)


def panel(x0, y0, title, kind):
    bio.label(ax, (x0 + 0.1, y0 + 3.55), title, size="small", bold=True, ha="left")
    A, Y = (x0 + 0.8, y0 + 0.8), (x0 + 4.6, y0 + 0.8)
    T = (x0 + 2.7, y0 + 2.6)
    node(A, "A", "rna", 1.1)
    node(Y, "Y", "dna", 1.1)
    if kind == "fork":
        node(T, "L", "neutral", 1.1)
        edge(T, A)
        edge(T, Y)
        edge(A, Y)
        note = "adjust for L"
    elif kind == "chain":
        node(T, "M", "enzyme", 1.1)
        edge(A, T)
        edge(T, Y)
        edge(A, Y)
        note = "do not adjust for M (total effect)"
    else:
        node(T, "C", "highlight", 1.1)
        edge(A, T)
        edge(Y, T)
        note = "do not adjust for C"
    bio.label(ax, (x0 + 2.7, y0 + 0.05), note, size="tiny", color=P.muted())


panel(0.2, 5.4, "A  Confounder", "fork")
panel(6.4, 5.4, "B  Mediator", "chain")
panel(12.6, 5.4, "C  Collider", "collider")
bio.label(ax, (0.3, 4.6), "D  Smoking and FEV in children", size="small", bold=True, ha="left")
pos = {"age": (1.8, 3.0), "sex": (1.8, 0.7), "smoke": (6.5, 3.85), "height": (8.5, 0.7), "FEV": (13.5, 2.3)}
tok = {"age": "neutral", "sex": "neutral", "smoke": "rna", "height": "enzyme", "FEV": "dna"}
for k, xy in pos.items():
    node(xy, k, tok[k], 1.7)
edge(pos["age"], pos["smoke"])
edge(pos["age"], pos["height"])
edge(pos["age"], pos["FEV"])
edge(pos["sex"], pos["height"])
edge(pos["sex"], pos["FEV"])
edge(pos["sex"], pos["smoke"], dashed=True)
edge(pos["smoke"], pos["height"])
edge(pos["height"], pos["FEV"])
edge(pos["smoke"], pos["FEV"])
bio.label(ax, (15.2, 3.9), "total effect of smoking:", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (15.2, 3.35), "adjust for age and sex,", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (15.2, 2.8), "not for height", size="tiny", color=P.muted(), ha="left")
