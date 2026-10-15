import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.6))

# Left: multiplying by w = 1.3 e^{i pi/6} rotates by 30 degrees and scales by 1.3
w = 1.3 * np.exp(1j * np.pi / 6)
# A small "F"-shaped figure so that rotation and scaling are visible
strokes = [0.75 * s for s in (
    np.array([0.5 + 0.2j, 0.5 + 1.2j]),
    np.array([0.5 + 1.2j, 1.1 + 1.2j]),
    np.array([0.5 + 0.7j, 0.95 + 0.7j]),
)]
for k, (z_mult, c, lab) in enumerate([(1, "tab:blue", "shape S"),
                                      (w, "tab:orange", "w S"),
                                      (w**2, "tab:green", "w^2 S")]):
    for j, s in enumerate(strokes):
        seg = z_mult * s
        ax1.plot(seg.real, seg.imag, color=c, lw=3, label=lab if j == 0 else None)
for z_mult, c in [(1, "tab:blue"), (w, "tab:orange"), (w**2, "tab:green")]:
    p = z_mult * 0.75 * (0.5 + 0.2j)
    ax1.annotate("", xy=(p.real, p.imag), xytext=(0, 0),
                 arrowprops=dict(arrowstyle="->", color=c, lw=1.2, ls="--"))
ax1.annotate("", xy=(w.real, w.imag), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", color="tab:red", lw=2))
ax1.text(w.real + 0.05, w.imag - 0.15, "w", color="tab:red", fontsize=13)
ax1.axhline(0, color="gray", lw=0.6)
ax1.axvline(0, color="gray", lw=0.6)
ax1.set_aspect("equal")
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-0.3, 2.2)
ax1.set_xlabel("Re")
ax1.set_ylabel("Im")
ax1.grid(True, alpha=0.3)
ax1.legend(loc="upper left")
ax1.set_title("z -> w z with w = 1.3 e^(i pi/6): rotate 30 deg, scale 1.3")

# Right: 8th roots of unity are the vertices of a regular octagon and sum to zero
n = 8
k = np.arange(n)
omega = np.exp(2j * np.pi * k / n)
th = np.linspace(0, 2 * np.pi, 400)
ax2.plot(np.cos(th), np.sin(th), color="gray", lw=0.8)
poly = np.append(omega, omega[0])
ax2.plot(poly.real, poly.imag, color="tab:blue", lw=1.5)
ax2.plot(omega.real, omega.imag, "o", color="tab:blue", ms=8)
for kk, z in zip(k, omega):
    ax2.text(1.17 * z.real - 0.08, 1.17 * z.imag - 0.04, f"w^{kk}", fontsize=11)
# Head-to-tail sum of the roots closes up: 1 + w + ... + w^7 = 0
partial = np.concatenate([[0], np.cumsum(omega)]) * 0.35
ax2.plot(partial.real, partial.imag, color="tab:orange", lw=2,
         label="partial sums (scaled 0.35) return to 0")
ax2.plot([0], [0], "o", color="tab:orange", ms=6)
ax2.axhline(0, color="gray", lw=0.6)
ax2.axvline(0, color="gray", lw=0.6)
ax2.set_aspect("equal")
ax2.set_xlim(-1.45, 1.45)
ax2.set_ylim(-1.45, 1.45)
ax2.set_xlabel("Re")
ax2.set_ylabel("Im")
ax2.legend(loc="lower left", fontsize=9)
ax2.set_title("8th roots of unity w^k, w = e^(2 pi i/8)")
fig.tight_layout()
