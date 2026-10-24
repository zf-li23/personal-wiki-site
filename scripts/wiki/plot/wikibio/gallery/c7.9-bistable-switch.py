# A bistable genetic toggle switch: the network motif (two mutually repressing genes, a signal S that
# boosts V), the phase plane with nullclines, flow and the separatrix, and the hysteresis of the
# steady state as S is swept up and down (saddle-node bifurcations).
import numpy as np

import wikibio as bio
from wikibio import network, quant

P = bio.P
fig, ax = bio.canvas(24.5, 9.6)

# ---- model (dimensionless): du/dt = a/(1+v^n) - u,  dv/dt = s a/(1+u^n) - v ------------------------
a, n = 10.0, 2.0


def rhs(u, v, s):
    return a / (1 + v**n) - u, s * a / (1 + u**n) - v


def fixed_points(s):
    """All steady states (u, v, stable) for signal s, by root bracketing of u = a/(1 + v(u)^n)."""
    u = np.logspace(-5, np.log10(a * 1.2), 6000)
    v = s * a / (1 + u**n)
    F = a / (1 + v**n) - u
    out = []
    for j in np.flatnonzero(np.sign(F[:-1]) != np.sign(F[1:])):
        lo, hi = u[j], u[j + 1]
        for _ in range(50):  # bisection
            mid = (lo + hi) / 2
            fm = a / (1 + (s * a / (1 + mid**n)) ** n) - mid
            flo = a / (1 + (s * a / (1 + lo**n)) ** n) - lo
            lo, hi = (lo, mid) if np.sign(fm) != np.sign(flo) else (mid, hi)
        uu = (lo + hi) / 2
        vv = s * a / (1 + uu**n)
        J = np.array([[-1, -a * n * vv ** (n - 1) / (1 + vv**n) ** 2], [-s * a * n * uu ** (n - 1) / (1 + uu**n) ** 2, -1]])
        out.append((uu, vv, bool(np.all(np.linalg.eigvals(J).real < 0))))
    return out


# ---- A: motif and equations --------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 9.5))
network.motif(ax, "toggle", (3.4, 6.5), size=4.4, names=("U", "V"), inputs={"V": "S"})
bio.box(ax, (3.4, 2.2), 6.0, 2.2, "neutral")
bio.label(ax, (3.4, 2.75), "$\\dfrac{\\mathrm{d}u}{\\mathrm{d}t} = \\dfrac{a}{1 + v^{n}} - u$", size="small", color=P.on_fill())
bio.label(ax, (3.4, 1.6), "$\\dfrac{\\mathrm{d}v}{\\mathrm{d}t} = \\dfrac{s\\,a}{1 + u^{n}} - v$", size="small", color=P.on_fill())
bio.label(ax, (3.4, 0.7), f"$a$ = {a:g},  $n$ = {n:g} (cooperativity)", size="tiny", color=P.muted())

# ---- B: phase plane at s = 1 ---------------------------------------------------------------------------
s0 = 1.0
X0, Y0, S = 9.2, 1.3, 6.6
pp = quant.Plot(ax, (X0, Y0, S, S), (0, 11), (0, 11), xlabel="$u$ (U protein)", ylabel="$v$ (V protein)",
                xticks=[0, 5, 10], yticks=[0, 5, 10])
bio.panel(ax, "B", (X0 - 1.5, 9.5))
g = np.linspace(0, 11, 40)
U, V = np.meshgrid(g, g)
du, dv = rhs(U, V, s0)
ax.streamplot(pp.X(g), pp.Y(g), du * S / 11, dv * S / 11, density=0.75, color=P.mix(P.muted(), P.surface(), 0.35),
              linewidth=0.6, arrowsize=0.7, zorder=4)
vv = np.linspace(0, 11, 400)
pp.line(a / (1 + vv**n), vv, P.protein(1), lw=2.0)
uu = np.linspace(0, 11, 400)
pp.line(uu, s0 * a / (1 + uu**n), P.protein(2), lw=2.0)
pp.line([0, 11], [0, 11], "muted", lw=1.0, dashed=True)  # separatrix: the diagonal, by symmetry at s = 1
pp.text(10.4, 9.6, "separatrix", ha="right", va="bottom", color=P.muted(), rotation=45)
pp.text(5.6, 1.45, "$\\dot u = 0$", ha="left", token=P.protein(1), size="small")
pp.text(1.75, 6.6, "$\\dot v = 0$", ha="left", va="center", token=P.protein(2), size="small")
for uu0, vv0, stable in fixed_points(s0):
    pp.points([uu0], [vv0], "ink", r=0.14, hollow=not stable, zorder=12)
for uu0, vv0, stable in fixed_points(s0):
    if stable:
        if uu0 > vv0:
            pp.text(uu0, vv0 + 0.55, "U on", ha="center", va="bottom", size="small")
        else:
            pp.text(uu0 + 0.5, vv0 + 0.3, "V on", ha="left", va="bottom", size="small")
for p0, tok in (((4.5, 6.0), "atp"), ((6.0, 4.4), "dna")):
    tr = quant.odeint_rk4(lambda t, y: np.array(rhs(y[0], y[1], s0)), np.array(p0), np.linspace(0, 12, 1200))
    pp.line(tr[:, 0], tr[:, 1], tok, lw=1.4)
    pp.points([p0[0]], [p0[1]], tok, r=0.08)

# ---- C: hysteresis --------------------------------------------------------------------------------------
X1, W1 = 18.4, 5.6
ph = quant.Plot(ax, (X1, Y0, W1, S), (0.1, 10), (0.01, 100), xlog=True, ylog=True, xlabel="Signal $s$",
                ylabel="Steady state $v^*$", xticks=[(0.1, "0.1"), (1, "1"), (10, "10")],
                yticks=[(0.01, "0.01"), (0.1, "0.1"), (1, "1"), (10, "10"), (100, "100")])
bio.panel(ax, "C", (X1 - 1.6, 9.5))
ss = np.logspace(-1, 1, 500)
low, mid, high = [], [], []
for s in ss:
    fp = sorted(fixed_points(s), key=lambda f: f[1])
    if len(fp) == 1:
        (low if fp[0][1] < 1 else high).append((s, fp[0][1]))
    else:
        low.append((s, fp[0][1]))
        mid.append((s, fp[1][1]))
        high.append((s, fp[2][1]))
low, mid, high = (np.array(z) for z in (low, mid, high))
s_lo, s_hi = mid[0, 0], mid[-1, 0]
ph.span(s_lo, s_hi, "highlight", text="bistable", strength=0.6)
ph.line(low[:, 0], low[:, 1], "dna", lw=2.2)
ph.line(high[:, 0], high[:, 1], "atp", lw=2.2)
ph.line(np.r_[high[0, 0], mid[:, 0], low[-1, 0]], np.r_[high[0, 1], mid[:, 1], low[-1, 1]], "muted", lw=1.2, dashed=True)
# jumps at the saddle-node points
up_s, up_from, up_to = low[-1, 0], low[-1, 1], high[high[:, 0] >= low[-1, 0]][0, 1]
dn_s, dn_from, dn_to = high[0, 0], high[0, 1], low[low[:, 0] <= high[0, 0]][-1, 1]
bio.arrow(ax, ph.xy(up_s, up_from * 1.4), ph.xy(up_s, up_to / 1.4), kind="process", color=quant.line_color("dna"), lw=1.2,
          head=0.2)
bio.arrow(ax, ph.xy(dn_s, dn_from / 1.4), ph.xy(dn_s, dn_to * 1.4), kind="process", color=quant.line_color("atp"),
          lw=1.2, head=0.2)
ph.text(0.12, 0.05, "U on", ha="left", va="top", token="dna", size="small")
ph.text(1.9, 40, "V on", ha="right", va="center", token="atp", size="small")
ph.text(1.0, 0.25, "unstable", ha="center", va="center", color=P.muted())
ph.text(s_lo / 1.1, 0.012, f"{s_lo:.2f}", ha="right", va="bottom", color=P.muted())
ph.text(s_hi * 1.1, 0.012, f"{s_hi:.2f}", ha="left", va="bottom", color=P.muted())
