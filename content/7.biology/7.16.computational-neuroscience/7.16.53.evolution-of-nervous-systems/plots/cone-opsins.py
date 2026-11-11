"""Evolution of cone opsins and its consequence for color discrimination.

Absorbance spectra from the Govardovskii et al. (2000) A1 template (alpha and beta bands).
A: the four cone opsin classes of the ancestral vertebrate (SWS1, SWS2, RH2, LWS; peaks typical of
   fish and birds), retained by many fish, reptiles and birds.
B: primates. Most mammals kept only SWS1 (S) and LWS (L'); catarrhines (Old World monkeys, apes,
   humans) duplicated LWS into M (530 nm) and L (560 nm). New World monkeys have one X-linked L' gene
   with polymorphic alleles (dotted, 535/550/563 nm): heterozygous females are trichromatic.
C: wavelength discrimination threshold predicted by the receptor-noise-limited model
   (Vorobyev and Osorio 1998) with Weber fraction 0.05 in every cone class plus a photon-noise term k / q_i
   (k = 0.002) that grows where a cone absorbs little: the wavelength step that changes the
   log cone excitations by one just-noticeable difference.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
lam = np.linspace(330, 700, 1500)


def template(lmax, wl=lam):
    x = lmax / wl
    a = 0.8795 + 0.0459 * np.exp(-((lmax - 300) ** 2) / 11940)
    alpha = 1 / (np.exp(69.7 * (a - x)) + np.exp(28 * (0.922 - x)) + np.exp(-14.9 * (1.104 - x)) + 0.674)
    lb = 189 + 0.315 * lmax
    bb = -40.5 + 0.195 * lmax
    beta = 0.26 * np.exp(-(((wl - lb) / bb) ** 2))
    return alpha + beta


def threshold(peaks, omega=0.05, k=0.002):
    """Delta-lambda (nm) for one JND in the receptor-noise-limited model.

    Noise of cone class i: omega_i^2 = omega^2 + k / q_i (a Weber term plus a photon-noise term that
    grows where the cone absorbs little), q_i the normalized absorbance at the test wavelength.
    """
    q = np.array([template(p) for p in peaks])
    f = np.gradient(np.log(q), lam, axis=1)  # d ln q_i / d lambda
    w2 = omega ** 2 + k / q
    if len(peaks) == 2:
        s2 = (f[0] - f[1]) ** 2 / (w2[0] + w2[1])
    else:
        num = w2[0] * (f[2] - f[1]) ** 2 + w2[1] * (f[2] - f[0]) ** 2 + w2[2] * (f[0] - f[1]) ** 2
        s2 = num / (w2[0] * w2[1] + w2[0] * w2[2] + w2[1] * w2[2])
    return 1 / np.sqrt(s2)


fig, axs = plt.subplots(1, 3, figsize=(13.5, 3.9))
ax = axs[0]
for lm, name, tok in ((370, "SWS1 (UV)", "highlight"), (440, "SWS2", "dna"), (505, "RH2", "positive"), (565, "LWS", "negative")):
    ax.plot(lam, template(lm), color=P.edge(tok), lw=1.8, label=f"{name}, {lm} nm")
ax.plot(lam, template(500), color=P.muted(), lw=1.0, ls="--", label="rod opsin RH1, 500 nm")
ax.set_title("A  Ancestral vertebrate: four cone classes", loc="left", fontsize=10)

ax = axs[1]
for lm, name, tok in ((420, "S", "dna"), (530, "M", "positive"), (560, "L", "negative")):
    ax.plot(lam, template(lm), color=P.edge(tok), lw=1.8, label=f"catarrhine {name}, {lm} nm")
for lm in (535, 550, 563):
    ax.plot(lam, template(lm), color=P.edge("protein"), lw=0.9, ls=":")
ax.plot([], [], color=P.edge("protein"), lw=0.9, ls=":", label="New World L' alleles")
ax.set_title("B  Primates: duplication of LWS", loc="left", fontsize=10)
for a in axs[:2]:
    a.set_xlabel("Wavelength / nm")
    a.set_ylabel("Normalized absorbance")
    a.set_xlim(330, 700)
    a.set_ylim(0, 1.42)
    a.legend(frameon=False, fontsize=7, loc="upper center", ncol=2)
    a.grid(True, alpha=0.3)

ax = axs[2]
cases = [("dichromat S + L' (430, 555)", (430, 555), "neutral", "-"),
         ("trichromat S, M, L (420, 530, 560)", (420, 530, 560), "negative", "-"),
         ("wild-type mouse (360, 510)", (360, 510), "dna", "--"),
         ("knock-in mouse + human L (556)", (360, 510, 556), "positive", "--")]
for name, peaks, tok, ls in cases:
    ax.plot(lam, threshold(peaks), color=P.edge(tok), lw=1.7, ls=ls, label=name)
ax.set_yscale("log")
ax.set_ylim(0.5, 200)
ax.set_xlim(440, 670)
ax.set_xlabel("Wavelength / nm")
ax.set_ylabel(r"Discrimination threshold $\Delta\lambda$ / nm")
ax.set_title("C  Predicted wavelength discrimination", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=7, loc="upper left")
ax.grid(True, alpha=0.3, which="both")
fig.tight_layout()
