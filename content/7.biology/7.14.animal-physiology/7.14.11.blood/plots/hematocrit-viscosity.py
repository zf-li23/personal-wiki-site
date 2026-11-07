# Blood viscosity and oxygen transport against hematocrit.
# Relative apparent viscosity (to plasma) in glass tubes of diameter D at high shear, from the empirical fit of
# Pries, Neuhaus & Gaehtgens (1992):
#   eta_0.45 = 220 exp(-1.3 D) + 3.2 - 2.44 exp(-0.06 D^0.645)
#   C = (0.8 + exp(-0.075 D)) (-1 + 1/(1 + 1e-11 D^12)) + 1/(1 + 1e-11 D^12)
#   eta_rel = 1 + (eta_0.45 - 1) ((1 - H)^C - 1) / ((1 - 0.45)^C - 1)
# A: eta_rel against H for a large vessel (D = 1 mm) and narrow tubes (smaller apparent viscosity: the
# Fahraeus-Lindqvist effect, treated with the vessels). B: at a fixed pressure difference flow is proportional
# to 1/eta, and the O2 content to H, so O2 delivery is proportional to H / eta(H) (normalized to H = 0.45).
import matplotlib.pyplot as plt
import numpy as np


def eta_rel(H, D):
    e45 = 220 * np.exp(-1.3 * D) + 3.2 - 2.44 * np.exp(-0.06 * D ** 0.645)
    g = 1 / (1 + 1e-11 * D ** 12)
    C = (0.8 + np.exp(-0.075 * D)) * (-1 + g) + g
    return 1 + (e45 - 1) * ((1 - H) ** C - 1) / ((1 - 0.45) ** C - 1)


H = np.linspace(0.0, 0.75, 400)
fig, (axa, axb) = plt.subplots(1, 2, figsize=(10.5, 4.2))
styles = [(1000, "#c0392b", "D = 1 mm"), (50, "#2f6fb5", "D = 50 µm"), (15, "#7a4fb3", "D = 15 µm")]
for D, c, lab in styles:
    axa.plot(H, eta_rel(H, D), color=c, lw=2, label=lab)
    q = H / eta_rel(H, D)
    q0 = 0.45 / eta_rel(0.45, D)
    axb.plot(H, q / q0, color=c, lw=2, label=lab)
    i = int(np.argmax(q))
    axb.plot(H[i], q[i] / q0, "o", color=c, ms=5)
for ax in (axa, axb):
    ax.axvspan(0.40, 0.50, color="#9e9e9e", alpha=0.18, lw=0)
    ax.set_xlabel("Hematocrit $H$")
    ax.set_xlim(0, 0.75)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
axa.text(0.45, 7.4, "normal", ha="center", fontsize=8.5)
axa.set_ylim(0, 8)
axa.set_ylabel("Viscosity relative to plasma")
axa.set_title("A  Viscosity rises steeply with H", loc="left", fontsize=11, fontweight="bold")
axa.legend(frameon=False, fontsize=8.5, loc="upper left")
axb.set_ylim(0, 1.3)
axb.set_ylabel("O$_2$ delivery $\\propto H/\\eta$ (H = 0.45 is 1)")
axb.set_title("B  A broad optimum", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8.5, loc="lower center")
fig.tight_layout()
