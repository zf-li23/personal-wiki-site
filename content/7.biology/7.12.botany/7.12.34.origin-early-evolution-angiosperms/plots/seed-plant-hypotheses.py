# Two hypotheses of seed-plant relationships. Left: the anthophyte hypothesis of morphological cladistics
# (simplified from Doyle & Donoghue 1986): Bennettitales, Pentoxylon and Gnetales form a clade with the
# angiosperms, united by flower-like reproductive structures; extinct groups are marked with a dagger.
# Right: the result of molecular phylogenetics: extant gymnosperms are monophyletic, Gnetales are close
# to Pinaceae (gnepine), and angiosperms are sister to all extant gymnosperms; possible extinct stem
# relatives of the angiosperms (Caytoniales, glossopterids) are of uncertain position (dashed).
import wikibio as bio
from wikibio import phylo

P = bio.P
LEFT = ("((Conifers,Ginkgo),(Cycads,('Glossopterids †',('Caytonia †',(('Bennettitales †','Pentoxylon †'),"
        "(Gnetales,Angiosperms))Anthophytes))));")
RIGHT = "(Angiosperms,((Cycads,Ginkgo),((Pinaceae,Gnetales),Cupressophytes))Gymnosperms);"
ITAL = {"Caytonia †", "Pentoxylon †", "Ginkgo"}

fig, ax = bio.canvas(30, 12.6)
bio.panel(ax, "A", (0.3, 12.3))
bio.label(ax, (7.2, 12.0), "Anthophyte hypothesis (morphology, 1980s)", size="title")
tl = phylo.tree(ax, LEFT, origin=(0.8, 1.4), width=8.6, height=9.4, label_size="small",
                italic=lambda n: n in ITAL,
                clades=[dict(node="Anthophytes", token="petal", style=("bar", "branch"), label="Anthophytes"),
                        dict(tips=["Angiosperms"], token="plant", style="branch")],
                marks=[dict(node="Anthophytes", kind="trait", text="Flower-like structures", text_size="tiny")])
bio.panel(ax, "B", (15.6, 12.3))
bio.label(ax, (22.4, 12.0), "Molecular phylogenies (since 1999)", size="title")
tr = phylo.tree(ax, RIGHT, origin=(16.2, 1.4), width=8.6, height=9.4, label_size="small",
                italic=lambda n: n == "Ginkgo",
                clades=[dict(node="Gymnosperms", token="neutral", style=("bar", "branch"), label="Extant gymnosperms"),
                        dict(tips=["Angiosperms"], token="plant", style="branch"),
                        dict(tips=["Gnetales"], token="petal", style="branch")])
a = tr.node("Angiosperms")
px, py = a.parent.xy
ax_, ay = a.xy
mx = px + (ax_ - px) * 0.45
ax.plot([mx, mx], [ay, ay - 0.9], color=P.muted(), lw=1.2, ls=(0, (3, 2.5)), zorder=7)
bio.label(ax, (mx + 0.2, ay - 0.8), "Extinct stem relatives? (Caytoniales, glossopterids)", size="tiny", ha="left",
          color=P.muted())
