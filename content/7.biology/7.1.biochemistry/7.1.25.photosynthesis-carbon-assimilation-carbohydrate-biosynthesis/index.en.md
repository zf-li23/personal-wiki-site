---
title: "Photosynthesis II: Carbon Assimilation and Carbohydrate Biosynthesis in Plants"
description: The Calvin cycle and its stoichiometry; rubisco, its mechanism and activation; regeneration of ribulose 1,5-bisphosphate and carbon bookkeeping; the Pi–triose phosphate translocator; light regulation by pH, Mg²⁺ and the ferredoxin–thioredoxin system; photorespiration, the specificity factor and the CO₂ compensation point; C4 photosynthesis, CAM and carboxysomes; synthesis of starch, sucrose and cellulose and their regulation; the pathway cards.
---

The light reactions of **photosynthesis** ([7.1.24](/7.1.24)) leave the chloroplast stroma supplied with ATP and **NADPH**. This chapter follows how plants spend them to turn $\ce{CO2}$ into sugar, and then into the three carbohydrates that dominate the biosphere: **starch**, sucrose and **cellulose**. The central pathway, the Calvin cycle, is built almost entirely from reactions already met in **glycolysis**, **gluconeogenesis** and the **pentose phosphate pathway** ([7.1.18](/7.1.18), [7.1.19](/7.1.19)); only three of its thirteen **enzymes** are unique to photosynthetic organisms, and one of them, rubisco, is the reason for most of what makes plant carbon **metabolism** distinctive. Rubisco is slow and cannot exclude $\ce{O2}$ from its **active site**. The oxygenase reaction forces plants to run a costly **salvage pathway**, photorespiration, whose cost grows with temperature; the C4 and CAM pathways are evolutionary answers that concentrate $\ce{CO2}$ around rubisco at the price of extra ATP. Regulation follows the logic of Part II ([7.1.17](/7.1.17)): the cycle is switched on by light through the redox state of the stroma, and the triose phosphate it makes is divided between starch in the chloroplast and sucrose in the cytosol by **reciprocal regulation** with **fructose 2,6-bisphosphate**, as in the liver ([7.1.19](/7.1.19#sec-19.2.3)). The physiology of **photosynthesis** in leaves (gas exchange, the Farquhar model of the response to $\ce{CO2}$ and light, the ecology of C4 and CAM plants and their leaf anatomy) is treated in [7.13](/7.13); here we stay with enzymes and pathways.

## 25.1. The Calvin Cycle

### 25.1.1. Tracing the Path of Carbon

Melvin Calvin, Andrew Benson and James Bassham worked out the pathway in the late 1940s and early 1950s by illuminating suspensions of the green alga *Chlorella* in the presence of $\ce{^{14}CO2}$ for a few seconds, killing the cells in boiling alcohol and separating the labeled compounds by two-dimensional paper chromatography (Calvin received the Nobel Prize in Chemistry in 1961). After the shortest exposures nearly all the label was in 3-phosphoglycerate, and within it in the carboxyl carbon. The acceptor was identified by perturbing the steady state: when the $\ce{CO2}$ supply was suddenly lowered, ribulose 1,5-bisphosphate accumulated and 3-phosphoglycerate fell, as expected if the first consumes $\ce{CO2}$ to make the second; when the light was switched off, 3-phosphoglycerate rose and ribulose 1,5-bisphosphate fell, because the reduction of 3-phosphoglycerate needs ATP and NADPH but its formation does not. Plants in which 3-phosphoglycerate is the first stable product, 80–90% of species (most trees, wheat, rice, soybean, spinach), are called C3 plants.

**Definition 25.1.1 (Carbon Assimilation and Carbon Fixation)** **Carbon assimilation** is the conversion of $\ce{CO2}$ into reduced organic compounds (triose phosphates and the biomolecules derived from them) by autotrophs. **Carbon fixation** is the single reaction in which $\ce{CO2}$ is incorporated into an organic molecule; in plants, the carboxylation of ribulose 1,5-bisphosphate to two molecules of 3-phosphoglycerate.

**Definition 25.1.2 (Calvin Cycle)** The **Calvin cycle** (reductive pentose phosphate pathway, Calvin–Benson–Bassham cycle) is the cyclic pathway of the chloroplast stroma (and of cyanobacteria and other autotrophic bacteria) that assimilates $\ce{CO2}$ in three stages: fixation of $\ce{CO2}$ by ribulose 1,5-bisphosphate carboxylase/oxygenase; reduction of the 3-phosphoglycerate formed to glyceraldehyde 3-phosphate with ATP and NADPH; and regeneration of ribulose 1,5-bisphosphate from five sixths of the triose phosphate, the remaining sixth being the net product.

The older name "dark reactions" is misleading: the cycle needs the ATP and NADPH of the light reactions and, as Section 25.2 shows, several of its enzymes are active only in the light. All thirteen enzymes are in the stroma. The reactions of stages 2 and 3 are those of **gluconeogenesis** and of the nonoxidative **pentose phosphate pathway** run toward pentose; only rubisco, sedoheptulose 1,7-bisphosphatase and phosphoribulokinase are unique to the cycle, and animals, lacking them, cannot convert $\ce{CO2}$ into sugar.

![The Calvin cycle in the chloroplast stroma, drawn for three molecules of CO₂. Stage 1: rubisco carboxylates three molecules of ribulose 1,5-bisphosphate (RuBP, C₅) to six 3-phosphoglycerate (C₃). Stage 2: 3-phosphoglycerate kinase (6 ATP) and the NADP-dependent glyceraldehyde 3-phosphate dehydrogenase (6 NADPH) reduce them to six glyceraldehyde 3-phosphate. One triose phosphate is the net product, used for starch in the stroma or exported for sucrose; the other five are rearranged in stage 3 (aldolase, transketolase, fructose 1,6-bisphosphatase, sedoheptulose 1,7-bisphosphatase, ribose 5-phosphate isomerase and ribulose 5-phosphate epimerase) into three ribulose 5-phosphate, which phosphoribulokinase phosphorylates (3 ATP) back to RuBP](./plots/calvin-cycle.py)

### 25.1.2. Rubisco

**Definition 25.1.3 (Rubisco)** **Rubisco** (ribulose 1,5-bisphosphate carboxylase/oxygenase) is the enzyme that adds $\ce{CO2}$ (carboxylase activity) or $\ce{O2}$ (oxygenase activity) to C-2 of the 2,3-enediolate of ribulose 1,5-bisphosphate, giving two molecules of 3-phosphoglycerate, or one of 3-phosphoglycerate and one of 2-phosphoglycolate. It is active only when a Lys residue of the active site (Lys201 in spinach) is carbamoylated by a $\ce{CO2}$ molecule distinct from the substrate and binds $\ce{Mg^2+}$.

```smiles
[O-]P(=O)([O-])OCC(=O)[C@H](O)[C@H](O)COP(=O)([O-])[O-] RuBP
[O-]C(=O)[C@H](O)COP(=O)([O-])[O-] 3-PG
[O-]C(=O)COP(=O)([O-])[O-] 2-PG
```

(Ribulose 1,5-bisphosphate, 3-phospho-D-glycerate and 2-phosphoglycolate, the products of carboxylation and oxygenation.)

Rubisco of plants, algae and cyanobacteria (form I) is a hexadecamer $\mathrm{L_8S_8}$ of $M_{\mathrm{r}}$ about 550 000: four dimers of large **subunits** ($M_{\mathrm{r}}$ 53 000, encoded by the chloroplast **gene** *rbcL*), each dimer forming two active sites at the interface between its subunits, capped by two tetramers of small subunits ($M_{\mathrm{r}}$ 14 000, encoded in the nucleus by *RbcS*). The small subunits are not catalytic but are needed for the assembly of the octameric core and tune its kinetic properties; folding of the large subunits needs the chloroplast **chaperonin** and specific assembly factors, which is why plant rubisco could not for many years be made in bacteria (achieved in 2017). Form II rubisco of purple bacteria (*Rhodospirillum rubrum*) is a simple $\mathrm{L_2}$ dimer, and archaea have a form III; all share the same active site.

The mechanism makes the carboxylation of an unactivated carbon possible:

1. The $\ce{Mg^2+}$ ion, held by the carbamate of Lys201 and by Asp203 and Glu204, binds the C-2 and C-3 oxygens of ribulose 1,5-bisphosphate. Removal of the C-3 proton gives the 2,3-enediolate, a carbanion-like nucleophile (compare the enolates of the **aldol reaction**, [6.5.22](/6.5.22)).
2. $\ce{CO2}$ (not $\ce{HCO3-}$) is attacked by C-2, forming the six-carbon β-keto acid 2-carboxy-3-keto-D-arabinitol 1,5-bisphosphate, which remains bound.
3. Hydration of the C-3 ketone and cleavage of the C-2–C-3 bond give one 3-phosphoglycerate, which carries the new carbon as its carboxyl, and a carbanion of the second, which is protonated.

The oxygenase reaction uses the same enediolate: $\ce{O2}$ adds at C-2 to give a hydroperoxide, which breaks down to 3-phosphoglycerate and 2-phosphoglycolate. No active site can prevent this completely, because both gases are small, uncharged and bind without a specific pocket; the enediolate reacts with whichever arrives.

Rubisco is a remarkably poor catalyst: its turnover number is only about $3\,\mathrm{s^{-1}}$ at $25\,^\circ\mathrm{C}$ in C3 plants, its $K_{\mathrm{M}}$ for $\ce{CO2}$ (about $10\,\mu\mathrm{M}$) is close to the concentration of $\ce{CO2}$ in the stroma, so that it works at about half its maximal rate, and it confuses its two **substrates** (Section 25.3). Plants compensate by quantity. Rubisco makes up about half of the soluble **protein** of leaves and is the most abundant enzyme on Earth; its concentration in the stroma, about $250\,\mathrm{mg\,mL^{-1}}$, corresponds to about 4 mM active sites, higher than that of its substrate $\ce{CO2}$ and comparable to that of ribulose 1,5-bisphosphate. A large share of the nitrogen of a leaf is invested in it, which links carbon fixation to nitrogen supply ([7.1.27](/7.1.27)). Among rubiscos from different organisms, a high carboxylation rate goes with a low specificity for $\ce{CO2}$ over $\ce{O2}$, a trade-off that suggests the enzyme is close to the best compromise its chemistry allows (Tcherkez, Farquhar and Andrews, 2006), and that attempts to engineer a faster and more specific rubisco are fighting chemistry, not only evolution.

### 25.1.3. Reduction of 3-Phosphoglycerate

The second stage reverses two steps of glycolysis ([7.1.18](/7.1.18#sec-18.2.3)). Stromal 3-phosphoglycerate kinase transfers a phosphoryl group from ATP to 3-phosphoglycerate, and the chloroplast **isozyme** of glyceraldehyde 3-phosphate dehydrogenase reduces the resulting 1,3-bisphosphoglycerate with NADPH (not **NADH**) to glyceraldehyde 3-phosphate and $\mathrm{P_i}$:

$$
\text{3-phosphoglycerate} + \ce{ATP} + \mathrm{NADPH} + \ce{H+} \to \text{glyceraldehyde 3-phosphate} + \ce{ADP} + \mathrm{P_i} + \ce{NADP+}. \tag{25.1}
$$
In glycolysis the same pair of reactions runs the other way; in the illuminated stroma the high [ATP]/[ADP] and $[\mathrm{NADPH}]/[\ce{NADP+}]$ ratios drive it toward triose phosphate. Triose phosphate isomerase equilibrates glyceraldehyde 3-phosphate with dihydroxyacetone phosphate (DHAP), and aldolase joins the two to fructose 1,6-bisphosphate.

### 25.1.4. Regenerating Ribulose 1,5-Bisphosphate

For the cycle to continue, five of every six triose phosphates (15 carbons) must be rebuilt into three ribulose 1,5-bisphosphate (15 carbons). The rearrangement uses only two kinds of carbon–carbon chemistry, both met in the pentose phosphate pathway ([7.1.18](/7.1.18#sec-18.6.2)): aldolase, which joins DHAP to an aldose (glyceraldehyde 3-phosphate or erythrose 4-phosphate), and **transketolase**, which moves the two-carbon ketol unit (C-1 and C-2) of a ketose (fructose 6-phosphate or sedoheptulose 7-phosphate) to glyceraldehyde 3-phosphate with **thiamine pyrophosphate** as carrier ([7.1.17](/7.1.17#sec-17.2.2)). Two phosphatases make the pathway irreversible in the direction of pentose:

| Step | Reaction | Carbons |
|---|---|---|
| 1 | aldolase: DHAP + glyceraldehyde 3-P → fructose 1,6-bisphosphate; FBPase: → fructose 6-P + $\mathrm{P_i}$ | 3 + 3 → 6 |
| 2 | **transketolase**: fructose 6-P + glyceraldehyde 3-P → erythrose 4-P + xylulose 5-P | 6 + 3 → 4 + 5 |
| 3 | aldolase: erythrose 4-P + DHAP → sedoheptulose 1,7-bisphosphate; SBPase: → sedoheptulose 7-P + $\mathrm{P_i}$ | 4 + 3 → 7 |
| 4 | transketolase: sedoheptulose 7-P + glyceraldehyde 3-P → ribose 5-P + xylulose 5-P | 7 + 3 → 5 + 5 |
| 5 | ribose 5-phosphate isomerase and ribulose 5-phosphate epimerase: → 3 ribulose 5-P | 3 × 5 |
| 6 | phosphoribulokinase (PRK): 3 ribulose 5-P + 3 ATP → 3 ribulose 1,5-bisphosphate + 3 ADP | 3 × 5 |

Three steps of the cycle are strongly exergonic and are its control points: the two bisphosphatases (FBPase and SBPase) and phosphoribulokinase, besides rubisco itself. Fructose 6-phosphate stands at a **branch point**: it can continue in the cycle or leave it for starch.

![Carbon bookkeeping and autocatalysis of the Calvin cycle. A: five triose phosphates (two dihydroxyacetone phosphate, DHAP, and three glyceraldehyde 3-phosphate, G3P; 15 carbons) are rearranged into three pentose phosphates. Each dot is a carbon, coloured by the triose phosphate it came from. Aldolase joins DHAP (which becomes carbons 1–3) to G3P or erythrose 4-phosphate (E4P); FBPase and SBPase remove the 1-phosphate of fructose 1,6-bisphosphate (F1,6BP) and sedoheptulose 1,7-bisphosphate (SBP); transketolase transfers carbons 1–2 of fructose 6-phosphate (F6P) or sedoheptulose 7-phosphate (S7P) to G3P, giving xylulose 5-phosphate (X5P). Ribose 5-phosphate (R5P) and the two X5P become three ribulose 5-phosphate (Ru5P), which phosphoribulokinase (PRK) converts to three RuBP. B: if a fraction f of the triose phosphate is withdrawn for starch and sucrose, the RuBP pool changes by the factor 6(1 − f)/5 per round (Formula 25.1.1): it grows for f < 1/6, is constant for f = 1/6 and shrinks for f > 1/6](./plots/calvin-carbon-bookkeeping.py)

The cycle is autocatalytic: its product can increase the amount of its own substrate. This has a simple quantitative form.

**Formula 25.1.1 (Autocatalysis of the Calvin Cycle)** If a fraction $f$ of the triose phosphate formed is withdrawn from the cycle, one round converts $R$ molecules of ribulose 1,5-bisphosphate into $2R(1 - f)$ triose phosphates that remain, which regenerate $\tfrac{3}{5}\cdot 2R(1-f)$ ribulose 1,5-bisphosphate. The pool is multiplied per round by

$$
g = \frac{6(1-f)}{5}. \tag{25.2}
$$

A steady state ($g = 1$) requires $f = 1/6$, the net product of the cycle. When a leaf is illuminated after a dark period, its pools of cycle intermediates are small, and for the first minutes photosynthesis accelerates gradually (the induction period) while the leaf withholds triose phosphate ($f < 1/6$) and builds up the pools. Conversely, if more than one sixth of the triose phosphate were exported, the cycle would run down; the regulation of export (Section 25.5) must therefore follow the rate of fixation.

### 25.1.5. Stoichiometry and Energy Efficiency

Three turns of the cycle fix three $\ce{CO2}$ and make one triose phosphate. Six ATP and six NADPH are used in stage 2 and three ATP by phosphoribulokinase:

$$
3\,\ce{CO2} + 9\,\ce{ATP} + 6\,\mathrm{NADPH} + 5\,\ce{H2O} \to \text{glyceraldehyde 3-phosphate} + 9\,\ce{ADP} + 8\,\mathrm{P_i} + 6\,\ce{NADP+} + 3\,\ce{H+}. \tag{25.3}
$$
Eight of the nine phosphates return to the stroma as $\mathrm{P_i}$; the ninth leaves with the triose phosphate and must be replaced from the cytosol (Section 25.1.6). The ratio ATP : NADPH = 3 : 2 matches approximately what linear electron flow provides, and **cyclic electron flow** makes up the difference ([7.1.24](/7.1.24)). Per $\ce{CO2}$, then, the cycle needs 3 ATP and 2 NADPH, and one glucose costs 18 ATP and 12 NADPH.

**Example 25.1.1** What is the maximal efficiency of the conversion of light energy into carbohydrate? Two NADPH need four electrons, each moved through both photosystems, so at least eight photons are absorbed per $\ce{CO2}$ (and per $\ce{O2}$ released); they also pump enough protons for about three ATP ([7.1.24](/7.1.24)). At 680 nm a mole of photons carries $176\,\mathrm{kJ}$, so eight moles carry $1408\,\mathrm{kJ}$. The standard Gibbs energy stored per mole of $\ce{CO2}$ reduced to the level of glucose is $2840/6 \approx 473\,\mathrm{kJ}$ ([7.1.16](/7.1.16#sec-16.2.1)). The efficiency is at most $473/1408 \approx 34\%$ for red light. Measured quantum requirements in low light and low $\ce{O2}$ are 9–10 photons per $\ce{CO2}$. For the whole solar spectrum, of which only the 400–700 nm band is absorbed and the blue photons lose their excess energy as heat, and after reflection, photorespiration and respiration, the theoretical maximum efficiency of conversion of sunlight into biomass is about 4.6% for C3 and 6% for C4 plants (Zhu, Long and Ort, 2008); crops in the field reach 1–2% over a growing season.

### 25.1.6. Export of Triose Phosphate

The inner chloroplast membrane is impermeable to most phosphorylated compounds, but it contains an abundant **antiporter**, the Pi–triose phosphate translocator (TPT), that exchanges stromal triose phosphate (DHAP, glyceraldehyde 3-phosphate) or 3-phosphoglycerate one for one with cytosolic $\mathrm{P_i}$. The exchange solves two problems at once: it exports the product to the cytosol, where it is made into sucrose, and it returns to the stroma the phosphate needed for **photophosphorylation**. Sucrose synthesis releases the phosphate of each triose phosphate in the cytosol, so the exchange is balanced. If sucrose synthesis lags, cytosolic $\mathrm{P_i}$ falls, export slows, triose phosphate and 3-phosphoglycerate accumulate in the stroma and $\mathrm{P_i}$ there falls: the signal for starch synthesis (Section 25.5.3).

The same translocator moves ATP and reducing power out of the chloroplast, although ATP and NADPH themselves cannot cross the envelope. DHAP exported to the cytosol is oxidized by the cytosolic glyceraldehyde 3-phosphate dehydrogenase and phosphoglycerate kinase to 3-phosphoglycerate, making NADH and ATP in the cytosol; the 3-phosphoglycerate returns on the translocator and is reduced again in the stroma. The DHAP–3-phosphoglycerate shuttle thus delivers one ATP and one NAD(P)H to the cytosol per turn.

## 25.2. Regulation by Light

### 25.2.1. Stromal pH and Mg²⁺

In the dark a plant must not spend its ATP on $\ce{CO2}$ fixation, and gluconeogenic and glycolytic reactions (both of which run in the stroma) must not cycle uselessly. Light changes the stroma in three ways that the Calvin cycle enzymes sense. First, pumping of protons into the thylakoid lumen raises the stromal pH from about 7 to about 8. Second, $\ce{Mg^2+}$ moves out of the lumen to balance the charge, raising the stromal $[\ce{Mg^2+}]$ from 1–3 mM to 3–6 mM. Both favour the carbamoylation of rubisco (the carbamate forms from the unprotonated Lys) and the formation of its $\ce{Mg^2+}$ complex, and the stromal FBPase, which needs $\ce{Mg^2+}$ and has a sharp pH optimum near 8, becomes more than a hundred times more active. Third, electrons flow from **photosystem I** into a regulatory relay.

### 25.2.2. The Ferredoxin–Thioredoxin System

**Definition 25.2.1 (Thioredoxin)** **Thioredoxin** is a small (about 12 kDa), ubiquitous protein with a redox-active disulfide in the conserved sequence –Cys–Gly–Pro–Cys–, which in its reduced (dithiol) form reduces disulfide bonds of target proteins. In chloroplasts it is reduced in the light by ferredoxin through ferredoxin:thioredoxin reductase.

In the light, reduced ferredoxin from **photosystem I** passes electrons to ferredoxin:thioredoxin reductase, an iron–sulfur enzyme, which reduces thioredoxins (types f and m in the stroma). Reduced thioredoxin reduces a regulatory disulfide in four enzymes of the cycle, FBPase, SBPase, phosphoribulokinase and NADP-glyceraldehyde 3-phosphate dehydrogenase, and in the γ subunit of the chloroplast **ATP synthase** and NADP-malate dehydrogenase; the change in conformation activates them. In the dark, the dithiols are reoxidized by $\ce{O2}$ and peroxides and the enzymes return to their inactive disulfide forms. In addition, in the dark the small protein CP12 binds glyceraldehyde 3-phosphate dehydrogenase and phosphoribulokinase in an inactive complex, which dissociates when CP12 is reduced. Glucose 6-phosphate dehydrogenase, the entry into the oxidative pentose phosphate pathway, is regulated by the same signal in the opposite sense: reduction inactivates it, so that the plastid does not oxidize hexose to make NADPH while the light reactions provide it, and reactivation at night lets the pathway supply NADPH from starch.

The logic is that of **reciprocal regulation** by a signal that reports the state of the energy supply, as with the **energy charge** in animals ([7.1.17](/7.1.17#sec-17.3.5)), except that here the signal is the redox state of the stroma. It is fast (seconds to minutes) and tied directly to the availability of the products of the light reactions.

![Light activation of the Calvin cycle (SBGN activity flow; open arrows activate, bars inhibit). Light drives electrons through photosystem I to ferredoxin; ferredoxin:thioredoxin reductase (FTR) reduces thioredoxin, whose dithiol reduces and activates FBPase, SBPase, phosphoribulokinase (PRK) and NADP-glyceraldehyde 3-phosphate dehydrogenase (NADP-GAPDH), activates rubisco activase, and inactivates glucose 6-phosphate dehydrogenase. Proton pumping into the lumen raises the stromal pH and Mg²⁺ concentration, which favour carbamoylation and activity of rubisco and the activity of FBPase. Rubisco activase releases inhibitory sugar phosphates (RuBP, CA1P) from rubisco. In the dark the disulfides re-form and the nocturnal inhibitor CA1P binds rubisco](./plots/light-activation.py)

### 25.2.3. Rubisco Activase and Inhibitors

The substrate itself is an inhibitor of rubisco. Ribulose 1,5-bisphosphate binds tightly to the active site of the uncarbamoylated enzyme and locks it in a closed conformation in which Lys201 cannot be carbamoylated; sugar phosphates formed by occasional misfires of the catalytic reaction (xylulose 1,5-bisphosphate, for example) block carbamoylated sites in the same way. Rubisco activase, a ring-shaped AAA+ ATPase, uses ATP to pull the bound sugar phosphates out of the active site, after which carbamoylation and $\ce{Mg^2+}$ binding can occur. Its activity rises with the [ATP]/[ADP] ratio and, for the isoform with a redox-sensitive C-terminal extension, with thioredoxin, so it too follows light. Many plants (bean and tobacco, for example; spinach makes little) also make at night a **transition-state analog**, 2-carboxyarabinitol 1-phosphate (CA1P, the "nocturnal inhibitor"), which binds the carbamoylated enzyme with high affinity; in the light activase releases it and a phosphatase degrades it. Rubisco activase is heat-labile, and its inactivation above about $35\,^\circ\mathrm{C}$ contributes to the decline of photosynthesis in heat waves.

## 25.3. Photorespiration

### 25.3.1. The Oxygenase Reaction and Its Cost

Under present air, roughly one in every three or four reactions catalyzed by rubisco in a C3 leaf at $25\,^\circ\mathrm{C}$ is an oxygenation. Its product 2-phosphoglycolate has no use and is toxic (it inhibits triose phosphate isomerase and SBPase), so its carbon must be recovered.

**Definition 25.3.1 (Photorespiration)** **Photorespiration** is the light-dependent uptake of $\ce{O2}$ and release of $\ce{CO2}$ that results from the oxygenase activity of rubisco and from the C2 (glycolate) pathway, which recycles two molecules of 2-phosphoglycolate into one 3-phosphoglycerate and one $\ce{CO2}$ through the chloroplast, the peroxisome and the mitochondrion.

The C2 pathway runs as follows.

1. In the chloroplast, phosphoglycolate phosphatase gives glycolate, which leaves through a transporter.
2. In the peroxisome, glycolate oxidase oxidizes glycolate with $\ce{O2}$ to glyoxylate and $\ce{H2O2}$ (destroyed by catalase), and glutamate:glyoxylate **aminotransferase** converts glyoxylate to glycine.
3. In the mitochondrion, the glycine decarboxylase complex, built like the **pyruvate dehydrogenase complex** from a **pyridoxal phosphate** enzyme, a lipoate-carrying protein, a **tetrahydrofolate** enzyme and dihydrolipoamide dehydrogenase, cleaves one glycine to $\ce{CO2}$ and $\ce{NH3}$ and transfers its α carbon to **tetrahydrofolate** with reduction of $\ce{NAD+}$; serine hydroxymethyltransferase adds this one-carbon unit to a second glycine:
$$
2\,\text{glycine} + \ce{NAD+} + \ce{H2O} \to \text{serine} + \ce{CO2} + \ce{NH3} + \mathrm{NADH} + \ce{H+}. \tag{25.4}
$$
4. Back in the peroxisome, serine is transaminated (serine:glyoxylate aminotransferase) to hydroxypyruvate, which hydroxypyruvate reductase reduces to glycerate.
5. In the chloroplast, glycerate kinase phosphorylates glycerate to 3-phosphoglycerate, which rejoins the Calvin cycle; the $\ce{NH3}$ is refixed by **glutamine synthetase** and ferredoxin-dependent **glutamate synthase** ([7.1.27](/7.1.27)).

![Photorespiration, the C2 (glycolate) pathway, in three organelles. Chloroplast: rubisco adds O₂ to ribulose 1,5-bisphosphate, giving 3-phosphoglycerate and 2-phosphoglycolate; phosphoglycolate phosphatase (PGLP) forms glycolate. Peroxisome: glycolate oxidase produces glyoxylate and H₂O₂ (destroyed by catalase); glutamate:glyoxylate aminotransferase (GGAT) forms glycine. Mitochondrion: the glycine decarboxylase complex and serine hydroxymethyltransferase (GDC + SHMT) convert two glycine into serine, CO₂ and NH₃ while reducing NAD⁺. Peroxisome: serine:glyoxylate aminotransferase (SGAT) and hydroxypyruvate reductase (HPR) give glycerate. Chloroplast: glycerate kinase (GLYK) returns 3-phosphoglycerate to the Calvin cycle, and glutamine synthetase and glutamate synthase (GS–GOGAT) refix the NH₃. Dashed arrows: transport between compartments](./plots/photorespiration-pathway.py)

Of the four carbons of two phosphoglycolates, three return as 3-phosphoglycerate and one is lost as $\ce{CO2}$, which undoes a quarter of a carboxylation. In energy, each oxygenation costs about 3.5 ATP and 2 NADPH (or the equivalent reduced ferredoxin): ATP for glycerate kinase, for the refixation of ammonia and for regenerating the consumed ribulose 1,5-bisphosphate. Unlike mitochondrial respiration, photorespiration conserves none of this energy. The flux is large: in bright light the glycolate pathway releases several times more $\ce{CO2}$ than the **citric acid cycle** of the same leaf, the four proteins of the glycine decarboxylase complex make up about half of the soluble protein of the mitochondrial matrix of pea and spinach leaves, and the ammonia released exceeds the primary assimilation of nitrate several-fold. Photorespiration has been estimated to lower the yield of soybean and wheat in the United States by about a third and a fifth.

Photorespiration is nonetheless indispensable as long as rubisco oxygenates: *Arabidopsis* mutants that lack an enzyme of the pathway grow normally in air enriched in $\ce{CO2}$ but die in normal air (Somerville and Ogren, 1979), from accumulated phosphoglycolate or glyoxylate. Engineered bypasses that oxidize glycolate completely to $\ce{CO2}$ inside the chloroplast, and release it next to rubisco, increased the field biomass of tobacco by about 25–40% (South, Cavanagh, Liu and Ort, 2019).

### 25.3.2. The Specificity Factor

Carboxylation and oxygenation compete for the same enzyme form E·RuBP-enediolate, so their rates follow the rule for two substrates of one enzyme, each with its own Michaelis–Menten parameters ([6.3.17](/6.3.17); competitive substrates, [7.1.9](/7.1.9#sec-9.4.1)): $v_{\mathrm{c}} = V_{\mathrm{c}}[\ce{CO2}]/\bigl(K_{\mathrm{c}}(1 + [\ce{O2}]/K_{\mathrm{o}}) + [\ce{CO2}]\bigr)$ and correspondingly for $v_{\mathrm{o}}$. The denominators are the same, and their ratio is independent of the amount of enzyme and of the RuBP concentration.

**Definition 25.3.2 (Specificity Factor)** The **specificity factor** of rubisco is the ratio of its specificity constants for the two gases,

$$
S_{\mathrm{c/o}} = \frac{V_{\mathrm{c}}/K_{\mathrm{c}}}{V_{\mathrm{o}}/K_{\mathrm{o}}} = \frac{V_{\mathrm{c}}K_{\mathrm{o}}}{V_{\mathrm{o}}K_{\mathrm{c}}},
$$
where $V_{\mathrm{c}}, V_{\mathrm{o}}$ are the maximal rates of carboxylation and oxygenation and $K_{\mathrm{c}}, K_{\mathrm{o}}$ the Michaelis constants for $\ce{CO2}$ and $\ce{O2}$; it equals the ratio of the rates of carboxylation and oxygenation at equal concentrations of the two gases.

**Formula 25.3.1 (Ratio of Oxygenation to Carboxylation)**

$$
\phi = \frac{v_{\mathrm{o}}}{v_{\mathrm{c}}} = \frac{[\ce{O2}]}{S_{\mathrm{c/o}}\,[\ce{CO2}]}. \tag{25.5}
$$

Since each oxygenation releases half a $\ce{CO2}$, net fixation is $v_{\mathrm{c}} - 0.5\,v_{\mathrm{o}} = v_{\mathrm{c}}(1 - 0.5\phi)$, which is zero when $\phi = 2$.

**Definition 25.3.3 (CO₂ Compensation Point)** The **CO₂ compensation point** of a leaf is the $\ce{CO2}$ concentration at which the net assimilation of $\ce{CO2}$ is zero; in the absence of mitochondrial respiration it is the photorespiratory compensation point

$$
\Gamma^* = \frac{[\ce{O2}]}{2\,S_{\mathrm{c/o}}}, \tag{25.6}
$$
at which the $\ce{CO2}$ released by photorespiration exactly balances that fixed.

**Example 25.3.1** Water in equilibrium with air (420 µmol $\ce{CO2}$ per mol, 21% $\ce{O2}$) at $25\,^\circ\mathrm{C}$ contains about $14\,\mu\mathrm{M}$ $\ce{CO2}$ and $270\,\mu\mathrm{M}$ $\ce{O2}$ (by **Henry's law**, with Henry constants of 0.034 and $0.0013\,\mathrm{M\,atm^{-1}}$). Diffusion through stomata and the mesophyll lowers $\ce{CO2}$ at rubisco to about $8\,\mu\mathrm{M}$. With $S_{\mathrm{c/o}} = 90$, typical of C3 crops, $\phi = 270/(90 \times 8) = 0.38$: about one oxygenation for every 2.7 carboxylations, and 19% of the carbon fixed is released again. $\Gamma^* = 270/180 = 1.5\,\mu\mathrm{M}$ in solution, about 44 µmol per mol in the gas phase, close to the value of $42.75\,\mu\mathrm{mol\,mol^{-1}}$ measured in leaves (Bernacchi et al., 2001).

The specificity factor of rubisco varies among organisms: about 40–60 in cyanobacteria and 70–85 in C4 plants, whose enzymes work at high $\ce{CO2}$ and are faster, 80–110 in C3 plants, and up to about 240 in some red algae, whose enzymes are slow. Temperature is decisive. Both the specificity factor and the solubility of $\ce{CO2}$ relative to $\ce{O2}$ fall as the temperature rises, so $\phi$ and $\Gamma^*$ increase steeply. At $35\,^\circ\mathrm{C}$ a C3 leaf with intercellular $\ce{CO2}$ of 280 µmol per mol oxygenates once for every two carboxylations; when drought partly closes its stomata and intercellular $\ce{CO2}$ falls, photorespiration rises further.

![Temperature dependence of photorespiration and the cost of C3 and C4 photosynthesis, computed from the temperature function of the photorespiratory compensation point Γ* (Bernacchi et al., 2001; activation energy 37.8 kJ mol⁻¹). A: ratio of oxygenation to carboxylation, $\phi = 2\Gamma^*/C_{\mathrm{i}}$ (solid), and the fraction of carboxylated carbon lost again as CO₂, 0.5φ (dashed), at intercellular CO₂ $C_{\mathrm{i}}$ = 280 µmol mol⁻¹ (open stomata) and 200 µmol mol⁻¹ (partly closed stomata). B: the specificity factor $S_{\mathrm{c/o}}$ implied by Γ* in solution (left axis) and the ratio of dissolved CO₂ to O₂ in water equilibrated with air (right axis); both fall with temperature. C: ATP needed per net CO₂ fixed, (3 + 3.5φ)/(1 − 0.5φ) for a C3 leaf, against 5 ATP for C4 photosynthesis (5.5 with 20% leakage of CO₂ from the bundle sheath): above about 27–30 °C at $C_{\mathrm{i}}$ = 280, and above about 20–24 °C at $C_{\mathrm{i}}$ = 200, the C4 pathway is the cheaper one](./plots/photorespiration-ratio.py)

## 25.4. CO₂-Concentrating Mechanisms

### 25.4.1. C4 Photosynthesis

If rubisco cannot tell $\ce{CO2}$ from $\ce{O2}$, the alternative is to change the gas mixture it sees. Many plants of hot, sunny habitats, including maize, sugarcane, sorghum, millet and crabgrass, fix $\ce{CO2}$ first into a four-carbon acid and release it again next to rubisco.

**Definition 25.4.1 (C4 Pathway)** The **C4 pathway** is a $\ce{CO2}$-concentrating mechanism in which phosphoenolpyruvate carboxylase in the cytosol of mesophyll cells fixes $\ce{HCO3-}$ into oxaloacetate; the four-carbon acid (malate or aspartate) diffuses into bundle-sheath cells, where it is decarboxylated, raising the $\ce{CO2}$ concentration around rubisco and the Calvin cycle; the three-carbon remainder returns to the mesophyll, where pyruvate phosphate dikinase regenerates phosphoenolpyruvate. Plants using it are C4 plants.

In the NADP-malic enzyme type (maize, sugarcane, sorghum):

1. Carbonic anhydrase in the mesophyll cytosol converts $\ce{CO2}$ to $\ce{HCO3-}$, the substrate of PEP carboxylase: $\text{PEP} + \ce{HCO3-} \to \text{oxaloacetate} + \mathrm{P_i}$. PEP carboxylase has a high affinity for $\ce{HCO3-}$ and does not react with $\ce{O2}$.
2. NADP-malate dehydrogenase of the mesophyll chloroplast reduces oxaloacetate to malate, which moves through plasmodesmata into the bundle-sheath cells.
3. In the bundle-sheath chloroplasts, NADP-malic enzyme decarboxylates malate to pyruvate and $\ce{CO2}$, producing NADPH; the $\ce{CO2}$ concentration rises to about ten times that in air, and rubisco works near its maximal rate with little oxygenation. Bundle-sheath chloroplasts of maize have little **photosystem II**, so they also receive reducing power with the malate.
4. Pyruvate returns to the mesophyll, where pyruvate phosphate dikinase (PPDK) phosphorylates it and $\mathrm{P_i}$ at the same time: $\text{pyruvate} + \ce{ATP} + \mathrm{P_i} \to \text{PEP} + \ce{AMP} + \mathrm{PP_i}$. Hydrolysis of the pyrophosphate makes the cost two phosphoanhydride bonds per $\ce{CO2}$.

In other C4 species, oxaloacetate is transaminated to aspartate for transport, and the bundle sheath decarboxylates with NAD-malic enzyme (millets, amaranth) or PEP carboxykinase (guinea grass). In all types the bundle-sheath cells, arranged in a wreath (Kranz anatomy) around the veins, have thick walls that slow the escape of $\ce{CO2}$; about 10–30% of the concentrated $\ce{CO2}$ still leaks back. Three enzymes of the C4 pathway are light-regulated: NADP-malate dehydrogenase by thioredoxin; PEP carboxylase by phosphorylation of a Ser **residue** by PEP carboxylase kinase in the light, which lowers its sensitivity to **feedback inhibition** by malate; and PPDK by the bifunctional PPDK regulatory protein, which inactivates it in the dark by phosphorylating a Thr residue (with ADP as donor) and reactivates it in the light by phosphorolytic removal of the phosphate.

![The two CO₂-concentrating pathways of land plants. A: C4 photosynthesis of the NADP-malic enzyme type. In the mesophyll cell, carbonic anhydrase converts CO₂ to HCO₃⁻, which PEP carboxylase adds to phosphoenolpyruvate (PEP); NADP-malate dehydrogenase (NADP-MDH) reduces the oxaloacetate to malate, which diffuses through plasmodesmata into the bundle-sheath cell. NADP-malic enzyme (NADP-ME) releases CO₂, concentrated about tenfold, which rubisco fixes in the Calvin cycle; pyruvate returns, and pyruvate phosphate dikinase (PPDK) regenerates PEP with ATP and Pᵢ, forming AMP and pyrophosphate. B: crassulacean acid metabolism. At night, with stomata open, PEP from the glycolytic breakdown of starch is carboxylated and the malate is stored as malic acid in the vacuole; during the day, with stomata closed, NADP-malic enzyme releases CO₂ for rubisco and the Calvin cycle, and the pyruvate is made back into starch by gluconeogenesis. C: schematic daily course in a CAM leaf: stomatal conductance is high at night (shaded) and low during the day, and vacuolar malic acid rises at night and falls during the day](./plots/c4-cam.py)

C4 photosynthesis costs 5 ATP and 2 NADPH per $\ce{CO2}$, against 3 ATP and 2 NADPH for the Calvin cycle alone. Whether it pays depends on how much photorespiration it avoids. Counting 3.5 ATP per oxygenation and half a $\ce{CO2}$ lost, a C3 leaf spends $(3 + 3.5\phi)/(1 - 0.5\phi)$ ATP per net $\ce{CO2}$, which rises with temperature through $\phi$ (Formula 25.3.1): the curves cross at about $27\text{–}30\,^\circ\mathrm{C}$ for open stomata, matching the temperature of about 28–30 °C above which C4 plants outgrow C3 plants, and at lower temperatures when stomata close (figure above, C). C4 plants also need less water and nitrogen per unit of carbon fixed: they can keep their stomata narrower, and they need less rubisco. Only about 3% of land plant species are C4, yet they account for roughly a quarter of terrestrial primary production. C4 photosynthesis evolved independently more than 60 times from C3 ancestors in the last 30 million years, as atmospheric $\ce{CO2}$ declined, by recruiting enzymes that all C3 plants already have and moving them to new cells; projects to engineer it into rice rely on the same parts.

### 25.4.2. Crassulacean Acid Metabolism

Succulents of deserts and epiphytes (cacti, agaves, pineapple, many orchids and bromeliads, about 6% of species) separate the two carboxylations in time instead of in space, which saves water.

**Definition 25.4.2 (Crassulacean Acid Metabolism)** **Crassulacean acid metabolism** (CAM) is a $\ce{CO2}$-concentrating mechanism in which the stomata open at night, when evaporation is low, and PEP carboxylase fixes $\ce{CO2}$ into oxaloacetate and malate, stored as malic acid in the vacuole; during the day the stomata close, malate is decarboxylated (by NADP- or NAD-malic enzyme or PEP carboxykinase), and the $\ce{CO2}$ released behind closed stomata is fixed by rubisco in the Calvin cycle in the same cells.

The PEP for the night carboxylation comes from the glycolytic breakdown of starch (or soluble sugars), and the three-carbon product of the day decarboxylation returns to starch by gluconeogenesis, so CAM plants cycle carbohydrate daily as well as malate. Vacuolar malic acid can exceed 100 mM by dawn and lowers the vacuolar pH to about 3.5; the stored acid made the leaves of stonecrops (Crassulaceae) taste sour in the morning, which led to the discovery of the pathway. The switch between night and day is set by the circadian clock, mainly through PEP carboxylase kinase, which phosphorylates and activates PEP carboxylase at night. CAM costs about 6.5 ATP and 2 NADPH per $\ce{CO2}$, but a CAM plant loses only about a third to a sixth as much water per $\ce{CO2}$ fixed as a C3 plant. Some species, such as the ice plant *Mesembryanthemum crystallinum*, switch from C3 photosynthesis to CAM under drought or salt stress.

| | C3 | C4 | CAM |
|---|---|---|---|
| Examples | wheat, rice, soybean, spinach, most trees | maize, sugarcane, sorghum, crabgrass | cacti, agaves, pineapple, orchids |
| First $\ce{CO2}$-fixing enzyme and product | rubisco; 3-phosphoglycerate | PEP carboxylase; oxaloacetate | PEP carboxylase (night); oxaloacetate |
| Separation of the two carboxylations | none | in space: mesophyll and bundle sheath | in time: night and day, same cell |
| Energy per $\ce{CO2}$ | 3 ATP, 2 NADPH | 5 ATP, 2 NADPH | about 6.5 ATP, 2 NADPH |
| Photorespiration | substantial, rising with temperature | strongly suppressed | suppressed (except at dusk and dawn) |
| Favoured environment | cool to moderate, moist | hot, bright, seasonally dry | arid, hot days and cool nights |

### 25.4.3. Carboxysomes and Pyrenoids

Aquatic photosynthesis faces a $\ce{CO2}$ diffusion coefficient in water ten thousand times lower than in air. Cyanobacteria pump $\ce{HCO3-}$ into the cell with transporters driven by $\ce{Na+}$ or ATP and concentrate it about a thousandfold; rubisco and carbonic anhydrase are packed together in carboxysomes, polyhedral compartments with a protein shell that is poorly permeable to $\ce{CO2}$, so that $\ce{CO2}$ formed from $\ce{HCO3-}$ inside the shell is fixed before it escapes. Many green algae concentrate rubisco instead in the pyrenoid of the chloroplast, a liquid-like **biomolecular condensate** held together by a multivalent linker protein (EPYC1 in *Chlamydomonas*), formed by **liquid–liquid phase separation** ([7.2.21](/7.2.21)). Installing carboxysomes or pyrenoids in crop chloroplasts is one of the main current strategies, with photorespiratory bypasses and faster rubisco, for raising the efficiency of C3 crops. Experience with other engineered steps is sobering: raising the amount of rubisco, or of single light-regulated enzymes, changed the rate of photosynthesis little, because flux control is shared among many steps (**metabolic control analysis**, [7.1.17](/7.1.17#sec-17.4)); increasing SBPase, which has a high **flux control coefficient** in tobacco, did raise growth.

## 25.5. Biosynthesis of Starch, Sucrose and Cellulose

### 25.5.1. Starch

In bright light a leaf makes more triose phosphate than it needs. Part is exported as sucrose; part is stored in the chloroplast as transitory starch, which is broken down at night to supply sucrose for export and fuel for respiration. Seeds, roots and tubers store long-term starch in amyloplasts. Starch synthesis follows the logic of **glycogen** synthesis ([7.1.19](/7.1.19#sec-19.4.1)): glucose is activated as a **sugar nucleotide**, here ADP-glucose rather than UDP-glucose, and added to the nonreducing ends of existing chains.

**Definition 25.5.1 (ADP-Glucose Pyrophosphorylase and Starch Synthase)** **ADP-glucose pyrophosphorylase** (AGPase) catalyzes glucose 1-phosphate + ATP → ADP-glucose + $\mathrm{PP_i}$, the regulated step of starch synthesis in plastids (and of glycogen synthesis in bacteria). **Starch synthase** transfers the glucosyl residue of ADP-glucose to the C-4 hydroxyl of the nonreducing end of an α(1→4)-glucan chain.

Inorganic pyrophosphatase in the plastid makes the overall reaction irreversible:

$$
\text{starch}_n + \text{glucose 1-phosphate} + \ce{ATP} \to \text{starch}_{n+1} + \ce{ADP} + 2\,\mathrm{P_i}, \qquad \Delta_{\mathrm{r}}G'^{\circ} \approx -50\,\mathrm{kJ\,mol^{-1}}. \tag{25.7}
$$
The hexose phosphate for starch comes from fructose 6-phosphate of the Calvin cycle through the stromal phosphohexose isomerase and phosphoglucomutase. Granule-bound starch synthase makes the unbranched **amylose**; soluble starch synthases, **branching enzymes** and a **debranching enzyme** (isoamylase) that trims misplaced branches together build **amylopectin** with its clusters of parallel chains, which crystallize into the semicrystalline granule ([7.1.10](/7.1.10#sec-10.3.2)). "Waxy" maize and rice, without **amylose**, lack the granule-bound enzyme. AGPase, a heterotetramer of two large and two small subunits, is activated allosterically by 3-phosphoglycerate and inhibited by $\mathrm{P_i}$, and in leaves also activated by thioredoxin-dependent reduction of a disulfide between its small subunits. The ratio $[\text{3-phosphoglycerate}]/[\mathrm{P_i}]$ in the stroma, which rises when fixation outruns export, therefore sets the rate of starch synthesis.

At night, transitory starch is degraded by an unusual route that starts with the phosphorylation of glucose residues at the granule surface by glucan, water dikinases, which loosens the crystalline structure; β-amylase then releases maltose, which is exported to the cytosol. The rate of degradation is set by the circadian clock so that starch falls linearly through the night and about 95% is used by dawn, whatever the length of the night (Graf, Schlereth, Stitt and Smith, 2010): a plant that runs out early starves before morning, and one that stops early wastes its store.

### 25.5.2. Sucrose

Sucrose is the main transport form of carbon in plants. It is made in the cytosol from exported triose phosphate: aldolase and the cytosolic FBPase-1 give fructose 6-phosphate, part of which becomes glucose 1-phosphate and, with UTP, UDP-glucose.

**Definition 25.5.2 (Sucrose 6-Phosphate Synthase)** **Sucrose 6-phosphate synthase** (SPS) catalyzes UDP-glucose + fructose 6-phosphate → sucrose 6-phosphate + UDP; sucrose 6-phosphate phosphatase (SPP) then hydrolyzes sucrose 6-phosphate to sucrose and $\mathrm{P_i}$.

The first reaction is nearly balanced ($\Delta_{\mathrm{r}}G'^{\circ} = -5.7\,\mathrm{kJ\,mol^{-1}}$); the hydrolysis of sucrose 6-phosphate ($-16.5\,\mathrm{kJ\,mol^{-1}}$) pulls it forward. SPS and SPP associate in a complex. Why sucrose? Its glycosidic bond links the anomeric carbons of both glucose and fructose (α1↔β2), so sucrose is a nonreducing sugar ([7.1.10](/7.1.10#sec-10.2.2)): it cannot react nonenzymatically with proteins (**glycation**), and it is not attacked by amylases and other common glycosidases, so it can travel at high concentration (up to 1 M in phloem sap) to the sink tissues, where it is cleaved by invertase (to glucose and fructose) or by sucrose synthase:

$$
\text{sucrose} + \ce{UDP} \rightleftharpoons \text{UDP-glucose} + \text{fructose}.
$$
(The enzyme is named for the reverse reaction.) Unlike animal cells, plant cells have no inorganic pyrophosphatase in the cytosol; cytosolic $\mathrm{PP_i}$ is about 0.3 mM, which keeps UDP-glucose pyrophosphorylase readily reversible and allows $\mathrm{PP_i}$ to serve as an energy donor, for example in the $\mathrm{PP_i}$-dependent phosphofructokinase and the vacuolar proton-pumping pyrophosphatase. A few plants, notably sugar beet and sugarcane, store sucrose rather than starch.

### 25.5.3. Partitioning between Sucrose and Starch

The Calvin cycle can spare one sixth of its triose phosphate (Formula 25.1.1); the division of this sixth between sucrose and starch must follow the rate of fixation and the demand of the sinks. Three controls achieve it.

1. **Fructose 2,6-bisphosphate**. As in the liver ([7.1.19](/7.1.19#sec-19.2.3)), **fructose 2,6-bisphosphate** inhibits the gluconeogenic enzyme, here cytosolic FBPase-1, and activates the glycolytic one, here $\mathrm{PP_i}$-dependent phosphofructokinase. It is made by a bifunctional PFK-2/FBPase-2, whose kinase is inhibited by DHAP and 3-phosphoglycerate and stimulated by fructose 6-phosphate and $\mathrm{P_i}$. During active photosynthesis, triose phosphate is abundant and $\mathrm{P_i}$ is consumed, so PFK-2 is inhibited, [F2,6BP] falls (it varies inversely with the rate of photosynthesis) and carbon flows into fructose 6-phosphate and sucrose; in the dark, [F2,6BP] rises and favours glycolysis.
2. SPS is activated allosterically by glucose 6-phosphate and inhibited by $\mathrm{P_i}$, and inactivated by phosphorylation of a Ser residue by a **protein kinase** of the SnRK1 family; glucose 6-phosphate inhibits the kinase and $\mathrm{P_i}$ the opposing phosphatase, which reinforces the allosteric effects. Because phosphohexose isomerase holds the hexose phosphates close to equilibrium, which lies toward glucose 6-phosphate, glucose 6-phosphate reports the supply of fructose 6-phosphate.
3. AGPase in the stroma responds to $[\text{3-phosphoglycerate}]/[\mathrm{P_i}]$ (Section 25.5.1). When sucrose synthesis is slower than fixation, $\mathrm{P_i}$ returning through the translocator falls, 3-phosphoglycerate accumulates in the stroma, and starch synthesis takes up the excess.

The result is a robust division: sucrose is made at the rate the sinks take it, starch absorbs the surplus during the day, and the night breakdown of starch keeps sucrose export going.

![Partitioning of triose phosphate between starch in the chloroplast and sucrose in the cytosol. The Pi–triose phosphate translocator (TPT) exchanges stromal triose phosphate for cytosolic Pᵢ. In the stroma, aldolase, FBPase, phosphohexose isomerase and phosphoglucomutase (PGM) give glucose 1-phosphate, which ADP-glucose pyrophosphorylase (AGPase) converts to ADP-glucose for starch synthase; 3-phosphoglycerate activates and Pᵢ inhibits AGPase. In the cytosol, aldolase and FBPase-1 give fructose 6-phosphate; glucose 6-phosphate, PGM and UDP-glucose pyrophosphorylase (UGPase) give UDP-glucose; sucrose 6-phosphate synthase (SPS) and sucrose 6-phosphate phosphatase (SPP) make sucrose for the phloem. Fructose 2,6-bisphosphate (F2,6BP), made by PFK-2 from fructose 6-phosphate, inhibits FBPase-1; triose phosphate and 3-phosphoglycerate inhibit PFK-2 in the light, Pᵢ and fructose 6-phosphate stimulate it in the dark. SPS is activated by glucose 6-phosphate and inhibited by Pᵢ and by phosphorylation](./plots/sucrose-starch-partition.py)

### 25.5.4. Cellulose

**Cellulose**, unbranched chains of thousands of β(1→4)-linked glucose residues assembled into crystalline microfibrils ([7.1.10](/7.1.10#sec-10.3.3)), is the most abundant biopolymer: plants make more than $10^{11}$ tonnes a year. Unlike starch and glycogen it is built outside the cell, by enzymes in the plasma membrane.

**Definition 25.5.3 (Cellulose Synthase)** **Cellulose synthase** (CesA) is a processive glycosyltransferase of the plasma membrane that transfers glucose from UDP-glucose on the cytoplasmic side to the nonreducing end of a growing β(1→4)-glucan chain, which it extrudes through a channel formed by its own transmembrane helices; in plants, CesA proteins assemble into hexameric rosettes of about 25–30 nm, the cellulose synthase complexes.

Each of the six particles of a rosette contains three CesA proteins, each making one chain, so a complex extrudes 18 parallel chains that crystallize at once into a microfibril about 3 nm across. The glucose in UDP-glucose is α-linked, that in cellulose β-linked: CesA is an inverting glycosyltransferase, with the acceptor hydroxyl attacking the anomeric carbon of the donor in a single displacement. The UDP-glucose comes largely from sucrose, through a membrane-associated sucrose synthase. The complexes move in the plane of the membrane, pushed by the polymerization itself, along tracks of cortical microtubules, so that the microfibrils are laid down perpendicular to the axis of growth and direct the expansion of the cell ([7.12](/7.12)). Bacterial cellulose synthase (BcsA of *Rhodobacter sphaeroides*, solved by X-ray crystallography) shows the same architecture; herbicides such as isoxaben target CesA.

### 25.5.5. From Fat to Sugar, and Pools of Intermediates

Oilseeds (sunflower, castor bean, rape) store triacylglycerols, and their seedlings, before they can photosynthesize, make sucrose from fat. **β oxidation** in glyoxysomes ([7.1.21](/7.1.21#sec-21.5.3)) gives acetyl-CoA; the **glyoxylate cycle** converts two acetyl-CoA into succinate; mitochondria convert succinate to malate; and in the cytosol PEP carboxykinase and gluconeogenesis make hexose phosphates and sucrose ([7.1.20](/7.1.20#sec-20.5.2)). Three compartments cooperate, and the separation of the glyoxysome from the mitochondrial citric acid cycle prevents the acetyl groups from being burned. Glycerol from the triacylglycerols and **glucogenic amino acids** from storage proteins feed gluconeogenesis as well. Animals lack isocitrate lyase and malate synthase, and their pyruvate dehydrogenase reaction is irreversible, so they cannot make net glucose from **fatty acids** ([7.1.19](/7.1.19#sec-19.1.5)).

Throughout plant metabolism, pathways are best seen not as separate lines but as pools of rapidly equilibrating intermediates (the hexose phosphates glucose 1-phosphate, glucose 6-phosphate and fructose 6-phosphate; the pentose 5-phosphates; the triose phosphates) shared among pathways and connected between compartments by specific transporters. The direction of flux through the pools reverses between day and night and differs between tissues. In leaves, the source tissues, triose phosphate goes to sucrose by day and starch goes to sucrose by night; sucrose is loaded into the phloem and moved by the osmotically generated pressure flow to the sinks (roots, tubers, fruits, growing tissues), where it is unloaded, cleaved and used for respiration, cell walls or storage ([7.13](/7.13)).

## Summary

The pathway cards ([7.1.16](/7.1.16#sec-16.1.3)):

| Field | Calvin cycle | Photorespiration (C2 pathway) | C4 pathway | Starch and sucrose synthesis |
|---|---|---|---|---|
| Location | chloroplast stroma (all autotrophic **eukaryotes**; cyanobacteria) | chloroplast, peroxisome, mitochondrion | mesophyll cytosol and chloroplast; bundle-sheath chloroplast | starch: stroma, amyloplasts; sucrose: cytosol |
| Net reaction | 3 $\ce{CO2}$ + 9 ATP + 6 NADPH → triose phosphate + 9 ADP + 8 $\mathrm{P_i}$ + 6 $\ce{NADP+}$ (Eq. (25.3)) | 2 2-phosphoglycolate + $\ce{O2}$ → 3-phosphoglycerate + $\ce{CO2}$ + $\ce{NH3}$ (refixed) | $\ce{CO2}$ (air) + 2 ATP equivalents → $\ce{CO2}$ (bundle sheath) | glucose 1-P + ATP → starch + ADP + 2 $\mathrm{P_i}$ (Eq. (25.7)); UDP-glucose + fructose 6-P → sucrose + UDP + $\mathrm{P_i}$ |
| Energy account | per $\ce{CO2}$: 3 ATP, 2 NADPH; ≥ 8 photons; at most 34% of red light (Example 25.1.1) | per oxygenation: about 3.5 ATP, 2 NADPH, 0.5 $\ce{CO2}$ lost | 5 ATP, 2 NADPH per $\ce{CO2}$ (CAM about 6.5 ATP) | 1 ATP (starch) or 1 UTP (sucrose) per hexose |
| Committed and regulated steps | rubisco (Definition 25.1.3); FBPase, SBPase, phosphoribulokinase | rubisco oxygenation, set by $S_{\mathrm{c/o}}$ (Definition 25.3.2) | PEP carboxylase; PPDK | AGPase (Definition 25.5.1); SPS (Definition 25.5.2); cytosolic FBPase-1 |
| Activators | light: stromal pH ≈ 8, $\ce{Mg^2+}$, reduced thioredoxin (Definition 25.2.1); rubisco activase | high $\ce{O2}$, high temperature, low $\ce{CO2}$ (Formula 25.3.1) | light; phosphorylation of PEP carboxylase (day in C4, night in CAM) | AGPase: 3-phosphoglycerate; SPS: glucose 6-P |
| Inhibitors | dark (disulfides), RuBP and CA1P bound to uncarbamoylated or carbamoylated rubisco | high $\ce{CO2}$ (C4, CAM, carboxysomes) | malate inhibits PEP carboxylase | AGPase and SPS: $\mathrm{P_i}$; FBPase-1: F2,6BP |
| Covalent and other control | thioredoxin–disulfide switches; CP12 complex in the dark | — | PPDK phosphorylated (inactive) in the dark; PEP carboxylase kinase | SPS phosphorylation (SnRK1); PFK-2 inhibited by triose phosphate and 3-PG |
| Opposing pathway | oxidative pentose phosphate pathway (G6PD inactivated by thioredoxin in the light) | — | — | night degradation of starch (glucan, water dikinase, β-amylase); invertase, sucrose synthase in sinks |
| **Coenzymes** | NADPH, **TPP** (transketolase), $\ce{Mg^2+}$ | **PLP**, tetrahydrofolate, **lipoate**, NAD (glycine decarboxylase); **FMN** (glycolate oxidase) | NADPH (malic enzyme, MDH) | ADP-glucose, UDP-glucose |
| Diseases, drugs, applications | engineering rubisco, SBPase | photorespiratory bypasses; lethal mutants in air | C4 rice project | waxy cereals (no amylose) |

| Topic | Key points |
|---|---|
| Calvin cycle (Definition 25.1.2) | fixation, reduction, regeneration; 13 stromal enzymes, three unique (rubisco, SBPase, PRK); autocatalytic, steady state at 1/6 export (Formula 25.1.1) |
| Rubisco (Definition 25.1.3) | $\mathrm{L_8S_8}$; carbamoyl-Lys201 and $\ce{Mg^2+}$; enediolate attacked by $\ce{CO2}$ or $\ce{O2}$; $k_{\mathrm{cat}} \approx 3\,\mathrm{s^{-1}}$, about half the leaf soluble protein |
| Light regulation (25.2) | pH 7 → 8, $\ce{Mg^2+}$ up; ferredoxin → FTR → thioredoxin activates FBPase, SBPase, PRK, GAPDH and inactivates G6PD; activase removes inhibitory sugar phosphates |
| Photorespiration (Definition 25.3.1) | three organelles; 2 C₂ → C₃ + $\ce{CO2}$; $\phi = [\ce{O2}]/(S_{\mathrm{c/o}}[\ce{CO2}])$, $\Gamma^* = [\ce{O2}]/(2S_{\mathrm{c/o}})$; rises with temperature |
| C4 and CAM (Definitions 25.4.1, 25.4.2) | PEP carboxylase on $\ce{HCO3-}$; separation in space (Kranz) or time (night/day); C4 cheaper above 27–30 °C; CAM saves water |
| Starch, sucrose, cellulose (25.5) | ADP-glucose and starch synthase; UDP-glucose, SPS and SPP; F2,6BP, $[\text{3-PG}]/[\mathrm{P_i}]$ and $\mathrm{P_i}$ partition the carbon; CesA rosettes extrude 18-chain microfibrils |

## Questions

1. A suspension of *Chlorella* photosynthesizing at steady state in light and 1% $\ce{CO2}$ is suddenly (a) darkened, (b) transferred to 0.003% $\ce{CO2}$ in the light. Predict the immediate changes in [3-phosphoglycerate] and [ribulose 1,5-bisphosphate] in each case, and explain how these experiments identified the $\ce{CO2}$ acceptor.

   **Answer** (a) In the dark, ATP and NADPH disappear within seconds, so the reduction of 3-phosphoglycerate and the phosphorylation of ribulose 5-phosphate stop, while carboxylation continues briefly with the remaining ribulose 1,5-bisphosphate: 3-phosphoglycerate rises and ribulose 1,5-bisphosphate falls. (b) At low $\ce{CO2}$ the carboxylation slows, while regeneration of ribulose 1,5-bisphosphate from the existing triose phosphates continues: ribulose 1,5-bisphosphate rises and 3-phosphoglycerate falls. The reciprocal behaviour, with ribulose 1,5-bisphosphate accumulating exactly when $\ce{CO2}$ becomes limiting, showed that it is the substance that reacts with $\ce{CO2}$ to give 3-phosphoglycerate.

2. Show that the Calvin cycle needs exactly 9 ATP and 6 NADPH per triose phosphate, and that one of the nine phosphates must be imported from the cytosol. What happens to photosynthesis if the Pi–triose phosphate translocator is blocked?

   **Answer** Three ribulose 1,5-bisphosphate + 3 $\ce{CO2}$ give 6 3-phosphoglycerate; 6 phosphoglycerate kinase reactions use 6 ATP, and 6 GAPDH reactions use 6 NADPH and release 6 $\mathrm{P_i}$; five triose phosphates are converted to three pentose phosphates, releasing 2 $\mathrm{P_i}$ (FBPase and SBPase); three PRK reactions use 3 ATP. Total 9 ATP, 6 NADPH, 8 $\mathrm{P_i}$ released; the ninth phosphate (from the ninth ATP) stays in the triose phosphate product. When the product leaves the chloroplast, one $\mathrm{P_i}$ must come in to regenerate ATP. If the translocator is blocked, the product cannot leave, triose phosphate is diverted to starch (which releases phosphate in the stroma), so photosynthesis continues for a while, but sucrose export stops and, if starch synthesis cannot keep up, stromal $\mathrm{P_i}$ falls, ATP synthesis slows and the cycle slows. Mutant plants lacking the translocator make much more starch during the day and export carbon at night by degrading it.

3. Iodoacetate reacts with free –SH groups of Cys residues. Which Calvin cycle enzymes would you expect to be affected in illuminated chloroplasts, and why?

   **Answer** The thioredoxin-regulated enzymes are activated by reduction of a disulfide to two free thiols, so in the light FBPase, SBPase, phosphoribulokinase and NADP-GAPDH have exposed Cys –SH groups and can be alkylated. GAPDH is also inhibited directly, because its catalytic Cys forms the thiohemiacetal and thioester intermediates (as in glycolysis). Alkylation of the regulatory thiols locks the enzymes in a modified state; in any case, the cycle stops at the GAPDH step.

4. A C3 leaf at $30\,^\circ\mathrm{C}$ has intercellular $\ce{CO2}$ of 260 µmol per mol and $\Gamma^* = 55\,\mu\mathrm{mol\,mol^{-1}}$. (a) Calculate $\phi$ and the fraction of carboxylated carbon lost by photorespiration. (b) How much ATP and NADPH does the leaf spend per net $\ce{CO2}$? (c) Compare with a C4 leaf.

   **Answer** (a) $\phi = 2\Gamma^*/C_{\mathrm{i}} = 110/260 = 0.42$; the fraction of carbon lost is $0.5\phi = 0.21$. (b) Per carboxylation 3 ATP and 2 NADPH, per oxygenation 3.5 ATP and 2 NADPH, and the net gain per carboxylation is $1 - 0.5\phi = 0.79\,\ce{CO2}$: ATP $(3 + 3.5 \times 0.42)/0.79 = 5.7$, NADPH $(2 + 2 \times 0.42)/0.79 = 3.6$ per net $\ce{CO2}$. (c) A C4 leaf needs 5 ATP (5.5 with 20% leakage) and 2 NADPH per $\ce{CO2}$, so at this temperature it is cheaper in ATP and much cheaper in reducing power; at $20\,^\circ\mathrm{C}$ ($\Gamma^* \approx 33$) the C3 leaf needs only about 4.4 ATP and is the more economical.

5. Maize leaves are exposed to $\ce{^{14}CO2}$ in the light for 1 s; more than 90% of the label is at C-4 of malate, aspartate and oxaloacetate. Only after about a minute does $\ce{^{14}C}$ appear in C-1 of 3-phosphoglycerate. Explain. Design an experiment with $\ce{^{14}CO2}$ that distinguishes a CAM plant from a C4 plant.

   **Answer** In maize, PEP carboxylase in the mesophyll adds $\ce{HCO3-}$ to the C-3 of PEP, which becomes C-4 (the new carboxyl) of oxaloacetate and, after reduction or transamination, of malate and aspartate. Only after these acids reach the bundle sheath and are decarboxylated does the same carbon enter 3-phosphoglycerate, in its carboxyl (C-1), through rubisco. To distinguish CAM from C4, supply $\ce{^{14}CO2}$ in the dark: a CAM plant incorporates it into malate, which accumulates overnight and whose label moves into 3-phosphoglycerate and sugars the next morning even without further $\ce{^{14}CO2}$; a C4 plant fixes almost nothing in the dark (its stomata close and PEP carboxylase and PPDK are inactive), and in the light the label passes through malate into sugars within seconds to minutes.

6. Explain why the concentration of fructose 2,6-bisphosphate in leaf cytosol falls when photosynthesis is fast, and why this favours sucrose synthesis. What would you expect in a transgenic plant that overexpresses an F2,6BP-insensitive cytosolic FBPase?

   **Answer** Fast photosynthesis produces triose phosphate and 3-phosphoglycerate, which are exported to the cytosol and inhibit PFK-2, and consumes $\mathrm{P_i}$, which stimulates PFK-2; both lower [F2,6BP]. Low F2,6BP releases the inhibition of cytosolic FBPase-1 (and reduces the activity of the opposing PP-PFK), so triose phosphate flows to fructose 6-phosphate, UDP-glucose and sucrose. A plant with an insensitive FBPase would make sucrose even when photosynthesis is slow, draining triose phosphate; in the light it would make less starch, and at the start of the day or in low light it could withdraw more than one sixth of the triose phosphate and slow the autocatalytic build-up of the Calvin cycle intermediates. (Such plants show altered partitioning toward sucrose and lower starch.)

7. (Open question) Rubisco has been called "the most important and most inefficient enzyme". Discuss the evidence for and against the view that rubisco is poorly optimized, and the strategies, natural and engineered, for working around it.

   **Answer** Points to cover: rubisco has a low $k_{\mathrm{cat}}$ (about $3\,\mathrm{s^{-1}}$), a $K_{\mathrm{M}}$ for $\ce{CO2}$ close to the ambient concentration, and it reacts with $\ce{O2}$; plants need huge amounts of it, and photorespiration costs C3 crops a fifth to a third of their potential yield. On the other hand, rubisco evolved when the atmosphere was rich in $\ce{CO2}$ and poor in $\ce{O2}$, and across organisms there is a strong negative correlation between $k_{\mathrm{cat}}$ and $S_{\mathrm{c/o}}$, which suggests that the chemistry of the enediolate (the same intermediate must be reactive enough to bind $\ce{CO2}$ and therefore $\ce{O2}$) imposes a trade-off and that each form is close to optimal for its $\ce{CO2}$ environment. Natural workarounds concentrate $\ce{CO2}$: C4 (in space), CAM (in time), carboxysomes and pyrenoids; they allow faster, less specific enzymes. Engineered strategies: photorespiratory bypasses (tobacco biomass +25–40%), transfer of carboxysomes or pyrenoids, C4 rice, replacement of rubisco by faster forms from other species, overexpression of steps with high flux control (SBPase) rather than of rubisco itself (metabolic control analysis), and faster recovery from photoprotection. Any evaluation should recognise that yield depends on the whole system, including nitrogen and water.
