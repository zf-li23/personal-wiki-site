# Choosing an ion exchanger from the net charge of a protein. Net charge Z(pH) computed from the numbers of
# ionizable groups with typical pKa values in proteins (N-terminus 8.0, C-terminus 3.1, Asp 3.9, Glu 4.1,
# His 6.0, Tyr 10.1, Lys 10.5, Arg 12.5) for hen lysozyme (K6 R11 H1 D7 E2 Y3; all 8 Cys in disulfides) and for
# a hypothetical acidic protein (K12 R6 H4 D18 E16 Y6). At pH 7.5 (dashed) lysozyme is positive and binds a
# cation exchanger (CM), the acidic protein is negative and binds an anion exchanger (DEAE).
import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts as C

pka = {"Nt": (8.0, 1), "Ct": (3.1, 0), "D": (3.9, 0), "E": (4.1, 0), "H": (6.0, 1), "Y": (10.1, 0),
       "K": (10.5, 1), "R": (12.5, 1)}


def Z(comp, pH):
    z = 0.0
    for g, n in comp.items():
        p, basic = pka[g]
        z += n / (1 + 10 ** (pH - p)) if basic else -n / (1 + 10 ** (p - pH))
    return z


lyso = {"Nt": 1, "Ct": 1, "K": 6, "R": 11, "H": 1, "D": 7, "E": 2, "Y": 3}
acid = {"Nt": 1, "Ct": 1, "K": 12, "R": 6, "H": 4, "D": 18, "E": 16, "Y": 6}
pH = np.linspace(2, 13, 500)

fig, ax = bio.canvas(14, 8.4)
F = bio.core.FONT["tiny"]
a = C.axes_at(ax, (1.9, 1.5, 11.4, 6.4))
band = bio.P.mix(bio.P.surface(), bio.P.muted(), 0.18)
a.axhspan(0, 20, color=bio.P.mix(bio.P.surface(), bio.P.fill("positive"), 0.25), lw=0)
a.axhspan(-40, 0, color=bio.P.mix(bio.P.surface(), bio.P.fill("dna"), 0.25), lw=0)
a.text(12.8, 17.5, "binds cation exchanger\n(CM-, S-matrix)", ha="right", va="top", fontsize=F, color=bio.P.ink())
a.text(2.2, -28, "binds anion exchanger\n(DEAE-, Q-matrix)", ha="left", va="top", fontsize=F, color=bio.P.ink())
for comp, tok, name in [(lyso, "negative", "lysozyme"), (acid, "dna", "acidic protein")]:
    z = Z(comp, pH)
    a.plot(pH, z, color=C.line(tok), lw=2.2)
    pi = brentq(lambda x: Z(comp, x), 2, 13)
    a.plot([pi], [0], "D", ms=5, mfc=bio.P.surface(), mec=C.line(tok), mew=1.3)
    a.text(pi + 0.15, 1.2, f"pI {pi:.1f}", fontsize=F, color=C.line(tok))
    zz = Z(comp, 7.5)
    a.plot([7.5], [zz], "o", ms=5, color=C.line(tok))
    a.text(7.65, zz + (1.0 if zz > 0 else -4.5), f"{name}: Z = {zz:+.1f}".replace("-", "\u2212"), fontsize=F, color=C.line(tok))
a.axhline(0, color=bio.P.muted(), lw=0.8)
a.axvline(7.5, color=bio.P.muted(), lw=0.8, ls=(0, (3, 3)))
a.set_xlim(2, 13)
a.set_ylim(-40, 20)
C.style_axes(a, "pH", "net charge Z")
