# Absorption wavelength of a conjugated chain of N carbon atoms (N pi electrons) in three models.
# Free-electron (particle-in-a-box) model: HOMO-LUMO gap dE = h^2 (N + 1) / (8 m_e L^2), lambda = hc / dE,
#   with the box length L = (N - 1) a (atoms at the walls) or L = (N + 1) a (box extending half a bond
#   beyond the terminal atoms), a = 0.14 nm; the dotted curve uses a = 0.10 nm.
# Hueckel model with bond alternation: nearest-neighbour couplings alternate between beta_d (double bonds)
#   and beta_s (single bonds); beta_d = 4.10 eV and beta_s = 3.03 eV were chosen so that the model gives
#   217 nm for butadiene (N = 4) and 470 nm for N = 22. The gap of an infinite chain is 2 (beta_d - beta_s)
#   = 2.14 eV (578 nm): the absorption saturates instead of growing without limit.
# Points: approximate absorption maxima of polyenes in hexane (butadiene 217 nm, hexatriene 258 nm,
#   beta-carotene 452 nm and lycopene 471 nm, both with 22 conjugated carbons).
# Right: the energy levels of the free-electron box for N = 22 (11 doubly occupied levels).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
h, c, me = 6.62607015e-34, 299792458.0, 9.1093837e-31


def free(N, a, ends):
    L = (N - 1) * a if ends == "atoms" else (N + 1) * a
    dE = h**2 * (N + 1) / (8 * me * L**2)
    return h * c / dE * 1e9


def huckel(N, bd=4.1001, bs=3.0278):
    H = np.zeros((N, N))
    for i in range(N - 1):
        H[i, i + 1] = H[i + 1, i] = bd if i % 2 == 0 else bs
    w = np.sort(np.linalg.eigvalsh(H))
    return 1239.84 / (w[N // 2] - w[N // 2 - 1])


Ns = np.arange(4, 41, 2)
fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.2), gridspec_kw=dict(width_ratios=[1.7, 1]))
ax = axs[0]
ax.axhspan(400, 700, color=P.fill("chloroplast"), alpha=0.25, lw=0)
ax.text(39.5, 690, "visible", ha="right", va="top", fontsize=7.5, color=P.muted())
ax.plot(Ns, [free(N, 0.14e-9, "atoms") for N in Ns], color=charts.line("rna"), lw=1.8,
        label="free electron, L = (N − 1)a, a = 0.14 nm")
ax.plot(Ns, [free(N, 0.14e-9, "beyond") for N in Ns], color=charts.line("rna"), lw=1.4, ls="--",
        label="free electron, L = (N + 1)a")
ax.plot(Ns, [free(N, 0.10e-9, "atoms") for N in Ns], color=charts.line("rna"), lw=1.0, ls=":",
        label="free electron, L = (N − 1)a, a = 0.10 nm")
ax.plot(Ns, [huckel(N) for N in Ns], color=charts.line("dna"), lw=1.8, label="Hückel with bond alternation")
ax.axhline(578, color=charts.line("dna"), lw=0.6, ls=":")
ax.text(5, 590, "infinite chain (Hückel)", fontsize=7, color=charts.line("dna"))
pts = [(4, 217, "butadiene"), (6, 258, "hexatriene"), (22, 452, "β-carotene"), (22, 471, "lycopene")]
for N, l, name in pts:
    ax.plot(N, l, "o", color=charts.line("atp"), ms=5, zorder=5)
    ax.text(N + 0.6, l - 18 if name != "lycopene" else l + 6, name, fontsize=7, color=P.ink())
ax.set_xlim(3, 40)
ax.set_ylim(100, 1600)
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "number of conjugated atoms N", "λ(HOMO → LUMO) / nm")
charts.title(ax, "A   Longer boxes absorb redder light")

ax = axs[1]
N, a = 22, 0.14e-9
L = (N - 1) * a
E1 = h**2 / (8 * me * L**2) / 1.602176634e-19
for n in range(1, 15):
    E = n**2 * E1
    occ = n <= N // 2
    ax.plot([0.15, 0.85], [E, E], color=charts.line("protein") if occ else P.muted(), lw=1.4 if occ else 0.9)
    if occ:
        ax.plot([0.44, 0.56], [E, E], ls="none", marker="o", ms=2.5, color=charts.line("protein"))
En, Em = (N // 2) ** 2 * E1, (N // 2 + 1) ** 2 * E1
ax.annotate("", xy=(0.5, Em), xytext=(0.5, En), arrowprops=dict(arrowstyle="-|>", color=charts.line("rna"), lw=1.4))
ax.text(0.9, (En + Em) / 2, f"ΔE = {Em - En:.2f} eV\n(HOMO n = 11 →\n LUMO n = 12)", fontsize=7, va="center",
        color=P.ink())
ax.set_xlim(0, 1.6)
ax.set_ylim(0, 15**2 * E1 * 0.95)
ax.set_xticks([])
charts.style_axes(ax, None, "energy / eV")
charts.title(ax, "B   Levels of a 22-atom box")
fig.tight_layout()
