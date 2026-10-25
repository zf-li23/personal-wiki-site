# MicroRNA biogenesis and target recognition.
# A: canonical pathway. Pol II transcribes a capped, polyadenylated pri-miRNA containing a hairpin; in the
# nucleus the Microprocessor (Drosha with DGCR8) cuts at the base of the stem, releasing a 60-70 nt pre-miRNA
# with a 2-nt 3' overhang; Exportin-5 with Ran-GTP exports it; in the cytoplasm Dicer (with TRBP) cuts off the
# loop, leaving a ~22-nt duplex; one strand (the guide, usually the one whose 5' end is less stably paired) is
# loaded into Argonaute, the other (passenger, miR*) is discarded; miRISC with GW182 (TNRC6) finds target
# mRNAs. Mirtrons bypass Drosha: they are excised by the spliceosome and debranched.
# B: anatomy of a miRNA bound to Argonaute: nucleotide 1 is held in the MID pocket and does not pair; the seed
# (nucleotides 2-8) pairs with the target; the central region (9-12) is unpaired in most animal sites; the
# supplementary region (13-16) can add pairing; the tail (17-22) is buried. Site types ranked by efficacy:
# 8mer (seed + match at 8 + A opposite position 1) > 7mer-m8 > 7mer-A1 > 6mer.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 10.0)

# --- A ---
bio.panel(ax, "A", (0.1, 9.85))
ax.add_patch(bio.core.FancyBboxPatch((0.4, 0.6), 6.6, 8.4, boxstyle="round,pad=0,rounding_size=0.4",
                                     facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=1.2, zorder=0, alpha=0.35))
bio.label(ax, (3.7, 8.6), "Nucleus", size="small", bold=True, color=P.edge("nucleus"))
bio.label(ax, (10.6, 8.6), "Cytoplasm", size="small", bold=True)
steps = [
    ((3.7, 7.5), "miRNA gene → Pol II", "dna"),
    ((3.7, 5.8), "pri-miRNA (cap, poly(A), hairpin)", "mrna"),
    ((3.7, 4.1), "pre-miRNA, 60–70 nt hairpin", "mrna"),
    ((10.6, 4.1), "Dicer + TRBP: ~22-nt duplex", "enzyme"),
    ((10.6, 5.8), "Argonaute loading: guide kept", "protein"),
    ((10.6, 7.5), "miRISC (Ago + GW182) → targets", "receptor"),
]
for (xy, text, tok) in steps:
    bio.box(ax, xy, 5.6, 0.95, token=tok, text=text, size="tiny", radius=0.12)
arrows = [((3.7, 7.0), (3.7, 6.3), ""), ((3.7, 5.3), (3.7, 4.6), "Drosha + DGCR8"),
          ((6.5, 4.1), (7.8, 4.1), ""), ((10.6, 4.6), (10.6, 5.3), ""), ((10.6, 6.3), (10.6, 7.0), "")]
for a, b, t in arrows:
    bio.arrow(ax, a, b, kind="process")
    if t:
        bio.label(ax, (a[0] + 0.25, (a[1] + b[1]) / 2), t, size="tiny", ha="left", color=P.muted())
bio.label(ax, (7.15, 4.45), "Exportin-5", size="tiny", color=P.muted())
bio.label(ax, (7.15, 3.75), "Ran-GTP", size="tiny", color=P.muted())
bio.label(ax, (3.7, 2.7), "mirtrons: spliceosome + debranching", size="tiny", color=P.muted())
bio.label(ax, (3.7, 2.25), "replace Drosha", size="tiny", color=P.muted())
bio.label(ax, (10.6, 3.05), "passenger strand (miR*) degraded", size="tiny", color=P.muted())
bio.label(ax, (10.6, 8.15), "", size="tiny")
bio.label(ax, (10.6, 1.6), "plants: near-perfect pairing → slicing", size="tiny", color=P.muted())
bio.label(ax, (10.6, 1.15), "animals: seed pairing in 3′ UTR → deadenylation, decay", size="tiny", color=P.muted())

# --- B ---
bio.panel(ax, "B", (14.4, 9.85))
mir = "UGAGGUAGUAGGUUGUAUAGUU"  # let-7a
x0, yg, dx = 15.0, 6.2, 0.46
regions = [(1, 1, "neutral", "anchor"), (2, 8, "highlight", "seed 2–8"), (9, 12, "neutral", "central"),
           (13, 16, "positive", "supplementary"), (17, 22, "neutral", "tail")]
for a, b, tok, name in regions:
    xa, xb = x0 + (a - 1) * dx - 0.2, x0 + (b - 1) * dx + 0.2
    bio.box(ax, ((xa + xb) / 2, yg - 0.75), xb - xa, 0.35, token=tok, radius=0.05, zorder=3)
    bio.label(ax, ((xa + xb) / 2, yg - 1.25), name, size="tiny", color=P.muted())
for i, ch in enumerate(mir):
    bio.label(ax, (x0 + i * dx, yg), ch, size="small", bold=(1 <= i <= 7), color=P.edge("trna"))
    bio.label(ax, (x0 + i * dx, yg - 0.75), str(i + 1), size="tiny", color=P.on_fill(), zorder=6)
bio.label(ax, (x0 - 0.5, yg), "5′", size="tiny", bold=True)
bio.label(ax, (x0 + 22 * dx - 0.1, yg), "3′", size="tiny", bold=True)
bio.label(ax, (x0 + 22 * dx + 0.4, yg), "let-7a (guide)", size="tiny", ha="left", color=P.edge("trna"))
# target: complementary to seed and supplementary, A opposite position 1
comp = {"A": "U", "U": "A", "G": "C", "C": "G"}
tgt = []
for i, ch in enumerate(mir):
    if i == 0:
        tgt.append("A")
    elif 1 <= i <= 7 or 12 <= i <= 15:
        tgt.append(comp[ch])
    else:
        tgt.append("N")
yt = yg + 1.3
for i, ch in enumerate(tgt):
    bio.label(ax, (x0 + i * dx, yt), ch, size="small", color=P.edge("mrna"), bold=(ch != "N"))
    if 1 <= i <= 7 or 12 <= i <= 15:
        ax.plot([x0 + i * dx] * 2, [yg + 0.3, yt - 0.3], color=P.muted(), lw=0.8)
bio.label(ax, (x0 - 0.5, yt), "3′", size="tiny", bold=True)
bio.label(ax, (x0 + 22 * dx - 0.1, yt), "5′", size="tiny", bold=True)
bio.label(ax, (x0 + 22 * dx + 0.4, yt), "target 3′ UTR", size="tiny", ha="left", color=P.edge("mrna"))
bio.label(ax, (x0, yt + 0.6), "t1 A", size="tiny", color=P.muted())
# site types
yy = 3.2
bio.label(ax, (15.0, yy + 0.6), "Site types (target positions opposite miRNA 1–8)", size="small", bold=True, ha="left")
sites = [("8mer", "A + 2–8", 8), ("7mer-m8", "2–8", 7), ("7mer-A1", "A + 2–7", 6), ("6mer", "2–7", 5)]
for k, (name, desc, n) in enumerate(sites):
    y = yy - 0.55 * k
    bio.label(ax, (15.0, y), name, size="tiny", bold=True, ha="left")
    bio.label(ax, (16.6, y), desc, size="tiny", ha="left")
    eff = [1.0, 0.7, 0.5, 0.25][k]
    ax.add_patch(bio.core.FancyBboxPatch((18.4, y - 0.15), 4.0 * eff, 0.3, boxstyle="square,pad=0",
                                         facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.7))
bio.label(ax, (22.6, yy - 0.8), "typical efficacy (relative)", size="tiny", color=P.muted(), ha="left")
