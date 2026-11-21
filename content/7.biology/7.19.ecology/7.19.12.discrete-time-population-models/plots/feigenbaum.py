"""Universality of period doubling (Section 12.5).

A: at the accumulation point R_inf of the logistic map f(x) = R x (1 - x) (extrapolated from the superstable
parameters R_n, which satisfy f^(2^n)(1/2) = 1/2 and are found by Newton's method), the iterates
f^(2^n), centered at the critical point 1/2 and rescaled so that their value there is 1,
G_n(y) = [f^(2^n)(1/2 + s_n y) - 1/2] / s_n with s_n = f^(2^n)(1/2) - 1/2, for n = 0..4,
converge to the universal function g of the Feigenbaum-Cvitanovic equation g(y) = alpha g(g(y/alpha)),
g(0) = 1, solved here with an even polynomial of degree 16 (collocation at 8 points, Newton iteration),
which gives alpha = 1/g(1); the scale factors satisfy s_n / s_(n+1) -> alpha.
B: estimates delta_n = (R_n - R_{n-1}) / (R_{n+1} - R_n) for the logistic map, the Ricker map
x exp(r (1 - x)) (critical point 1/r) and the sine map mu sin(pi x) (critical point 1/2).
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq, fsolve, newton

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT


def it(f, x, n):
    for _ in range(n):
        x = f(x)
    return x


def superstable(fam, xc, R0, R1, nmax):
    R = [R0, R1]
    for n in range(2, nmax + 1):
        guess = R[-1] + (R[-1] - R[-2]) / 4.669
        g = lambda p: it(lambda x: fam(p, x), xc(p), 2 ** n) - xc(p)
        R.append(newton(g, guess, tol=1e-15, maxiter=200))
    return np.array(R)


logi = lambda R, x: R * x * (1 - x)
ric = lambda r, x: x * np.exp(r * (1 - x))
sine = lambda m, x: m * np.sin(np.pi * x)
fams = [("logistic", logi, lambda p: 0.5, 2.0, 1 + np.sqrt(5), C.line("dna")),
        ("Ricker", ric, lambda p: 1 / p, 1.0,
         brentq(lambda r: it(lambda x: ric(r, x), 1 / r, 2) - 1 / r, 2.1, 2.4), C.line("rna")),
        ("sine", sine, lambda p: 0.5, 0.5,
         brentq(lambda m: it(lambda x: sine(m, x), 0.5, 2) - 0.5, 0.75, 0.82), C.line("positive"))]

# universal function: g(y) = 1 + sum c_k y^(2k), solve g(y) = alpha g(g(y/alpha)), alpha = 1/g(1)
K = 8
ys = np.linspace(0.1, 1.0, K)


def gfun(c, y):
    return 1 + sum(ck * y ** (2 * (k + 1)) for k, ck in enumerate(c))


def eqs(c):
    alpha = 1 / gfun(c, 1.0)
    return gfun(c, ys) - alpha * gfun(c, gfun(c, ys / alpha))


c0 = np.zeros(K)
c0[:3] = [-1.5276, 0.1048, 0.0267]
csol = fsolve(eqs, c0, xtol=1e-13)
alpha = 1 / gfun(csol, 1.0)

fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.0))
ax = axes[0]
R = superstable(logi, lambda p: 0.5, 2.0, 1 + np.sqrt(5), 9)
y = np.linspace(-1, 1, 400)
shades = [P.mix(C.line("dna"), P.surface(), t) for t in (0.75, 0.6, 0.45, 0.3, 0.0)]
Rinf = R[-1] + (R[-1] - R[-2]) / (4.6692016 - 1)
f = lambda x: logi(Rinf, x)
for n, col in zip(range(0, 5), shades):
    sn = it(f, 0.5, 2 ** n) - 0.5
    G = (it(f, 0.5 + y * sn, 2 ** n) - 0.5) / sn
    ax.plot(y, G, color=col, lw=1.4, label=f"n = {n}")
ax.plot(y, gfun(csol, y), color=C.line("negative"), lw=1.2, ls=(0, (4, 2)), label="universal g")
ax.axhline(0, color=P.muted(), lw=0.5)
ax.text(-0.3, -0.5, f"α = 1/g(1) = {alpha:.5f}", fontsize=FS["tiny"], color=C.line("negative"))
ax.set_ylim(-0.6, 1.15)
C.style_axes(ax, "y (rescaled distance from the critical point)", "rescaled iterate")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right", ncol=2)
C.title(ax, "A  Convergence to the universal function")

ax = axes[1]
for name, fam, xc, a0, a1, col in fams:
    Rn = superstable(fam, xc, a0, a1, 9)
    dd = np.diff(Rn)
    delta = dd[:-1] / dd[1:]
    ax.plot(np.arange(1, len(delta) + 1), delta, "o-", ms=4, lw=1.4, color=col,
            label=f"{name}: R∞ ≈ {Rn[-1]:.5f}")
ax.axhline(4.6692016, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
ax.text(6.0, 4.69, "δ = 4.6692…", fontsize=FS["tiny"], color=P.muted())
ax.set_ylim(3.6, 5.0)
C.style_axes(ax, "n", "δₙ = (Rₙ − Rₙ₋₁)/(Rₙ₊₁ − Rₙ)")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
C.title(ax, "B  The same δ for three maps")
fig.tight_layout()
