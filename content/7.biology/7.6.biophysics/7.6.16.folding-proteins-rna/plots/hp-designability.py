# Lattice HP models of protein folding, solved by exact enumeration.
# Top: the six-monomer toy model on a 2 x 3 lattice (Phillips et al., Physical Biology of the Cell, 8.4).
#   The three compact structures unrelated by symmetry; the energy is a cost eps for every contact of an H
#   monomer with solvent (outside the lattice) or with a non-bonded P monomer. A: the sequence PHPPHP has
#   energies 4, 4 and 2 eps and a unique native structure. B: its probability of being native,
#   p = exp(-2b) / (exp(-2b) + 2 exp(-4b)), b = eps/kT, against temperature.
# Bottom: designability on a 4 x 4 lattice (in the spirit of Li, Helling, Tang and Wingreen 1996). All 38
#   compact 16-monomer structures and all 2^16 = 65536 HP sequences; contact energies E_HH = -2.3,
#   E_HP = -1, E_PP = 0 between non-bonded neighbours. A sequence "designs" a structure if that structure is
#   its unique ground state. C: the number N_s of sequences designing each structure, in decreasing order.
#   D: the most and the least designable structures, each with the designing sequence of largest gap
#   (dotted lines: non-bonded contacts). E: the mean energy gap between the ground state and the
#   next structure, for the sequences designing each structure, against N_s: highly designable structures
#   are also the most stable ones.
import itertools

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
STEPS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def hamiltonian_paths(W, H):
    out = []

    def rec(path, seen):
        if len(path) == W * H:
            out.append(tuple(path))
            return
        x, y = path[-1]
        for dx, dy in STEPS:
            q = (x + dx, y + dy)
            if 0 <= q[0] < W and 0 <= q[1] < H and q not in seen:
                seen.add(q)
                path.append(q)
                rec(path, seen)
                path.pop()
                seen.remove(q)

    for s in itertools.product(range(W), range(H)):
        rec([s], {s})
    return out


def canonical(path, W, H):
    maps = [lambda x, y: (x, y), lambda x, y: (W - 1 - x, y), lambda x, y: (x, H - 1 - y),
            lambda x, y: (W - 1 - x, H - 1 - y)]
    if W == H:
        maps += [lambda x, y: (y, x), lambda x, y: (H - 1 - y, x), lambda x, y: (y, W - 1 - x),
                 lambda x, y: (H - 1 - y, W - 1 - x)]
    forms = []
    for f in maps:
        q = tuple(f(*s) for s in path)
        forms += [q, q[::-1]]
    return min(forms)


def structures(W, H):
    return sorted({canonical(p, W, H) for p in hamiltonian_paths(W, H)})


def draw(ax, path, seq=None, origin=(0, 0), scale=1.0, lw=2.0, r=0.22, contacts=()):
    ox, oy = origin
    xy = np.array([(ox + scale * x, oy + scale * y) for x, y in path])
    for i, j in contacts:
        ax.plot([xy[i, 0], xy[j, 0]], [xy[i, 1], xy[j, 1]], color=P.muted(), lw=0.9, ls=":", zorder=1)
    ax.plot(xy[:, 0], xy[:, 1], color=P.ink(), lw=lw, zorder=2, solid_capstyle="round")
    for k, (x, y) in enumerate(xy):
        tok = "neutral" if seq is None else ("highlight" if seq[k] == "H" else "neutral")
        ax.add_patch(plt.Circle((x, y), r * scale, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=3))
    ax.plot(*xy[0], marker="o", ms=2.5, color=P.ink(), zorder=4)


fig = plt.figure(figsize=(13.5, 8.2))
gs = fig.add_gridspec(2, 3, height_ratios=[1, 1.15], width_ratios=[1.25, 1, 1])

# ---- top: 2 x 3 toy model
u6 = structures(3, 2)


def toy_energy(seq, path):
    pos = {s: i for i, s in enumerate(path)}
    E = 0
    for i, (x, y) in enumerate(path):
        if seq[i] != "H":
            continue
        for dx, dy in STEPS:
            q = (x + dx, y + dy)
            if q not in pos:
                E += 1
            elif abs(pos[q] - i) > 1 and seq[pos[q]] == "P":
                E += 1
    return E


ax = fig.add_subplot(gs[0, 0:2])
ax.set_aspect("equal")
ax.axis("off")
seq = "PHPPHP"
for k, p in enumerate(u6):
    draw(ax, p, seq, origin=(k * 3.6, 0), scale=1.0, r=0.24)
    ax.text(k * 3.6 + 1.0, -0.75, f"E = {toy_energy(seq, p)} ε", ha="center", fontsize=9, color=P.ink())
    ax.text(k * 3.6 + 1.0, -1.25, f"HPHPHP: {toy_energy('HPHPHP', p)} ε", ha="center", fontsize=7.5, color=P.muted())
ax.text(-0.4, 1.75, "A   The 2 × 3 HP six-mer: three compact structures, sequence PHPPHP", fontsize=9, weight="bold",
        color=P.ink())
ax.text(10.2, 0.9, "H (hydrophobic)", fontsize=8, color=P.ink())
ax.add_patch(plt.Circle((9.95, 0.95), 0.12, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight")))
ax.text(10.2, 0.4, "P (polar)", fontsize=8, color=P.ink())
ax.add_patch(plt.Circle((9.95, 0.45), 0.12, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral")))
ax.set_xlim(-0.6, 12.6)
ax.set_ylim(-1.5, 2.0)

ax = fig.add_subplot(gs[0, 2])
T = np.linspace(0.05, 3, 300)
b = 1 / T
ax.plot(T, np.exp(-2 * b) / (np.exp(-2 * b) + 2 * np.exp(-4 * b)), color=charts.line("highlight"), lw=1.8)
ax.axhline(1 / 3, color=P.muted(), lw=0.6, ls=":")
ax.text(2.0, 0.36, "random: 1/3", fontsize=7.5, color=P.muted())
ax.set_ylim(0.25, 1.03)
charts.style_axes(ax, "temperature  kT/ε", "probability native")
charts.title(ax, "B   Melting of the toy protein")

# ---- bottom: 4 x 4 designability
u16 = structures(4, 4)
N = 16
contacts = []
for p in u16:
    pos = {s: i for i, s in enumerate(p)}
    cs = [(i, pos[q]) for i, (x, y) in enumerate(p) for q in ((x + 1, y), (x, y + 1)) if q in pos and abs(pos[q] - i) > 1]
    contacts.append(cs)
seqs = ((np.arange(2**N)[:, None] >> np.arange(N)) & 1).astype(np.int8)  # 1 = H
E = np.zeros((2**N, len(u16)))
for k, cs in enumerate(contacts):
    for i, j in cs:
        a, c = seqs[:, i], seqs[:, j]
        E[:, k] += np.where((a == 1) & (c == 1), -2.3, np.where(a + c == 1, -1.0, 0.0))
srt = np.sort(E, axis=1)
unique = srt[:, 0] < srt[:, 1] - 1e-9
best = np.argmin(E, axis=1)
Ns = np.bincount(best[unique], minlength=len(u16))
gap = srt[:, 1] - srt[:, 0]
mgap = np.array([gap[unique & (best == k)].mean() for k in range(len(u16))])
order = np.argsort(Ns)[::-1]

ax = fig.add_subplot(gs[1, 0])
ax.bar(np.arange(len(u16)), Ns[order], color=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.6)
ax.set_yscale("log")
charts.style_axes(ax, "structure (ranked by designability)", "sequences designing it, N_s")
ax.text(len(u16) * 0.35, Ns.max() * 0.6,
        f"{unique.sum()} of {2**N} sequences ({100 * unique.mean():.0f} %)\nhave a unique ground state", fontsize=8,
        color=P.ink())
charts.title(ax, f"C   Designability of the {len(u16)} compact 4 × 4 structures")

ax = fig.add_subplot(gs[1, 1])
ax.set_aspect("equal")
ax.axis("off")
for col, k in enumerate((order[0], order[-1])):
    p = u16[k]
    cand = np.flatnonzero(unique & (best == k))
    ex = cand[np.argmax(gap[cand])]          # the designing sequence with the largest gap
    sq = "".join("H" if seqs[ex, i] else "P" for i in range(N))
    draw(ax, p, sq, origin=(col * 5.0, 0), scale=1.0, lw=1.6, r=0.2, contacts=contacts[k])
    ax.text(col * 5.0 + 1.5, -0.9, f"N_s = {Ns[k]}", ha="center", fontsize=8.5, color=P.ink())
    ax.text(col * 5.0 + 1.5, -1.45, "most designable" if col == 0 else "least designable", ha="center", fontsize=7.5,
            color=P.muted())
ax.set_xlim(-0.6, 9.2)
ax.set_ylim(-1.8, 4.2)
ax.text(-0.5, 3.75, "D   Extremes, with their most stable sequence", fontsize=9, weight="bold", color=P.ink())

ax = fig.add_subplot(gs[1, 2])
ax.semilogx(Ns, mgap, "o", ms=4, color=charts.line("protein"))
r = np.corrcoef(np.log(Ns), mgap)[0, 1]
charts.style_axes(ax, "designability N_s", "mean energy gap to next structure")
ax.text(Ns.min() * 1.2, mgap.max() * 0.97, f"r(ln N_s, gap) = {r:.2f}", fontsize=8, color=P.ink())
charts.title(ax, "E   Designable structures are stable")
fig.tight_layout()
