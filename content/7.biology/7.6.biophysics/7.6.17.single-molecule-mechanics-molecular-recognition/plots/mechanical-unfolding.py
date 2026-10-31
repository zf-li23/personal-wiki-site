# Mechanical unfolding of single molecules (simulations).
# A: AFM force-extension "sawtooth" of a polyprotein of eight titin I27-like immunoglobulin domains, pulled at
#    400 nm/s with a cantilever of stiffness 50 pN/nm. The unfolded polypeptide is a worm-like chain
#    (persistence length 0.4 nm, Marko-Siggia); each unfolding adds 28 nm of contour length. Domains unfold
#    stochastically with the Bell rate k(F) = k0 exp(F x/kT), k0 = 3.3e-4 /s, x = 0.25 nm; dashed: WLC curves
#    with contour lengths increasing in steps of 28 nm.
# B: an RNA hairpin held at constant force hops between folded and unfolded states (two-state, extension change
#    18 nm, equal rates of 2 /s at F_1/2 = 15.0 pN, transition-state distances 9 nm on each side), with 2 nm
#    measurement noise. C: open probability and ln(k_open / k_close) against force: a sigmoid of width
#    kT/dx = 0.23 pN and a straight line of slope dx/kT.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
kT = 4.11


def wlc_force(x, Lc, p=0.4):
    r = np.clip(x / Lc, 0, 0.999)
    return kT / p * (r + 1 / (4 * (1 - r) ** 2) - 0.25)


fig, axs = plt.subplots(1, 3, figsize=(14, 4.2), gridspec_kw={"width_ratios": [1.4, 1.2, 0.9]})
kc, v, dt = 50.0, 400.0, 2e-5
k0, xb, dL, L0, ndom = 3.3e-4, 0.25, 28.0, 40.0, 8
folded, Lc, t = ndom, L0, 0.0
xs, Fs = [], []
x = 0.0
while folded >= 0 and t < 2.0:
    z = v * t
    if z > 0:
        x = brentq(lambda q: kc * (z - q) - wlc_force(q, Lc), 0, min(z, 0.999 * Lc))
    F = kc * (z - x)
    xs.append(x)
    Fs.append(F)
    if folded > 0 and rng.random() < folded * k0 * np.exp(F * xb / kT) * dt:
        folded -= 1
        Lc += dL
    if F > 600:
        break
    t += dt
xs, Fs = np.array(xs), np.array(Fs)
axs[0].plot(xs, Fs, color=charts.line("protein"), lw=1.0)
for k in range(ndom + 1):
    q = np.linspace(1, 0.97 * (L0 + k * dL), 200)
    axs[0].plot(q, wlc_force(q, L0 + k * dL), color=P.muted(), lw=0.6, ls="--")
axs[0].set_ylim(-20, 450)
axs[0].set_xlim(0, L0 + ndom * dL + 20)
charts.style_axes(axs[0], "extension / nm", "force / pN")
charts.title(axs[0], "A   AFM sawtooth of an (I27)₈ polyprotein")

Fh, dx, k_half, xu = 15.0, 18.0, 2.0, 9.0
for i, (F, tok) in enumerate(((14.8, "dna"), (15.0, "neutral"), (15.2, "rna"))):
    ko = k_half * np.exp((F - Fh) * xu / kT)
    kcl = k_half * np.exp(-(F - Fh) * (dx - xu) / kT)
    T, dtt = 10.0, 1e-3
    n = int(T / dtt)
    s = np.zeros(n, int)
    for j in range(1, n):
        r = ko if s[j - 1] == 0 else kcl
        s[j] = 1 - s[j - 1] if rng.random() < r * dtt else s[j - 1]
    y = s * dx + rng.normal(0, 2.0, n) + i * 40
    axs[1].plot(np.arange(n) * dtt, y, color=charts.line(tok), lw=0.4)
    axs[1].text(10.2, i * 40 + 9, f"{F} pN\np_open = {s.mean():.2f}", fontsize=7.5, color=P.ink(), va="center")
axs[1].set_xlim(0, 12)
axs[1].set_yticks([])
charts.style_axes(axs[1], "time / s", "extension (offset) / nm")
charts.title(axs[1], "B   Hopping at constant force")

F = np.linspace(14, 16, 200)
po = 1 / (1 + np.exp(-(F - Fh) * dx / kT))
axs[2].plot(F, po, color=charts.line("rna"), lw=1.8)
ax2 = axs[2].twinx()
ax2.plot(F, (F - Fh) * dx / kT, color=charts.line("dna"), lw=1.2, ls="--")
ax2.set_ylabel("ln (k_open / k_close)", color=charts.line("dna"), fontsize=8)
ax2.tick_params(colors=P.muted(), labelcolor=charts.line("dna"), labelsize=7)
for sp in ax2.spines.values():
    sp.set_color(P.muted())
charts.style_axes(axs[2], "force / pN", "open probability")
charts.title(axs[2], "C   Force tilts the equilibrium")
fig.tight_layout()
