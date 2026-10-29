# Nodal and Lefty at the zebrafish blastoderm margin (Formula 16.4.1). One-dimensional tissue from the margin (x = 0)
# towards the animal pole; a source at the margin (the yolk syncytial layer and maternal inputs) starts Nodal
# production; Nodal signalling induces more Nodal and Lefty; Lefty blocks Nodal signalling. Diffusion coefficients are
# those measured for Squint and Lefty1 by FRAP (Muller and colleagues, 2012: 3.2 and 11 um^2/s); both clearance rates
# 2 x 10^-4 per s (half-life about 1 h); 3 h of signalling. A: Nodal signalling with Lefty (solid) and without it
# (dashed), log scale: Lefty confines the self-enhancing Nodal domain to the margin, without it Nodal autoactivation spreads
# through the tissue. B: with Lefty, Nodal and Lefty concentrations; Lefty, faster and induced by Nodal, extends
# further and caps the range of signalling.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P


def lapmat(N, dx):
    A = np.zeros((N, N))
    for i in range(N):
        A[i, i] = -2
        if i > 0:
            A[i, i - 1] = 1
        if i < N - 1:
            A[i, i + 1] = 1
    A[0, 1] = 2
    A[-1, -2] = 2
    return A / dx ** 2


def run(lefty=True, L=400.0, N=101, T=3 * 3600, dt=20.0, DN=3.2, DL=11.0):
    x = np.linspace(0, L, N)
    dx = x[1] - x[0]
    Lp = lapmat(N, dx)
    I = np.eye(N)
    kN = kL = 2e-4
    AN = np.linalg.inv(I - dt * DN * Lp)
    AL = np.linalg.inv(I - dt * DL * Lp)
    n = np.zeros(N)
    l = np.zeros(N)
    src = np.where(x < 25, 1.0, 0.0) * 2e-3
    sN, sL, K, h, KL = 1.0e-3, 3.0e-3, 0.5, 2, 1.0
    for _ in range(int(T / dt)):
        S = n / (1 + l / KL)
        f = S ** h / (K ** h + S ** h)
        n = AN @ (n + dt * (-kN * n + src + sN * f))
        if lefty:
            l = AL @ (l + dt * (-kL * l + sL * f))
    return x, n, l, n / (1 + l / KL)


x, n1, l1, S1 = run(True)
_, n0, l0, S0 = run(False)
fig, ax = bio.canvas(20.0, 7.8)
pa = C.axes_at(ax, (1.6, 1.4, 7.6, 5.4))
pa.semilogy(x, S1, color=C.line("receptor"), lw=2.0, label="with Lefty")
pa.semilogy(x, S0, color=P.muted(), lw=1.4, ls=(0, (4, 3)), label="no Lefty")
pa.axhline(0.5, color=P.muted(), lw=0.8, ls=(0, (1, 2)))
pa.text(390, 0.56, "half-maximal autoinduction", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="right")
pa.set_xlim(0, 400)
pa.set_ylim(0.1, 10)
C.style_axes(pa, "distance from margin / µm", "Nodal signalling (units of K)")
pa.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.2, 7.7))
pb = C.axes_at(ax, (12.0, 1.4, 7.2, 5.4))
pb.plot(x, n1 / n1.max(), color=C.line("receptor"), lw=2.0, label="Nodal")
pb.plot(x, l1 / l1.max(), color=C.line("metabolite"), lw=2.0, label="Lefty")
pb.set_xlim(0, 400)
pb.set_ylim(0, 1.05)
C.style_axes(pb, "distance from margin / µm", "concentration / maximum")
pb.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (10.6, 7.7))
