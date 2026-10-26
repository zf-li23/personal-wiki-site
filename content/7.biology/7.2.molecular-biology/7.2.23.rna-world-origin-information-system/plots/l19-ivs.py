# L-19 IVS: a ribozyme that satisfies the definition of an enzyme, and what ribozyme catalysis is worth.
# A: origin - the excised 414-nt group I intron cyclizes and loses 19 nt from its 5' end, leaving a linear
#    395-nt RNA that keeps the guanosine site and part of the internal guide sequence but has no splice sites.
# B: the catalytic cycle - (C)5 binds the guide sequence, the 3'-OH of the terminal G attacks it, giving a
#    covalent ribozyme-C intermediate and releasing (C)4; a second oligonucleotide takes the C, giving (C)6
#    and free ribozyme. The ribozyme is unchanged: it is a catalyst, not a substrate.
# C: Michaelis-Menten plot with k_cat = 0.028 /s (the measured 100 turnovers per hour) and K_m = 30 uM (the
#    measured value is a few tens of uM); together they reproduce the measured k_cat/K_m ~ 1e3 /M/s.
# D: specificity constants on a logarithmic scale, from the uncatalysed reaction to the diffusion limit.
import numpy as np
import wikibio as bio
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(25.0, 12.0)

# ----------------------------------------------------------------- A: origin of L-19 IVS
bio.panel(ax, "A", (0.1, 11.8))
bio.label(ax, (5.6, 11.8), "Where L-19 IVS comes from", size="small", bold=True)
yA = 9.6
for x, w, text, token in ((2.4, 4.2, "excised intron, 414 nt\n(G added by splicing at its 5′ end)", "rna"),
                          (8.8, 3.6, "circular forms", "rna")):
    bio.box(ax, (x, yA), w, 1.1, token=token, text=text, size="tiny", radius=0.12)
bio.arrow(ax, (4.6, yA), (7.0, yA), kind="process")
bio.label(ax, (5.8, yA + 0.5), "cyclization", size="tiny", color=P.muted())
bio.arrow(ax, (8.8, yA - 0.6), (8.8, yA - 1.5), kind="process")
bio.label(ax, (9.1, yA - 1.05), "loss of 19 nt from the 5′ end", size="tiny", color=P.muted(), ha="left")
bio.box(ax, (4.6, yA - 2.1), 6.0, 1.1, token="highlight",
        text="L-19 IVS, 395 nt: guanosine site and part of the\ninternal guide sequence kept, splice sites gone",
        size="tiny", radius=0.12)

# ----------------------------------------------------------------- B: the catalytic cycle
bio.panel(ax, "B", (0.1, 6.6))
bio.label(ax, (5.6, 6.6), "The cycle: nucleotidyl transfer between external substrates", size="small", bold=True)
cy = 3.4
states = [("free ribozyme\nG–3′-OH", "highlight", (1.9, cy + 1.5)),
          ("ribozyme · (C)$_5$", "neutral", (5.6, cy + 2.1)),
          ("ribozyme–C\ncovalent intermediate", "enzyme", (9.3, cy + 1.5)),
          ("ribozyme · (C)$_5$ + C", "neutral", (9.3, cy - 1.3)),
          ("free ribozyme\n+ (C)$_6$", "highlight", (5.6, cy - 2.0))]
for text, token, xy in states:
    bio.box(ax, xy, 3.3, 1.05, token=token, text=text, size="tiny", radius=0.12, zorder=10)
order = [0, 1, 2, 3, 4, 0]
for i in range(5):
    bio.arrow(ax, states[order[i]][2], states[order[i + 1]][2], kind="process", bend=0.18, shrink=1.15,
              color=P.muted())
bio.label(ax, (5.6, cy + 2.8), "(C)$_5$ pairs with the guide sequence", size="tiny", color=P.muted())
bio.label(ax, (11.1, cy + 0.3), "(C)$_4$ released", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (6.3, cy + 0.55), "100 turnovers per hour", size="small", bold=True, color=P.edge("positive"))
bio.label(ax, (6.3, cy - 0.05), "the ribozyme leaves each cycle unchanged", size="tiny", color=P.muted())

# ----------------------------------------------------------------- C: Michaelis-Menten
bio.panel(ax, "C", (13.2, 11.8))
bio.label(ax, (17.0, 11.8), "Saturable, Michaelis–Menten kinetics", size="small", bold=True)
kcat, Km = 0.028, 30.0
s = np.linspace(0, 200, 400)
v = kcat * s / (Km + s)
pl = Q.Plot(ax, (15.0, 7.0, 4.2, 3.9), xlim=(0, 200), ylim=(0, 0.032),
            xlabel="[(C)$_5$] / μM", ylabel="$v$ / (s$^{-1}$ per ribozyme)",
            xticks=[0, 50, 100, 150, 200], yticks=[0, 0.01, 0.02, 0.03], ylabel_offset=1.3)
pl.line(s, v, "highlight", lw=1.8)
pl.hline(kcat, text="$k_{\\mathrm{cat}} = 0.028\\ \\mathrm{s^{-1}}$", side="right")
pl.vline(Km, text="$K_{\\mathrm{m}} = 30\\ \\mathrm{\\mu M}$")
pl.line(s[:40], kcat / Km * s[:40], "muted", lw=1.0, dashed=True)
bio.label(ax, (17.0, 5.95), "initial slope $k_{\\mathrm{cat}}/K_{\\mathrm{m}} \\approx 10^{3}\\ \\mathrm{M^{-1}\\,s^{-1}}$;"
          " competitive inhibitors raise $K_{\\mathrm{m}}$ and leave $k_{\\mathrm{cat}}$ alone",
          size="tiny", color=P.muted())

# ----------------------------------------------------------------- D: catalytic efficiency
bio.panel(ax, "D", (13.2, 5.15))
bio.label(ax, (17.0, 5.15), "How good a catalyst is RNA?", size="small", bold=True)
items = [("uncatalysed transesterification", 1e-7, "neutral"),
         ("hammerhead ribozyme", 1e1, "rna"),
         ("L-19 IVS", 1e3, "highlight"),
         ("peptidyl transferase centre", 1e5, "rrna"),
         ("typical protein enzyme", 1e6, "enzyme"),
         ("catalytically perfect enzyme", 1e8, "positive")]
pl = Q.Plot(ax, (16.6, 0.9, 5.4, 3.6), xlim=(1e-8, 1e9), ylim=(-0.6, len(items) - 0.4), xlog=True,
            xlabel="$k_{\\mathrm{cat}}/K_{\\mathrm{m}}$ / (M$^{-1}$ s$^{-1}$)",
            xticks=[(1e-8, "$10^{-8}$"), (1e-4, "$10^{-4}$"), (1, "1"), (1e4, "$10^{4}$"), (1e8, "$10^{8}$")],
            frame="l", yticks=None)
for i, (name, val, tok) in enumerate(items):
    y = len(items) - 1 - i
    x0, x1 = pl.X(1e-8), pl.X(val)
    ax.plot([x0, x1], [pl.Y(y), pl.Y(y)], color=Q.line_color(tok), lw=4.5, solid_capstyle="round", zorder=7)
    bio.label(ax, (x0 - 0.15, pl.Y(y)), name, size="tiny", ha="right", color=P.ink())
bio.label(ax, (19.3, 4.75), "ribozymes occupy a band some five orders of magnitude below good protein enzymes",
          size="tiny", color=P.muted())
