# Macdonald-May model of schistosome transmission: dM/dt = mu M [R0 Phi(M,k) f(M,k,z) - 1], with the
# mating probability Phi for polygamous worms in negative-binomially distributed hosts (May 1977) and
# density-dependent fecundity f = (1 + M(1-z)/k)^-(k+1). k = 0.3, z = 0.99, mu = 0.2 per year.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
k, z, mu = 0.3, 0.99, 0.2
TH = np.linspace(0, 2 * np.pi, 2001)


def phi(M):
    a = M / (M + k)
    integrand = (1 - np.cos(TH)) / (1 + a * np.cos(TH)) ** (1 + k)
    return 1 - (1 - a) ** (1 + k) / (2 * np.pi) * np.trapezoid(integrand, TH)


def fec(M):
    return (1 + M * (1 - z) / k) ** (-(k + 1))


Ms = np.logspace(-3, 3, 500)
PHI = np.array([phi(m) for m in Ms])
F = fec(Ms)

fig, ax = bio.canvas(26, 10)
bio.panel(ax, "A", (0.2, 9.8))
pa = quant.Plot(ax, (2.2, 1.6, 9.6, 7.4), (1e-3, 1e3), (0, 3.4), xlog=True, ylabel="Net reproduction  $R_0\\Phi f$",
                xlabel="Mean worm burden M (worms per host)",
                xticks=[(1e-3, "0.001"), (1e-2, "0.01"), (1e-1, "0.1"), (1, "1"), (10, "10"), (100, "100"), (1000, "1000")],
                yticks=[0, 1, 2, 3])
pa.line([1e-3, 1e3], [1, 1], token="neutral", dashed=True, lw=1.0)
tokens = {2: "dna", 3: "negative", 5: "positive"}
for R0, tok in tokens.items():
    G = R0 * PHI * F
    pa.line(Ms, G, token=tok, lw=1.8)
    i = int(np.argmax(G))
    bio.label(ax, (pa.X(Ms[i]), pa.Y(G[i]) + 0.3), f"$R_0$ = {R0}", size="small", color=quant.line_color(tok))
    cr = np.flatnonzero(np.diff(np.sign(G - 1)))
    for j, c in enumerate(cr):
        x, y = pa.xy(Ms[c], 1.0)
        col = quant.line_color(tok)
        ax.plot(x, y, "o", ms=7, mfc=(P.surface() if j == 0 else col), mec=col, mew=1.5, zorder=14)
bio.label(ax, (pa.X(0.004), pa.Y(1.25)), "breakpoints", size="tiny", color=P.muted())
bio.label(ax, (pa.X(150), pa.Y(1.25)), "endemic\nequilibria", size="tiny", color=P.muted())

bio.panel(ax, "B", (13.6, 9.8))
pb = quant.Plot(ax, (15.6, 1.6, 9.6, 7.4), (0, 40), (1e-2, 100), ylog=True, xlabel="Time (years)",
                ylabel="Mean worm burden M", xticks=[0, 10, 20, 30, 40],
                yticks=[(0.01, "0.01"), (0.1, "0.1"), (1, "1"), (10, "10"), (100, "100")])
R0 = 3.0
G = R0 * PHI * F
Mb = Ms[np.flatnonzero(np.diff(np.sign(G - 1)))[0]]
pb.line([0, 40], [Mb, Mb], token="neutral", dashed=True, lw=1.0)
bio.label(ax, (pb.X(39.5), pb.Y(Mb) + 0.25), "breakpoint", size="tiny", color=P.muted(), ha="right")


def rhs(M):
    return mu * M * (R0 * np.interp(np.log(M), np.log(Ms), PHI) * fec(M) - 1)


t = np.linspace(0, 40, 2001)
for M0 in (0.05, 0.2, 0.28, 0.4, 0.6, 2.0, 80.0):
    M = np.empty_like(t)
    M[0] = M0
    for i in range(1, len(t)):
        h = t[i] - t[i - 1]
        m = M[i - 1]
        k1 = rhs(m); k2 = rhs(m + h / 2 * k1); k3 = rhs(m + h / 2 * k2); k4 = rhs(m + h * k3)
        M[i] = max(m + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4), 1.1e-3)
    pb.line(t, M, token="negative" if M0 > Mb else "dna", lw=1.5)
