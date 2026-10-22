import numpy as np
import matplotlib.pyplot as plt

# Volumes of 100 g water(A)-ethanol(B) mixtures at 20 C (table in the text, from CRC densities).
MA, MB = 18.015, 46.069  # g/mol
VA_star, VB_star = MA / 0.99820, MB / 0.78924  # cm^3/mol of the pure liquids
w = np.array([20, 40, 60, 80.0])
V100 = np.array([103.24, 106.93, 112.22, 118.56])
nB, nA = w / MB, (100 - w) / MA
x = nB / (nA + nB)
Vm = V100 / (nA + nB)
VE = Vm - (x * VB_star + (1 - x) * VA_star)

# Two-parameter Redlich-Kister fit of the excess molar volume.
X = np.column_stack([x * (1 - x), x * (1 - x) * (2 * x - 1)])
rk0, rk1 = np.linalg.lstsq(X, VE, rcond=None)[0]


def VE_fit(x):
    return x * (1 - x) * (rk0 + rk1 * (2 * x - 1))


def dVm_dx(x, h=1e-6):
    f = lambda s: s * VB_star + (1 - s) * VA_star + VE_fit(s)
    return (f(x + h) - f(x - h)) / (2 * h)


xs = np.linspace(0, 1, 401)
Vm_fit = xs * VB_star + (1 - xs) * VA_star + VE_fit(xs)
VA = Vm_fit - xs * dVm_dx(xs)
VB = Vm_fit + (1 - xs) * dVm_dx(xs)

fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.8))
a1.plot(xs, Vm_fit, color="#2563eb", lw=2, label="mean molar volume (fit)")
a1.plot(xs, xs * VB_star + (1 - xs) * VA_star, color="#94a3b8", lw=1, ls=":", label="ideal (additive)")
a1.plot(x, Vm, "o", color="#2563eb", label="data")
x0 = 0.4
v0, s0 = np.interp(x0, xs, Vm_fit), dVm_dx(x0)
a1.plot([0, 1], [v0 - x0 * s0, v0 + (1 - x0) * s0], color="#d97706", lw=1.5, ls="--", label=f"tangent at $x_B$ = {x0}")
a1.plot([0, 1], [v0 - x0 * s0, v0 + (1 - x0) * s0], "s", color="#d97706")
a1.annotate("$V_A$", (0, v0 - x0 * s0), textcoords="offset points", xytext=(8, -14), color="#d97706")
a1.annotate("$V_B$", (1, v0 + (1 - x0) * s0), textcoords="offset points", xytext=(-24, 6), color="#d97706")
a1.set_xlabel("$x_B$ (ethanol)")
a1.set_ylabel(r"$V_\mathrm{m}$ / (cm$^3$ mol$^{-1}$)")
a1.set_title("Intercept method", fontsize=11)
a1.legend(fontsize=9, loc="upper left")
a1.grid(alpha=0.3)

m = xs >= 0.05
a2.plot(xs[m], (VA - VA_star)[m], color="#16a34a", lw=2, label=r"water: $V_A - V^*_{\mathrm{m},A}$")
a2.plot(xs[m], (VB - VB_star)[m], color="#dc2626", lw=2, label=r"ethanol: $V_B - V^*_{\mathrm{m},B}$")
a2.axhline(0, color="#94a3b8", lw=1)
a2.set_xlim(0, 1)
a2.set_xlabel("$x_B$ (ethanol)")
a2.set_ylabel(r"partial molar volume change / (cm$^3$ mol$^{-1}$)")
a2.set_title("Partial molar volumes move in opposite directions", fontsize=11)
a2.legend(fontsize=9, loc="lower right")
a2.grid(alpha=0.3)
fig.tight_layout()
