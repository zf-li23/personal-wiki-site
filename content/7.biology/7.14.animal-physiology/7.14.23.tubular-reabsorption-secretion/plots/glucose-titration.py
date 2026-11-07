# Renal glucose titration curve with splay (illustrative, human-like values).
# GFR = 125 mL/min; filtered load = GFR x plasma glucose. The kidney is a population of nephrons whose
# transport maximum per unit filtration (Tm_i / GFR_i) varies: log-normal with SD 0.25 (natural log) around a
# mean chosen so that the whole-kidney Tm is 375 mg/min. Each nephron reabsorbs min(load_i, Tm_i).
# Dashed: an ideal kidney in which all nephrons saturate together (no splay). Glucose appears in urine at
# the renal threshold (about 180-200 mg/dL, 10-11 mmol/L), well below the plasma level at which the whole
# kidney saturates (375 / 125 = 3 mg/mL = 300 mg/dL). 1 mmol/L glucose = 18 mg/dL.
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(0)
n = 4000
GFR, TM = 125.0, 375.0
gfr_i = rng.gamma(20, 1, n)
gfr_i *= GFR / gfr_i.sum()
ratio = np.exp(rng.normal(0, 0.25, n))
tm_i = gfr_i * ratio
tm_i *= TM / tm_i.sum()

P = np.linspace(0, 700, 400)                      # plasma glucose, mg/dL
load = GFR * P / 100                             # mg/min
reab = np.array([np.minimum(gfr_i * p / 100, tm_i).sum() for p in P])
excr = load - reab
ideal_reab = np.minimum(load, TM)

fig, ax = plt.subplots(figsize=(6.6, 4.4))
ax.plot(P, load, color="#7a7a7a", lw=2, label="Filtered")
ax.plot(P, reab, color="#3c9a5f", lw=2.2, label="Reabsorbed")
ax.plot(P, excr, color="#c0392b", lw=2.2, label="Excreted")
ax.plot(P, ideal_reab, color="#3c9a5f", lw=1, ls="--", label="Reabsorbed, no splay")
ax.plot(P, load - ideal_reab, color="#c0392b", lw=1, ls="--", label="Excreted, no splay")
ax.axhline(TM, color="#9e9e9e", lw=0.8, ls=":")
ax.text(690, TM + 12, "Tm = 375 mg/min", ha="right", fontsize=8.5)
thr = P[np.argmax(excr > 2)]
ax.axvline(thr, color="#9e9e9e", lw=0.8)
ax.text(thr + 5, 760, f"threshold\n~{thr:.0f} mg/dL", fontsize=8.5, va="top")
ax.axvspan(70, 110, color="#2f6fb5", alpha=0.12, lw=0)
ax.text(90, 30, "normal", ha="center", fontsize=8.5)
ax.set_xlim(0, 700)
ax.set_ylim(0, 800)
ax.set_xlabel("Plasma glucose (mg/dL)")
ax.set_ylabel("Glucose flux (mg/min)")
sec = ax.secondary_xaxis("top", functions=(lambda x: x / 18, lambda x: x * 18))
sec.set_xlabel("Plasma glucose (mmol/L)")
ax.legend(frameon=False, fontsize=8.5, loc="upper left")
ax.spines["right"].set_visible(False)
fig.tight_layout()
