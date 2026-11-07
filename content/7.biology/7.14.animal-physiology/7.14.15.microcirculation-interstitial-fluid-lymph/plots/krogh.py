"""Krogh cylinder: a capillary of radius r_c supplies a coaxial tissue cylinder of radius R that consumes O2
at a uniform rate M. Steady radial diffusion, K (1/r) d/dr (r dP/dr) = M with P(r_c) = P_c and dP/dr = 0 at R:
    P(r) = P_c + M/(4K) (r^2 - r_c^2) - M R^2/(2K) ln(r / r_c).
K = D alpha (Krogh diffusion constant): D = 2000 um^2/s, alpha = 3e-5 mL O2 per mL per mmHg.
M in mL O2 per mL tissue per s: resting muscle 1e-4, exercising muscle 1e-3 to 3e-3 (heart at rest about 1.5e-3).
A: radial profiles at P_c = 30 mmHg (near the venous end), R = 25 um (about 500 capillaries per mm^2).
B: minimum tissue PO2 (at r = R) against R for several M (top axis: capillary density n = 1/(pi R^2)).
C: along the capillary (length 0.5 mm): blood PO2 from the Hill curve (n = 2.7, P50 = 26.8 mmHg, capacity
0.2 mL O2/mL) as O2 is removed, and the PO2 at the far corner of the cylinder. Rest: M = 1e-4, flow set for 25 %
extraction. Exercise: M = 3e-3 with flow 10x; with capillary recruitment R falls from 25 to 15 um.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
K = 2000 * 3e-5
rc = 3.0


def profile(r, Pc, M, R):
    return Pc + M / (4 * K) * (r**2 - rc**2) - M * R**2 / (2 * K) * np.log(r / rc)


def drop(M, R):
    return Pc0 - profile(R, Pc0, M, R)


Pc0 = 30.0
fig, axs = plt.subplots(1, 3, figsize=(13, 4.2))
ax, bx, cx = axs
cols = [P.edge("dna"), P.edge("positive"), P.edge("protein"), P.edge("blood")]
Ms = [1e-4, 1e-3, 2e-3, 3e-3]
labs = ["rest, M = 0.1", "M = 1", "M = 2", "M = 3 (heavy exercise)"]
R = 25.0
r = np.linspace(rc, R, 200)
for M, c, l in zip(Ms, cols, labs):
    ax.plot(r, np.maximum(profile(r, Pc0, M, R), 0), color=c, lw=2, label=l)
ax.axvspan(0, rc, color=P.fill("blood"), alpha=0.35, lw=0)
ax.text(rc / 2, 30, "capillary", rotation=90, ha="center", va="top", fontsize=8, color=P.muted())
ax.set_xlim(0, R)
ax.set_ylim(0, 32)
ax.set_xlabel("Distance from capillary axis r / um")
ax.set_ylabel("Tissue PO$_2$ / mmHg")
ax.legend(frameon=False, fontsize=7.5, title="M / 10$^{-3}$ mL O$_2$ mL$^{-1}$ s$^{-1}$", title_fontsize=7.5)
ax.set_title("A  Radial profiles (P$_c$ = 30, R = 25 um)", loc="left", fontsize=10)

Rs = np.linspace(8, 40, 200)
for M, c, l in zip(Ms, cols, labs):
    bx.plot(Rs, Pc0 - drop(M, Rs), color=c, lw=2)
bx.axhline(0, color=P.muted(), lw=1)
bx.fill_between(Rs, -40, 0, color=P.fill("negative"), alpha=0.25, lw=0)
bx.text(30, -15, "anoxic corner", fontsize=8, color=P.muted(), ha="center")
bx.set_ylim(-40, 32)
bx.set_xlabel("Tissue cylinder radius R / um")
bx.set_ylabel("PO$_2$ at r = R / mmHg")
top = bx.secondary_xaxis("top", functions=(lambda R: 1e6 / (np.pi * np.maximum(R, 1) ** 2), lambda n: np.sqrt(1e6 / (np.pi * np.maximum(n, 1)))))
top.set_xticks([2000, 1000, 500, 300, 200])
top.set_xlabel("Capillaries per mm$^2$", fontsize=8)
bx.text(0.0, 1.2, "B  Density sets the worst-supplied point", transform=bx.transAxes, fontsize=10)

n, P50, cap, L = 2.7, 26.8, 0.2, 500.0


def sat(p):
    return p**n / (p**n + P50**n)


def p_of_s(s):
    s = np.clip(s, 1e-4, 0.9999)
    return P50 * (s / (1 - s)) ** (1 / n)


z = np.linspace(0, L, 200)
Sa = sat(95.0)
cases = [("rest", 1e-4, 25.0, 0.25, P.edge("dna"), "-"),
         ("exercise, no recruitment", 3e-3, 25.0, 0.25 * 30 / 10, P.edge("blood"), "-"),
         ("exercise, R = 15 um", 3e-3, 15.0, 0.25 * 30 / 10, P.edge("positive"), "-")]
for name, M, Rr, E, c, ls in cases:
    E = min(E, 0.95)
    S = Sa * (1 - E * z / L)
    pb = p_of_s(S)
    if Rr != 15.0:
        cx.plot(z, pb, color=c if M < 1e-3 else P.ink(), lw=2, label="rest: blood" if M < 1e-3 else "exercise: blood")
    cx.plot(z, pb - drop(M, Rr), color=c, lw=1.6, ls="--", label=f"{name}: corner")
cx.axhline(0, color=P.muted(), lw=1)
cx.fill_between(z, -40, 0, color=P.fill("negative"), alpha=0.25, lw=0)

cx.set_ylim(-40, 100)
cx.set_xlabel("Distance along capillary / um (arterial to venous)")
cx.set_ylabel("PO$_2$ / mmHg")
cx.legend(frameon=False, fontsize=7.5, loc="upper right")
cx.set_title("C  The lethal corner at the venous end", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
