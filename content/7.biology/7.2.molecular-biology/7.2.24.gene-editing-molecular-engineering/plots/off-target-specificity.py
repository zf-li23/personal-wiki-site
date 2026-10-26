# What specificity means for an editor, and how it is measured.
# A: three independent classes of off-target activity - guide-dependent cleavage at mismatched sites,
#    guide-independent deamination of single-stranded DNA, and deamination of RNA.
# B: guide-dependent off-target cleavage from the directional-interrogation model of Section 24.4.2, for one
#    and two mismatches as a function of their position.
# C: what each assay can see, as the range of allele frequencies against the classes of event it reports.
# D: the structural variants that indel-level assays miss.
# E: pre-existing immunity to Cas9 orthologues.
import numpy as np
import wikibio as bio
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(25.0, 13.2)

NEG = P.edge("negative")
N, SEED = 20, 10
DG_SEED, DG_LATE, DG_MISMATCH = -0.15, -1.6, 4.0


def commit(mismatches=()):
    steps = np.array([DG_SEED if j < SEED else DG_LATE for j in range(N)])
    for m in mismatches:
        steps[m - 1] += DG_MISMATCH
    g = np.concatenate([[0.0], np.cumsum(steps)])
    return 1.0 / (1.0 + np.sum(np.exp(g[:-1])))


# ----------------------------------------------------------------- A: three classes
bio.panel(ax, "A", (0.1, 13.0))
bio.label(ax, (6.0, 13.0), "An editor's specificity is three numbers", size="small", bold=True)
classes = [("guide-dependent cleavage",
            "sites that resemble the protospacer,\nmismatches PAM-distal", "negative"),
           ("guide-independent deamination",
            "any single-stranded DNA exposed at a\nreplication fork or transcription bubble", "highlight"),
           ("RNA deamination",
            "thousands of transcript positions,\nindependent of the guide", "rna")]
for k, (name, note, token) in enumerate(classes):
    y = 11.8 - k * 1.7
    bio.box(ax, (3.4, y), 5.0, 0.64, token=token, text=name, size="tiny", radius=0.1)
    bio.label(ax, (6.3, y - 0.75), note, size="tiny", color=P.muted())
bio.label(ax, (6.0, 6.5), "each needs its own assay; an engineered deaminase can lower the last two\n"
          "without changing the first", size="tiny", color=P.ink())

# ----------------------------------------------------------------- B: mismatch position
bio.panel(ax, "B", (0.1, 5.9))
bio.label(ax, (6.0, 5.9), "Guide-dependent cleavage against mismatch position", size="small", bold=True)
pos = np.arange(1, N + 1)
one = np.array([commit((m,)) for m in pos]) / commit()
two = np.array([commit((m, min(m + 1, N))) for m in pos]) / commit()
pl = Q.Plot(ax, (2.2, 1.3, 7.2, 3.6), xlim=(0, N + 1), ylim=(1e-4, 2.0), ylog=True,
            xlabel="position of the mismatch (1 = PAM-proximal)", ylabel="relative cleavage",
            xticks=[1, 5, 10, 15, 20],
            yticks=[(1e-4, "$10^{-4}$"), (1e-2, "$10^{-2}$"), (1, "1")], ylabel_offset=1.2)
pl.line(pos, one, "negative", text="one mismatch", at=0.3, dy=0.5)
pl.line(pos, two, "neutral", text="two adjacent mismatches", at=0.6, dy=-0.55)
pl.span(1, SEED, token="highlight", text="seed", strength=0.78)
bio.label(ax, (6.0, 0.4), "two PAM-distal mismatches are still cut; one seed mismatch is not — so an off-target"
          " score must weight position", size="tiny", color=P.muted())

# ----------------------------------------------------------------- C: the assays
bio.panel(ax, "C", (10.6, 13.0))
bio.label(ax, (17.6, 13.0), "What each assay can see", size="small", bold=True)
assays = [("predicted sites, then amplicon sequencing", 1e-4, 1.0, "sequence-similar sites only", "neutral"),
          ("unbiased capture of breaks in cells", 1e-3, 1.0, "real breaks, in chromatin", "positive"),
          ("in vitro cleavage of genomic DNA", 1e-6, 1.0, "everything cuttable; over-reports", "rna"),
          ("whole-genome sequencing of clones", 1e-1, 1.0, "everything, including structural variants", "highlight")]
pl = Q.Plot(ax, (14.6, 9.4, 4.6, 2.9), xlim=(1e-6, 2), ylim=(-0.6, 3.6), xlog=True,
            xlabel="allele frequency it can detect",
            xticks=[(1e-6, "$10^{-6}$"), (1e-4, "$10^{-4}$"), (1e-2, "$10^{-2}$"), (1, "1")], yticks=None)
for i, (name, lo, hi, note, token) in enumerate(assays):
    y = 3 - i
    ax.plot([pl.X(lo), pl.X(hi)], [pl.Y(y), pl.Y(y)], color=Q.line_color(token), lw=5.0,
            solid_capstyle="round", zorder=7)
    bio.label(ax, (pl.X(lo) - 0.15, pl.Y(y)), name, size="tiny", ha="right")
    bio.label(ax, (pl.X(hi) + 0.2, pl.Y(y)), note, size="tiny", ha="left", color=P.muted())

# ----------------------------------------------------------------- D: structural variants
bio.panel(ax, "D", (10.6, 8.1))
bio.label(ax, (17.6, 8.1), "What an indel assay does not see", size="small", bold=True)
y = 7.4
for k, (label_text, token) in enumerate((("large deletion", "negative"), ("inversion", "highlight"),
                                         ("translocation between two guides", "rna"))):
    yy = y - k * 1.5
    ax.plot([12.6, 18.0], [yy, yy], color=P.edge("dna"), lw=2.0, zorder=5)
    if k == 0:
        ax.plot([14.2, 16.4], [yy, yy], color=P.surface(), lw=4.0, zorder=6)
        ax.plot([14.2, 16.4], [yy, yy], color=P.edge("negative"), lw=2.0, dashes=(3, 2), zorder=7)
    if k == 1:
        bio.arrow(ax, (14.2, yy + 0.35), (16.4, yy + 0.35), kind="link", bend=0.5,
                  color=P.edge("highlight"))
    if k == 2:
        ax.plot([12.6, 15.3], [yy - 0.45, yy - 0.45], color=P.edge("receptor"), lw=2.0, zorder=5)
        ax.plot([15.3, 18.0], [yy - 0.45, yy], color=P.edge("rna"), lw=2.0, dashes=(4, 2), zorder=8)
    bio.label(ax, (18.4, yy), label_text, size="tiny", ha="left", color=P.edge(token))
bio.label(ax, (17.6, 3.5), "two guides used together give the translocation between their sites\n"
          "at a measurable frequency", size="tiny", color=P.muted())

# ----------------------------------------------------------------- E: immunity
bio.panel(ax, "E", (10.6, 2.8))
bio.label(ax, (17.6, 2.8), "Pre-existing immunity", size="small", bold=True)
bars = [("antibodies to SpCas9", 0.6, "negative"), ("T cells against SpCas9", 0.5, "negative"),
        ("antibodies to SaCas9", 0.8, "receptor")]
pl = Q.Plot(ax, (16.0, 0.6, 4.2, 1.5), xlim=(0, 1), ylim=(-0.6, 2.6),
            xlabel="fraction of healthy adults", xticks=[(0, "0"), (0.5, "0.5"), (1, "1")], yticks=None)
for i, (name, v, token) in enumerate(bars):
    y = 2 - i
    ax.plot([pl.X(0), pl.X(v)], [pl.Y(y), pl.Y(y)], color=Q.line_color(token), lw=5.0,
            solid_capstyle="round", zorder=7)
    bio.label(ax, (pl.X(0) - 0.15, pl.Y(y)), name, size="tiny", ha="right")
bio.label(ax, (21.2, 1.4), "a constraint on in vivo editing,\nnot on ex vivo editing", size="tiny", ha="left",
          color=P.ink())
