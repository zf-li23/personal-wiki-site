# Gastric acid secretion after a meal: cephalic, gastric and intestinal phases (minimal model).
# Meal (with protein) eaten at t = 0; sight and smell of food from t = -10 min.
#   P(t)  meal remaining in the stomach, emptied with rate constant k_e = 1/70 per min
#   c(t)  cephalic (vagal) drive, starts at -10 min and decays with time constant 25 min
#   G(t)  gastric drive (distension and gastrin): dG/dt = (P f(H) - G) / 8 min,
#         f(H) = 1 / (1 + (H / 1 mM)^2): acid in the antrum inhibits gastrin via somatostatin (D cells)
#   I(t)  intestinal drive, proportional to chyme entering the duodenum, k_e P, weight 6
#   S(t)  acid output = Smax D / (0.6 + D), D = 1.3 c + 1.6 G + I, Smax = 40 mmol/h
#   luminal acid: dA/dt = S - k_e A (mmol), buffered by the meal (60 mmol x P of buffer, pKa 4.5);
#   gastric volume 0.05 L + 0.6 L x P. Output is split among phases in proportion to their drives.
# A: acid output by phase (stacked). B: luminal pH: food buffers the acid at first; acid output is
# self-limited because falling pH suppresses gastrin.
import matplotlib.pyplot as plt
import numpy as np

dt = 0.05
t = np.arange(-30, 300, dt)
ke, Smax = 1 / 70, 40.0
Ka = 10 ** (-4.5) * 1e3
P = G = 0.0
A = 1.0
out = np.zeros((len(t), 3))
pH = np.zeros(len(t))
for i, ti in enumerate(t):
    if ti >= 0 and P == 0 and (ti - dt) < 0:
        P = 1.0
    c = np.exp(-(ti + 10) / 25) if ti >= -10 else 0.0
    V = 0.05 + 0.6 * P
    Ca, Cb = A / V, 60 * P / V
    # [H] + Cb [H]/([H] + Ka) = Ca  (mM), buffer pKa 4.5; quadratic in [H]
    b = Ka + Cb - Ca
    Hm = (-b + np.sqrt(b * b + 4 * Ka * Ca)) / 2 + 1e-4
    pH[i] = 3 - np.log10(Hm)
    free = Hm
    f = 1 / (1 + (free / 1.0) ** 2)
    I = 6 * ke * P
    D = 1.3 * c + 1.6 * G + I
    S = Smax * D / (0.6 + D)
    out[i] = S * np.array([1.3 * c, 1.6 * G, I]) / (D + 1e-12)
    G += dt * (P * f - G) / 8.0
    A += dt * (S / 60 - ke * A)
    P -= dt * ke * P

tot = out.sum(axis=0) * dt / 60
frac = tot / tot.sum()
fig, (axa, axb) = plt.subplots(1, 2, figsize=(11, 4.2))
cols = ("#2f6fb5", "#c0392b", "#d9822b")
names = ("cephalic", "gastric", "intestinal")
axa.stackplot(t, out.T, colors=cols, alpha=0.85,
              labels=[f"{n} ({100 * q:.0f} %)" for n, q in zip(names, frac)])
axa.axvline(0, color="0.5", lw=0.8, ls=":")
axa.text(1, 37, "meal", fontsize=8.5, color="0.4")
axa.set_xlabel("Time from start of meal / min")
axa.set_ylabel("Acid output / (mmol/h)")
axa.set_ylim(0, 42)
axa.set_title("A  Acid output by phase", loc="left", fontsize=11, fontweight="bold")
axa.legend(frameon=False, fontsize=8.5, loc="upper right")
axb.plot(t, pH, color="0.2", lw=1.8)
axb.axvline(0, color="0.5", lw=0.8, ls=":")
axb.axhline(3, color="#c0392b", lw=0.8, ls="--")
axb.text(295, 3.1, "gastrin suppressed below pH 3", ha="right", va="bottom", fontsize=8, color="#c0392b")
axb.set_xlabel("Time from start of meal / min")
axb.set_ylabel("Luminal pH")
axb.set_ylim(0.5, 7)
axb.set_title("B  Food buffers, acid feeds back", loc="left", fontsize=11, fontweight="bold")
fig.tight_layout()
