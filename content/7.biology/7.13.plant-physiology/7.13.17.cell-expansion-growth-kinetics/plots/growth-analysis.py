# Classical growth analysis of a simulated plant (illustrative parameters). Dry mass W grows with
# dW/dt = NAR * A, leaf area A = LAR * W; NAR declines slowly with self-shading and LAR declines as the plant
# invests more in stems and roots. (A) W on a log scale: its slope is RGR. (B) RGR = NAR x LAR, with the
# two components.
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 40, 401)
dt = t[1] - t[0]
W = np.empty_like(t)
W[0] = 0.05  # g
LAR = 0.030 * np.exp(-t / 45) + 0.008  # m2 g-1
NAR = 9.0 * (1 - 0.35 * t / 40)  # g m-2 d-1
for i in range(1, t.size):
    W[i] = W[i - 1] + dt * NAR[i - 1] * LAR[i - 1] * W[i - 1]
RGR = NAR * LAR
fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
a.semilogy(t, W, color="#2f6fb5", lw=2.4)
for t1, t2 in ((5, 10), (30, 35)):
    i1, i2 = int(t1 / dt), int(t2 / dt)
    r = (np.log(W[i2]) - np.log(W[i1])) / (t2 - t1)
    a.plot([t1, t2], [W[i1], W[i2]], "o", color="#c0504d", ms=6)
    a.annotate(f"mean RGR {t1}–{t2} d\n= {r:.3f} d⁻¹", xy=(t2, W[i2]), xytext=(t2 + 1, W[i2] / 12), fontsize=8.5,
               ha="left" if t1 < 20 else "right", arrowprops=dict(arrowstyle="-", color="0.5", lw=0.8))
a.set_xlabel("Time t / d")
a.set_ylabel("Plant dry mass W / g (log scale)")
a.set_xlim(0, 40)
a.set_title("A   Dry mass (slope of ln W = RGR)", loc="left", fontsize=10)
b.plot(t, RGR, color="black", lw=2.4, label="RGR = NAR × LAR / d⁻¹")
b.set_xlabel("Time t / d")
b.set_ylabel("RGR / d⁻¹")
b.set_ylim(0, 0.4)
b.set_xlim(0, 40)
b2 = b.twinx()
b2.plot(t, NAR / 30, color="#c0504d", lw=2, ls="--", label="NAR / (30 g m⁻² d⁻¹)")
b2.plot(t, LAR / 0.04, color="#3a9a5b", lw=2, ls="-.", label="LAR / (0.04 m² g⁻¹)")
b2.set_ylim(0, 1.05)
b2.set_ylabel("NAR and LAR (scaled)")
lines = b.get_lines() + b2.get_lines()
b.legend(lines, [l.get_label() for l in lines], frameon=False, fontsize=8.5, loc="lower left")
b.set_title("B   RGR decomposed", loc="left", fontsize=10)
a.spines[["top", "right"]].set_visible(False)
b.spines[["top"]].set_visible(False)
fig.tight_layout()
