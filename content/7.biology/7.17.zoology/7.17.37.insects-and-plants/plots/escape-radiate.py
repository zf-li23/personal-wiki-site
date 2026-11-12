# Escape-and-radiate coevolution (schematic, after Ehrlich and Raven 1964). Left: plant phylogeny; a new
# defence evolves on one branch and that clade radiates. Right: insect phylogeny; a tolerance mechanism
# evolves later on one branch, which colonizes the defended clade and radiates. Dashed lines: host use.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(20, 11)
ink, mut = P.ink(), P.muted()


def seg(p, q, color=ink, lw=1.6, ls="-"):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=color, lw=lw, ls=ls, solid_capstyle="round", zorder=5)


def tree(xroot, xtip, ys, split_y, clade, tok, flip=1):
    # simple ladder: undefended tips plus a radiating clade of len(clade) tips
    ymid = (min(ys) + max(ys)) / 2
    seg((xroot, ys[0]), (xroot, split_y))
    for y in ys:
        seg((xroot, y), (xtip, y))
    xs = xroot + flip * 2.2
    seg((xroot, split_y), (xs, split_y), color=P.edge(tok), lw=2.2)
    seg((xs, clade[0]), (xs, clade[-1]), color=P.edge(tok), lw=2.2)
    for y in clade:
        seg((xs, y), (xtip, y), color=P.edge(tok), lw=2.2)
    return xs


ys_p = [10.0, 9.0]
clade_p = [7.8, 7.0, 6.2, 5.4, 4.6, 3.8]
tree(1.2, 7.0, ys_p, 5.8, clade_p, "plant")
ax.plot([2.3], [5.8], marker="s", ms=9, color=P.fill("negative"), mec=P.edge("negative"), zorder=8)
bio.label(ax, (2.3, 5.2), "new defence", size="small", color=P.edge("negative"))
bio.label(ax, (4.1, 10.7), "Plants", size="normal", bold=True)
for y in ys_p:
    bio.label(ax, (4.1, y + 0.35), "undefended", size="tiny", color=mut)
bio.label(ax, (4.6, 2.9), "escape: defended clade radiates", size="small", color=P.edge("plant"))

ys_i = [10.0, 9.0, 8.0]
clade_i = [6.6, 5.6, 4.6, 3.6]
tree(18.8, 13.0, ys_i, 5.1, clade_i, "enzyme", flip=-1)
ax.plot([17.7], [5.1], marker="o", ms=9, color=P.fill("positive"), mec=P.edge("positive"), zorder=8)
bio.label(ax, (17.7, 4.5), "tolerance", size="small", color=P.edge("positive"))
bio.label(ax, (15.9, 10.7), "Insects", size="normal", bold=True)
bio.label(ax, (15.4, 2.9), "radiate onto defended plants", size="small", color=P.edge("enzyme"))
for yi, yp in zip(clade_i, clade_p[1:5]):
    seg((13.0, yi), (7.0, yp), color=mut, lw=0.9, ls="--")
for yi, yp in zip(ys_i[:2], ys_p):
    seg((13.0, yi), (7.0, yp), color=mut, lw=0.9, ls=":")
bio.label(ax, (10.0, 1.6), "Example: Brassicales (glucosinolates, ~90 Ma) and Pierinae (nitrile-specifier protein, ~70-80 Ma)",
          size="small", color=mut)
bio.label(ax, (10.0, 0.8), "time runs from the roots (outside) toward the tips (centre)", size="tiny", color=mut)
