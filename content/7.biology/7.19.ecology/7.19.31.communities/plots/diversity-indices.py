"""Diversity indices and Hill numbers for small example communities.

Communities C and D each have 24 individuals of 3 species: C = (8, 8, 8), D = (22, 1, 1).
A: abundances, with richness S, Shannon H' (natural log), Simpson D (finite-sample form
sum n_i (n_i - 1) / (N (N - 1))), Gini-Simpson 1 - D and Pielou J' = H' / ln S.
B: Hill diversity profiles qD = (sum p_i^q)^(1/(1-q)) for q from 0 to 4 (q = 1: exp H') for C, D and
a simulated community E of 20 species with geometric abundances (each species is the
previous one times 0.7): profiles that cross no other are unambiguously ranked.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
comms = {"C": np.array([8, 8, 8]), "D": np.array([22, 1, 1])}


def indices(n):
    N = n.sum()
    p = n / N
    H = -(p * np.log(p)).sum()
    Dfin = (n * (n - 1)).sum() / (N * (N - 1))
    return len(n), H, Dfin, 1 - Dfin, H / np.log(len(n))


def hill(p, q):
    p = p[p > 0]
    if abs(q - 1) < 1e-9:
        return np.exp(-(p * np.log(p)).sum())
    return (p**q).sum() ** (1 / (1 - q))


fig, ax = bio.canvas(30.0, 11.0)
pa = C.axes_at(ax, (2.0, 2.0, 10.0, 7.0))
toks = ["plant", "highlight", "dna"]
w = 0.25
for j, (name, n) in enumerate(comms.items()):
    for i in range(3):
        pa.bar(j + (i - 1) * w, n[i], width=w * 0.9, color=P.fill(toks[i]), edgecolor=P.edge(toks[i]), lw=0.8,
               label=f"species {'abc'[i]}" if j == 0 else None)
    S, H, D, GS, J = indices(n)
    pa.text(j, 24.5, f"S = {S}\nH' = {H:.3f}\nD = {D:.3f}\n1 - D = {GS:.3f}\nJ' = {J:.3f}", ha="center", va="bottom",
            fontsize=FS["tiny"], color=P.ink())
pa.set_xticks([0, 1], ["community C", "community D"])
pa.set_ylim(0, 36)
pa.set_xlim(-0.6, 1.6)
C.style_axes(pa, None, "individuals")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right", bbox_to_anchor=(1.0, 0.62))
bio.panel(ax, "A", (0.3, 10.7))
bio.label(ax, (2.0, 10.0), "Two communities with equal richness", size="small", bold=True, ha="left")

qs = np.linspace(0, 4, 200)
pb = C.axes_at(ax, (17.5, 2.0, 11.0, 7.0))
E = 0.7 ** np.arange(20)
for lab, p, tok in (("C", comms["C"] / 24, "plant"), ("D", comms["D"] / 24, "negative"), ("E (20 species)", E / E.sum(), "dna")):
    pb.plot(qs, [hill(p, q) for q in qs], color=Q.line_color(tok), lw=1.8, label=lab)
for q in (0, 1, 2):
    pb.axvline(q, color=P.muted(), lw=0.6, ls=":")
pb.text(0.05, 18.5, "q = 0: richness", fontsize=FS["tiny"], color=P.ink())
pb.text(1.05, 12.0, "q = 1: exp H'", fontsize=FS["tiny"], color=P.ink())
pb.text(2.05, 8.0, "q = 2: 1 / sum p^2", fontsize=FS["tiny"], color=P.ink())
pb.set_yscale("log")
pb.set_ylim(1, 25)
pb.set_yticks([1, 2, 3, 5, 10, 20], ["1", "2", "3", "5", "10", "20"])
pb.set_xlim(0, 4)
C.style_axes(pb, "order q", "effective number of species qD")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (15.8, 10.7))
bio.label(ax, (17.5, 10.0), "Hill diversity profiles", size="small", bold=True, ha="left")
