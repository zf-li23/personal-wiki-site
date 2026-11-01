"""Fragment ions of the tryptic peptide HLVDEPQNLIK (monoisotopic M = 1304.709, [M+2H]2+ m/z 653.36).
A: the b ladder (N-terminal fragments, read left to right) and the y ladder (C-terminal fragments,
read right to left) with the singly charged m/z of every fragment; each peptide bond gives one
b/y pair, and b_i + y_(n-i) = M + 2 m(H+). B: a simulated MS2 spectrum: 14 of the 20 b and y ions
(y ions stronger, as is usual for tryptic peptides with a C-terminal Lys or Arg) among 46 noise
peaks; matched peaks are coloured. The mass differences between neighbouring y ions are residue
masses, which is how the sequence is read from the spectrum."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
RES = dict(G=57.02146, A=71.03711, S=87.03203, P=97.05276, V=99.06841, T=101.04768,
           L=113.08406, I=113.08406, N=114.04293, D=115.02694, Q=128.05858, K=128.09496,
           E=129.04259, M=131.04049, H=137.05891, F=147.06841, R=156.10111, Y=163.06333)
H2O, PROTON = 18.010565, 1.007276
pep = "HLVDEPQNLIK"
n = len(pep)
b = np.cumsum([RES[a] for a in pep])[:-1] + PROTON
y = np.cumsum([RES[a] for a in pep[::-1]])[:-1] + H2O + PROTON

cb, cy, cn = charts.line("dna"), charts.line("negative"), P.muted()
fig = plt.figure(figsize=(9.6, 6.2))
a = fig.add_axes([0.03, 0.62, 0.94, 0.33])
a.set_xlim(-0.6, n - 0.4)
a.set_ylim(-1.6, 1.7)
a.axis("off")
for i, aa in enumerate(pep):
    a.text(i, 0, aa, ha="center", va="center", fontsize=15, color=P.ink(), family="monospace", weight="bold")
for i in range(n - 1):
    x = i + 0.5
    a.plot([x, x], [-0.35, 0.35], color=P.muted(), lw=0.8)
    a.plot([x, x - 0.22], [0.35, 0.35], color=cb, lw=1.4)          # b: charge kept on the N-terminal side
    a.plot([x, x + 0.22], [-0.35, -0.35], color=cy, lw=1.4)        # y: C-terminal side
    a.text(x, 0.62, f"b{i + 1}", ha="center", fontsize=8, color=cb)
    a.text(x, 1.05, f"{b[i]:.2f}", ha="center", fontsize=7, color=cb, rotation=60)
    a.text(x, -0.75, f"y{n - 1 - i}", ha="center", fontsize=8, color=cy)
    a.text(x, -1.45, f"{y[n - 2 - i]:.2f}", ha="center", fontsize=7, color=cy, rotation=60)
a.text(-0.6, 1.55, "A  b and y ladders (singly charged m/z)", fontsize=9, color=P.ink(), weight="bold")

# simulated spectrum
obs = set(rng.choice(20, 14, replace=False))
ions = [(m, f"b{i + 1}", cb, 0.25 + 0.35 * rng.random()) for i, m in enumerate(b)]
ions += [(m, f"y{i + 1}", cy, 0.45 + 0.55 * rng.random()) for i, m in enumerate(y)]
s = fig.add_axes([0.08, 0.1, 0.9, 0.42])
noise = rng.uniform(150, 1300, 46)
s.vlines(noise, 0, 0.05 + 0.25 * rng.random(46) ** 2, color=cn, lw=0.8)
for k, (m, lab, c, h) in enumerate(ions):
    if k in obs:
        s.vlines(m, 0, h, color=c, lw=1.6)
        s.text(m, h + 0.02, lab, ha="center", fontsize=7, color=c)
yi = [y[j] for j in range(len(y)) if (j + len(b)) in obs]
s.set_xlim(120, 1320)
s.set_ylim(0, 1.15)
charts.style_axes(s, "m/z", "relative intensity")
charts.title(s, "B  Simulated MS2 spectrum of [M+2H]2+ = 653.36: 14 of 20 fragment ions matched")
