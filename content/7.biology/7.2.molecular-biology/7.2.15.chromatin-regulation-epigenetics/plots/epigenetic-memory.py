# Epigenetic memory from read-write feedback: the model of Dodd, Micheelsen, Sneppen and Thon (2007).
# N = 60 nucleosomes in states M (0), U (1), A (2). Each event: pick n1; with probability alpha a recruited
# conversion (pick n2 at random; if n2 = M move n1 one step toward M, if n2 = A one step toward A); otherwise a noisy
# conversion (n1 moves one step to a random neighbouring state). F = alpha / (1 - alpha). Every 100 sweeps a cell
# division replaces each nucleosome by U with probability 1/2. A: F = 1; B: F = 4 (traces of the M fraction).
# C: histograms of (fraction M - fraction A) sampled every sweep over long runs.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
N = 60
DIV = 100


def run(F, sweeps, seed):
    rng = np.random.default_rng(seed)
    alpha = F / (1 + F)
    s = np.full(N, 1)
    s[: N // 2] = 0
    nM, nA = [], []
    r_pick = rng.integers(0, N, size=(sweeps, N, 2))
    r_u = rng.random((sweeps, N, 2))
    for t in range(sweeps):
        if t % DIV == 0 and t > 0:
            s[rng.random(N) < 0.5] = 1
        for k in range(N):
            i, j = r_pick[t, k]
            if r_u[t, k, 0] < alpha:
                if s[j] == 0 and s[i] > 0:
                    s[i] -= 1
                elif s[j] == 2 and s[i] < 2:
                    s[i] += 1
            else:
                if s[i] == 1:
                    s[i] = 0 if r_u[t, k, 1] < 0.5 else 2
                else:
                    s[i] = 1
        nM.append(np.mean(s == 0))
        nA.append(np.mean(s == 2))
    return np.array(nM), np.array(nA)


fig, ax = bio.canvas(22.0, 10.0)
T = 3000
res = {F: run(F, T, 1) for F in (1.0, 4.0)}
long = {F: run(F, 8000, 2) for F in (1.0, 4.0)}

for k, (F, tok, letter) in enumerate([(1.0, "neutral", "A"), (4.0, "chromatin", "B")]):
    y = 5.6 - 4.4 * k
    a = C.axes_at(ax, (1.5, y, 11.6, 3.1))
    m, _ = res[F]
    a.plot(np.arange(T), m, color=C.line(tok), lw=0.9)
    for d in range(DIV, T, DIV):
        a.plot([d, d], [1.02, 1.08], color=P.muted(), lw=0.6, clip_on=False)
    a.set_xlim(0, T)
    a.set_ylim(0, 1.0)
    a.set_yticks([0, 0.5, 1])
    C.style_axes(a, "time / sweeps (one division every 100 sweeps)" if k == 1 else None, "fraction M")
    bio.panel(ax, letter, (0.1, y + 3.95))
    bio.label(ax, (0.6, y + 3.6), f"F = {F:g}" + ("  (weak feedback)" if F < 2 else "  (strong feedback: bistable)"),
              size="normal", bold=True, ha="left")

c = C.axes_at(ax, (15.6, 1.2, 5.8, 7.5))
bins = np.linspace(-1, 1, 31)
for F, tok in [(1.0, "neutral"), (4.0, "chromatin")]:
    m, aa = long[F]
    c.hist(m - aa, bins=bins, density=True, color=P.fill(tok), edgecolor=C.line(tok), lw=0.7, alpha=0.75,
           label=f"F = {F:g}")
c.set_xlim(-1, 1)
C.style_axes(c, "fraction M − fraction A", "probability density")
c.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper center")
bio.panel(ax, "C", (14.3, 9.9))
bio.label(ax, (14.8, 9.55), "State distribution", size="normal", bold=True, ha="left")
