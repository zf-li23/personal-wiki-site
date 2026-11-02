"""Metabolic control analysis of a branched pathway. A: the pathway: enzyme 1 converts the fixed
source X0 into S1 and is inhibited by its product; S1 is either converted by enzyme 2 into S2 and
by enzyme 3 into the product P, or diverted by enzyme 4 into the branch product Q (irreversible
Michaelis-Menten rate laws; V1 = 10, K1 = 0.5, Ki = 1, V2 = 4, K2 = 1, V3 = 10, K3 = 1, V4 = 6,
K4 = 2, X0 = 1). B: the flux control coefficients C^J_i computed from the elasticities with the
matrix formula of 14.5.2; every row sums to one; enzyme 4 has negative control over the flux to P
and enzyme 2 over the flux to Q; enzyme 3 has none, because S2 acts on no other step. C: the steady
fluxes J_P and J_Q, relative to the reference state, when the amount of enzyme 4 is varied from
0.25 to 4 times its reference value (logarithmic axes); the slopes at the reference point (circle)
are the control coefficients of enzyme 4."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import wikibio as bio
from wikibio import charts

P = bio.P
X0 = 1.0
V1, K1, Ki, V2, K2, V3, K3, V4, K4 = 10.0, 0.5, 1.0, 4.0, 1.0, 10.0, 1.0, 6.0, 2.0
N = np.array([[1, -1, 0, -1], [0, 1, -1, 0]], float)


def rates(S, e):
    S1, S2 = S
    return np.array([e[0] * V1 * X0 / (K1 + X0) / (1 + S1 / Ki), e[1] * V2 * S1 / (K2 + S1),
                     e[2] * V3 * S2 / (K3 + S2), e[3] * V4 * S1 / (K4 + S1)])


def steady(e):
    return fsolve(lambda S: N @ rates(S, e), [1.0, 1.0], xtol=1e-12)


e0 = np.ones(4)
S = steady(e0)
v = rates(S, e0)
h = 1e-6
eps = np.zeros((4, 2))
for j in range(2):
    up, dn = S.copy(), S.copy()
    up[j] *= 1 + h
    dn[j] *= 1 - h
    eps[:, j] = (np.log(rates(up, e0)) - np.log(rates(dn, e0))) / (2 * h)
M = N @ np.diag(v) @ eps
CS = -np.linalg.solve(M, N @ np.diag(v))
CJ = np.eye(4) + eps @ CS

fig = plt.figure(figsize=(11, 3.6))
axA = fig.add_axes([0.01, 0.08, 0.30, 0.8])
axB = fig.add_axes([0.40, 0.17, 0.24, 0.66])
axC = fig.add_axes([0.75, 0.17, 0.23, 0.66])
axA.set_xlim(0, 10)
axA.set_ylim(0, 6)
axA.axis("off")
nodes = {"X0": (1, 3), "S1": (4, 3), "S2": (7, 4.6), "P": (9.4, 4.6), "Q": (7, 1.2)}
for k, (x, y) in nodes.items():
    axA.text(x, y, k, ha="center", va="center", fontsize=10, color=P.on_fill(),
             bbox=dict(boxstyle="round,pad=0.3", fc=P.fill("metabolite"), ec=P.edge("metabolite")))
for a, b, lab in [("X0", "S1", "1"), ("S1", "S2", "2"), ("S2", "P", "3"), ("S1", "Q", "4")]:
    (x1, y1), (x2, y2) = nodes[a], nodes[b]
    axA.annotate("", (x2 - 0.55 * np.sign(x2 - x1) * (abs(x2 - x1) > 0.1), y2 + (0.45 if y2 < y1 else -0.35) * (abs(y2 - y1) > 0.1)),
                 (x1 + 0.6 * (x2 > x1), y1), arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=1.3))
    axA.text((x1 + x2) / 2 + (0.1 if lab != "1" else 0), (y1 + y2) / 2 + (0.35 if lab != "1" else -0.45), f"E{lab}", fontsize=8, color=P.ink(), ha="center")
bio.arrow(axA, (4.0, 3.5), (2.5, 3.2), kind="inhibition", bend=-0.8, color=charts.line("negative"), lw=1.2)
axA.text(3.2, 4.45, "product inhibition", fontsize=7, color=charts.line("negative"), ha="center")
charts.title(axA, "A  Branched pathway")

rows = [0, 2, 3]
mat = CJ[rows]
axB.imshow(mat, cmap="coolwarm", vmin=-1, vmax=1, aspect="auto")
for i in range(3):
    for j in range(4):
        axB.text(j, i, f"{mat[i, j]:.2f}", ha="center", va="center", fontsize=8, color=P.on_fill())
axB.set_xticks(range(4))
axB.set_xticklabels([f"E{i}" for i in range(1, 5)])
axB.set_yticks(range(3))
axB.set_yticklabels(["J1 (supply)", "J_P (via E2, E3)", "J_Q (via E4)"])
charts.style_axes(axB, "enzyme i", None, box=True)
charts.title(axB, "B  Flux control coefficients")

f4 = np.logspace(np.log10(0.25), np.log10(4), 41)
JP, JQ = [], []
for f in f4:
    e = e0.copy()
    e[3] = f
    r = rates(steady(e), e)
    JP.append(r[2] / v[2])
    JQ.append(r[3] / v[3])
axC.loglog(f4, JP, color=charts.line("positive"), lw=1.8, label="J_P")
axC.loglog(f4, JQ, color=charts.line("negative"), lw=1.8, label="J_Q")
axC.plot([1, 1], [1, 1], "o", color=P.ink(), mfc="none")
axC.set_xticks([0.25, 0.5, 1, 2, 4])
axC.set_xticklabels(["0.25", "0.5", "1", "2", "4"])
axC.set_yticks([0.25, 0.5, 1, 2])
axC.set_yticklabels(["0.25", "0.5", "1", "2"])
axC.minorticks_off()
axC.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(axC, "relative amount of E4", "relative flux")
charts.title(axC, "C  Varying enzyme 4")
