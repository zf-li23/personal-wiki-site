# A: PTH secretion versus ionized Ca2+ (four-parameter inverse sigmoid), set point 1.2 mmol/L, steep slope.
#    FHH (heterozygous inactivating CaSR mutation): set point +0.12 mmol/L; calcimimetic: set point -0.1.
# B: renal phosphate threshold model (see 7.14.23): excretion = GFR * max(P - C0, 0).
#    Steady state where excretion equals net intestinal absorption (30 mmol/day).
import matplotlib.pyplot as plt
import numpy as np

fig, (axa, axb) = plt.subplots(1, 2, figsize=(11.5, 4.4))

ca = np.linspace(0.8, 1.6, 400)


def pth(ca, setp=1.2, slope=25.0, lo=5.0, hi=100.0):
    return lo + (hi - lo) / (1.0 + (ca / setp) ** slope)


axa.axvspan(1.1, 1.3, color="0.88", lw=0)
axa.text(1.2, 103, "normal range", ha="center", fontsize=8, color="0.4")
axa.plot(ca, pth(ca), color="#2c6fbb", lw=2.2, label="normal (set point 1.2)")
axa.plot(ca, pth(ca, setp=1.32), color="#c0392b", lw=1.8, ls="--", label="FHH (inactivating CaSR)")
axa.plot(ca, pth(ca, setp=1.10), color="#2e8b57", lw=1.8, ls=":", label="calcimimetic")
axa.set_xlabel("Plasma ionized Ca$^{2+}$ / (mmol/L)")
axa.set_ylabel("PTH secretion / % of maximum")
axa.set_ylim(0, 110)
axa.set_title("A  Steep inverse sigmoid of the CaSR", loc="left", fontsize=11, fontweight="bold")
axa.legend(frameon=False, fontsize=8.5, loc="upper right", bbox_to_anchor=(1.0, 0.92))

P = np.linspace(0, 2.5, 500)
intake = 30.0
for gfr_ml, c0, col, lab in ((120, 1.0, "#2c6fbb", "C$_0$ = 1.0, GFR 120"),
                             (120, 0.7, "#2e8b57", "C$_0$ = 0.7 (PTH or FGF23 high)"),
                             (30, 0.7, "#c0392b", "C$_0$ = 0.7, GFR 30 (CKD)")):
    gfr = gfr_ml * 1.44  # L/day
    ex = gfr * np.maximum(P - c0, 0.0)
    axb.plot(P, ex, color=col, lw=2, label=lab)
    pss = c0 + intake / gfr
    axb.plot([pss], [intake], "o", color=col, ms=6)
    axb.annotate(f"{pss:.2f}", (pss, intake), xytext=(4, 6), textcoords="offset points", fontsize=8.5, color=col)
axb.axhline(intake, color="0.5", lw=0.9, ls="--")
axb.text(2.45, intake - 7, "net absorption 30 mmol/day", ha="right", fontsize=8.5, color="0.35")
axb.set_xlim(0, 2.5)
axb.set_ylim(0, 120)
axb.set_xlabel("Plasma phosphate / (mmol/L)")
axb.set_ylabel("Phosphate excretion / (mmol/day)")
axb.set_title("B  Renal threshold sets plasma phosphate", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8.5, loc="upper left", bbox_to_anchor=(0.0, 0.88))
fig.tight_layout()
