# The economics of translation.
# A: fraction of protein molecules without any misincorporated residue, (1 - e)^L, against chain length L
#    for per-residue error e = 1e-3, 1e-4 and 1e-5; marks: a typical bacterial protein (300 aa), a large
#    protein (1000 aa) and titin (about 34,000 aa).
# B: energy per peptide bond in NTP-equivalents (phosphoanhydride bonds): two for aminoacylation (ATP -> AMP +
#    PPi, PPi -> 2 Pi), one for EF-Tu, one for EF-G; initiation (IF2), termination (RF3) and recycling (EF-G
#    with RRF) cost three per chain, i.e. 0.01 per bond for L = 300; GTP spent on rejected near-cognate
#    ternary complexes and on editing adds a few percent (illustrative value 0.05).
# C: the bacterial growth law (Scott, Hwa and colleagues, 2010): the RNA/protein mass ratio r, proportional to
#    the ribosome content, rises linearly with growth rate when growth is varied by the nutrients,
#    r = r0 + lambda/kappa_t, with r0 = 0.087 and kappa_t = 4.5 h^-1 for E. coli; the slope is set by the
#    elongation rate of the ribosome. Doubling times are marked on the top.
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(12.6, 3.9), gridspec_kw={"width_ratios": [1.1, 0.9, 1.0]})

ax = axs[0]
L = np.logspace(1, 4.7, 300)
for e, tok in ((1e-3, "negative"), (1e-4, "rna"), (1e-5, "dna")):
    ax.semilogx(L, (1 - e) ** L, color=charts.line(tok), lw=1.7, label=f"ε = {e:.0e}".replace("e-0", "e−"))
for x, name in ((300, "300 aa"), (1000, "1000 aa"), (34000, "titin")):
    ax.axvline(x, color=P.muted(), lw=0.7, ls=":")
    ax.text(x * 1.08, 0.04, name, fontsize=7, color=P.muted(), rotation=90, va="bottom")
ax.set_ylim(0, 1.03)
ax.legend(fontsize=7, frameon=False, loc="lower left", bbox_to_anchor=(0.0, 0.18))
charts.style_axes(ax, "chain length L (residues)", "error-free fraction (1 − ε)ᴸ")
ax.set_title("A   Error-free proteins", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
parts = [("aminoacylation", 2.0, "atp"), ("EF-Tu", 1.0, "enzyme"), ("EF-G", 1.0, "receptor"),
         ("initiation etc. per bond", 0.01, "neutral"), ("rejection, editing", 0.05, "negative")]
bottom = 0.0
for name, v, tok in parts:
    ax.bar([0], [v], bottom=bottom, width=0.55, color=P.fill(tok), edgecolor=P.edge(tok))
    yt = bottom + v / 2 if v > 0.5 else {0.01: 4.3, 0.05: 4.55}[v]
    ax.text(0.36, yt, f"{name}: {v:g}".replace("\n", " "), fontsize=7, va="center", color=P.ink())
    bottom += v
ax.set_xlim(-0.5, 1.9)
ax.set_xticks([])
ax.set_ylim(0, 4.8)
charts.style_axes(ax, None, "NTP → NDP or NMP per peptide bond")
ax.set_title("B   Energy per peptide bond", loc="left", fontsize=9, color=P.ink())

ax = axs[2]
lam = np.linspace(0, 2.0, 100)
r = 0.087 + lam / 4.5
ax.plot(lam, r, color=charts.line("rrna"), lw=1.8)
ax.fill_between(lam, 0, 0.087, color=P.fill("neutral"), alpha=0.3, lw=0)
ax.text(0.05, 0.04, "r₀: ribosomes not translating\nat full speed", fontsize=7, color=P.muted())
ax.text(0.25, 0.45, "r = r₀ + λ / κ_t", fontsize=8, color=P.ink())
ax.set_xlim(0, 2.0)
ax.set_ylim(0, 0.6)
charts.style_axes(ax, "growth rate λ / h⁻¹", "RNA / protein mass ratio r")
top = ax.twiny()
top.set_xlim(ax.get_xlim())
ticks = [np.log(2) / t for t in (3.0, 1.0, 0.5, 0.35)]
top.set_xticks(ticks)
top.set_xticklabels(["3 h", "1 h", "30 min", "21 min"], fontsize=7, color=P.muted())
top.tick_params(colors=P.muted(), length=2)
for sp in top.spines.values():
    sp.set_visible(False)
ax.set_title("C   Growth law", loc="left", fontsize=9, color=P.ink(), pad=18)
fig.tight_layout()
