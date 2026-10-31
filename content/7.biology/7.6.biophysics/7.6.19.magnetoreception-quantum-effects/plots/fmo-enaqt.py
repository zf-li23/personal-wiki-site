# Environment-assisted transport in a model of the Fenna-Matthews-Olson (FMO) complex.
# Seven bacteriochlorophyll sites with the site energies and couplings (cm^-1) of Adolphs and Renger (2006).
# The excitation evolves under the Lindblad (Haken-Strobl) equation with pure dephasing at rate gamma
# (all coherences between sites decay at gamma), trapping from site 3 into the reaction center at
# 1 ps^-1 and loss everywhere at 1 ns^-1. The transfer efficiency is the time-integrated trapping,
# eta = k_trap int rho_33 dt, obtained by solving L x = -rho(0) for the integrated density matrix.
# A: site populations after excitation of site 1 without dephasing (coherent, oscillating) and with
#    gamma = 100 cm^-1.
# B: efficiency against dephasing rate for excitation starting on site 1 or on site 6: some dephasing helps
#    (it destroys the interference and energy mismatches that trap the excitation), too much freezes
#    the motion (quantum Zeno effect). Pure dephasing has no temperature: it lets the excitation climb in
#    energy as easily as descend; real systems relax towards thermal populations.
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import expm

import wikibio as bio
from wikibio import charts

P = bio.P
E = np.array([12410, 12530, 12210, 12320, 12480, 12630, 12440.0])
J = {(1, 2): -87.7, (1, 3): 5.5, (1, 4): -5.9, (1, 5): 6.7, (1, 6): -13.7, (1, 7): -9.9, (2, 3): 30.8,
     (2, 4): 8.2, (2, 5): 0.7, (2, 6): 11.8, (2, 7): 4.3, (3, 4): -53.5, (3, 5): -2.2, (3, 6): -9.6,
     (3, 7): 6.0, (4, 5): -70.7, (4, 6): -17.0, (4, 7): -63.3, (5, 6): 81.1, (5, 7): -1.3, (6, 7): 39.7}
n = 7
cm = 2 * np.pi * 2.99792458e10 * 1e-12  # rad/ps per cm^-1
H = np.diag(E - E.mean())
for (i, j), v in J.items():
    H[i - 1, j - 1] = H[j - 1, i - 1] = v
H = H * cm
ktrap, kloss = 1.0, 1e-3
Id = np.eye(n)


def liouvillian(gam_cm):
    gam = gam_cm * cm
    Heff = H - 0.5j * np.diag([kloss + (ktrap if i == 2 else 0.0) for i in range(n)])
    L = -1j * (np.kron(Id, Heff) - np.kron(Heff.conj(), Id))
    D = np.array([gam if a != b else 0.0 for b in range(n) for a in range(n)])
    return L - np.diag(D)


def efficiency(gam_cm, init):
    r0 = np.zeros((n, n), complex)
    r0[init, init] = 1
    x = np.linalg.solve(liouvillian(gam_cm), -r0.flatten(order="F"))
    return float(np.real(ktrap * x.reshape(n, n, order="F")[2, 2]))


fig, axs = plt.subplots(1, 2, figsize=(11.6, 4.0))
ax = axs[0]
t = np.linspace(0, 2.0, 201)
r0 = np.zeros((n, n), complex)
r0[0, 0] = 1
v0 = r0.flatten(order="F")
for gam, ls in ((0.0, "-"), (100.0, "--")):
    Lm = liouvillian(gam)
    U = expm(Lm * (t[1] - t[0]))
    v = v0.copy()
    pops = []
    for _ in t:
        pops.append(np.real(np.diag(v.reshape(n, n, order="F"))))
        v = U @ v
    pops = np.array(pops)
    for s, tok in ((0, "dna"), (1, "enzyme"), (2, "rna")):
        ax.plot(t, pops[:, s], color=charts.line(tok), lw=1.4, ls=ls,
                label=f"site {s + 1}" + (" (γ = 0)" if gam == 0 else " (γ = 100 cm⁻¹)"))
ax.legend(fontsize=6.5, frameon=False, loc="upper right", ncol=2)
ax.set_ylim(0, 1.25)
charts.style_axes(ax, "t / ps", "population")
charts.title(ax, "A   Coherent beating and its damping")

ax = axs[1]
gs = np.logspace(-4, 5, 73)
for init, tok in ((0, "dna"), (5, "rna")):
    ax.semilogx(gs, [efficiency(g, init) for g in gs], color=charts.line(tok), lw=1.8,
                label=f"excitation starts on site {init + 1}")
ax.axvspan(50, 300, color=P.fill("enzyme"), alpha=0.18, lw=0)
ax.text(60, 0.3, "dephasing in\nproteins at 300 K", fontsize=7, color=P.ink())
ax.set_ylim(0, 1.05)
ax.legend(fontsize=7, frameon=False, loc="lower left")
charts.style_axes(ax, "dephasing rate γ / cm⁻¹", "transfer efficiency η")
charts.title(ax, "B   Noise-assisted transport")
fig.tight_layout()
