# Four solutions to priming DNA synthesis and to the end of a linear genome.
# A: RNA primers at an internal origin on a circular genome (simian virus 40) - two forks, no ends.
# B: protein priming and strand displacement (adenovirus) - the terminal protein carries the first dCMP,
#    and the displaced strand anneals its inverted terminal repeats into a new duplex origin.
# C: self-priming by a terminal hairpin (parvovirus), resolved by a nick at the terminal resolution site.
# D: rolling-circle synthesis from a nick, giving a concatemer that is cut into genome-length units.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(18, 10.2)
LW = 2.1


def strand(pts, tok="dna", lw=LW, dashed=False, zorder=6):
    p = np.asarray(pts, float)
    ax.plot(p[:, 0], p[:, 1], color=P.edge(tok), lw=lw, ls="--" if dashed else "-",
            solid_capstyle="round", zorder=zorder)


def new_strand(pts, zorder=7):
    """Newly made DNA, in the lighter shade used throughout the site."""
    strand(pts, "negative", lw=LW, zorder=zorder)


def title(xy, text):
    bio.label(ax, xy, text, size="title", bold=True)


def note(xy, text):
    bio.label(ax, xy, text, size="tiny", color=P.muted())


# --- A  RNA priming at an internal origin -----------------------------------------------------------------
bio.panel(ax, "A", (0.1, 10.0))
title((4.3, 9.7), "RNA primer at an origin")
y = 7.6
x0, x1 = 1.2, 7.6
xs = np.linspace(x0, x1, 200)
bub = np.where((xs > 3.0) & (xs < 5.8), 0.55 * np.cos((xs - 4.4) / 1.4 * np.pi / 2) ** 2, 0.0)
strand(np.c_[xs, y + 0.18 + bub], "dna")
strand(np.c_[xs, y - 0.18 - bub], "dna2")
for s in (1, -1):
    xx = np.linspace(3.6, 5.2, 40)
    new_strand(np.c_[xx, np.full_like(xx, y + s * 0.46)])
for x in (3.5, 5.3):
    ax.plot([x, x + 0.45], [y + 0.46, y + 0.46], color=P.edge("rna"), lw=3.0, solid_capstyle="round", zorder=9)
    ax.plot([x - 0.1, x + 0.35], [y - 0.46, y - 0.46], color=P.edge("rna"), lw=3.0, solid_capstyle="round", zorder=9)
bio.label(ax, (4.4, y + 1.15), "Ori", size="small", bold=True)
bio.callout(ax, (3.72, y + 0.46), (1.9, 9.0), "RNA primer")
for x, s in ((2.95, -1), (5.9, 1)):
    bio.arrow(ax, (x, y), (x + s * 0.8, y), kind="process", color=P.muted())
bio.label(ax, (4.3, 6.1), "Two forks move outwards; on a circle there is no end to leave unreplicated",
          size="small", color=P.muted())
note((4.3, 5.65), "polyomaviruses, papillomaviruses, herpesviruses, integrated proviruses")

# --- B  protein priming -------------------------------------------------------------------------------------
bio.panel(ax, "B", (9.3, 10.0))
title((13.8, 9.7), "Protein priming")
y = 8.4
strand([(10.4, y), (16.8, y)], "dna")                     # template strand
bio.protein(ax, (10.4, y), 0.4, 0.4, "enzyme", zorder=10)
bio.label(ax, (10.6, y + 0.55), "pTP–dCMP", size="tiny", ha="left")
new_strand([(10.6, y - 0.16), (14.0, y - 0.16)])
bio.arrow(ax, (14.05, y - 0.16), (15.1, y - 0.16), kind="process", color=P.edge("negative"))
strand([(10.4, y - 0.32), (11.3, y - 1.05), (12.5, y - 1.25), (13.7, y - 0.95), (14.3, y - 0.42), (16.8, y - 0.36)], "dna2")
bio.callout(ax, (12.5, y - 1.25), (13.9, 6.75), "Displaced parental strand")
y2 = 5.7
strand([(11.4, y2), (16.2, y2)], "dna2")
for x, dx in ((11.4, 0.38), (16.2, -0.38)):
    bio.box(ax, (x + dx, y2), 0.72, 0.42, "highlight", text="ITR", size="tiny", radius=0.05)
t = np.linspace(np.pi, 2 * np.pi, 80)
ax.plot(13.8 + 2.0 * np.cos(t), y2 + 0.85 * np.sin(t) * -1, color=P.edge("dna2"), lw=LW, zorder=5)
bio.arrow(ax, (16.4, 6.8), (16.4, 6.1), kind="process", color=P.muted())
bio.label(ax, (11.1, y2 + 0.95), "the strand folds back:\nits ITRs pair", size="tiny", color=P.muted())
bio.label(ax, (13.8, 4.95), "a duplex origin is re-formed, and this strand is copied in the same way",
          size="small", color=P.muted())
note((13.8, 4.5), "adenoviruses, bacteriophage φ29, (on RNA) picornaviruses and hepadnaviruses")

# --- C  self-priming hairpin ---------------------------------------------------------------------------------
bio.panel(ax, "C", (0.1, 4.3))
title((4.3, 4.0), "Self-priming hairpin")
y = 2.4
strand([(1.6, y), (6.4, y)], "dna")
for x, s in ((1.6, -1),):
    ax.plot([x, x - 0.5], [y, y], color=P.edge("dna"), lw=LW, zorder=6)
    ax.plot([x - 0.5, x - 0.5], [y - 0.4, y + 0.4], color=P.edge("dna"), lw=LW, zorder=6)
    ax.plot([x - 0.5, x - 0.15], [y + 0.4, y + 0.4], color=P.edge("dna"), lw=LW, zorder=6)
    ax.plot([x - 0.5, x - 0.15], [y - 0.4, y - 0.4], color=P.edge("dna"), lw=LW, zorder=6)
bio.label(ax, (1.0, y + 0.72), "3′-OH", size="tiny", bold=True)
new_strand([(1.45, y + 0.4), (5.3, y + 0.4)])
bio.arrow(ax, (5.35, y + 0.4), (6.3, y + 0.4), kind="process", color=P.edge("negative"))
ax.plot([4.2, 4.2], [y - 0.32, y + 0.72], color=P.edge("highlight"), lw=2.2, zorder=11)
bio.callout(ax, (4.2, y + 0.72), (5.3, 3.5), "Rep nicks the terminal\nresolution site")
bio.label(ax, (4.3, 1.1), "the folded end primes synthesis; a nick lets the hairpin itself be copied",
          size="small", color=P.muted())
note((4.3, 0.65), "parvoviruses; a related scheme closes poxvirus genomes")

# --- D  rolling circle ----------------------------------------------------------------------------------------
bio.panel(ax, "D", (9.3, 4.3))
title((13.8, 4.0), "Rolling circle")
c = (11.6, 2.2)
t = np.linspace(0.25, 2 * np.pi + 0.1, 300)
ax.plot(c[0] + 1.0 * np.cos(t), c[1] + 1.0 * np.sin(t), color=P.edge("dna"), lw=LW, zorder=6)
t2 = np.linspace(0, 2 * np.pi, 300)
ax.plot(c[0] + 0.82 * np.cos(t2), c[1] + 0.82 * np.sin(t2), color=P.edge("dna2"), lw=LW, zorder=6)
bio.label(ax, (c[0] + 1.5, c[1] + 0.55), "nick", size="tiny", color=P.edge("highlight"))
tail = np.array([(c[0] + 1.0 * np.cos(0.25), c[1] + 1.0 * np.sin(0.25)), (13.6, 2.6), (15.0, 2.9), (16.6, 2.75)])
new_strand(tail)
for x in (14.0, 15.3, 16.4):
    ax.plot([x, x], [2.55, 3.1], color=P.muted(), lw=1.0, ls=":", zorder=9)
bio.label(ax, (15.2, 3.45), "concatemer: head-to-tail copies", size="tiny", color=P.muted())
bio.label(ax, (15.2, 2.1), "cut to genome length\nduring packaging", size="tiny", color=P.muted())
note((13.8, 0.65), "bacteriophage φX174 and λ; the late phase of herpesvirus replication")
