"""The cell mechanics of meiosis (schematic) and a cohesion-decay model of the maternal age effect.

(A) Prophase I of one pair of homologues (blue paternal, orange maternal; sister chromatids drawn as one
line until diplotene). Leptotene: chromosomes condense along protein axes; programmed double-strand breaks
(Spo11) start recombination and the search for the homologue. Zygotene: synapsis begins, the
synaptonemal complex zipping the axes together about 100 nm apart. Pachytene: full synapsis; recombination
nodules mark crossovers. Diplotene: the synaptonemal complex disassembles and the homologues stay joined at
chiasmata (the visible crossovers). Diakinesis: the bivalents condense further.
(B) Chromosomes at metaphase and anaphase of meiosis I and II. In meiosis I the two sister kinetochores of a
homologue are fused and face the same pole (co-orientation; monopolin in budding yeast, Meikin in mammals);
separase cleaves arm cohesin (the Rec8 kleisin), which releases the chiasmata and separates the homologues,
while centromeric Rec8 is protected by shugoshin (Sgo2 in mammals) with PP2A-B56. In meiosis II the sisters
bi-orient as in mitosis and the remaining cohesin is cleaved.
(C) An illustrative model of the maternal age effect. Cohesin is loaded on oocyte chromosomes before birth and
is not replaced; suppose it decays exponentially at rate k = 0.035 per year from a starting amount that varies
between the 23 bivalents (log-normal, standard deviation 0.75 in log units) and that a bivalent missegregates
when it falls below 6% of the mean starting amount. The predicted fraction of aneuploid eggs (at least one
missegregating bivalent) rises from about 10% at 25 to about half at 40, the shape of the observed
increase; the parameters are chosen for illustration, not fitted to data.
"""

import numpy as np
from scipy.stats import norm

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

fig, ax = bio.canvas(27.0, 12.0)

# ----- A
bio.panel(ax, "A", (0.2, 11.8))
names = ["leptotene", "zygotene", "pachytene", "diplotene", "diakinesis"]
xs = np.linspace(1.6, 11.6, 5)
y0, L = 8.3, 3.0
for i, (x, n) in enumerate(zip(xs, names)):
    bio.label(ax, (x, 11.1), n, size="tiny", bold=True)
    t = np.linspace(-1, 1, 50)
    if i == 0:
        gap = np.full_like(t, 0.7)
    elif i == 1:
        gap = 0.15 + 0.55 * np.clip((t + 0.2), 0, 1.2) / 1.2
    elif i in (2,):
        gap = np.full_like(t, 0.15)
    else:
        gap = 0.45 + 0.0 * t
        gap = np.where(np.abs(t - 0.35) < 0.08, 0.05, gap)
    length = L if i < 4 else L * 0.6
    yy = y0 + t * length / 2
    lw = 3.0 if i < 3 else 2.2
    if i < 3:
        ax.plot(x - gap / 2, yy, color=P.edge("dna"), lw=lw, solid_capstyle="round", zorder=5)
        ax.plot(x + gap / 2, yy, color=P.edge("receptor"), lw=lw, solid_capstyle="round", zorder=5)
        if i >= 1:
            for k in range(len(t)):
                if gap[k] <= 0.16 and k % 3 == 0:
                    ax.plot([x - gap[k] / 2, x + gap[k] / 2], [yy[k]] * 2, color=P.muted(), lw=0.7, zorder=4)
        if i == 2:
            for tt in (-0.5, 0.35):
                ax.add_patch(__import__("matplotlib.patches", fromlist=["Circle"]).Circle(
                    (x, y0 + tt * L / 2), 0.11, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), zorder=6))
    else:
        # four chromatids with one chiasma (colors swap beyond it)
        for side, tok in ((-1, "dna"), (1, "receptor")):
            for o in (-0.07, 0.07):
                xx = x + side * gap / 2 + side * o
                above = t > 0.35
                ax.plot(np.where(above | (o * side > 0), xx, np.nan), yy, color=P.edge(tok), lw=lw, zorder=5)
                other = "receptor" if tok == "dna" else "dna"
                ax.plot(np.where(~above & (o * side < 0), xx, np.nan), yy, color=P.edge(other), lw=lw, zorder=5)
        bio.callout(ax, (x, y0 + 0.35 * length / 2), (x + 0.9, y0 + 2.1), "chiasma", size="tiny")
bio.label(ax, (6.6, 6.2), "grey rungs: synaptonemal complex   yellow: recombination nodules", size="tiny", color=P.muted())

# ----- B
bio.panel(ax, "B", (0.2, 5.6))
cols = [("metaphase I", 1.8), ("anaphase I", 5.4), ("metaphase II", 8.9), ("anaphase II", 12.0)]
yb = 2.8
for name, x in cols:
    bio.label(ax, (x, 5.0), name, size="tiny", bold=True)
    ax.plot([x - 1.5, x - 1.5], [yb - 1.6, yb + 1.6], color=P.muted(), lw=0.8, ls=":")
    ax.plot([x + 1.5, x + 1.5], [yb - 1.6, yb + 1.6], color=P.muted(), lw=0.8, ls=":")


def chrom(x, y, tok, n=2, h=1.0, lw=3.0):
    for o in ((-0.06, 0.06) if n == 2 else (0.0,)):
        ax.plot([x + o, x + o], [y - h / 2, y + h / 2], color=P.edge(tok), lw=lw, solid_capstyle="round", zorder=5)


# metaphase I: bivalent, each homologue co-oriented to one pole
x = cols[0][1]
chrom(x - 0.25, yb, "dna"); chrom(x + 0.25, yb, "receptor")
for s, tok in ((-1, "dna"), (1, "receptor")):
    ax.plot([x + s * 0.32, x + s * 1.5], [yb, yb], color=P.edge("channel"), lw=1.0, zorder=4)
bio.label(ax, (x, yb - 1.25), "sister kinetochores\nco-oriented", size="tiny", color=P.muted())
# anaphase I
x = cols[1][1]
chrom(x - 0.9, yb, "dna"); chrom(x + 0.9, yb, "receptor")
for s in (-1, 1):
    bio.arrow(ax, (x + s * 1.0, yb + 0.9), (x + s * 1.45, yb + 0.9), kind="process")
bio.label(ax, (x, yb - 1.25), "arm cohesin cleaved;\ncentromeres protected", size="tiny", color=P.muted())
ax.add_patch(__import__("matplotlib.patches", fromlist=["Circle"]).Circle((x - 0.9, yb), 0.1, facecolor=P.fill("highlight"),
             edgecolor=P.edge("highlight"), zorder=7))
ax.add_patch(__import__("matplotlib.patches", fromlist=["Circle"]).Circle((x + 0.9, yb), 0.1, facecolor=P.fill("highlight"),
             edgecolor=P.edge("highlight"), zorder=7))
# metaphase II: sisters bi-oriented
x = cols[2][1]
chrom(x, yb, "dna")
for s in (-1, 1):
    ax.plot([x + s * 0.08, x + s * 1.5], [yb, yb], color=P.edge("channel"), lw=1.0, zorder=4)
bio.label(ax, (x, yb - 1.25), "sisters bi-oriented", size="tiny", color=P.muted())
# anaphase II
x = cols[3][1]
chrom(x - 0.7, yb, "dna", n=1); chrom(x + 0.7, yb, "dna", n=1)
bio.label(ax, (x, yb - 1.25), "centromeric\ncohesin cleaved", size="tiny", color=P.muted())

# ----- C
bio.panel(ax, "C", (14.6, 11.8))
c = charts.axes_at(ax, (16.4, 1.8, 10.0, 9.0))
age = np.linspace(15, 48, 300)
K, SD, TH = 0.035, 0.75, 0.06
pb = norm.cdf((np.log(TH) + K * age) / SD)
pe = 1 - (1 - pb) ** 23
c.plot(age, 100 * pe, color=charts.line("negative"), lw=2.0, label="eggs with ≥ 1 error")
c.plot(age, 100 * np.exp(-K * age), color=charts.line("enzyme"), lw=1.4, ls="--", label="mean cohesin (% of amount at birth)")
c.set_xlim(15, 48)
c.set_ylim(0, 100)
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(c, "maternal age / years", "percent")
