# Per-position quality of simulated Illumina-style 2 x 150 reads, drawn as in the FastQC module "per base sequence
# quality": a box (quartiles), whiskers (10th-90th percentiles) and the mean at each cycle. Read 1 (A) has high
# quality that declines slowly towards the 3' end as phasing accumulates; read 2 (B) is lower throughout. The
# background bands mark the FastQC zones (good above Q28, reasonable Q20-28, poor below Q20). Quality is simulated
# per read: a read-level offset plus a decline with cycle and occasional low-quality bursts, capped at Q41.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
L, n = 150, 4000
cyc = np.arange(1, L + 1)


def simulate(base, slope, burst):
    off = rng.normal(0, 1.5, (n, 1))
    trend = base - slope * (cyc / L) ** 2.2
    q = trend + off + rng.normal(0, 2.0, (n, L))
    bad = rng.random((n, L)) < burst * (cyc / L) ** 2
    q[bad] -= rng.uniform(10, 30, bad.sum())
    q[:, :3] -= 2.5
    return np.clip(np.round(q), 2, 41)


fig, ax = bio.canvas(24.0, 8.4)
for k, (q, title, x0) in enumerate([(simulate(37.5, 6.0, 0.06), "read 1", 1.6),
                                     (simulate(36.0, 11.0, 0.12), "read 2", 13.4)]):
    a = C.axes_at(ax, (x0, 1.3, 10.0, 6.0))
    a.axhspan(28, 42, color=P.light("positive"), lw=0, zorder=0)
    a.axhspan(20, 28, color=P.light("highlight"), lw=0, zorder=0)
    a.axhspan(0, 20, color=P.light("negative"), lw=0, zorder=0)
    sel = cyc[::5] - 1
    stats = np.percentile(q[:, sel], [10, 25, 50, 75, 90], axis=0)
    for j, c in enumerate(sel):
        x = c + 1
        a.plot([x, x], [stats[0, j], stats[4, j]], color=P.ink(), lw=0.6, zorder=2)
        a.add_patch(__import__("matplotlib").patches.Rectangle((x - 1.6, stats[1, j]), 3.2, stats[3, j] - stats[1, j],
                    facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.5, zorder=3))
        a.plot([x - 1.6, x + 1.6], [stats[2, j]] * 2, color=P.edge("negative"), lw=0.8, zorder=4)
    a.plot(cyc, q.mean(0), color=C.line("protein"), lw=1.4, zorder=5, label="mean")
    a.set_xlim(0, 152)
    a.set_ylim(0, 42)
    C.style_axes(a, "position in read (cycle)", "Phred quality Q")
    bio.panel(ax, "AB"[k], (x0 - 1.4, 8.2))
    bio.label(ax, (x0 + 0.1, 7.75), title, size="normal", bold=True, ha="left")
    a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="lower left")
