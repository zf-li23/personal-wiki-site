"""Seven circuit motifs simulated with the same threshold-linear rate model,
tau dr/dt = -r + [sum_j w_j r_j + input]_+ (tau = 10 ms for every cell), driven by a step of
input from 50 to 250 ms (shaded). Each panel shows the response of the output cell B (and other
cells where relevant). The lateral-inhibition panel shows a spatial profile instead: a row of 41
cells receiving a step edge in input, each inhibited by its neighbours within 3 cells."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
dt, T, tau = 0.1, 350.0, 10.0
t = np.arange(0, T, dt)
step = ((t >= 50) & (t < 250)).astype(float)
relu = lambda x: np.maximum(x, 0.0)


def run(f, n):
    r = np.zeros((len(t), n))
    for _ in range(5000):  # start from the steady state without input
        r[0] = r[0] + dt / tau * (-r[0] + relu(f(r[0], 0.0, 0)))
    for k in range(1, len(t)):
        r[k] = r[k - 1] + dt / tau * (-r[k - 1] + relu(f(r[k - 1], step[k - 1], k)))
    return r


models = []
# 1 feedforward excitation: A -> B
models.append(("Feedforward excitation", "A → B",
               run(lambda r, s, k: np.array([s, 1.0 * r[0]]), 2), [(1, "B", "neuron"), (0, "A", "neutral")]))
# 2 recurrent excitation: B -> B (w = 0.8)
models.append(("Recurrent excitation", "input → B, B → B (w = 0.8)",
               run(lambda r, s, k: np.array([0.2 * s + 0.8 * r[0]]), 1), [(0, "B", "neuron")]))
# 3 feedforward inhibition: input -> B, input -> I, I -| B (slower interneuron)
models.append(("Feedforward inhibition", "input → B, input → I ⊣ B",
               run(lambda r, s, k: np.array([s - 1.5 * r[1], 0.6 * s + 0.4 * r[1]]), 2), [(0, "B", "neuron"), (1, "I", "negative")]))
# 4 feedback inhibition: input -> B, B -> I, I -| B
models.append(("Feedback inhibition", "input → B → I ⊣ B",
               run(lambda r, s, k: np.array([s - 2.0 * r[1], 1.0 * r[0]]), 2), [(0, "B", "neuron"), (1, "I", "negative")]))
# 5 disinhibition: tonic I1 -| B; input -> I2 -| I1
models.append(("Disinhibition", "input → I2 ⊣ I1 ⊣ B (B tonically driven)",
               run(lambda r, s, k: np.array([1.0 - 2.0 * r[1], 1.0 - 3.0 * r[2], s]), 3), [(0, "B", "neuron"), (1, "I1", "negative")]))
# 6 reciprocal inhibition with adaptation (half-centre oscillator)
ta = 150.0
def recip():
    r = np.zeros((len(t), 2)); a = np.zeros(2); r[0] = [0.1, 0.0]
    for k in range(1, len(t)):
        s = step[k - 1]
        inp = np.array([s - 2.5 * r[k - 1, 1] - a[0], s - 2.5 * r[k - 1, 0] - a[1]])
        r[k] = r[k - 1] + dt / tau * (-r[k - 1] + relu(inp))
        a = a + dt / ta * (-a + 2.5 * r[k - 1])
    return r
models.append(("Reciprocal inhibition", "B1 ⊣ B2, B2 ⊣ B1, with adaptation", recip(), [(0, "B1", "neuron"), (1, "B2", "dna")]))

fig, axs = plt.subplots(2, 4, figsize=(11.6, 5.0))
fig.subplots_adjust(wspace=0.32, hspace=0.75, left=0.06, right=0.99, bottom=0.11, top=0.88)
for ax, (name, wiring, r, traces) in zip(axs.flat, models):
    ax.axvspan(50, 250, color=P.mix(P.muted(), P.surface(), 0.85), lw=0)
    for idx, lab, tok in traces:
        ax.plot(t, r[:, idx], color=charts.line(tok), lw=1.6, label=lab)
    ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right", handlelength=1.2)
    ax.set_ylim(bottom=-0.02)
    ax.set_xlim(0, T)
    charts.style_axes(ax, "t / ms", "rate (a.u.)")
    ax.text(0.0, 1.15, name, transform=ax.transAxes, fontsize=FT["small"], color=P.ink(), weight="bold", va="bottom", ha="left")
    ax.text(0.0, 1.03, wiring, transform=ax.transAxes, fontsize=FT["tiny"], color=P.muted(), va="bottom", ha="left")

# 7 lateral inhibition (spatial)
ax = axs.flat[6]
n = 41
x = np.arange(n) - n // 2
inp = np.where(x >= 0, 1.0, 0.3)
W = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if 0 < abs(i - j) <= 3:
            W[i, j] = 0.12
r = np.zeros(n)
for _ in range(3000):
    r = r + 0.05 * (-r + relu(inp - W @ r))
sl = slice(8, n - 8)
ax.plot(x[sl], inp[sl], color=charts.line("neutral"), lw=1.3, ls="--", label="input")
ax.plot(x[sl], r[sl], color=charts.line("neuron"), lw=1.6, marker="o", ms=2.5, label="output")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left", handlelength=1.2)
charts.style_axes(ax, "cell position", "rate (a.u.)")
ax.text(0.0, 1.15, "Lateral inhibition", transform=ax.transAxes, fontsize=FT["small"], color=P.ink(), weight="bold", va="bottom", ha="left")
ax.text(0.0, 1.03, "neighbours within 3 cells ⊣ each other", transform=ax.transAxes, fontsize=FT["tiny"], color=P.muted(), va="bottom", ha="left")

# 8 convergence / divergence: summary of gains
ax = axs.flat[7]
nin = np.arange(1, 21)
ax.plot(nin, nin * 0.1, color=charts.line("neuron"), lw=1.6, label="convergence: drive ∝ inputs")
ax.plot(nin, np.sqrt(nin) * 0.1, color=charts.line("highlight"), lw=1.6, ls="--", label="noise s.d. ∝ √inputs")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left", handlelength=1.6)
charts.style_axes(ax, "number of converging inputs", "B input (a.u.)")
ax.text(0.0, 1.15, "Convergence", transform=ax.transAxes, fontsize=FT["small"], color=P.ink(), weight="bold", va="bottom", ha="left")
ax.text(0.0, 1.03, "N independent inputs → B", transform=ax.transAxes, fontsize=FT["tiny"], color=P.muted(), va="bottom", ha="left")
