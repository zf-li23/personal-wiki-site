"""Brain mass against body mass in vertebrates and the encephalization quotient.

Approximate adult values (body mass in kg, brain mass in g) compiled from the literature
(e.g. Crile and Quiring 1940; Jerison 1973; Iwaniuk and Nelson 2003; Boddy et al. 2012);
single representative values per species, enough to show the grades between classes.
Each class is fitted by least squares on log10 scales. The dashed line is Jerison's
expected brain mass for mammals, E = 0.12 P^(2/3) (E and P in g); EQ = observed / expected.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
data = {
    "Mammals": [
        ("shrew", 0.01, 0.17), ("bat", 0.008, 0.15), ("mouse", 0.02, 0.42), ("rat", 0.3, 2.0),
        ("hedgehog", 0.8, 3.4), ("rabbit", 2.5, 11), ("opossum", 3, 7.5), ("cat", 3.3, 30),
        ("rhesus", 7, 90), ("dog", 15, 80), ("kangaroo", 30, 60), ("chimpanzee", 45, 400),
        ("sheep", 55, 140), ("human", 65, 1350), ("pig", 100, 180), ("gorilla", 140, 500),
        ("dolphin", 170, 1600), ("horse", 450, 600), ("cow", 600, 450), ("giraffe", 800, 680),
        ("elephant", 4000, 4800), ("orca", 5500, 5600), ("sperm whale", 35000, 7800),
        ("blue whale", 100000, 6900),
    ],
    "Birds": [
        ("hummingbird", 0.004, 0.13), ("zebra finch", 0.012, 0.45), ("pigeon", 0.4, 2.3),
        ("barn owl", 0.4, 6.0), ("grey parrot", 0.42, 8.8), ("crow", 0.5, 9.5),
        ("raven", 1.2, 15), ("duck", 1.2, 6.0), ("chicken", 2.0, 3.6), ("emu", 40, 25),
        ("ostrich", 100, 40),
    ],
    "Reptiles": [
        ("gecko", 0.01, 0.05), ("lizard", 0.1, 0.2), ("iguana", 1.0, 0.6), ("turtle", 1.0, 0.5),
        ("python", 10, 1.5), ("Komodo dragon", 50, 6.0), ("crocodile", 200, 12),
    ],
    "Fishes": [
        ("goldfish", 0.05, 0.1), ("elephantnose fish", 0.01, 0.3), ("trout", 1.0, 0.6),
        ("cod", 5, 1.5), ("tuna", 50, 10), ("white shark", 1000, 35),
    ],
}
cols = {"Mammals": P.edge("rna"), "Birds": P.edge("dna"), "Reptiles": P.edge("plant"),
        "Fishes": P.edge("enzyme")}
marks = {"Mammals": "o", "Birds": "s", "Reptiles": "^", "Fishes": "D"}
label_these = {"human", "dolphin", "chimpanzee", "elephant", "blue whale", "mouse", "raven",
               "ostrich", "crocodile", "white shark", "elephantnose fish", "grey parrot"}

fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.5, 4.6), gridspec_kw=dict(width_ratios=[1.5, 1]))
xx = np.logspace(-3, 5.2, 50)
for grp, rows in data.items():
    m = np.array([r[1] for r in rows])
    e = np.array([r[2] for r in rows])
    slope, icpt = np.polyfit(np.log10(m), np.log10(e), 1)
    ax.loglog(m, e, marks[grp], color=cols[grp], ms=5, label=f"{grp} (slope {slope:.2f})")
    xr = np.logspace(np.log10(m.min()), np.log10(m.max()), 20)
    ax.loglog(xr, 10**icpt * xr**slope, color=cols[grp], lw=1.2)
    for name, mm, ee in rows:
        if name in label_these:
            off = {"human": (-20, 5), "mouse": (-8, 8), "elephantnose fish": (6, -10),
                   "chimpanzee": (-38, 5), "grey parrot": (-40, 5)}.get(name, (4, 3))
            ax.annotate(name, (mm, ee), xytext=off, textcoords="offset points", fontsize=7,
                        color=P.ink())
ax.loglog(xx, 0.12 * (xx * 1000) ** (2 / 3), "--", color=P.muted(), lw=1,
          label=r"Jerison: $E = 0.12\,P^{2/3}$")
ax.set_xlabel("Body mass / kg")
ax.set_ylabel("Brain mass / g")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("A  Brain-body allometry: grades between classes", loc="left", fontsize=10)
ax.grid(True, which="major", alpha=0.3)

names = ["human", "dolphin", "chimpanzee", "rhesus", "elephant", "dog", "cat", "horse",
         "mouse", "rat", "cow", "blue whale"]
allm = {r[0]: r for r in data["Mammals"]}
eq = [allm[n][2] / (0.12 * (allm[n][1] * 1000) ** (2 / 3)) for n in names]
order = np.argsort(eq)
bx.barh(np.arange(len(names)), np.array(eq)[order], color=P.fill("rna"), edgecolor=P.edge("rna"))
bx.set_yticks(np.arange(len(names)))
bx.set_yticklabels(np.array(names)[order], fontsize=8)
bx.axvline(1, color=P.muted(), lw=1, ls="--")
bx.set_xlabel("Encephalization quotient EQ")
bx.set_title("B  EQ of some mammals", loc="left", fontsize=10)
bx.grid(True, axis="x", alpha=0.3)
fig.tight_layout()
for n, v in zip(names, eq):
    print(n, round(v, 2))
