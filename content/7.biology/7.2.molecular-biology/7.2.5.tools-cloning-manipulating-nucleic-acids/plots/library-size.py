# How many clones make a complete genomic library? Clarke-Carbon formula N = ln(1 - P) / ln(1 - f), f = insert
# size / genome size, for a 99 % chance that any given sequence is present (P = 0.99), against insert size for
# four genomes (E. coli 4.6 Mb, S. cerevisiae 12 Mb, D. melanogaster 140 Mb, human 3.1 Gb). The shaded bands
# are the insert ranges of the main vector types. For the human genome: about 7e5 lambda clones (20 kb) or
# 1e5 BAC clones (150 kb).
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(16.0, 9.0)
a = C.axes_at(ax, (1.8, 1.4, 13.4, 6.8))
ins = np.logspace(np.log10(2e3), np.log10(2e6), 300)
for G, name, tok in [(4.6e6, "E. coli", "bacterium"), (1.2e7, "S. cerevisiae", "enzyme"),
                     (1.4e8, "D. melanogaster", "protein"), (3.1e9, "H. sapiens", "receptor")]:
    f = ins / G
    ok = f < 0.5
    N = np.log(0.01) / np.log1p(-f[ok])
    a.loglog(ins[ok], N, color=C.line(tok), lw=2.0)
    a.text(2.3e3, N[0] * (0.45 if name == "E. coli" else 1.25), name, fontsize=bio.core.FONT["tiny"], color=C.line(tok), style="italic")
bands = [(2e3, 1e4, "plasmid"), (9e3, 2.3e4, "λ"), (3.5e4, 4.5e4, "cosmid,\nfosmid"), (1e5, 3e5, "BAC"), (2e5, 2e6, "YAC")]
for k, (lo, hi, name) in enumerate(bands):
    a.axvspan(lo, hi, ymin=0, ymax=1, color=P.fill("neutral"), alpha=0.25 if k % 2 == 0 else 0.4, lw=0)
    a.text(np.sqrt(lo * hi), 4e7 if name != "YAC" else 4e7, name, ha="center", va="top",
           fontsize=bio.core.FONT["tiny"], color=P.ink())
for x, G in [(2e4, 3.1e9), (1.5e5, 3.1e9)]:
    N = np.log(0.01) / np.log1p(-x / G)
    a.plot([x], [N], "o", ms=5, mfc=P.fill("receptor"), mec=C.line("receptor"))
    a.text(x * 1.15, N * 1.4, f"{N:.1e}".replace("e+0", "×10^").replace("×10^5", "×10⁵").replace("×10^4", "×10⁴"),
           fontsize=bio.core.FONT["tiny"], color=P.ink())
a.set_xlim(2e3, 2e6)
a.set_ylim(1, 1e8)
a.set_xticks([1e4, 1e5, 1e6], ["10 kb", "100 kb", "1 Mb"])
C.style_axes(a, "insert size", "clones needed (P = 0.99)")
bio.label(ax, (1.0, 8.7), "Clarke–Carbon: N = ln(1 − P) / ln(1 − f)", size="normal", bold=True, ha="left")
