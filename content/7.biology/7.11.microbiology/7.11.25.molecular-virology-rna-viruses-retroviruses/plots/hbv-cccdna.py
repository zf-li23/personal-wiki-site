# The hepatitis B virus replication cycle inside one hepatocyte.
# The entering gapped genome is repaired in the nucleus into covalently closed circular DNA, a chromatinized
# minichromosome; host RNA polymerase II makes the pregenomic RNA; the P protein binds the epsilon stem-loop
# of its own transcript, is packaged with it, and primes (-) strand DNA on a tyrosine of its terminal-protein
# domain; the capped 5' fragment left by RNase H primes the (+) strand, which stays incomplete. Cores are
# either enveloped and secreted or returned to the nucleus to build up the cccDNA pool.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(16.0, 10.2)


def ring(center, r, tok, lw=2.0, t0=0.0, t1=2 * np.pi, dash=False):
    t = np.linspace(t0, t1, 300)
    ax.plot(center[0] + r * np.cos(t), center[1] + r * np.sin(t), color=P.edge(tok), lw=lw,
            ls="--" if dash else "-", solid_capstyle="round", zorder=8)


bio.cell(ax, (8.0, 5.8), 7.3, 4.0, kind="animal")
bio.label(ax, (2.2, 2.4), "Hepatocyte", size="small", color=P.muted(), ha="left")
bio.nucleus(ax, (4.8, 6.9), 2.9)
bio.label(ax, (4.8, 9.3), "Nucleus", size="small", color=P.muted())

# entering genome -> cccDNA
bio.virus(ax, (1.3, 8.8), 0.45, kind="enveloped", spikes=9)
bio.label(ax, (1.3, 9.5), "virion", size="tiny", bold=True)
bio.arrow(ax, (1.9, 8.6), (3.0, 8.2), kind="process")
ring((3.6, 7.9), 0.52, "dna")
ring((3.6, 7.9), 0.40, "dna2", t0=-0.3 * np.pi, t1=0.8 * np.pi)
bio.label(ax, (3.6, 8.7), "gapped DNA", size="tiny")
bio.arrow(ax, (4.2, 7.6), (5.0, 7.1), kind="process")
bio.label(ax, (4.9, 7.65), "repair", size="tiny", color=P.muted())
ring((5.6, 6.4), 0.68, "dna")
for k in range(7):
    a = 2 * np.pi * k / 7
    bio.protein(ax, (5.6 + 0.68 * np.cos(a), 6.4 + 0.68 * np.sin(a)), 0.22, 0.22, "chromatin", zorder=10)
bio.label(ax, (5.3, 5.25), "cccDNA minichromosome", size="tiny", bold=True)

# transcription
bio.arrow(ax, (7.6, 6.5), (9.2, 6.5), kind="process")
bio.label(ax, (8.4, 6.15), "host RNA polymerase II", size="tiny", color=P.muted())
ax.plot([9.3, 12.4], [6.5, 6.5], color=P.edge("rna"), lw=2.2, solid_capstyle="round", zorder=8)
bio.molecule(ax, (9.2, 6.5), token="metabolite", r=0.14)
bio.label(ax, (12.6, 6.5), "AAAA", size="tiny", bold=True, ha="left")
bio.label(ax, (11.3, 7.55), "pregenomic RNA (3.5 kb), also the mRNA for C and P", size="tiny", color=P.muted())
ax.plot([9.9, 9.9], [6.6, 7.1], color=P.edge("highlight"), lw=2.0, zorder=10)
bio.label(ax, (9.9, 7.35), "ε", size="small", color=P.edge("highlight"))

# packaging and reverse transcription
bio.arrow(ax, (11.0, 6.1), (11.0, 5.1), kind="process")
bio.label(ax, (11.25, 5.6), "P binds ε on its own transcript\nand is packaged with it", size="tiny",
          color=P.muted(), ha="left")
t = np.linspace(0, 2 * np.pi, 7, endpoint=False)
core = np.c_[11.0 + 1.25 * np.cos(t), 3.7 + 1.25 * np.sin(t)]
bio.shape(ax, core, "virus", alpha=0.35)
bio.label(ax, (11.0, 2.75), "core particle", size="tiny", bold=True)
ax.plot([10.2, 11.8], [4.0, 4.0], color=P.edge("rna"), lw=2.0, zorder=11)
ax.plot([10.3, 11.4], [3.6, 3.6], color=P.edge("negative"), lw=2.2, zorder=11)
bio.protein(ax, (10.2, 3.6), 0.34, 0.3, "enzyme", zorder=12)

# fates
bio.arrow(ax, (9.7, 3.7), (7.2, 5.6), kind="process", bend=0.2, dashed=True)
bio.label(ax, (7.9, 4.05), "recycling: more cccDNA\n(up to ~30 copies per nucleus)", size="tiny", color=P.muted())
bio.arrow(ax, (12.3, 3.7), (14.3, 3.7), kind="process")
bio.label(ax, (13.3, 4.05), "envelopment\nin the ER", size="tiny", color=P.muted())
bio.virus(ax, (14.9, 3.7), 0.42, kind="enveloped", spikes=9)
bio.label(ax, (14.9, 2.9), "secreted\nvirion", size="tiny", bold=True)

bio.label(ax, (8.0, 0.65), "Nucleoside analogues block the step inside the core; they do not touch the cccDNA,\nwhich is why treatment suppresses but rarely cures the infection",
          size="small", color=P.muted())
