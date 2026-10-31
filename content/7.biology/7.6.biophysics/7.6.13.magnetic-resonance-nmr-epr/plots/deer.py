# DEER (four-pulse PELDOR): from a distance distribution to the time trace and back.
# The dipolar kernel for a spin pair at distance r, averaged over orientations (x = cos theta):
#   K(t, r) = int_0^1 cos[(3 x^2 - 1) omega_dd(r) t] dx,  omega_dd = 2 pi x 52.04 MHz nm^3 / r^3.
# The form factor is F(t) = (1 - lambda) + lambda int P(r) K(t, r) dr (modulation depth lambda = 0.35) and the
# measured trace V(t) = F(t) B(t) with a homogeneous 3D background B(t) = exp(-k t) (k = 0.15 us^-1); Gaussian
# noise of s.d. 0.01 is added (seed 0).
# A: the true distribution, a mixture of two conformations at 3.0 nm (60 %, s.d. 0.25 nm) and 4.2 nm (40 %,
#    s.d. 0.3 nm), and the distribution recovered by Tikhonov regularization with a second-derivative penalty
#    and non-negativity (alpha chosen by hand; the background is assumed known and divided out).
# B: the background-corrected form factor with its fit, and the dipolar oscillation of a single 3.0 nm pair.
# C: the Pake pattern (dipolar spectrum) of the 3.0 nm pair: horns at nu_perp = 1.93 MHz, edges at 2 nu_perp.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import nnls

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
t = np.linspace(0, 3.0, 300)            # microseconds
r = np.linspace(1.5, 6.5, 200)          # nm
dr = r[1] - r[0]
x = np.linspace(0, 1, 400)


def kernel(t, r):
    w = 2 * np.pi * 52.04 / r**3
    ph = (3 * x[None, None, :] ** 2 - 1) * w[None, :, None] * t[:, None, None]
    return np.trapezoid(np.cos(ph), x, axis=2)


K = kernel(t, r) * dr
gauss = lambda m, s: np.exp(-0.5 * ((r - m) / s) ** 2) / (s * np.sqrt(2 * np.pi))
Ptrue = 0.6 * gauss(3.0, 0.25) + 0.4 * gauss(4.2, 0.3)
lam, kbg = 0.35, 0.15
F = (1 - lam) + lam * K @ Ptrue
V = F * np.exp(-kbg * t) + rng.normal(0, 0.01, t.size)

# Tikhonov with non-negativity: minimize ||K' P - S||^2 + alpha^2 ||L P||^2, P >= 0
S = (V / np.exp(-kbg * t) - (1 - lam)) / lam
Lmat = np.diff(np.eye(r.size), 2, axis=0) / dr**2
alpha = 0.04
A = np.vstack([K, alpha * Lmat * dr])
b = np.concatenate([S, np.zeros(Lmat.shape[0])])
Pfit, _ = nnls(A, b)

fig, axs = plt.subplots(1, 3, figsize=(13.0, 3.9))
ax = axs[0]
ax.fill_between(r, Ptrue, color=P.light("protein"), lw=0)
ax.plot(r, Ptrue, color=charts.line("protein"), lw=1.8, label="true P(r)")
ax.plot(r, Pfit, color=charts.line("rna"), lw=1.6, ls="--", label="Tikhonov + non-negativity")
ax.set_xlim(1.5, 6.5)
ax.set_ylim(0, None)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "r / nm", "P(r) / nm⁻¹")
charts.title(ax, "A   Distance distribution")

ax = axs[1]
ax.plot(t, V, ".", color=P.muted(), ms=2.5, label="V(t), with background and noise")
ax.plot(t, (1 - lam) + lam * K @ Pfit, color=charts.line("rna"), lw=1.4, label="fit (background-corrected F(t))")
ax.plot(t, S * lam + (1 - lam), ".", color=charts.line("protein"), ms=2.0, label="F(t) = V(t) / B(t)")
single = (1 - lam) + lam * kernel(t, np.array([3.0]))[:, 0]
ax.plot(t, single - 0.75, color=charts.line("enzyme"), lw=1.0, label="single pair at 3.0 nm (offset)")
ax.set_xlim(0, 3.0)
ax.set_ylim(-0.45, 1.25)
ax.legend(fontsize=7.0, frameon=False, loc="upper right")
charts.style_axes(ax, "t / μs", "echo intensity")
charts.title(ax, "B   Time trace")

ax = axs[2]
nu = np.linspace(-5, 5, 2000)
nperp = 52.04 / 3.0**3
spec = np.zeros_like(nu)
for c in np.linspace(0, 1, 4000):
    f = nperp * (3 * c**2 - 1)
    spec += np.exp(-0.5 * ((nu - f) / 0.05) ** 2) + np.exp(-0.5 * ((nu + f) / 0.05) ** 2)
ax.plot(nu, spec / spec.max(), color=charts.line("dna"), lw=1.6)
for f, lab in ((nperp, "ν⊥"), (2 * nperp, "2ν⊥")):
    ax.axvline(f, color=P.muted(), lw=0.6, ls=":")
    ax.text(f + 0.08, 0.9 if lab == "ν⊥" else 0.6, f"{lab} = {f:.2f} MHz", fontsize=7.5, color=P.ink())
ax.set_xlim(-5, 5)
ax.set_ylim(0, 1.05)
ax.set_yticks([])
charts.style_axes(ax, "dipolar frequency / MHz", None)
charts.title(ax, "C   Pake pattern, r = 3.0 nm")
fig.tight_layout()
