"""Scaling of resting metabolic rate with body mass.

A: resting O2 consumption of eleven mammals (shrew to elephant; standard comparative-physiology table) converted to
watts with 20.1 J per mL O2, the ordinary least-squares fit of log B on log M, and the literature allometric lines:
Kleiber (1932) mammals B = 3.39 M^0.75 W (70 kcal/d), Lasiewski & Dawson (1967) passerine birds 6.25 M^0.724 W and
non-passerine birds 3.79 M^0.723 W, and ectotherms at 20 C 0.14 M^0.75 W (Hemmingsen 1960). M in kg.
B: Hemmingsen's three parallel lines (unicells 0.018, ectotherms at 20 C 0.14, endotherms at 39 C 4.1 W kg^-0.75)
over 20 orders of magnitude of mass; dotted: the ectotherm line corrected to 39 C with Q10 = 2.5.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
mass = np.array([0.0048, 0.009, 0.025, 0.096, 0.29, 2.5, 11.7, 42.7, 70, 650, 3833])
vo2 = np.array([0.0355, 0.0225, 0.041, 0.09, 0.25, 1.7, 3.87, 9.59, 14.76, 71.1, 268])  # L O2 per hour
names = ["shrew", "harvest mouse", "mouse", "ground squirrel", "rat", "cat", "dog", "sheep", "human", "horse",
         "elephant"]
B = vo2 * 20.1 / 3.6  # W

x, y = np.log10(mass), np.log10(B)
slope, icpt = np.polyfit(x, y, 1)
res = y - (icpt + slope * x)
se = np.sqrt(res @ res / (len(x) - 2) / ((x - x.mean()) @ (x - x.mean())))

fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.5, 4.8))
mm = np.logspace(-3, 4, 50)
ax.plot(mm, 3.39 * mm ** 0.75, color=P.edge("blood"), lw=2, label="mammals (Kleiber): 3.39 $M^{0.75}$")
ax.plot(mm, 6.25 * mm ** 0.724, color=P.edge("rna"), lw=1.6, ls="--", label="passerine birds: 6.25 $M^{0.724}$")
ax.plot(mm, 3.79 * mm ** 0.723, color=P.edge("rna"), lw=1.6, ls=":", label="non-passerine birds: 3.79 $M^{0.723}$")
ax.plot(mm, 0.14 * mm ** 0.75, color=P.edge("plant"), lw=2, label="ectotherms, 20 $^\\circ$C: 0.14 $M^{0.75}$")
ax.scatter(mass, B, s=28, color=P.fill("dna"), edgecolor=P.edge("dna"), zorder=5,
           label=f"mammal data, OLS slope {slope:.2f} $\\pm$ {se:.2f}")
ax.annotate("shrew", (mass[0], B[0]), xytext=(-30, 6), textcoords="offset points", fontsize=7.5, color=P.muted())
for m_, b_, n_ in zip(mass, B, names):
    if n_ in ("mouse", "rat", "dog", "human", "elephant"):
        ax.annotate(n_, (m_, b_), xytext=(4, -10), textcoords="offset points", fontsize=7.5, color=P.muted())
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("Body mass $M$ / kg")
ax.set_ylabel("Resting metabolic rate $B$ / W")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.set_title("A  Mammals, birds and ectotherms", loc="left", fontsize=10)

for lo, hi, a0, c, lab in ((1e-15, 1e-6, 0.018, P.edge("dna"), "unicells"),
                          (1e-9, 3e2, 0.14, P.edge("plant"), "ectotherms (20 $^\\circ$C)"),
                          (2e-3, 1e4, 4.1, P.edge("blood"), "endotherms (39 $^\\circ$C)")):
    m = np.logspace(np.log10(lo), np.log10(hi), 50)
    bx.plot(m, a0 * m ** 0.75, color=c, lw=2.2, label=lab)
m = np.logspace(-9, np.log10(3e2), 50)
bx.plot(m, 0.14 * 2.5 ** 1.9 * m ** 0.75, color=P.edge("plant"), lw=1.4, ls=":",
        label="ectotherms corrected to 39 $^\\circ$C ($Q_{10}$ = 2.5)")
bx.set_xscale("log")
bx.set_yscale("log")
bx.set_xlabel("Body mass $M$ / kg")
bx.set_ylabel("Metabolic rate / W")
bx.legend(frameon=False, fontsize=7.5, loc="upper left")
bx.set_title("B  Hemmingsen: three parallel lines of slope 3/4", loc="left", fontsize=10)
fig.tight_layout()
