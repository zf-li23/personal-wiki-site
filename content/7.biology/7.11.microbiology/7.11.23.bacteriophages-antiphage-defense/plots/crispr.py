# CRISPR-Cas as an immune system: the locus, the three stages, the types, and how phages evade it.
# A: the locus (leader, repeats, spacers acquired from past invaders, cas genes) and adaptation by Cas1-Cas2.
# B: expression (pre-crRNA processed into crRNAs loaded on effector complexes) and interference (PAM
#    recognition, seed pairing, R loop, cleavage).
# C: the classes and types, with the effector and what it cuts.
# D: the phage counter-measures.
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(32, 13.6)
MUT = P.muted()
DNA = P.edge("dna") if not P.is_dark() else P.fill("dna")
RNA = P.edge("rna") if not P.is_dark() else P.fill("rna")


def repeat(x, y, w=0.42, h=0.52, zorder=10):
    ax.add_patch(Polygon([[x, y - h / 2], [x + w, y - h / 2], [x + w * 0.5, y + h / 2]], closed=True,
                         facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.5, zorder=zorder))


def spacer(x, y, w, token, h=0.52, text=None, zorder=10):
    ax.add_patch(Rectangle((x, y - h / 2), w, h, facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.6, zorder=zorder))
    if text:
        bio.label(ax, (x + w / 2, y), text, size="tiny", color=P.on_fill(), zorder=zorder + 1)


# ---------------------------------------------------------------- A: locus and adaptation
bio.panel(ax, "A", (0.2, 13.3))
bio.label(ax, (0.9, 13.1), "The locus and its growth", size="title", bold=True, ha="left")
y = 11.2
x = 1.0
ax.add_patch(FancyBboxPatch((x, y - 0.3), 1.5, 0.6, boxstyle="round,pad=0,rounding_size=0.1",
                            facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.7, zorder=10))
bio.label(ax, (x + 0.75, y), "cas genes", size="tiny", color=P.on_fill(), zorder=11)
x += 1.7
ax.add_patch(Rectangle((x, y - 0.25), 1.0, 0.5, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                       lw=0.6, zorder=10))
bio.label(ax, (x + 0.5, y), "leader", size="tiny", color=P.on_fill(), zorder=11)
x += 1.1
toks = ["negative", "drug", "protein", "virus"]
for i in range(4):
    repeat(x, y)
    x += 0.5
    spacer(x, y, 0.95, toks[i], text=f"{4 - i}")
    x += 1.05
repeat(x, y)
bio.label(ax, (2.7, y + 0.95), "newest spacer is added here", size="tiny", color=MUT, ha="left")
bio.arrow(ax, (4.3, y + 0.8), (4.3, y + 0.35), kind="process", lw=0.9, head=0.16, color=MUT)
bio.label(ax, (10.6, y), "a dated record\nof past infections", size="tiny", color=MUT, ha="left")
# adaptation
yy = 8.6
ax.plot([1.0, 7.6], [yy, yy], color=DNA, lw=2.4)
spacer(3.2, yy, 1.0, "negative", h=0.36, zorder=12)
ax.add_patch(Rectangle((2.7, yy - 0.18), 0.45, 0.36, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                       lw=0.5, zorder=12))
bio.label(ax, (2.9, yy + 0.55), "PAM", size="tiny", color=MUT)
bio.label(ax, (3.7, yy - 0.6), "protospacer", size="tiny", color=MUT)
bio.label(ax, (1.0, yy + 1.0), "incoming phage genome", size="tiny", color=MUT, ha="left")
ax.add_patch(Circle((6.2, yy + 0.9), 0.45, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.7, zorder=12))
bio.label(ax, (6.2, yy + 0.9), "Cas1\nCas2", size="tiny", color=P.on_fill(), zorder=13)
bio.arrow(ax, (4.3, yy + 0.4), (4.3, 10.6), kind="process", lw=1.1, head=0.2, bend=0.1)
bio.label(ax, (7.0, yy + 0.9), "excision and integration\nat the leader end", size="tiny", color=MUT, ha="left")
bio.label(ax, (1.0, 7.3), "priming: a partial match that fails to be cut strongly stimulates the acquisition of further\n"
                          "spacers from the same genome, so the host updates its memory faster than the phage escapes",
          size="tiny", color=MUT, ha="left")

# ---------------------------------------------------------------- B: expression and interference
bio.panel(ax, "B", (0.2, 6.3))
bio.label(ax, (0.9, 6.1), "Expression and interference", size="title", bold=True, ha="left")
y3 = 4.6
ax.plot([1.0, 5.2], [y3, y3], color=RNA, lw=2.0)
bio.label(ax, (1.0, y3 + 0.5), "pre-crRNA", size="tiny", color=MUT, ha="left")
bio.arrow(ax, (5.5, y3), (6.4, y3), kind="process", lw=1.1, head=0.2)
bio.label(ax, (5.95, y3 + 0.45), "processing", size="tiny", color=MUT)
for i in range(3):
    xx = 6.9 + i * 1.5
    ax.plot([xx, xx + 1.0], [y3, y3], color=RNA, lw=2.0)
    spacer(xx + 0.2, y3, 0.6, toks[i], h=0.3, zorder=12)
bio.label(ax, (8.6, y3 - 0.6), "crRNAs", size="tiny", color=MUT)
# interference
y4 = 2.3
ax.plot([1.0, 9.6], [y4 + 0.2, y4 + 0.2], color=DNA, lw=2.0)
ax.plot([1.0, 9.6], [y4 - 0.2, y4 - 0.2], color=DNA, lw=2.0)
ax.add_patch(Rectangle((3.4, y4 - 0.3), 0.5, 0.6, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                       lw=0.5, zorder=12))
bio.label(ax, (3.65, y4 + 0.8), "PAM", size="tiny", color=MUT)
ax.add_patch(FancyBboxPatch((4.0, y4 - 0.75), 2.6, 1.5, boxstyle="round,pad=0,rounding_size=0.2",
                            facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.8, alpha=0.9, zorder=11))
bio.label(ax, (5.3, y4 + 0.1), "effector\n+ crRNA", size="tiny", color=P.on_fill(), zorder=13)
bio.label(ax, (4.3, y4 - 1.1), "seed", size="tiny", color=MUT)
bio.arrow(ax, (7.2, y4 + 0.9), (7.2, y4 + 0.35), kind="process", lw=1.0, head=0.18,
          color=P.edge("negative") if not P.is_dark() else P.fill("negative"))
bio.label(ax, (7.3, y4 + 1.25), "cleavage", size="tiny", color=MUT)
bio.label(ax, (1.0, 0.75), "the spacer inside the array has repeats beside it, not a PAM, so the cell never cuts its own locus",
          size="tiny", color=MUT, ha="left")

# ---------------------------------------------------------------- C: classes and types
bio.panel(ax, "C", (12.4, 13.3))
bio.label(ax, (13.1, 13.1), "Classes and types", size="title", bold=True, ha="left")
rows = [("Class 1", "", "multi-subunit effector complexes", True),
        ("I", "Cascade + Cas3", "processive degradation of dsDNA; priming", False),
        ("III", "Csm / Cmr", "binds nascent transcripts, cuts RNA and DNA;\nmakes cyclic oligoadenylate, which switches on\nan indiscriminate RNase", False),
        ("IV", "Csf", "mostly plasmid-encoded, targets plasmids", False),
        ("Class 2", "", "a single large effector protein", True),
        ("II", "Cas9", "dual-RNA-guided dsDNA cleavage (the editing tool)", False),
        ("V", "Cas12", "dsDNA cleavage; collateral ssDNase activity", False),
        ("VI", "Cas13", "targets RNA; once activated cleaves RNA\nindiscriminately and arrests the cell", False)]
yy = 11.9
for name, eff, txt, is_head in rows:
    if is_head:
        bio.label(ax, (13.1, yy), name, size="small", bold=True, ha="left")
        bio.label(ax, (15.0, yy), txt, size="tiny", color=MUT, ha="left")
        yy -= 0.85
        continue
    bio.label(ax, (13.4, yy), name, size="small", ha="left")
    bio.label(ax, (14.3, yy), eff, size="tiny", ha="left")
    bio.label(ax, (16.6, yy), txt, size="tiny", color=MUT, ha="left")
    yy -= 1.05 if "\n" not in txt else 1.5
bio.label(ax, (13.1, 2.3), "About 40 % of bacterial and 85 % of archaeal genomes carry a CRISPR–Cas system.\n"
                           "Cas1 and Cas2, the adaptation module, are the only proteins common to all of them.",
          size="tiny", color=MUT, ha="left")

# ---------------------------------------------------------------- D: evasion
bio.panel(ax, "D", (24.0, 13.3))
bio.label(ax, (24.7, 13.1), "How phages evade it", size="title", bold=True, ha="left")
ev = [("escape mutants", "one substitution in the seed region or the PAM\nabolishes interference — but primes new spacers"),
      ("anti-CRISPR proteins", "small proteins, injected with the genome or made\nat once, that block target binding or cleavage,\nmimic DNA, or degrade the signalling nucleotides"),
      ("phage-encoded CRISPR", "phages of $Vibrio$ $cholerae$ carry their own system,\ndirected against the host's antiphage island"),
      ("compartmentalization", "jumbo phages wall their DNA inside a proteinaceous\nshell that DNA-targeting nucleases cannot enter")]
yy = 11.9
for name, txt in ev:
    bio.label(ax, (24.7, yy), name, size="small", ha="left")
    bio.label(ax, (24.7, yy - 0.95), txt, size="tiny", color=MUT, ha="left")
    ax.plot([24.7, 31.6], [yy + 0.6, yy + 0.6], color=P.mix(MUT, P.surface(), 0.65), lw=0.6)
    yy -= 2.6
