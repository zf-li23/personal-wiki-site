"""The human globin gene clusters (schematic, not to scale): the alpha-like cluster on 16p13.3 and the
beta-like cluster on 11p15.4, genes in their 5'-to-3' order, colored by the developmental stage at which
each is expressed; psi marks pseudogenes. Both clusters are controlled by an upstream regulatory region
(MCS-R2 for alpha, the locus control region LCR for beta). Below: hemoglobin tetramers of each stage."""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 7.2)
stage = {"emb": ("receptor", "embryonic"), "fet": ("antibody", "fetal"), "adu": ("dna", "adult"), "psi": ("neutral", "pseudogene"),
         "min": ("enzyme", "minor / unclear")}
alpha = [("ζ", "emb"), ("ψζ", "psi"), ("μ", "psi"), ("ψα2", "psi"), ("α2", "adu"), ("α1", "adu"), ("θ", "min")]
beta = [("ε", "emb"), ("Gγ", "fet"), ("Aγ", "fet"), ("ψβ", "psi"), ("δ", "min"), ("β", "adu")]
for y, name, reg, genes in ((5.6, "α-globin cluster, chromosome 16", "MCS-R2", alpha), (3.2, "β-globin cluster, chromosome 11", "LCR", beta)):
    bio.label(ax, (0.5, y + 0.9), name, size="small", ha="left")
    ax.plot([0.8, 22.5], [y, y], color=P.muted(), lw=1.2, zorder=2)
    bio.box(ax, (2.0, y), 1.6, 0.6, token="highlight", text=reg, size="tiny")
    for i, (g, st) in enumerate(genes):
        x = 4.6 + i * 2.5
        bio.box(ax, (x, y), 1.5, 0.62, token=stage[st][0], text=g, size="small")
    bio.arrow(ax, (4.0, y - 0.65), (6.0, y - 0.65), kind="process", head=0.14, lw=0.9)
    bio.label(ax, (6.2, y - 0.65), "5′ → 3′ = order of expression", size="tiny", ha="left", color=P.muted())
x = 1.0
for st in ("emb", "fet", "adu", "min", "psi"):
    bio.box(ax, (x + 0.35, 1.3), 0.5, 0.4, token=stage[st][0])
    bio.label(ax, (x + 0.8, 1.3), stage[st][1], size="tiny", ha="left")
    x += 3.6
bio.label(ax, (1.0, 0.45), "Hemoglobins: embryonic ζ2ε2, α2ε2, ζ2γ2; fetal HbF α2γ2; adult HbA α2β2 (97 %), HbA2 α2δ2 (2.5 %)",
          size="tiny", ha="left", color=P.muted())
