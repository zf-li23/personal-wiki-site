# How Cas9 finds a target and commits to cutting it.
# A: the search - three-dimensional collisions, millisecond dwells, pausing only at a PAM.
# B: directional interrogation - unwinding starts at the PAM, the guide pairs from the PAM-proximal end and the
#    growing RNA-DNA hybrid displaces the non-target strand as an R loop; HNH and RuvC then cut.
# C: the free-energy ladder of R-loop propagation: each matched base pair gains about 2 kT, a mismatch costs
#    about 4 kT, so a PAM-proximal (seed) mismatch raises the whole ladder while a PAM-distal one does not.
# D: cleavage against the position of a single mismatch, computed from the ladder as the splitting probability
#    of a one-dimensional walk, P = 1 / (1 + sum_i exp(G_i / kT)).
# E: cloning a guide - two annealed oligonucleotides into a type IIS-cut vector.
import numpy as np
import wikibio as bio
from wikibio import genetics as G
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(25.0, 13.4)

NEG = P.edge("negative")
N, SEED = 20, 10
DG_SEED, DG_LATE, DG_MISMATCH = -0.15, -1.6, 4.0   # kT per base pair; the seed is nearly thermoneutral


def ladder(mismatch=None):
    """Cumulative free energy G_i after i paired positions, counted from the PAM.

    Unwinding the duplex almost cancels the pairing energy over the first SEED base pairs, so the
    landscape is flat there and steeply downhill afterwards; a mismatch adds DG_MISMATCH at its position.
    """
    steps = np.array([DG_SEED if j < SEED else DG_LATE for j in range(N)])
    if mismatch is not None:
        steps[mismatch - 1] += DG_MISMATCH
    return np.concatenate([[0.0], np.cumsum(steps)])


def commit(mismatch=None):
    """Probability of completing the R loop before dissociating (1-D splitting probability)."""
    g = ladder(mismatch)
    return 1.0 / (1.0 + np.sum(np.exp(g[:-1])))


# ----------------------------------------------------------------- A: the search
bio.panel(ax, "A", (0.1, 13.2))
bio.label(ax, (5.6, 13.2), "The search is for PAMs, not for protospacers", size="small", bold=True)
yA = 11.4
ax.plot([1.2, 10.6], [yA, yA], color=P.edge("dna"), lw=2.2, zorder=5)
ax.plot([1.2, 10.6], [yA - 0.3, yA - 0.3], color=P.edge("dna2"), lw=2.2, zorder=5)
pam_x = [2.4, 4.3, 6.1, 8.9]
for i, x in enumerate(pam_x):
    tok = "highlight" if i < 3 else "positive"
    bio.box(ax, (x, yA - 0.15), 0.62, 0.78, token=tok, text="NGG", size="tiny", radius=0.05, zorder=9)
for i, x in enumerate(pam_x[:3]):
    bio.shape(ax, bio.blob((x, yA + 0.95), 0.55, 0.36, wobble=0.05, seed=i), token="enzyme", zorder=8)
    bio.label(ax, (x, yA + 1.45), "ms", size="tiny", color=P.muted())
bio.shape(ax, bio.blob((pam_x[3], yA + 0.95), 0.75, 0.46, wobble=0.05, seed=9), token="enzyme", zorder=8)
bio.label(ax, (pam_x[3], yA + 1.5), "complete match → cleavage", size="tiny",
          color=P.edge("positive"))
bio.label(ax, (5.9, yA - 1.0), "$\\approx 10^{8}$ NGG sites in a human genome; each is interrogated and nearly all"
          " are abandoned", size="tiny", color=P.muted())

# ----------------------------------------------------------------- B: the R loop
bio.panel(ax, "B", (0.1, 9.4))
bio.label(ax, (5.6, 9.4), "Directional interrogation and the R loop", size="small", bold=True)
for k, (frac, text) in enumerate(((0.0, "PAM recognized"), (0.45, "R loop propagating"), (1.0, "hybrid complete → cut"))):
    y = 8.2 - k * 1.95
    x0, x1 = 1.4, 8.4
    ax.plot([x0, x1], [y, y], color=P.edge("dna2"), lw=2.0, zorder=5)
    bio.box(ax, (x1 + 0.45, y + 0.2), 0.62, 0.72, token="highlight", text="NGG", size="tiny", radius=0.05, zorder=9)
    xo = x1 - frac * (x1 - x0)
    if frac > 0:                                   # displaced non-target strand bulges out
        xs = np.linspace(xo, x1, 40)
        ax.plot(xs, y + 0.42 + 0.3 * np.sin(np.pi * (xs - xo) / (x1 - xo)), color=P.edge("dna"), lw=1.8, zorder=6)
        ax.plot([x0, xo], [y + 0.42, y + 0.42], color=P.edge("dna"), lw=1.8, zorder=6)
        ax.plot([xo, x1], [y + 0.08, y + 0.08], color=P.edge("rna"), lw=2.2, zorder=7)
        ax.plot([x0, xo], [y + 0.08, y + 0.08], color=P.edge("rna"), lw=2.2, dashes=(3, 2), zorder=7)
    else:
        ax.plot([x0, x1], [y + 0.42, y + 0.42], color=P.edge("dna"), lw=1.8, zorder=6)
        ax.plot([x0, x1], [y + 0.08, y + 0.08], color=P.edge("rna"), lw=2.2, dashes=(3, 2), zorder=7)
    bio.label(ax, (9.9, y + 0.25), text, size="tiny", ha="left", color=P.ink())
    if frac == 1.0:
        ax.plot([x1 - 3 * (x1 - x0) / 20, x1 - 3 * (x1 - x0) / 20], [y + 0.7, y - 0.35], color=NEG, lw=1.6,
                zorder=14)
        bio.label(ax, (x1 - 3 * (x1 - x0) / 20 - 0.1, y - 0.65), "HNH / RuvC", size="tiny", color=NEG, ha="right")
bio.label(ax, (4.9, 3.2), "guide RNA (orange), target strand paired with it, non-target strand displaced (blue)",
          size="tiny", color=P.muted())

# ----------------------------------------------------------------- C: the free-energy ladder
bio.panel(ax, "C", (12.2, 13.2))
bio.label(ax, (16.4, 13.2), "The ladder of R-loop propagation", size="small", bold=True)
i = np.arange(N + 1)
pl = Q.Plot(ax, (14.0, 8.8, 4.4, 3.5), xlim=(0, N), ylim=(-20, 8),
            xlabel="base pairs paired, counted from the PAM", ylabel="$G$ / $k_{\\mathrm{B}}T$",
            xticks=[0, 5, 10, 15, 20], yticks=[-16, -8, 0, 8], ylabel_offset=1.1)
pl.hline(0)
pl.line(i, ladder(), "positive", text="perfect match", at=0.3, dy=-0.55)
pl.line(i, ladder(mismatch=3), "negative", text="seed mismatch", at=0.42, dy=0.5)
pl.line(i, ladder(mismatch=18), "neutral", text="PAM-distal mismatch", at=0.8, dy=-0.5)
pl.span(0, 10, token="highlight", text="seed", strength=0.75, text_y=pl.box[1] + 0.15)
bio.label(ax, (16.4, 7.65), "a mismatch costs $\\approx 4\\,k_{\\mathrm{B}}T$; paid early it stalls the loop,"
          " paid late it is paid after commitment", size="tiny", color=P.muted())

# ----------------------------------------------------------------- D: cleavage vs mismatch position
bio.panel(ax, "D", (12.2, 7.0))
bio.label(ax, (16.4, 7.0), "Cleavage against the position of one mismatch", size="small", bold=True)
pos = np.arange(1, N + 1)
rel = np.array([commit(m) for m in pos]) / commit()
pl = Q.Plot(ax, (14.0, 1.6, 4.4, 4.0), xlim=(0, N + 1), ylim=(1e-3, 2.0), ylog=True,
            xlabel="position of the mismatch (1 = PAM-proximal)", ylabel="relative cleavage",
            xticks=[1, 5, 10, 15, 20],
            yticks=[(1e-3, "$10^{-3}$"), (1e-2, "$10^{-2}$"), (1e-1, "$10^{-1}$"), (1, "1")], ylabel_offset=1.15)
pl.bars(np.append(pos - 0.42, N + 0.58), rel, token="rna")
pl.hline(1.0, text="perfect match", side="left")
bio.label(ax, (16.4, 0.45), "the same ladder explains both the specificity and the off-target spectrum"
          " (Section 24.8)", size="tiny", color=P.muted())

# ----------------------------------------------------------------- E: cloning a guide
bio.panel(ax, "E", (19.6, 7.0))
bio.label(ax, (22.6, 7.0), "Cloning a guide", size="small", bold=True)
G.construct(ax, 20.2, 5.4, [
    {"kind": "promoter", "text": "U6", "width": 0.9},
    {"kind": "cds", "text": "BbsI", "width": 0.8, "token": "negative"},
    {"kind": "cds", "text": "scaffold", "width": 1.5, "token": "rna"},
    {"kind": "terminator", "text": "TTTTTT", "width": 0.8},
], unit=0.5)
bio.label(ax, (22.6, 4.5), "cut the vector with a type IIS enzyme\n(7.2.5): the overhangs are designed, not found",
          size="tiny", color=P.muted())
for k, (lab, tok) in enumerate((("5′-CACCG  N$_{20}$", "dna"), ("3′-  N$_{20}$  CAAA-5′", "dna2"))):
    bio.label(ax, (20.3, 3.4 - k * 0.5), lab, size="tiny", ha="left", color=P.edge(tok))
bio.label(ax, (22.6, 2.3), "two annealed oligonucleotides ligate into the gap;\n"
          "a library of $10^{5}$ guides is one array synthesis", size="tiny", color=P.ink())
bio.box(ax, (22.6, 1.0), 4.6, 0.8, token="positive", text="new target = new 20-mer", size="tiny", radius=0.12)
