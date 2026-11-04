# Scale and distribution of the virosphere.
# A: genome sizes of selected viroids, viruses and prokaryotic cells on a log axis (values from
#    Madigan et al., Brock Biology of Microorganisms 15e, Fig. 10.1).
# B: which Baltimore classes infect which host group, as a qualitative matrix (dominant / common /
#    rare / none known); counts of described species are not shown because they change constantly.
import numpy as np
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(17, 7.6)

# --- A  genome sizes ------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 7.4))
bio.label(ax, (4.6, 7.25), "Genome size", size="title", bold=True)

ENTRIES = [  # (name, bases or base pairs, token, row, side of the label)
    ("coconut cadang-cadang viroid", 246, "rna", 0, "right"),
    ("hepatitis delta (satellite)", 1700, "rna", 1, "right"),
    ("circovirus", 1750, "dna", 2, "left"),
    ("hepatitis B", 3200, "dna", 2, "right"),
    ("MS2 (phage)", 3500, "rna", 3, "left"),
    ("poliovirus", 7500, "rna", 3, "right"),
    ("HIV-1", 9100, "rna", 4, "left"),
    ("rotavirus", 17900, "rna", 4, "right"),
    ("SARS-CoV-2", 30000, "rna", 5, "left"),
    ("lambda (phage)", 48500, "dna", 5, "right"),
    ("herpes simplex 1", 152000, "dna", 6, "left"),
    ("T4 (phage)", 170000, "dna", 6, "right"),
    ("phage G", 500000, "dna", 7, "left"),
    ("mimivirus", 1200000, "dna", 8, "left"),
    ("pandoravirus", 2500000, "dna", 9, "left"),
]
CELLS = [("Mycoplasma genitalium", 580000), ("Escherichia coli", 4600000)]

pl = quant.Plot(ax, (1.1, 1.3, 7.2, 5.3), xlim=(2.2, 7.0), ylim=(-1.4, 10.2),
                xlabel="$\\log_{10}$ (genome size / bases or base pairs)",
                xticks=[3, 4, 5, 6, 7], yticks=[], frame="b")
pl.band(np.array([np.log10(246), np.log10(30000)]), np.array([-0.9, -0.9]), np.array([9.9, 9.9]),
        "rna", alpha=0.10)
pl.band(np.array([np.log10(1750), np.log10(2500000)]), np.array([-0.9, -0.9]), np.array([9.9, 9.9]),
        "dna", alpha=0.10)
for name, size, tok, row, side in ENTRIES:
    x = np.log10(size)
    pl.points(np.array([x]), np.array([row]), tok, r=0.075)
    dx = 0.10 if side == "right" else -0.10
    pl.text(x + dx, row, name, size="tiny", ha="left" if side == "right" else "right", color=P.muted())
for name, size in CELLS:
    x = np.log10(size)
    pl.vline(x, token="bacterium", dashed=True)
    pl.points(np.array([x]), np.array([-0.7]), "bacterium", r=0.08)
    side = -1 if name.startswith("Mycoplasma") else 1
    pl.text(x + 0.09 * side, -0.7, name, size="tiny", ha="left" if side > 0 else "right",
            color=P.muted(), italic=True)
pl.text(np.log10(500), 10.0, "RNA genomes", size="tiny", color=quant.line_color("rna"))
pl.text(np.log10(600000), 10.0, "DNA genomes", size="tiny", color=quant.line_color("dna"))

# --- B  Baltimore class by host group -------------------------------------------------------------------
bio.panel(ax, "B", (9.0, 7.4))
bio.label(ax, (13.4, 7.25), "Which classes infect which hosts", size="title", bold=True)

CLASSES = ["I\ndsDNA", "II\nssDNA", "III\ndsRNA", "IV\nss(+)", "V\nss(−)", "VI\nRT RNA", "VII\nRT DNA"]
HOSTS = ["Bacteria", "Archaea", "Protists", "Fungi", "Plants", "Animals"]
M = np.array([              # 3 dominant, 2 common, 1 rare, 0 none known
    [3, 1, 1, 1, 0, 0, 0],  # Bacteria
    [3, 1, 0, 0, 0, 0, 0],  # Archaea
    [3, 1, 2, 3, 1, 0, 0],  # Protists
    [0, 0, 3, 3, 0, 0, 0],  # Fungi
    [1, 2, 2, 3, 1, 0, 2],  # Plants
    [2, 2, 2, 3, 3, 3, 1],  # Animals
])
TOK = {3: "virus", 2: "virus", 1: "neutral"}
RAD = {3: 0.24, 2: 0.17, 1: 0.11}
x0, y0, cw, ch = 10.6, 2.3, 0.84, 0.64
for i, host in enumerate(HOSTS):
    y = y0 + (len(HOSTS) - 1 - i) * ch + ch / 2
    bio.label(ax, (x0 - 0.25, y), host, size="small", ha="right")
    for j in range(len(CLASSES)):
        v = int(M[i, j])
        xc = x0 + j * cw + cw / 2
        if v == 0:
            bio.label(ax, (xc, y), "–", size="small", color=P.muted())
        else:
            ax.add_patch(Circle((xc, y), RAD[v], facecolor=P.fill(TOK[v]), edgecolor=P.edge(TOK[v]),
                                lw=0.8, zorder=8))
for j, cl in enumerate(CLASSES):
    bio.label(ax, (x0 + j * cw + cw / 2, y0 + len(HOSTS) * ch + 0.34), cl, size="tiny", color=P.muted())

for k, (v, txt) in enumerate(((3, "dominant"), (2, "common"), (1, "rare"))):
    xc = 10.7 + k * 1.75
    ax.add_patch(Circle((xc, 1.55), RAD[v], facecolor=P.fill(TOK[v]), edgecolor=P.edge(TOK[v]), lw=0.8))
    bio.label(ax, (xc + 0.3, 1.55), txt, size="tiny", ha="left", color=P.muted())
bio.label(ax, (16.7, 1.55), "–  none known", size="tiny", ha="right", color=P.muted())
bio.label(ax, (13.4, 0.85),
          "only animals host all seven classes; classes V and VI are essentially confined to them",
          size="tiny", color=P.muted())
