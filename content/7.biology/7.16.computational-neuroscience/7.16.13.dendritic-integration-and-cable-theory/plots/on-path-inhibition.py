"""Where shunting inhibition is most effective: on the path to the soma or off it (steady state).

Passive tree: soma (diameter 20 um) - trunk (3 um, 300 um) - two daughter branches A and B
(1.89 um = 3 um / 2^(2/3), 500 um each; Rall's 3/2 rule holds at the branch point), 25 um
compartments, R_m = 20 kOhm cm^2, R_i = 100 Ohm cm. An excitatory conductance (g_e = 1 nS,
E_e = 0 mV) sits on branch A, 300 um from the branch point. An inhibitory conductance
(E_i = E_L = -65 mV, i.e. purely shunting) of 0 to 40 nS is placed at one of five sites.
The steady-state somatic depolarization V_soma - E_L is computed by solving the linear system
(G + diag(g_syn)) V = G_L E_L + g_e E_e + g_i E_i.
A: the tree (soma, trunk, branches) with excitation (triangle) and the inhibitory sites.
B: reduction of the somatic EPSP (percent) against g_i: sites on the path from the excitatory
   synapse to the soma (trunk, proximal on A) are most effective, a site distal to the
   excitation or on the sister branch is least effective.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
EL, Ee, Ei = -65.0, 0.0, -65.0
gm = 5e-4  # nS / um^2
Ri_um = 1e6
seg = 25.0
diam = {"trunk": 3.0, "A": 3.0 / 2 ** (2 / 3), "B": 3.0 / 2 ** (2 / 3)}
nt, nb = 12, 20
# node 0 = soma; trunk 1..nt; A nt+1..nt+nb; B nt+nb+1..nt+2nb
n = 1 + nt + 2 * nb
parent = np.zeros(n, int)
d = np.zeros(n)
d[0] = 20.0
for k in range(1, n):
    if k <= nt:
        parent[k] = k - 1
        d[k] = diam["trunk"]
    elif k <= nt + nb:
        parent[k] = nt if k == nt + 1 else k - 1
        d[k] = diam["A"]
    else:
        parent[k] = nt if k == nt + nb + 1 else k - 1
        d[k] = diam["B"]
area = np.where(np.arange(n) == 0, 4 * np.pi * 10.0**2, np.pi * d * seg)
gL = gm * area
G = np.diag(gL)
for k in range(1, n):
    p = parent[k]
    a1 = np.pi * (d[k] / 2) ** 2
    a2 = np.pi * (d[p] / 2) ** 2 if p else a1
    # series conductance between node centres (half segments); soma treated as a node of 12.5 um
    r = Ri_um * (0.5 * seg / a1 + 0.5 * seg / a2) if p else Ri_um * (seg / a1)
    g = 1e9 / r
    G[k, k] += g
    G[p, p] += g
    G[k, p] -= g
    G[p, k] -= g


def vsoma(ge_node, gi_node, gi):
    gs = np.zeros(n)
    rhs = gL * EL
    gs[ge_node] += 1.0
    rhs[ge_node] += 1.0 * Ee
    if gi_node is not None:
        gs[gi_node] += gi
        rhs[gi_node] += gi * Ei
    V = np.linalg.solve(G + np.diag(gs), rhs)
    return V[0] - EL


e_node = nt + 12
sites = [("soma", 0, P.edge("negative")),
         ("trunk (on path)", 6, P.edge("ca")),
         ("branch A proximal (on path)", nt + 5, P.edge("dna")),
         ("branch A distal to synapse (off path)", nt + nb, P.edge("positive")),
         ("sister branch B (off path)", nt + nb + 12, P.edge("protein"))]
gis = np.linspace(0, 40, 81)
fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.2), gridspec_kw=dict(width_ratios=[1, 1.25]))
ax = axs[0]
# layout: trunk upward from the soma, branches fan out
pos = {0: (0.0, 0.0)}
for k in range(1, nt + 1):
    pos[k] = (0.0, k * seg / 100.0)
top = pos[nt]
for k in range(nt + 1, nt + nb + 1):
    f = (k - nt) * seg / 100.0
    pos[k] = (top[0] - 0.6 * f, top[1] + 0.8 * f)
for k in range(nt + nb + 1, n):
    f = (k - nt - nb) * seg / 100.0
    pos[k] = (top[0] + 0.6 * f, top[1] + 0.8 * f)
for k in range(1, n):
    p = parent[k]
    ax.plot([pos[p][0], pos[k][0]], [pos[p][1], pos[k][1]], color=P.ink(), lw=0.8 + 0.9 * d[k] / 3.0, solid_capstyle="round")
ax.plot(*pos[0], "o", ms=14, color=P.fill("neuron"), mec=P.edge("neuron"), zorder=5)
ax.plot(*pos[e_node], "^", ms=11, color=P.edge("positive"), zorder=6)
ax.annotate("excitation", pos[e_node], xytext=(pos[e_node][0] - 1.5, pos[e_node][1] + 0.3), fontsize=8, color=P.ink(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.8))
for nm, node, c in sites:
    if node == 0:
        continue
    ax.plot(*pos[node], "s", ms=8, color=c, zorder=6)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("A  Tree and inhibitory sites", loc="left", fontsize=10)
ax = axs[1]
base = vsoma(e_node, None, 0.0)
for nm, node, c in sites:
    red = [100 * (1 - vsoma(e_node, node, g) / base) for g in gis]
    ax.plot(gis, red, color=c, lw=2.0, ls="--" if node == 6 else "-", label=nm)
ax.set_xlabel("Inhibitory conductance $g_{\\mathrm{i}}$ / nS")
ax.set_ylabel("Reduction of somatic EPSP / %")
ax.set_ylim(0, 100)
ax.set_title("B  Shunting is most effective on the path", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower right")
ax.grid(True, alpha=0.3)
fig.tight_layout()
