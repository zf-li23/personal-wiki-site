# Fidelity of aminoacylation and of translation.
# A: the double sieve of isoleucyl-tRNA synthetase (Fersht). The synthetic (activation) site excludes amino
#    acids larger than Ile (e.g. Phe; Leu has the wrong shape) but cannot exclude smaller ones; Val, one CH2
#    smaller, is activated about 1/200 as often as Ile. The editing site, about 3 nm away, admits Val-AMP or
#    Val-tRNA(Ile) but excludes Ile, and hydrolyses them (pre- and post-transfer editing). Gly and Ala are
#    rejected at the first step because they bind too weakly.
# B: typical error frequencies along the path from gene to protein (order of magnitude; ranges vary between
#    codons and organisms): transcription about 1e-5 per nt (about 3e-5 per codon), aminoacylation 1e-5 to
#    1e-4 for synthetases with editing, decoding by the ribosome 1e-4 to 1e-3 (dominant), frameshifting about
#    1e-5 per codon. Overall about 1e-4 per residue.
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(12.6, 4.4))
gs = fig.add_gridspec(1, 2, width_ratios=[1.35, 1])
ax = fig.add_subplot(gs[0])
ax.set_xlim(0, 14)
ax.set_ylim(0, 7)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("A   Double sieve of Ile-tRNA synthetase", loc="left", fontsize=9, color=P.ink())

aas = [("Gly", 0.28), ("Ala", 0.36), ("Val", 0.48), ("Ile", 0.56), ("Leu", 0.56), ("Phe", 0.68)]
xs = np.linspace(1.2, 12.8, len(aas))
for (name, r), x in zip(aas, xs):
    tok = "channel"
    ax.add_patch(bio.core.Circle((x, 6.1), r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9))
    bio.label(ax, (x, 6.1), name, size="tiny", bold=True, color=P.on_fill())
# sieve 1
bio.box(ax, (7.0, 4.35), 13.2, 0.9, token="enzyme", text="Synthetic site: binds and activates (aa + ATP → aa-AMP + PPi)", size="tiny")
results1 = {"Gly": "weak binding", "Ala": "weak binding", "Leu": "wrong shape", "Phe": "too large"}
for (name, r), x in zip(aas, xs):
    if name in results1:
        bio.label(ax, (x, 5.15), results1[name], size="tiny", color=P.edge("negative"))
    else:
        bio.arrow(ax, (x, 5.45), (x, 4.85), kind="process")
bio.box(ax, (3.6, 2.05), 6.4, 0.9, token="highlight", text="Editing site: excludes Ile; hydrolyses Val-AMP, Val-tRNA(Ile)",
        size="tiny")
iv = xs[2], xs[3]
bio.arrow(ax, (iv[0], 3.85), (iv[0], 2.55), kind="process")
bio.label(ax, (iv[0] - 0.3, 3.2), "Val-AMP (1/200)", size="tiny", ha="right")
bio.arrow(ax, (iv[1], 3.85), (iv[1], 0.75), kind="process", color=P.edge("positive"))
bio.label(ax, (iv[1] + 0.3, 2.6), "Ile-AMP + tRNA(Ile)", size="tiny", ha="left")
bio.arrow(ax, (iv[0], 1.55), (iv[0], 0.75), kind="process", color=P.edge("negative"))
bio.label(ax, (iv[0], 0.45), "Val + AMP (+ tRNA)", size="tiny", color=P.edge("negative"))
bio.label(ax, (iv[1], 0.45), "Ile-tRNA(Ile)", size="tiny", color=P.edge("positive"))

ax = fig.add_subplot(gs[1])
steps = ["transcription\n(per codon)", "aminoacylation", "decoding\n(ribosome)", "frameshifting", "overall"]
lo = np.array([1e-5, 1e-5, 1e-4, 3e-6, 5e-5])
hi = np.array([1e-4, 1e-4, 1e-3, 3e-5, 5e-4])
toks = ["rna", "enzyme", "rrna", "neutral", "protein"]
for i, (a, b, t) in enumerate(zip(lo, hi, toks)):
    ax.barh(i, np.log10(b) - np.log10(a), left=np.log10(a), height=0.55, color=P.fill(t), edgecolor=P.edge(t))
ax.set_yticks(range(len(steps)))
ax.set_yticklabels(steps)
ax.invert_yaxis()
ax.set_xlim(-6, -2)
ax.set_xticks([-6, -5, -4, -3, -2])
ax.set_xticklabels(["10⁻⁶", "10⁻⁵", "10⁻⁴", "10⁻³", "10⁻²"])
charts.style_axes(ax, "error frequency per residue", None)
ax.set_title("B   Where translation errors arise", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
