"""The two-stage model of gene expression with every parameter expanded into the chapter that sets it.

The steady-state protein number is a product of factors,
    p* = g * p_on * r * Psi * k_tl / (k'_deg (k_p + mu)),
one per step of the central dogma: template copies (replication), promoter occupancy (chromatin,
repressors and activators), initiation and elongation, processing into a functional transcript,
mRNA lifetime, translation and protein removal by degradation and dilution. Each box is a molecular
state, each arrow a step; to the right of each step are the factor it contributes and the formula
and chapter that determine it. A regulator acts by changing one factor, so on a logarithmic scale
the effects of regulators at different steps add."""

import wikibio as bio
from matplotlib.patches import FancyBboxPatch

P = bio.P
FONT = bio.core.FONT
fig, ax = bio.canvas(13.0, 14.6)

rows = [
    ("DNA (gene copies)", "dna", "$g$", "gene dosage $\\propto 2^{C(1-m)/\\tau}$", "7.2.7"),
    ("Promoter", "chromatin", "$p_{\\mathrm{on}}$", "accessibility; occupancy $p_{\\mathrm{bound}}$; ON/OFF switching", "7.2.4, 7.2.11, 7.2.14, 7.2.15, 7.2.22"),
    ("Pre-mRNA", "rna", "$r$", "two-step initiation; $T = k_{\\mathrm{t}}/(k_{\\mathrm{t}} + k_{\\mathrm{e}})$", "7.2.10, 7.2.13"),
    ("mRNA", "mrna", "$\\Psi$", "splicing window; polyadenylation", "7.2.16, 7.2.17"),
    ("Protein", "protein", "$k_{\\mathrm{tl}}$", "initiation control; uORFs; $\\rho_i = J/k_i$", "7.2.19, 7.2.20"),
]
removal = {
    3: ("$1/k'_{\\mathrm{deg}}$", "decay; miRNA $+\\gamma r/K$; sRNA titration", "7.2.18"),
    4: ("$1/(k_{\\mathrm{p}} + \\mu)$", "degradation and dilution", "7.2.20, 7.2.22"),
}

x0, w, h = 0.4, 3.6, 1.15
ys = [13.7 - 2.55 * i for i in range(len(rows))]
for i, (name, tok, *_rest) in enumerate(rows):
    y = ys[i]
    ax.add_patch(FancyBboxPatch((x0, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.25",
                                fc=P.fill(tok), ec=P.edge(tok), lw=1.4, zorder=3))
    ax.text(x0 + w / 2, y, name, ha="center", va="center", fontsize=FONT["normal"], color=P.on_fill(), zorder=4)

tx, dx = x0 + w + 0.9, 1.7


def label(y, sym, formula, ch, color):
    ax.text(tx, y + 0.28, sym, fontsize=FONT["normal"], color=color, va="center", weight="bold")
    ax.text(tx + dx, y + 0.28, formula, fontsize=FONT["small"], color=P.ink(), va="center")
    ax.text(tx + dx, y - 0.30, ch, fontsize=FONT["small"], color=P.muted(), va="center")


label(ys[0], *rows[0][2:], P.ink())
for i in range(len(rows) - 1):
    ya, yb = ys[i] - h / 2 - 0.08, ys[i + 1] + h / 2 + 0.08
    bio.arrow(ax, (x0 + w / 2, ya), (x0 + w / 2, yb), kind="process")
    label((ya + yb) / 2, *rows[i + 1][2:], P.ink())
for i, (sym, formula, ch) in removal.items():
    y = ys[i]
    bio.arrow(ax, (x0 + w + 0.05, y), (x0 + w + 0.5, y), kind="process")
    ax.text(x0 + w + 0.55, y, "$\\varnothing$", fontsize=FONT["small"], color=P.ink(), va="center")
    label(y, sym, formula, ch, P.edge("negative"))

ax.text(6.5, 0.75, "$p^{*} = g \\cdot p_{\\mathrm{on}} \\cdot r \\cdot \\Psi \\cdot \\dfrac{1}{k'_{\\mathrm{deg}}}"
        "\\cdot k_{\\mathrm{tl}} \\cdot \\dfrac{1}{k_{\\mathrm{p}} + \\mu}$",
        ha="center", va="center", fontsize=FONT["title"], color=P.ink())
