"""A mass-conserved reaction-diffusion model of PAR polarity in the C. elegans zygote (after Goehring et al.,
2011). Anterior PAR proteins (A: PAR-3/PAR-6/PKC-3) and posterior PAR proteins (P: PAR-1/PAR-2) bind the
cortex from a shared cytoplasmic pool, diffuse in it, and remove each other from it. The domain is half the
circumference of the embryo (anterior pole at 0, posterior pole at 67 µm); parameters are the measured ones.
A: membrane concentrations after 50 min, starting from a posterior P domain covering 40 % of the cortex (as
left by the cortical flow that the sperm centrosome triggers). B: the time course of the same simulation:
the two domains stay separated by a sharp, stable boundary. C: the final width of the P domain against the
size of the initial cue: a cue covering less than about a tenth of the cortex is erased and the zygote
stays unpolarized; any larger cue establishes polarity, and the final boundary settles near the middle of the
embryo almost independently of the cue: the system is bistable, needs a cue above a threshold, and then
maintains and positions its domains itself."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
DA, DP = 0.28, 0.15
konA, koffA, konP, koffP = 8.58e-3, 5.4e-3, 4.74e-2, 7.3e-3
kAP, kPA, psi, rhoA, rhoP, L = 0.19, 2.0, 0.174, 1.56, 1.0, 67.33
nx = 120
x = np.linspace(0, L, nx)
dx = x[1] - x[0]


def lap(u):
    out = np.empty_like(u)
    out[1:-1] = u[2:] - 2 * u[1:-1] + u[:-2]
    out[0], out[-1] = 2 * (u[1] - u[0]), 2 * (u[-2] - u[-1])
    return out / dx**2


def run(frac, T=3000.0, dt=0.05, every=400):
    A = np.where(x < L * (1 - frac), 1.0, 0.0)
    Pm = 1.0 - A
    hist = []
    for k in range(int(T / dt)):
        Ac, Pc = rhoA - psi * A.mean(), rhoP - psi * Pm.mean()
        dA = DA * lap(A) + konA * Ac - koffA * A - kAP * Pm * A
        dP = DP * lap(Pm) + konP * Pc - koffP * Pm - kPA * A**2 * Pm
        A, Pm = A + dt * dA, Pm + dt * dP
        if k % every == 0:
            hist.append(A - Pm / 2.2)
    return A, Pm, np.array(hist)


fig, ax = bio.canvas(22, 13)
A, Pm, H = run(0.4)
a = charts.axes_at(ax, (1.7, 7.6, 8.2, 4.6))
a.plot(x, A, color=charts.line("receptor"), lw=1.8, label="anterior PARs (A)")
a.plot(x, Pm, color=charts.line("dna"), lw=1.8, label="posterior PARs (P)")
charts.style_axes(a, "position along the cortex / µm (anterior to posterior)", "membrane concentration / µm⁻²")
charts.title(a, "A  Stable polarized state")
lg = a.legend(fontsize=7, frameon=False, loc="upper center")
[t.set_color(P.ink()) for t in lg.get_texts()]

b = charts.axes_at(ax, (12.6, 7.6, 8.2, 4.6))
b.imshow(H.T, aspect="auto", origin="lower", extent=(0, 50, 0, L), cmap="coolwarm", vmin=-2, vmax=2)
charts.style_axes(b, "time / min", "position / µm", box=True)
charts.title(b, "B  Kymograph (red: A, blue: P)")

c = charts.axes_at(ax, (1.7, 1.2, 8.2, 4.6))
fr = np.array([0.03, 0.06, 0.08, 0.1, 0.13, 0.2, 0.3, 0.45, 0.6])
w = []
for f in fr:
    A2, P2, _ = run(f, T=2400.0, every=10**9)
    w.append(np.mean(P2 > A2))
c.plot(fr, w, "-o", color=charts.line("dna"), lw=1.6, ms=3.5)
c.plot([0, 0.7], [0, 0.7], color=P.muted(), lw=0.7, ls=(0, (3, 2)))
c.text(0.42, 0.33, "final = initial", fontsize=6.5, color=P.muted(), rotation=33)
charts.style_axes(c, "initial P domain (fraction of cortex)", "final P domain")
charts.title(c, "C  A threshold for polarization")

bio.label(ax, (12.6, 5.6), "Model (per unit membrane area)", size="small", bold=True, ha="left")
eqs = [r"$\partial_t A = D_A \partial_x^2 A + k_{\mathrm{on}}^A A_{\mathrm{cyt}} - k_{\mathrm{off}}^A A - k_{AP} P A$",
       r"$\partial_t P = D_P \partial_x^2 P + k_{\mathrm{on}}^P P_{\mathrm{cyt}} - k_{\mathrm{off}}^P P - k_{PA} A^2 P$",
       r"$A_{\mathrm{cyt}} = \rho_A - \psi \langle A \rangle, \quad P_{\mathrm{cyt}} = \rho_P - \psi \langle P \rangle$"]
for k, e in enumerate(eqs):
    bio.label(ax, (12.8, 4.7 - 0.85 * k), e, size="small", ha="left")
bio.label(ax, (12.8, 2.0), "conservation couples the domains: a growing domain\ndepletes its own cytoplasmic pool", size="tiny",
          color=P.muted(), ha="left")
