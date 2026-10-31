# Magnetotactic bacteria as swimming compass needles.
# A: mean alignment of a magnetic dipole m in a field B at temperature T (Langevin function),
#    <cos theta> = coth(xi) - 1/xi, xi = m B / kT. Markers: a chain of 20 magnetite cubes of 50 nm
#    (m = 20 x 4.8e5 A/m x (50 nm)^3 = 1.2e-15 A m^2) in the geomagnetic field of 50 uT at 293 K (xi = 15)
#    and the same chain in 5 uT; an isolated magnetite nanoparticle of 50 nm (xi = 0.7).
# B: U-turns after a reversal of the field. The cell swims at v = 40 um/s along its body axis, whose angle phi
#    to the field obeys f_r dphi/dt = -m B sin(phi) (overdamped rotation, rotational drag f_r = 8 pi eta a^3,
#    a = 1 um, eta = 1 mPa s). At t = 0 the field is reversed (phi jumps from ~0 to ~pi); a small initial angle
#    (5 degrees) breaks the symmetry. The loop diameter is L = pi v f_r / (m B) and the U-turn time
#    tau = (f_r / m B) ln(2 m B / kT). Two moments shown (1.2e-15 and 0.4e-15 A m^2).
# C: alignment time and U-turn diameter against the magnetic moment (B = 50 uT).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
kT = 1.380649e-23 * 293
fig, axs = plt.subplots(1, 3, figsize=(13.4, 4.0), gridspec_kw=dict(width_ratios=[1, 1.1, 1]))

ax = axs[0]
xi = np.logspace(-2, 2.3, 400)
L = 1 / np.tanh(xi) - 1 / xi
ax.semilogx(xi, L, color=charts.line("dna"), lw=1.8)
ax.semilogx(xi, xi / 3, color=P.muted(), lw=0.8, ls=":")
m_chain = 20 * 4.8e5 * (50e-9) ** 3
for mm, B, lab in ((m_chain, 50e-6, "chain, 50 μT"), (m_chain, 5e-6, "chain, 5 μT"),
                   (4.8e5 * (50e-9) ** 3, 50e-6, "single crystal, 50 μT")):
    x = mm * B / kT
    y = 1 / np.tanh(x) - 1 / x
    ax.plot(x, y, "o", ms=5, color=charts.line("rna"))
    ax.text(x * 1.15, y - 0.07, f"{lab}\nξ = {x:.2g}", fontsize=6.8, color=P.ink())
ax.text(0.012, 0.12, "ξ/3 (weak field)", fontsize=6.8, color=P.muted())
ax.set_ylim(0, 1.05)
charts.style_axes(ax, "ξ = mB / kBT", "⟨cos θ⟩")
charts.title(ax, "A   Langevin alignment")

ax = axs[1]
eta, a, v = 1e-3, 1e-6, 40e-6
fr = 8 * np.pi * eta * a**3
B = 50e-6
for mm, tok in ((1.2e-15, "dna"), (0.4e-15, "enzyme")):
    dt = 1e-3
    phi = np.radians(5.0)
    x = y = 0.0
    xs, ys = [], []
    # swim 1 s aligned with B (along +x), then reverse the field
    for i in range(int(12.0 / dt)):
        t = i * dt
        if t < 1.0:
            target = 0.0
        else:
            target = np.pi
        phi += -mm * B / fr * np.sin(phi - target) * dt
        x += v * np.cos(phi) * dt
        y += v * np.sin(phi) * dt
        xs.append(x)
        ys.append(y)
    Ld = np.pi * v * fr / (mm * B)
    ax.plot(np.array(xs) * 1e6, np.array(ys) * 1e6, color=charts.line(tok), lw=1.6,
            label=f"m = {mm:.1e} A m², L = {Ld * 1e6:.0f} μm")
ax.annotate("", xy=(0, -30), xytext=(60, -30), arrowprops=dict(arrowstyle="-|>", color=P.muted()))
ax.text(30, -26, "B after reversal (t > 1 s)", fontsize=7, ha="center", va="bottom", color=P.muted())
ax.set_ylim(-45, 190)
ax.legend(fontsize=6.8, frameon=False, loc="upper left")
charts.style_axes(ax, "x / μm", "y / μm")
charts.title(ax, "B   U-turns after field reversal")

ax = axs[2]
m = np.logspace(-16, -14, 200)
tau0 = fr / (m * B)
ax.loglog(m, tau0, color=charts.line("dna"), lw=1.6, label=r"alignment time $f_{\mathrm{r}}/mB$ / s")
ax.loglog(m, tau0 * np.log(2 * m * B / kT), color=charts.line("protein"), lw=1.6, label="U-turn time / s")
ax.loglog(m, np.pi * v * tau0 * 1e6 / 100, color=charts.line("rna"), lw=1.6, ls="--",
          label="U-turn diameter / (100 μm)")
ax.axvline(m_chain, color=P.muted(), lw=0.6, ls=":")
ax.legend(fontsize=6.8, frameon=False, loc="upper right")
charts.style_axes(ax, "magnetic moment m / (A m²)", "value")
charts.title(ax, "C   Stronger magnets turn faster")
fig.tight_layout()
