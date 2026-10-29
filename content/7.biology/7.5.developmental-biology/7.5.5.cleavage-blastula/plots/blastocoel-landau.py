"""The lattice energy model of blastocoel formation (Percus and Childress). A: the local energy density
E(σ) = σ⁴/12 + uσ²/2 + vσ/3 of the coarse-grained cell density σ (σ = 1: cell, σ = -1: no cell, i.e. cavity);
for u > 0 it has one minimum, for u < 0 two. B: the control plane (u, v); inside the cusp v² + 4u³ = 0 two
minima coexist. A weakly adhesive embryo (u > 0) moves through v = 0 smoothly and its interior empties
gradually (sea urchin); a strongly adhesive one (u < 0) must cross the bistable wedge and jumps (mammal).
C: the interior density σ at the minimum along the two paths; the jump on the second path occurs at the far
edge of the wedge if the embryo stays in its minimum as long as it exists (perfect delay), and at v = 0 under
the Maxwell convention (global minimum). D: the radial profile from the first integral, with σ = 1 held at the
surface by adhesion to the hyaline layer: a thin shell of cells over a cavity, and for nearly equal minima a
thick shell with a plateau (depth in units of the adhesion length ℓ = (Ja²c/24)^½)."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(22, 15)
E = lambda s, u, v: s**4 / 12 + u * s**2 / 2 + v * s / 3  # noqa: E731

a = charts.axes_at(ax, (1.7, 9.0, 8.0, 5.0))
s = np.linspace(-2.6, 2.6, 400)
for (u, v, tk, lab) in ((0.6, 0.0, "neutral", "u > 0: one minimum"), (-1.2, 0.0, "dna", "u < 0, v = 0: two equal minima"),
                        (-1.2, 0.8, "receptor", "u < 0, v > 0: cavity minimum lower")):
    a.plot(s, E(s, u, v), color=charts.line(tk), lw=1.7, label=lab)
a.set_ylim(-1.4, 1.6)
a.set_xlim(-2.6, 2.6)
charts.style_axes(a, "local cell density σ", "energy density E(σ)")
charts.title(a, "A  Landau potential")
lg = a.legend(fontsize=6.5, frameon=False, loc="upper center")
[t.set_color(P.ink()) for t in lg.get_texts()]

b = charts.axes_at(ax, (12.8, 9.0, 8.0, 5.0))
uu = np.linspace(-2, 0, 200)
vc = 2 * (-uu) ** 1.5
b.fill_between(uu, -vc, vc, color=P.mix(P.fill("highlight"), P.surface(), 0.5), lw=0)
b.plot(uu, vc, color=charts.line("highlight"), lw=1.5)
b.plot(uu, -vc, color=charts.line("highlight"), lw=1.5)
b.annotate("", xy=(0.8, 2.2), xytext=(0.8, -2.2), arrowprops=dict(arrowstyle="-|>", color=charts.line("positive"), lw=1.6))
b.annotate("", xy=(-1.2, 2.6), xytext=(-1.2, -2.6), arrowprops=dict(arrowstyle="-|>", color=charts.line("receptor"), lw=1.6))
b.text(0.92, -1.6, "gradual\n(sea urchin)", fontsize=7, color=charts.line("positive"))
b.text(-1.12, -2.4, "sudden\n(mammal)", fontsize=7, color=charts.line("receptor"))
b.text(-1.9, 0.15, "two minima", fontsize=7, color=P.ink())
b.text(-0.55, 3.0, "v² + 4u³ = 0", fontsize=7, color=charts.line("highlight"))
b.set_xlim(-2, 1.6)
b.set_ylim(-3.6, 3.6)
b.axhline(0, color=P.muted(), lw=0.6, ls=(0, (2, 2)))
charts.style_axes(b, "u = 1 - Jc/4 (adhesion)", "v ∝ λ - Jc/2 (cavity bias)")
charts.title(b, "B  Control plane and the cusp")

c = charts.axes_at(ax, (1.7, 1.4, 8.0, 5.0))
vv = np.linspace(-3.4, 3.4, 700)
for u, tk in ((0.8, "positive"), (-1.2, "receptor")):
    roots = [np.sort(np.roots([1 / 3, 0, u, v / 3]).real[np.abs(np.roots([1 / 3, 0, u, v / 3]).imag) < 1e-9]) for v in vv]
    lo = np.array([r[0] for r in roots])
    hi = np.array([r[-1] for r in roots])
    if u > 0:
        c.plot(vv, lo, color=charts.line(tk), lw=1.8, label="u = 0.8")
    else:
        mid = np.array([r[1] if len(r) == 3 else np.nan for r in roots])
        ok = np.array([len(r) == 3 for r in roots])
        c.plot(vv, np.where(vv < 2 * 1.2**1.5 + 1e-9, hi, np.nan), color=charts.line(tk), lw=1.8, label="u = -1.2")
        c.plot(vv, np.where(vv > -2 * 1.2**1.5 - 1e-9, lo, np.nan), color=charts.line(tk), lw=1.8)
        c.plot(vv[ok], mid[ok], color=charts.line(tk), lw=1.0, ls=(0, (2, 2)))
        vj = 2 * 1.2**1.5
        c.annotate("", xy=(vj, -1.9), xytext=(vj, 0.95), arrowprops=dict(arrowstyle="-|>", color=charts.line(tk), lw=1.0))
        c.text(vj - 0.08, -0.6, "jump\n(delay)", ha="right", fontsize=6.5, color=charts.line(tk))
        c.axvline(0, color=P.muted(), lw=0.7, ls=(0, (2, 2)))
        c.text(0.07, 2.2, "Maxwell", fontsize=6.5, color=P.muted())
c.set_xlim(-3.4, 3.4)
c.set_ylim(-2.7, 2.7)
charts.style_axes(c, "cavity bias v", "interior density σ at a minimum")
charts.title(c, "C  Gradual versus sudden cavitation")
lg = c.legend(fontsize=6.5, frameon=False, loc="lower left")
[t.set_color(P.ink()) for t in lg.get_texts()]

d = charts.axes_at(ax, (12.8, 1.4, 8.0, 5.0))
for (u, v, tk, lab) in ((0.6, 0.4, "neutral", "u = 0.6, v = 0.4"), (0.6, 1.5, "dna", "u = 0.6, v = 1.5"),
                        (-0.3, 0.02, "receptor", "u = -0.3, v = 0.02")):
    rts = np.roots([1 / 3, 0, u, v / 3])
    rts = np.sort(rts.real[np.abs(rts.imag) < 1e-9])
    smin = rts[0] if E(rts[0], u, v) <= E(rts[-1], u, v) else rts[-1]
    Emin = E(smin, u, v)
    sg = np.linspace(1.0, smin + 1e-4 * np.sign(1 - smin), 20000)
    f = 1 / np.sqrt(np.maximum(E(sg, u, v) - Emin, 1e-14))
    depth = np.concatenate([[0], np.cumsum(0.5 * (f[1:] + f[:-1]) * np.abs(np.diff(sg)))])
    d.plot(depth, sg, color=charts.line(tk), lw=1.7, label=lab)
d.axhline(0, color=P.muted(), lw=0.6, ls=(0, (2, 2)))
d.set_xlim(0, 9)
d.set_ylim(-2.2, 1.6)
d.text(0.15, 1.2, "surface (σ = 1)", fontsize=6.5, color=P.muted())
d.text(6.0, -1.0, "cavity", fontsize=7, color=P.muted())
charts.style_axes(d, "depth below the surface / ℓ", "cell density σ")
charts.title(d, "D  Radial profile of the blastula wall")
lg = d.legend(fontsize=6.5, frameon=False, loc="upper right")
[t.set_color(P.ink()) for t in lg.get_texts()]
