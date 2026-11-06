# Stomatal conductance models and optimal stomatal behaviour.
# (A) Medlyn et al. (2011): g_s / A = 1.6 (1 + g1 / sqrt(D)) / c_a (g0 = 0, c_a = 420 umol/mol), for a C3
# (g1 = 4 kPa^0.5) and a C4 plant (g1 = 1.6 kPa^0.5); expressed as g_s for A = 20 umol m^-2 s^-1.
# (B) c_i / c_a = g1 / (g1 + sqrt(D)) (Eq. 10.5).
# (C) Cowan-Farquhar optimum: A(g) from a saturating supply function, A = Amax g / (g + k), and E = g D / p;
# the optimal g makes dA/dE = 1 / lambda; tangent lines for two values of lambda.
import matplotlib.pyplot as plt
import numpy as np

D = np.linspace(0.2, 4, 300)
ca = 420.0
fig, (a, b, c) = plt.subplots(1, 3, figsize=(13, 4.1))
for g1, col, name in ((4.0, "#3a8a3a", "C3, g₁ = 4"), (1.6, "#c07a20", "C4, g₁ = 1.6")):
    gs = 1.6 * (1 + g1 / np.sqrt(D)) * 20 / ca
    a.plot(D, gs, color=col, lw=2.2, label=name)
    b.plot(D, g1 / (g1 + np.sqrt(D)), color=col, lw=2.2, label=name)
a.set_xlabel("D / kPa")
a.set_ylabel("g_s / (mol m⁻² s⁻¹) at A = 20 µmol m⁻² s⁻¹")
a.set_ylim(0, 1.4)
a.legend(frameon=False, fontsize=9)
a.set_title("A   Medlyn model", loc="left", fontsize=10)
b.set_xlabel("D / kPa")
b.set_ylabel("c_i / c_a")
b.set_ylim(0.3, 1.0)
b.set_title("B   c_i / c_a = g₁ / (g₁ + √D)", loc="left", fontsize=10)

g = np.linspace(0, 1.2, 400)
Amax, k, Dk, p = 30.0, 0.25, 1.5, 100.0
A = Amax * g / (g + k)
E = g * Dk / p * 1000  # mmol m^-2 s^-1
c.plot(E, A, color="#2f7fbf", lw=2.4, label="A vs E as g_s rises")
for lam, col in ((0.5, "#7a4fb3"), (1.5, "#c0504d")):
    # dA/dE = (dA/dg) / (dE/dg) = Amax k / (g + k)^2 / (Dk/p*1000); set equal to 1/lam (umol/mmol)
    dEdg = Dk / p * 1000
    gopt = np.sqrt(Amax * k * lam / dEdg) - k
    Eo, Ao = gopt * dEdg, Amax * gopt / (gopt + k)
    xs = np.linspace(Eo - 3.5, Eo + 3.5, 10)
    c.plot(xs, Ao + (xs - Eo) / lam, color=col, lw=1.1, ls="--")
    c.plot(Eo, Ao, "o", color=col, ms=6, label=f"optimum, λ = {lam:g} mmol µmol⁻¹")
c.set_xlabel("E / (mmol m⁻² s⁻¹)")
c.set_ylabel("A / (µmol m⁻² s⁻¹)")
c.set_xlim(0, 18)
c.set_ylim(0, 32)
c.legend(frameon=False, fontsize=8, loc="lower right")
c.set_title("C   Cowan–Farquhar optimum", loc="left", fontsize=10)
for ax in (a, b, c):
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
