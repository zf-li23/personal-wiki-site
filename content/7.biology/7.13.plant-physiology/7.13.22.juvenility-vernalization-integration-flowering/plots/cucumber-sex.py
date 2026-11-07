# Sex expression in cucumber (schematic, illustrative numbers).
# A: flower type at successive nodes of the main stem in three genotypes: monoecious (male flowers on
#    the lower nodes, then female flowers at increasing frequency), gynoecious (F locus, a duplicated
#    ACC synthase gene CsACS1G: female flowers from the first nodes) and andromonoecious (m mutants of
#    CsACS2: bisexual flowers replace female ones).
# B: percentage of female nodes on monoecious plants sprayed with ethephon (ethylene-releasing) at the
#    seedling stage, with and without gibberellin (GA3), which promotes maleness; Hill curves.
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(0)
nodes = np.arange(1, 26)
col = {"M": "#2f6fb5", "F": "#d93a6b", "B": "#9c6bc4", "-": "0.85"}


def monoecious(n):
    p_f = np.clip((n - 6) / 16, 0, 0.8)
    return ["F" if rng.random() < p else "M" for p in p_f]


mono = monoecious(nodes)
rows = [("monoecious", mono),
        ("gynoecious (F)", ["F"] * 25),
        ("andromonoecious (m)", ["B" if s == "F" else s for s in mono])]

fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 3.8), gridspec_kw={"width_ratios": [1.6, 1]})
for i, (name, seq) in enumerate(rows):
    y = 2 - i
    for n, s in zip(nodes, seq):
        ax.scatter(n, y, s=95, color=col[s], edgecolor="0.25", lw=0.5, zorder=3,
                   marker="o" if s != "B" else "D")
    ax.text(0.2, y, name, ha="right", va="center", fontsize=9)
for s, lab in (("M", "male"), ("F", "female"), ("B", "bisexual")):
    ax.scatter([], [], s=60, color=col[s], edgecolor="0.25", lw=0.5, marker="o" if s != "B" else "D", label=lab)
ax.legend(frameon=False, fontsize=8, ncol=3, loc="upper center", bbox_to_anchor=(0.55, 1.18))
ax.set_xlim(-6.5, 26)
ax.set_ylim(-0.6, 2.6)
ax.set_xticks([1, 5, 10, 15, 20, 25])
ax.set_yticks([])
ax.set_xlabel("Node number on the main stem")
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_bounds(1, 25)

c = np.logspace(0, 3.3, 300)  # ethephon / (mg L^-1)
base = 25


def female(c, ec50):
    return base + (90 - base) * c**1.5 / (ec50**1.5 + c**1.5)


bx.plot(c, female(c, 100), color="#d93a6b", lw=2.2, label="ethephon")
bx.plot(c, female(c, 400) - 10 / (1 + c / 30), color="#2f6fb5", lw=2.2, ls="--", label="ethephon + GA3")
bx.set_xscale("log")
bx.set_xlabel("Ethephon / (mg L⁻¹)")
bx.set_ylabel("Female nodes / %")
bx.set_ylim(0, 100)
bx.legend(frameon=False, fontsize=8, loc="upper left")
bx.spines[["top", "right"]].set_visible(False)
for a, letter in zip((ax, bx), "AB"):
    a.text(-0.03 if a is ax else -0.18, 1.04, letter, transform=a.transAxes, fontsize=12, weight="bold")
fig.tight_layout()
