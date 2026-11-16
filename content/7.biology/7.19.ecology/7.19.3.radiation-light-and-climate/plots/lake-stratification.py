# Thermal structure of a deep temperate (dimictic) lake.
# A: density of pure water against temperature (Tilton and Taylor 1937 formula as used by Chen and Millero),
#    rho(T) = 1000 [1 - (T + 288.9414) (T - 3.9863)^2 / (508929.2 (T + 68.12963))] kg m^-3, maximum at 3.98 C.
# B: idealized seasonal temperature profiles (schematic, not measurements): winter inverse stratification
#    under ice, spring and autumn mixing (isothermal near 4 C and about 10 C), and summer stratification with
#    epilimnion (22 C, 0-6 m), metalimnion with the thermocline (6-11 m), hypolimnion (6 C), modelled with a
#    hyperbolic tangent.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P


def rho(T):
    return 1000 * (1 - (T + 288.9414) * (T - 3.9863) ** 2 / (508929.2 * (T + 68.12963)))


fig, (a, b) = plt.subplots(1, 2, figsize=(10.6, 4.5))
T = np.linspace(0, 30, 301)
a.plot(T, rho(T), color=P.edge("dna"), lw=2)
a.plot(3.98, rho(3.98), "o", color=P.edge("negative"), ms=5)
a.text(4.8, rho(3.98) + 0.05, "maximum density at 3.98 °C", fontsize=8, color=P.edge("negative"))
a.set_xlabel("Temperature / °C")
a.set_ylabel("Density / kg m⁻³")
a.set_title("A  Density of water", loc="left", fontweight="bold")

z = np.linspace(0, 30, 301)
summer = 6 + 16 * 0.5 * (1 - np.tanh((z - 8.5) / 1.4))
winter = 4 - 3.9 * np.exp(-z / 1.5)
spring = np.full_like(z, 4.2)
autumn = np.full_like(z, 10.0)
for prof, tok, name in ((winter, "dna", "winter (ice cover)"), (spring, "positive", "spring overturn"),
                        (summer, "negative", "summer stratification"), (autumn, "atp", "autumn overturn")):
    b.plot(prof, z, color=P.edge(tok), lw=2, label=name)
b.axhspan(0, 6, color=P.light("negative"), alpha=0.35, lw=0)
b.axhspan(6, 11, color=P.light("atp"), alpha=0.35, lw=0)
b.text(25.5, 3, "epilimnion", fontsize=8, color=P.ink(), ha="right")
b.text(25.5, 8.5, "metalimnion\n(thermocline)", fontsize=8, color=P.ink(), ha="right", va="center")
b.text(25.5, 15, "hypolimnion", fontsize=8, color=P.ink(), ha="right")
b.set_ylim(30, 0)
b.set_xlim(0, 26)
b.set_xlabel("Temperature / °C")
b.set_ylabel("Depth / m")
b.legend(frameon=False, fontsize=7.5, loc="lower right", bbox_to_anchor=(1.0, 0.18))
b.set_title("B  Seasonal profiles (schematic)", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
