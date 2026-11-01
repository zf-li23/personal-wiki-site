# BLOSUM62 and PAM250 as heat maps, residues ordered by Dayhoff's physicochemical groups (cysteine; small
# residues S T P A G; acids and amides N D E Q; bases H R K; hydrophobic M I L V; aromatic F Y W). Blue is
# positive (the pair is seen in related proteins more often than by chance), red negative. Both matrices
# have positive blocks along the diagonal for the groups; BLOSUM62 rewards identities of rare residues
# (W, C) strongly, and PAM250, extrapolated to a large distance, has smaller identity scores and more
# positive off-diagonal entries.
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import wikibio as bio
from wikibio import charts as C

P = bio.P
ORDER = "CSTPAGNDEQHRKMILVFYW"
BLOSUM62 = [
    "9 -1 -1 -3 0 -3 -3 -3 -4 -3 -3 -3 -3 -1 -1 -1 -1 -2 -2 -2",
    "-1 4 1 -1 1 0 1 0 0 0 -1 -1 0 -1 -2 -2 -2 -2 -2 -3",
    "-1 1 5 -1 0 -2 0 -1 -1 -1 -2 -1 -1 -1 -1 -1 0 -2 -2 -2",
    "-3 -1 -1 7 -1 -2 -2 -1 -1 -1 -2 -2 -1 -2 -3 -3 -2 -4 -3 -4",
    "0 1 0 -1 4 0 -2 -2 -1 -1 -2 -1 -1 -1 -1 -1 0 -2 -2 -3",
    "-3 0 -2 -2 0 6 0 -1 -2 -2 -2 -2 -2 -3 -4 -4 -3 -3 -3 -2",
    "-3 1 0 -2 -2 0 6 1 0 0 1 0 0 -2 -3 -3 -3 -3 -2 -4",
    "-3 0 -1 -1 -2 -1 1 6 2 0 -1 -2 -1 -3 -3 -4 -3 -3 -3 -4",
    "-4 0 -1 -1 -1 -2 0 2 5 2 0 0 1 -2 -3 -3 -2 -3 -2 -3",
    "-3 0 -1 -1 -1 -2 0 0 2 5 0 1 1 0 -3 -2 -2 -3 -1 -2",
    "-3 -1 -2 -2 -2 -2 1 -1 0 0 8 0 -1 -2 -3 -3 -3 -1 2 -2",
    "-3 -1 -1 -2 -1 -2 0 -2 0 1 0 5 2 -1 -3 -2 -3 -3 -2 -3",
    "-3 0 -1 -1 -1 -2 0 -1 1 1 -1 2 5 -1 -3 -2 -2 -3 -2 -3",
    "-1 -1 -1 -2 -1 -3 -2 -3 -2 0 -2 -1 -1 5 1 2 1 0 -1 -1",
    "-1 -2 -1 -3 -1 -4 -3 -3 -3 -3 -3 -3 -3 1 4 2 3 0 -1 -3",
    "-1 -2 -1 -3 -1 -4 -3 -4 -3 -2 -3 -2 -2 2 2 4 1 0 -1 -2",
    "-1 -2 0 -2 0 -3 -3 -3 -2 -2 -3 -3 -2 1 3 1 4 -1 -1 -3",
    "-2 -2 -2 -4 -2 -3 -3 -3 -3 -3 -1 -3 -3 0 0 0 -1 6 3 1",
    "-2 -2 -2 -3 -2 -3 -2 -3 -2 -1 2 -2 -2 -1 -1 -1 -1 3 7 2",
    "-2 -3 -2 -4 -3 -2 -4 -4 -3 -2 -2 -3 -3 -1 -3 -2 -3 1 2 11",
]
PAM250 = [
    "12 0 -2 -3 -2 -3 -4 -5 -5 -5 -3 -4 -5 -5 -2 -6 -2 -4 0 -8",
    "0 2 1 1 1 1 1 0 0 -1 -1 0 0 -2 -1 -3 -1 -3 -3 -2",
    "-2 1 3 0 1 0 0 0 0 -1 -1 -1 0 -1 0 -2 0 -3 -3 -5",
    "-3 1 0 6 1 0 0 -1 -1 0 0 0 -1 -2 -2 -3 -1 -5 -5 -6",
    "-2 1 1 1 2 1 0 0 0 0 -1 -2 -1 -1 -1 -2 0 -3 -3 -6",
    "-3 1 0 0 1 5 0 1 0 -1 -2 -3 -2 -3 -3 -4 -1 -5 -5 -7",
    "-4 1 0 0 0 0 2 2 1 1 2 0 1 -2 -2 -3 -2 -3 -2 -4",
    "-5 0 0 -1 0 1 2 4 3 2 1 -1 0 -3 -2 -4 -2 -6 -4 -7",
    "-5 0 0 -1 0 0 1 3 4 2 1 -1 0 -2 -2 -3 -2 -5 -4 -7",
    "-5 -1 -1 0 0 -1 1 2 2 4 3 1 1 -1 -2 -2 -2 -5 -4 -5",
    "-3 -1 -1 0 -1 -2 2 1 1 3 6 2 0 -2 -2 -2 -2 -2 0 -3",
    "-4 0 -1 0 -2 -3 0 -1 -1 1 2 6 3 0 -2 -3 -2 -4 -4 2",
    "-5 0 0 -1 -1 -2 1 0 0 1 0 3 5 0 -2 -3 -2 -5 -4 -3",
    "-5 -2 -1 -2 -1 -3 -2 -3 -2 -1 -2 0 0 6 2 4 2 0 -2 -4",
    "-2 -1 0 -2 -1 -3 -2 -2 -2 -2 -2 -2 -2 2 5 2 4 1 -1 -5",
    "-6 -3 -2 -3 -2 -4 -3 -4 -3 -2 -2 -3 -3 4 2 6 2 2 -1 -2",
    "-2 -1 0 -1 0 -1 -2 -2 -2 -2 -2 -2 -2 2 4 2 4 -1 -2 -6",
    "-4 -3 -3 -5 -3 -5 -3 -6 -5 -5 -2 -4 -5 0 1 2 -1 9 7 0",
    "0 -3 -3 -5 -3 -5 -2 -4 -4 -4 0 -4 -4 -2 -1 -1 -2 7 10 0",
    "-8 -2 -5 -6 -6 -7 -4 -7 -7 -5 -3 2 -3 -4 -5 -2 -6 0 0 17",
]
cmap = LinearSegmentedColormap.from_list("score", [P.fill("negative"), P.surface(), P.fill("dna")])
fig, ax = bio.canvas(24.0, 11.6)
groups = [1, 5, 4, 3, 4, 3]
for k, (name, rows) in enumerate([("BLOSUM62", BLOSUM62), ("PAM250", PAM250)]):
    m = np.array([[int(v) for v in r.split()] for r in rows])
    a = C.axes_at(ax, (1.6 + 12.0 * k, 1.0, 9.6, 9.6))
    vmax = 12
    a.imshow(m, cmap=cmap, vmin=-vmax, vmax=vmax, extent=(0, 20, 20, 0))
    for i in range(20):
        for j in range(20):
            a.text(j + 0.5, i + 0.5, str(m[i, j]), ha="center", va="center", fontsize=5.2,
                   color=P.ink())
    edge = np.cumsum([0] + groups)
    for e in edge[1:-1]:
        a.axhline(e, color=P.ink(), lw=0.6)
        a.axvline(e, color=P.ink(), lw=0.6)
    a.set_xticks(np.arange(20) + 0.5, list(ORDER))
    a.set_yticks(np.arange(20) + 0.5, list(ORDER))
    a.xaxis.tick_top()
    C.style_axes(a, box=True)
    a.tick_params(length=0)
    bio.label(ax, (1.6 + 12.0 * k + 4.8, 0.4), name, size="small", bold=True)
