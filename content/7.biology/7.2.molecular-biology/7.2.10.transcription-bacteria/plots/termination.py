# Bacterial transcription termination.
# A: an intrinsic terminator (an illustrative designed sequence, not a particular natural one): a GC-rich stem
# of 7 bp closed by a UUCG loop, followed by a tract of eight U, which at the termination point pairs with dA of
# the template strand in the RNA-DNA hybrid (weak rU-dA pairs) inside the paused polymerase.
# B: rho-dependent termination: the hexameric rho ring loads on a C-rich, unstructured rut site of the nascent
# RNA and translocates 5'->3' with ATP hydrolysis towards a paused polymerase.
# C: kinetic competition at a pause site, T = k_t / (k_t + k_e), against the elongation rate constant k_e for a
# strong terminator (k_t = 2 /s) and a weak one (k_t = 0.2 /s).
import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import molbio as MB

P = bio.P
fig, ax = bio.canvas(22.0, 9.6)

# --- A: intrinsic terminator --------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 9.45))
bio.label(ax, (4.2, 9.2), "Intrinsic terminator", size="normal", bold=True)
dx = 0.34
y0 = 2.6
stem5, loop, stem3 = "GCCCGCC", "UUCG", "GGCGGGC"
xa, xb = 2.4, 2.4 + 0.62  # the two stem columns
# upstream single-stranded RNA leading into the stem
lead = "AAUCA"
for i, ch in enumerate(lead):
    x = 0.55 + i * dx
    bio.label(ax, (x, y0), ch, size="tiny", color=P.edge("rna"))
ax.plot([0.4, xa - 0.05], [y0 - 0.22, y0 - 0.22], color=P.edge("rna"), lw=1.6)
# stem: 5' side goes up the left column, 3' side comes down the right column
for i, (c5, c3) in enumerate(zip(stem5, reversed(stem3))):
    yy = y0 + 0.45 + i * 0.5
    bio.label(ax, (xa, yy), c5, size="tiny", bold=True, color=P.edge("rna"))
    bio.label(ax, (xb, yy), c3, size="tiny", bold=True, color=P.edge("rna"))
    ax.plot([xa + 0.15, xb - 0.15], [yy, yy], color=P.muted(), lw=1.0)
ytop = y0 + 0.45 + 6 * 0.5
ax.plot([xa - 0.18, xa - 0.18], [y0 - 0.22, ytop], color=P.edge("rna"), lw=1.6)
ax.plot([xb + 0.18, xb + 0.18], [ytop, y0 - 0.22], color=P.edge("rna"), lw=1.6)
th = np.linspace(np.pi, 0, 60)
cxl, rl = (xa + xb) / 2, (xb - xa) / 2 + 0.18
ax.plot(cxl + rl * np.cos(th), ytop + 0.05 + 0.55 * np.sin(th), color=P.edge("rna"), lw=1.6)
for k, ch in enumerate(loop):
    ang = np.pi - (k + 0.5) / 4 * np.pi
    bio.label(ax, (cxl + (rl + 0.25) * np.cos(ang), ytop + 0.1 + 0.8 * np.sin(ang)), ch, size="tiny", color=P.edge("rna"))
bio.callout(ax, (xa - 0.25, y0 + 1.8), (0.9, y0 + 3.6), "GC-rich stem")
# U tract paired with template dA in the hybrid
utr = "UUUUUUUU"
x0 = xb + 0.55
ax.plot([xb + 0.18, x0 + 8 * dx], [y0 - 0.22, y0 - 0.22], color=P.edge("rna"), lw=1.6)
for i, ch in enumerate(utr):
    x = x0 + i * dx
    bio.label(ax, (x, y0), ch, size="tiny", bold=True, color=P.edge("rna"))
    ax.plot([x, x], [y0 - 0.32, y0 - 0.62], color=P.muted(), lw=0.8, ls=(0, (1.5, 1.2)))
    bio.label(ax, (x, y0 - 0.86), "A", size="tiny", color=P.edge("dna2"))
bio.label(ax, (x0 + 8 * dx + 0.1, y0 + 0.02), "3′", size="tiny", bold=True, ha="left")
ax.plot([0.4, 7.8], [y0 - 1.1, y0 - 1.1], color=P.edge("dna2"), lw=1.8)
ax.plot([0.4, 7.8], [y0 - 1.55, y0 - 1.55], color=P.edge("dna"), lw=1.8)
bio.label(ax, (0.3, y0 - 1.1), "template", size="tiny", ha="right", color=P.edge("dna2"))
pol = bio.core.blob((x0 + 4 * dx, y0 - 0.55), 1.7, 1.35, wobble=0.05, seed=11, k=9)
bio.shape(ax, pol, token="enzyme", zorder=1, alpha=0.45)
bio.label(ax, (x0 + 4 * dx, y0 - 2.2), "paused RNAP", size="small", color=P.ink())
bio.label(ax, (x0 + 4 * dx, y0 + 0.55), "rU–dA hybrid (weak)", size="tiny", color=P.ink())
bio.label(ax, (0.55, y0 + 0.4), "5′", size="tiny", bold=True)

# --- B: rho -----------------------------------------------------------------------------------------------
bio.panel(ax, "B", (8.4, 9.45))
bio.label(ax, (11.6, 9.2), "ρ-dependent termination", size="normal", bold=True)
yb = 5.2
rna = np.c_[np.linspace(8.7, 13.8, 200), yb + 0.18 * np.sin(np.linspace(0, 9 * np.pi, 200))]
MB.backbone(ax, rna, "rna", lw=2.0)
bio.label(ax, (8.6, yb + 0.4), "5′", size="tiny", bold=True)
# rut site: a stretch of the RNA itself
seg = (rna[:, 0] >= 9.2) & (rna[:, 0] <= 10.7)
ax.plot(rna[seg, 0], rna[seg, 1], color=P.edge("highlight"), lw=4.0, alpha=0.6, zorder=9, solid_capstyle="round")
bio.label(ax, (9.95, yb + 0.6), "rut (C-rich)", size="tiny")
# rho hexamer ring threaded on the RNA
cxr = 11.6
for k in range(6):
    ang = 2 * np.pi * k / 6
    bio.molecule(ax, (cxr + 0.42 * np.cos(ang), yb + 0.42 * np.sin(ang)), token="protein", r=0.24)
bio.label(ax, (cxr, yb - 1.0), "ρ hexamer", size="small")
bio.arrow(ax, (cxr + 0.7, yb + 0.85), (13.3, yb + 0.85), kind="process")
bio.label(ax, (12.5, yb + 1.15), "5′→3′, ATP", size="tiny", color=P.muted())
pol2 = bio.core.blob((14.6, yb - 0.75), 1.05, 1.3, wobble=0.05, seed=12, k=9)
bio.shape(ax, pol2, token="enzyme", zorder=1, alpha=0.6)
bio.label(ax, (14.6, yb - 2.4), "paused RNAP", size="small")
ax.plot([8.7, 16.2], [yb - 1.5, yb - 1.5], color=P.edge("dna2"), lw=1.8, zorder=0.5)
ax.plot([8.7, 16.2], [yb - 1.9, yb - 1.9], color=P.edge("dna"), lw=1.8, zorder=0.5)
bio.label(ax, (12.4, 2.2), "no ribosome on the RNA: rut is exposed", size="tiny", color=P.muted())

# --- C: kinetic competition ---------------------------------------------------------------------------------
bio.panel(ax, "C", (16.6, 9.45))
c = C.axes_at(ax, (18.0, 1.3, 3.6, 6.9))
ke = np.logspace(-1, 2, 300)
for kt, tok, name in [(2.0, "negative", r"strong: $k_{\mathrm{t}}$ = 2 s$^{-1}$"), (0.2, "enzyme", r"weak: $k_{\mathrm{t}}$ = 0.2 s$^{-1}$")]:
    c.semilogx(ke, kt / (kt + ke), color=C.line(tok), lw=1.8, label=name)
c.set_xlim(0.1, 100)
c.set_ylim(0, 1.02)
C.style_axes(c, r"$k_{\mathrm{e}}$ / s$^{-1}$", "termination efficiency T")
c.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
