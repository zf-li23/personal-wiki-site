# mTORC1, the integrator of growth signals for translation.
# A: inputs: insulin and growth factors act through PI3K and PKB (Akt), which phosphorylates and inhibits the
#    TSC complex, the GAP of the small GTPase Rheb; Rheb-GTP activates mTORC1 on the lysosome, where amino acids
#    recruit mTORC1 through the Rag GTPases; low energy activates AMPK, which activates TSC2 and inhibits Raptor;
#    rapamycin with FKBP12 inhibits mTORC1. Outputs: phosphorylation of 4E-BP1 releases eIF4E for binding
#    eIF4G (eIF4F assembly, cap-dependent initiation); S6K1 phosphorylates rpS6 and eIF4B and triggers the
#    degradation of PDCD4, an inhibitor of eIF4A; LARP1 repression of 5' TOP mRNAs (ribosomal proteins,
#    elongation factors) is relieved.
# B: competition of 4E-BP and eIF4G for eIF4E (equilibrium binding, same binding site, totals eIF4E = 1,
#    eIF4G = 0.6, 4E-BP = 2, dissociation constants 0.01 for eIF4G and 0.002 for 4E-BP, illustrative values; phosphorylated 4E-BP does not bind): eIF4F
#    forms only when most 4E-BP is phosphorylated, a threshold set by the excess of 4E-BP over eIF4E.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(12.6, 5.0))
gs = fig.add_gridspec(1, 2, width_ratios=[1.45, 1])
ax = fig.add_subplot(gs[0])
ax.set_xlim(0, 15)
ax.set_ylim(0, 9)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("A   Inputs and outputs of mTORC1", loc="left", fontsize=9, color=P.ink())

B = {}


def node(k, xy, text, tok, w=2.0, h=0.6):
    bio.box(ax, xy, w, h, token=tok, text=text, size="tiny")
    B[k] = (xy, w, h)


node("ins", (1.4, 8.3), "insulin, GF", "drug")
node("pi3k", (1.4, 7.1), "PI3K → PKB", "enzyme")
node("tsc", (1.4, 5.6), "TSC1/2 (GAP)", "negative")
node("rheb", (4.4, 5.6), "Rheb·GTP", "receptor")
node("ampk", (4.4, 8.3), "AMPK (ATP ↓)", "highlight")
node("aa", (10.6, 8.3), "amino acids", "metabolite")
node("rag", (10.6, 7.1), "Rag GTPases", "receptor")
node("rapa", (12.9, 5.6), "rapamycin·FKBP12", "drug", w=2.6)
node("mtor", (7.5, 5.6), "mTORC1", "protein", w=2.4, h=0.8)
node("bp", (2.3, 3.2), "4E-BP1", "negative")
node("e4e", (2.3, 1.4), "eIF4E → eIF4F", "enzyme", w=2.6)
node("s6k", (7.5, 3.2), "S6K1", "positive")
node("pd", (7.5, 1.4), "eIF4B ↑, PDCD4 ↓, rpS6", "positive", w=3.6)
node("larp", (12.4, 3.2), "LARP1", "negative")
node("top", (12.4, 1.4), "5′ TOP mRNAs", "mrna", w=2.6)


def edge(a, b, kind, dashed=False):
    (xa, ya), wa, ha = B[a]
    (xb, yb), wb, hb = B[b]
    d = np.array([xb - xa, yb - ya], float)
    d /= np.hypot(*d)

    def edge_pt(x, y, w, h, s):
        t = min((w / 2 + 0.05) / max(abs(d[0]), 1e-9), (h / 2 + 0.05) / max(abs(d[1]), 1e-9))
        return (x + s * d[0] * t, y + s * d[1] * t)
    bio.arrow(ax, edge_pt(xa, ya, wa, ha, 1), edge_pt(xb, yb, wb, hb, -1), kind=kind, dashed=dashed)


edge("ins", "pi3k", "activation")
edge("pi3k", "tsc", "inhibition")
edge("tsc", "rheb", "inhibition")
edge("rheb", "mtor", "activation")
edge("ampk", "tsc", "activation")
edge("ampk", "mtor", "inhibition")
edge("aa", "rag", "activation")
edge("rag", "mtor", "activation")
edge("rapa", "mtor", "inhibition")
edge("mtor", "bp", "inhibition")
edge("bp", "e4e", "inhibition")
edge("mtor", "s6k", "activation")
edge("s6k", "pd", "activation")
edge("mtor", "larp", "inhibition")
edge("larp", "top", "inhibition")
bio.label(ax, (9.9, 5.05), "on the lysosome surface", size="tiny", color=P.muted())

# --- B ---
ax = fig.add_subplot(gs[1])
ET, GT, BT, KG, KB = 1.0, 0.6, 2.0, 0.01, 0.002


def eif4f(bfree_total):
    # solve for free eIF4E e: ET = e + EG + EB with EG = e g/KG, EB = e b/KB, g = GT - EG, b = BT - EB
    def resid(e):
        eg = GT * e / (KG + e)
        eb = bfree_total * e / (KB + e)
        return e + eg + eb - ET
    e = brentq(resid, 0, ET)
    return GT * e / (KG + e)


ph = np.linspace(0, 1, 300)
f = np.array([eif4f(BT * (1 - x)) for x in ph])
ax.plot(ph, f / GT, color=charts.line("enzyme"), lw=1.8, label="eIF4G bound to eIF4E")
fb = np.array([BT * (1 - x) for x in ph])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.05)
charts.style_axes(ax, "fraction of 4E-BP phosphorylated", "fraction of eIF4G in eIF4F")
ax.axvline(1 - (ET - GT) / BT, color=P.muted(), lw=0.7, ls=":")
ax.text(1 - (ET - GT) / BT - 0.02, 0.9, "active 4E-BP = eIF4E − eIF4G", fontsize=7, color=P.muted(), ha="right")
ax.set_title("B   4E-BP sets a threshold for eIF4F", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
