# The eIF2 cycle and its control by eIF2alpha phosphorylation (the integrated stress response).
# A: eIF2-GTP binds Met-tRNAi (ternary complex, TC), which joins the 40S subunit (43S complex); at the start
#    codon eIF5 triggers GTP hydrolysis and eIF2-GDP is released. The decameric guanine nucleotide-exchange
#    factor eIF2B regenerates eIF2-GTP. Four kinases phosphorylate Ser51 of eIF2alpha in response to different
#    stresses: HRI (heme deficiency, also oxidative and mitochondrial stress), PKR (double-stranded RNA, viral
#    infection), PERK (unfolded proteins in the ER) and GCN2 (uncharged tRNA, amino-acid starvation).
#    Phosphorylated eIF2-GDP binds eIF2B tightly without exchange and sequesters it. ISRIB stabilizes eIF2B.
# B: a steady-state model of sequestration: eIF2B (total B_T = 0.2 of total eIF2, as in reticulocytes and many
#    mammalian cells) is titrated by phosphorylated eIF2 (dissociation constant K_i = 0.002 E_T, tight
#    binding solved exactly), and exchange on unphosphorylated eIF2-GDP follows Michaelis-Menten kinetics
#    (K_m = 0.1 E_T). Relative ternary-complex formation falls steeply once the phosphorylated fraction p
#    approaches B_T/E_T; if eIF2B were as abundant as eIF2 (B_T = E_T, dashed) the decline would be shallow.
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(12.6, 4.6))
gs = fig.add_gridspec(1, 2, width_ratios=[1.35, 1])
ax = fig.add_subplot(gs[0])
ax.set_xlim(0, 14)
ax.set_ylim(0, 8)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("A   The eIF2 cycle", loc="left", fontsize=9, color=P.ink())

nodes = {
    "gtp": ((7.0, 6.6), "eIF2·GTP", "enzyme"),
    "tc": ((11.2, 5.0), "eIF2·GTP·Met-tRNAi\n(ternary complex)", "trna"),
    "pic": ((10.6, 1.8), "43S → 48S, scanning\nstart codon (eIF5)", "rrna"),
    "gdp": ((4.6, 1.8), "eIF2·GDP", "neutral"),
    "seq": ((2.2, 5.0), "eIF2(αP)·GDP·eIF2B\n(sequestered)", "negative"),
}
for k, (xy, text, tok) in nodes.items():
    w = 3.4 if "\n" in text else 2.2
    bio.box(ax, xy, w, 1.0 if "\n" in text else 0.7, token=tok, text=text, size="tiny")
bio.arrow(ax, (8.2, 6.4), (10.3, 5.6), kind="process")
bio.label(ax, (9.7, 6.4), "+ Met-tRNAi", size="tiny", color=P.muted())
bio.arrow(ax, (11.1, 4.45), (10.8, 2.35), kind="process")
bio.label(ax, (11.6, 3.4), "+ 40S, mRNA", size="tiny", color=P.muted(), ha="left")
bio.arrow(ax, (8.85, 1.8), (5.75, 1.8), kind="process")
bio.label(ax, (7.3, 2.15), "GTP hydrolysis, Pi release", size="tiny", color=P.muted())
bio.label(ax, (7.3, 1.45), "60S joins (eIF5B)", size="tiny", color=P.muted())
bio.arrow(ax, (5.0, 2.2), (6.6, 6.2), kind="process")
bio.box(ax, (6.4, 4.2), 1.3, 0.6, token="receptor", text="eIF2B", size="tiny")
bio.label(ax, (6.4, 3.65), "GEF", size="tiny", color=P.muted())
# phosphorylation branch
bio.arrow(ax, (4.0, 2.2), (2.5, 4.45), kind="process", color=P.edge("negative"))
bio.label(ax, (4.0, 3.5), "P-Ser51", size="tiny", color=P.edge("negative"))
bio.arrow(ax, (3.95, 5.0), (5.75, 4.3), kind="inhibition", color=P.edge("negative"))
kin = [("HRI: heme ↓", 3.85), ("PKR: dsRNA", 3.15), ("PERK: ER stress", 2.45), ("GCN2: free tRNA", 1.75)]
for k, y in kin:
    bio.box(ax, (1.1, y), 2.0, 0.5, token="highlight", text=k, size="tiny")
    bio.arrow(ax, (2.15, y), (3.15, 3.25), kind="activation", lw=0.7, dashed=True)

# --- B: sequestration model ---
ax = fig.add_subplot(gs[1])
p = np.linspace(0, 0.6, 300)


def tc_rate(p, BT, ET=1.0, Ki=0.002, Km=0.1):
    inh = p * ET
    # free eIF2B from tight binding with inhibitor (quadratic)
    s = BT + inh + Ki
    bound = (s - np.sqrt(s * s - 4 * BT * inh)) / 2
    bfree = BT - bound
    sub = (1 - p) * ET
    return bfree * sub / (Km + sub)


for BT, ls, lab in ((0.2, "-", "eIF2B / eIF2 = 0.2"), (1.0, "--", "eIF2B / eIF2 = 1")):
    r = tc_rate(p, BT) / tc_rate(0.0, BT)
    ax.plot(p, r, color=charts.line("enzyme"), lw=1.8, ls=ls, label=lab)
ax.axvline(0.2, color=P.muted(), lw=0.7, ls=":")
ax.set_xlim(0, 0.6)
ax.set_ylim(0, 1.05)
ax.legend(fontsize=7, frameon=False)
charts.style_axes(ax, "fraction of eIF2α phosphorylated", "ternary complex formation (relative)")
ax.set_title("B   Sequestration amplifies the signal", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
