"""The p53 hub of the DNA damage response (SBGN activity flow; open arrows activate, bars inhibit).

DNA breaks (including uncapped telomeres) activate ATM and Chk2; stalled replication forks and single-stranded
DNA activate ATR and Chk1. The checkpoint kinases inhibit or destroy Cdc25A and Cdc25C (rapid arrest, because
Cdk2 and Cdk1 stay phosphorylated on Tyr15) and stabilize p53 by phosphorylation. Oncogenic signals (excess Ras,
Myc or E2F) induce ARF, and ribosomal proteins freed by nucleolar stress (RPL5, RPL11) bind Mdm2; both inhibit
Mdm2, the ubiquitin ligase that destroys p53. p53 induces Mdm2 (negative feedback), the Cdk inhibitor p21
(sustained arrest in G1 and G2), repair genes and the pro-apoptotic Puma and Noxa; the outcomes are transient
arrest with repair, senescence or apoptosis.
"""

import wikibio as bio
from wikibio import network

P = bio.P

fig, ax = bio.canvas(14.0, 12.8, scale=0.45)
d2 = network.Diagram(ax, size="small")
d2.compartment("c2", (0.5, 0.4, 13.4, 12.2), "the p53 hub", token="nucleus")
d2.activity("dsb", (2.4, 11.0), "DNA breaks,\nshort telomeres", token="neutral", w=2.8, h=1.2)
d2.activity("fork", (6.2, 11.0), "stalled forks", token="neutral", w=2.4)
d2.activity("onc", (10.2, 11.0), "oncogenic Ras,\nMyc, E2F", token="neutral", w=2.8, h=1.2)
d2.activity("atm", (2.4, 8.8), "ATM–Chk2", token="enzyme", w=2.4)
d2.activity("atr", (6.2, 8.8), "ATR–Chk1", token="enzyme", w=2.4)
d2.activity("arf", (10.2, 8.8), "ARF", token="drug", w=1.6)
d2.activity("cdc25", (2.4, 6.2), "Cdc25A, Cdc25C", token="enzyme", w=2.8)
d2.activity("p53", (6.6, 5.6), "p53", token="negative", w=1.8)
d2.activity("mdm2", (10.2, 6.6), "Mdm2", token="receptor", w=1.8)
d2.activity("rpl", (12.2, 4.6), "RPL5, RPL11\n(nucleolar\nstress)", token="neutral", w=2.0, h=1.6)
d2.activity("p21", (3.4, 3.6), "p21", token="drug", w=1.6)
d2.activity("cdk", (2.4, 1.5), "Cdk2, Cdk1", token="protein", w=2.4)
d2.phenotype("arrest", (6.6, 1.5), "arrest, repair\nor senescence", token="highlight", w=3.2, h=1.2)
d2.phenotype("apo", (10.4, 1.5), "apoptosis\n(Puma, Noxa)", token="negative", w=3.0, h=1.2)
d2.connect("dsb", "atm", "positive")
d2.connect("fork", "atr", "positive")
d2.connect("onc", "arf", "positive")
d2.connect("atm", "cdc25", "negative")
d2.connect("atr", "cdc25", "negative", start=(5.4, 8.35), end=(3.4, 6.65))
d2.connect("atm", "p53", "positive", start=(3.2, 8.35), end=(6.2, 6.05))
d2.connect("atr", "p53", "positive")
d2.connect("arf", "mdm2", "negative")
d2.connect("rpl", "mdm2", "negative")
d2.connect("mdm2", "p53", "negative", start=(9.3, 6.45), end=(7.5, 5.85))
d2.connect("p53", "mdm2", "positive", start=(7.5, 5.35), end=(9.3, 6.25))
d2.connect("p53", "p21", "positive")
d2.connect("p21", "cdk", "negative")
d2.connect("cdc25", "cdk", "positive", via=[(1.0, 6.2), (1.0, 1.5)], start=(1.0, 6.2), end=(1.2, 1.5))
d2.connect("p53", "arrest", "positive")
d2.connect("p53", "apo", "positive", start=(7.2, 5.15), end=(9.8, 2.1))
