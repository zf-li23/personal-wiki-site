# The programme of a T4 infection.
# A: the timetable at 37 C (times from the classical description of the T4 cycle): host synthesis stops,
#    early, middle and late transcription follow one another, DNA replication starts at 4-5 min, the first
#    complete particle appears at about 12 min (the end of the eclipse period), and lysis occurs at 25-30 min.
# B: how the switch is made - progressive modification of the host RNA polymerase, and the coupling of late
#    transcription to replication through the sliding clamp gp45 acting as a mobile enhancer.
# C: replication gives a concatemer; the terminase packages a headful, which makes the progeny genomes
#    circularly permuted and terminally redundant.
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Polygon

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(30, 12.2)
MUT = P.muted()

# ---------------------------------------------------------------- A: the timetable
bio.panel(ax, "A", (0.2, 11.9))
bio.label(ax, (0.9, 11.7), "The timetable of one infection (37 °C)", size="title", bold=True, ha="left")
pl = quant.Plot(ax, (2.2, 2.6, 9.4, 7.0), xlim=(0, 30), ylim=(0, 9), xlabel="time after infection / min",
                xticks=[0, 5, 10, 15, 20, 25, 30], frame="l")
bars = [("host transcription and\nDNA synthesis", 0, 1.2, "negative", 8.3),
        ("early transcripts", 0.3, 6, "dna", 7.2),
        ("middle transcripts", 2, 12, "enzyme", 6.1),
        ("late transcripts", 9, 30, "drug", 5.0),
        ("phage DNA replication", 4.5, 30, "dna2", 3.9),
        ("heads, tails and fibres", 9, 30, "protein", 2.8),
        ("complete virions inside", 12, 30, "virus", 1.7)]
for name, a, b, tok, y in bars:
    x0, x1 = pl.X(a), pl.X(b)
    yy = pl.Y(y)
    ax.add_patch(FancyBboxPatch((x0, yy - 0.22), x1 - x0, 0.44, boxstyle="round,pad=0,rounding_size=0.1",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.7, zorder=8))
    bio.label(ax, (x0 - 0.15, yy), name, size="tiny", ha="right", zorder=9)
for t_, txt, tok in ((12, "first particle:\nend of the eclipse", "highlight"), (27, "lysis:\n~100 progeny", "negative")):
    pl.vline(t_, token=tok, dashed=True)
    bio.label(ax, (pl.X(t_) + 0.12, pl.Y(0.55)), txt, size="tiny", color=quant.line_color(tok), ha="left")

# ---------------------------------------------------------------- B: the transcriptional switch
bio.panel(ax, "B", (12.6, 11.9))
bio.label(ax, (13.3, 11.7), "Switching the host RNA polymerase", size="title", bold=True, ha="left")
stages = [("early", 13.2, "host core + σ⁷⁰", "host-like promoters;\nAlt (injected) and ModA\nADP-ribosylate the α subunits,\nAsiA binds σ⁷⁰"),
          ("middle", 13.2 - 0.0, "core + modified σ⁷⁰ + MotA", "MotA boxes replace the −35 element"),
          ("late", 13.2, "core + gp55 + gp33", "only a −10 element; gp45, the sliding\nclamp loaded at nicks in replicating\nDNA, acts as a mobile enhancer")]
y = 9.6
for i, (name, x, holo, txt) in enumerate(stages):
    yy = y - i * 2.6
    ax.add_patch(FancyBboxPatch((13.2, yy - 0.42), 2.1, 0.84, boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=8))
    bio.label(ax, (14.25, yy), name, size="small", bold=True, color=P.on_fill(), zorder=9)
    bio.label(ax, (15.6, yy + 0.22), holo, size="tiny", ha="left")
    bio.label(ax, (15.6, yy - 0.42), txt, size="tiny", ha="left", color=MUT)
    if i < 2:
        bio.arrow(ax, (14.25, yy - 0.5), (14.25, yy - 2.1), kind="process", lw=1.1, head=0.2)
bio.label(ax, (13.2, 2.1), "The genome itself is modified: cytosine is replaced by 5-hydroxymethylcytosine\n"
                           "and glucosylated, which protects it from the host's restriction enzymes, while a phage\n"
                           "nuclease specific for ordinary cytosine destroys the host chromosome.",
          size="tiny", ha="left", color=MUT)

# ---------------------------------------------------------------- C: concatemer and headful packaging
bio.panel(ax, "C", (22.4, 11.9))
bio.label(ax, (23.1, 11.7), "Concatemers and headful packaging", size="title", bold=True, ha="left")
letters = list("ABCDEFG")
col = P.edge("dna") if not P.is_dark() else P.fill("dna")
x0, w = 22.9, 0.78
ax.plot([x0, x0 + 7 * w * 1.6], [9.6, 9.6], color=col, lw=2.4, solid_capstyle="butt")
for i in range(11):
    bio.label(ax, (x0 + (i + 0.5) * w, 9.95), letters[i % 7], size="tiny", color=MUT)
ax.plot([x0, x0 + 11 * w], [9.6, 9.6], color=col, lw=2.6, solid_capstyle="butt")
bio.label(ax, (x0, 10.5), "concatemer: genomes joined end to end by recombination", size="tiny", ha="left", color=MUT)
for k in range(3):
    a = x0 + k * 3.1 * w
    b = a + 3.4 * w
    yy = 8.1 - k * 1.25
    ax.plot([a, b], [yy, yy], color=col, lw=2.6, solid_capstyle="butt")
    for s, xx in ((-1, a), (1, b)):
        ax.plot([xx, xx], [yy - 0.28, yy + 0.28], color=P.edge("negative") if not P.is_dark() else P.fill("negative"), lw=1.2)
    bio.label(ax, (b + 0.25, yy), f"headful {k + 1}", size="tiny", ha="left", color=MUT)
bio.label(ax, (x0, 4.0), "each cut is a headful — slightly more than one genome length — so every progeny genome\n"
                         "carries the same genes beginning at a different point (circular permutation) and repeats\n"
                         "3–6 kbp at its two ends (terminal redundancy)", size="tiny", ha="left", color=MUT)
# the packaging motor
mx, my = 24.6, 2.3
ax.add_patch(Polygon(np.array([[-0.9, -0.8], [-0.9, 0.5], [0, 1.1], [0.9, 0.5], [0.9, -0.8], [0, -1.3]]) + [mx, my],
                     closed=True, facecolor=P.fill("virus"), edgecolor=P.edge("virus"), lw=1.0, zorder=8))
ax.add_patch(Circle((mx, my - 1.35), 0.3, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.8, zorder=9))
ax.plot([mx, mx + 2.6], [my - 1.75, my - 1.75], color=col, lw=2.2, zorder=7)
bio.arrow(ax, (mx + 1.3, my - 1.2), (mx + 0.5, my - 1.2), kind="process", lw=1.0, head=0.18)
bio.label(ax, (mx + 1.5, my + 0.3), "terminase gp17/gp16: an ATP-driven motor,\nup to 2000 bp s⁻¹, against tens of\n"
                                    "atmospheres of internal pressure", size="tiny", ha="left", color=MUT)
