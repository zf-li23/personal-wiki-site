"""Gene trees, duplication and the molecular clock. A: a gene duplicated (square) in an ancestral
species into copies alpha and beta, and the species then split (circles) into species 1 and 2. Genes whose
last common ancestor is a speciation node are orthologs (alpha1 and alpha2; beta1 and beta2); genes whose last
common ancestor is a duplication node are paralogs (for example alpha1 and beta2). The gene tree groups the
genes by copy, not by species (after Futuyma and Kirkpatrick 2017, Fig. 2.14). B: reading a molecular clock
(Formula 2.6.1). If a calibration line, fitted to species pairs whose divergence time is known from fossils,
gives a difference D = 2rt, a pair with 45 differences diverged about 74 Myr ago (numbers of Futuyma and
Kirkpatrick 2017, Fig. 2.17)."""
import numpy as np
import wikibio as bio
from wikibio import phylo, charts

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(24, 9.0)
bio.panel(ax, "A", (0.2, 8.8))
NW = "((alpha_1,alpha_2)S_alpha,(beta_1,beta_2)S_beta)Dup;"
TXT = {"alpha 1": "α1 (species 1)", "alpha 2": "α2 (species 2)", "beta 1": "β1 (species 1)", "beta 2": "β2 (species 2)"}
t = phylo.tree(ax, NW, origin=(1.4, 1.4), width=6.0, height=5.6, direction="up", root_edge=0.6, tip_text=TXT,
               label_size="small",
               clades=[dict(node="S alpha", token="negative", style="branch"), dict(node="S beta", token="positive",
                                                                                    style="branch")],
               marks=[dict(node="Dup", kind="duplication", at=1.0, size=0.3),
                      dict(node="S alpha", kind="speciation", at=1.0, size=0.28),
                      dict(node="S beta", kind="speciation", at=1.0, size=0.28)])
for name, text in (("Dup", "duplication"), ("S alpha", "speciation"), ("S beta", "speciation")):
    x, y = t.node(name).xy
    bio.label(ax, (x + 0.25, y - 0.35), text, size="tiny", ha="left", va="top", color=P.muted())
bio.label(ax, (4.4, 0.55), "orthologs: α1–α2, β1–β2      paralogs: α1–β1, α1–β2, α2–β1, α2–β2", size="tiny",
          color=P.muted())

bio.panel(ax, "B", (12.0, 8.8))
pax = charts.axes_at(ax, (13.8, 1.6, 9.4, 6.4))
r = 45 / (2 * 74)
tt = np.linspace(0, 125, 50)
pax.plot(tt, 2 * r * tt, color=charts.line("dna"), lw=1.8, label="calibration $D = 2rt$")
pax.plot([0, 74], [45, 45], color=P.muted(), lw=1.0, ls=(0, (3, 2)))
pax.plot([74, 74], [45, 0], color=P.muted(), lw=1.0, ls=(0, (3, 2)))
pax.plot([74], [45], "o", color=P.edge("rna"), ms=6)
pax.text(76, 40, "45 differences\n→ about 74 Myr", fontsize=FT["tiny"], color=P.ink(), va="top")
pax.set_xlim(0, 125)
pax.set_ylim(0, 80)
charts.style_axes(pax, "time since divergence $t$ (Myr)", "differences $D$")
pax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
