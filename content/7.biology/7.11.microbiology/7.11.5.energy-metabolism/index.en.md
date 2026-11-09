---
title: "Energy Metabolism: Fermentation and Respiration"
description: "How chemoorganotrophic microorganisms conserve energy: free energy, reduction potentials and the redox tower; energy-rich compounds and storage; the diversity of sugar catabolism (glycolysis, the Entner–Doudoroff pathway, the pentose phosphate pathway, the phosphoketolase pathways, the modified pathways of archaea); fermentations (lactic, alcoholic, mixed-acid, butanediol, butyric and acetone–butanol, propionic, the Stickland reaction, fermentations driven by ion pumps); branched bacterial respiratory chains, the proton-motive force and ATP yields; and an outline of biosynthesis."
---

A microorganism growing on sugar has two broad ways to make ATP from it. It can *ferment*, breaking the sugar into smaller organic molecules and excreting them, with ATP made directly in a few enzymatic steps; or it can *respire*, oxidizing the sugar completely and passing the electrons down a membrane-bound chain to an external acceptor, with most ATP made by ATP synthase. The biochemistry of glycolysis, the citric acid cycle and oxidative phosphorylation has been worked out in mitochondria and in a few model organisms and is presented in [7.1.18](/7.1.18), [7.1.20](/7.1.20) and [7.1.23](/7.1.23). What is distinctively microbial is the variety built on that common core: several ways of splitting a sugar, dozens of fermentations with different products, respiratory chains assembled from interchangeable modules, and organisms that conserve energy from reactions yielding a third of an ATP. This chapter treats energy conservation by chemoorganotrophs (7.11.4) and closes with an outline of biosynthesis; the electron donors and acceptors used by phototrophs, chemolithotrophs and anaerobic respirers are the subject of 7.11.6 and 7.11.7, which use the same principles.

## 5.1. Energy and Redox

### 5.1.1. Free Energy in Microbial Metabolism

The **bioenergetics** of [7.1.16](/7.1.16) applies unchanged: a reaction can supply energy to a cell only if its Gibbs energy change is negative. Microbiologists compute standard changes in the **biochemical standard state** (pH 7, all other species at unit activity) from free energies of formation $\Delta_{\mathrm{f}}G^\circ{}'$, "products minus reactants".

**Formula 5.1.1 (Gibbs Energy from Free Energies of Formation)** For a balanced reaction $\sum_{\mathrm{B}} \nu_{\mathrm{B}}\mathrm{B} = 0$ (stoichiometric numbers $\nu_{\mathrm{B}}$ negative for reactants),

$$
\Delta_{\mathrm{r}}G^\circ{}' = \sum_{\mathrm{B}} \nu_{\mathrm{B}}\,\Delta_{\mathrm{f}}G^\circ{}'(\mathrm{B}).
$$

**Example 5.1.1** With the values compiled by Thauer, Jungermann and Decker (1977) ($\Delta_{\mathrm{f}}G^\circ{}'$ in $\mathrm{kJ\,mol^{-1}}$: glucose −917.2, lactate⁻ −517.8, ethanol −181.7, $\ce{CO2}$(g) −394.4, $\ce{H2O}$ −237.2, $\ce{H+}$ at pH 7 −39.8), the three ways of degrading glucose compare as follows:

| Reaction | $\Delta_{\mathrm{r}}G^\circ{}'$ / ($\mathrm{kJ\,mol^{-1}}$ glucose) |
|---|---|
| glucose → 2 lactate⁻ + 2 $\ce{H+}$ | $2(-517.8) + 2(-39.8) + 917.2 = -198$ |
| glucose → 2 ethanol + 2 $\ce{CO2}$ | $2(-181.7) + 2(-394.4) + 917.2 = -235$ |
| glucose + 6 $\ce{O2}$ → 6 $\ce{CO2}$ + 6 $\ce{H2O}$ | $6(-394.4) + 6(-237.2) + 917.2 = -2872$ |

:::

Fermentation releases less than a tenth of the energy available from respiration, because its products, lactate and ethanol, are still highly reduced.

The actual $\Delta_{\mathrm{r}}G$ in a habitat depends on the concentrations ([Formula 16.2.1](/7.1.16#fml-16.2.1)). Usually the correction is modest, but for reactions that produce $\ce{H2}$ it is decisive: hydrogen-consuming organisms keep its partial pressure so low that reactions endergonic under standard conditions become exergonic. This is the basis of **syntrophy** (7.11.7).

### 5.1.2. Reduction Potentials and the Redox Tower

Every energy-conserving reaction of a chemotroph is an oxidation–reduction reaction between an electron donor and an electron acceptor. Each half-reaction is characterized by the reduction potential of its **redox couple** at pH 7, $E^\circ{}'$ (written oxidized form/reduced form; [7.1.16](/7.1.16#sec-16.4.3)). The more negative $E^\circ{}'$, the stronger the reduced form as a donor; the more positive, the stronger the oxidized form as an acceptor.

**Formula 5.1.2 (Gibbs Energy from Reduction Potentials)** When $z$ electrons pass from a donor couple to an acceptor couple, with $\Delta E^\circ{}' = E^\circ{}'_{\mathrm{acceptor}} - E^\circ{}'_{\mathrm{donor}}$,

$$
\Delta_{\mathrm{r}}G^\circ{}' = -zF\,\Delta E^\circ{}',
$$
where $F = 96.485\,\mathrm{kJ\,mol^{-1}\,V^{-1}}$ is the Faraday constant.

**Definition 5.1.1 (Redox Tower)** The **redox tower** is the arrangement of the redox couples used in metabolism by their reduction potentials, the most negative (strongest donors) at the top and the most positive (strongest acceptors) at the bottom. The farther electrons "fall" from a donor to the acceptor that catches them, the more energy the reaction releases.

![The redox tower: reduction potentials E°′ at pH 7 of redox couples used in microbial energy metabolism, from CO₂/glucose and 2H⁺/H₂ at the top to ½O₂/H₂O at the bottom (number of electrons in parentheses). Couples used mainly as electron donors are on the left, couples used mainly as electron acceptors on the right; the cellular carriers NAD⁺/NADH, menaquinone, ubiquinone and cytochrome c are marked. Right: the Gibbs energy released when H₂ (z = 2 per H₂) reduces different acceptors, from Formula 5.1.2. Values from Thauer et al. (1977) and Madigan et al. (2019).](./plots/redox-tower.py)

**Example 5.1.2** Hydrogen ($E^\circ{}' = -0.414\,\mathrm{V}$) can be oxidized by several acceptors. Per $\ce{H2}$ ($z = 2$): with $\ce{O2}$ ($+0.816\,\mathrm{V}$), $\Delta E^\circ{}' = 1.230\,\mathrm{V}$ and $\Delta_{\mathrm{r}}G^\circ{}' = -237\,\mathrm{kJ}$; with nitrate reduced to nitrite ($+0.43\,\mathrm{V}$), $-163\,\mathrm{kJ}$; with fumarate ($+0.03\,\mathrm{V}$), $-86\,\mathrm{kJ}$; with sulfate reduced to sulfide ($-0.22\,\mathrm{V}$), $-38\,\mathrm{kJ}$; with $\ce{CO2}$ reduced to methane ($-0.24\,\mathrm{V}$), $-33\,\mathrm{kJ}$. Per molecule of acceptor the last two are larger ($-152$ and $-131\,\mathrm{kJ}$ for four $\ce{H2}$), but per electron they are small, which is why sulfate reducers and methanogens make little ATP per electron pair (7.11.7). The complete oxidation of acetate by $\ce{O2}$ ($\ce{CH3COO- + H+ + 2O2 -> 2CO2 + 2H2O}$, $z = 8$, $E^\circ{}'(\ce{CO2}/\text{acetate}) = -0.29\,\mathrm{V}$) gives $-8 \times 96.485 \times 1.106 = -854\,\mathrm{kJ}$, in agreement with $-854\,\mathrm{kJ}$ from free energies of formation.

:::

The tower organizes the whole of microbial metabolism. Chemoorganotrophy and chemolithotrophy differ in the donor near the top; aerobic and anaerobic respiration differ in the acceptor near the bottom; fermentation is the case in which the donor and the acceptor are both derived from the substrate. Wherever a donor and an acceptor that are far enough apart meet, some microorganism usually exploits the gap.

### 5.1.3. Electron Carriers

Inside the cell, electrons travel between enzymes on a few carriers ([7.1.16](/7.1.16#sec-16.5.1)). $\ce{NAD+}$/NADH ($-0.32\,\mathrm{V}$) serves catabolism and $\ce{NADP+}$/NADPH biosynthesis. Flavins (FAD, FMN) are bound to proteins and transfer one or two electrons. Two carriers are especially important in microorganisms. *Ferredoxins*, small iron–sulfur proteins with potentials near $-0.4\,\mathrm{V}$ or lower, are reduced in many anaerobic oxidations (of pyruvate, for example) and can reduce protons to $\ce{H2}$ through hydrogenases, a reaction NADH cannot drive at ordinary hydrogen pressures. Anaerobes make reduced ferredoxin from NADH by *flavin-based electron bifurcation*, in which an enzyme splits an electron pair from NADH, sending one electron uphill to ferredoxin and the other downhill to a high-potential acceptor such as crotonyl-CoA, so that the overall reaction is exergonic. Second, membrane **quinones** carry electrons and protons between the complexes of respiratory chains: **ubiquinone** ($E^\circ{}' \approx +0.11\,\mathrm{V}$) in aerobic respiration, and menaquinone ($E^\circ{}' \approx -0.07\,\mathrm{V}$), which can reduce low-potential acceptors such as fumarate, in anaerobic respiration and in Gram-positive bacteria.

### 5.1.4. Energy-Rich Compounds and Storage

Energy released in catabolism is conserved in **high-energy compounds** ([7.1.16](/7.1.16#sec-16.3.3)), whose group transfer to ADP makes ATP by **substrate-level phosphorylation**. In glycolysis these are 1,3-bisphosphoglycerate and phosphoenolpyruvate. Anaerobes add a second family: acyl **thioesters** of coenzyme A (acetyl-CoA, butyryl-CoA, succinyl-CoA) and the acyl phosphates derived from them. The pair of enzymes phosphotransacetylase (acetyl-CoA + $\mathrm{P_i}$ → acetyl phosphate + CoA) and acetate kinase (acetyl phosphate + ADP → acetate + ATP) turns every acetyl-CoA that a fermenter excretes as acetate into one ATP; butyrate is made in the same way through butyryl phosphate. Because of this, the formation of an acid instead of an alcohol is worth one extra ATP to an anaerobe, a theme that recurs through Section 5.3.

For long-term storage, prokaryotes accumulate insoluble polymers as cytoplasmic inclusions (7.11.2): **glycogen**, **polyhydroxybutyrate** and other polyhydroxyalkanoates when carbon is in excess and another nutrient is limiting, polyphosphate, and elemental sulfur in sulfur-oxidizing bacteria. They are mobilized in starvation to supply the small maintenance energy needed to stay alive without growing.

## 5.2. Many Ways to Split a Sugar

### 5.2.1. Glycolysis

The Embden–Meyerhof–Parnas pathway, **glycolysis** ([7.1.18](/7.1.18)), converts glucose to two pyruvate with a net gain of 2 ATP and 2 NADH. It is used by most bacteria, by fungi and by animals, and it is the starting point of most of the fermentations below. In bacteria, glucose often enters it as glucose 6-phosphate delivered by the phosphotransferase system (7.11.4), which saves the hexokinase step. It is not, however, the only way to split a hexose, and in many bacteria and archaea it is not the main one.

### 5.2.2. The Entner–Doudoroff Pathway

**Definition 5.2.1 (Entner–Doudoroff Pathway)** The **Entner–Doudoroff pathway** (ED pathway, KDPG pathway) converts glucose 6-phosphate to two pyruvate through 6-phosphogluconate and 2-keto-3-deoxy-6-phosphogluconate (KDPG). Glucose 6-phosphate is oxidized by glucose-6-phosphate dehydrogenase to 6-phosphogluconate, generating NADPH; 6-phosphogluconate dehydratase (Edd) removes water to form KDPG; and KDPG aldolase (Eda) cleaves KDPG into pyruvate and glyceraldehyde 3-phosphate, which the lower steps of glycolysis oxidize to a second pyruvate.

Only one of the two C₃ units passes through the ATP-generating steps of glycolysis, so the yield is 1 ATP, 1 NADH and 1 NADPH per glucose, half the ATP of glycolysis. Named after Nathan Entner and Michael Doudoroff, who described it in *Pseudomonas saccharophila* in 1952, the pathway is the main route of glucose catabolism in *Pseudomonas*, many of which lack phosphofructokinase, in *Azotobacter* and *Zymomonas*, and in many other Gram-negative bacteria; *E. coli* uses it for gluconate. Modified forms are widespread in archaea (Section 5.2.5), and it is also active in cyanobacteria and plants. Its lower ATP yield is offset by a lower protein cost: computations of the amount of enzyme needed to carry a given flux show that the ED pathway needs several times less enzyme protein than glycolysis, because its steps are fewer and thermodynamically more favorable. Organisms for which ATP is not limiting, such as aerobes that make most of their ATP by respiration, can therefore profit from it.

### 5.2.3. The Pentose Phosphate Pathway

The **pentose phosphate pathway** ([7.1.18](/7.1.18#sec-18.6)) oxidizes glucose 6-phosphate to ribulose 5-phosphate and $\ce{CO2}$ with 2 NADPH, and rearranges sugar phosphates in its nonoxidative phase. In microorganisms as in animals its main roles are biosynthetic: NADPH for reductive biosyntheses, ribose 5-phosphate for nucleotides and erythrose 4-phosphate for aromatic amino acids. Pentoses taken up as nutrients (xylose, arabinose, ribose) enter metabolism through it. Its oxidative steps are shared with the ED and phosphoketolase pathways, which branch from 6-phosphogluconate.

### 5.2.4. The Phosphoketolase Pathways

**Definition 5.2.2 (Phosphoketolase Pathway)** A **phosphoketolase pathway** is a route of sugar catabolism in which a phosphoketolase cleaves a ketose phosphate with inorganic phosphate into acetyl phosphate and a shorter sugar phosphate: xylulose 5-phosphate into acetyl phosphate and glyceraldehyde 3-phosphate (in heterofermentative lactic acid bacteria), or fructose 6-phosphate into acetyl phosphate and erythrose 4-phosphate (in bifidobacteria).

In the heterofermentative pathway (also called the phosphogluconate pathway), glucose 6-phosphate is oxidized and decarboxylated as in the pentose phosphate pathway to ribulose 5-phosphate (2 NAD(P)H and $\ce{CO2}$), which is epimerized to xylulose 5-phosphate and split by phosphoketolase. Glyceraldehyde 3-phosphate goes down the lower glycolytic steps (2 ATP, 1 NADH) to pyruvate, which is reduced to lactate; acetyl phosphate is reduced through acetyl-CoA and acetaldehyde to ethanol, consuming 2 NADH. The balance is

$$
\text{glucose} \to \text{lactate}^- + \text{ethanol} + \ce{CO2} + \ce{H+}, \qquad 1\ \text{ATP per glucose}.
$$
If an external electron acceptor is available, such as $\ce{O2}$ or fructose (reduced to mannitol by *Leuconostoc*), the NADH can be reoxidized without making ethanol and the acetyl phosphate yields a second ATP as acetate.

The bifidobacteria use a different phosphoketolase arrangement, the *bifid shunt*. Of two fructose 6-phosphate, one is split into acetyl phosphate and erythrose 4-phosphate; transaldolase and transketolase combine the erythrose 4-phosphate with the second fructose 6-phosphate to form two pentose phosphates, which a second phosphoketolase reaction splits into two acetyl phosphate and two glyceraldehyde 3-phosphate. The balance is

$$
2\ \text{glucose} \to 3\ \text{acetate}^- + 2\ \text{lactate}^- + 5\ \ce{H+}, \qquad 2.5\ \text{ATP per glucose},
$$
more than either homolactic or heterolactic fermentation. The bifid shunt is a diagnostic trait of *Bifidobacterium*, an abundant genus in the gut of breast-fed infants (7.11.32).

![Four routes from glucose to pyruvate or its products. A: glycolysis (Embden–Meyerhof–Parnas). B: the Entner–Doudoroff pathway, with the key intermediate KDPG split into pyruvate and glyceraldehyde 3-phosphate. C: the oxidative pentose phosphate pathway, mainly a source of NADPH and pentoses. D: the heterofermentative phosphoketolase pathway, ending in lactate, ethanol and CO₂. The net yield per glucose (bottom of each panel) differs: glycolysis 2 ATP and 2 NADH; ED 1 ATP, 1 NADH and 1 NADPH; oxidative PPP 2 NADPH per glucose 6-phosphate oxidized (and 1 ATP spent on phosphorylation); phosphoketolase 1 ATP.](./plots/glucose-pathways.py)

### 5.2.5. Sugar Catabolism in Archaea

Archaea that grow on sugars use modified versions of these pathways, with enzymes unrelated to those of bacteria and eukaryotes. The hyperthermophile *Pyrococcus furiosus* runs a modified glycolysis in which glucokinase and phosphofructokinase use ADP instead of ATP, and glyceraldehyde 3-phosphate is oxidized directly to 3-phosphoglycerate by a ferredoxin-dependent oxidoreductase (GAPOR), bypassing 1,3-bisphosphoglycerate and therefore the ATP-generating phosphoglycerate kinase step. The energy is conserved instead in reduced ferredoxin, which drives a membrane-bound hydrogenase that pumps ions, and in the conversion of acetyl-CoA to acetate. Many Thermoproteota (formerly Crenarchaeota), such as *Sulfolobus*, and haloarchaea use branched forms of the ED pathway, a semiphosphorylative one in which KDG (2-keto-3-deoxygluconate) is phosphorylated only after the dehydration, and a nonphosphorylative one in which no phosphorylated intermediate appears before glycerate. That the most basic carbohydrate metabolism differs between the domains is one more line of evidence for their deep separation ([7.10.27](/7.10.27)).

## 5.3. Fermentation

### 5.3.1. Principles

A **fermentation** ([7.1.18](/7.1.18#sec-18.4.1)) is an anaerobic catabolism in which an organic compound serves as both electron donor and electron acceptor, so that no external acceptor is needed, and ATP is made by **substrate-level phosphorylation**. Three constraints shape every fermentation:

1. *Redox balance.* The NADH (or reduced ferredoxin) formed in the oxidative steps must be reoxidized by reducing intermediates of the same pathway, which are excreted as reduced products: lactate, ethanol, butyrate, butanol, succinate. Alternatively, electrons can be released as $\ce{H2}$ by hydrogenases from reduced ferredoxin, or from formate by formate hydrogenlyase. The total oxidation state of the products must equal that of the substrate.
2. *ATP yield.* ATP comes only from energy-rich intermediates; making an acid (acetate, butyrate) from its CoA thioester gives an extra ATP, making the corresponding alcohol gives none.
3. *Carbon and electron bookkeeping.* Each fermentation is a compromise between these two: more acid means more ATP, but the electrons must still go somewhere, so the product ratio shifts with conditions such as pH and hydrogen partial pressure.

Fermentations are named after their main products or, for unusual substrates, after the substrate. Most of their products, the acids and alcohols of food and industry, are waste for the organism but valuable to people.

![Fermentation products formed from pyruvate (and from phosphoenolpyruvate for succinate), colored by the group of organisms that makes them: lactic acid bacteria (lactate), yeasts and *Zymomonas* (ethanol and CO₂ by pyruvate decarboxylase), enteric bacteria (formate, H₂ and CO₂ by pyruvate formate-lyase and formate hydrogenlyase; acetate, ethanol, succinate; acetoin and 2,3-butanediol in *Klebsiella* and *Enterobacter*), clostridia (acetyl-CoA, CO₂ and H₂ by pyruvate:ferredoxin oxidoreductase; butyrate, butanol, acetone) and propionibacteria (propionate). Arrows marked ATP are steps of substrate-level phosphorylation; NADH marks steps that reoxidize NADH.](./plots/fermentation-products.py)

### 5.3.2. Lactic Acid Fermentations

The lactic acid bacteria, Gram-positive, aerotolerant, nonsporulating fermenters of the order Lactobacillales (7.11.18), have two patterns of **lactic acid fermentation**. *Homofermentative* species (*Lactococcus*, *Streptococcus*, *Lactobacillus delbrueckii* of yogurt) use glycolysis and reduce all pyruvate to lactate: glucose → 2 lactate, 2 ATP. *Heterofermentative* species (*Leuconostoc*, and obligately heterofermentative species formerly placed in *Lactobacillus*, such as *Limosilactobacillus reuteri*) lack aldolase and use the phosphoketolase pathway: glucose → lactate + ethanol + $\ce{CO2}$, 1 ATP. Production of gas from glucose, seen as a bubble in an inverted (Durham) tube in the broth, distinguishes the two. In 2020 the old genus *Lactobacillus*, which had become phylogenetically far too broad, was split into 25 genera; names such as *Lactiplantibacillus plantarum* (formerly *Lactobacillus plantarum*) are now standard.

### 5.3.3. Alcoholic Fermentation

In yeast, **alcoholic fermentation** ([7.1.18](/7.1.18#sec-18.4.3)) follows glycolysis with pyruvate decarboxylase and alcohol dehydrogenase: glucose → 2 ethanol + 2 $\ce{CO2}$, 2 ATP. *Saccharomyces cerevisiae* is Crabtree-positive: at high glucose concentrations it ferments even in the presence of oxygen, an instance of **overflow metabolism** ([7.6.39](/7.6.39#sec-39.4)), and respires mainly when glucose is scarce; the **Pasteur effect** ([7.1.18](/7.1.18#sec-18.4.4)), the suppression of fermentation by oxygen, is therefore seen in this yeast only at low sugar concentrations. Among bacteria, *Zymomonas mobilis*, the fermenter of the Mexican agave drink pulque, makes ethanol by the ED pathway with the same two final enzymes: glucose → 2 ethanol + 2 $\ce{CO2}$, but only 1 ATP. It compensates with an extremely high rate of glucose consumption and a high ethanol yield, because little sugar is diverted into biomass, which has made it a candidate organism for bioethanol production.

### 5.3.4. Mixed-Acid and Butanediol Fermentations

The enteric bacteria (Enterobacterales, 7.11.17), facultative anaerobes, ferment sugars by glycolysis followed by a branched set of reactions.

**Definition 5.3.1 (Mixed-Acid Fermentation)** **Mixed-acid fermentation** is the fermentation of sugars by *Escherichia*, *Salmonella*, *Shigella* and related enteric bacteria to a mixture of acids (acetate, lactate, succinate, formate) together with ethanol, $\ce{CO2}$ and $\ce{H2}$. Pyruvate is cleaved by pyruvate formate-lyase to acetyl-CoA and formate; formate is split by formate hydrogenlyase into equal amounts of $\ce{H2}$ and $\ce{CO2}$; acetyl-CoA is converted to acetate (with ATP) or reduced to ethanol; and part of the phosphoenolpyruvate is carboxylated to oxaloacetate and reduced through fumarate to succinate.

The proportions vary, but the acids typically lower the pH of a glucose broth below 4.4, where the indicator methyl red turns red: the methyl red test. Redox balance links the products: for every acetyl-CoA converted to acetate (gaining an ATP), another must be reduced to ethanol (consuming 2 NADH) to reoxidize the NADH from glycolysis.

**Definition 5.3.2 (Butanediol Fermentation)** **Butanediol fermentation** is a variant of mixed-acid fermentation, in *Klebsiella*, *Enterobacter* and *Serratia*, in which much of the pyruvate is converted to the neutral product 2,3-butanediol: two pyruvate are condensed by α-acetolactate synthase to α-acetolactate (releasing $\ce{CO2}$), which is decarboxylated to acetoin and reduced by NADH to 2,3-butanediol.

Because two pyruvate (from one glucose, with 2 NADH) yield one butanediol with only one NADH consumed, butanediol producers must reduce more acetyl-CoA to ethanol, and they release considerably more $\ce{CO2}$ than $\ce{H2}$; they acidify the medium less, so they are methyl red negative. Their intermediate acetoin is detected by the Voges–Proskauer test, a red color with α-naphthol and KOH. The two tests separate *E. coli* (methyl red positive, Voges–Proskauer negative) from *Klebsiella aerogenes* (formerly *Enterobacter aerogenes*; methyl red negative, Voges–Proskauer positive), and are part of the IMViC panel used in identification (7.11.16).

| Feature | Mixed-acid (*E. coli*) | Butanediol (*K. aerogenes*) |
|---|---|---|
| Main products | acetate, lactate, succinate, formate, ethanol | 2,3-butanediol, ethanol |
| $\ce{CO2}$ : $\ce{H2}$ | about 1 : 1 (from formate) | $\ce{CO2}$ in excess |
| Final pH of glucose broth | below 4.4 | about 6 |
| Methyl red / Voges–Proskauer | + / − | − / + |

### 5.3.5. Clostridial Fermentations

Species of *Clostridium*, obligately anaerobic endospore formers (7.11.18), ferment sugars, amino acids, purines and other substrates. The saccharolytic clostridia use glycolysis and then oxidize pyruvate with pyruvate:ferredoxin oxidoreductase to acetyl-CoA, $\ce{CO2}$ and reduced ferredoxin, from which hydrogenase releases $\ce{H2}$ (the phosphoroclastic reaction). Two acetyl-CoA are condensed to acetoacetyl-CoA and reduced by NADH through crotonyl-CoA to butyryl-CoA, which yields butyrate and ATP through butyryl phosphate. *Clostridium butyricum* carries out

$$
\text{glucose} \to \text{butyrate}^- + 2\ \ce{CO2} + 2\ \ce{H2} + \ce{H+}, \qquad \Delta_{\mathrm{r}}G^\circ{}' = -264\,\mathrm{kJ},\ 3\ \text{ATP}.
$$

*Clostridium acetobutylicum* shows that the products are a regulated choice. In an early acidogenic phase it makes butyrate and acetate, gaining ATP; when the pH falls to about 5, it switches to a solventogenic phase, reabsorbs part of the acids and makes acetone, butanol and some ethanol. Neutral products protect the cell from acid but cost ATP, because butyryl-CoA reduced to butanol does not pass through butyryl phosphate. This acetone–butanol–ethanol fermentation supplied acetone for explosives in the First World War, when Chaim Weizmann developed it on an industrial scale.

The proteolytic clostridia, which decompose proteins in anoxic environments, ferment amino acids. Some ferment single amino acids; others couple the oxidation of one amino acid to the reduction of another in the *Stickland reaction*. In *Clostridium sporogenes*, alanine is the electron donor and glycine the acceptor:

$$
\text{alanine} + 2\ \text{glycine} + 2\ \ce{H2O} \to 3\ \text{acetate}^- + 3\ \ce{NH4+} + \ce{CO2}, \qquad \Delta_{\mathrm{r}}G^\circ{}' = -135\,\mathrm{kJ}.
$$
ATP is made from acetyl phosphate in both the oxidative and the reductive branch; glycine reductase is a selenoprotein, one of the reasons some clostridia require selenium. The foul smells of putrefaction, hydrogen sulfide, methanethiol, cadaverine and putrescine, are by-products of such fermentations. *Clostridium kluyveri* performs a *secondary fermentation* of two common fermentation products: it oxidizes ethanol and uses acetate as the acceptor, elongating it to butyrate and caproate (6 ethanol + 3 acetate⁻ → 3 butyrate⁻ + caproate⁻ + 2 $\ce{H2}$ + 4 $\ce{H2O}$ + $\ce{H+}$), with about 1 ATP per 6 ethanol; flavin-based electron bifurcation was discovered in this organism.

### 5.3.6. Propionic Acid Fermentation

*Propionibacterium* ferments lactate, the product of lactic acid bacteria with which it lives in cheese and in the rumen:

$$
3\ \text{lactate}^- \to 2\ \text{propionate}^- + \text{acetate}^- + \ce{CO2} + \ce{H2O}, \qquad \Delta_{\mathrm{r}}G^\circ{}' = -171\,\mathrm{kJ}.
$$
One lactate is oxidized to acetate and $\ce{CO2}$, giving 1 ATP by substrate-level phosphorylation; two are oxidized to pyruvate and reduced to propionate by the methylmalonyl-CoA pathway, in which a biotin-dependent transcarboxylase moves a carboxyl group from methylmalonyl-CoA to pyruvate, oxaloacetate is reduced through malate and fumarate to succinate, and **methylmalonyl-CoA mutase**, a coenzyme $\mathrm{B_{12}}$ enzyme, converts succinyl-CoA back to methylmalonyl-CoA. The reduction of fumarate is catalyzed by a membrane-bound fumarate reductase that generates a proton-motive force, so this fermentation combines substrate-level phosphorylation with a small amount of electron-transport phosphorylation. In Emmental cheese, the propionate and acetate contribute the flavor and the $\ce{CO2}$ forms the holes. (*Anaerotignum propionicum*, formerly *Clostridium propionicum*, reaches propionate by a different route, through acrylyl-CoA.)

### 5.3.7. Fermentations Without Substrate-Level Phosphorylation

A few fermentations release too little energy to form an energy-rich phosphate bond, yet support growth. *Propionigenium modestum*, a marine anaerobe of the phylum Fusobacteriota, ferments succinate:

$$
\text{succinate}^{2-} + \ce{H2O} \to \text{propionate}^- + \ce{HCO3-}, \qquad \Delta_{\mathrm{r}}G^\circ{}' = -20.5\,\mathrm{kJ}.
$$
The decarboxylation of methylmalonyl-CoA in this pathway is catalyzed by a membrane-bound decarboxylase that pumps $\ce{Na+}$ out of the cell, and a $\ce{Na+}$-translocating ATP synthase uses the resulting sodium-motive force to make ATP. *Oxalobacter formigenes*, a gut bacterium that degrades dietary oxalate, decarboxylates oxalate to formate ($\Delta_{\mathrm{r}}G^\circ{}' = -26.7\,\mathrm{kJ}$); an antiporter exchanges external oxalate²⁻ for internal formate⁻, so each turn moves one negative charge inward, and the decarboxylation consumes a cytoplasmic proton. The net effect is an electrochemical proton gradient that drives ATP synthase, with no proton pump at all.

These organisms show that the unit of energy conservation is not one ATP but one ion translocated: a reaction that releases enough energy to move a fraction of the four or so ions needed per ATP can be coupled to ATP synthesis through a membrane gradient. The minimum free energy that can sustain life in this way has been estimated at roughly $-10$ to $-20\,\mathrm{kJ\,mol^{-1}}$ per reaction, and the syntrophs of 7.11.7 live close to it.

## 5.4. Respiration

### 5.4.1. Respiratory Chains in Prokaryotes

In **cellular respiration** ([7.1.20](/7.1.20#sec-20.1.1)) electrons from the substrate pass through a **respiratory chain** to an external terminal acceptor, and the chain translocates protons, generating the **proton-motive force** that **ATP synthase** uses to make ATP (**oxidative phosphorylation**, [7.1.23](/7.1.23)). Prokaryotic chains are built from the same kinds of components as mitochondrial ones, NADH dehydrogenases, flavoproteins, iron–sulfur proteins, **quinones** and **cytochromes**, but they differ in three ways:

- They lie in the cytoplasmic membrane (or in intracytoplasmic membranes), and protons are pumped from the cytoplasm to the periplasm or the outside.
- They are modular and branched. A cell has several dehydrogenases that feed electrons from different donors into a common quinone pool, and several terminal enzymes that take electrons from the pool to different acceptors. Which modules are made depends on the conditions.
- Many lack parts of the mitochondrial chain. *Paracoccus denitrificans*, a member of the Alphaproteobacteria, the group from which mitochondria descend, has a chain with Complexes I–IV much like that of mitochondria; *E. coli* has no cytochrome $bc_1$ complex and no cytochrome $c$ in its aerobic chain, and its quinol oxidases take electrons directly from the quinone pool.

### 5.4.2. The Branched Respiratory Chain of *Escherichia coli*

The aerobic chain of *E. coli* has two NADH dehydrogenases and two main terminal oxidases:

- NADH dehydrogenase I (NDH-1, encoded by the *nuo* operon) is a homolog of **Complex I** ([7.1.23](/7.1.23#sec-23.1.4)) and pumps 4 $\ce{H+}$ per 2 e⁻. NADH dehydrogenase II (NDH-2) is a single flavoprotein that transfers electrons to quinone without pumping. Succinate dehydrogenase (Complex II) and other dehydrogenases (for lactate, glycerol 3-phosphate, formate, $\ce{H2}$) also reduce the quinone pool.
- The quinone pool contains ubiquinone-8 under aerobic conditions and menaquinone-8 and demethylmenaquinone under anaerobic conditions.
- Cytochrome $bo_3$ ubiquinol oxidase (*cyo*), a heme–copper oxidase related to mitochondrial Complex IV, has a relatively low affinity for $\ce{O2}$ and translocates 2 $\ce{H+}$ per electron (one by pumping, one by taking up the protons for water from the cytoplasm while the protons of quinol are released outside), that is 4 $\ce{H+}$ per 2 e⁻. Cytochrome $bd$-I oxidase (*cyd*), unrelated to the heme–copper family, does not pump and translocates 1 $\ce{H+}$ per electron, but it has a very high affinity for $\ce{O2}$, works at nanomolar oxygen, and is relatively insensitive to cyanide and nitric oxide.

**Definition 5.4.1 (Terminal Oxidase)** A **terminal oxidase** is the last enzyme of an aerobic respiratory chain, which takes electrons from cytochrome $c$ (cytochrome $c$ oxidases) or directly from quinol (quinol oxidases) and reduces $\ce{O2}$ to water.

![The branched aerobic respiratory chain of *E. coli* in the cytoplasmic membrane (periplasm on top). Electrons (blue) from NADH enter the quinone pool (Q) through the proton-pumping NADH dehydrogenase I (NDH-1) or the nonpumping NADH dehydrogenase II (NDH-2); succinate dehydrogenase (SDH) and other dehydrogenases feed the same pool. From quinol, electrons go to O₂ through cytochrome bo₃ (low O₂ affinity, 4 H⁺ per 2 e⁻) or cytochrome bd (high O₂ affinity, 2 H⁺ per 2 e⁻). Protons translocated (red) per pair of electrons from NADH range from 8 (NDH-1 with bo₃) to 2 (NDH-2 with bd). Under anoxic conditions, menaquinone and terminal reductases for nitrate or fumarate replace the oxidases (dashed).](./plots/ecoli-respiratory-chain.py)

The combinations give a fourfold range of energy conservation:

| Route from NADH to $\ce{O2}$ | $\ce{H+}$ per 2 e⁻ | Used when |
|---|---|---|
| NDH-1 + cytochrome $bo_3$ | 8 | oxygen plentiful, energy-limited growth |
| NDH-1 + cytochrome $bd$ | 6 | microaerobic conditions |
| NDH-2 + cytochrome $bo_3$ | 4 | |
| NDH-2 + cytochrome $bd$ | 2 | fast growth on rich media, high flux |

The low-yield routes are not waste. NDH-2 and cytochrome $bd$ carry high fluxes with little protein and keep NADH turning over when the cell is limited by the rate of catabolism rather than by energy, and cytochrome $bd$ scavenges oxygen at concentrations where $bo_3$ fails, which also protects oxygen-sensitive enzymes. The global regulators ArcB–ArcA (ArcB senses the redox state of the quinone pool) and FNR (an oxygen-sensitive transcription factor with an Fe–S cluster) switch the operons as oxygen falls (7.11.11). When oxygen is absent, the same quinone pool delivers electrons to terminal reductases for nitrate, fumarate, dimethyl sulfoxide or trimethylamine $N$-oxide. This is **anaerobic respiration**:

**Definition 5.4.2 (Anaerobic Respiration)** **Anaerobic respiration** is respiration in which an electron acceptor other than $\ce{O2}$, inorganic (nitrate, nitrite, ferric iron, sulfate, $\ce{CO2}$ and others) or organic (fumarate, dimethyl sulfoxide), is reduced at the end of a membrane-bound electron transport chain that generates a proton-motive force.

Because every alternative acceptor lies higher on the redox tower than $\ce{O2}$, less energy is conserved per electron pair; *E. coli* uses acceptors in the order $\ce{O2}$ > nitrate > fumarate > fermentation, which is the order of their energy yields. The diversity of anaerobic respiration, including denitrification, sulfate reduction, iron reduction and methanogenesis, is treated in 7.11.7.

### 5.4.3. The Proton-Motive Force and ATP Synthase

The proton-motive force across the bacterial membrane ([7.1.23](/7.1.23#sec-23.2.2)), written as a potential, is

$$
\Delta p = \Delta\varphi - \frac{2.303\,RT}{F}\,\Delta\mathrm{pH},
$$
inside relative to outside. In respiring *E. coli* $\Delta p$ is about $-0.15$ to $-0.20\,\mathrm{V}$, mostly as the membrane potential; alkaliphiles keep their cytoplasm less alkaline than the medium and so must work with an unfavorable $\Delta\mathrm{pH}$ (7.11.9). Unlike in mitochondria, the bacterial proton-motive force powers not only ATP synthesis but also most nutrient uptake (7.11.4), the rotation of the flagellar motor ([7.6.28](/7.6.28)) and the export of drugs and protons. Strict fermenters, which have no respiratory chain, still have ATP synthase: they run it in reverse, hydrolyzing ATP from substrate-level phosphorylation to generate the proton-motive force their transporters and flagella need.

The ATP synthase of *E. coli* has 10 c subunits in its rotor ring, so by [Formula 23.3.1](/7.1.23#fml-23.3.1) it needs about $10/3 \approx 3.3$ protons per ATP (no adenine nucleotide translocase is needed, because ATP is made in the cytoplasm). Some bacteria and archaea use $\ce{Na+}$ instead of $\ce{H+}$: *Vibrio* species have a sodium-pumping NADH:quinone oxidoreductase (Na⁺-NQR) and sodium-driven flagella, and *Propionigenium* and many anaerobes have $\ce{Na+}$-translocating ATP synthases.

### 5.4.4. The Citric Acid and Glyoxylate Cycles

The **citric acid cycle** ([7.1.20](/7.1.20)) oxidizes acetyl-CoA to $\ce{CO2}$ in the cytoplasm of bacteria, producing per acetyl unit 3 NAD(P)H, one reduced quinone (from succinate) and one ATP or GTP. In microorganisms it serves two roles that can be separated. Under aerobic conditions it runs as a cycle; under anaerobic conditions many facultative anaerobes, including *E. coli*, run it as two branches, an oxidative branch from citrate to 2-oxoglutarate and a reductive branch from oxaloacetate through fumarate to succinate, which supply biosynthetic precursors without the need to reoxidize much NADH. As an **amphibolic pathway** its intermediates are drained for biosynthesis and must be replenished by **anaplerotic reactions**, the carboxylation of phosphoenolpyruvate (PEP carboxylase) or pyruvate (pyruvate carboxylase).

Growth on acetate or fatty acids, which enter metabolism as acetyl-CoA, requires the **glyoxylate cycle** ([7.1.20](/7.1.20#sec-20.5)): isocitrate lyase splits isocitrate into succinate and glyoxylate, and malate synthase condenses glyoxylate with acetyl-CoA, so that the two decarboxylations of the cycle are bypassed and C₂ units are converted to C₄ compounds for biosynthesis. In *E. coli* the partition of isocitrate between the two cycles is controlled by phosphorylation of isocitrate dehydrogenase. *Mycobacterium tuberculosis* depends on isocitrate lyase to persist in host tissues, where it lives on host fatty acids, which makes the glyoxylate cycle a drug target (7.11.14).

### 5.4.5. Energy Yields Compared

Per glucose oxidized completely through glycolysis and the citric acid cycle, a bacterium obtains 4 ATP by substrate-level phosphorylation and about 10 NAD(P)H and 2 reduced quinones. How much more ATP the respiratory chain makes depends on its composition:

**Example 5.4.1** For *E. coli* with NDH-1 and cytochrome $bo_3$, the 10 NADH translocate $10 \times 8 = 80$ protons and the 2 quinols from succinate $2 \times 4 = 8$, in total 88; at 3.3 protons per ATP this gives about 26 ATP, or about 30 ATP per glucose in all. With NDH-2 and cytochrome $bd$, the protons are $10 \times 2 + 2 \times 2 = 24$, about 7 ATP from the chain and 11 in all. A mitochondrion, with a P/O ratio of about 2.5 for NADH and 1.5 for succinate ([7.1.23](/7.1.23#sec-23.3.5)), makes about 30–32 ATP per glucose. The figure of 38 ATP per glucose found in older textbooks assumed integral P/O ratios of 3 and 2, which are not observed.

:::

![ATP made per glucose by different modes of energy metabolism (theoretical values from the pathway stoichiometries in this chapter). Fermentations by substrate-level phosphorylation yield 1–3 ATP: heterolactic (1), ethanol by *Zymomonas* through the ED pathway (1), homolactic (2), ethanol by yeast (2), bifid shunt (2.5), butyrate (3). Aerobic respiration by *E. coli* yields about 11 (NDH-2 + bd) to 30 ATP (NDH-1 + bo₃); mitochondria about 32. Respiratory yields assume 3.3 H⁺ per ATP for *E. coli* and P/O ratios of 2.5 and 1.5 for mitochondria; actual values are lower because part of the proton-motive force is spent on transport and leaks.](./plots/atp-yields.py)

The order of magnitude, one or two ATP for fermentation and tens for respiration, explains why fermenters must process far more substrate per unit of biomass and why they excrete so much product. It also explains the preference of facultative anaerobes for respiration when an acceptor is available, and the **diauxic growth** of cells on mixtures of substrates when catabolite control is involved (7.11.4). But the faster pathway is not always the higher-yield one: when growth is limited by the protein the cell can devote to catabolism rather than by the energy, fermentation or low-yield respiration can support a higher growth rate, which is the explanation of overflow metabolism given in [7.6.39](/7.6.39#sec-39.4).

## 5.5. Biosynthesis in Outline

### 5.5.1. Twelve Precursor Metabolites

All of the monomers of a bacterial cell are made from a small set of intermediates of central metabolism. For *E. coli* there are twelve such precursor metabolites: glucose 6-phosphate, fructose 6-phosphate, ribose 5-phosphate, erythrose 4-phosphate, glyceraldehyde 3-phosphate, 3-phosphoglycerate, phosphoenolpyruvate, pyruvate, acetyl-CoA, 2-oxoglutarate, succinyl-CoA and oxaloacetate. Together with ATP, NADPH, ammonium and sulfide, they suffice to make every amino acid, nucleotide, sugar, lipid and cofactor. A cell growing on glucose draws them from glycolysis, the pentose phosphate pathway and the citric acid cycle; one growing on acetate makes them from acetyl-CoA by the glyoxylate cycle and **gluconeogenesis** ([7.1.19](/7.1.19)). The pathways of biosynthesis are largely those of biochemistry ([7.1.19](/7.1.19), [7.1.26](/7.1.26)–[7.1.28](/7.1.28)); what follows notes only what is special about microorganisms.

### 5.5.2. Sugars and Polysaccharides

Polysaccharides are made from sugar nucleotides. Bacteria synthesize glycogen from ADP-glucose, as plants make starch, whereas animals and fungi use UDP-glucose. UDP-glucose, UDP-$N$-acetylglucosamine and other sugar nucleotides are precursors of the cell wall, capsule and lipopolysaccharide; the assembly of **peptidoglycan** from UDP-$N$-acetylmuramyl-pentapeptide and the lipid carrier bactoprenol is described in 7.11.8, with the antibiotics that block it in 7.11.14. Deoxyribonucleotides are made from ribonucleotides by ribonucleotide reductases ([7.1.28](/7.1.28)), of which bacteria have three classes differing in their need for oxygen: anaerobes use an oxygen-sensitive class.

### 5.5.3. Amino Acids and Nucleotides

The carbon skeletons of the amino acids come from the precursor metabolites in families: glutamate (2-oxoglutarate), aspartate (oxaloacetate), serine (3-phosphoglycerate), pyruvate, the aromatic family (phosphoenolpyruvate and erythrose 4-phosphate) and histidine (ribose 5-phosphate) ([7.1.27](/7.1.27#sec-27.2.1)). Bacteria assimilate ammonium by two routes. At high ammonium concentrations, glutamate dehydrogenase aminates 2-oxoglutarate directly; at low concentrations, **glutamine synthetase** and glutamate synthase (GOGAT) together incorporate ammonium at the cost of one ATP per nitrogen, but with much higher affinity, and the activity of glutamine synthetase is regulated by covalent modification in response to the nitrogen supply (7.11.11). Nucleotides are synthesized by the same pathways as in other organisms ([7.1.28](/7.1.28)); folate synthesis from $p$-aminobenzoate, absent in humans, is the target of the sulfonamides (7.11.14).

### 5.5.4. Fatty Acids and Lipids

Bacteria synthesize fatty acids with a type II fatty acid synthase, a set of separate enzymes acting on the growing chain attached to an **acyl carrier protein**, unlike the large multifunctional type I synthase of animals and fungi ([7.1.26](/7.1.26#sec-26.1.2)). The difference makes the bacterial enzymes drug targets: isoniazid blocks the enoyl-ACP reductase InhA of *Mycobacterium tuberculosis*, and triclosan the enoyl-ACP reductase FabI of other bacteria. Bacteria adjust their fatty acids to the temperature, making more unsaturated, shorter or branched chains in the cold to keep the membrane fluid, and many Gram-positive bacteria make mainly branched iso- and anteiso-fatty acids from branched starter units. Archaea make no fatty acids for their membranes; their isoprenoid ether lipids are built from isopentenyl units (7.11.2).

## Summary

- Energy conservation is governed by $\Delta_{\mathrm{r}}G^\circ{}' = -zF\Delta E^\circ{}'$ (Formula 5.1.2) and by the actual concentrations: the farther electrons fall on the redox tower (Definition 5.1.1), the more energy they release. Glucose yields $-198\,\mathrm{kJ}$ in lactic fermentation, $-235\,\mathrm{kJ}$ in alcoholic fermentation and $-2872\,\mathrm{kJ}$ in aerobic respiration (Example 5.1.1). Ferredoxin, NAD(P)H and quinones carry electrons; acyl-CoA thioesters and acyl phosphates add ATP in anaerobes.
- Sugar-splitting pathways:

  | Pathway | Key enzyme or intermediate | Net yield per glucose | Typical users |
  |---|---|---|---|
  | Glycolysis (EMP) | phosphofructokinase, aldolase | 2 ATP, 2 NADH | most bacteria, yeasts, animals |
  | Entner–Doudoroff (Definition 5.2.1) | KDPG aldolase | 1 ATP, 1 NADH, 1 NADPH | *Pseudomonas*, *Zymomonas*, many Gram-negatives; modified in archaea |
  | Pentose phosphate | glucose-6-phosphate and 6-phosphogluconate dehydrogenases | NADPH, pentoses | all, mainly biosynthetic |
  | Phosphoketolase, heterolactic (Definition 5.2.2) | xylulose-5-phosphate phosphoketolase | 1 ATP (lactate + ethanol + $\ce{CO2}$) | *Leuconostoc*, heterofermentative lactobacilli |
  | Bifid shunt | fructose-6-phosphate phosphoketolase | 2.5 ATP (3 acetate + 2 lactate per 2 glucose) | *Bifidobacterium* |

- Fermentations:

  | Fermentation | Products | ATP | Organisms |
  |---|---|---|---|
  | Homolactic | 2 lactate | 2 per glucose | *Lactococcus*, *Streptococcus* |
  | Heterolactic | lactate, ethanol, $\ce{CO2}$ | 1 per glucose | *Leuconostoc* |
  | Alcoholic | 2 ethanol, 2 $\ce{CO2}$ | 2 (yeast), 1 (*Zymomonas*) per glucose | *Saccharomyces*, *Zymomonas* |
  | Mixed-acid (Definition 5.3.1) | acetate, lactate, succinate, formate, ethanol, $\ce{H2}$, $\ce{CO2}$ | about 2–3 per glucose | *E. coli*, *Salmonella*, *Shigella* |
  | Butanediol (Definition 5.3.2) | 2,3-butanediol, ethanol, $\ce{CO2}$, $\ce{H2}$ | about 2 per glucose | *Klebsiella*, *Enterobacter*, *Serratia* |
  | Butyric | butyrate, $\ce{CO2}$, $\ce{H2}$ | 3 per glucose | *Clostridium butyricum* |
  | Acetone–butanol | butanol, acetone, $\ce{CO2}$, $\ce{H2}$ | 2 per glucose | *C. acetobutylicum* |
  | Propionic | propionate, acetate, $\ce{CO2}$ (from lactate) | 1 per lactate | *Propionibacterium* |
  | Stickland | acetate, $\ce{NH4+}$, $\ce{CO2}$ (from amino acid pairs) | about 1 per amino acid | proteolytic clostridia |
  | Succinate or oxalate decarboxylation | propionate or formate | via a $\ce{Na+}$ or $\ce{H+}$ gradient | *Propionigenium*, *Oxalobacter* |

- Prokaryotic respiratory chains are modular and branched: in *E. coli*, two NADH dehydrogenases (NDH-1 pumping, NDH-2 not), a ubiquinone or menaquinone pool, and terminal oxidases $bo_3$ (4 $\ce{H+}$/2e⁻, low $\ce{O2}$ affinity) and $bd$ (2 $\ce{H+}$/2e⁻, high affinity) (Definition 5.4.1); terminal reductases replace the oxidases in anaerobic respiration (Definition 5.4.2). The proton-motive force drives ATP synthesis, transport and motility; fermenters generate it by reversing ATP synthase; some organisms use $\ce{Na+}$.
- Respiration of glucose yields about 11–30 ATP in *E. coli* depending on the chain, about 32 in mitochondria, against 1–3 ATP for fermentations (Example 5.4.1). The citric acid cycle runs as a branched pathway under anoxia; the glyoxylate cycle is needed on acetate and fatty acids.
- Twelve precursor metabolites, ATP, NADPH, nitrogen and sulfur supply all biosynthesis. Microbial specifics: ADP-glucose for glycogen, GS–GOGAT for ammonium at low concentrations, type II fatty acid synthase (target of isoniazid and triclosan), folate synthesis (target of sulfonamides).

## Questions

1. Using Formula 5.1.2 and the redox tower, calculate $\Delta_{\mathrm{r}}G^\circ{}'$ for the oxidation of NADH by $\ce{O2}$ and by fumarate. Why does *E. coli* prefer oxygen when both are present?

   **Answer** NADH/O₂: $\Delta E^\circ{}' = 0.816 - (-0.320) = 1.136\,\mathrm{V}$, $\Delta_{\mathrm{r}}G^\circ{}' = -2 \times 96.485 \times 1.136 = -219\,\mathrm{kJ\,mol^{-1}}$. NADH/fumarate: $\Delta E^\circ{}' = 0.033 + 0.320 = 0.353\,\mathrm{V}$, $-68\,\mathrm{kJ\,mol^{-1}}$. Oxygen releases about three times more energy per electron pair and supports a chain that pumps more protons, so ArcAB and FNR repress fumarate reductase and other anaerobic enzymes when oxygen is available.

2. A culture of lactic acid bacteria produces gas from glucose and accumulates both lactate and ethanol. Which pathway does it use, what is its ATP yield, and why does adding fructose to the medium increase the growth yield of *Leuconostoc*?

   **Answer** It is heterofermentative and uses the phosphoketolase pathway: glucose → lactate + ethanol + $\ce{CO2}$ (the gas), 1 ATP per glucose. Fructose serves as an external electron acceptor (reduced to mannitol), so NADH need not be spent reducing acetyl phosphate to ethanol; acetyl phosphate then gives a second ATP via acetate kinase.

3. Explain, in terms of redox balance, why *Klebsiella aerogenes* produces more $\ce{CO2}$ relative to $\ce{H2}$ and less acid than *E. coli*, and how the methyl red and Voges–Proskauer tests exploit this.

   **Answer** Making one 2,3-butanediol uses two pyruvate (releasing two $\ce{CO2}$ in the acetolactate and acetoin steps) but reoxidizes only one of the two NADH formed in glycolysis, so the organism must make extra ethanol and makes fewer acids. $\ce{CO2}$ thus comes both from formate (with an equal amount of $\ce{H2}$) and from the butanediol pathway. With less acid the pH stays near 6 (methyl red negative), whereas *E. coli* drops below 4.4 (methyl red positive); the Voges–Proskauer test detects the intermediate acetoin, present only in butanediol fermenters.

4. *Oxalobacter formigenes* grows on the decarboxylation of oxalate, which releases only about $27\,\mathrm{kJ\,mol^{-1}}$. How can it make ATP?

   **Answer** About $27\,\mathrm{kJ}$ is less than the free energy needed to form ATP (more than $30\,\mathrm{kJ}$ even under standard conditions, $50$–$60\,\mathrm{kJ}$ in the cell), so substrate-level phosphorylation is impossible. Instead an oxalate²⁻/formate⁻ antiporter brings in one net negative charge per turn and the cytoplasmic decarboxylation consumes a proton; together they generate a membrane potential and a pH gradient, a proton-motive force that drives ATP synthase. A fraction of an ATP per reaction is thus conserved through the ion gradient.

5. Why can a mutant of *E. coli* lacking cytochrome $bo_3$ still grow aerobically, and what would you expect for its growth yield on glucose? Under what conditions might the wild type itself rely mainly on cytochrome $bd$?

   **Answer** Cytochrome $bd$ also reduces $\ce{O2}$ with electrons from quinol, so respiration continues. It translocates 2 instead of 4 $\ce{H+}$ per electron pair, so the yield on glucose falls (with NDH-1, from 8 to 6 $\ce{H+}$ per NADH, roughly a quarter less ATP from the chain). The wild type relies on $bd$ under microaerobic conditions, where its high oxygen affinity is decisive, and when it must tolerate nitric oxide or cyanide, to which $bd$ is less sensitive.
