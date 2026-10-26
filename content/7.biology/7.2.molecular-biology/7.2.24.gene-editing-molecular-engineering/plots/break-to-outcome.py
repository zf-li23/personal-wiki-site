# A targeted double-strand break and what the cell does with it.
# A: the two repair routes - end joining (all phases, indels, knockout) and homology-directed repair
#    (S/G2 only, needs a donor, gives the designed sequence).
# B: why a break is made at all: HDR frequency against the cut rate, with the 1e-6..1e-3 band of spontaneous
#    gene targeting marked.
# C: the time course of Eq. 24.1 for p_HDR = 0.15: unmodified sites decay exponentially while indel and HDR
#    products accumulate in a fixed ratio.
# D: an illustrative indel spectrum at one site, dominated by deletions whose endpoints lie at short
#    microhomologies, which is why outcomes are predictable from sequence.
import numpy as np
import wikibio as bio
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(25.0, 9.2)

NEG = P.edge("negative")
BP = 0.17


def duplex(x0, n, y, token="dna", gap=0.3):
    x1 = x0 + n * BP
    ax.plot([x0, x1], [y, y], color=P.edge(token), lw=2.0, zorder=6)
    ax.plot([x0, x1], [y - gap, y - gap], color=P.edge("dna2"), lw=2.0, zorder=6)
    return x1


# ----------------------------------------------------------------- A: the two routes
bio.panel(ax, "A", (0.1, 9.0))
bio.label(ax, (4.6, 9.0), "One break, two repair routes", size="small", bold=True)
y = 7.6
duplex(1.4, 14, y)
duplex(4.2, 14, y)
bio.label(ax, (3.9, y + 0.5), "double-strand break", size="tiny", color=NEG)
ax.plot([3.95, 3.95], [y + 0.25, y - 0.55], color=NEG, lw=1.6, zorder=12)

# end joining branch
bio.arrow(ax, (3.0, y - 0.75), (2.2, y - 1.6), kind="process")
bio.box(ax, (2.3, y - 2.2), 3.8, 1.0, token="negative",
        text="end joining\nall cell-cycle phases", size="tiny", radius=0.12)
duplex(1.0, 10, y - 3.3)
duplex(2.9, 9, y - 3.3)
bio.label(ax, (2.75, y - 3.75), "✕", size="small", color=NEG)
bio.label(ax, (2.6, y - 4.3), "small insertions and deletions\n→ frameshift, knockout", size="tiny",
          color=P.muted())

# HDR branch
bio.arrow(ax, (5.0, y - 0.75), (6.2, y - 1.6), kind="process")
bio.box(ax, (6.6, y - 2.2), 4.2, 1.0, token="positive",
        text="homology-directed repair\nS and G2 only, needs a donor", size="tiny", radius=0.12)
duplex(5.2, 20, y - 3.3)
ax.add_patch(bio.core.Circle((8.0, y - 3.15), 0.2, facecolor=P.fill("highlight"),
                             edgecolor=P.edge("highlight"), lw=0.9, zorder=12))
bio.label(ax, (8.0, y - 3.15), "★", size="tiny", color=P.on_fill(), zorder=13)
bio.label(ax, (7.4, y - 4.3), "the designed sequence from the donor", size="tiny", color=P.muted())
bio.box(ax, (8.3, y - 1.1), 2.6, 0.55, token="mrna", text="donor", size="tiny", radius=0.08)

# ----------------------------------------------------------------- B: why cut at all
bio.panel(ax, "B", (11.3, 9.0))
bio.label(ax, (14.6, 9.0), "Why a break is made", size="small", bold=True)
kcut = np.logspace(-4, 0.3, 200)
hdr = 0.15 * (1 - np.exp(-kcut * 48))                   # 48 h of exposure, p_HDR = 0.15
pl = Q.Plot(ax, (12.9, 5.8, 3.4, 2.5), xlim=(1e-4, 2), ylim=(1e-7, 0.5), xlog=True, ylog=True,
            xlabel="cutting rate $k_{\\mathrm{cut}}$ / h$^{-1}$", ylabel="edited fraction",
            xticks=[(1e-4, "$10^{-4}$"), (1e-2, "$10^{-2}$"), (1, "1")],
            yticks=[(1e-7, "$10^{-7}$"), (1e-4, "$10^{-4}$"), (1e-1, "$10^{-1}$")], ylabel_offset=1.25)
pl.band(kcut, np.full_like(kcut, 1e-6), np.full_like(kcut, 1e-3), token="neutral", alpha=0.3)
pl.text(3e-3, 3e-5, "spontaneous gene targeting", size="tiny", color=P.muted())
pl.line(kcut, hdr, "positive", lw=1.8)
pl.text(2e-2, 0.2, "with a nuclease", size="tiny", color=P.edge("positive"))

# ----------------------------------------------------------------- C: the time course
bio.panel(ax, "C", (11.3, 4.6))
bio.label(ax, (14.6, 4.6), "Equation 24.1", size="small", bold=True)
t = np.linspace(0, 72, 400)
k, p_hdr = 0.06, 0.15
u = np.exp(-k * t)
pl = Q.Plot(ax, (12.9, 1.5, 3.4, 2.4), xlim=(0, 72), ylim=(0, 1.02),
            xlabel="$t$ / h", ylabel="fraction of cells", xticks=[0, 24, 48, 72], yticks=[0, 0.5, 1],
            ylabel_offset=0.85)
pl.line(t, u, "neutral", text="unmodified", at=0.32, dy=0.45)
pl.line(t, (1 - p_hdr) * (1 - u), "negative", text="indels", at=0.7, dy=-0.45)
pl.line(t, p_hdr * (1 - u), "positive", text="HDR", at=0.86, dy=0.4)
bio.label(ax, (14.6, 0.3), "the dose sets the efficiency, the repair\ncompetition sets the precision",
          size="tiny", color=P.muted())

# ----------------------------------------------------------------- D: indel spectrum
bio.panel(ax, "D", (17.4, 9.0))
bio.label(ax, (21.4, 9.0), "The indel spectrum at one site is reproducible", size="small", bold=True)
rng = np.random.default_rng(3)
sizes = np.arange(-20, 11)
# illustrative spectrum: a 1 bp insertion, a dominant microhomology-mediated deletion, a tail of deletions
freq = 0.9 * np.exp(-((sizes + 1) ** 2) / 1.2) + 1.5 * np.exp(-((sizes + 7) ** 2) / 1.0) \
    + 0.35 * np.exp(-((sizes + 13) ** 2) / 2.0) + 0.1 * np.exp(-(sizes ** 2) / 30.0)
freq[sizes > 1] *= 0.15
freq = freq / freq.sum()
pl = Q.Plot(ax, (19.0, 4.7, 5.2, 3.6), xlim=(-21, 11), ylim=(0, 0.42),
            xlabel="insertion (+) or deletion (−) / bp", ylabel="fraction of edited alleles",
            xticks=[-20, -10, 0, 10], yticks=[0, 0.2, 0.4], ylabel_offset=1.0)
for s, f in zip(sizes, freq):
    tok = "positive" if s == 1 else "negative"
    pl.bars([s - 0.45, s + 0.45], [f], token=tok)
pl.text(-7, 0.37, "−7: deletion between two\n3 bp microhomologies", size="tiny", color=P.ink())
pl.text(2.0, 0.22, "+1 insertion:\nblunt-end\nfill-in", size="tiny", color=P.edge("positive"))

bio.label(ax, (21.4, 3.5), "two 3 bp microhomologies flanking the cut dictate the dominant deletion",
          size="tiny", color=P.muted())
seq = "GCTTAG" + "CCAGT" + "GCTTAG" + "ACGT"
x = 18.4
for i, ch in enumerate(seq):
    mh = (3 <= i <= 5) or (14 <= i <= 16)
    tok = "highlight" if mh else "neutral"
    ax.add_patch(bio.core.Circle((x + i * 0.32, 2.4), 0.15, facecolor=P.fill(tok), edgecolor=P.edge(tok),
                                 lw=0.6, zorder=8))
    bio.label(ax, (x + i * 0.32, 2.4), ch, size="tiny", color=P.on_fill(), zorder=9)
ax.plot([x + 10.5 * 0.32, x + 10.5 * 0.32], [2.9, 1.9], color=NEG, lw=1.5, zorder=12)
bio.label(ax, (x + 10.5 * 0.32, 3.05), "cut", size="tiny", color=NEG)
bio.label(ax, (x + 4.2 * 0.32, 1.55), "microhomology", size="tiny", color=P.edge("highlight"))
bio.label(ax, (x + 15.2 * 0.32, 1.55), "microhomology", size="tiny", color=P.edge("highlight"))
bio.arrow(ax, (x + 4.5 * 0.32, 1.9), (x + 14.8 * 0.32, 1.9), kind="link", bend=-0.3, color=P.edge("highlight"))
bio.label(ax, (x + 9.8 * 0.32, 0.9), "annealing of the two copies deletes the 7 bp between them",
          size="tiny", color=P.muted())
