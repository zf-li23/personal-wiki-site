# Acid-base behaviour of amino acids and peptides, computed from pKa values.
# A: titration curves (pH against equivalents of OH- added to the fully protonated form) of glycine,
# glutamate and histidine (pKa from Lehninger Table 3-1); dots mark the pKa values and diamonds the pI,
# where the average net charge is zero.
# B: net charge Z(pH) = sum over basic groups of 1/(1 + 10^(pH - pKa)) - sum over acidic groups of
# 1/(1 + 10^(pKa - pH)) for the tetrapeptide Ala-Glu-Gly-Lys and for glucagon (29 residues), with typical
# pKa values of groups in peptides; the pI is the root of Z, found with brentq.
import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts as C

aa = {  # name: (list of (pKa, kind)), kind +1 for groups that are positive when protonated
    "Gly": [(2.34, 0), (9.60, 1)],
    "Glu": [(2.19, 0), (4.25, 0), (9.67, 1)],
    "His": [(1.82, 0), (6.00, 1), (9.17, 1)],
}
tokens = {"Gly": "neutral", "Glu": "negative", "His": "positive"}
pH = np.linspace(0.5, 13.0, 600)


def deprot(pka, x):
    return 1 / (1 + 10 ** (pka - x))


def charge(groups, x):
    z = 0.0
    for pka, kind, n in groups:
        if kind:
            z += n / (1 + 10 ** (x - pka))
        else:
            z -= n / (1 + 10 ** (pka - x))
    return z


fig, ax = bio.canvas(20, 8.6)
F = bio.core.FONT["tiny"]
a = C.axes_at(ax, (1.7, 1.5, 7.6, 6.4))
for k, (name, groups) in enumerate(aa.items()):
    eq = sum(deprot(p, pH) for p, _ in groups)
    col = C.line(tokens[name])
    a.plot(eq, pH, color=col, lw=2.0)
    for j, (p, _) in enumerate(groups):
        a.plot([j + 0.5], [p], "o", ms=4, color=col)
    zg = [(p, kind, 1) for p, kind in groups]
    pi = brentq(lambda x: charge(zg, x), 0.5, 13.0)
    e_pi = sum(deprot(p, pi) for p, _ in groups)
    a.plot([e_pi], [pi], "D", ms=5, mfc=bio.P.surface(), mec=col, mew=1.3)
    ny = {"Gly": 12.4, "Glu": 11.2, "His": 12.6}[name]
    nx = {"Gly": 2.05, "Glu": 3.05, "His": 3.05}[name]
    a.text(nx, ny, name, color=col, fontsize=bio.core.FONT["small"], ha="left")
    if name == "Gly":
        a.text(e_pi - 0.08, pi, f"pI {pi:.2f}", color=col, fontsize=F, ha="right", va="center")
    else:
        a.text(e_pi + 0.08, pi - 0.55, f"pI {pi:.2f}", color=col, fontsize=F)
a.set_xlim(0, 3.4)
a.set_ylim(0, 13.5)
a.set_xticks([0, 0.5, 1, 1.5, 2, 2.5, 3])
C.style_axes(a, "OH$^-$ added / equivalents", "pH")
bio.panel(ax, "A", (0.1, 8.4))

b = C.axes_at(ax, (11.4, 1.5, 8.0, 6.4))
pep = {  # typical pKa values in peptides: N-terminus 8.0, C-terminus 3.1, Asp 3.9, Glu 4.1, His 6.0,
    # Cys 8.3, Tyr 10.1, Lys 10.5, Arg 12.5
    "Ala-Glu-Gly-Lys": [(8.0, 1, 1), (3.1, 0, 1), (4.1, 0, 1), (10.5, 1, 1)],
    "glucagon": [(8.0, 1, 1), (3.1, 0, 1), (3.9, 0, 3), (6.0, 1, 1), (10.1, 0, 2), (10.5, 1, 1), (12.5, 1, 2)],
}
for (name, groups), tok in zip(pep.items(), ["protein", "drug"]):
    z = charge(groups, pH)
    col = C.line(tok)
    b.plot(pH, z, color=col, lw=2.0)
    pi = brentq(lambda x: charge(groups, x), 1.0, 13.0)
    b.plot([pi], [0], "D", ms=5, mfc=bio.P.surface(), mec=col, mew=1.3)
    b.text(pi + 0.15, 0.25 if name == "glucagon" else -0.55, f"pI {pi:.1f}", color=col, fontsize=F)
b.axhline(0, color=bio.P.muted(), lw=0.8)
b.axvline(7.4, color=bio.P.muted(), lw=0.7, ls=(0, (3, 3)))
b.text(8.2, 1.4, "glucagon (29 residues)", color=C.line("drug"), fontsize=F)
b.text(0.9, 2.35, "Ala-Glu-Gly-Lys", color=C.line("protein"), fontsize=F)
b.set_xlim(0.5, 13.0)
b.set_ylim(-6.5, 5.5)
C.style_axes(b, "pH", "net charge")
bio.panel(ax, "B", (9.9, 8.4))
