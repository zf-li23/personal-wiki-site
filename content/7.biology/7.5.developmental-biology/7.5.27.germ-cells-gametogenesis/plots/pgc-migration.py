"""Migration and expansion of mouse primordial germ cells. A: transverse section of the posterior trunk at about
E10.5 (dorsal up): PGCs (purple) leave the hindgut epithelium, move dorsally through the dorsal mesentery and
then laterally into the genital ridges on the ventromedial face of the mesonephros; SDF1 (CXCL12) from the
ridges and body wall attracts them through CXCR4, and Kit ligand (SCF) on the cells along the route keeps them
alive and motile. B: PGC number against embryonic day (log scale; approximate counts, after Tam and Snow
1981): about 40 at E7.25 to about 25 000 at E13.5, a doubling time of about 16 hours."""
import numpy as np
from matplotlib.patches import Circle, Ellipse
import wikibio as bio
from wikibio import quant

P = bio.P
G = "protein"
fig, ax = bio.canvas(22, 10)
bio.panel(ax, "A", (0.2, 9.8))
cx = 5.6
# neural tube, notochord, aorta
ax.add_patch(Ellipse((cx, 8.4), 1.6, 1.8, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=1, zorder=4))
ax.add_patch(Ellipse((cx, 8.4), 0.3, 1.0, facecolor=P.surface(), edgecolor=P.edge("protein"), lw=0.6, zorder=5))
ax.add_patch(Circle((cx, 7.1), 0.22, facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=0.8, zorder=4))
ax.add_patch(Circle((cx, 6.35), 0.42, facecolor=P.fill("blood"), edgecolor=P.edge("blood"), lw=0.8, zorder=4))
bio.label(ax, (cx, 6.35), "DA", size="tiny", color=P.on_fill())
# body wall outline and coelom
body = bio.blob((cx, 5.5), 4.6, 4.0, wobble=0.02, seed=3, k=12)
ax.plot(*body.T, color=P.edge("ectoderm"), lw=2.0, zorder=3)
coel = bio.blob((cx, 3.6), 3.4, 2.3, wobble=0.03, seed=5, k=10)
bio.shape(ax, coel, "vacuole", lw=0.8, zorder=2)
# mesonephros and genital ridges
for s in (-1, 1):
    ax.add_patch(Ellipse((cx + s * 1.9, 5.7), 1.6, 1.3, facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=0.8, zorder=4))
    ax.add_patch(Ellipse((cx + s * 1.25, 4.85), 0.75, 1.05, angle=-s * 25, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                         lw=0.8, zorder=5))
# dorsal mesentery and hindgut
ax.add_patch(Ellipse((cx, 5.0), 0.45, 1.9, facecolor=P.light("muscle"), edgecolor=P.edge("muscle"), lw=0.7, zorder=4))
ax.add_patch(Circle((cx, 3.55), 0.75, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.9, zorder=5))
ax.add_patch(Circle((cx, 3.55), 0.3, facecolor=P.surface(), edgecolor=P.edge("highlight"), lw=0.6, zorder=6))
pg = [(cx - 0.35, 3.9), (cx + 0.4, 3.85), (cx + 0.05, 4.45), (cx - 0.05, 5.1), (cx + 0.1, 5.6), (cx - 0.6, 5.3), (cx + 0.65, 5.2),
      (cx - 1.15, 4.95), (cx + 1.2, 4.9), (cx - 1.35, 4.6), (cx + 1.3, 4.6)]
for p in pg:
    ax.add_patch(Circle(p, 0.11, facecolor=P.fill(G), edgecolor=P.edge(G), lw=0.6, zorder=8))
bio.arrow(ax, (cx + 0.9, 3.6), (cx + 0.9, 5.0), kind="process", bend=-0.25)
bio.arrow(ax, (cx + 0.4, 5.85), (cx + 1.15, 5.45), kind="process")
bio.arrow(ax, (cx - 0.4, 5.85), (cx - 1.15, 5.45), kind="process")
bio.callout(ax, (cx, 3.2), (1.3, 1.6), "Hindgut")
bio.callout(ax, (cx, 4.95), (1.0, 3.0), "Dorsal mesentery")
bio.callout(ax, (cx + 1.35, 4.5), (10.3, 3.3), "Genital ridge")
bio.callout(ax, (cx + 2.3, 5.9), (10.3, 6.6), "Mesonephros")
bio.callout(ax, (cx, 8.9), (9.4, 9.4), "Neural tube")
bio.callout(ax, pg[2], (10.3, 2.0), "PGCs")

bio.panel(ax, "B", (12.0, 9.8))
d = np.array([7.25, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5])
n = np.array([40, 120, 350, 1000, 3000, 10000, 25000])
pl = quant.Plot(ax, (13.6, 1.8, 7.8, 7.0), xlim=(7, 14), ylim=(1, 5), xlabel="embryonic day", ylabel="log10 PGC number",
                xticks=[7, 9, 11, 13], yticks=[1, 2, 3, 4, 5])
k = np.polyfit(d, np.log10(n), 1)
xx = np.linspace(7, 14, 50)
pl.line(xx, np.polyval(k, xx), "muted", dashed=True)
pl.points(d, np.log10(n), "protein", r=0.11)
dt = np.log10(2) / k[0] * 24
bio.label(ax, (17.6, 8.6), f"doubling time about {dt:.0f} h", size="small")
