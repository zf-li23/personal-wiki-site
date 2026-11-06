# Douady-Couder model of phyllotaxis (Douady & Couder 1996, discrete version). Primordia appear one per
# plastochron T on a circle of radius R0 at the edge of the apex; existing primordia move outwards, their
# radius growing by a factor exp(G) per plastochron (G = growth during one plastochron, dimensionless).
# Each new primordium appears where the inhibition E(theta) = sum_j 1/d_j^3 from the existing primordia is
# lowest (Hofmeister's rule). (A) Bifurcation diagram: divergence angle reached after the transient, for
# runs started from a distichous (alternate) and from a slightly asymmetric initial pair. Large G gives
# 180 degrees; as G decreases the angle bifurcates, and the main branch converges to 137.5 degrees (Fibonacci
# spirals), a minor branch to 99.5 degrees (Lucas). (B) Pattern simulated at G = 0.2 seen from above (dashed circle: radius R0).
import matplotlib.pyplot as plt
import numpy as np

GOLD = 360 * (1 - 2 / (1 + 5 ** 0.5))
grid = np.radians(np.linspace(0, 360, 1440, endpoint=False))


def run(G, th0, n=90, keep=40):
    r = [np.exp(G), 1.0]
    th = list(np.radians(th0))
    for _ in range(n):
        r = [x * np.exp(G) for x in r]
        R = np.array(r[-keep:])
        T = np.array(th[-keep:])
        dx = np.cos(grid)[:, None] - R * np.cos(T)
        dy = np.sin(grid)[:, None] - R * np.sin(T)
        E = (1 / (dx ** 2 + dy ** 2) ** 1.5).sum(1)
        th.append(grid[np.argmin(E)])
        r.append(1.0)
    return np.array(r), np.array(th)


def divergence(th, last=12):
    d = np.degrees(np.diff(th[-last:])) % 360
    d = np.where(d > 180, 360 - d, d)
    return d.mean(), d.std()


fig, (a, b) = plt.subplots(1, 2, figsize=(11.5, 4.8), gridspec_kw=dict(width_ratios=[1.35, 1]))
Gs = np.logspace(np.log10(0.03), np.log10(2.0), 70)
for th0, col, name in (((0, 180), "#2f6fb5", "start: distichous pair"), ((0, 150), "#c0504d", "start: asymmetric pair"),
                       ((0, 95), "#3a9a5b", "start: small angle")):
    pts = []
    for G in Gs:
        m, s = divergence(run(G, th0)[1])
        if s < 3:
            pts.append((G, m))
    pts = np.array(pts)
    a.plot(pts[:, 0], pts[:, 1], "o", ms=4, color=col, label=name, alpha=0.85)
a.axhline(GOLD, color="0.5", lw=0.9, ls="--")
a.text(2.05, GOLD, "137.5°", va="center", fontsize=8.5, color="0.4")
a.axhline(99.5, color="0.5", lw=0.9, ls=":")
a.text(2.05, 99.5, "99.5°", va="center", fontsize=8.5, color="0.4")
a.set_xscale("log")
a.set_xlim(0.03, 2.6)
a.set_ylim(60, 190)
a.set_xlabel("Growth per plastochron G (dimensionless)")
a.set_ylabel("Divergence angle / °")
a.legend(frameon=False, fontsize=8.5, loc="lower right")
a.set_title("A   Bifurcation diagram (only converged runs)", loc="left", fontsize=10)
r, th = run(0.2, (0, 180), n=150)
a.axvline(0.2, color="0.6", lw=0.8, ls="-.")
x, y = r * np.cos(th), r * np.sin(th)
sel = r < 13
b.scatter(x[sel], y[sel], s=(r[sel] * 9) ** 1.25, c=np.arange(sel.sum())[::-1], cmap="viridis", edgecolor="0.3", lw=0.4)
b.add_patch(plt.Circle((0, 0), 1, fill=False, ls="--", color="0.5", lw=0.8))
m, _ = divergence(th)
b.set_title(f"B   Pattern at G = 0.2 (divergence {m:.1f}°)", loc="left", fontsize=10)
b.set_aspect("equal")
b.set_xlim(-15, 15)
b.set_ylim(-15, 15)
b.axis("off")
a.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
