# Muscle architecture trades force for speed at constant volume (simplified planar model, fibre angle constant).
# Three muscles of the same volume V = 200 cm^3 and specific tension sigma = 25 N cm^-2:
#   parallel, fibre length L_f = 20 cm, pennation angle theta = 0;  pennate, L_f = 8 cm, theta = 20 deg;
#   pennate, L_f = 4 cm, theta = 30 deg.
# PCSA = V / L_f; isometric force along the tendon F0 = sigma PCSA cos(theta); fibres shorten at up to
# 5 L_f per second and the tendon moves 1 / cos(theta) times faster than the fibres (architectural gear),
# so v_max = 5 L_f / cos(theta). Hill curvature a/F0 = 0.25. Usable excursion along the tendon about
# 0.4 L_f / cos(theta) (sarcomeres from about 2.8 to 1.7 um).
# (A) force-velocity along the tendon; (B) power: the maximum is the same, set by volume alone;
# (C) isometric force, maximal speed and excursion of the three designs.
import matplotlib.pyplot as plt
import numpy as np

V, sigma, al = 200.0, 25.0, 0.25
designs = [("parallel, L_f = 20 cm, θ = 0°", 20.0, 0.0, "#2f6fb5"),
           ("pennate, L_f = 8 cm, θ = 20°", 8.0, 20.0, "#7a5fb0"),
           ("pennate, L_f = 4 cm, θ = 30°", 4.0, 30.0, "#c0504d")]
fig, (a, b, c) = plt.subplots(1, 3, figsize=(13.5, 4.2))
f = np.linspace(0, 1, 400)
rows = []
for name, Lf, th, col in designs:
    ct = np.cos(np.radians(th))
    F0 = sigma * V / Lf * ct
    vmax = 5 * Lf / ct / 100  # m/s
    v = vmax * al * (1 - f) / (f + al)
    a.plot(v, f * F0, color=col, lw=2.2, label=name)
    b.plot(v, f * F0 * v, color=col, lw=2.2, label=name)
    rows.append((F0, vmax, 0.4 * Lf / ct, col))
a.set_xlabel("Shortening velocity of the tendon / (m s⁻¹)")
a.set_ylabel("Force along the tendon / N")
a.legend(frameon=False, fontsize=8.5)
a.set_title("A   Force-velocity at equal volume", loc="left", fontsize=10)
b.set_xlabel("Shortening velocity of the tendon / (m s⁻¹)")
b.set_ylabel("Power / W")
b.text(0.5, 26.5, "same peak power ≈ 0.096 σ V × 5 s⁻¹", fontsize=8.5, color="0.45")
b.set_ylim(0, 30)
b.set_title("B   Power is set by volume", loc="left", fontsize=10)
labels = ["F₀ / kN", "v_max / (m s⁻¹)", "excursion / (10 cm)"]
x = np.arange(3)
for k, (F0, vmax, exc, col) in enumerate(rows):
    c.bar(x + (k - 1) * 0.26, [F0 / 1000, vmax, exc / 10], width=0.26, color=col)
c.set_xticks(x)
c.set_xticklabels(labels, fontsize=8.5)
c.set_title("C   The trade-off", loc="left", fontsize=10)
for ax in (a, b, c):
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
