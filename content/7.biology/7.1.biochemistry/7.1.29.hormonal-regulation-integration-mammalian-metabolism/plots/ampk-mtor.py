"""AMPK, the energy sensor, and mTORC1, the nutrient and growth sensor (activity-flow diagram).
AMPK is activated when AMP and ADP rise relative to ATP (exercise, fasting, hypoxia), by phosphorylation of
Thr172 by LKB1 (or by CaMKK2 when Ca2+ rises), by adiponectin through its receptors, and indirectly by
metformin, which raises AMP by inhibiting mitochondrial respiration. Its targets switch catabolism on and
anabolism off: phosphorylation inactivates acetyl-CoA carboxylase (malonyl-CoA falls, so fatty acid synthesis
stops and beta oxidation is disinhibited), HMG-CoA reductase, glycerol-3-phosphate acyltransferase and glycogen
synthase; phosphorylation of TBC1D1 promotes GLUT4 translocation in muscle; AMPK activates ULK1 (autophagy) and
PGC-1alpha (mitochondrial biogenesis), and inhibits mTORC1 by activating TSC2 and phosphorylating raptor.
mTORC1 on the lysosome is activated by amino acids (Rag GTPases) and by Rheb-GTP when insulin, through PKB,
inhibits TSC2, the GAP of Rheb; it stimulates protein synthesis (S6K, 4E-BP), lipid synthesis (SREBP) and
nucleotide synthesis (CAD, ATF4-MTHFD2), and inhibits autophagy (ULK1)."""

import numpy as np

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(21.0, 10.6)
B = {}


def node(k, xy, text, tok, w=2.6, h=0.75, size="tiny"):
    bio.box(ax, xy, w, h, token=tok, text=text, size=size)
    B[k] = (xy, w, h)


def edge(a, b, kind, dashed=False, bend=0.0):
    (xa, ya), wa, ha = B[a]
    (xb, yb), wb, hb = B[b]
    d = np.array([xb - xa, yb - ya], float)
    d /= np.hypot(*d)

    def pt(x, y, w, h, s):
        t = min((w / 2 + 0.06) / max(abs(d[0]), 1e-9), (h / 2 + 0.06) / max(abs(d[1]), 1e-9))
        return (x + s * d[0] * t, y + s * d[1] * t)
    col = P.edge("positive") if kind == "activation" else P.edge("negative") if kind == "inhibition" else P.ink()
    bio.arrow(ax, pt(xa, ya, wa, ha, 1), pt(xb, yb, wb, hb, -1), kind=kind, dashed=dashed, color=col, lw=1.6,
              bend=bend)


# inputs
node("stress", (2.2, 9.6), "exercise, fasting, hypoxia:\nAMP, ADP ↑", "atp", w=3.6, h=0.95)
node("adipo", (6.4, 9.6), "adiponectin\n(AdipoR1)", "lipid", w=2.6, h=0.95)
node("met", (9.9, 9.6), "metformin\n(respiration ↓)", "drug", w=2.6, h=0.95)
node("ins", (14.2, 9.6), "insulin → PKB", "receptor", w=2.8)
node("aa", (18.6, 9.6), "amino acids\n(Rag GTPases)", "metabolite", w=2.6, h=0.95)
# core
node("lkb1", (3.0, 7.4), "LKB1 (Thr172)", "enzyme")
node("ampk", (6.4, 6.2), "AMPK", "highlight", w=2.8, h=1.0, size="normal")
node("tsc", (11.2, 6.2), "TSC2 (GAP)", "negative")
node("rheb", (14.6, 6.2), "Rheb·GTP", "receptor")
node("mtor", (18.0, 6.2), "mTORC1", "protein", w=2.8, h=1.0, size="normal")
# AMPK outputs
node("acc", (1.6, 3.8), "ACC", "enzyme", w=1.8)
node("hmgr", (3.8, 3.8), "HMGR", "enzyme", w=1.8)
node("gs", (6.0, 3.8), "GPAT, glycogen\nsynthase", "enzyme", w=2.4, h=0.95)
node("tbc", (8.5, 3.8), "TBC1D1", "channel", w=2.0)
node("pgc", (10.9, 3.8), "PGC-1α", "positive", w=2.0)
node("ulk", (13.0, 2.2), "ULK1", "positive", w=2.0)
# mTORC1 outputs
node("s6k", (15.6, 3.8), "S6K, 4E-BP", "positive", w=2.2)
node("srebp", (17.9, 3.8), "SREBP", "positive", w=1.8)
node("cad", (20.0, 3.8), "CAD, ATF4", "positive", w=1.8)

edge("stress", "ampk", "activation")
edge("lkb1", "ampk", "activation")
edge("adipo", "ampk", "activation")
edge("met", "ampk", "activation", dashed=True)
edge("ampk", "tsc", "activation")
edge("ins", "tsc", "inhibition")
edge("tsc", "rheb", "inhibition")
edge("rheb", "mtor", "activation")
edge("aa", "mtor", "activation")
edge("ampk", "mtor", "inhibition", bend=-0.25)
for k in ("acc", "hmgr", "gs"):
    edge("ampk", k, "inhibition")
for k in ("tbc", "pgc"):
    edge("ampk", k, "activation")
edge("ampk", "ulk", "activation", bend=0.15)
edge("mtor", "ulk", "inhibition", bend=-0.15)
for k in ("s6k", "srebp", "cad"):
    edge("mtor", k, "activation")

out = [((1.6, 2.95), "malonyl-CoA ↓:\nFA synthesis ↓,\nβ oxidation ↑"), ((3.8, 2.95), "cholesterol\nsynthesis ↓"),
       ((6.0, 2.95), "TAG, glycogen\nsynthesis ↓"), ((8.5, 2.95), "GLUT4 →\nmembrane"),
       ((10.9, 2.95), "mitochondrial\nbiogenesis"), ((13.0, 1.4), "autophagy"),
       ((15.6, 2.95), "protein\nsynthesis"), ((17.9, 2.95), "lipid\nsynthesis"), ((20.0, 2.95), "nucleotide\nsynthesis\n(7.1.28)")]
for xy, t in out:
    bio.label(ax, xy, t, size="tiny", color=P.muted(), va="top")
bio.label(ax, (4.8, 0.5), "catabolism ↑, anabolism ↓ (energy stress)", size="small", bold=True, color=P.edge("atp"))
bio.label(ax, (17.4, 0.5), "growth and biosynthesis (fed state)", size="small", bold=True, color=P.edge("protein"))
