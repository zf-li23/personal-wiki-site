# Schematic model of the RNA "walking" cross-linking experiment (Nudler et al. 1997) that measured the length
# of the RNA-DNA hybrid. A reactive UMP analog U* placed in the RNA is cross-linked to the template DNA only
# while it is base paired in the hybrid. With the end of the hybrid at about 8-9 nt from the RNA 3' end,
# smoothed by fraying of the terminal base pair (logistic step centred at 8.5 nt, width 0.6 nt), the DNA
# signal is high up to 8 nt and falls to background beyond 10 nt; cross-linking to protein (beta and beta')
# continues as the RNA runs through the exit channel (slow decline over about 20 nt).
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(14.0, 7.4)
a = C.axes_at(ax, (1.8, 1.3, 11.4, 5.4))
d = np.arange(1, 25)
paired = 1 / (1 + np.exp((d - 8.5) / 0.6))
dna = 0.06 + 0.94 * paired
prot = 0.25 + 0.65 * np.exp(-np.clip(d - 6, 0, None) / 14)
a.plot(d, dna, "o-", color=C.line("dna"), lw=1.6, ms=4, label="cross-link to template DNA")
a.plot(d, prot, "s-", color=C.line("enzyme"), lw=1.6, ms=4, label="cross-link to polymerase (β, β′)")
a.axvspan(0.5, 8.5, color=P.fill("dna"), alpha=0.18, lw=0)
a.text(4.5, 1.06, "RNA–DNA hybrid (8–9 bp)", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.text(16.0, 1.06, "single-stranded RNA in the exit channel", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.set_xlim(0.5, 24.5)
a.set_ylim(0, 1.15)
a.set_xticks([1, 4, 8, 12, 16, 20, 24])
C.style_axes(a, "distance of U• from the RNA 3′ end / nt", "relative cross-linking")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="lower right", bbox_to_anchor=(1.0, 0.12))
