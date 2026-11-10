# Positive feedback in the interferon response (Example 6.6.1): dx/dt = s + alpha x^n/(K^n + x^n) - delta x,
# dimensionless. A: rate balance at s = 0 (three fixed points). B: responses to transient inputs of different
# strength. C: bifurcation diagram x* vs s (saddle-node, hysteresis).
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import quant

P = bio.P
N, ALPHA, K, DELTA = 2, 1.0, 0.4, 1.0
fig, ax = bio.canvas(24.0, 7.6)


def prod(x, s=0.0):
    return s + ALPHA * x ** N / (K ** N + x ** N)


# fixed points at s = 0: x = 0 and the roots of x^2 - x + K^2 = 0 (for delta = alpha = 1): 0.2 and 0.8
r = np.roots([1, -1, K ** 2])
x_lo, x_hi = sorted(r.real)

# ---- A ------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 7.5))
pa = quant.Plot(ax, (1.6, 1.4, 5.6, 5.4), xlim=(0, 1.2), ylim=(0, 1.2), xlabel="interferon output x",
                ylabel="rate", xticks=[0, 0.5, 1.0], yticks=[0, 0.5, 1.0])
xs = np.linspace(0, 1.2, 400)
pa.line(xs, prod(xs), "dna", lw=2.0)
pa.line(xs, DELTA * xs, "drug", lw=2.0)
pa.points([0, x_hi], [0, x_hi], "ink", r=0.11)
pa.points([x_lo], [x_lo], "ink", r=0.11, hollow=True)
pa.text(1.18, 0.76, "production", size="tiny", ha="right", color=quant.line_color("dna"))
pa.text(1.0, 1.12, "decay δx", size="tiny", ha="right", color=quant.line_color("drug"))
pa.text(x_lo + 0.03, x_lo - 0.1, "threshold", size="tiny", ha="left")

# ---- B ------------------------------------------------------------------------------------------
bio.panel(ax, "B", (8.2, 7.5))
pb = quant.Plot(ax, (9.6, 1.4, 6.0, 5.4), xlim=(0, 12), ylim=(0, 1.1), xlabel="time (dimensionless)",
                ylabel="x", xticks=[0, 2, 4, 8, 12], yticks=[0, 0.5, 1.0])
pb.span(2, 4, "highlight", text="virus input", strength=0.4)


def run(s0):
    f = lambda t, y: [prod(y[0], s0 if 2 <= t <= 4 else 0.0) - DELTA * y[0]]
    sol = solve_ivp(f, (0, 12), [0.0], max_step=0.02)
    return sol.t, sol.y[0]


for k_, (s0, tok) in enumerate(((0.05, "dna2"), (0.12, "dna"), (0.15, "protein"))):
    t, y = run(s0)
    pb.line(t, y, tok, lw=2.0)
    pb.text(9.3, [0.04, 0.12, 0.84][k_], f"s = {s0:g}", size="tiny", ha="left", color=quant.line_color(tok))
pb.hline(x_lo, "muted", text="threshold", side="left")

# ---- C ------------------------------------------------------------------------------------------
bio.panel(ax, "C", (16.6, 7.5))
pc = quant.Plot(ax, (18.0, 1.4, 5.6, 5.4), xlim=(0, 0.2), ylim=(0, 1.2), xlabel="viral input s",
                ylabel="steady state x*", xticks=[0, 0.05, 0.1, 0.15, 0.2], yticks=[0, 0.5, 1.0])
# parametrize by x: s(x) = delta x - alpha x^n/(K^n+x^n)
xx = np.linspace(0, 1.2, 2000)
ss = DELTA * xx - ALPHA * xx ** N / (K ** N + xx ** N)
ds = np.gradient(ss, xx)
stable = ds > 0
for mask, dashed in ((stable & (xx < 0.5), False), (~stable, True), (stable & (xx > 0.5), False)):
    m = mask & (ss >= 0) & (ss <= 0.2)
    pc.line(ss[m], xx[m], "dna", lw=2.0, dashed=dashed)
pc.text(0.1, 1.08, "high (antiviral) state", size="tiny", ha="center")
pc.text(0.045, 0.02, "resting state", size="tiny", ha="left")
