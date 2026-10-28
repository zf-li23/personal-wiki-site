# Fine mapping after conjugation: the position of the second crossover decides which donor markers are kept
import wikibio as bio
from wikibio import transmission as T

P = bio.P
fig, ax = bio.canvas(22, 10)
loc = [0.25, 0.5, 0.8]
names_d = ["met+", "arg+", "leu+"]
names_r = ["met", "arg", "leu"]
rows = [(r"left of $\it{met}$", 0.12, 628), (r"between $\it{met}$ and $\it{arg}$", 0.37, 210), (r"between $\it{arg}$ and $\it{leu}$", 0.65, 160)]
for k, (where, xc, n) in enumerate(rows):
    y = 8.2 - k * 3.0
    x0, x1 = 1.0, 9.0
    T.chromatid_bar(ax, x0 + 0.8, x1 - 0.8, y + 0.55, [(0, 1, "dna")], height=0.24,
                    loci=[((f * (x1 - x0) - 0.8) / (x1 - x0 - 1.6), a) for f, a in zip(loc, names_d)], label_pos="above")
    T.chromatid_bar(ax, x0, x1, y - 0.55, [(0, 1, "receptor")], height=0.24,
                    loci=list(zip(loc, names_r)), label_pos="below")
    for xx in (x0 + xc * (x1 - x0), x0 + 0.9 * (x1 - x0)):
        ax.plot([xx - 0.18, xx + 0.18], [y + 0.42, y - 0.42], color=P.ink(), lw=1.4)
        ax.plot([xx - 0.18, xx + 0.18], [y - 0.42, y + 0.42], color=P.ink(), lw=1.4)
    bio.label(ax, (0.5, y), str(k + 1), size="small", bold=True)
    bio.arrow(ax, (9.6, y), (10.8, y))
    # recombinant chromosome
    cut = xc
    segs = [(0, cut, "receptor"), (cut, 0.9, "dna"), (0.9, 1, "receptor")]
    T.chromatid_bar(ax, 11.2, 19.2, y, segs, height=0.26, loci=[(f, "") for f in loc], label_pos=None)
    kept = ["met+" if cut < 0.25 else "met", "arg+" if cut < 0.5 else "arg", "leu+"]
    for f, a_ in zip(loc, kept):
        bio.label(ax, (11.2 + f * 8.0, y + 0.25), T.allele(a_), size="small", va="bottom")
    bio.label(ax, (19.5, y), f"{n}", size="normal", ha="left")
    bio.label(ax, (15.2, y - 0.6), f"second crossover {where}", size="tiny", color=P.muted())
bio.label(ax, (5.0, 9.6), "Hfr fragment (blue) over the F- chromosome (pink)", size="small")
bio.label(ax, (15.2, 9.6), r"$\it{leu}^{+}$ recombinant", size="small")
bio.label(ax, (19.5, 9.6), "number", size="small", ha="left", color=P.muted())
