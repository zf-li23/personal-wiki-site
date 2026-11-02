# Target sites of the microRNA let-7 in the 3' untranslated region of human HMGA2 (2999 nt, the UTR of the
# Ensembl canonical transcript ENST00000403681, in hmga2-utr3.txt). Sites are found by exact matching to
# the seed of let-7a-5p (UGAGGUAGUAGGUUGUAUAGUU): the 6mer matches nucleotides 2-7, the 7mer-m8 adds a
# match to nucleotide 8, the 7mer-A1 adds an A opposite nucleotide 1, and the 8mer has both. Each site is
# counted once, under its strongest type. A: the pairing of the 8mer site with the microRNA. B: the
# positions of the sites along the UTR, by type. C: the AU content of the 30 nt on each side of every
# site, a determinant of site efficacy (AU-rich context favors repression); the dashed line is the AU
# content of the whole UTR.
import re

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FT = bio.core.FONT
utr = open("hmga2-utr3.txt").read().strip()
mir = "UGAGGUAGUAGGUUGUAUAGUU"
comp = {"A": "U", "C": "G", "G": "C", "U": "A"}
seed6 = "".join(comp[b] for b in mir[1:7])[::-1]            # match to nucleotides 2-7
m8 = "".join(comp[b] for b in mir[1:8])[::-1]               # match to nucleotides 2-8
sites = []
for p in [m.start() for m in re.finditer("(?=" + m8 + ")", utr)]:
    sites.append((p, "8mer" if utr[p + 7] == "A" else "7mer-m8", 7 + (utr[p + 7] == "A")))
taken = {p for p, _, _ in sites} | {p + 1 for p, _, _ in sites}
for p in [m.start() for m in re.finditer("(?=" + seed6 + ")", utr)]:
    if p in taken or p - 1 in {q for q, _, _ in sites}:
        continue
    if utr[p + 6] == "A":
        sites.append((p, "7mer-A1", 7))
    else:
        sites.append((p, "6mer", 6))
sites.sort()
toks = {"8mer": "positive", "7mer-m8": "dna", "7mer-A1": "rna", "6mer": "neutral"}
au_all = np.mean([ch in "AU" for ch in utr])


def context_au(p, L):
    left = utr[max(0, p - 30):p]
    right = utr[p + L:p + L + 30]
    s = left + right
    return np.mean([ch in "AU" for ch in s])


fig, ax = bio.canvas(26.0, 13.0)
# A: duplex of the 8mer site with the microRNA
p8, _, L8 = next(s for s in sites if s[1] == "8mer")
target = utr[p8 - 11:p8 + 11]                              # the site occupies display columns 11-18
cw, x0, y = 0.70, 2.6, 11.6
for k, ch in enumerate(target):
    bio.label(ax, (x0 + k * cw, y), ch, size="small",
              color=C.line("positive") if 11 <= k <= 18 else P.ink())
for k in range(19):                                        # microRNA nucleotides 1-19, 5' end on the right
    bio.label(ax, (x0 + (18 - k) * cw, y - 1.1), mir[k], size="small")
for k in range(2, 9):                                      # pairs: nucleotide k with column 19 - k
    xx = x0 + (19 - k) * cw
    ax.plot([xx, xx], [y - 0.30, y - 0.80], color=C.line("positive"), lw=1.1)
bio.label(ax, (x0 - 1.0, y), "5'", size="tiny", color=P.muted())
bio.label(ax, (x0 + 21 * cw + 1.0, y), "3'", size="tiny", color=P.muted())
bio.label(ax, (x0 - 1.4, y - 1.1), "3' (nt 19)", size="tiny", color=P.muted())
bio.label(ax, (x0 + 18 * cw + 1.0, y - 1.1), "5'", size="tiny", color=P.muted())
bio.label(ax, (x0 + 4 * cw, y + 0.75), "HMGA2 3' UTR", size="small")
bio.label(ax, (x0 + 4 * cw, y - 1.9), "let-7a-5p", size="small")
bio.label(ax, (x0 + 18 * cw, y - 1.9), "nt 1, opposite the A", size="tiny", color=C.line("positive"))
bio.label(ax, (x0 + 14.5 * cw, y + 0.75), "8mer site", size="tiny", color=C.line("positive"))
bio.panel(ax, "A", (0.3, 12.6))
# B: the sites along the UTR
b = C.axes_at(ax, (2.6, 6.2, 21.5, 2.3))
b.plot([0, len(utr)], [0, 0], color=P.muted(), lw=2.0, solid_capstyle="butt")
for p, kind, L in sites:
    b.plot([p, p], [0, 1], color=C.line(toks[kind]), lw=1.4)
    b.scatter([p], [1], s=16, color=C.line(toks[kind]))
for k, (kind, tok) in enumerate(toks.items()):
    n_ = sum(1 for s in sites if s[1] == kind)
    b.text(60 + 700 * k, 1.75, f"{kind} ({n_})", color=C.line(tok), fontsize=FT["tiny"])
b.set_ylim(-0.6, 2.4)
b.set_yticks([])
C.style_axes(b, "position in the 3' UTR (nt)", None)
b.spines["left"].set_visible(False)
bio.panel(ax, "B", (0.3, 8.8))
# C: AU content of the flanks
c = C.axes_at(ax, (2.6, 1.2, 21.5, 3.4))
xs = np.arange(len(sites))
c.bar(xs, [context_au(p, L) for p, _, L in sites], color=[C.line(toks[k]) for _, k, _ in sites], width=0.6)
c.axhline(au_all, color=P.muted(), ls=(0, (4, 2)), lw=1.0)
c.text(len(sites) - 0.4, au_all + 0.02, "whole UTR", ha="right", fontsize=FT["tiny"], color=P.muted())
c.set_xticks(xs)
c.set_xticklabels([f"{p + 1}\n{k}" for p, k, _ in sites], fontsize=FT["tiny"] * 0.95)
c.set_ylim(0, 0.9)
C.style_axes(c, None, "AU content of the 30 nt flanks")
bio.panel(ax, "C", (0.3, 5.0))
