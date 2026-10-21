import matplotlib.pyplot as plt

Tc = 10.0
t_pcq, t_pd, t_su = 2.0, 5.0, 1.5
H = 0.8
RISE = 0.15
fig, ax = plt.subplots(figsize=(8.6, 3.4))

# clock with rising edges at 0 and Tc
cb = 2.8
clk_x = [-2.0, 0.0, RISE, Tc / 2, Tc / 2 + RISE, Tc, Tc + RISE, Tc + 1.8]
clk_y = [0, 0, 1, 1, 0, 0, 1, 1]
ax.plot(clk_x, [cb + H * v for v in clk_y], color="C0", lw=1.8)
ax.text(-2.2, cb + H / 2, "CLK", ha="right", va="center")


def bus(base, change_at, width, color, end=Tc + 1.8):
    a, b = change_at, change_at + width
    ax.plot([-2.0, a], [base, base], color=color, lw=1.6)
    ax.plot([-2.0, a], [base + H, base + H], color=color, lw=1.6)
    ax.plot([a, b], [base, base + H], color=color, lw=1.2)
    ax.plot([a, b], [base + H, base], color=color, lw=1.2)
    ax.plot([b, end], [base, base], color=color, lw=1.6)
    ax.plot([b, end], [base + H, base + H], color=color, lw=1.6)


bus(1.5, t_pcq - 0.3, 0.3, "C1")
ax.text(-2.2, 1.5 + H / 2, "Q1", ha="right", va="center")
bus(0.2, t_pcq + t_pd - 0.3, 0.3, "C2")
ax.text(-2.2, 0.2 + H / 2, "D2", ha="right", va="center")

for x in [0, Tc]:
    ax.axvline(x, color="0.55", ls="--", lw=0.8)


def dim(x0, x1, y, label):
    ax.annotate("", xy=(x0, y), xytext=(x1, y), arrowprops=dict(arrowstyle="<->", lw=1.0, color="0.35"))
    ax.text((x0 + x1) / 2, y + 0.08, label, ha="center", va="bottom", fontsize=10)


dim(0, t_pcq, 2.45, r"$t_{\mathrm{pcq}}$")
dim(t_pcq, t_pcq + t_pd, 1.1, r"$t_{\mathrm{pd}}$ (logic)")
dim(Tc - t_su, Tc, 1.1, r"$t_{\mathrm{su}}$")
dim(t_pcq + t_pd, Tc - t_su, -0.25, "slack")
dim(0, Tc, 3.95, r"$T_{\mathrm{c}}$")
ax.axvspan(Tc - t_su, Tc, color="C2", alpha=0.10, lw=0)
ax.set_xlim(-3.4, Tc + 1.9)
ax.set_ylim(-0.6, 4.5)
ax.axis("off")
ax.set_title("FF1 launches at the first edge; D2 must settle t_su before the next edge", fontsize=10)
fig.tight_layout()
