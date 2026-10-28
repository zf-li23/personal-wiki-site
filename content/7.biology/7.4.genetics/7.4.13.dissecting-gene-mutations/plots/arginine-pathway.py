"""One gene, one enzyme: the arginine pathway of Neurospora inferred from auxotrophs.
Top: the pathway N-acetylornithine -> ornithine -> citrulline -> argininosuccinate -> arginine, with the enzymes
encoded by ARG-E, ARG-F, ARG-G and ARG-H (four complementation groups). Bottom: growth (+) or no growth (-) of the
wild type and of each mutant class on minimal medium alone or supplemented with one intermediate. A mutant grows on
every compound downstream of its block; the fewer supplements rescue a mutant, the later its block."""

from matplotlib.patches import Rectangle

import wikibio as bio

P = bio.P

fig, ax = bio.canvas(18.0, 9.2)
mets = ["N-acetyl-\nornithine", "ornithine", "citrulline", "arginino-\nsuccinate", "arginine"]
genes = ["ARG-E", "ARG-F", "ARG-G", "ARG-H"]
xs = [2.2, 5.9, 9.6, 13.3, 17.0 - 0.3]
y = 7.8
for x, m in zip(xs, mets):
    bio.box(ax, (x, y), 2.4, 1.0, token="metabolite", text=m, size="small")
for k, g in enumerate(genes):
    bio.arrow(ax, (xs[k] + 1.25, y), (xs[k + 1] - 1.25, y), kind="process")
    bio.label(ax, ((xs[k] + xs[k + 1]) / 2, y + 0.45), g, size="tiny", italic=True)

cols = ["nothing", "ornithine", "citrulline", "arginino-\nsuccinate", "arginine"]
rows = [("wild type", 0), ("ARG-E", 1), ("ARG-F", 2), ("ARG-G", 3), ("ARG-H", 4)]
cx0, cw, ch = 5.0, 2.4, 0.72
ty = 5.6
bio.label(ax, (cx0 - 2.6, ty + 0.55), "minimal medium plus:", size="tiny", ha="left", color=P.muted())
for j, c in enumerate(cols):
    bio.label(ax, (cx0 + j * cw + cw / 2, ty + 0.5), c, size="tiny")
for r, (name, block) in enumerate(rows):
    yy = ty - (r + 1) * ch
    bio.label(ax, (cx0 - 0.2, yy + ch / 2), name if r == 0 else f"{name} mutant", size="small", ha="right",
              italic=r > 0)
    for j in range(len(cols)):
        grow = r == 0 or j >= block
        ax.add_patch(Rectangle((cx0 + j * cw, yy), cw, ch, facecolor=P.fill("positive") if grow else
                               P.fill("negative"), edgecolor=P.surface(), lw=1.5))
        bio.label(ax, (cx0 + j * cw + cw / 2, yy + ch / 2), "+" if grow else "-", size="normal",
                  color=P.on_fill())
bio.label(ax, (9.0, 0.6), "growth on a compound places the block upstream of it", size="small")
