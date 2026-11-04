"""Three substrates, one terminal step: the pathways of methanogenesis (simplified).

Centre, hydrogenotrophic methanogenesis (CO2 + 4 H2): CO2 is bound to methanofuran (MFR) and reduced to
the formyl level with reduced ferredoxin (Fd); the formyl group moves to tetrahydromethanopterin (H4MPT) and is
reduced through methenyl- and methylene- to methyl-H4MPT with reduced coenzyme F420. The membrane-bound
methyl-H4MPT:coenzyme M methyltransferase (Mtr) transfers the methyl group to coenzyme M and pumps Na+.
Methyl-coenzyme M reductase (Mcr, nickel cofactor F430) reduces methyl-CoM with coenzyme B to CH4 and the
heterodisulfide CoM-S-S-CoB, which heterodisulfide reductase (Hdr) reduces again; in methanogens without
cytochromes this step is coupled by flavin-based electron bifurcation to the reduction of ferredoxin with H2.
Left, methylotrophic: methyltransferases pass the methyl group of methanol (or methylamines) to CoM.
Right, acetoclastic: acetate is activated to acetyl-CoA and split by CO dehydrogenase/acetyl-CoA synthase;
the methyl group goes via H4MPT (H4SPT in Methanosarcina) to CoM, the carbonyl is oxidized to CO2.
"""
import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(24.0, 17.0, scale=0.42)
pw = M.Pathway(ax, size="small")
x = 12.0
chain = [("co2", "CO₂", 16.0), ("cho_mfr", "Formyl-MFR", 14.3), ("cho_mpt", "Formyl-H₄MPT", 12.6),
         ("ch_mpt", "Methenyl-H₄MPT⁺", 10.9), ("ch2_mpt", "Methylene-H₄MPT", 9.2), ("ch3_mpt", "Methyl-H₄MPT", 7.5),
         ("ch3_com", "CH₃–S–CoM", 5.3), ("ch4", "CH₄", 2.9)]
for k, t, y in chain:
    pw.node(k, (x, y), t, token="highlight" if k in ("ch3_com", "ch4") else ("neutral" if k == "co2" else "metabolite"),
            bold=k in ("ch3_com", "ch4"))
pw.step("co2", "cho_mfr", side=("Fd(red)", "Fd(ox)"), enzyme="Fmd", side_reach=0.6)
pw.step("cho_mfr", "cho_mpt", side=(None, "MFR"))
pw.step("cho_mpt", "ch_mpt", side=(None, "H₂O"))
pw.step("ch_mpt", "ch2_mpt", side=("F₄₂₀H₂", "F₄₂₀"), enzyme="Mtd", side_reach=0.6)
pw.step("ch2_mpt", "ch3_mpt", side=("F₄₂₀H₂", "F₄₂₀"), enzyme="Mer", side_reach=0.6)
pw.step("ch3_mpt", "ch3_com", side=("HS–CoM", "H₄MPT"), enzyme="Mtr (Na⁺ out)", side_reach=0.6)
pw.step("ch3_com", "ch4", side=("HS–CoB", "CoM–S–S–CoB"), enzyme="Mcr (F₄₃₀)", side_reach=0.7)
bio.label(ax, (x, 17.0), "hydrogenotrophic: CO₂ + 4 H₂", size="small", bold=True, color=P.edge("dna"))

# heterodisulfide recycling
pw.node("hdr", (x + 5.6, 1.2), "CoM–S–S–CoB → HS–CoM + HS–CoB", token="neutral", size="tiny")
bio.arrow(ax, (x + 2.6, 2.6), (x + 3.4, 1.5), kind="process", color=P.muted())
bio.label(ax, (x + 5.6, 0.4), "Hdr: H₂ (bifurcation → Fd(red)) or membrane-bound, pumping H⁺", size="tiny", color=P.muted())

# methylotrophic branch
pw.node("meoh", (3.0, 9.2), "CH₃OH, methylamines", token="neutral")
pw.node("ch3_cor", (3.0, 6.8), "CH₃–corrinoid", token="metabolite")
pw.step("meoh", "ch3_cor", enzyme="MtaB")
pw.step("ch3_cor", "ch3_com", enzyme="MtaA", side=("HS–CoM", None), bend=-0.15, side_reach=0.5)
bio.label(ax, (3.0, 10.6), "methylotrophic", size="small", bold=True, color=P.edge("protein"))
bio.label(ax, (3.0, 4.2), "some methanol is oxidized\nback along the central\npathway for electrons", size="tiny", color=P.muted())

# acetoclastic branch
pw.node("ac", (20.6, 14.3), "Acetate", token="neutral")
pw.node("acoa", (20.6, 12.0), "Acetyl-CoA", token="metabolite")
pw.node("co", (22.4, 9.6), "[CO] → CO₂", token="neutral", size="tiny")
pw.step("ac", "acoa", side=("ATP", "ADP"), enzyme="activation", side_reach=0.5)
pw.step("acoa", "ch3_mpt", enzyme="CODH/ACS", bend=0.15)
pw.step("acoa", "co", bend=-0.1)
bio.label(ax, (20.6, 15.6), "acetoclastic", size="small", bold=True, color=P.edge("rna"))
bio.label(ax, (21.6, 8.6), "Fd(red) for the\nterminal step", size="tiny", color=P.muted())
