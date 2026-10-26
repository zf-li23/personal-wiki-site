---
title: "Nitrogen Metabolism: Nitrogen Fixation, Amino Acid Biosynthesis, and Derived Molecules"
description: The nitrogen cycle; nitrogenase, its cofactors, mechanism, cost and protection from oxygen; nitrate assimilation; incorporation of ammonia by glutamine synthetase and glutamate synthase; the bicyclic cascade that regulates glutamine synthetase; glutamine amidotransferases; essential amino acids and the six biosynthetic families; the shikimate pathway; feedback control of branched pathways; porphyrins and heme, bilirubin; creatine, glutathione and D-amino acids; biogenic amines and nitric oxide; the pathway cards.
---

Nitrogen is the fourth most abundant element of living matter, after carbon, hydrogen and oxygen, and it is often the one that limits growth. The atmosphere is four-fifths $\ce{N2}$, but the triple bond makes it unusable to almost all organisms; only a few bacteria and archaea can reduce it to ammonia, and the supply of fixed nitrogen, natural and, since the Haber–Bosch process, industrial, sets the productivity of ecosystems and of agriculture. This chapter follows nitrogen from the atmosphere into biomolecules. Section 27.1 describes the nitrogen cycle, the nitrogenase complex, and the entry of ammonia into **metabolism** through glutamate and glutamine, controlled at glutamine synthetase by one of the most elaborate regulatory systems known. Section 27.2 builds the twenty amino acids from a handful of precursors of **glycolysis**, the **citric acid cycle** and the **pentose phosphate pathway**, and shows the patterns of **feedback inhibition** that keep their syntheses in balance; it is the anabolic counterpart of [7.1.22](/7.1.22), where the same carbon skeletons were degraded. Section 27.3 turns to molecules made from amino acids: porphyrins and **heme**, the bile pigments, creatine and glutathione, neurotransmitters and nitric oxide. Nucleotides, the other great class of nitrogen compounds, follow in [7.1.28](/7.1.28). The chemistry is familiar from Part II: **transamination** with **pyridoxal phosphate**, one-carbon transfers with **tetrahydrofolate** and **S-adenosylmethionine** ([7.1.17](/7.1.17#sec-17.2)), and transfer of the amide nitrogen of glutamine.

## 27.1. Overview of Nitrogen Metabolism

### 27.1.1. The Nitrogen Cycle

**Definition 27.1.1 (Nitrogen Cycle and Nitrogen Fixation)** The **nitrogen cycle** is the set of biological (and industrial) processes that interconvert the forms of nitrogen in the biosphere, from $\ce{NH4+}$ and organic nitrogen (oxidation number −3) through $\ce{N2}$ (0) to nitrate (+5). **Nitrogen fixation** is the conversion of $\ce{N2}$ into ammonia (or other reactive compounds); in biology it is catalyzed only by the nitrogenase of some bacteria and archaea.

| Process | Reaction | Organisms | Role |
|---|---|---|---|
| nitrogen fixation | $\ce{N2}$ → $\ce{NH3}$ | diazotrophs: cyanobacteria, *Azotobacter*, rhizobia in legume nodules, some methanogens | entry of new nitrogen |
| assimilation | $\ce{NH4+}$ → glutamine, glutamate → organic N | all organisms | **biosynthesis** |
| ammonification | organic N → $\ce{NH4+}$ | decomposers | recycling |
| nitrification | $\ce{NH3}$ → $\ce{NH2OH}$ → $\ce{NO2-}$ → $\ce{NO3-}$ | ammonia- and nitrite-oxidizing bacteria and archaea; complete ammonia oxidizers (comammox) | energy for chemolithotrophs |
| assimilatory nitrate reduction | $\ce{NO3-}$ → $\ce{NO2-}$ → $\ce{NH4+}$ | plants, algae, fungi, bacteria | the main nitrogen source of plants |
| denitrification | $\ce{NO3-}$ → $\ce{NO2-}$ → NO → $\ce{N2O}$ → $\ce{N2}$ | facultative anaerobes | anaerobic respiration; returns $\ce{N2}$ |
| anammox | $\ce{NH4+}$ + $\ce{NO2-}$ → $\ce{N2H4}$ → $\ce{N2}$ | Planctomycetes (anammoxosome) | anaerobic ammonium oxidation; a large part of oceanic $\ce{N2}$ production |

Nitrate is, after $\ce{O2}$, the most important biological electron acceptor. The anammox bacteria, discovered in a wastewater plant in Delft in the 1980s, form hydrazine as an intermediate and confine it in an organelle, the anammoxosome, whose membrane is made of ladderane **lipids** with fused, strained cyclobutane rings dense enough to slow the escape of hydrazine; they are now used to remove ammonia from wastewater at a fraction of the cost of nitrification and denitrification.

Most of the ammonia used by plants does not come from fixation but from nitrate assimilation. Nitrate reductase, a large soluble **enzyme**, passes two electrons from **NADH** through an –SH group, **FAD**, a **cytochrome** ($b_{557}$) and a molybdenum **cofactor** to nitrate; nitrite reductase of the chloroplast reduces nitrite to $\ce{NH4+}$ with six electrons, which come one at a time from ferredoxin reduced by **photosystem I**, through a [4Fe–4S] cluster and siroheme.

![The nitrogen cycle on a scale of oxidation number. Nitrogen fixation by nitrogenase reduces N₂ (0) to NH₃ (−3); assimilation by glutamine synthetase and glutamate synthase (GS–GOGAT) makes organic nitrogen, and ammonification returns it. Nitrification oxidizes NH₃ through hydroxylamine (−1) to nitrite (+3) and nitrate (+5); assimilatory nitrate reduction returns nitrate to NH₄⁺ with eight electrons; denitrification reduces nitrate and nitrite through NO (+2) and N₂O (+1) to N₂; anammox combines NH₄⁺ and nitrite through hydrazine (−2) to N₂](./plots/nitrogen-cycle.py)

Human activity has doubled the natural rate at which nitrogen enters the biosphere. The Haber–Bosch process makes ammonia from $\ce{N2}$ and $\ce{H2}$ at 400–500 °C and pressures of 15–30 MPa over an iron catalyst, consuming one to two percent of the world's energy; its fertilizer feeds about half of humanity. The excess reactive nitrogen washes into rivers and seas, causing eutrophication and hypoxic dead zones, and $\ce{N2O}$ from soils is a potent greenhouse gas and the main ozone-depleting emission of this century.

### 27.1.2. The Nitrogenase Complex

The reduction of $\ce{N2}$ by $\ce{H2}$ is exergonic ($\Delta_{\mathrm{r}}G'^{\circ} = -33.5\,\mathrm{kJ\,mol^{-1}}$ for $\ce{N2 + 3H2 -> 2NH3}$), but the triple bond, with a **bond energy** of about $945\,\mathrm{kJ\,mol^{-1}}$, gives it an enormous **activation energy**. The Haber–Bosch process overcomes it with heat and pressure; nitrogenase overcomes it at ambient temperature and 0.08 MPa of $\ce{N2}$ with ATP and highly reduced metal clusters.

**Definition 27.1.2 (Nitrogenase)** The **nitrogenase complex** consists of two proteins: dinitrogenase reductase (the Fe protein), a $\gamma_2$ homodimer with one [4Fe–4S] cluster between its subunits and two MgATP binding sites, and dinitrogenase (the MoFe protein), an $\alpha_2\beta_2$ tetramer with two P clusters ([8Fe–7S]) and two FeMo cofactors ([MoFe₇S₉C]-homocitrate) at which $\ce{N2}$ is reduced. The overall reaction is

$$
\ce{N2} + 10\,\ce{H+} + 8\,\mathrm{e^-} + 16\,\ce{ATP} \to 2\,\ce{NH4+} + \ce{H2} + 16\,\ce{ADP} + 16\,\mathrm{P_i}. \tag{27.1}
$$

The electrons come from reduced ferredoxin or flavodoxin (from **photosynthesis**, **fermentation** or respiration). The Fe **protein**, reduced and carrying two MgATP, docks on the MoFe protein; ATP binding shifts the reduction potential of its cluster from about −300 to about −420 mV and brings it within 14 Å of the P cluster; one electron passes to the P cluster and on to the FeMo cofactor, both ATP are hydrolyzed, and the Fe protein with MgADP dissociates. The switch regions that couple ATP hydrolysis to conformational change are homologous to those of **G proteins** ([7.1.14](/7.1.14#sec-14.2.1)). Dissociation of the Fe protein (about $6\,\mathrm{s^{-1}}$) limits the rate, so eight cycles are needed per $\ce{N2}$ and nitrogenase is one of the slowest enzymes, which diazotrophs compensate by making it in large amounts. Six electrons reduce $\ce{N2}$; two are released as $\ce{H2}$, an obligatory part of the mechanism: in the currently favoured model, the FeMo cofactor accumulates four electrons and protons as two metal hydrides, and their reductive elimination as $\ce{H2}$ is what activates the cofactor to bind and reduce $\ce{N2}$. The central carbon of the FeMo cofactor was identified only in 2011. Alternative nitrogenases with vanadium (VFe) or only iron (FeFe) instead of molybdenum are used when molybdenum is scarce; the vanadium enzyme can also reduce CO to short hydrocarbons.

![The nitrogenase complex and the energy cost of reduced nitrogen. A: electrons from reduced ferredoxin or flavodoxin reduce the [4Fe–4S] cluster of the Fe protein (γ₂); with two MgATP bound, its potential falls from about −300 to −420 mV, and on docking with the MoFe protein (α₂β₂) one electron passes through the P cluster ([8Fe–7S]) to the FeMo cofactor (MoFe₇S₉C–homocitrate), where N₂ is reduced; ATP is hydrolysed and the Fe protein dissociates (the rate-limiting step). Eight cycles give 2 NH₃ + H₂. B: cost of one NH₄⁺ incorporated into glutamate, in ATP equivalents (a pair of electrons counted as one NAD(P)H, one NAD(P)H as 2.5 ATP): fixation (8 ATP and 4 electrons per NH₃), nitrate reduction (8 electrons) and the glutamine synthetase–glutamate synthase step (1 ATP and 1 NAD(P)H) common to both](./plots/nitrogenase.py)

**Example 27.1.1** Compare the cost of nitrogen from $\ce{N2}$ and from nitrate. By Eq. (27.1), each $\ce{NH4+}$ from $\ce{N2}$ costs 8 ATP and 4 electrons (2 NAD(P)H equivalents, about 5 ATP equivalents): about 13 ATP equivalents. Nitrate needs 8 electrons (4 NAD(P)H equivalents, about 10 ATP equivalents) but no ATP. Assimilation into glutamate costs a further 1 ATP and 1 NAD(P)H in both cases. Fixation is thus somewhat more expensive than nitrate uptake, which is why legumes reduce nodulation when soil nitrate is plentiful; legumes spend roughly 6–12 g of carbon from photosynthesis for each gram of nitrogen fixed by their symbionts.

Nitrogenase is destroyed by $\ce{O2}$: the Fe protein has a half-life of about 30 s in air, the MoFe protein about 10 min. Diazotrophs protect it in several ways:

- strict anaerobes fix nitrogen only without $\ce{O2}$, and many facultative species repress the *nif* **genes** in its presence;
- *Azotobacter* respires so fast, partly uncoupled ([7.1.23](/7.1.23)), that it consumes $\ce{O2}$ as quickly as it enters;
- filamentous cyanobacteria such as *Anabaena* separate fixation from oxygenic photosynthesis in heterocysts, cells formed at intervals along the filament that lack **photosystem II**, have a thick **glycolipid** envelope that slows $\ce{O2}$ entry, and import sugar from their neighbours;
- in legume root nodules, rhizobia live as bacteroids in plant cells filled with leghemoglobin, a plant globin with very high affinity for $\ce{O2}$, which keeps free $\ce{O2}$ in the nanomolar range while delivering it to the bacterial **respiratory chain**; the nodules are pink.

In the symbiosis the plant supplies carbon (dicarboxylic acids) and protection, the bacteria supply ammonia, and the enrichment of soil nitrogen by legumes is the basis of crop rotation. Fixation is regulated tightly because it is expensive: ADP inhibits nitrogenase, ammonia represses the roughly 20 *nif* genes, and in some species (*Rhodospirillum*) ADP-ribosylation of an Arg **residue** of the Fe protein switches it off within minutes. Transferring nitrogen fixation to cereals would need the *nif* genes, the assembly machinery of the cofactors, an energy supply and an $\ce{O2}$-free compartment; the mitochondrial matrix and plastids are current candidates.

### 27.1.3. Assimilation of Ammonia: Glutamine Synthetase and Glutamate Synthase

Ammonia enters biomolecules through glutamate and glutamine, whose concentrations in most cells are far higher than those of other amino acids (glutamate is a main osmolyte of *E. coli*). The amide nitrogen of glutamine and the amino group of glutamate are then distributed: glutamate gives the α-amino groups of most other amino acids by **transamination**, and glutamine is the donor for a dozen biosyntheses.

**Definition 27.1.3 (Glutamine Synthetase)** **Glutamine synthetase** (GS) catalyzes the ATP-dependent amidation of glutamate through an enzyme-bound γ-glutamyl phosphate intermediate:

$$
\text{glutamate} + \ce{NH4+} + \ce{ATP} \to \text{glutamine} + \ce{ADP} + \mathrm{P_i} + \ce{H+}. \tag{27.2}
$$

**Definition 27.1.4 (Glutamate Synthase)** **Glutamate synthase** (glutamate:oxoglutarate aminotransferase, GOGAT), present in bacteria and plants but not in animals, transfers the amide nitrogen of glutamine to α-ketoglutarate with reduction, giving two glutamates:

$$
\alpha\text{-ketoglutarate} + \text{glutamine} + \mathrm{NAD(P)H} + \ce{H+} \to 2\,\text{glutamate} + \ce{NAD(P)+}. \tag{27.3}
$$
The plastid enzyme of plants uses reduced ferredoxin instead.

Together, the GS–GOGAT pathway makes one glutamate from α-ketoglutarate, $\ce{NH4+}$, ATP and NAD(P)H. Glutamate dehydrogenase can do the same in one step without ATP (the reverse of **oxidative deamination**, [7.1.22](/7.1.22#sec-22.1.4)), but its $K_{\mathrm{M}}$ for $\ce{NH4+}$ (about 1 mM) is too high for the low ammonia concentrations of most environments, and its equilibrium in cells lies toward **deamination**; glutamine synthetase, with a much higher affinity, is the route of choice, and the ATP it consumes is the price of scavenging scarce ammonia. In leaves, the ammonia released by **photorespiration** ([7.1.25](/7.1.25)) exceeds primary nitrate assimilation several-fold and is refixed by the plastid GS and ferredoxin-dependent GOGAT. In mammals, glutamine synthetase converts toxic free ammonia into glutamine for transport in the blood, and the **glucose–alanine cycle** carries amino groups from muscle to liver ([7.1.22](/7.1.22#sec-22.1.6)).

### 27.1.4. Regulation of Glutamine Synthetase

As the entry point of nitrogen, bacterial glutamine synthetase is regulated at three levels. The *E. coli* enzyme (class I, GSI) is a dodecamer of two stacked hexameric rings, with twelve **active sites** at the **subunit** interfaces (eukaryotic GSII is a decamer).

1. Cumulative **feedback inhibition**. Six end products of glutamine metabolism (tryptophan, histidine, **carbamoyl phosphate**, glucosamine 6-phosphate, AMP and CTP) and two indicators of the general amino acid supply (alanine and glycine) bind separate sites. Each inhibits only partially; their effects add up, and all eight together nearly abolish activity, so the rate of glutamine synthesis follows the summed demand of its many consumers.
2. Covalent modification. Adenylyltransferase (AT) attaches AMP to Tyr397 of each subunit; adenylylated subunits are much more sensitive to the feedback inhibitors and less active, and the activity of the dodecamer falls with the number of modified subunits. AT removes the AMP as well. Which of its two activities prevails is set by the regulatory protein PII: unmodified PII stimulates adenylylation, PII carrying UMP (PII–UMP) stimulates deadenylylation. A bifunctional uridylyltransferase/uridylyl-removing enzyme (UT/UR) adds UMP to a Tyr of PII when α-ketoglutarate and ATP are high (carbon and energy plentiful, nitrogen scarce) and removes it when glutamine and $\mathrm{P_i}$ are high. Thus a high [α-ketoglutarate]/[glutamine] ratio activates glutamine synthetase.
3. **Transcription**. PII–UMP also activates, through the **two-component system** NtrB–NtrC ([7.1.15](/7.1.15#sec-15.5.1)), transcription of *glnA*, which encodes glutamine synthetase; unmodified PII has the opposite effect.

The cascade of two modification cycles, each with a converter enzyme acting on another modifiable protein, is a **regulatory cascade** ([7.1.9](/7.1.9#sec-9.5.5)) analysed by Earl Stadtman and Boon Chock in the 1970s. Its quantitative behaviour follows from the Goldbeter–Koshland analysis of one cycle (**zero-order ultrasensitivity**, [7.1.9](/7.1.9#sec-9.6.1)).

**Formula 27.1.1 (Steady State of a Covalent-Modification Cycle)** If a converter enzyme modifies a protein with maximal rate $V_1$ and an opposing enzyme demodifies it with maximal rate $V_2$, both with Michaelis constants $J_1$, $J_2$ expressed as fractions of the total target protein, the steady-state fraction modified is the Goldbeter–Koshland function

$$
u = G(V_1, V_2, J_1, J_2) = \frac{2V_1J_2}{B + \sqrt{B^2 - 4(V_2 - V_1)V_1J_2}}, \qquad B = V_2 - V_1 + J_1V_2 + J_2V_1. \tag{27.4}
$$

When the converter enzymes are far from saturation ($J \gg 1$), $u$ depends hyperbolically on $V_1/V_2$; when they are saturated ($J \ll 1$), $u$ switches sharply at $V_1 = V_2$. In two cycles in series, the output of the first (here $u$, the fraction of PII uridylylated) sets the ratio of converter activities of the second; the response of glutamine synthetase to the [glutamine]/[α-ketoglutarate] ratio becomes steeper and can be shifted by each of the effectors that act on either converter enzyme, which gives the system both sensitivity and flexibility.

![The bicyclic cascade that controls bacterial glutamine synthetase. A (SBGN activity flow): α-ketoglutarate and ATP stimulate the uridylyltransferase (UT) activity of GlnD, glutamine and Pᵢ its uridylyl-removing (UR) activity; PII–UMP stimulates deadenylylation of glutamine synthetase (GS) by adenylyltransferase (AT), activating it, unmodified PII stimulates adenylylation, inactivating it; adenylylated GS is more sensitive to its eight cumulative feedback inhibitors. B: steady-state fraction of active GS as a function of the [glutamine]/[α-ketoglutarate] ratio computed with Formula 27.1.1 (illustrative parameters): one modification cycle with unsaturated converter enzymes (J = 1) responds gently (apparent Hill coefficient about 1.3); two cycles in series are steeper (about 1.8); with partly saturated enzymes (J = 0.2) the cascade behaves as a switch (about 8)](./plots/glutamine-synthetase-cascade.py)

### 27.1.5. Reaction Classes of Nitrogen Metabolism

Three kinds of reactions recur throughout the biosynthesis of amino acids and nucleotides: transamination and other reactions of **pyridoxal phosphate** ([7.1.22](/7.1.22#sec-22.1.3)); one-carbon transfers, with **tetrahydrofolate** at the oxidation levels of –$\ce{CH2OH}$ and –CHO and with **S-adenosylmethionine** at the level of –$\ce{CH3}$ ([7.1.22](/7.1.22#sec-22.3.2)); and transfers of the amide nitrogen of glutamine.

**Definition 27.1.5 (Glutamine Amidotransferase)** A **glutamine amidotransferase** is an enzyme that uses the amide nitrogen of glutamine to aminate a second substrate. It has a glutamine-binding domain, in which a conserved Cys attacks the amide and forms a γ-glutamyl thioester while $\ce{NH3}$ is released, and an acceptor domain, often activated by ATP as an acyl phosphate or adenylate; the $\ce{NH3}$ travels to the acceptor site through an internal channel without mixing with the solvent.

Examples are glutamate synthase, asparagine synthetase, **carbamoyl phosphate synthetase II**, glutamine–**PRPP** amidotransferase (the first enzyme of purine synthesis), CTP synthetase, anthranilate synthase and glucosamine 6-phosphate synthase. The ammonia channel, up to several nanometres long (in carbamoyl phosphate synthetase it links three active sites), is an example of **substrate channeling** that prevents the protonation of $\ce{NH3}$ to unreactive $\ce{NH4+}$ and its loss.

## 27.2. Biosynthesis of Amino Acids

### 27.2.1. Essential Amino Acids and the Six Families

Bacteria and plants make all twenty amino acids; mammals make about half, generally those with short pathways from common intermediates.

**Definition 27.2.1 (Essential Amino Acid)** An **essential amino acid** is an amino acid that an animal cannot synthesize at all, or not fast enough, and must obtain in the diet. For humans the nine essential amino acids are histidine, isoleucine, leucine, lysine, methionine, phenylalanine, threonine, tryptophan and valine; arginine, cysteine, glutamine, glycine, proline and tyrosine are conditionally essential, required when synthesis cannot meet demand (in growth, illness, or when the precursor is short, as tyrosine in phenylketonuria); alanine, asparagine, aspartate, glutamate and serine are nonessential.

The amino acids form six families according to their carbon precursor, all intermediates of glycolysis, the citric acid cycle or the **pentose phosphate pathway**; nitrogen is supplied by glutamate and glutamine. Aromatic amino acids are the most expensive to make: tryptophan costs about 74 high-energy phosphate bonds per molecule in *E. coli*, glycine and alanine about 12 (Akashi and Gojobori, 2002), and the most expensive amino acids are used less often in highly expressed proteins.

![The six biosynthetic families of the amino acids, by carbon precursor. Ribose 5-phosphate gives histidine (through PRPP and ATP); erythrose 4-phosphate and phosphoenolpyruvate give phenylalanine, tyrosine and tryptophan (through shikimate and chorismate); 3-phosphoglycerate gives serine, glycine and cysteine; pyruvate gives alanine, valine, leucine and, with threonine, isoleucine; oxaloacetate gives aspartate, asparagine, methionine, threonine and lysine; α-ketoglutarate gives glutamate, glutamine, proline and arginine. Colours: essential (red), conditionally essential (yellow) and nonessential (green) for humans](./plots/amino-acid-families.py)

The names of the precursors and of the amino acids in each family are worth memorizing as a table:

| Precursor (pathway) | Amino acids | Key steps |
|---|---|---|
| α-ketoglutarate (citric acid cycle) | Glu, Gln, Pro, Arg | GDH or GS–GOGAT; glutamate γ-semialdehyde cyclizes to Pro; Arg via ornithine |
| 3-phosphoglycerate (glycolysis) | Ser, Gly, Cys | phosphoserine pathway; SHMT; sulfide (bacteria, plants) or transsulfuration from Met (animals) |
| oxaloacetate (citric acid cycle) | Asp, Asn, Met, Thr, Lys | transamination; asparagine synthetase; aspartate β-semialdehyde **branch point** |
| pyruvate (glycolysis) | Ala, Val, Leu, (Ile) | transamination; acetohydroxy acid synthase (**TPP**) |
| PEP + erythrose 4-P (glycolysis, pentose phosphate pathway) | Phe, Tyr, Trp | shikimate → chorismate |
| ribose 5-phosphate (pentose phosphate pathway) | His | PRPP + ATP |

### 27.2.2. The α-Ketoglutarate Family

Glutamate and glutamine are made as in Section 27.1.3. For proline, γ-glutamyl kinase phosphorylates the γ-carboxyl of glutamate and the acyl phosphate is reduced (NAD(P)H) to glutamate γ-semialdehyde, which cyclizes spontaneously to Δ¹-pyrroline-5-carboxylate and is reduced to proline. Plants accumulate proline as an osmolyte under drought and salt stress. Bacteria make ornithine, and from it arginine, by a parallel pathway in which the α-amino group of glutamate is first acetylated, which prevents cyclization of the semialdehyde; transamination then gives N-acetylornithine, from which the acetyl group is removed. Ornithine becomes arginine through citrulline and argininosuccinate, as in the **urea cycle** ([7.1.22](/7.1.22#sec-22.2.1)). Mammals lack the acetylated route; they make ornithine by ornithine δ-aminotransferase acting on glutamate γ-semialdehyde and arginine through the **urea cycle** enzymes, which explains why arginine is conditionally essential in growth.

### 27.2.3. The 3-Phosphoglycerate Family

Serine is made in all organisms in three steps: 3-phosphoglycerate dehydrogenase oxidizes 3-phosphoglycerate with $\ce{NAD+}$ to 3-phosphohydroxypyruvate, a transamination from glutamate gives 3-phosphoserine, and phosphoserine phosphatase releases serine. (The dehydrogenase, the **committed step**, is amplified in some breast cancers and melanomas.) Serine hydroxymethyltransferase (PLP) transfers C-3 of serine to tetrahydrofolate as $N^5,N^{10}$-methylene-tetrahydrofolate, giving glycine; this is the main source of one-carbon units in the cell. In vertebrate liver the glycine cleavage system can also run backward ($\ce{CO2}$ + $\ce{NH4+}$ + methylene-THF + NADH → glycine).

The sulfur of cysteine comes from two different sources.

- Bacteria and plants reduce sulfate: ATP sulfurylase forms adenosine 5′-phosphosulfate (APS), which is reduced (in bacteria after phosphorylation to 3′-phosphoadenosine 5′-phosphosulfate) to sulfite and by sulfite reductase (6 electrons) to sulfide. Serine acetyltransferase activates serine to O-acetylserine, and O-acetylserine sulfhydrylase (PLP) replaces the acetate by sulfide to give cysteine.
- Mammals take the sulfur from methionine by transsulfuration: S-adenosylmethionine donates its methyl group in methylation reactions, S-adenosylhomocysteine is hydrolyzed to homocysteine, cystathionine β-synthase (PLP) condenses homocysteine with serine to cystathionine, and cystathionine γ-lyase (PLP) cleaves it to cysteine, α-ketobutyrate and $\ce{NH4+}$. Cysteine is therefore spared by methionine and becomes essential when methionine is short or transsulfuration is defective; deficiency of cystathionine β-synthase causes homocystinuria, with lens dislocation, skeletal abnormalities and thrombosis.

### 27.2.4. The Oxaloacetate and Pyruvate Families

Alanine and aspartate are made by transamination of pyruvate and oxaloacetate; asparagine synthetase, a glutamine amidotransferase, amidates aspartate with ATP (forming AMP and $\mathrm{PP_i}$). The lymphoblasts of childhood acute lymphoblastic leukemia make little asparagine synthetase and depend on plasma asparagine; bacterial L-asparaginase, which depletes it, is part of the standard chemotherapy, with remission in more than 95% of children when combined with other drugs.

The other six amino acids of these families are essential for humans and are made in bacteria and plants by long, interconnected pathways.

- Aspartate is phosphorylated by aspartokinase and reduced to aspartate β-semialdehyde, the branch point. One branch leads to lysine (through diaminopimelate in bacteria and plants, a precursor also of bacterial **peptidoglycan**; fungi make lysine by a different route through α-aminoadipate). The other is reduced by homoserine dehydrogenase to homoserine, the branch point between threonine (two steps) and methionine (succinylation or acetylation, sulfur from cysteine, and methylation of homocysteine by $N^5$-methyl-tetrahydrofolate).
- Threonine dehydratase (PLP) converts threonine to α-ketobutyrate, the start of isoleucine synthesis.
- Pyruvate gives valine and, with α-ketobutyrate, isoleucine through four shared enzymes; the first, acetohydroxy acid synthase, transfers a hydroxyethyl group from **thiamine pyrophosphate** to pyruvate or α-ketobutyrate. It is the target of the sulfonylurea and imidazolinone herbicides, harmless to animals, which lack the pathway. The valine intermediate α-ketoisovalerate starts a four-step branch to leucine.

### 27.2.5. The Aromatic Family: Shikimate and Chorismate

Aromatic rings are stable but not available in the environment; bacteria, fungi and plants build them from aliphatic precursors by ring closure and stepwise introduction of double bonds.

**Definition 27.2.2 (Shikimate Pathway)** The **shikimate pathway** converts phosphoenolpyruvate and erythrose 4-phosphate in seven steps, through 3-deoxy-D-arabino-heptulosonate 7-phosphate (DAHP), 3-dehydroquinate and shikimate, and with a second PEP added by 5-enolpyruvylshikimate 3-phosphate (EPSP) synthase, into chorismate, the common precursor of phenylalanine, tyrosine and tryptophan and of many other aromatic compounds; it is absent from animals.

```smiles
O=C([O-])C1=C[C@@H](O)[C@@H](O)[C@H](O)C1 shikimate
O=C([O-])C1=C[C@@H](OC(=C)C(=O)[O-])[C@H](O)C=C1 chorismate
```

Glyphosate, the most widely used herbicide, is a competitive inhibitor of EPSP synthase with respect to PEP; it is relatively nontoxic to animals because they lack the enzyme, and glyphosate-tolerant crops carry a bacterial EPSP synthase (CP4) insensitive to it. Besides the three amino acids, chorismate gives p-aminobenzoate for folate (whose use by bacteria is blocked by the sulfonamides, which mimic it), the quinone ring of **ubiquinone** and menaquinone in bacteria, salicylate and siderophores.

From chorismate the pathways branch.

1. Tryptophan. Anthranilate synthase replaces the 4-hydroxyl with an amino group from glutamine; anthranilate is joined to PRPP, rearranged and decarboxylated to indole-3-glycerol phosphate. Tryptophan synthase, an $\alpha_2\beta_2$ complex, cleaves it in the α subunit to indole and glyceraldehyde 3-phosphate, and the indole, never released, travels through a 25 Å tunnel to the β subunit, where a PLP-bound aminoacrylate derived from serine accepts it. The tunnel, a classic case of channeling, keeps the hydrophobic indole from escaping through membranes.
2. Phenylalanine and tyrosine. Chorismate mutase converts chorismate to prephenate by a **Claisen rearrangement**, a rare pericyclic reaction in biology; prephenate is decarboxylated (with loss of water) to phenylpyruvate or (with oxidation) to 4-hydroxyphenylpyruvate, and transamination gives phenylalanine and tyrosine. Animals make tyrosine by hydroxylation of phenylalanine (phenylalanine hydroxylase with tetrahydrobiopterin), the enzyme missing in **phenylketonuria** ([7.1.22](/7.1.22#sec-22.3.4)).

### 27.2.6. Histidine

Histidine is built from three precursors. ATP phosphoribosyltransferase joins N-1 of the adenine of ATP to C-1 of PRPP (5-phosphoribosyl-1-pyrophosphate, made from ribose 5-phosphate and ATP by ribose phosphate pyrophosphokinase); the purine ring is opened, glutamine donates a nitrogen, and the imidazole ring is closed with N-1 and C-2 of adenine. The remnant of the ATP is 5-aminoimidazole-4-carboxamide ribonucleotide (AICAR), an intermediate of purine synthesis ([7.1.28](/7.1.28)) that is recycled to ATP, so the purine serves as a metabolite rather than as an energy source without being wasted. PRPP contributes five carbons, ATP one carbon and one nitrogen, glutamine one nitrogen, and glutamate (by transamination) the α-amino group. ATP phosphoribosyltransferase is inhibited by histidine.

### 27.2.7. Regulation of Branched Pathways

In bacteria the first committed step of each amino acid pathway is usually catalyzed by an **allosteric enzyme** inhibited by the end product. The first example to be discovered (Umbarger, 1956) was threonine dehydratase, the first enzyme on the way from threonine to isoleucine, inhibited by isoleucine. Branched pathways pose a problem: if one end product inhibited the common first step, an excess of it would starve the cell of the others. Several patterns solve it, and many pathways combine them.

| Pattern | Mechanism | Example |
|---|---|---|
| sequential feedback inhibition | each end product inhibits the first enzyme after its own branch point; the intermediate at the branch point accumulates and inhibits the common first step | threonine inhibits homoserine dehydrogenase and aspartokinase; isoleucine inhibits threonine dehydratase |
| enzyme multiplicity | the common step is catalyzed by several **isozymes**, each controlled by a different end product | aspartokinases I (threonine), II (repressed by methionine), III (lysine) of *E. coli*; three DAHP synthases inhibited by Phe, Tyr and Trp |
| concerted inhibition | the enzyme is inhibited strongly only when two end products are present together | aspartokinase of several bacteria inhibited by lysine plus threonine |
| cumulative inhibition | each of several end products inhibits partially at separate sites, and the effects add | glutamine synthetase (Section 27.1.4) |
| repression of enzyme synthesis | the end product represses transcription (or causes **attenuation**) of the genes | *trp* **operon** ([7.2.11](/7.2.11)) |

![Feedback control of the branched aspartate pathway in E. coli. A: aspartate is phosphorylated by three aspartokinases (AK I, II, III) and reduced to aspartate β-semialdehyde, the branch point to lysine (dihydrodipicolinate synthase, DHDPS) and, through homoserine dehydrogenase (HDH I, II), to homoserine, which branches to methionine (homoserine succinyltransferase, MetA) and threonine; threonine dehydratase begins the path to isoleucine. Bars: allosteric inhibition by end products; AK II and HDH II are not inhibited but repressed by methionine. B: relative flux through the aspartokinase step as lysine rises (in units of its inhibition constant) for a single lysine-sensitive enzyme and for three equal isozymes of which only one is lysine-sensitive, with threonine low or high: with enzyme multiplicity, excess lysine cannot shut off the supply of threonine and methionine](./plots/branched-feedback.py)

Fast-growing bacteria must make the twenty amino acids in the proportions in which proteins use them, and they combine these allosteric controls (seconds) with repression and attenuation (minutes) and with the global stringent response to amino acid starvation ([7.2](/7.2)). In plants, the same aspartate pathway is a target of engineering: feedback-insensitive aspartokinase and dihydrodipicolinate synthase raise the lysine content of maize and soybean grain, which is nutritionally limiting.

## 27.3. Molecules Derived from Amino Acids

### 27.3.1. Porphyrins and Heme

**Definition 27.3.1 (Porphyrin)** A **porphyrin** is a planar macrocycle of four pyrrole rings joined by methine bridges, with a fully conjugated system that absorbs strongly near 400 nm (the Soret band); metal complexes of porphyrins are the heme of hemoglobin, myoglobin and the **cytochromes**, and, as the related chlorins, the **chlorophylls**.

In animals and fungi all the carbons and nitrogens of porphyrins come from glycine and succinyl-CoA (Shemin's experiments with ¹⁵N-glycine in the 1940s, using his own blood). **Heme** synthesis runs partly in mitochondria and partly in the cytosol:

1. δ-Aminolevulinate synthase (ALAS), a PLP enzyme of the mitochondrial matrix, condenses glycine with succinyl-CoA and decarboxylates the product to δ-aminolevulinate (ALA), the committed step. Plants and most bacteria make ALA instead from glutamate by the C5 pathway, through glutamyl-tRNA^Glu (the same **tRNA** used for protein synthesis) and glutamate 1-semialdehyde.
2. In the cytosol, ALA dehydratase, a Zn enzyme strongly inhibited by lead, joins two ALA to the pyrrole porphobilinogen (PBG).
3. PBG deaminase (hydroxymethylbilane synthase) links four PBG head to tail into the linear hydroxymethylbilane; uroporphyrinogen III synthase closes the ring, inverting the last pyrrole to give the asymmetric III isomer of all natural porphyrins (without the synthase the bilane cyclizes spontaneously to the useless symmetric uroporphyrinogen I).
4. Uroporphyrinogen decarboxylase converts the four acetate **side chains** to methyls; back in the mitochondrion, coproporphyrinogen oxidase and protoporphyrinogen oxidase give protoporphyrin IX, and ferrochelatase (also inhibited by lead) inserts $\ce{Fe^2+}$.

Heme represses the synthesis of the liver **isozyme** ALAS1, inhibits its import into mitochondria and promotes its degradation. The erythroid isozyme ALAS2 is regulated instead by iron, through an **iron-responsive element** in its **mRNA** ([7.2.18](/7.2.18)); its **mutations** cause X-linked sideroblastic anemia. Defects of the later enzymes cause the porphyrias, in which intermediates accumulate.

| Porphyria | Deficient enzyme | Main features |
|---|---|---|
| acute intermittent porphyria | PBG deaminase (heterozygous) | attacks of abdominal pain and neuropsychiatric symptoms triggered by drugs, fasting or **hormones** that induce ALAS1; ALA and PBG in urine. Treated with heme infusion and, since 2019, givosiran, an **siRNA** against ALAS1 mRNA |
| congenital erythropoietic porphyria | uroporphyrinogen III synthase | uroporphyrinogen I accumulates; red urine, teeth that fluoresce in UV light, severe photosensitivity and anemia |
| porphyria cutanea tarda | uroporphyrinogen decarboxylase (often acquired, with iron overload, alcohol, hepatitis C) | the most common porphyria; blistering of sun-exposed skin |
| erythropoietic protoporphyria | ferrochelatase | protoporphyrin in red cells and skin; painful sensitivity to light |

The photosensitivity has a photophysical cause: porphyrins absorb visible light and pass the excitation to $\ce{O2}$, forming singlet oxygen that damages membranes; the same reaction is used therapeutically in photodynamic therapy. It has been suggested that the episodes of madness of King George III were acute intermittent porphyria and that the vampire legends drew on the congenital form, but both suggestions are speculative.

### 27.3.2. Heme Degradation and Bilirubin

An adult breaks down about 6 g of hemoglobin a day, mostly in macrophages of the spleen that engulf aged red cells. Heme oxygenase (inducible HO-1 and constitutive HO-2) opens the ring at the α-methine bridge with $\ce{O2}$ and **NADPH**, releasing the bridge carbon as CO and the iron as $\ce{Fe^2+}$ (stored by ferritin), and giving the green linear tetrapyrrole biliverdin; biliverdin reductase reduces it to bilirubin.

**Definition 27.3.2 (Bilirubin)** **Bilirubin** is the yellow-orange linear tetrapyrrole formed from heme by heme oxygenase and biliverdin reductase. It is poorly soluble in water and travels in the blood bound to serum albumin; in the liver, UDP-glucuronosyltransferase 1A1 (UGT1A1) conjugates it with two glucuronates to the water-soluble bilirubin diglucuronide, which is secreted into bile.

In the intestine, bacteria convert bilirubin to urobilinogen; part is reabsorbed and excreted by the kidney as yellow urobilin, the rest becomes the brown stercobilin of feces. The colour changes of a bruise follow the pathway: purple hemoglobin, green biliverdin, yellow bilirubin.

![Heme synthesis and degradation. Synthesis: in the mitochondrion, δ-aminolevulinate synthase (ALAS, pyridoxal phosphate) condenses glycine and succinyl-CoA to δ-aminolevulinate (ALA), releasing CO₂ and CoA; heme inhibits ALAS1. In the cytosol, ALA dehydratase (ALAD; inhibited by lead) makes porphobilinogen, PBG deaminase joins four PBG into hydroxymethylbilane, uroporphyrinogen III synthase (UROS) closes the ring, and uroporphyrinogen decarboxylase (UROD) gives coproporphyrinogen III; in the mitochondrion, coproporphyrinogen and protoporphyrinogen oxidases (CPOX, PPOX) give protoporphyrin IX, and ferrochelatase inserts Fe²⁺ to make heme. Red labels: acute intermittent porphyria (AIP), congenital erythropoietic porphyria (CEP, with accumulation of uroporphyrinogen I), porphyria cutanea tarda (PCT) and erythropoietic protoporphyria (EPP) at the deficient steps. Degradation: heme oxygenase gives biliverdin, Fe²⁺ and CO; biliverdin reductase gives bilirubin, carried by albumin to the liver, conjugated by UGT1A1 and secreted in bile; gut bacteria make urobilinogen, which leaves as urobilin in urine and stercobilin in feces](./plots/heme-metabolism.py)

When bilirubin production exceeds the capacity of the liver, or its conjugation or excretion fails, it accumulates in blood and tissues and colours the skin and sclera yellow: jaundice. Unconjugated hyperbilirubinemia follows hemolysis or deficient conjugation; conjugated hyperbilirubinemia, with dark urine and pale stools, signals obstruction of bile flow or liver disease. Newborns, with a high turnover of fetal red cells and immature UGT1A1, often become jaundiced; very high unconjugated bilirubin can cross the blood–brain barrier and damage the basal ganglia (kernicterus), and phototherapy with blue light converts bilirubin into more soluble isomers that are excreted without conjugation. In Gilbert syndrome (5–10% of people), a **promoter** variant of *UGT1A1* lowers conjugation and causes harmless mild jaundice; the Crigler–Najjar syndromes are severe deficiencies. The products are not only waste: bilirubin is the main lipid-soluble antioxidant of plasma, and CO from heme oxygenase acts, like NO, as a vasodilator and signal; HO-1 is induced by heme, oxidative stress and hypoxia and protects tissues from heme toxicity.

### 27.3.3. Creatine, Glutathione and D-Amino Acids

Creatine, whose phosphorylated form **phosphocreatine** buffers ATP in muscle and brain ([7.1.16](/7.1.16#sec-16.3.5)), is made from three amino acids: arginine:glycine amidinotransferase (in kidney) transfers the amidino group of arginine to glycine, giving guanidinoacetate, and guanidinoacetate methyltransferase (in liver) methylates it with S-adenosylmethionine. Creatine and **phosphocreatine** cyclize nonenzymatically to creatinine at a nearly constant rate (about 2% of the body pool a day), which is excreted by the kidney; plasma creatinine is therefore a standard measure of the glomerular filtration rate.

Glutathione (γ-glutamylcysteinylglycine, GSH) is present at 1–10 mM in most cells and acts as a redox buffer. γ-Glutamylcysteine synthetase joins the γ-carboxyl of glutamate (activated as an acyl phosphate) to cysteine, the rate-limiting step, inhibited by GSH; glutathione synthetase adds glycine. GSH keeps protein thiols reduced, reduces glutaredoxin for deoxyribonucleotide synthesis ([7.1.28](/7.1.28)), conjugates electrophilic drugs and toxins (glutathione S-transferases; the acetaminophen story in [7.1.26](/7.1.26#sec-26.2.3)), and destroys peroxides through glutathione peroxidase, a selenocysteine enzyme: $2\,\text{GSH} + \ce{R-OOH} \to \text{GSSG} + \ce{R-OH} + \ce{H2O}$. Glutathione reductase regenerates GSH from glutathione disulfide (GSSG) with NADPH, which is why deficiency of glucose 6-phosphate dehydrogenase, the source of NADPH in red cells, leaves them vulnerable to oxidants ([7.1.18](/7.1.18#sec-18.6.1)).

D-Amino acids are made from the L isomers by PLP-dependent racemases. D-Alanine and D-glutamate are components of bacterial **peptidoglycan**, whose D-Ala–D-Ala terminus is the target of vancomycin; the antituberculosis drug cycloserine inhibits alanine racemase and D-Ala–D-Ala ligase. In the mammalian brain, serine racemase makes D-serine, a co-agonist of the NMDA glutamate **receptor**.

### 27.3.4. Plant Products of the Aromatic Amino Acids

Plants divert large fluxes of phenylalanine and tyrosine into secondary metabolism. Phenylalanine ammonia-lyase, which eliminates ammonia to give trans-cinnamate with an unusual cofactor formed from its own Ala–Ser–Gly sequence, opens the phenylpropanoid pathway to lignin (second only to **cellulose** in abundance in plants), flavonoids, coumarins and salicylate; tyrosine is the precursor of alkaloids such as morphine, and tryptophan of indole alkaloids and of the hormone auxin (indole-3-acetate, made through indole-3-pyruvate by the TAA and YUCCA enzymes; [7.1.15](/7.1.15#sec-15.5.6)). The flavours of cinnamon, vanilla, cloves and chili peppers are aromatic amino acid derivatives.

### 27.3.5. Biogenic Amines

**Definition 27.3.3 (Biogenic Amine)** A **biogenic amine** is an amine formed in organisms by decarboxylation of an amino acid (and often further modification), usually by a PLP-dependent decarboxylase; many are neurotransmitters, hormones or local mediators.

| Precursor | Steps (enzyme, cofactor) | Products and roles |
|---|---|---|
| tyrosine | tyrosine hydroxylase (tetrahydrobiopterin, Fe; rate-limiting) → L-DOPA; aromatic L-amino acid decarboxylase (PLP) → dopamine; dopamine β-hydroxylase (Cu, ascorbate) → norepinephrine; phenylethanolamine N-methyltransferase (SAM; adrenal medulla) → **epinephrine** | catecholamines: dopamine (movement, reward; deficient in Parkinson disease), norepinephrine (sympathetic transmitter), epinephrine (hormone, [7.1.14](/7.1.14)) |
| tryptophan | tryptophan hydroxylase (tetrahydrobiopterin) → 5-hydroxytryptophan; aromatic L-amino acid decarboxylase → serotonin; N-acetylation and O-methylation (SAM) in the pineal gland → melatonin | serotonin (mood, gut motility; target of antidepressants), melatonin (circadian rhythm) |
| glutamate | glutamate decarboxylase (PLP) | γ-aminobutyrate (GABA), the main inhibitory transmitter of the brain |
| histidine | histidine decarboxylase (PLP) | histamine: allergy and inflammation, gastric acid secretion, a transmitter |
| ornithine | ornithine decarboxylase (PLP) → putrescine; aminopropyl groups from decarboxylated SAM | polyamines spermidine and spermine, which bind nucleic acids and are needed for growth |

Pharmacology follows from the table. L-DOPA, which crosses the blood–brain barrier, replaces dopamine in Parkinson disease; carbidopa, an inhibitor of the decarboxylase that does not enter the brain, is given with it to prevent its conversion in peripheral tissues. Vigabatrin, an **irreversible inhibitor** of GABA **aminotransferase**, raises GABA in epilepsy. Cimetidine and its successors block the histamine $\mathrm{H_2}$ receptors of the stomach and reduce acid secretion. Eflornithine (difluoromethylornithine), a **suicide inactivator** of ornithine decarboxylase ([7.1.9](/7.1.9#sec-9.4.4)), treats African sleeping sickness: the trypanosome enzyme turns over slowly, so the parasite cannot replace it.

```smiles
NCCc1ccc(O)c(O)c1 dopamine
NC[C@H](O)c1ccc(O)c(O)c1 norepinephrine
NCCc1c[nH]c2ccc(O)cc12 serotonin
NCCc1c[nH]cn1 histamine
```

### 27.3.6. Nitric Oxide

In the 1980s, nitric oxide, until then known as a pollutant, was found to be the endothelium-derived relaxing factor that dilates blood vessels (Furchgott, Ignarro and Murad, Nobel Prize 1998).

**Definition 27.3.4 (Nitric Oxide Synthase)** **Nitric oxide synthase** (NOS) is the homodimeric enzyme that oxidizes a guanidino nitrogen of arginine to nitric oxide in two monooxygenation steps through $N^{\omega}$-hydroxy-L-arginine, a five-electron oxidation:

$$
\text{arginine} + 2\,\ce{O2} + 1.5\,\mathrm{NADPH} + 1.5\,\ce{H+} \to \text{citrulline} + \ce{NO} + 2\,\ce{H2O} + 1.5\,\ce{NADP+}. \tag{27.5}
$$
Each subunit has a reductase **domain** with FAD and **FMN**, related to NADPH–**cytochrome P-450** reductase, and an oxygenase domain with heme and tetrahydrobiopterin; electron flow between them is gated by $\ce{Ca^2+}$–**calmodulin**.

The neuronal (nNOS) and endothelial (eNOS) isoforms are activated by $\ce{Ca^2+}$–**calmodulin** within seconds; the inducible isoform (iNOS) of macrophages binds calmodulin so tightly that it is always active, and is controlled by transcription in response to cytokines and bacterial products, producing large amounts of NO that kill microbes (and in sepsis cause dangerous vasodilation). NO cannot be stored and lives only seconds, reacting with $\ce{O2}$, superoxide and heme; it diffuses through membranes to nearby cells, where it binds the heme of soluble **guanylyl cyclase** and activates the synthesis of cGMP, which relaxes smooth muscle through **protein kinase G** ([7.1.14](/7.1.14#sec-14.3.3)). Nitroglycerin, used since the nineteenth century against angina, works by releasing NO; sildenafil prolongs the cGMP signal by inhibiting **phosphodiesterase** 5.

## Summary

The pathway cards ([7.1.16](/7.1.16#sec-16.1.3)):

| Field | Nitrogen fixation | Ammonia assimilation (GS–GOGAT) | Amino acid synthesis | Heme synthesis |
|---|---|---|---|---|
| Location | diazotrophs (heterocysts, bacteroids in nodules) | all organisms (GOGAT: bacteria, plants) | cytosol; plastids in plants | mitochondria and cytosol (liver, erythroid cells) |
| Net reaction | $\ce{N2}$ + 10 $\ce{H+}$ + 8 e⁻ + 16 ATP → 2 $\ce{NH4+}$ + $\ce{H2}$ + 16 ADP + 16 $\mathrm{P_i}$ (Eq. (27.1)) | α-KG + $\ce{NH4+}$ + ATP + NAD(P)H → glutamate + ADP + $\mathrm{P_i}$ + NAD(P)⁺ | six families from glycolytic, citric acid cycle and pentose phosphate intermediates | 8 glycine + 8 succinyl-CoA + $\ce{Fe^2+}$ → heme + 8 **CoA** + 14 $\ce{CO2}$ + 4 $\ce{NH4+}$ |
| Energy account | about 13 ATP equivalents per $\ce{NH3}$ (Example 27.1.1) | 1 ATP + 1 NAD(P)H | from about 12 (Gly, Ala) to 74 (Trp) high-energy bonds | — |
| Committed and regulated steps | nitrogenase (Definition 27.1.2) | glutamine synthetase (Definition 27.1.3) | first enzyme after each branch point; aspartokinase, DAHP synthase, threonine dehydratase | ALA synthase |
| Activators | ATP; low $\ce{NH4+}$ | α-ketoglutarate, ATP (via PII–UMP) | — | — |
| Inhibitors | ADP; $\ce{O2}$ (inactivation) | eight cumulative feedback inhibitors; glutamine, $\mathrm{P_i}$ (via PII) | end products (Section 27.2.7) | heme (ALAS1); lead (ALAD, ferrochelatase) |
| Covalent and transcriptional control | ADP-ribosylation of the Fe protein; $\ce{NH4+}$ represses *nif* | adenylylation of Tyr397; PII uridylylation; NtrB–NtrC | repression, attenuation | heme represses ALAS1; iron controls ALAS2 **translation** |
| **Coenzymes** (**vitamins**) | Fe–S, FeMo cofactor; ferredoxin or flavodoxin | NAD(P)H or ferredoxin | PLP ($\mathrm{B_6}$), THF ($\mathrm{B_9}$), SAM, TPP ($\mathrm{B_1}$), $\mathrm{B_{12}}$ (methionine synthase), BH₄ | PLP |
| Diseases and drugs | — | — | **PKU**, homocystinuria; glyphosate, sulfonylureas, imidazolinones (herbicides); asparaginase (leukemia) | porphyrias; lead poisoning; givosiran |

| Topic | Key points |
|---|---|
| Nitrogen cycle (Definition 27.1.1) | fixation, nitrification, denitrification, anammox, nitrate assimilation; Haber–Bosch now comparable to biological fixation |
| Nitrogenase (Definition 27.1.2) | Fe protein + MoFe protein; P cluster, FeMo-co; 8 e⁻, 16 ATP, obligatory $\ce{H2}$; $\ce{O2}$ protection: heterocysts, leghemoglobin |
| GS, GOGAT (Definitions 27.1.3, 27.1.4) | γ-glutamyl phosphate; high affinity for $\ce{NH4+}$; cumulative inhibition, adenylylation cascade with PII and UT/UR (Formula 27.1.1) |
| Amidotransferases (Definition 27.1.5) | Cys nucleophile, ammonia channel |
| Amino acid families (27.2) | 9 essential amino acids (Definition 27.2.1); α-KG, 3-PG, OAA, pyruvate, PEP + E4P (shikimate, Definition 27.2.2), R5P |
| Branched pathways (27.2.7) | sequential feedback, enzyme multiplicity, concerted and cumulative inhibition, repression |
| Derived molecules (27.3) | porphyrins (Definition 27.3.1), bilirubin (Definition 27.3.2); creatine, glutathione, D-amino acids; biogenic amines (Definition 27.3.3); NO synthase (Definition 27.3.4) |

## Questions

1. Calculate how many ATP and how many electrons a soybean nodule needs to fix enough nitrogen for one molecule of glutamine. Explain why nitrogenase also produces $\ce{H2}$ and why some rhizobia carry an uptake hydrogenase.

   **Answer** Glutamine contains two nitrogens, so one $\ce{N2}$ is needed: 16 ATP and 8 electrons by Eq. (27.1), giving 2 $\ce{NH4+}$ and 1 $\ce{H2}$. The first $\ce{NH4+}$ is incorporated into glutamate by GS and GOGAT together (1 ATP and 1 NAD(P)H, 2 electrons), the second converts that glutamate into glutamine by GS (1 ATP): in total 18 ATP and 10 electrons per glutamine. $\ce{H2}$ formation is part of the mechanism: the FeMo cofactor must accumulate electrons as hydrides, and reductive elimination of $\ce{H2}$ is what allows $\ce{N2}$ to bind, so at least 25% of the electrons are lost as $\ce{H2}$. An uptake hydrogenase oxidizes this $\ce{H2}$ and returns electrons to the respiratory chain, recovering part of the energy and consuming $\ce{O2}$ that would damage nitrogenase.

2. *E. coli* is grown first with excess $\ce{NH4+}$ and then shifted to a medium with very little $\ce{NH4+}$. Describe the changes in the modification states of PII and glutamine synthetase and in the amount of the synthetase, and explain why a bicyclic cascade is useful here.

   **Answer** With excess ammonia, glutamine is high and α-ketoglutarate low; UR removes UMP from PII, unmodified PII stimulates adenylylation of GS, and GS is mostly adenylylated, inactive and sensitive to feedback inhibitors; *glnA* transcription is low. After the shift, glutamine falls and α-ketoglutarate rises, UT uridylylates PII, PII–UMP stimulates deadenylylation, GS becomes active, and PII–UMP, through NtrB–NtrC, induces *glnA*, so the amount of enzyme rises over the following generation. The cascade responds to the ratio of carbon to nitrogen signals rather than to either alone, amplifies small changes (each converter enzyme acts catalytically on many targets), produces a steeper response than a single cycle (Formula 27.1.1), and lets different effectors act at different levels.

3. A child with homocystinuria due to cystathionine β-synthase deficiency is treated with a methionine-restricted diet supplemented with cysteine, and some patients respond to large doses of pyridoxine. Explain the biochemical basis of each measure.

   **Answer** Without cystathionine β-synthase, homocysteine from S-adenosylmethionine cannot be converted to cystathionine and cysteine; homocysteine and methionine accumulate (homocysteine damages connective tissue and vessels) and cysteine becomes essential. Restricting methionine lowers the production of homocysteine; supplementing cysteine supplies what the blocked transsulfuration would have made. The enzyme uses pyridoxal phosphate; in patients whose mutant enzyme has reduced affinity for PLP, high doses of pyridoxine raise the coenzyme concentration enough to restore part of the activity. Betaine and folate, which remethylate homocysteine to methionine, are also used.

4. Glyphosate kills plants but has low acute toxicity in mammals; sulfonamides inhibit bacteria but not human cells. Explain both with the pathways of this chapter.

   **Answer** Glyphosate inhibits EPSP synthase of the shikimate pathway, which plants (and microbes) need to make phenylalanine, tyrosine, tryptophan and many aromatic compounds; animals lack the whole pathway and obtain these amino acids in the diet, so they have no target. Sulfonamides are analogues of p-aminobenzoate, made from chorismate, and inhibit dihydropteroate synthase in folate synthesis; bacteria must make folate, whereas humans take up folate from the diet and lack the enzyme.

5. In a patient with acute intermittent porphyria, attacks can be triggered by barbiturates, fasting and alcohol, and are treated by intravenous heme and glucose. Explain.

   **Answer** PBG deaminase activity is halved, which is sufficient normally; any stimulus that increases the demand for heme in the liver induces ALAS1 and raises the flux of ALA and PBG beyond what the half-active deaminase can handle, so ALA and PBG accumulate (they are neurotoxic). Barbiturates and alcohol induce cytochrome P-450 enzymes, whose synthesis consumes heme and relieves the repression of ALAS1; fasting induces ALAS1 through the transcriptional coactivator PGC-1α. Infused heme restores the negative feedback on ALAS1, and glucose suppresses its induction; givosiran silences ALAS1 mRNA.

6. A patient with yellow skin has (a) high unconjugated bilirubin, normal urine and dark stools; (b) high conjugated bilirubin, dark urine and pale stools. Where is the defect in each case?

   **Answer** (a) Unconjugated bilirubin is bound to albumin and not filtered by the kidney, so urine colour is normal; production exceeds conjugation capacity (hemolysis, or reduced UGT1A1 as in Gilbert or Crigler–Najjar syndrome), and plenty of bilirubin still reaches the gut, giving normal to dark stools. (b) Conjugated bilirubin is water-soluble and spills into urine, darkening it; it cannot reach the intestine because bile flow is obstructed (gallstone, tumour) or hepatocyte secretion fails, so no stercobilin forms and stools are pale.

7. (Open question) Nitrogen fixation by the Haber–Bosch process now rivals biological fixation. Discuss the biochemical options for reducing agriculture's dependence on industrial nitrogen, and the obstacles to each.

   **Answer** Points to cover: (1) Transferring the *nif* genes to cereals: some 20 genes, complex metallocluster assembly (NifB, NifEN, the FeMo-co maturation), the need for high ATP and low-potential electrons, and above all $\ce{O2}$ protection; targeting nitrogenase to mitochondria (high ATP, respiratory $\ce{O2}$ consumption) or plastids (in the dark) are the current approaches. (2) Engineering cereals to form nodules with rhizobia or to host associative diazotrophs: requires the symbiotic signalling pathway (Nod factors, common symbiosis genes) and the nodule organogenesis program. (3) Improving the use of applied nitrogen: higher nitrogen-use efficiency through regulation of nitrate uptake, GS activity and remobilization; inhibitors of nitrification that keep nitrogen as ammonium and reduce $\ce{N2O}$ losses. (4) Reducing photorespiration and its ammonia cycling (7.1.25) and rubisco demand for nitrogen. Each faces trade-offs: energy cost of fixation (about 13 ATP per N, paid by photosynthesis, which can lower yield), regulation and field performance; quantitative comparison with the energy cost of Haber–Bosch ammonia is part of the argument.
