# An antenna as a random walk of the excitation on a lattice with a trap (master-equation model).
# Sites: an L x L square lattice (N = L^2 pigments, periodic boundaries, i.e. a tiling of identical
# photosynthetic units) with the reaction center (RC) at the center. Hopping between nearest neighbours
# obeys detailed balance, k(i -> j) = k0 exp[-(E_j - E_i) / 2kT], k0 = (0.5 ps)^-1. Funnel: site energies
# rise linearly with the distance from the RC, E_i = eps * r_i / r_max. From the RC the excitation is trapped
# by charge separation at k_cs = (1 ps)^-1; everywhere it decays (fluorescence, heat) at 1/tau0, tau0 = 2 ns.
# The excitation starts on a random site (uniform absorption). The time-integrated populations x solve
# M x = -p(0), where M is the rate matrix; the trapping yield is Phi = k_cs x_RC and the mean time to
# trapping or decay is sum(x).
# A: site energies of a funnel with eps = 3 kT (L = 15) and the time-integrated occupation (log scale):
#    the excitation spends its time near the RC.
# B: quantum yield of trapping against the antenna size N for several funnel depths.
# C: mean trapping time for a flat antenna, compared with Montroll's mean number of steps of a random walk
#    to a single trap on a periodic square lattice, <n> = (N/pi) ln N + 0.195 N, converted to time as
#    <n> / (4 k0), plus the trap-limited time N / k_cs of an excitation spread
#    evenly over the antenna (the two times add; Pearlstein).
import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

import wikibio as bio
from wikibio import charts

P = bio.P
k0, kcs, tau0 = 2.0, 1.0, 2000.0   # ps^-1, ps^-1, ps


def solve(L, eps):
    N = L * L
    c = L // 2
    ii, jj = np.meshgrid(np.arange(L), np.arange(L), indexing="ij")
    di = np.minimum(abs(ii - c), L - abs(ii - c))
    dj = np.minimum(abs(jj - c), L - abs(jj - c))
    r = np.hypot(di, dj).ravel()
    E = eps * r / max(r.max(), 1)
    idx = lambda a, b: (a % L) * L + (b % L)
    M = lil_matrix((N, N))
    for a in range(L):
        for b in range(L):
            i = idx(a, b)
            out = 1 / tau0 + (kcs if i == idx(c, c) else 0.0)
            for da, db in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                j = idx(a + da, b + db)
                k = k0 * np.exp(-(E[j] - E[i]) / 2)
                M[j, i] += k
                out += k
            M[i, i] -= out
    p0 = np.full(N, 1.0 / N)
    x = spsolve(M.tocsc(), -p0)
    return kcs * x[idx(c, c)], x.sum(), E.reshape(L, L), x.reshape(L, L)


fig, axs = plt.subplots(1, 3, figsize=(13.4, 4.0), gridspec_kw=dict(width_ratios=[1.0, 1.1, 1.1]))
ax = axs[0]
phi, tm, E, x = solve(15, 3.0)
im = ax.imshow(np.log10(x / x.sum()), cmap="viridis", origin="lower")
cs = ax.contour(E, levels=[0.6, 1.2, 1.8, 2.4], colors=[P.on_fill()], linewidths=0.6)
ax.plot(7, 7, marker="*", ms=11, color=charts.line("atp"))
ax.set_xticks([])
ax.set_yticks([])
cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.03)
cb.ax.tick_params(labelsize=7, colors=P.muted(), labelcolor=P.ink())
cb.set_label("log₁₀ time-integrated occupation", fontsize=7, color=P.ink())
charts.title(ax, f"A   Funnel 3 kT, N = 225: Φ = {phi:.3f}")

ax = axs[1]
Ls = np.array([5, 7, 9, 11, 15, 19, 25, 31])
cols = ["neutral", "dna", "enzyme", "rna"]
for eps, tok in zip([0.0, 1.0, 3.0, 6.0], cols):
    ph = [solve(L, eps)[0] for L in Ls]
    ax.plot(Ls**2, ph, "o-", ms=3.5, lw=1.5, color=charts.line(tok), label=f"funnel depth {eps:.0f} kT")
ax.set_xscale("log")
ax.set_ylim(0.5, 1.0)
ax.legend(fontsize=7, frameon=False, loc="lower left")
charts.style_axes(ax, "pigments per reaction center N", "trapping yield Φ")
charts.title(ax, "B   Yield falls slowly with antenna size")

ax = axs[2]
tm = [solve(L, 0.0)[1] for L in Ls]
N = Ls**2.0
mont = ((N / np.pi) * np.log(N) + 0.195 * N) / (4 * k0) + N / kcs
ax.plot(N, tm, "o", ms=4, color=charts.line("dna"), label="master equation (flat)")
ax.plot(N, 1 / (1 / mont + 1 / tau0), color=charts.line("rna"), lw=1.4, label="Montroll walk + N/k_cs, with decay")
tm3 = [solve(L, 3.0)[1] for L in Ls]
ax.plot(N, tm3, "s", ms=3.5, color=charts.line("enzyme"), label="funnel 3 kT")
ax.set_xscale("log")
ax.set_yscale("log")
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "pigments per reaction center N", "mean time to trapping / ps")
charts.title(ax, "C   Search time grows as N ln N")
fig.tight_layout()
