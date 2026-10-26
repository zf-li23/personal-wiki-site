# Editing without a double-strand break.
# A: the cytosine base editor - deaminase on the strand displaced by the R loop, UGI to stop base excision
#    repair, D10A nickase on the opposite strand so that repair copies the edited strand.
# B: the editing window - fraction edited against position in the protospacer for a cytosine and an adenine
#    editor (Gaussian windows centred on positions 6 and 6.5), and the bystander problem.
# C: prime editing step by step.
# D: what each approach can write.
import numpy as np
import wikibio as bio
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(25.0, 13.0)

NEG = P.edge("negative")
BP = 0.42


def strandpair(x0, n, y, gap=0.46, top="dna", bot="dna2", lw=2.0):
    x1 = x0 + n * BP
    ax.plot([x0, x1], [y, y], color=P.edge(top), lw=lw, zorder=6)
    ax.plot([x0, x1], [y - gap, y - gap], color=P.edge(bot), lw=lw, zorder=6)
    return x1


# ----------------------------------------------------------------- A: the cytosine base editor
bio.panel(ax, "A", (0.1, 12.8))
bio.label(ax, (5.8, 12.8), "Cytosine base editor", size="small", bold=True)
yA = 10.6
x0 = 1.6
# target strand (paired with the guide) and displaced non-target strand
ax.plot([x0, x0 + 20 * BP], [yA - 0.9, yA - 0.9], color=P.edge("dna2"), lw=2.2, zorder=6)
ax.plot([x0, x0 + 20 * BP], [yA - 0.5, yA - 0.5], color=P.edge("rna"), lw=2.4, zorder=7)
xs = np.linspace(x0 + 1.5 * BP, x0 + 18.5 * BP, 60)
ax.plot(xs, yA + 0.28 * np.sin(np.pi * (xs - xs[0]) / (xs[-1] - xs[0])), color=P.edge("dna"), lw=2.2, zorder=7)
ax.plot([x0, x0 + 1.5 * BP], [yA, yA], color=P.edge("dna"), lw=2.2, zorder=7)
ax.plot([x0 + 18.5 * BP, x0 + 20 * BP], [yA, yA], color=P.edge("dna"), lw=2.2, zorder=7)
bio.label(ax, (x0 + 10 * BP, yA - 1.35), "guide RNA : target strand", size="tiny", color=P.edge("rna"))
bio.label(ax, (x0 - 0.2, yA + 0.1), "C", size="tiny", bold=True, ha="right", color=P.edge("dna"))
for k, pos in enumerate((5, 6, 7)):
    ax.add_patch(bio.core.Circle((x0 + pos * BP, yA + 0.25), 0.17, facecolor=P.fill("highlight"),
                                 edgecolor=P.edge("highlight"), lw=0.8, zorder=12))
    bio.label(ax, (x0 + pos * BP, yA + 0.25), "C", size="tiny", color=P.on_fill(), zorder=13)
bio.shape(ax, bio.blob((x0 + 6 * BP, yA + 1.5), 1.25, 0.6, wobble=0.05, seed=4), token="enzyme", zorder=9)
bio.label(ax, (x0 + 6 * BP, yA + 1.5), "deaminase", size="tiny", color=P.on_fill(), zorder=10)
bio.shape(ax, bio.blob((x0 + 12.5 * BP, yA + 1.5), 1.0, 0.6, wobble=0.05, seed=5), token="protein", zorder=9)
bio.label(ax, (x0 + 12.5 * BP, yA + 1.5), "nCas9", size="tiny", color=P.on_fill(), zorder=10)
bio.shape(ax, bio.blob((x0 + 17.5 * BP, yA + 1.5), 0.75, 0.52, wobble=0.05, seed=6), token="positive", zorder=9)
bio.label(ax, (x0 + 17.5 * BP, yA + 1.5), "UGI", size="tiny", color=P.on_fill(), zorder=10)
bio.box(ax, (x0 + 21.5 * BP, yA - 0.45), 1.2, 0.8, token="highlight", text="NGG", size="tiny", radius=0.05)
bio.label(ax, (x0 + 10 * BP, yA + 0.68), "single-stranded window of the displaced strand",
          size="tiny", color=P.muted())
# the nick on the opposite strand
ax.plot([x0 + 17 * BP, x0 + 17 * BP], [yA - 0.75, yA - 1.05], color=NEG, lw=1.8, zorder=14)
bio.label(ax, (x0 + 17 * BP + 0.1, yA - 1.35), "D10A nick", size="tiny", color=NEG, ha="left")
bio.label(ax, (5.8, 8.35), "U·G is not excised (UGI blocks the glycosylase); the nick makes repair copy the"
          " edited strand", size="tiny", color=P.muted())

# ----------------------------------------------------------------- B: the window
bio.panel(ax, "B", (0.1, 7.8))
bio.label(ax, (5.8, 7.8), "The editing window", size="small", bold=True)
pos = np.arange(1, 21)
cbe = 0.62 * np.exp(-((pos - 6.0) ** 2) / 3.2)
abe = 0.55 * np.exp(-((pos - 6.5) ** 2) / 3.6)
pl = Q.Plot(ax, (2.2, 1.9, 7.2, 4.9), xlim=(0, 21), ylim=(0, 0.8),
            xlabel="position in the protospacer (PAM at 21–23)", ylabel="fraction of alleles edited",
            xticks=[1, 5, 10, 15, 20], yticks=[0, 0.4, 0.8], ylabel_offset=1.0)
pl.span(4, 8, token="highlight", text="window", strength=0.75)
pl.line(pos, cbe, "negative")
pl.line(pos, abe, "positive")
pl.points([5, 7], [cbe[4], cbe[6]], "negative", r=0.09)
pl.text(14.5, 0.66, "cytosine editor", size="tiny", color=Q.line_color("negative"))
pl.text(14.5, 0.56, "adenine editor", size="tiny", color=Q.line_color("positive"))
pl.text(13.5, 0.3, "two Cs in the window:\nboth are deaminated\n(bystander editing)", size="tiny",
        color=P.ink())
bio.label(ax, (5.8, 0.55), "position is set by the PAM, so a target is editable only if a PAM puts it here",
          size="tiny", color=P.muted())

# ----------------------------------------------------------------- C: prime editing
bio.panel(ax, "C", (10.8, 12.8))
bio.label(ax, (17.6, 12.8), "Prime editing, step by step", size="small", bold=True)
steps = [
    ("nick the non-target strand (H840A)", "negative"),
    ("the 3′ end anneals to the primer binding site of the pegRNA", "rna"),
    ("reverse transcription copies the edit from the pegRNA template", "enzyme"),
    ("the edited 3′ flap and the unedited 5′ flap equilibrate", "neutral"),
    ("the 5′ flap is excised and the nick ligated", "positive"),
    ("the heteroduplex is resolved — mismatch repair tends to undo it", "highlight"),
]
for k, (text, token) in enumerate(steps):
    y = 11.8 - k * 1.0
    bio.box(ax, (12.4, y), 1.0, 0.62, token=token, text=f"{k + 1}", size="tiny", radius=0.1)
    bio.label(ax, (13.1, y), text, size="tiny", ha="left", color=P.ink())
    if k < len(steps) - 1:
        bio.arrow(ax, (12.4, y - 0.34), (12.4, y - 0.66), kind="process")
bio.label(ax, (17.6, 5.5), "the pegRNA has four designable parts: spacer, scaffold,\n"
          "reverse-transcriptase template and primer binding site", size="tiny", color=P.muted())
# the pegRNA itself
pg = [("spacer 20 nt", "rna", 2.6), ("scaffold", "neutral", 2.0), ("RT template", "enzyme", 2.4),
      ("PBS 13 nt", "highlight", 2.0)]
x = 11.6
for text, token, w in pg:
    bio.box(ax, (x + w / 2, 4.5), w, 0.7, token=token, text=text, size="tiny", radius=0.08)
    x += w + 0.12
bio.label(ax, (11.6, 3.9), "5′", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (20.9, 3.9), "3′", size="tiny", color=P.muted(), ha="right")

# ----------------------------------------------------------------- D: what each can write
bio.panel(ax, "D", (10.8, 3.2))
bio.label(ax, (17.8, 3.2), "What each approach can write", size="small", bold=True)
rows = [("cytosine editor", ["C·G → T·A"], "negative"),
        ("adenine editor", ["A·T → G·C"], "positive"),
        ("prime editing", ["all 12 substitutions", "insertions and deletions up to tens of bp"], "enzyme"),
        ("HDR with a donor", ["any sequence — but needs a break, a donor and S/G2"], "neutral")]
for i, (name, what, token) in enumerate(rows):
    y = 2.5 - i * 0.62
    bio.box(ax, (13.1, y), 3.4, 0.5, token=token, text=name, size="tiny", radius=0.08)
    bio.label(ax, (15.0, y), "; ".join(what), size="tiny", ha="left", color=P.ink())
