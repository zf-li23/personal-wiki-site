# The excision repair pathways compared on the same stretch of DNA (damaged strand on top, template
# strand below; schematic, lengths not to scale). Direct reversal: the lesion is repaired in place.
# BER: one base removed, one nucleotide replaced. NER: dual incision around a helix-distorting lesion,
# an oligonucleotide replaced. MMR: excision from a strand signal (hemimethylated GATC or nick) through
# the mismatch. Resynthesized DNA is light blue; lesions are yellow; incisions are triangles.
import numpy as np
import wikibio as bio
from wikibio import molbio as MB

P = bio.P
fig, ax = bio.canvas(21, 12.2)
half = 0.2
x0, x1 = 5.6, 19.6
xs = np.arange(x0 + 0.1, x1, 0.2)
seq = MB.sequence(len(xs), "repair")
comp = MB.complement(seq)


def cut(x, y, up=True):
    s = 0.17
    yy = y + (0.42 if up else -0.42)
    d = -1 if up else 1
    ax.fill([x - s, x + s, x], [yy, yy, yy + d * 0.3], color=P.edge("negative"), zorder=20, lw=0)


def lesion(x, y, w=0.36):
    ax.add_patch(__import__("matplotlib.patches", fromlist=["x"]).FancyBboxPatch(
        (x - w / 2, y - 0.14), w, 0.28, boxstyle="round,pad=0.02,rounding_size=0.1",
        facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=21))


def row(y, name, detail, new=None, lesion_x=None, cuts=(), signal=None, patch_text=None, bend=False):
    top, bot = MB.track(xs, y + half), MB.track(xs, y - half)
    MB.ladder(ax, top, bot, seq)
    MB.backbone(ax, [(x0, y - half), (x1, y - half)], "dna")
    if new:
        a, b = new
        MB.backbone(ax, [(x0, y + half), (a, y + half)], "dna")
        MB.backbone(ax, [(a, y + half), (b, y + half)], "dna", shade="fill")
        MB.backbone(ax, [(b, y + half), (x1, y + half)], "dna")
        ax.plot([a, a, b, b], [y + 0.5, y + 0.62, y + 0.62, y + 0.5], color=P.muted(), lw=0.9, zorder=19)
        bio.label(ax, ((a + b) / 2, y + 0.9), patch_text, size="tiny", color=P.muted())
    else:
        MB.backbone(ax, [(x0, y + half), (x1, y + half)], "dna")
    if lesion_x is not None:
        lesion(lesion_x, y + half + 0.02)
    for c in cuts:
        cut(c, y + half)
    if signal:
        sx, stext = signal
        ax.plot([sx], [y + half + 0.34], marker="o", ms=5, color=P.edge("protein"), zorder=22)
        bio.label(ax, (sx, y + half + 0.72), stext, size="tiny", color=P.edge("protein"))
    bio.label(ax, (0.4, y + 0.28), name, size="small", bold=True, ha="left")
    bio.label(ax, (0.4, y - 0.3), detail, size="tiny", color=P.muted(), ha="left")
    bio.label(ax, (x0 - 0.3, y + half), "5′", size="tiny", bold=True)
    bio.label(ax, (x1 + 0.3, y + half), "3′", size="tiny", bold=True)


row(10.6, "Direct reversal", "photolyase, MGMT, AlkB", lesion_x=12.6)
bio.arrow(ax, (12.6, 11.55), (12.6, 11.15), kind="process", color=P.edge("highlight"))
bio.label(ax, (14.6, 11.55), "lesion reversed in place, no excision", size="tiny", color=P.muted())
row(8.0, "Base excision", "glycosylase, APE1, Pol β, ligase III", new=(12.5, 12.75), lesion_x=12.62,
    cuts=(12.5,), patch_text="1 nt (long patch 2–10 nt)")
row(5.4, "Nucleotide excision", "UvrABC; XPC, TFIIH, XPG, XPF–ERCC1", new=(10.6, 15.2), lesion_x=13.6,
    cuts=(10.6, 15.2), patch_text=r"12–13 nt ($\it{E.\ coli}$), 24–32 nt (human)")
row(2.8, "Mismatch repair", "MutS, MutL, MutH; MutSα, MutLα, EXO1", new=(7.4, 17.6), lesion_x=16.8,
    cuts=(7.4,), signal=(7.0, "GATC (CH₃ on template) or nick"), patch_text="up to ~1 kb, from the strand signal through the mismatch")
bio.label(ax, (16.8, 2.8 - half - 0.42), "mismatch", size="tiny", color=P.edge("highlight"))
# legend
ly = 0.7
items = [(P.edge("dna"), "original DNA"), (P.fill("dna"), "resynthesized")]
for k, (col, text) in enumerate(items):
    xx = 5.2 + k * 3.4
    ax.plot([xx, xx + 0.6], [ly, ly], color=col, lw=bio.core.LINE * 2.2, solid_capstyle="round")
    bio.label(ax, (xx + 0.8, ly), text, size="small", ha="left")
lesion(12.2, ly)
bio.label(ax, (12.55, ly), "site of the lesion or wrong base", size="small", ha="left")
cut(18.9, ly - 0.27)
bio.label(ax, (19.25, ly), "incision", size="small", ha="left")
