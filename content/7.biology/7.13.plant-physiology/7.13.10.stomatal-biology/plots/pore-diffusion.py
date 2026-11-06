# Diffusion through small pores (Brown & Escombe 1900) and the anatomical maximum stomatal conductance
# (Franks & Farquhar 2001), 25 C.
# (A) Water-vapour flux through one circular pore of depth l = 8 um, J = pi r^2 D dc / (l + pi r / 2),
# compared with the "area-proportional" flux pi r^2 D dc / l (long-tube limit, scaled to match at small r is
# not done: both use the same l); right axis: flux per unit pore area relative to the 10-um-radius pore.
# Driving force: 1 kPa vapour-pressure difference, dc = dp / RT.
# (B) g_max = (D / v) N a / (l + (pi/2) sqrt(a / pi)) over stomatal density N for three pore areas a; the
# dot marks the leaf of Example 10.7.1 (N = 200 mm^-2, a = 78.5 um^2).
import matplotlib.pyplot as plt
import numpy as np

R, T, p = 8.314, 298.15, 101325.0
D = 2.49e-5
v = R * T / p
dc = 1000.0 / (R * T)  # mol m^-3 for 1 kPa
l = 8e-6

r = np.linspace(0.2e-6, 12e-6, 300)
J = np.pi * r**2 * D * dc / (l + np.pi * r / 2)
Jt = np.pi * r**2 * D * dc / l
Jthin = 2 * r * D * dc

fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.3))
a.plot(r * 1e6, J * 1e12, color="#2f7fbf", lw=2.3, label="pore of depth 8 µm, Eq. (10.1)")
a.plot(r * 1e6, Jt * 1e12, color="0.5", lw=1.5, ls="--", label="tube only (∝ area)")
a.plot(r * 1e6, Jthin * 1e12, color="#d9822b", lw=1.5, ls=":", label="thin septum (∝ diameter)")
a.set_xlim(0, 12)
a.set_ylim(0, 1.2 * J.max() * 1e12)
a.set_xlabel("Pore radius r / µm")
a.set_ylabel("Flux per pore / pmol s⁻¹")
a.legend(frameon=False, fontsize=8, loc="upper left")
a.set_title("A   One pore", loc="left", fontsize=10)
a2 = a.twinx()
per_area = J / (np.pi * r**2)
a2.plot(r * 1e6, per_area / per_area[np.argmin(abs(r - 10e-6))], color="#7a4fb3", lw=1.2, alpha=0.8)
a2.set_ylabel("Flux per pore area (relative)", color="#7a4fb3")
a2.set_ylim(0, 3.5)
a2.tick_params(axis="y", colors="#7a4fb3")

N = np.linspace(20, 400, 300) * 1e6
for area, col in ((40e-12, "#5aa05a"), (78.5e-12, "#2f7fbf"), (150e-12, "#c0504d")):
    g = (D / v) * N * area / (l + np.pi / 2 * np.sqrt(area / np.pi))
    b.plot(N / 1e6, g, color=col, lw=2, label=f"a = {area * 1e12:.0f} µm²")
N0, a0 = 200e6, 78.5e-12
g0 = (D / v) * N0 * a0 / (l + np.pi / 2 * np.sqrt(a0 / np.pi))
b.plot(N0 / 1e6, g0, "o", color="#2f7fbf", ms=7)
b.axvline(200, color="0.6", lw=0.6, ls=":")
b.set_xlabel("Stomatal density N / mm⁻²")
b.set_ylabel("g_max / (mol m⁻² s⁻¹)")
b.set_xlim(0, 400)
b.set_ylim(0, 3)
b.legend(frameon=False, fontsize=8, loc="upper left")
b.set_title("B   Maximum stomatal conductance", loc="left", fontsize=10)
for ax in (a, b):
    ax.spines["top"].set_visible(False)
b.spines["right"].set_visible(False)
fig.tight_layout()
