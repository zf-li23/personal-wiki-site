"""The amphibian blastula as a Stokes drop driven by its surface tension (Percus and Childress), with the
coefficients recomputed. The tension is expanded in Legendre polynomials of cos θ, θ measured from the
vegetal pole (bottom): T = A1 P1 + A2 P2 + A3 P3, higher at the vegetal (endodermal) pole. A: three
tension profiles. B–D: streamlines (contours of the Stokes stream function) of the initial flow inside the
unit sphere, arrows for the surface velocity, and the boundary after a short time (dashed). B: P1 alone: the
surface streams towards the vegetal pole and the shape does not change. C: P1 + P2: both poles dimple. D:
P1 + P3: only the vegetal pole invaginates, the gastrulation mode. E: the shell model with a blastocoel of
radius a; coefficient of the tangential surface velocity, −u_θ/sin θ, for an outer tension b cos θ and an
inner one c cos θ: streaming towards the vegetal pole persists even for an inner tension of opposite sign."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
coef = {1: (-1 / 6, 1 / 6), 2: (-2 / 19, 13 / 114), 3: (-5 / 66, 7 / 88)}  # (B_n, C_n) per unit A_n; C_1 fixes the frame
leg = {1: lambda x: x, 2: lambda x: 1.5 * x**2 - 0.5, 3: lambda x: 2.5 * x**3 - 1.5 * x}
dleg = {1: lambda t: -np.sin(t), 2: lambda t: -3 * np.sin(t) * np.cos(t), 3: lambda t: -np.sin(t) * (15 * np.cos(t)**2 - 3) / 2}
ur_s = {1: 0.0, 2: -1 / 19, 3: -1 / 22}          # u_r(1, θ) = Σ ur_s[n] A_n P_n(cos θ)
ut_s = {1: 1 / 3, 2: 7 / 38, 3: 3 / 22}          # u_θ(1, θ) = Σ ut_s[n] A_n dP_n/dθ


def psi(r, t, A):
    out = 0.0
    for n, a in A.items():
        B, C = coef[n]
        out = out + a * np.sin(t) * dleg[n](t) * (B * r**(n + 3) + C * r**(n + 1))
    return out


cases = [("B  P1: streaming", {1: 1.0}), ("C  P1 + P2: both poles", {1: 1.0, 2: 0.8}), ("D  P1 + P3: gastrulation mode", {1: 1.0, 3: 0.6})]
fig, ax = bio.canvas(24, 14)
a = charts.axes_at(ax, (1.8, 8.4, 5.6, 4.6))
th = np.linspace(0, np.pi, 200)
for (name, A), tk in zip(cases, ("neutral", "dna", "receptor")):
    T = sum(v * leg[n](np.cos(th)) for n, v in A.items())
    a.plot(np.degrees(th), T, color=charts.line(tk), lw=1.7, label=name[3:].split(":")[0])
a.set_xticks([0, 90, 180])
a.set_xticklabels(["0\nvegetal", "90", "180\nanimal"])
charts.style_axes(a, "θ / degree", "surface tension T")
charts.title(a, "A  Tension profiles")
lg = a.legend(fontsize=7, frameon=False)
[t.set_color(P.ink()) for t in lg.get_texts()]

boxes = [(9.6, 7.9, 5.4, 5.4), (16.5, 7.9, 5.4, 5.4), (9.6, 0.9, 5.4, 5.4)]
g = np.linspace(-1, 1, 241)
X, Z = np.meshgrid(g, g)
R = np.hypot(X, Z)
TH = np.arccos(np.clip(-Z / np.maximum(R, 1e-9), -1, 1))  # angle from the vegetal pole (z = -1)
for (name, A), box in zip(cases, boxes):
    b = charts.axes_at(ax, box)
    S = np.where(R <= 1, psi(R, TH, A) * np.sign(X + 1e-12), np.nan)
    b.contour(X, Z, S, levels=np.linspace(np.nanmin(S), np.nanmax(S), 22), colors=[charts.line("dna")], linewidths=0.7)
    tt = np.linspace(0, 2 * np.pi, 400)
    b.plot(np.cos(tt), np.sin(tt), color=P.ink(), lw=1.2)
    # deformed boundary after a short time: r = 1 + eps u_r
    thv = np.linspace(0, np.pi, 200)
    ur = sum(ur_s[n] * v * leg[n](np.cos(thv)) for n, v in A.items())
    rr = 1 + 4.0 * ur
    for s in (1, -1):
        b.plot(s * rr * np.sin(thv), -rr * np.cos(thv), color=charts.line("receptor"), lw=1.2, ls=(0, (3, 2)))
    for t0 in np.radians(np.arange(20, 171, 25)):
        ut = sum(ut_s[n] * v * dleg[n](t0) for n, v in A.items())
        urr = sum(ur_s[n] * v * leg[n](np.cos(t0)) for n, v in A.items())
        # unit vectors: e_r = (sin t, -cos t), e_θ = (cos t, sin t) in (x, z) with θ from the vegetal pole
        p = np.array([np.sin(t0), -np.cos(t0)]) * 1.05
        v = 1.3 * (urr * np.array([np.sin(t0), -np.cos(t0)]) + ut * np.array([np.cos(t0), np.sin(t0)]))
        for s in (1, -1):
            b.annotate("", xy=(s * (p[0] + v[0]), p[1] + v[1]), xytext=(s * p[0], p[1]),
                       arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=0.9, mutation_scale=7))
    b.set_xlim(-1.35, 1.35)
    b.set_ylim(-1.35, 1.35)
    b.set_aspect("equal")
    b.axis("off")
    b.text(0, -1.32, "vegetal", ha="center", fontsize=6.5, color=P.muted())
    b.text(0, 1.22, "animal", ha="center", fontsize=6.5, color=P.muted())
    charts.title(b, name)

e = charts.axes_at(ax, (17.2, 1.4, 5.6, 4.4))
av = np.linspace(0.0, 0.85, 100)
for cb, tk in ((0.0, "neutral"), (-0.5, "dna"), (-1.0, "receptor"), (-1.5, "positive")):
    k = ((2 + 3 * av**5) + 5 * av**3 * cb) / (6 * (1 - av**5))
    e.plot(av, k, color=charts.line(tk), lw=1.6, label=f"c/b = {cb:g}")
e.axhline(0, color=P.muted(), lw=0.6, ls=(0, (2, 2)))
charts.style_axes(e, "blastocoel radius a", "streaming coefficient (b = 1)")
charts.title(e, "E  Hollow blastula")
lg = e.legend(fontsize=6.5, frameon=False, loc="upper left")
[t.set_color(P.ink()) for t in lg.get_texts()]
