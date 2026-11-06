# Lockhart's model of cell growth and its coupling to water uptake (illustrative parameters).
# (A) Relative growth rate r = phi (P - Y) above the yield threshold Y (zero below): wall loosening by acid
# (auxin) raises the extensibility phi and lowers Y; gibberellin mainly raises phi.
# (B) Coupled model (Lockhart 1965; Ortega 1985): water uptake L (D - P), with D = Psi_source - Psi_s the
# osmotic driving force, and turgor dynamics dP/dt = eps [L (D - P) - phi (P - Y)], eps = volumetric
# elastic modulus. At t = 0 the water supply is cut (L = 0): wall yielding at constant volume relaxes P
# towards Y with time constant 1 / (eps phi) (in vivo stress relaxation); at t = 1.5 h water is restored.
import matplotlib.pyplot as plt
import numpy as np

fig, (a, b) = plt.subplots(1, 2, figsize=(11.5, 4.3))
P = np.linspace(0, 1.0, 400)
cases = [("Control: φ = 0.20, Y = 0.35 MPa", 0.20, 0.35, "0.35", "-"),
         ("Acid / auxin: φ = 0.50, Y = 0.20 MPa", 0.50, 0.20, "#c0504d", "-"),
         ("Gibberellin: φ = 0.40, Y = 0.35 MPa", 0.40, 0.35, "#2f6fb5", "--")]
for name, phi, Y, col, ls in cases:
    r = phi * np.clip(P - Y, 0, None) * 100
    a.plot(P, r, color=col, lw=2.2, ls=ls, label=name)
    a.plot(Y, 0, "o", color=col, ms=6, zorder=5)
a.axvline(0.6, color="0.6", lw=0.8, ls=":")
a.text(0.61, 33, "typical turgor", fontsize=8.5, color="0.4")
a.set_xlabel("Turgor pressure P / MPa")
a.set_ylabel("Relative growth rate (1/V) dV/dt / % h⁻¹")
a.set_xlim(0, 1.0)
a.set_ylim(0, 36)
a.legend(frameon=False, fontsize=8.5, loc="upper left")
a.set_title("A   Lockhart equation", loc="left", fontsize=10)

L0, D, phi, Y, eps = 1.0, 0.70, 0.20, 0.30, 10.0
dt = 0.001
t = np.arange(-0.5, 3.5, dt)
Pt = np.empty_like(t)
p = (L0 * D + phi * Y) / (L0 + phi)
for i, ti in enumerate(t):
    L = 0.0 if 0 <= ti < 1.5 else L0
    Pt[i] = p
    p += dt * eps * (L * D - L * p - phi * max(p - Y, 0))
G = phi * np.clip(Pt - Y, 0, None) * 100
b.axvspan(0, 1.5, color="0.85", alpha=0.6, lw=0)
b.text(0.75, 0.68, "water supply cut", ha="center", fontsize=8.5, color="0.35")
b.plot(t, Pt, color="#2f6fb5", lw=2.4, label="Turgor P")
b.axhline(Y, color="#2f6fb5", lw=0.9, ls="--")
b.text(3.45, Y + 0.012, "Y", color="#2f6fb5", ha="right", fontsize=9)
b.set_xlabel("Time t / h")
b.set_ylabel("Turgor pressure P / MPa", color="#2f6fb5")
b.set_ylim(0.25, 0.72)
b.set_xlim(-0.5, 3.5)
b2 = b.twinx()
b2.plot(t, G, color="#c0504d", lw=2.0, ls="-", label="Growth rate")
b2.set_ylabel("Relative growth rate / % h⁻¹", color="#c0504d")
b2.set_ylim(0, 9.4)
tau = 1 / (eps * phi)
b.annotate(f"τ = 1/(εφ) = {tau * 60:.0f} min", xy=(tau, Y + (Pt[0] - Y) * np.exp(-1)), xytext=(0.55, 0.52),
           fontsize=8.5, arrowprops=dict(arrowstyle="-", color="0.4", lw=0.8))
b.set_title("B   Water uptake and stress relaxation", loc="left", fontsize=10)
lines = b.get_lines()[:1] + b2.get_lines()
b.legend(lines, [l.get_label() for l in lines], frameon=False, fontsize=8.5, loc="center right")
for x in (a, b):
    x.spines[["top"]].set_visible(False)
a.spines[["right"]].set_visible(False)
fig.tight_layout()
