# The radical pair mechanism in its simplest form: two electron spins, one of which is coupled to one
# spin-1/2 nucleus by an anisotropic (axial) hyperfine tensor A = diag(-0.1, -0.1, 1.75) mT (similar to the
# N5 nitrogen of a flavin radical); the second radical has no hyperfine coupling; no exchange or dipolar
# coupling. Hamiltonian (angular frequency): H = gamma_e B b.(S1 + S2) + gamma_e S1.A.I, gamma_e =
# 176.1 rad us^-1 mT^-1, B = 50 uT, b = (sin theta, 0, cos theta).
# The pair is born in the singlet state, rho(0) = P_S / 2 (nuclear spin unpolarized), and both singlet and
# triplet pairs react at the same rate k (Haberkorn); the singlet yield is
#   Phi_S = k int_0^inf exp(-k t) P_S(t) dt = (1/2) sum_{m,n} |<m|P_S|n>|^2 k^2 / (k^2 + w_mn^2),
# with |m> the eigenstates of H and w_mn their frequency differences.
# A: singlet probability P_S(t) without recombination for the field along the hyperfine axis and
#    perpendicular to it. B: singlet yield against the field direction for k = 0.1, 1 and 10 us^-1.
# C: depth of the directional effect (max - min of Phi_S over theta) against k, at 50 uT and 500 uT.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
sx = np.array([[0, 1], [1, 0]]) / 2
sy = np.array([[0, -1j], [1j, 0]]) / 2
sz = np.array([[1, 0], [0, -1]]) / 2
I2 = np.eye(2)


def op(a, pos):
    m = [I2, I2, I2]
    m[pos] = a
    return np.kron(np.kron(m[0], m[1]), m[2])


S1 = [op(s, 0) for s in (sx, sy, sz)]
S2 = [op(s, 1) for s in (sx, sy, sz)]
In = [op(s, 2) for s in (sx, sy, sz)]
PS = 0.25 * np.eye(8) - sum(S1[i] @ S2[i] for i in range(3))
g = 176.086
A = (-0.1, -0.1, 1.75)


def ham(theta, B):
    b = (np.sin(theta), 0.0, np.cos(theta))
    return g * B * sum(b[i] * (S1[i] + S2[i]) for i in range(3)) + g * sum(A[i] * S1[i] @ In[i] for i in range(3))


def phi_s(theta, k, B=0.05):
    w, V = np.linalg.eigh(ham(theta, B))
    Pm = V.conj().T @ PS @ V
    dw = w[:, None] - w[None, :]
    return float((np.abs(Pm) ** 2 * k**2 / (k**2 + dw**2)).sum() / 2)


def ps_t(theta, t, B=0.05):
    w, V = np.linalg.eigh(ham(theta, B))
    Pm = V.conj().T @ PS @ V
    out = []
    for tt in t:
        U = np.exp(-1j * w * tt)
        rho = np.outer(U, U.conj()) * Pm / 2
        out.append(np.real(np.sum(Pm.T * rho)))
    return np.array(out)


fig, axs = plt.subplots(1, 3, figsize=(13.4, 4.0))
ax = axs[0]
t = np.linspace(0, 1.0, 1500)
for th, tok, lab in ((0.0, "dna", "B along the hyperfine axis"), (np.pi / 2, "rna", "B perpendicular")):
    ax.plot(t, ps_t(th, t), color=charts.line(tok), lw=1.0, label=lab)
ax.set_ylim(0, 1.15)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "t / μs", r"singlet probability $P_{\mathrm{S}}(t)$")
charts.title(ax, "A   Coherent singlet–triplet mixing")

ax = axs[1]
th = np.linspace(0, np.pi, 91)
for k, tok in ((0.1, "dna"), (1.0, "enzyme"), (10.0, "protein")):
    ax.plot(np.degrees(th), [phi_s(x, k) for x in th], color=charts.line(tok), lw=1.7, label=f"k = {k:g} μs⁻¹")
ax.legend(fontsize=7, frameon=False, loc="upper center")
ax.set_xticks([0, 45, 90, 135, 180])
charts.style_axes(ax, "angle θ between B and the hyperfine axis / degree", r"singlet yield $\Phi_{\mathrm{S}}$")
charts.title(ax, "B   A chemical compass (50 μT)")

ax = axs[2]
ks = np.logspace(-2, 3, 40)
th2 = np.linspace(0, np.pi / 2, 19)
for B, tok in ((0.05, "dna"), (0.5, "rna")):
    depth = []
    for k in ks:
        v = [phi_s(x, k, B) for x in th2]
        depth.append(max(v) - min(v))
    ax.semilogx(ks, depth, color=charts.line(tok), lw=1.7, label=f"B = {B * 1000:.0f} μT")
w0 = g * 0.05
ax.axvline(w0, color=P.muted(), lw=0.6, ls=":")
ax.text(w0 * 1.15, 0.13, "k = γB\n(50 μT)", fontsize=6.8, color=P.muted())
ax.set_ylim(0, None)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "recombination rate k / μs⁻¹", r"anisotropy $\Delta\Phi_{\mathrm{S}}$")
charts.title(ax, "C   The pair must live microseconds")
fig.tight_layout()
