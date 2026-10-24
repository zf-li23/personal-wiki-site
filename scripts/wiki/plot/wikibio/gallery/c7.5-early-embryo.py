# Human preimplantation development (days after fertilisation, approximate): the zygote with male and female
# pronuclei and two polar bodies, cleavage divisions without growth (2-, 4-, 8-cell), compaction into the
# morula, and cavitation into the blastocyst, whose trophectoderm surrounds the fluid-filled blastocoel and
# the inner cell mass (the future embryo proper). Everything stays inside the zona pellucida until hatching
# just before implantation (about day 6-7).
import wikibio as bio
from wikibio import development as D

fig, ax = bio.canvas(20.4, 6.5)
P = bio.P
stages = [("zygote", "Zygote", "day 1"), ("2-cell", "2-cell", "day 1.5"), ("4-cell", "4-cell", "day 2"),
          ("8-cell", "8-cell", "day 3"), ("morula", "Morula", "day 4"), ("blastocyst", "Blastocyst", "day 5")]
r, y, dx, x0 = 1.15, 3.35, 3.35, 1.75
pos = {}
for k, (stage, name, day) in enumerate(stages):
    x = x0 + k * dx
    pos[stage] = D.embryo(ax, (x, y), r, stage)
    bio.label(ax, (x, y - r * 1.14 - 0.4), name, size="normal", bold=True)
    bio.label(ax, (x, y - r * 1.14 - 0.85), day, size="small", color=P.muted())
    if k:
        bio.arrow(ax, (x - dx + r * 1.25, y), (x - r * 1.25, y), kind="process", head=0.18)

# annotations
xz = x0
bio.callout(ax, (xz - 0.29, y), (xz - 1.0, 5.75), "Pronuclei")
bio.callout(ax, (xz + 0.3, y + r * 1.0), (xz + 0.7, 5.75), "Polar bodies")
bio.callout(ax, (x0 + dx + r * 0.8, y + r * 0.8), (x0 + dx + 1.0, 5.75), "Zona pellucida")
bio.callout(ax, (x0 + 2 * dx, y + 0.1), (x0 + 2 * dx + 0.4, 5.75), "Blastomeres")
ax.plot([x0 + dx - 0.8, x0 + dx - 0.8, x0 + 3 * dx + 0.8, x0 + 3 * dx + 0.8], [0.75, 0.6, 0.6, 0.75], color=P.muted(), lw=0.9)
bio.label(ax, (x0 + 2 * dx, 0.3), "Cleavage: more, smaller cells, no growth", size="small", color=P.muted())
bio.label(ax, (x0 + 4 * dx, 5.1), "Compaction", size="small", color=P.muted())
xb = x0 + 5 * dx
bio.callout(ax, pos["blastocyst"], (xb - 0.3, 6.0), "Inner cell mass")
bio.callout(ax, (xb + r * 0.88 * 0.71, y - r * 0.88 * 0.71), (xb + 1.0, 0.9), "Trophectoderm")
bio.callout(ax, (xb - 0.2, y - 0.35), (xb + 1.65, 5.6), "Blastocoel")
