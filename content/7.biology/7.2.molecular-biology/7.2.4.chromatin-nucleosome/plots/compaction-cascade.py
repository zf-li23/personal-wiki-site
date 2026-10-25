# Compaction of human chromosome 22 (48 Mbp in the course's round number). A: contour length at each level of
# packing on a log scale: B-DNA (0.34 nm per bp) 1.6 cm; a compact nucleosome array (one 200 bp repeat per
# 11 nm) 2.6 mm; the in vitro 30 nm fibre (six nucleosomes per 11 nm, hollow bar: not a regular structure in
# most interphase nuclei) 0.44 mm; the metaphase chromatid about 2 um. Fold compaction relative to B-DNA is
# written beside each bar. B: the diploid genome (6.2e9 bp) as B-DNA (a 2 nm cylinder) occupies only about
# 6 % of a 6 um nucleus, so packing is a problem of organisation and access rather than of space.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(19.0, 7.6)

bp = 48e6
levels = [
    ("B-DNA (2 nm)", bp * 0.34e-9, "dna", False),
    ("nucleosome array (10 nm)", bp / 200 * 11e-9, "chromatin", False),
    ("30 nm fibre (in vitro)", bp / 1200 * 11e-9, "chromatin", True),
    ("metaphase chromatid", 2e-6, "protein", False),
]
a = C.axes_at(ax, (5.2, 1.3, 7.4, 5.2))
y = np.arange(len(levels))[::-1]
for yi, (name, L, tok, hollow) in zip(y, levels):
    if hollow:
        a.barh(yi, L, height=0.55, left=1e-7, color="none", edgecolor=C.line(tok), lw=1.4, ls=(0, (4, 2)))
    else:
        a.barh(yi, L, height=0.55, left=1e-7, color=P.fill(tok), edgecolor=C.line(tok), lw=1.0)
    fold = bp * 0.34e-9 / L
    txt = f"{L * 1e2:.2g} cm" if L > 1e-2 else f"{L * 1e3:.2g} mm" if L > 1e-4 else f"{L * 1e6:.2g} µm"
    a.text(L * 1.25, yi, f"{txt}   ({fold:,.0f}×)", va="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.set_xscale("log")
a.set_xlim(1e-7, 2e-1)
a.set_yticks(y, [lv[0] for lv in levels])
a.set_xticks([1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1], ["1 µm", "10 µm", "0.1 mm", "1 mm", "1 cm", "10 cm"])
C.style_axes(a, "contour length of chromosome 22")
a.tick_params(axis="y", length=0)
bio.panel(ax, "A", (0.1, 7.5))
bio.label(ax, (0.6, 7.15), "Packing chromosome 22 (48 Mbp)", size="normal", bold=True, ha="left")

# B: volume fraction
G = 6.2e9
v_dna = G * np.pi * (1e-9) ** 2 * 0.34e-9  # m^3
v_nuc = 4 / 3 * np.pi * (3e-6) ** 3
frac = v_dna / v_nuc
cx, cy, R = 16.0, 3.7, 2.3
bio.shape(ax, bio.core.smooth_closed(np.c_[cx + R * np.cos(np.linspace(0, 2 * np.pi, 13)[:-1]),
                                           cy + R * np.sin(np.linspace(0, 2 * np.pi, 13)[:-1])], 200), "nucleus", lw=1.2)
r_dna = R * frac ** (1 / 3)
bio.shape(ax, bio.core.smooth_closed(np.c_[cx + r_dna * np.cos(np.linspace(0, 2 * np.pi, 13)[:-1]),
                                           cy + r_dna * np.sin(np.linspace(0, 2 * np.pi, 13)[:-1])], 200), "dna", lw=1.0, zorder=7)
bio.panel(ax, "B", (13.4, 7.5))
bio.label(ax, (13.9, 7.15), "How full is the nucleus?", size="normal", bold=True, ha="left")
bio.label(ax, (cx, cy - 0.05), f"DNA {frac * 100:.0f}%", size="small", color=P.on_fill())
bio.label(ax, (cx, cy + 1.55), f"nucleus Ø 6 µm: {v_nuc * 1e18:.0f} µm³", size="small")
bio.label(ax, (cx, 0.9), f"6.2×10⁹ bp of B-DNA: {v_dna * 1e18:.1f} µm³", size="small")
bio.label(ax, (cx, 0.5), "(contour length ≈ 2.1 m)", size="tiny", color=P.muted())
