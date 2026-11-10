# Two layers of self-tolerance as a linear kinetic model (illustrative parameters, relative units).
#   naive self-reactive T cells   dS/dt = theta (1 - delta) - (mu + alpha) S
#   self-reactive effectors       dE/dt = alpha S + (rho g - d) E,   g = 1 / (1 + R / K)
# theta: thymic output of self-reactive clones; delta: fraction removed by negative selection;
# mu: death of naive cells; alpha: rate at which naive cells are activated by self antigen;
# rho: expansion rate of activated effectors, suppressed by regulatory T cells R through g; d: effector loss.
# Panel A: the four combinations of central (delta) and peripheral (R) tolerance.
# Panel B: a schematic dose-response for low- and high-zone tolerance (shape only, no data).
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
theta, mu, alpha, rho, d, K = 1.0, 0.02, 0.002, 0.05, 0.03, 1.0
t = np.linspace(0, 720, 2000)
dt = t[1] - t[0]


def run(delta, R):
    g = 1 / (1 + R / K)
    S, E = 0.0, 0.0
    out = []
    for _ in t:
        out.append(E)
        dS = theta * (1 - delta) - (mu + alpha) * S
        dE = alpha * S + (rho * g - d) * E
        S, E = S + dt * dS, E + dt * dE
    return np.array(out)


cases = [(0.95, 4.0, "positive", "central + peripheral (normal)", "-"),
         (0.0, 4.0, "enzyme", "no negative selection (AIRE-like)", "--"),
         (0.95, 0.0, "rna", "no Treg (FOXP3-like)", "--"),
         (0.0, 0.0, "negative", "neither", "-")]

fig, ax = bio.canvas(24, 9.4)
bio.panel(ax, "A", (0.1, 9.2))
pa = quant.Plot(ax, (2.0, 1.6, 9.8, 6.6), (0, 720), (1e-2, 1e4), ylog=True, xlabel="Time / d",
                ylabel="Self-reactive effector T cells (rel.)", xticks=[0, 180, 360, 540, 720],
                yticks=[(1e-2, "10⁻²"), (1, "1"), (1e2, "10²"), (1e4, "10⁴")], grid=True)
for k, (delta, R, tok, txt, ls) in enumerate(cases):
    E = run(delta, R)
    m = E < 1e4
    pa.line(t[m], np.maximum(E[m], 1e-3), tok, lw=1.8, dashed=(ls == "--"))
    if E[-1] < 1e4:
        pa.text(725, max(E[-1], 1.2e-2), txt, ha="left", va="center", color=quant.line_color(tok))
    else:
        i = int(np.argmax(E > 1.5e3))
        pa.text(t[i] + 20, 1.5e3, txt, ha="left", va="center", color=quant.line_color(tok))
pa.hline(100, "muted", text="", side="right")
pa.text(10, 130, "illustrative threshold for tissue damage", ha="left", va="bottom", color=P.muted())

bio.panel(ax, "B", (16.0, 9.2))
x = np.linspace(-4, 4, 300)  # log10 antigen dose (arbitrary origin)
resp = np.exp(-((x - 0.3) ** 2) / 2.2)
pb = quant.Plot(ax, (17.6, 1.6, 5.8, 6.6), (-4, 4), (0, 1.15), xlabel="log₁₀ antigen dose (schematic)",
                ylabel="Immune response", xticks=[(-3.5, "low"), (0.3, "optimal"), (3.5, "high")], yticks=[0, 1])
pb.line(x, resp, "dna", lw=1.9)
pb.span(-4, -2.2, "positive", text="low-zone\ntolerance", text_y=pb.Y(1.08))
pb.span(2.6, 4, "positive", text="high-zone\ntolerance", text_y=pb.Y(1.08))
