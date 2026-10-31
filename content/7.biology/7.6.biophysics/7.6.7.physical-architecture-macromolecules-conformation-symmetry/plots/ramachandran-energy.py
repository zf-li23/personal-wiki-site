"""From hard spheres to energies: a soft-potential conformational map of a blocked residue.

Ac-X-NHMe (X = L-Ala or Gly) is built with standard geometry (trans peptides, tau = 111 deg).
Every (phi, psi) on a 3-degree grid gets the energy of all atom pairs whose distance depends
on phi or psi and that are at least three bonds apart: Lennard-Jones 12-6 with AMBER-like
radii and well depths (united-atom methyls) plus Coulomb between peptide partial charges in a
dielectric of 4 (1-4 pairs scaled by 1/2 and 1/1.2). The energy is converted to a Boltzmann
probability at 298 K. Panels: A energy of Ala, B probability of Ala with region populations,
C energy of Gly, D effective accessible fraction of the torus and the conformational entropy.
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
KT = 0.5925                                  # kcal/mol at 298 K


def place(a, b, c, bond, angle, torsion):
    """NeRF: position of d bonded to c, with angle b-c-d and torsion a-b-c-d (degrees)."""
    angle, torsion = np.radians(angle), np.radians(torsion)
    bc = c - b
    bc = bc / np.linalg.norm(bc, axis=-1, keepdims=True)
    n = np.cross(b - a, bc)
    n = n / np.linalg.norm(n, axis=-1, keepdims=True)
    m = np.cross(n, bc)
    x = -bond * np.cos(angle) * np.ones_like(torsion)
    y = bond * np.sin(angle) * np.cos(torsion)
    z = bond * np.sin(angle) * np.sin(torsion)
    return c + x[..., None] * bc + y[..., None] * m + z[..., None] * n


def build(phi, psi, gly):
    one = np.ones(phi.shape)
    sh = phi.shape + (3,)
    a = np.radians(116.2)
    CA0 = np.broadcast_to(np.array([0.0, 1.52, 0.0]), sh)
    C0 = np.broadcast_to(np.zeros(3), sh)
    N1 = np.broadcast_to(np.array([1.329 * np.sin(a), 1.329 * np.cos(a), 0.0]), sh)
    CA1 = place(CA0, C0, N1, 1.458, 121.7, 180.0 * one)
    O0 = place(CA1, N1, C0, 1.231, 123.0, 0.0 * one)
    H1 = place(CA0, C0, N1, 1.01, 119.5, 0.0 * one)
    C1 = place(C0, N1, CA1, 1.525, 111.0, phi)
    N2 = place(N1, CA1, C1, 1.329, 116.2, psi)
    O1 = place(N1, CA1, C1, 1.231, 120.8, psi + 180.0)
    CA2 = place(CA1, C1, N2, 1.458, 121.7, 180.0 * one)
    H2 = place(CA1, C1, N2, 1.01, 119.5, 0.0 * one)
    # Gly: the two alpha hydrogens are placed symmetrically, so its map is centrosymmetric
    CB = place(N1, C1, CA1, 1.09 if gly else 1.53, 109.5, (120.35 if gly else 122.7) * one)
    HA = place(N1, C1, CA1, 1.09, 109.5, (-120.35 if gly else -118.0) * one)
    return dict(CA0=CA0, C0=C0, O0=O0, N1=N1, H1=H1, CA1=CA1, HA=HA, CB=CB, C1=C1, O1=O1, N2=N2,
                H2=H2, CA2=CA2)


BONDS = [("CA0", "C0"), ("C0", "O0"), ("C0", "N1"), ("N1", "H1"), ("N1", "CA1"), ("CA1", "HA"),
         ("CA1", "CB"), ("CA1", "C1"), ("C1", "O1"), ("C1", "N2"), ("N2", "H2"), ("N2", "CA2")]
GROUPS = {"CA0": 0, "C0": 0, "O0": 0, "N1": 0, "H1": 0, "CA1": 1, "HA": 1, "CB": 1,
          "C1": 2, "O1": 2, "N2": 2, "H2": 2, "CA2": 2}


def params(gly):
    # (half of r_min in A, epsilon in kcal/mol, partial charge); methyls are united atoms
    t = {"CA0": (2.00, 0.18, 0.0), "C0": (1.908, 0.086, 0.597), "O0": (1.661, 0.21, -0.568),
         "N1": (1.824, 0.17, -0.416), "H1": (0.60, 0.0157, 0.272), "CA1": (1.908, 0.109, 0.034),
         "HA": (1.387, 0.0157, 0.082), "CB": (2.00, 0.18, 0.0), "C1": (1.908, 0.086, 0.597),
         "O1": (1.661, 0.21, -0.568), "N2": (1.824, 0.17, -0.416), "H2": (0.60, 0.0157, 0.272),
         "CA2": (2.00, 0.18, 0.0)}
    if gly:
        t["CB"] = (1.387, 0.0157, 0.082)
    return t


def graph_distance():
    names = list(GROUPS)
    adj = {n: set() for n in names}
    for a, b in BONDS:
        adj[a].add(b)
        adj[b].add(a)
    dist = {}
    for s in names:
        seen, front, d = {s: 0}, [s], 0
        while front:
            d += 1
            nxt = []
            for u in front:
                for v in adj[u]:
                    if v not in seen:
                        seen[v] = d
                        nxt.append(v)
            front = nxt
        dist[s] = seen
    return dist


def energy(phi, psi, gly):
    X = build(phi, psi, gly)
    par = params(gly)
    gd = graph_distance()
    names = list(GROUPS)
    E = np.zeros(phi.shape)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            if GROUPS[a] == GROUPS[b] or gd[a][b] < 3:
                continue
            r = np.linalg.norm(X[a] - X[b], axis=-1)
            ra, ea, qa = par[a]
            rb, eb, qb = par[b]
            rm, eps = ra + rb, np.sqrt(ea * eb)
            lj = eps * ((rm / r) ** 12 - 2 * (rm / r) ** 6)
            el = 332.06 * qa * qb / (4.0 * r)
            if gd[a][b] == 3:
                lj, el = lj / 2.0, el / 1.2
            E += lj + el
    return E


step = 3.0
ang = np.arange(-180, 180, step) + step / 2
PHI, PSI = np.meshgrid(ang, ang, indexing="xy")
EA = energy(PHI, PSI, False)
EG = energy(PHI, PSI, True)
EA -= EA.min()
EG -= EG.min()


def boltz(E):
    w = np.exp(-E / KT)
    return w / w.sum()


pA, pG = boltz(EA), boltz(EG)


def eff_fraction(p):
    return np.exp(-(p * np.log(p + 1e-300)).sum()) / p.size


fA, fG = eff_fraction(pA), eff_fraction(pG)
R = 8.314
dS = R * np.log(fG / fA)


def regions(p):
    alpha = (PHI < 0) & (PSI > -100) & (PSI <= 50)
    beta = (PHI < 0) & ((PSI > 50) | (PSI <= -150))
    left = PHI > 0
    return p[alpha].sum(), p[beta].sum(), p[left].sum()


IDEAL = {r"$\alpha_\mathrm{R}$": (-57, -47), r"$\beta$": (-139, 135), "PPII": (-75, 145),
         r"$\alpha_\mathrm{L}$": (57, 47), r"$3_{10}$": (-49, -26)}

fig, ax = bio.canvas(25.6, 7.4)
levels = np.arange(0, 8.01, 1.0)
cmap = "viridis"


def ramaplot(pax, Z, title, show_y=True, filled=True):
    pax.contourf(ang, ang, np.minimum(Z, 8.0), levels=levels, cmap=cmap, extend="max")
    pax.contour(ang, ang, Z, levels=[2.0], colors=[P.ink()], linewidths=0.7)
    for name, (f, s) in IDEAL.items():
        pax.plot(f, s, "o", ms=3.2, mfc="white", mec="black", mew=0.6)
        pax.text(f + 7, s + 7, name, fontsize=FT["tiny"], color="white")
    pax.set_xlim(-180, 180)
    pax.set_ylim(-180, 180)
    pax.set_xticks([-180, -90, 0, 90, 180])
    pax.set_yticks([-180, -90, 0, 90, 180])
    charts.style_axes(pax, r"$\varphi$ / deg", r"$\psi$ / deg" if show_y else None, box=True)
    charts.title(pax, title)


bio.panel(ax, "A", (0.1, 7.3))
pa = charts.axes_at(ax, (1.3, 1.2, 5.2, 5.2))
ramaplot(pa, EA, "L-Ala: energy")
bio.panel(ax, "B", (6.9, 7.3))
pb = charts.axes_at(ax, (8.0, 1.2, 5.2, 5.2))
lp = np.log10(np.maximum(pA / pA.max(), 1e-12))
pb.contourf(ang, ang, np.maximum(lp, -4), levels=np.arange(-4, 0.01, 0.5), cmap="magma")
for name, (f, s) in IDEAL.items():
    pb.plot(f, s, "o", ms=3.2, mfc="white", mec="black", mew=0.6)
a1, b1, l1 = regions(pA)
pb.text(-170, -95, f"α region {a1:.0%}", fontsize=FT["tiny"], color="white")
pb.text(-170, 160, f"β + PPII {b1:.0%}", fontsize=FT["tiny"], color="white", va="top")
pb.text(60, -150, f"φ > 0: {l1:.0%}", fontsize=FT["tiny"], color="white")
pb.set_xlim(-180, 180)
pb.set_ylim(-180, 180)
pb.set_xticks([-180, -90, 0, 90, 180])
pb.set_yticks([-180, -90, 0, 90, 180])
charts.style_axes(pb, r"$\varphi$ / deg", None, box=True)
charts.title(pb, "L-Ala: Boltzmann probability (log10)")
bio.panel(ax, "C", (13.6, 7.3))
pc = charts.axes_at(ax, (14.7, 1.2, 5.2, 5.2))
ramaplot(pc, EG, "Gly: energy", show_y=False)
cb = fig.colorbar(pc.collections[0], cax=charts.axes_at(ax, (20.1, 1.2, 0.22, 5.2)))
cb.set_label(r"$(E - E_\mathrm{min})$ / (kcal/mol)", fontsize=FT["tiny"], color=P.ink())
cb.ax.tick_params(labelsize=FT["tiny"], colors=P.muted(), labelcolor=P.ink())
cb.outline.set_edgecolor(P.muted())

# D: accessible fraction and entropy
bio.panel(ax, "D", (22.0, 7.3))
pd = charts.axes_at(ax, (23.4, 1.2, 1.8, 4.6))
pd.bar([0, 1], [fA, fG], width=0.6, color=[P.fill("protein"), P.fill("enzyme")],
       edgecolor=[P.edge("protein"), P.edge("enzyme")])
pd.set_xticks([0, 1])
pd.set_xticklabels(["Ala", "Gly"])
pd.set_xlim(-0.6, 1.6)
pd.set_ylim(0, max(fA, fG) * 1.2)
for i, v in enumerate((fA, fG)):
    pd.text(i, v + 0.01, f"{v:.2f}", ha="center", fontsize=FT["tiny"], color=P.ink())
pd.text(0.5, max(fA, fG) * 1.42, "ΔS = R ln(f$_\\mathrm{Gly}$/f$_\\mathrm{Ala}$)\n" + f"= {dS:.1f} J/(mol K)", ha="center",
        fontsize=FT["tiny"], color=P.ink())
charts.style_axes(pd, None, "accessible fraction of torus")
