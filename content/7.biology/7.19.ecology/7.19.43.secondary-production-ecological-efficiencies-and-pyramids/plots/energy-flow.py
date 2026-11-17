# A: fate of assimilated energy in Cedar Bog Lake (Lindeman 1942; J cm^-2 yr^-1).
# B: compartment model (Proposition 43.5.1): fraction of NPP respired in the grazer chain vs passed to
#    dead organic matter. Herbivore step with (c1, a2, p2); higher levels (c, a, p).
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
fig, (a, b) = plt.subplots(1, 2, figsize=(11.4, 4.4), gridspec_kw=dict(width_ratios=[1.3, 1]))
levels = ["Producers", "Herbivores", "Carnivores"]
A = [464.6, 62.8, 12.6]
parts = {"respiration": ([96.3, 18.8, 7.5], "negative"), "to decomposers": ([12.5, 2.1, 0.1], "animal"),
         "unused (sediment)": ([293.0, 29.3, 5.0], "neutral"), "to next level": ([62.8, 12.6, 0.0], "plant")}
y = np.arange(3)[::-1]
left = np.zeros(3)
for name, (vals, tok) in parts.items():
    frac = np.array(vals) / np.array(A) * 100
    a.barh(y, frac, left=left, color=P.fill(tok), edgecolor=P.edge(tok), label=name, height=0.6)
    for yi, l, f in zip(y, left, frac):
        if f > 6:
            a.text(l + f / 2, yi, f"{f:.0f}%", ha="center", va="center", fontsize=7.5, color=P.on_fill())
    left += frac
for yi, val in zip(y, A):
    a.text(101, yi, f"A = {val:g}", va="center", fontsize=8, color=P.ink())
a.annotate("", (50, 1.42), (50, 1.98), arrowprops=dict(arrowstyle="->", color=P.edge("plant"), lw=1.2))
a.text(52, 1.7, "13.5%", fontsize=8, color=P.edge("plant"), va="center")
a.annotate("", (50, 0.42), (50, 0.98), arrowprops=dict(arrowstyle="->", color=P.edge("plant"), lw=1.2))
a.text(52, 0.7, "20.1%", fontsize=8, color=P.edge("plant"), va="center")
a.set_yticks(y, levels)
a.set_xlim(0, 120)
a.set_xlabel("Share of assimilated energy / %")
a.legend(frameon=False, fontsize=7.5, loc="upper center", bbox_to_anchor=(0.45, -0.16), ncol=4)
a.set_title("A  Cedar Bog Lake (Lindeman 1942)", loc="left", fontweight="bold")


def grazer_resp(c1, a2, p2, c, aa, p):
    r2 = c1 * a2 * (1 - p2)
    I3 = c * c1 * a2 * p2
    return r2 + I3 * aa * (1 - p) / (1 - c * aa * p)


systems = [("Forest", (0.05, 0.4, 0.1, 0.25, 0.8, 0.1)), ("Grassland", (0.25, 0.4, 0.1, 0.25, 0.8, 0.1)),
           ("Plankton", (0.6, 0.6, 0.3, 0.3, 0.6, 0.3))]
g = np.array([grazer_resp(*v) for _, v in systems]) * 100
x = np.arange(3)
b.bar(x, g, color=P.fill("plant"), edgecolor=P.edge("plant"), label="respired in grazer chain")
b.bar(x, 100 - g, bottom=g, color=P.fill("animal"), edgecolor=P.edge("animal"),
      label="to dead organic matter (decomposers)")
for xi, v in zip(x, g):
    b.text(xi, v + 2, f"{v:.1f}%", ha="center", fontsize=8, color=P.ink())
b.set_xticks(x, [s[0] for s in systems])
b.set_ylim(0, 100)
b.set_ylabel("Share of NPP / %")
b.legend(frameon=False, fontsize=7.5, loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=1)
b.set_title("B  Grazer vs decomposer pathway (model)", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
