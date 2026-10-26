"""Class I ribonucleotide reductase and its two allosteric sites. Left: the alpha2-beta2 enzyme (E. coli
numbering). Each alpha subunit carries the active site with the cysteines that reduce the substrate and Cys439,
which becomes a thiyl radical; the specificity site at the alpha-alpha interface; and the activity site in the
N-terminal ATP cone. Each beta subunit has a diferric (Fe3+-O-Fe3+) centre that generates and stabilizes the
Tyr122 radical, which is passed about 3.5 nm to Cys439 along a chain of aromatic residues (proton-coupled
electron transfer) each time a substrate binds. Electrons for the reduction come from NADPH through
thioredoxin or glutaredoxin. Right: the regulatory logic. Activity site: ATP activates, dATP inactivates (in
E. coli by forming inactive alpha4-beta4 rings). Specificity site: ATP or dATP bound favours reduction of CDP
and UDP, dTTP bound favours GDP, dGTP bound favours ADP; each product thus calls for the next."""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(21.0, 9.4)
ink, neg, pos = P.ink(), P.edge("negative"), P.edge("positive")

# alpha2
for x, tag in ((2.6, "α"), (6.0, "α")):
    bio.protein(ax, (x, 6.2), 3.2, 2.6, "protein", text="", wobble=0.04)
    bio.label(ax, (x, 6.6), tag, size="title", bold=True, color=P.on_fill())
for x in (2.6, 6.0):
    bio.box(ax, (x - 0.9 if x < 4 else x + 0.9, 7.4), 1.1, 0.6, token="highlight", text="A", size="small", radius=0.3, zorder=20)
bio.box(ax, (4.3, 6.9), 0.9, 0.6, token="atp", text="S", size="small", radius=0.3, zorder=20)
for x in (2.6, 6.0):
    bio.box(ax, (x, 5.6), 1.5, 0.62, token="enzyme", text="C439•", size="tiny", radius=0.3, zorder=20)
# beta2
for x in (2.9, 5.7):
    bio.protein(ax, (x, 2.6), 2.6, 2.2, "receptor", text="", wobble=0.04)
    bio.label(ax, (x, 1.9), "β", size="title", bold=True, color=P.on_fill())
for x in (2.9, 5.7):
    bio.box(ax, (x, 3.0), 1.6, 0.6, token="highlight", text="Y122•", size="tiny", radius=0.3, zorder=20)
    bio.box(ax, (x, 2.4), 1.8, 0.5, token="drug", text="Fe³⁺–O–Fe³⁺", size="tiny", radius=0.25, zorder=20)
for x in (2.6, 6.0):
    xb = 2.9 if x < 4 else 5.7
    ax.plot([xb, xb - 0.3 if x < 4 else xb + 0.3, x], [3.3, 4.3, 5.3], color=P.edge("highlight"), lw=1.8,
            ls=(0, (2, 1.5)), zorder=8)
bio.label(ax, (4.3, 4.35), "radical transfer\n~3.5 nm", size="tiny", color=P.edge("highlight"), bold=True)
bio.callout(ax, (1.7, 7.4), (0.9, 8.75), "activity site (ATP cone)", size="tiny")
bio.callout(ax, (4.3, 7.2), (5.3, 8.75), "specificity site", size="tiny")
bio.callout(ax, (6.5, 5.6), (8.3, 5.0), "active site", size="tiny")
bio.label(ax, (4.3, 0.5), "NADPH → thioredoxin (or glutaredoxin) → active-site cysteines", size="tiny", color=P.muted())

# logic panel
X0 = 10.6
bio.label(ax, (X0, 8.7), "Activity site", size="title", bold=True, ha="left")
bio.box(ax, (X0 + 1.0, 7.8), 1.6, 0.6, token="atp", text="ATP", size="small")
bio.arrow(ax, (X0 + 1.85, 7.8), (X0 + 3.5, 7.8), kind="activation", color=pos, lw=1.6)
bio.box(ax, (X0 + 1.0, 7.0), 1.6, 0.6, token="positive", text="dATP", size="small")
bio.arrow(ax, (X0 + 1.85, 7.0), (X0 + 3.5, 7.0), kind="inhibition", color=neg, lw=1.6)
bio.label(ax, (X0 + 3.8, 7.4), "all four reductions\n(dATP: inactive α₄β₄ rings)", size="tiny", ha="left")

bio.label(ax, (X0, 5.9), "Specificity site", size="title", bold=True, ha="left")
rows = [("ATP, dATP", "atp", "CDP, UDP", "dCTP, dTTP"), ("dTTP", "negative", "GDP", "dGTP"),
        ("dGTP", "rna", "ADP", "dATP")]
for i, (eff, tok, sub, prod) in enumerate(rows):
    y = 5.0 - 1.25 * i
    bio.box(ax, (X0 + 1.0, y), 1.9, 0.62, token=tok, text=eff, size="small")
    bio.arrow(ax, (X0 + 2.0, y), (X0 + 3.4, y), kind="activation", color=pos, lw=1.6)
    bio.box(ax, (X0 + 4.6, y), 2.2, 0.62, token="metabolite", text=sub, size="small")
    bio.arrow(ax, (X0 + 5.75, y), (X0 + 7.0, y), kind="process", color=ink, lw=1.4)
    bio.label(ax, (X0 + 7.2, y), prod, size="small", ha="left")
bio.label(ax, (X0 + 4.6, 0.95), "each product shifts the enzyme to the next substrate:\n"
          "pyrimidines → dTTP → GDP → dGTP → ADP → dATP → off", size="tiny", color=P.muted())
