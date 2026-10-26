# DNA methylation and its measurement.
# A: bisulfite conversion (schematic): reference sequence with two CpGs, one methylated (5mC, marked m) and one not;
# sodium bisulfite deaminates unmethylated C to U, 5mC is unchanged; after PCR U is read as T. Comparing the read
# with the reference: a C at a CpG means methylated, a T means unmethylated.
# B: site-independent copying, Eq. (15.2): m_{t+1} = mu m_t + delta (1 - mu m_t), started from m0 = 1 and m0 = 0,
# for (mu, delta) = (0.97, 0.03) and (0.995, 0.005); both starting states converge on m* = delta / (1 - mu (1 - delta)).
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(22.0, 8.6)
bio.panel(ax, "A", (0.1, 8.5))
bio.label(ax, (0.6, 8.15), "Bisulfite conversion", size="normal", bold=True, ha="left")

ref = "ATCGTTACGATC"
meth = {2}           # index of the methylated C (in the first CpG)
rows = [("reference", ref, None),
        ("after bisulfite", "".join("U" if (b == "C" and i not in meth) else b for i, b in enumerate(ref)), "U"),
        ("after PCR (read)", "".join("T" if (b == "C" and i not in meth) else b for i, b in enumerate(ref)), "T")]
dx = 0.62
for r, (name, seq, conv) in enumerate(rows):
    y = 6.6 - 1.75 * r
    bio.label(ax, (3.3, y), name, size="small", ha="right")
    for i, b in enumerate(seq):
        x = 3.9 + i * dx
        cpg = (ref[i] == "C" and i + 1 < len(ref) and ref[i + 1] == "G")
        if cpg:
            bio.box(ax, (x, y), 0.5, 0.56, "highlight" if i in meth else "neutral", None, radius=0.08, zorder=5)
        changed = conv is not None and b != ref[i]
        bio.label(ax, (x, y), b, size="normal", bold=changed or (i in meth),
                  color=P.edge("negative") if changed else P.ink(), zorder=8)
        if i in meth and r < 2:
            bio.label(ax, (x + 0.2, y + 0.33), "m", size="tiny", color=P.edge("positive"), zorder=9)
    if r < 2:
        bio.arrow(ax, (3.9 + 5.5 * dx, y - 0.4), (3.9 + 5.5 * dx, y - 1.3), kind="process")
bio.label(ax, (3.9 + 2 * dx, 1.15), "5mC: stays C\n(methylated)", size="tiny", color=P.edge("positive"))
bio.label(ax, (3.9 + 7 * dx, 1.15), "C: read as T\n(unmethylated)", size="tiny", color=P.edge("negative"))

# ---- B
bio.panel(ax, "B", (12.0, 8.5))
bio.label(ax, (12.5, 8.15), "Site-independent copying forgets", size="normal", bold=True, ha="left")
b = C.axes_at(ax, (13.4, 1.3, 8.0, 5.9))
t = np.arange(0, 201)
for (mu, de), tok in [((0.97, 0.03), "drug"), ((0.995, 0.005), "chromatin")]:
    mstar = de / (1 - mu * (1 - de))
    for m0, ls in [(1.0, "-"), (0.0, (0, (4, 2)))]:
        m = np.empty(t.size)
        m[0] = m0
        for k in range(1, t.size):
            m[k] = mu * m[k - 1] + de * (1 - mu * m[k - 1])
        b.plot(t, m, color=C.line(tok), lw=1.8, ls=ls,
               label=(f"μ = {mu}, δ = {de}: m* = {mstar:.2f}" if m0 == 1.0 else None))
    b.axhline(mstar, color=C.line(tok), lw=0.6, ls=(0, (1, 2)))
b.set_xlim(0, 200)
b.set_ylim(-0.02, 1.02)
C.style_axes(b, "cell divisions $t$", "methylation level $m_t$")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
b.text(195, 0.06, "solid: start methylated\ndashed: start unmethylated", ha="right", fontsize=bio.core.FONT["tiny"],
       color=P.muted())
