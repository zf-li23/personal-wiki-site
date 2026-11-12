# Cyclical parthenogenesis in a monogonont rotifer, Eq. (12.1): density-dependent mixis in a population that
# depletes a non-renewed food supply (illustrative values).
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
r, Fh, a, d, mmax, Nc, h, c = 0.8, 0.3, 0.002, 0.15, 0.6, 40.0, 4.0, 1.0


def m(N):
    return mmax * N ** h / (N ** h + Nc ** h)


def f(y):
    A, M, F, E = y
    N = A + M
    b = r * F / (F + Fh)
    return np.array([b * A * (1 - m(N)) - d * A, b * A * m(N) - d * M, -a * N * F, c * M])


t = np.linspace(0, 40, 4001)
y = np.zeros((len(t), 4))
y[0] = [1.0, 0.0, 1.0, 0.0]
for i in range(1, len(t)):
    hs = t[i] - t[i - 1]
    k1 = f(y[i - 1]); k2 = f(y[i - 1] + hs / 2 * k1); k3 = f(y[i - 1] + hs / 2 * k2); k4 = f(y[i - 1] + hs * k3)
    y[i] = y[i - 1] + hs / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
A, M, F, E = y.T
N = A + M

fig, ax = bio.canvas(25, 9.6)
bio.panel(ax, "A", (0.2, 9.4))
pa = quant.Plot(ax, (2.0, 1.6, 9.6, 7.0), (0, 40), (0, 140), xlabel="Time (days)", ylabel="Females per mL",
                xticks=[0, 10, 20, 30, 40], yticks=[0, 40, 80, 120])
pa.line(t, A, token="dna", lw=1.8)
bio.label(ax, pa.xy(16.5, 70), "Amictic (asexual)", size="tiny", color=quant.line_color("dna"), ha="right")
pa.line(t, N, token="ink", lw=1.0, dotted=True, text="Total", at=0.36, dy=0.3)
pa.line(t, F * 100, token="positive", lw=1.2, dashed=True, text="Food (% of initial)", at=0.6, dy=0.3)
pa.line(t, M, token="negative", lw=1.8, text="Mictic (sexual)", at=0.62, dy=0.45)
pa.line([0, 40], [Nc, Nc], token="neutral", dashed=True, lw=1.0)
bio.label(ax, (pa.X(30.0), pa.Y(Nc) - 0.25), "critical density $N_{\\mathrm{c}}$", size="tiny", color=P.muted(), ha="left")

bio.panel(ax, "B", (13.0, 9.4))
pb = quant.Plot(ax, (14.8, 1.6, 8.6, 7.0), (0, 40), (0, 1), xlabel="Time (days)", ylabel="Fraction mictic  m(N)",
                xticks=[0, 10, 20, 30, 40], yticks=[0, 0.25, 0.5, 0.75, 1])
pb.line(t, m(N), token="negative", lw=1.8, text="m(N)", at=0.45, dy=0.3)
Emax = E.max()
pb.line(t, 0.98 * E / Emax, token="positive", lw=1.8, dashed=True, text="Resting eggs (cumulative, scaled)", at=0.75, dx=-3.0, dy=-0.55)
