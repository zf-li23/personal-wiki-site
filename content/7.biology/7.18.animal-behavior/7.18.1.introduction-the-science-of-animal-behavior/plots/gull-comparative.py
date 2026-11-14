"""Comparative logic of mobbing: parsimony of nest-site evolution in gulls, and divergence versus convergence."""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 11.0)
GROUND, CLIFF = "plant", "rna"


def seg(a, b, token, lw=3.0):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge(token), lw=lw, solid_capstyle="round", zorder=5)


def tree(x0, root_state, title, letter):
    # tips: 3 ground-nesting gulls and 2 cliff-nesting species (kittiwakes), sharing a recent cliff ancestor
    bio.label(ax, (x0 + 4.0, 10.2), title, size="small", bold=True)
    root = (x0 + 4.0, 1.6)
    n1 = (x0 + 2.4, 4.2)   # ground clade
    n2 = (x0 + 6.4, 5.2)   # recent cliff ancestor
    tips = [(x0 + 0.6, 8.2), (x0 + 2.4, 8.2), (x0 + 4.2, 8.2), (x0 + 5.6, 8.2), (x0 + 7.4, 8.2)]
    if root_state == "ground":
        seg(root, n1, GROUND)
        seg(root, ((root[0] + n2[0]) / 2, (root[1] + n2[1]) / 2), GROUND)
        seg(((root[0] + n2[0]) / 2, (root[1] + n2[1]) / 2), n2, CLIFF)
        changes = [((root[0] + n2[0]) / 2, (root[1] + n2[1]) / 2)]
    else:
        mid = ((root[0] + n1[0]) / 2, (root[1] + n1[1]) / 2)
        seg(root, mid, CLIFF)
        seg(mid, n1, GROUND)
        seg(root, n2, CLIFF)
        mid2 = ((root[0] - 0.4) , root[1] - 0.0)
        changes = [mid]
        # second change: back to cliff in the kittiwake lineage implies cliff->ground->cliff when root is cliff
        # drawn as cliff root, ground clade, cliff clade: two changes are needed if the cliff clade is nested
    for t in tips[:3]:
        seg(n1, t, GROUND)
    for t in tips[3:]:
        seg(n2, t, CLIFF)
    for c in changes:
        ax.plot(*c, marker="o", ms=9, color=P.ink(), zorder=8)
    for t, name in zip(tips, ["gull", "gull", "gull", "kittiwake", "kittiwake"]):
        bio.label(ax, (t[0], t[1] + 0.5), name, size="tiny")
    return root, n1, n2, tips


rA = tree(1.0, "ground", "A  Ancestor nested on the ground: 1 change", "")
# B: cliff-nesting root, ground clade nested inside a cliff grade -> two changes
x0 = 11.0
bio.label(ax, (x0 + 4.0, 10.2), "B  Ancestor nested on cliffs: 2 changes", size="small", bold=True)
root = (x0 + 4.0, 1.6)
n0 = (x0 + 3.6, 3.0)
n1 = (x0 + 2.4, 4.6)
n2 = (x0 + 6.4, 5.6)
tips = [(x0 + 0.6, 8.2), (x0 + 2.4, 8.2), (x0 + 4.2, 8.2), (x0 + 5.6, 8.2), (x0 + 7.4, 8.2)]
seg(root, n0, CLIFF)
c1 = ((n0[0] + n1[0]) / 2, (n0[1] + n1[1]) / 2)
seg(n0, c1, CLIFF); seg(c1, n1, GROUND)
seg(n0, ((n0[0] + n2[0]) / 2, (n0[1] + n2[1]) / 2), GROUND)
c2 = ((n0[0] + n2[0]) / 2, (n0[1] + n2[1]) / 2)
seg(c2, n2, CLIFF)
c3 = ((n0[0] + c2[0]) / 2, (n0[1] + c2[1]) / 2)
# ground segment from n0 to c2 starts with a change at n0 side
for t in tips[:3]:
    seg(n1, t, GROUND)
for t in tips[3:]:
    seg(n2, t, CLIFF)
for c in (c1, c2):
    ax.plot(*c, marker="o", ms=9, color=P.ink(), zorder=8)
for t, name in zip(tips, ["gull", "gull", "gull", "kittiwake", "kittiwake"]):
    bio.label(ax, (t[0], t[1] + 0.5), name, size="tiny")
ax.plot(*n0, marker="o", ms=0)

# legend
for i, (tok, txt) in enumerate([(GROUND, "ground nesting"), (CLIFF, "cliff nesting")]):
    seg((2.0 + 7 * i, 0.5), (3.0 + 7 * i, 0.5), tok)
    bio.label(ax, (3.3 + 7 * i, 0.5), txt, size="tiny", ha="left")
ax.plot(15.6, 0.5, marker="o", ms=9, color=P.ink())
bio.label(ax, (16.0, 0.5), "change of nest site", size="tiny", ha="left")

# C: 2 x 2 diagram
bio.label(ax, (25.4, 10.2), "C  Ancestry versus selection", size="small", bold=True)
bio.box(ax, (23.4, 7.0), 3.6, 2.0, "plant", text=None)
bio.label(ax, (23.4, 7.4), "ground gulls", size="tiny", color=P.on_fill())
bio.label(ax, (23.4, 6.7), "mob", size="tiny", color=P.on_fill(), bold=True)
bio.box(ax, (27.6, 7.0), 3.6, 2.0, "rna", text=None)
bio.label(ax, (27.6, 7.4), "kittiwake", size="tiny", color=P.on_fill())
bio.label(ax, (27.6, 6.7), "no mobbing", size="tiny", color=P.on_fill(), bold=True)
bio.box(ax, (23.4, 3.4), 3.6, 2.0, "protein", text=None)
bio.label(ax, (23.4, 3.8), "colonial swallows", size="tiny", color=P.on_fill())
bio.label(ax, (23.4, 3.1), "mob", size="tiny", color=P.on_fill(), bold=True)
bio.label(ax, (25.5, 8.55), "shared ancestry, divergent behavior", size="tiny", color=P.muted())
bio.label(ax, (21.2, 5.2), "distinct ancestry, convergent", size="tiny", color=P.muted(), rotation=90)
bio.arrow(ax, (25.3, 7.0), (25.7, 7.0), kind="link", color=P.muted())
bio.arrow(ax, (23.4, 5.95), (23.4, 4.45), kind="link", color=P.muted())
bio.label(ax, (25.5, 1.6), "high nest predation: mobbing; low: none", size="tiny", color=P.muted())
