"""The challenge hypothesis (Wingfield et al. 1990), schematic. Plasma testosterone over the year in a seasonally
breeding male bird. Level A: nonbreeding baseline; level B: breeding baseline, sufficient for spermatogenesis,
song and secondary sexual characters; level C: physiological maximum, reached only during social challenges
(territory establishment, intrusions, mate guarding while females are fertile). The hypothesis predicts that
monogamous males that feed their young keep testosterone near B except when challenged, so their response to a
challenge (C - B) is large, whereas polygynous males without paternal care stay near C through the breeding
season and respond little to challenges. Spikes: simulated territorial intrusions."""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(24, 10.4)
m = np.linspace(0, 12, 1200)


def bump(c, w):
    return np.exp(-0.5 * ((m - c) / w) ** 2)


A, B, C = 0.15, 0.45, 1.0
season = np.clip((np.tanh((m - 3.2) * 3) + 1) / 2 * (np.tanh((7.6 - m) * 3) + 1) / 2, 0, 1)
mono = A + (B - A) * season + (C - B) * (0.9 * bump(3.6, 0.18) + 0.75 * bump(4.6, 0.12) + 0.6 * bump(6.2, 0.1))
poly = A + (C - A) * 0.9 * season + 0.08 * bump(4.6, 0.12)
for k, (y, tok, name, title) in enumerate([(mono, "dna", "mono", "Monogamous, biparental care"),
                                           (poly, "rna", "poly", "Polygynous, no paternal care")]):
    x0 = 1.8 + k * 11.4
    bio.panel(ax, "AB"[k], (x0 - 1.4, 10.1))
    bio.label(ax, (x0 + 4.5, 9.8), title, size="small", bold=True)
    p = quant.Plot(ax, (x0, 1.8, 9.2, 7.2), xlim=(0, 12), ylim=(0, 1.15), xlabel="Month",
                   ylabel="Plasma testosterone" if k == 0 else None,
                   xticks=[(0, "Jan"), (2, "Mar"), (4, "May"), (6, "Jul"), (8, "Sep"), (10, "Nov"), (12, "")], yticks=None)
    p.span(3.2, 7.6, "highlight", text="breeding season", text_y=p.Y(1.1))
    for lev, name_ in [(A, "A"), (B, "B"), (C, "C")]:
        p.hline(lev, text=name_, side="right")
    p.line(m, y, tok, lw=1.8)
    if k == 0:
        p.text(3.6, 1.04, "territory", size="tiny")
        p.text(4.75, 0.9, "female fertile", size="tiny", ha="left")
        p.text(6.3, 0.75, "intrusion", size="tiny", ha="left")
ax.set_ylim(0.3, 10.4)
