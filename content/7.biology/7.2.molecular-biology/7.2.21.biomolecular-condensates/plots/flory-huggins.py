# Flory-Huggins free energy of mixing per lattice site, f/kT = (phi/N) ln phi + (1 - phi) ln(1 - phi)
# + chi phi (1 - phi), for a polymer of N segments in a solvent of monomers.
# A: f(phi) for N = 100 at chi = 0.50, chi_c = 0.605 and 0.70, each drawn after subtracting its chord between
#    the two coexisting compositions at chi = 0.70 (dots; for chi = 0.70 the chord is the common tangent).
#    A curve below its chord is stable as one phase; the chi = 0.70 curve bulges above it, so the mixture
#    lowers its free energy by splitting into the two dotted compositions. Crosses: spinodal (f'' = 0).
# B: phase diagrams in the (phi, chi) plane for N = 1, 10 and 100: binodal (solid, from equal exchange
#    chemical potential and equal osmotic pressure in the two phases) and spinodal (dashed, f'' = 0),
#    with the critical points phi_c = 1/(1 + sqrt N), chi_c = (1 + 1/sqrt N)^2 / 2. Larger chi means stronger
#    effective attraction (lower temperature for an upper critical point). As N grows the critical point moves
#    to small phi and chi_c falls toward 1/2, and the dilute branch of the binodal hugs phi = 0.
# C: the dilute-phase volume fraction (log scale) on the binodal against chi for the same N: a polymer of 100
#    segments has a saturation concentration many orders of magnitude below that of a small molecule with the
#    same per-segment interaction.
import matplotlib.pyplot as plt
import numpy as np

np.seterr(all="ignore")
from scipy.optimize import fsolve

import wikibio as bio
from wikibio import charts

P = bio.P


def f(phi, N, chi):
    return phi / N * np.log(phi) + (1 - phi) * np.log(1 - phi) + chi * phi * (1 - phi)


def df(phi, N, chi):
    return (np.log(phi) + 1) / N - np.log(1 - phi) - 1 + chi * (1 - 2 * phi)


def crit(N):
    s = np.sqrt(N)
    return 1 / (1 + s), 0.5 * (1 + 1 / s) ** 2


def spinodal(N, chi):
    # 1/(N phi) + 1/(1 - phi) = 2 chi  ->  2 chi N phi^2 + (N - 1 - 2 chi N) phi + 1 = 0
    a, b, c = 2 * chi * N, N - 1 - 2 * chi * N, 1.0
    disc = b * b - 4 * a * c
    if disc < 0:
        return None
    r = np.sqrt(disc)
    return (-b - r) / (2 * a), (-b + r) / (2 * a)


def binodal(N, chi, guess):
    # unknowns u = ln(phi1), w = ln(1 - phi2); equal mu = f' and equal Pi = phi f' - f in the two phases
    def eqs(z):
        p1, p2 = np.exp(z[0]), 1 - np.exp(z[1])
        mu1, mu2 = df(p1, N, chi), df(p2, N, chi)
        return [mu1 - mu2, (p1 * mu1 - f(p1, N, chi)) - (p2 * mu2 - f(p2, N, chi))]

    z = fsolve(eqs, [np.log(guess[0]), np.log(1 - guess[1])], xtol=1e-13)
    if np.max(np.abs(eqs(z))) > 1e-9:
        return None
    return np.exp(z[0]), 1 - np.exp(z[1])


def binodal_curve(N, chi_max=2.4, n=600):
    """Binodal by continuation from a deep quench (chi = 2.4) toward the critical point: rows (chi, phi_dilute,
    phi_dense) with chi <= chi_max."""
    pc, cc = crit(N)
    top = 2.4
    chis = cc + (top - cc) * np.linspace(1, 0, n) ** 2
    out, g = [], (np.exp(-N * (top - 0.5)) if N > 1 else np.exp(-top), 1 - np.exp(-top))
    for chi in chis[:-1]:
        r = binodal(N, chi, g)
        if r is None or not (r[0] < pc < r[1]):
            break
        out.append((chi, *r))
        g = r
    out = np.array(out[::-1])
    return out[out[:, 0] <= chi_max]


fig, axs = plt.subplots(1, 3, figsize=(13.2, 4.0), gridspec_kw={"width_ratios": [1.0, 1.05, 0.95]})

# --- A ---
ax = axs[0]
N = 100
pc, cc = crit(N)
chi_hi = 0.70
b = binodal_curve(N, chi_hi)
p1, p2 = b[-1, 1], b[-1, 2]
phi = np.linspace(1e-6, 0.6, 1500)
for chi, tok, name in ((0.50, "dna", "χ = 0.50"), (cc, "positive", f"χ = χc = {cc:.3f}"), (chi_hi, "negative", "χ = 0.70")):
    slope = (f(p2, N, chi) - f(p1, N, chi)) / (p2 - p1)
    g = f(phi, N, chi) - (f(p1, N, chi) + slope * (phi - p1))
    ax.plot(phi, 1e3 * g, color=charts.line(tok), lw=1.7, label=name)
s_hi = (f(p2, N, chi_hi) - f(p1, N, chi_hi)) / (p2 - p1)
g1 = lambda x: 1e3 * (f(x, N, chi_hi) - (f(p1, N, chi_hi) + s_hi * (x - p1)))
ax.plot([p1, p2], [g1(p1), g1(p2)], "o", color=charts.line("negative"), ms=4.5)
sp = spinodal(N, chi_hi)
ax.plot(sp, [g1(sp[0]), g1(sp[1])], "x", color=charts.line("negative"), ms=6, mew=1.5)
ax.axhline(0, color=P.muted(), lw=0.7, ls=":")
ax.set_xlim(0, 0.6)
ax.set_ylim(-12, 4)
ax.legend(fontsize=7, frameon=False, loc="lower left")
ax.text(0.36, -11, "binodal ●   spinodal ×", fontsize=7, color=P.muted())
charts.style_axes(ax, "polymer volume fraction φ", "10³ × (f − chord) / kBT")
ax.set_title("A   Free energy of mixing (N = 100)", loc="left", fontsize=9, color=P.ink())

# --- B ---
ax = axs[1]
styles = ((1, "dna"), (10, "positive"), (100, "negative"))
for N, tok in styles:
    pc, cc = crit(N)
    b = binodal_curve(N)
    x = np.r_[b[::-1, 1], pc, b[:, 2]]
    y = np.r_[b[::-1, 0], cc, b[:, 0]]
    ax.plot(x, y, color=charts.line(tok), lw=1.8, label=f"N = {N}")
    sx, sy = [], []
    for chi in np.linspace(cc, 2.4, 400):
        s = spinodal(N, chi)
        if s is not None:
            sx.append(s)
            sy.append(chi)
    sx = np.array(sx)
    ax.plot(np.r_[sx[::-1, 0], sx[:, 1]], np.r_[sy[::-1], sy], color=charts.line(tok), lw=1.1, ls=(0, (4, 2.4)))
    ax.plot([pc], [cc], "o", color=charts.line(tok), ms=4)
ax.axhline(0.5, color=P.muted(), lw=0.7, ls=":")
ax.text(0.74, 0.43, "χ = 1/2", fontsize=7, color=P.muted())
ax.set_xlim(0, 1)
ax.set_ylim(0.3, 2.4)
ax.legend(fontsize=7, frameon=False, loc="lower right", bbox_to_anchor=(1.0, 0.12))
ax.text(0.50, 1.45, "two phases", fontsize=8, color=P.ink(), ha="center")
ax.text(0.30, 0.38, "one phase", fontsize=8, color=P.ink(), ha="center")
charts.style_axes(ax, "polymer volume fraction φ", "interaction parameter χ")
ax.set_title("B   Phase diagrams: binodal (solid), spinodal (dashed)", loc="left", fontsize=9, color=P.ink())

# --- C ---
ax = axs[2]
for N, tok in styles:
    pc, cc = crit(N)
    b = binodal_curve(N)
    ax.semilogy(b[:, 0], b[:, 1], color=charts.line(tok), lw=1.8, label=f"N = {N}")
ax.set_xlim(0.4, 2.4)
ax.set_ylim(1e-30, 1)
ax.legend(fontsize=7, frameon=False, loc="lower left")
charts.style_axes(ax, "interaction parameter χ", "dilute-phase φ (saturation)")
ax.set_title("C   Saturation concentration", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
