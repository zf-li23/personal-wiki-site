# The Shea-Ackers model of the lambda right operator O_R.
# Eight states (each of OR1, OR2, OR3 empty or bound by a CI dimer). Weight of state s:
#   w_s = D^n_s exp(-dG_s / RT),
# dG_s = sum of intrinsic free energies of occupied sites (-12.5, -10.5, -9.5 kcal/mol for OR1, OR2, OR3)
# + a cooperative term -2.7 kcal/mol for one adjacent occupied pair (OR1-OR2, or OR2-OR3 when OR1 is empty).
# Free dimer D follows from total CI monomer M by dimerization (dG = -11.1 kcal/mol, K_dim = exp(dG/RT) M):
#   M = m + 2 m^2 / K_dim, D = m^2 / K_dim. RT = 0.593 kcal/mol (25 C). Depletion by the operator is neglected.
# PR is active when OR1 and OR2 are empty; PRM has basal activity 1 with OR2 and OR3 empty, 10 with OR2
# occupied and OR3 empty, and 0 with OR3 occupied.
import itertools

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
RT = 0.593
G = np.array([-12.5, -10.5, -9.5])
coop = -2.7
Kdim = np.exp(-11.1 / RT)  # M

M = np.logspace(-10, -5.5, 400)  # total CI monomer, M
m = (-1 + np.sqrt(1 + 8 * M / Kdim)) / (4 / Kdim)
D = m ** 2 / Kdim

states = list(itertools.product([0, 1], repeat=3))
W = []
for s in states:
    g = float(np.dot(s, G))
    if s[0] and s[1]:
        g += coop
    elif s[1] and s[2]:
        g += coop
    W.append(D ** sum(s) * np.exp(-g / RT))
W = np.array(W)
Z = W.sum(axis=0)
prob = W / Z
occ = [sum(prob[k] for k, s in enumerate(states) if s[i]) for i in range(3)]
pr = sum(prob[k] for k, s in enumerate(states) if not s[0] and not s[1])
prm = sum(prob[k] * (0 if s[2] else (10 if s[1] else 1)) for k, s in enumerate(states))

fig, ax = bio.canvas(20.0, 7.6)
fs = bio.core.FONT["tiny"]
Mn = M * 1e9
a = C.axes_at(ax, (2.0, 1.4, 6.8, 5.4))
for i, tok in enumerate(["negative", "enzyme", "dna"]):
    a.semilogx(Mn, occ[i], color=C.line(tok), lw=1.8, label=f"OR{i + 1}")
a.set_xlim(Mn[0], Mn[-1])
a.set_ylim(0, 1.03)
C.style_axes(a, "total CI / nM (monomers)", "fractional occupancy")
a.legend(fontsize=fs, frameon=False, labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.1, 7.45))

b = C.axes_at(ax, (12.4, 1.4, 6.8, 5.4))
b.semilogx(Mn, pr, color=C.line("negative"), lw=1.8, label="PR (cro)")
b.semilogx(Mn, prm / 10, color=C.line("positive"), lw=1.8, label="PRM (cI)")
b.set_xlim(Mn[0], Mn[-1])
b.set_ylim(0, 1.12)
C.style_axes(b, "total CI / nM (monomers)", "relative promoter activity")
b.legend(fontsize=fs, frameon=False, labelcolor=P.ink(), loc="center left")
bio.panel(ax, "B", (10.6, 7.45))
