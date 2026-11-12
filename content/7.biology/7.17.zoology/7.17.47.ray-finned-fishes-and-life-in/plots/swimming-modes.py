# Swimming modes of fishes: the lateral envelope of body undulation (dorsal view, head to the left) for
# anguilliform, subcarangiform, carangiform and thunniform swimming. The midline is modelled as a travelling
# wave h(x, t) = A(x) sin(2 pi (x / lambda - f t)) with amplitude envelope A(x) = a0 + a1 x + a2 x^2 and
# wavelength lambda (in body lengths) chosen to match typical published kinematics (eel lambda ~ 0.6 L,
# trout ~ 0.9 L, jack ~ 1.1 L, tuna ~ 1.3 L; tail-tip amplitude ~ 0.1 L). Ten midlines through one
# tailbeat are drawn, with the body outline at one instant. Schematic, not measured data.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 10.5)
MODES = [("Anguilliform (eel)", 0.6, (0.035, 0.0, 0.065)), ("Subcarangiform (trout, carp)", 0.9, (0.01, 0.0, 0.09)),
         ("Carangiform (jack, herring)", 1.1, (0.005, -0.02, 0.115)), ("Thunniform (tuna)", 1.3, (0.004, -0.03, 0.126))]
x = np.linspace(0, 1, 160)
L, x0 = 8.5, 1.0
for k, (name, lam, (a0, a1, a2)) in enumerate(MODES):
    col, row = k % 2, k // 2
    ox, oy = x0 + col * 12.0, 7.6 - row * 4.6
    A = a0 + a1 * x + a2 * x ** 2
    for i, t in enumerate(np.linspace(0, 1, 10, endpoint=False)):
        h = A * np.sin(2 * np.pi * (x / lam - t))
        ax.plot(ox + x * L, oy + h * L, color=P.mix(P.muted(), P.surface(), 0.35), lw=0.8, zorder=3)
    h = A * np.sin(2 * np.pi * (x / lam - 0.2))
    wmax = 0.025 if k == 0 else 0.05
    w = np.where(x < 0.25, wmax * np.sqrt(x / 0.25), wmax * (1 - 0.9 * np.clip((x - 0.25) / 0.75, 0, 1)))
    w = np.maximum(w, 0.003)
    top = np.column_stack([ox + x * L, oy + (h + w) * L])
    bot = np.column_stack([ox + x[::-1] * L, oy + (h[::-1] - w[::-1]) * L])
    bio.shape(ax, np.vstack([top, bot]), token="animal", zorder=5)
    ax.plot(ox + x * L, oy + A * L, color=P.edge("dna"), lw=1.2, ls="--", zorder=4)
    ax.plot(ox + x * L, oy - A * L, color=P.edge("dna"), lw=1.2, ls="--", zorder=4)
    bio.label(ax, (ox, oy + 1.75), name, size="small", ha="left", bold=True)
    bio.label(ax, (ox + L + 0.2, oy), f"wavelength {lam:.1f} L", size="tiny", ha="left", color=P.muted())
bio.label(ax, (0.6, 0.35), "Dashed: amplitude envelope; grey: midlines through one tailbeat (model)", size="tiny",
          color=P.muted(), ha="left")
