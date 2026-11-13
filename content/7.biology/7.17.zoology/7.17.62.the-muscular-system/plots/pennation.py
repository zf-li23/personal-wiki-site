# Model of a unipennate muscle in a fixed envelope (Example 62.7.1): force along the line of action and fibre
# length relative to a parallel-fibred muscle, as functions of the pennation angle. Model, not data.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22, 8.6)

# ---------------- geometry (left)
bio.panel(ax, "A", (0.3, 8.2))
bio.label(ax, (0.9, 8.2), "Same envelope, two architectures", size="title", ha="left")
L, t = 6.5, 1.3
for y0, title, pennate in ((5.6, "parallel-fibred", False), (2.2, "unipennate", True)):
    x0 = 1.2
    bio.label(ax, (x0, y0 + t + 0.45), title, size="small", ha="left")
    box = np.array([(x0, y0), (x0 + L, y0), (x0 + L, y0 + t), (x0, y0 + t)])
    bio.shape(ax, box, token="muscle", zorder=3, lw=0.8)
    if not pennate:
        for k in range(1, 6):
            y = y0 + t * k / 6
            ax.plot([x0 + 0.1, x0 + L - 0.1], [y, y], color=P.on_fill(), lw=0.9, zorder=4)
        bio.label(ax, (x0 + L / 2, y0 - 0.35), "fibre length L, PCSA = t", size="tiny")
    else:
        th = np.radians(30)
        dx = t / np.tan(th)
        for k in range(0, 12):
            xa = x0 + 0.1 + k * (L - dx - 0.2) / 11
            ax.plot([xa, xa + dx], [y0 + 0.04, y0 + t - 0.04], color=P.on_fill(), lw=0.9, zorder=4)
        for yy in (y0, y0 + t):
            ax.plot([x0 - 0.2, x0 + L + 0.2], [yy, yy], color=P.ink(), lw=2.2, zorder=5)
        a0 = (x0 + 0.1 + 5 * (L - dx - 0.2) / 11, y0 + 0.04)
        arc = np.linspace(0, th, 20)
        ax.plot(a0[0] + 0.7 * np.cos(arc), a0[1] + 0.7 * np.sin(arc), color=P.ink(), lw=0.9, zorder=6)
        bio.label(ax, (a0[0] + 0.95, a0[1] + 0.22), "θ", size="small")
        bio.label(ax, (x0 + L / 2, y0 - 0.35), "fibres t / sin θ, PCSA = L sin θ (aponeuroses dark)", size="tiny")
    ax.annotate("", (x0 + L + 0.6, y0), (x0 + L + 0.6, y0 + t), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.8))
    bio.label(ax, (x0 + L + 0.85, y0 + t / 2), "t", size="small", ha="left")
bio.label(ax, (1.2 + L / 2, 0.95), "envelope length L, thickness t", size="tiny", color=P.muted())

# ---------------- model (right)
bio.panel(ax, "B", (10.6, 8.2))
p = quant.Plot(ax, (12.2, 1.4, 8.8, 5.8), xlim=(0, 90), ylim=(0, 2.6), xlabel="pennation angle θ / °",
               ylabel="relative to parallel muscle", xticks=[0, 15, 30, 45, 60, 75, 90], yticks=[0, 0.5, 1, 1.5, 2, 2.5])
p.span(5, 30, "highlight", text="typical", strength=0.35)
th = np.linspace(1, 89, 200)
r = 5.0
force = r * np.sin(np.radians(th)) * np.cos(np.radians(th))
fib = 1 / (r * np.sin(np.radians(th)))
p.line(th, force, "muscle", text="force (L/t = 5)", at=0.62, dy=0.15)
p.line(th, fib, "dna", dashed=True, text="fibre length / L", at=0.75, dy=0.12)
p.hline(1.0, text="parallel muscle", side="right")
p.points([45], [r / 2], "muscle", r=0.09)
