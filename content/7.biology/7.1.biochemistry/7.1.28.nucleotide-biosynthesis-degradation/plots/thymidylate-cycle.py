"""The thymidylate cycle and its drugs. dUMP comes from dUDP or dCDP through dUTP (dUTPase keeps dUTP low)
or, in animals, from dCMP (dCMP deaminase). Thymidylate synthase (TS) transfers a one-carbon unit from
N5,N10-methylenetetrahydrofolate to C5 of dUMP and reduces it to a methyl group with a hydride taken from the
cofactor, which leaves as dihydrofolate (DHF). Dihydrofolate reductase (DHFR) regenerates tetrahydrofolate
(THF) with NADPH, and serine hydroxymethyltransferase (SHMT) reloads it with the beta carbon of serine.
Inhibitors: FdUMP (from 5-fluorouracil) and the antifolates raltitrexed and pemetrexed block TS;
methotrexate and aminopterin block DHFR, trimethoprim the bacterial DHFR selectively."""

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(19.0, 10.4)
neg = P.edge("negative")

pw = M.Pathway(ax, size="small")
pw.node("dudp", (1.8, 9.6), "dUDP")
pw.node("dctp", (1.8, 7.4), "dCTP (bacteria)")
pw.node("dutp", (5.6, 8.5), "dUTP")
pw.node("dcmp", (1.8, 5.2), "dCMP (animals)")
pw.node("dump", (5.6, 5.2), "dUMP", bold=True)
pw.node("dtmp", (12.4, 5.2), "dTMP", bold=True, token="highlight")
pw.node("dttp", (16.8, 5.2), "dTTP → DNA", size="tiny")
pw.step("dudp", "dutp", enzyme="NDP kinase", enzyme_flip=True)
pw.step("dctp", "dutp", enzyme="dCTP deaminase")
pw.step("dutp", "dump", enzyme="dUTPase", side=("H₂O", "PPᵢ"))
pw.step("dcmp", "dump", enzyme="dCMP\ndeaminase", side=(None, "NH₄⁺"), flip=True)
mid, _, _ = pw.step("dump", "dtmp", enzyme="thymidylate synthase (TS)", enzyme_flip=True)
pw.step("dtmp", "dttp", enzyme="kinases", side=("2 ATP", "2 ADP"), flip=True)

# folate cycle under TS
pw.node("mthf", (6.6, 2.6), "N⁵,N¹⁰-Methylene-THF")
pw.node("dhf", (11.6, 2.6), "DHF", bold=True)
pw.node("thf", (9.1, 0.6), "THF")
m1, _, _ = pw.step("mthf", "dhf")
bio.arrow(ax, (mid[0], mid[1] - 0.2), (mid[0], m1[1] + 0.25), kind="link", color=P.muted(), dashed=True)
bio.label(ax, (mid[0] + 0.25, 3.9), "C₁ unit + hydride\nto dUMP", size="tiny", color=P.muted(), ha="left")
m2, _, _ = pw.step("dhf", "thf", enzyme="DHFR", side=("NADPH + H⁺", "NADP⁺"))
pw.step("thf", "mthf", enzyme="SHMT", side=("Ser", "Gly"))


def drug(xy, text, start, target, w):
    bio.box(ax, xy, w, 0.7, token="drug", text=text, size="tiny")
    bio.arrow(ax, start, target, kind="inhibition", color=neg, lw=1.6)


drug((9.0, 7.6), "FdUMP (from 5-fluorouracil),\nraltitrexed, pemetrexed", (9.0, 7.25), (9.0, 5.75), 4.4)
drug((15.6, 1.2), "methotrexate, aminopterin\n(trimethoprim: bacterial DHFR)", (13.4, 1.2), (m2[0] + 0.9, m2[1] - 0.1), 4.4)
bio.box(ax, (12.4, 8.6), 3.4, 0.7, token="neutral", text="thymidine (salvage)", size="tiny")
pw_ = pw.step(None, None, enzyme="thymidine kinase", start=(12.4, 8.25), end=(12.4, 5.75))
