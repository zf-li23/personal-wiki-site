---
title: Glycolysis, Fermentation, and the Pentose Phosphate Pathway
description: Glucose and its fates; the ten reactions of glycolysis with their chemistry, energetics in cells and logic; feeder pathways for polysaccharides, disaccharides, fructose, galactose, mannose and glycerol; the fates of pyruvate, lactic and alcoholic fermentation, the Pasteur and Warburg effects; regulation of hexokinase, PFK-1 and pyruvate kinase; the oxidative and nonoxidative phases of the pentose phosphate pathway, its modes, G6PD deficiency; the pathway card of glycolysis.
---

Glucose is the central fuel of most organisms and a versatile precursor: its complete oxidation releases $2840\,\mathrm{kJ\,mol^{-1}}$, it can be stored as **glycogen** or **starch** (or converted to fat) without raising the **osmolarity** of the cell, and *Escherichia coli* can make from it the carbon skeleton of every molecule it contains. This chapter follows glucose along the two pathways that start from glucose 6-phosphate in the cytosol: glycolysis, which splits it into two molecules of pyruvate and yields ATP and **NADH**, and the pentose phosphate pathway, which oxidizes it to pentoses and **NADPH**. Glycolysis is the first pathway of Part II to be read with the tools of the previous two chapters: every step belongs to one of the five reaction classes ([7.1.17](/7.1.17#sec-17.1.2)), its energy account follows from [7.1.16](/7.1.16), and its regulation is concentrated at the three steps far from equilibrium ([7.1.17](/7.1.17#sec-17.3.3)). **Gluconeogenesis**, glycogen **metabolism** and the **reciprocal regulation** of glycolysis and gluconeogenesis are the subject of the next chapter ([7.1.19](/7.1.19)); the oxidation of pyruvate in mitochondria follows in [7.1.20](/7.1.20) and [7.1.23](/7.1.23). The chemistry of the sugars themselves is in [6.5.32](/6.5.32) and [7.1.10](/7.1.10).

## 18.1. Glucose and Its Fates

In animals and vascular plants glucose has four main fates: it is used to synthesize extracellular polysaccharides and **glycoconjugates** (7.1.10); it is stored as glycogen, starch or sucrose (7.1.19, 7.1.25); it is oxidized by glycolysis to pyruvate, which supplies ATP and metabolic intermediates; or it is oxidized in the pentose phosphate pathway to ribose 5-phosphate and NADPH (18.6).

**Definition 18.1.1 (Glycolysis)** **Glycolysis** (from Greek *glykys*, sweet, and *lysis*, splitting) is the sequence of ten enzyme-catalyzed reactions, all in the cytosol, by which one molecule of glucose is converted into two molecules of pyruvate, with net formation of two ATP and two NADH.

Glycolysis is nearly universal and its chemistry has been conserved throughout evolution; it was the first pathway to be worked out, and its history is the history of biochemistry. In 1897 Eduard Buchner found that a cell-free extract of yeast ferments sucrose to ethanol, which overturned the vitalist view that fermentation requires living cells (Nobel Prize 1907). Arthur Harden and William Young (1905–1906) showed that fermentation requires $\mathrm{P_i}$, isolated fructose 1,6-bisphosphate, and separated the extract into a heat-labile, nondialyzable fraction (zymase, the **enzymes**) and a heat-stable, dialyzable fraction (cozymase: $\ce{NAD+}$, ATP, ADP and metal ions). Gustav Embden and Otto Meyerhof reconstructed the conversion of glycogen to lactate in muscle extracts and recognized that lactic and alcoholic fermentation share most of their steps; by about 1940 the whole pathway, often called the Embden–Meyerhof (–Parnas) pathway, was known. The search for its enzymes produced much of enzymology, and the discovery of ATP and of its role in energy transfer.

## 18.2. The Ten Reactions of Glycolysis

### 18.2.1. Two Phases

Glycolysis has a preparatory phase, in which two ATP are invested to phosphorylate glucose and cleave it into two triose phosphates, and a payoff phase, in which each of the two glyceraldehyde 3-phosphates is oxidized to pyruvate with formation of two ATP and one NADH.

![Glycolysis. Preparatory phase (steps 1–5): glucose is phosphorylated by hexokinase, isomerized to fructose 6-phosphate, phosphorylated again by phosphofructokinase-1 (PFK-1, the committed step) and cleaved by aldolase into dihydroxyacetone phosphate and glyceraldehyde 3-phosphate, which are interconverted by triose phosphate isomerase. Payoff phase (steps 6–10, twice per glucose): glyceraldehyde 3-phosphate is oxidized and phosphorylated to 1,3-bisphosphoglycerate (NAD⁺ → NADH), whose acyl phosphate is transferred to ADP; after a group shift and a dehydration, phosphoenolpyruvate gives a second ATP and pyruvate. Irreversible steps (far from equilibrium in cells) have single heads, near-equilibrium steps double heads; co-substrates are on arcs; the reaction class of each step (7.1.17) is written on the right](./plots/glycolysis-pathway.py)

| Step | Enzyme | Reaction | Class (7.1.17) | $\Delta_{\mathrm{r}}G'^{\circ}$ / (kJ mol⁻¹) | $\Delta_{\mathrm{r}}G$ in erythrocytes / (kJ mol⁻¹) |
|---|---|---|---|---|---|
| 1 | hexokinase | glucose + ATP → glucose 6-phosphate + ADP | phosphoryl transfer | $-16.7$ | $-33.4$ |
| 2 | phosphohexose isomerase | glucose 6-phosphate ⇌ fructose 6-phosphate | isomerization | $+1.7$ | $-2.5$ |
| 3 | phosphofructokinase-1 | fructose 6-phosphate + ATP → fructose 1,6-bisphosphate + ADP | phosphoryl transfer | $-14.2$ | $-22.2$ |
| 4 | aldolase | fructose 1,6-bisphosphate ⇌ DHAP + glyceraldehyde 3-phosphate | C–C cleavage (retro-aldol) | $+23.8$ | $-1.3$ |
| 5 | triose phosphate isomerase | DHAP ⇌ glyceraldehyde 3-phosphate | isomerization | $+7.5$ | $+2.5$ |
| 6 | glyceraldehyde 3-phosphate dehydrogenase | **GAP** + $\mathrm{P_i}$ + $\ce{NAD+}$ ⇌ 1,3-bisphosphoglycerate + NADH + $\ce{H+}$ | oxidation, phosphorylation | $+6.3$ | $-1.7$ (6 + 7) |
| 7 | phosphoglycerate kinase | 1,3-bisphosphoglycerate + ADP ⇌ 3-phosphoglycerate + ATP | phosphoryl transfer | $-18.5$ | (with 6) |
| 8 | phosphoglycerate mutase | 3-phosphoglycerate ⇌ 2-phosphoglycerate | group shift | $+4.4$ | $+0.8$ |
| 9 | enolase | 2-phosphoglycerate ⇌ phosphoenolpyruvate + $\ce{H2O}$ | dehydration (elimination) | $+7.5$ | $-3.3$ |
| 10 | pyruvate kinase | phosphoenolpyruvate + ADP → pyruvate + ATP | phosphoryl transfer | $-31.4$ | $-16.7$ |

($\Delta_{\mathrm{r}}G'^{\circ}$ from Lehninger 8e; actual values computed from the metabolite concentrations measured in human erythrocytes, Minakami and Yoshikawa (1965), as tabulated in Lehninger 8e, Table 14-2, and Berg et al. The actual value for step 2 is printed in Lehninger's table as "0 to 25", evidently a misprint for a small value near zero.)

The table contains the whole energetic logic of the pathway. Three steps (1, 3, 10) are strongly exergonic in the cell; the other seven operate near equilibrium, whatever their standard values. The aldolase step, with $\Delta_{\mathrm{r}}G'^{\circ} = +23.8\,\mathrm{kJ\,mol^{-1}}$, runs forward in the cell because it produces two molecules from one and its products are present at micromolar concentrations ([7.1.16](/7.1.16#sec-16.2.2)).

![Free-energy profile of glycolysis per glucose. Cumulative standard Gibbs energy (ΔrG′°, dashed) and cumulative actual Gibbs energy in human erythrocytes (ΔrG, solid) after each step; from step 6 on, every step counts twice (two trioses per glucose), and steps 6 and 7 are combined. Under standard conditions the profile climbs at aldolase and triose phosphate isomerase; in the cell, the free energy falls in three large drops, at hexokinase, PFK-1 and pyruvate kinase, while the other steps are nearly level, near equilibrium](./plots/glycolysis-free-energy.py)

### 18.2.2. The Preparatory Phase

1. Hexokinase phosphorylates glucose at C-6 with ATP; the true **substrate** is $\ce{MgATP^2-}$ ([7.1.16](/7.1.16#sec-16.3.1)). The reaction is irreversible in cells, and its product cannot leave the cell, because the plasma membrane has no **transporter** for glucose 6-phosphate. Hexokinase undergoes a large induced-fit closure when glucose binds, which excludes water from the **active site** and prevents the wasteful hydrolysis of ATP ([7.1.8](/7.1.8#sec-8.4.3)). Humans have four hexokinase **isozymes** (I–IV); **hexokinase IV**, also called glucokinase, of liver and pancreatic β cells has different kinetics and regulation (18.5.2, [7.1.19](/7.1.19)).
2. Phosphohexose isomerase (phosphoglucose isomerase) converts the aldose glucose 6-phosphate into the ketose fructose 6-phosphate through an enediol intermediate; **general acid–base catalysis** by active-site **residues** moves the carbonyl from C-1 to C-2 ([7.1.17](/7.1.17#sec-17.1.2)). The reaction is freely reversible.
3. Phosphofructokinase-1 (PFK-1) transfers a second phosphoryl group from ATP to C-1 of fructose 6-phosphate. This is the **committed step** of glycolysis (Definition 17.3.1): fructose 1,6-bisphosphate has no other fate. PFK-1 is the main **regulatory enzyme** of the pathway (18.5). ("-1" distinguishes it from PFK-2, which makes **fructose 2,6-bisphosphate**, 7.1.19.) Some plants and protists use a $\mathrm{PP_i}$-dependent phosphofructokinase, whose reaction is reversible.
4. Aldolase (fructose 1,6-bisphosphate aldolase) cleaves the C-3–C-4 bond in a reverse aldol reaction, giving the ketose dihydroxyacetone phosphate (DHAP, carbons 1–3) and the aldose glyceraldehyde 3-phosphate (GAP, carbons 4–6). The class I **aldolase** of animals and plants binds the C-2 carbonyl as a protonated Schiff base with an active-site Lys, the electron sink that stabilizes the carbanion formed on C-3; class II aldolases of fungi and bacteria use $\ce{Zn^2+}$ instead. The mechanism is drawn in [6.5.22](/6.5.22#sec-22.10.1).
5. Triose phosphate isomerase interconverts DHAP and GAP through an enediol(ate) intermediate. Only GAP continues; DHAP is converted to it, so that both halves of glucose pass through the payoff phase. Triose phosphate isomerase is the classic "perfect" enzyme: $k_{\mathrm{cat}}/K_{\mathrm{M}}$ is about $10^{8}$–$10^{9}\,\mathrm{M^{-1}\,s^{-1}}$, near the diffusion limit ([6.3.17](/6.3.17)), and a flexible loop closes over the substrate to prevent the elimination of phosphate from the enediol intermediate to the toxic methylglyoxal.

The two isomerizations follow from chemical logic. A retro-aldol cleavage needs a carbonyl at C-2 and a hydroxyl at C-4 of the substrate; glucose (an aldose) cleaved directly would give a C₂ and a C₄ fragment, but fructose cleaves symmetrically into two C₃ units. Phosphorylating C-1 of fructose before cleavage puts a phosphate on each triose. After step 5, carbons 1, 2 and 3 of GAP derive from carbons 6, 5 and 4 or 1, 2 and 3 of glucose, respectively, a fact used in isotope tracing:

| Carbon of glyceraldehyde 3-phosphate | C-1 (aldehyde) | C-2 | C-3 (phosphate ester) |
|---|---|---|---|
| derived from carbon of glucose | 3 or 4 | 2 or 5 | 1 or 6 |

### 18.2.3. The Payoff Phase

6. Glyceraldehyde 3-phosphate dehydrogenase (GAPDH) oxidizes the aldehyde of GAP and phosphorylates the resulting carboxyl group with $\mathrm{P_i}$, giving the acyl phosphate 1,3-bisphosphoglycerate. The mechanism conserves the energy of oxidation as a high-energy bond: the active-site Cys attacks the aldehyde, forming a thiohemiacetal; hydride transfer to $\ce{NAD+}$ oxidizes it to a **thioester** (a covalent acyl-enzyme, 7.1.17); and **phosphorolysis** of the thioester by $\mathrm{P_i}$ releases the mixed anhydride, whose **phosphoryl group transfer potential** ($-49.3\,\mathrm{kJ\,mol^{-1}}$) is higher than that of ATP. Iodoacetate, which alkylates the Cys, inhibits the enzyme. Arsenate, which resembles phosphate, can replace $\mathrm{P_i}$; the product 1-arseno-3-phosphoglycerate hydrolyzes spontaneously, so glycolysis continues but the ATP of step 7 is lost, one reason why arsenate is toxic.
7. Phosphoglycerate kinase transfers the phosphoryl group from the acyl phosphate of 1,3-bisphosphoglycerate to ADP (the enzyme is named for the reverse reaction). Steps 6 and 7 together are an energy-coupling process through the shared intermediate 1,3-bisphosphoglycerate: GAP + ADP + $\mathrm{P_i}$ + $\ce{NAD+}$ ⇌ 3-phosphoglycerate + ATP + NADH + $\ce{H+}$, $\Delta_{\mathrm{r}}G'^{\circ} = +6.3 - 18.5 = -12.2\,\mathrm{kJ\,mol^{-1}}$. The pair is near equilibrium in the cell and can run backward in gluconeogenesis.

   **Definition 18.2.1 (Substrate-Level Phosphorylation)** The formation of ATP by transfer of a phosphoryl group from a substrate of high phosphoryl group transfer potential to ADP, catalyzed by a soluble enzyme, is called **substrate-level phosphorylation**; it is distinguished from respiration-linked (oxidative) phosphorylation and photophosphorylation, which use a transmembrane proton gradient (7.1.23–7.1.24).

   In erythrocytes, part of the 1,3-bisphosphoglycerate is diverted by bisphosphoglycerate mutase to **2,3-bisphosphoglycerate**, the **allosteric effector** of hemoglobin ([7.1.7](/7.1.7#sec-7.3.6)), which a phosphatase then converts to 3-phosphoglycerate (the Rapoport–Luebering shunt); the shunt bypasses step 7 and costs one ATP.
8. Phosphoglycerate mutase moves the phosphoryl group from C-3 to C-2. The enzyme of vertebrates and yeast is phosphorylated on a His residue; it transfers this phosphoryl group to C-2 of 3-phosphoglycerate, giving **2,3-bisphosphoglycerate** bound to the enzyme, and then takes the phosphoryl group from C-3. A small amount of 2,3-bisphosphoglycerate is therefore needed as a **cofactor** to rephosphorylate the enzyme; plants have a cofactor-independent mutase with a different mechanism.
9. Enolase dehydrates 2-phosphoglycerate to phosphoenolpyruvate (PEP) with the help of two $\ce{Mg^2+}$ ions ([7.1.8](/7.1.8#sec-8.4.4)). The standard Gibbs energies of hydrolysis of the reactant and the product differ enormously ($-17.6$ and $-61.9\,\mathrm{kJ\,mol^{-1}}$), although the dehydration itself has a small $\Delta_{\mathrm{r}}G'^{\circ}$: the elimination locks the phosphate onto an enol, whose hydrolysis product can tautomerize ([7.1.16](/7.1.16#sec-16.3.3)). Fluoride inhibits enolase by forming a fluorophosphate–$\ce{Mg^2+}$ complex in the active site; it is added to blood samples to stop glycolysis before glucose is measured.
10. Pyruvate kinase transfers the phosphoryl group from PEP to ADP ($\ce{Mg^2+}$ and $\ce{K+}$ required). The enol product tautomerizes to the keto form of pyruvate, which makes the reaction strongly exergonic and irreversible in cells. Pyruvate kinase is the third regulated enzyme (18.5.3).

### 18.2.4. Balance and Logic

Overall, per glucose,

$$
\text{glucose} + 2\,\ce{NAD+} + 2\,\ce{ADP} + 2\,\mathrm{P_i} \to 2\,\text{pyruvate} + 2\,\ce{NADH} + 2\,\ce{H+} + 2\,\ce{ATP} + 2\,\ce{H2O}. \tag{18.1}
$$
The equation can be split into the oxidation of glucose to pyruvate with $\ce{NAD+}$, glucose + 2 $\ce{NAD+}$ → 2 pyruvate + 2 NADH + 2 $\ce{H+}$ ($\Delta_{\mathrm{r}}G'^{\circ} = -146\,\mathrm{kJ\,mol^{-1}}$), and the formation of two ATP ($+61.0\,\mathrm{kJ\,mol^{-1}}$); the sum is $-85\,\mathrm{kJ\,mol^{-1}}$ (Lehninger 8e). Under cellular conditions the overall $\Delta_{\mathrm{r}}G$ is about $-100\,\mathrm{kJ\,mol^{-1}}$ (the sum of the actual values in the table, counting steps 6–10 twice), so the pathway is irreversible as a whole. Glycolysis releases only about 5% of the free energy of glucose ($146/2840$); most of it remains in the two pyruvates and the two NADH, and is recovered in mitochondria, where complete oxidation yields about 30–32 ATP per glucose (7.1.23).

Three features recur in all of central metabolism.

- All nine intermediates between glucose and pyruvate are phosphorylated. At pH 7 their phosphate groups are ionized, so the intermediates cannot cross the plasma membrane and stay in the cell without the expense of transport; the phosphoryl groups are needed to form the **high-energy compounds** 1,3-bisphosphoglycerate and PEP; and their binding to the enzymes (often as complexes with $\ce{Mg^2+}$) contributes **binding energy** and specificity ([7.1.8](/7.1.8#sec-8.3.1)).
- ATP is invested before it is earned. The two ATP of the preparatory phase convert glucose into fructose 1,6-bisphosphate, whose cleavage products carry the phosphates that will be raised to high transfer potential; the pathway returns four ATP for two.
- Oxidation is coupled to phosphorylation at a single step (GAPDH), through a covalent thioester intermediate, as in all substrate-level phosphorylations.

Glycolysis needs a continuous supply of $\ce{NAD+}$, which is present in the cytosol at less than a millimolar ([7.1.16](/7.1.16#sec-16.5.1)) and would be fully reduced within seconds to minutes of active glycolysis if the NADH were not reoxidized: by the **respiratory chain**, via shuttles into mitochondria, in aerobic cells (7.1.23), or by fermentation (18.4) in anaerobic ones. Under some conditions the concentrations of glycolytic intermediates in yeast oscillate with periods of minutes, because PFK-1 is activated by its products ([6.3.18](/6.3.18#sec-18.3.3), **glycolytic oscillation**).

## 18.3. Feeder Pathways for Glycolysis

Besides glucose, many carbohydrates enter glycolysis after conversion to one of its intermediates.

![Feeder pathways for glycolysis. Glycogen and starch are phosphorolyzed to glucose 1-phosphate, which phosphoglucomutase converts to glucose 6-phosphate; dietary disaccharides are hydrolyzed to monosaccharides. Fructose enters as fructose 6-phosphate in muscle and kidney (hexokinase) or, in liver, as fructose 1-phosphate, which aldolase B cleaves to dihydroxyacetone phosphate and glyceraldehyde (phosphorylated by triose kinase), bypassing PFK-1. Galactose is converted by the Leloir pathway (galactokinase, galactose 1-phosphate uridylyltransferase, UDP-glucose 4-epimerase) to glucose 1-phosphate. Mannose enters as mannose 6-phosphate and fructose 6-phosphate; glycerol from triacylglycerols enters as glycerol 3-phosphate and dihydroxyacetone phosphate. Inherited defects are marked at the enzymes concerned](./plots/hexose-entry.py)

### 18.3.1. Polysaccharides and Disaccharides

Endogenous glycogen in muscle and liver, and starch in plants, are broken down by phosphorolysis rather than hydrolysis: **glycogen phosphorylase** (or starch phosphorylase) attacks the terminal (α1→4) bond at a nonreducing end with $\mathrm{P_i}$, releasing glucose 1-phosphate without spending ATP, and phosphoglucomutase converts it to glucose 6-phosphate (Example 16.2.1). A glucose residue from glycogen thus enters glycolysis already phosphorylated, and anaerobic glycolysis from glycogen yields three ATP per glucosyl unit instead of two. Phosphorolysis, its enzymes and its regulation are treated in [7.1.19](/7.1.19).

Dietary polysaccharides and disaccharides are hydrolyzed in the gut. Salivary and pancreatic α-amylases hydrolyze the internal (α1→4) bonds of starch and glycogen to maltose, maltotriose and α-limit dextrins (the fragments that contain the (α1→6) **branch points**); enzymes of the brush border of the small intestine (maltase–glucoamylase, sucrase–isomaltase, lactase, trehalase) complete the hydrolysis to monosaccharides, which are absorbed by $\ce{Na+}$–glucose **symport** (SGLT1) and **facilitated diffusion** (GLUT5 for fructose, GLUT2) and carried by the blood to the tissues ([7.1.13](/7.1.13)).

Lactase activity falls after weaning in most mammals and in about two-thirds of adult humans. In these people (lactase non-persistence) lactose reaches the large intestine, where bacteria ferment it to gases and short-chain acids, causing cramps and diarrhea (lactose intolerance). Persistence of lactase into adulthood is common in populations with a long history of dairying (northern Europe, parts of Africa and the Middle East), where several independent regulatory **mutations** upstream of the lactase **gene** were favored by natural selection in the last ten thousand years, one of the clearest examples of recent human evolution ([7.10](/7.10)).

### 18.3.2. Fructose, Galactose, Mannose and Glycerol

Fructose enters in two ways. In muscle and kidney, hexokinase phosphorylates it to fructose 6-phosphate, a glycolytic intermediate. In the liver, which takes up most dietary fructose, fructokinase phosphorylates it to fructose 1-phosphate, which fructose 1-phosphate aldolase (aldolase B) cleaves to DHAP and glyceraldehyde; triose kinase phosphorylates glyceraldehyde to GAP. This route bypasses PFK-1, the main control point, so that large amounts of dietary fructose (from sucrose and high-fructose syrups) are converted to pyruvate and acetyl-CoA without feedback control, favoring fat synthesis in the liver (7.1.26). In hereditary fructose intolerance, deficiency of aldolase B, fructose 1-phosphate accumulates after fructose intake and traps the phosphate of the cell, so that ATP falls and glycogen breakdown is inhibited; severe hypoglycemia and liver damage result unless fructose and sucrose are avoided.

Galactose, from lactose, is converted to glucose 1-phosphate by the Leloir pathway. Galactokinase phosphorylates it at C-1; galactose 1-phosphate uridylyltransferase exchanges it with UDP-glucose, giving UDP-galactose and glucose 1-phosphate; and UDP-glucose 4-epimerase converts UDP-galactose back to UDP-glucose by oxidizing C-4 with a tightly bound $\ce{NAD+}$ and reducing it from the other face. The net reaction is galactose + ATP → glucose 1-phosphate + ADP, the UDP-sugar acting catalytically. Galactosemia, inherited deficiency of any of the three enzymes, is detected by newborn screening. In the classic form (uridylyltransferase deficiency), galactose 1-phosphate and galactose accumulate, causing liver damage, cataracts and intellectual disability unless galactose is excluded from the diet; in galactokinase deficiency the main problem is cataract, caused by galactitol formed from galactose by aldose reductase in the lens.

Mannose, from the digestion of **glycoproteins**, is phosphorylated by hexokinase to mannose 6-phosphate and isomerized by phosphomannose isomerase to fructose 6-phosphate. Glycerol, released by the hydrolysis of triacylglycerols (7.1.21), is phosphorylated by glycerol kinase (mainly in liver) and oxidized by glycerol 3-phosphate dehydrogenase to DHAP.

## 18.4. Fates of Pyruvate

### 18.4.1. Three Fates

Pyruvate stands at a branch point. Under aerobic conditions in most cells it enters mitochondria and is oxidatively decarboxylated to acetyl-CoA by the **pyruvate dehydrogenase complex**; the acetyl group is oxidized in the **citric acid cycle** (7.1.20) and the NADH formed in glycolysis passes its electrons to $\ce{O2}$, so that no fermentation product is needed. Under anaerobic or hypoxic conditions, or in cells without mitochondria, the NADH must be reoxidized in the cytosol by reducing pyruvate or a product derived from it. Pyruvate is also a precursor: it is carboxylated to oxaloacetate in gluconeogenesis and **anaplerosis** (7.1.19–7.1.20) and transaminated to alanine (7.1.22).

**Definition 18.4.1 (Fermentation)** **Fermentation** is the anaerobic degradation of a fuel in which the electrons removed in its oxidation are transferred to an organic acceptor derived from the fuel itself, so that the energy is conserved as ATP by substrate-level phosphorylation without consumption of $\ce{O2}$ and without a net change in the concentrations of $\ce{NAD+}$ and NADH. In **lactic acid fermentation**, pyruvate is reduced to lactate; in **alcoholic fermentation**, it is decarboxylated to acetaldehyde, which is reduced to ethanol.

### 18.4.2. Lactic Acid Fermentation

Lactate dehydrogenase reduces pyruvate with NADH: pyruvate + NADH + $\ce{H+}$ ⇌ L-lactate + $\ce{NAD+}$, $\Delta_{\mathrm{r}}G'^{\circ} = -25.1\,\mathrm{kJ\,mol^{-1}}$. The two NADH formed per glucose by GAPDH are reoxidized by the two pyruvates, and the overall reaction,

$$
\text{glucose} + 2\,\ce{ADP} + 2\,\mathrm{P_i} \to 2\,\text{lactate} + 2\,\ce{ATP} + 2\,\ce{H2O}, \qquad \Delta_{\mathrm{r}}G'^{\circ} = -196\,\mathrm{kJ\,mol^{-1}},
$$
involves no net oxidation: the carbon of lactate is at the same average oxidation state as that of glucose. Lactate is formed by vigorously contracting skeletal muscle whose glycolysis outpaces the delivery of $\ce{O2}$, by erythrocytes (which have no mitochondria), by the retina, and by many microorganisms (lactic acid bacteria of yogurt, cheese, sauerkraut and silage). Mammalian LDH is a tetramer of two kinds of **subunits**, H (heart) and M (muscle), which combine into five **isozymes** ([7.1.9](/7.1.9#sec-9.1.3)); the H₄ form of heart is inhibited by high pyruvate and favors oxidation of lactate to pyruvate, the M₄ form of skeletal muscle and liver favors reduction of pyruvate.

Lactate is not a waste product. It diffuses out of muscle into the blood and is taken up by the heart, which oxidizes it, and by the liver, which converts it back to glucose (the **Cori cycle**, 7.1.19); during recovery from exercise most of the lactate is oxidized. Lactic **acidosis** develops when lactate production exceeds its removal (shock, severe exercise, some poisonings and inherited mitochondrial diseases). Some animals depend on lactic fermentation for bursts of activity: an alligator or a coelacanth, normally sluggish, can sprint or strike with glycolytic white muscle and then needs hours to clear the lactate.

### 18.4.3. Alcoholic Fermentation

Yeast and some other microorganisms ferment glucose to ethanol and $\ce{CO2}$ in two steps after glycolysis. Pyruvate decarboxylase, which requires $\ce{Mg^2+}$ and **thiamine pyrophosphate**, removes the carboxyl group irreversibly (the mechanism is drawn in [7.1.17](/7.1.17#sec-17.2.2)); alcohol dehydrogenase, a $\ce{Zn^2+}$ enzyme, then reduces acetaldehyde with NADH (Example 16.4.1):

$$
\text{glucose} + 2\,\ce{ADP} + 2\,\mathrm{P_i} \to 2\,\text{ethanol} + 2\,\ce{CO2} + 2\,\ce{ATP} + 2\,\ce{H2O}, \qquad \Delta_{\mathrm{r}}G'^{\circ} = -235\,\mathrm{kJ\,mol^{-1}}.
$$
The $\ce{CO2}$ raises bread and carbonates champagne and beer. Humans have alcohol dehydrogenase, which oxidizes ingested ethanol to acetaldehyde in the liver (7.1.9, alcohol flushing), but no pyruvate decarboxylase; pyruvate decarboxylase is present in brewer's and baker's yeast and in a few other organisms (and in plants under anoxia), and the reaction is the classic example of TPP catalysis.

Other fermentations yield other products. Propionibacteria make propionate and $\ce{CO2}$ (the holes of Swiss cheese); clostridia make butyrate, acetone and butanol (the acetone–butanol–ethanol fermentation was developed by Chaim Weizmann during the First World War to produce acetone for explosives); enteric bacteria make a mixture of acids, ethanol, $\ce{H2}$ and $\ce{CO2}$. Industrial fermentations produce ethanol for fuel, lactic acid for biodegradable plastics, and, with engineered microorganisms, many other chemicals; their design uses the ideas of **metabolic control analysis** ([7.1.17](/7.1.17#sec-17.4)).

### 18.4.4. The Pasteur and Warburg Effects

**Definition 18.4.2 (Pasteur Effect and Warburg Effect)** The decrease in the rate of glucose consumption (and of fermentation) that occurs when a facultatively anaerobic cell is shifted from anaerobic to aerobic conditions is the **Pasteur effect**. The high rate of glucose uptake and conversion to lactate, even in the presence of enough oxygen for respiration, that is characteristic of many tumor cells and of rapidly proliferating normal cells is the **Warburg effect** (aerobic glycolysis).

The Pasteur effect follows from the energy account. Respiration yields about 30–32 ATP per glucose, fermentation 2; to make ATP at the same rate without oxygen, a cell must consume glucose about fifteen times faster. Pasteur observed the effect in yeast in 1861; in muscle and yeast it is mediated by the adenine nucleotides and citrate acting on PFK-1 (18.5.1): when respiration supplies ATP, [AMP] is low and citrate high, and glycolysis slows.

Otto Warburg (Nobel Prize 1931, for the discovery of the respiratory enzyme) observed in the 1920s that tumor slices convert glucose to lactate at high rates even in oxygen. He proposed that cancer arises from a defect of respiration, which has not been borne out: most tumors have functional mitochondria and also respire. The present view is that aerobic glycolysis serves proliferation. A dividing cell needs carbon skeletons (for nucleotides, **lipids** and amino acids, drawn off from glycolytic intermediates and the pentose phosphate pathway) and NADPH more than ATP, and a high glycolytic flux, with the excess carbon discarded as lactate, keeps the intermediates abundant. Oncogenic signaling (**PI3K**–**Akt**, Myc) and the hypoxia-inducible **transcription** factor HIF-1, stabilized in the poorly perfused regions of a tumor, increase the expression of glucose transporters and of most glycolytic enzymes, including hexokinase II and lactate dehydrogenase A; many tumors express the less active M2 isozyme of pyruvate kinase, whose regulation allows intermediates to accumulate for **biosynthesis**. The high glucose uptake of tumors is used for imaging by positron emission tomography (PET) with 2-[¹⁸F]fluoro-2-deoxyglucose (FDG): hexokinase phosphorylates FDG, but phosphohexose isomerase cannot act on the 2-deoxy compound, so FDG 6-phosphate is trapped in the cells that take it up. Inhibitors of glycolytic enzymes and of lactate export are being explored as cancer therapy. Activated T cells and other rapidly dividing cells show the same metabolic program, which is one reason why metabolism is now studied as part of immunology (7.15).

## 18.5. Regulation of Glycolysis

The three irreversible steps, catalyzed by hexokinase, PFK-1 and pyruvate kinase, are the regulated ones ([7.1.17](/7.1.17#sec-17.3.3)). In the supply–demand view of [7.1.17](/7.1.17#sec-17.4.4), the regulation of these enzymes by the adenine nucleotides matches glycolytic flux to the demand for ATP while keeping [ATP] and the concentrations of the intermediates nearly constant; the coordination with gluconeogenesis, through fructose 2,6-bisphosphate and **hormones**, is the subject of [7.1.19](/7.1.19).

### 18.5.1. Phosphofructokinase-1

PFK-1 is a tetramer (in *E. coli* of four identical subunits, each with a catalytic and a regulatory site; the mammalian enzyme has muscle, liver and platelet isoforms). It is a K-type **allosteric enzyme** in the sense of the **MWC model** ([7.1.9](/7.1.9#sec-9.5.2)): its effectors change the half-saturating concentration of fructose 6-phosphate, $K_{0.5}$, more than $v_{\max}$.

- ATP is a substrate and also an end product of the pathway. At high concentration it binds to a separate regulatory site, which favors the **T state** and lowers the affinity for fructose 6-phosphate; the substrate–activity curve becomes sigmoid with a much higher $K_{0.5}$.
- ADP and AMP, which accumulate when ATP is consumed faster than it is made, relieve the inhibition by ATP. AMP is the more sensitive signal, amplified by **adenylate kinase** ([7.1.17](/7.1.17#sec-17.3.5)).
- Citrate, an intermediate of the aerobic oxidation of pyruvate, **fatty acids** and amino acids, reinforces the inhibition by ATP: when the citric acid cycle is well supplied, glycolysis need not run.
- Fructose 2,6-bisphosphate, made by PFK-2 under hormonal control, is the most potent **activator**: it raises the affinity of PFK-1 for fructose 6-phosphate and lowers that for ATP, and at physiological concentrations of the other effectors PFK-1 is nearly inactive without it (7.1.19).
- $\ce{H+}$ inhibits PFK-1; the fall of pH in intensely working muscle thus limits further lactate production.

![Allosteric regulation of PFK-1 in a concerted (MWC) model with four sites (Formula 9.5.1 of 7.1.9). Relative activity against [fructose 6-phosphate] at low [ATP] (0.5 mM), at high [ATP] (5 mM), and at high [ATP] with AMP (0.1 mM) or with fructose 2,6-bisphosphate (1 µM). ATP, binding to a regulatory site of the T state, makes the curve sigmoid and shifts it to higher substrate concentrations; AMP and fructose 2,6-bisphosphate, binding to the R state, reverse the shift. Parameters are illustrative: L₀ = 10, c = 0.01, K_R(F6P) = 0.05 mM, K(ATP) = 0.25 mM, K(AMP) = 50 µM, K(F2,6BP) = 1 µM](./plots/pfk1-regulation.py)

### 18.5.2. Hexokinase

Hexokinases I to III, of muscle, brain and most other tissues, have a high affinity for glucose ($K_{\mathrm{M}}$ about 0.1 mM, well below the 4–5 mM in blood) and work near $v_{\max}$; they are inhibited allosterically by their product, glucose 6-phosphate. When PFK-1 is inhibited, fructose 6-phosphate and, through the near-equilibrium isomerase, glucose 6-phosphate accumulate and slow hexokinase: the inhibition of the committed step propagates back to the entry of glucose. Hexokinase II is the main isozyme of skeletal muscle. Hexokinase IV (glucokinase) of the liver has a $K_{0.5}$ of about 10 mM, a cooperative response to glucose, and no inhibition by glucose 6-phosphate; it is regulated by a nuclear regulatory **protein** and suits the role of the liver as a buffer of blood glucose ([7.1.19](/7.1.19)).

### 18.5.3. Pyruvate Kinase

Vertebrates have several isozymes of pyruvate kinase: L (liver), M1 (muscle and brain), M2 (fetal tissues and proliferating cells) and R (erythrocytes). All are inhibited allosterically by ATP, acetyl-CoA and long-chain fatty acids, signs of an abundant energy supply, and the liver enzyme also by alanine, made from pyruvate in one step. Fructose 1,6-bisphosphate, the product of PFK-1, activates the L and M2 isozymes (feedforward activation), so that the last step keeps pace with the committed step. The L isozyme is also regulated covalently: when blood glucose is low, **glucagon** raises **cAMP**, and **PKA** phosphorylates and inactivates it, so that the liver stops consuming glucose and PEP is directed into gluconeogenesis ([7.1.19](/7.1.19)); **insulin** promotes its dephosphorylation and its synthesis. Inherited deficiency of the R isozyme is the most common enzyme defect of glycolysis and causes hemolytic anemia: erythrocytes, which depend entirely on glycolysis for ATP, cannot maintain their ion pumps and shape.

## 18.6. The Pentose Phosphate Pathway

**Definition 18.6.1 (Pentose Phosphate Pathway)** The **pentose phosphate pathway** (phosphogluconate pathway, hexose monophosphate shunt) is the cytosolic pathway that oxidizes glucose 6-phosphate with $\ce{NADP+}$ to ribulose 5-phosphate and $\ce{CO2}$ (oxidative phase) and interconverts pentose phosphates and glycolytic intermediates by transfers of two- and three-carbon units (nonoxidative phase).

Its two products serve different tissues. NADPH is the reductant of biosynthesis (fatty acids in liver, adipose tissue and lactating mammary gland; **cholesterol** and **steroid hormones** in liver, adrenal cortex and gonads) and of the defense against oxygen radicals (erythrocytes, lens and cornea, phagocytes). Ribose 5-phosphate is the precursor of nucleotides, **coenzymes** and nucleic acids, needed in large amounts by dividing cells (bone marrow, skin, intestinal mucosa, tumors).

### 18.6.1. The Oxidative Phase

Glucose 6-phosphate dehydrogenase (G6PD) oxidizes C-1 of glucose 6-phosphate, the hemiacetal carbon, to a lactone, 6-phosphoglucono-δ-lactone, with $\ce{NADP+}$ as acceptor; the equilibrium lies far toward NADPH, and this is the committed, regulated step. A lactonase hydrolyzes the lactone to 6-phosphogluconate, and 6-phosphogluconate dehydrogenase catalyzes its oxidative decarboxylation to the ketopentose ribulose 5-phosphate, forming a second NADPH. Phosphopentose isomerase converts ribulose 5-phosphate to ribose 5-phosphate (and an epimerase to xylulose 5-phosphate). The oxidative phase is

$$
\text{glucose 6-phosphate} + 2\,\ce{NADP+} + \ce{H2O} \to \text{ribose 5-phosphate} + \ce{CO2} + 2\,\ce{NADPH} + 2\,\ce{H+}. \tag{18.2}
$$

In erythrocytes the NADPH keeps glutathione reduced: glutathione peroxidase destroys $\ce{H2O2}$ and lipid peroxides with reduced glutathione (GSH), and glutathione reductase regenerates GSH from the disulfide GSSG with NADPH. G6PD deficiency, the most common enzyme deficiency of humans (about 400 million people, X-linked), is usually silent, but oxidative stress from fava beans (which contain divicine and isouramil), the antimalarial primaquine, sulfonamides or infections can cause acute hemolysis within one or two days, with jaundice and sometimes kidney failure (favism). The deficiency reaches frequencies of up to 25% in tropical Africa, the Middle East and Southeast Asia, where malaria is or was common: the parasite *Plasmodium falciparum* is very sensitive to oxidative damage and grows poorly in G6PD-deficient erythrocytes, a balanced polymorphism like that of the sickle cell allele ([7.1.7](/7.1.7#sec-7.3.8)). Pythagoras's prohibition of beans may have had this basis.

### 18.6.2. The Nonoxidative Phase

When a tissue needs more NADPH than ribose 5-phosphate, the pentose phosphates are recycled into hexose phosphates by two enzymes unique to the pathway, together with enzymes of glycolysis and gluconeogenesis. All these reactions are freely reversible.

**Definition 18.6.2 (Transketolase and Transaldolase)** **Transketolase** transfers a two-carbon unit (C-1 and C-2 of a ketose donor) to an aldose acceptor; it requires thiamine pyrophosphate, which carries the two-carbon unit as a carbanion. **Transaldolase** transfers a three-carbon unit (C-1 to C-3 of a ketose donor) to an aldose acceptor; the donor is bound as a Schiff base with an active-site Lys, as in the aldolase of glycolysis.

The carbon shuffle uses three reactions:

$$
\begin{aligned}
&\mathrm{C_5}\ (\text{xylulose 5-P}) + \mathrm{C_5}\ (\text{ribose 5-P}) \rightleftharpoons \mathrm{C_3}\ (\text{GAP}) + \mathrm{C_7}\ (\text{sedoheptulose 7-P}) && \text{transketolase} \\
&\mathrm{C_7}\ (\text{sedoheptulose 7-P}) + \mathrm{C_3}\ (\text{GAP}) \rightleftharpoons \mathrm{C_4}\ (\text{erythrose 4-P}) + \mathrm{C_6}\ (\text{fructose 6-P}) && \text{transaldolase} \\
&\mathrm{C_5}\ (\text{xylulose 5-P}) + \mathrm{C_4}\ (\text{erythrose 4-P}) \rightleftharpoons \mathrm{C_3}\ (\text{GAP}) + \mathrm{C_6}\ (\text{fructose 6-P}) && \text{transketolase}
\end{aligned}
$$
whose sum converts three pentoses into two fructose 6-phosphates and one GAP ($3\,\mathrm{C_5} \to 2\,\mathrm{C_6} + \mathrm{C_3}$). Two such rounds give $6\,\mathrm{C_5} \to 4\,\mathrm{C_6} + 2\,\mathrm{C_3}$, and the two GAP are joined by triose phosphate isomerase, aldolase and fructose 1,6-bisphosphatase into a fifth hexose phosphate: six pentoses become five hexoses. Run in reverse, the same reactions make pentoses from hexoses without oxidation; in photosynthetic organisms a closely related set regenerates the $\ce{CO2}$ acceptor of the Calvin cycle (the **reductive pentose phosphate pathway**, 7.1.25).

### 18.6.3. Four Modes

Because the nonoxidative reactions are reversible and share intermediates with glycolysis, the pathway can be run in four modes according to the needs of the cell for ribose 5-phosphate, NADPH and ATP (Berg et al.):

| Mode | Need | Route | Net reaction |
|---|---|---|---|
| 1 | much more ribose 5-phosphate than NADPH (rapidly dividing cells) | glycolytic F6P and GAP → nonoxidative phase in reverse; oxidative phase bypassed | 5 glucose 6-P + ATP → 6 ribose 5-P + ADP + $\ce{H+}$ |
| 2 | balanced | oxidative phase only | glucose 6-P + 2 $\ce{NADP+}$ + $\ce{H2O}$ → ribose 5-P + 2 NADPH + 2 $\ce{H+}$ + $\ce{CO2}$ |
| 3 | much more NADPH than ribose 5-phosphate (adipose tissue) | oxidative phase, pentoses recycled to glucose 6-phosphate by the nonoxidative phase and gluconeogenic enzymes | glucose 6-P + 12 $\ce{NADP+}$ + 7 $\ce{H2O}$ → 6 $\ce{CO2}$ + 12 NADPH + 12 $\ce{H+}$ + $\mathrm{P_i}$ |
| 4 | NADPH and ATP | oxidative phase; pentoses to F6P and GAP, then through glycolysis to pyruvate | 3 glucose 6-P + 6 $\ce{NADP+}$ + 5 $\ce{NAD+}$ + 5 $\mathrm{P_i}$ + 8 ADP → 5 pyruvate + 3 $\ce{CO2}$ + 6 NADPH + 5 NADH + 8 ATP + 2 $\ce{H2O}$ + 8 $\ce{H+}$ |

In mode 3, six turns of the oxidative phase oxidize the equivalent of one glucose 6-phosphate completely to six $\ce{CO2}$, with all the electrons collected as NADPH.

![The four modes of the pentose phosphate pathway. In each panel the active routes are drawn in colour and the inactive ones are dashed and gray. Mode 1: fructose 6-phosphate and glyceraldehyde 3-phosphate from glycolysis are converted into ribose 5-phosphate by the nonoxidative reactions run in reverse. Mode 2: the oxidative phase alone, giving ribose 5-phosphate, CO₂ and 2 NADPH. Mode 3: the pentoses are recycled into glucose 6-phosphate, so that glucose 6-phosphate is oxidized completely to CO₂ and NADPH. Mode 4: the pentoses are converted into glycolytic intermediates and oxidized to pyruvate, yielding NADPH, ATP and NADH](./plots/ppp-modes.py)

### 18.6.4. Regulation and Partition of Glucose 6-Phosphate

Whether glucose 6-phosphate enters glycolysis or the pentose phosphate pathway is decided mainly at G6PD, by the availability of its substrate $\ce{NADP+}$: NADPH is a strong competitive inhibitor of the enzyme, and the free $[\ce{NADP+}]/[\mathrm{NADPH}]$ ratio in the cytosol is very low ([7.1.16](/7.1.16#sec-16.5.1)), so G6PD works far below its capacity. When reductive biosynthesis or glutathione reduction consumes NADPH, $[\ce{NADP+}]$ rises and the flux through the oxidative phase increases at once; when the demand falls, glucose 6-phosphate goes into glycolysis. This is a supply–demand system of the kind described in [7.1.17](/7.1.17#sec-17.4.4), with NADPH as the linking intermediate. Over longer times, insulin induces G6PD and 6-phosphogluconate dehydrogenase together with the enzymes of fat synthesis (7.1.26, 7.1.29).

Transketolase depends on TPP, and its activity in erythrocytes, measured with and without added TPP, is a test of thiamine status. Thiamine deficiency causes beriberi (edema, pain, paralysis, heart failure) and, especially in chronic alcoholics, whose absorption of thiamine is impaired, the Wernicke–Korsakoff syndrome (abnormal eye movements, ataxia, confusion and severe memory loss); a variant of transketolase with tenfold lower affinity for TPP makes its carriers more susceptible.

## Summary

The pathway card of glycolysis ([7.1.16](/7.1.16#sec-16.1.3)):

| Field | Glycolysis |
|---|---|
| Location | cytosol of all cells |
| Net reaction | glucose + 2 $\ce{NAD+}$ + 2 ADP + 2 $\mathrm{P_i}$ → 2 pyruvate + 2 NADH + 2 $\ce{H+}$ + 2 ATP + 2 $\ce{H2O}$ (Eq. (18.1)) |
| Energy account | 2 ATP invested (steps 1, 3), 4 made by substrate-level phosphorylation (Definition 18.2.1; steps 7, 10, twice); 2 NADH; $\Delta_{\mathrm{r}}G'^{\circ} = -85$, in cells about $-100\,\mathrm{kJ\,mol^{-1}}$; 5% of the free energy of glucose released |
| Committed and regulated steps | hexokinase (1), PFK-1 (3, committed), pyruvate kinase (10); the other seven near equilibrium |
| Activators | PFK-1: AMP, ADP, fructose 2,6-bisphosphate; pyruvate kinase: fructose 1,6-bisphosphate (feedforward) |
| Inhibitors | hexokinase I–III: glucose 6-phosphate; PFK-1: ATP, citrate, $\ce{H+}$; pyruvate kinase: ATP, acetyl-CoA, long-chain fatty acids, alanine |
| Covalent, hormonal and transcriptional control | liver pyruvate kinase L inactivated by PKA (glucagon); fructose 2,6-bisphosphate under insulin/glucagon (7.1.19); insulin and HIF-1 induce glycolytic enzymes |
| Opposing pathway | gluconeogenesis (7.1.19): bypasses at steps 1, 3, 10, reciprocal regulation |
| Coenzymes (**vitamins**) | $\ce{NAD+}$ (niacin); $\ce{Mg^2+}$, $\ce{K+}$; fermentation: TPP (thiamine) in pyruvate decarboxylase |
| Diseases and drugs | pyruvate kinase deficiency (hemolytic anemia); hereditary fructose intolerance, galactosemia; lactose intolerance; arsenate, iodoacetate, fluoride; FDG-PET; Warburg effect |

| Topic | Key points |
|---|---|
| Ten steps (18.2) | phosphorylate, isomerize, phosphorylate, cleave (C₆ → 2 C₃), isomerize; oxidize with phosphorylation (thioester, GAPDH), transfer to ADP, shift, dehydrate, transfer to ADP |
| Feeder pathways (18.3) | glycogen/starch by phosphorolysis (Glc 1-P); fructose via F6P (muscle) or F1P and aldolase B (liver, bypasses PFK-1); galactose by the Leloir pathway; mannose; glycerol |
| Fates of pyruvate (18.4) | acetyl-CoA (aerobic); lactate (LDH, −196 kJ mol⁻¹ overall); ethanol + CO₂ (pyruvate decarboxylase, TPP; −235 kJ mol⁻¹); fermentation regenerates NAD⁺ (Definition 18.4.1) |
| Pasteur and Warburg effects (Definition 18.4.2) | 2 vs ~30 ATP per glucose; aerobic glycolysis of proliferating cells: biosynthesis, HIF-1, PKM2; FDG-PET |
| Pentose phosphate pathway (Definitions 18.6.1, 18.6.2) | oxidative phase: G6PD (regulated by $\ce{NADP+}$), 6PGD → 2 NADPH + Ru5P + CO₂ (Eq. (18.2)); nonoxidative: transketolase (TPP, C₂), transaldolase (Schiff base, C₃); 6 C₅ ⇌ 5 C₆; four modes; G6PD deficiency and malaria |

## Questions

1. Glucose labeled with ¹⁴C at C-1 is fed to a yeast extract carrying out alcoholic fermentation. Where does the label appear in the ethanol? Where would it appear if the label were at C-4, and what would be the fate of label at C-3 and C-4 in lactic fermentation?

   **Answer** C-1 of glucose becomes C-3 of GAP (via DHAP and triose phosphate isomerase), the methyl carbon of pyruvate, and the methyl carbon (C-2) of ethanol. C-4 becomes C-1 of GAP, the carboxyl carbon of pyruvate, and is released as $\ce{CO2}$ by pyruvate decarboxylase; the same holds for C-3. In lactic fermentation no carbon is lost, and C-3 and C-4 end up in the carboxyl group of lactate.

2. Iodoacetate, arsenate and fluoride all inhibit glycolysis. For each, state the enzyme affected and the consequence for ATP production.

   **Answer** Iodoacetate alkylates the active-site Cys of glyceraldehyde 3-phosphate dehydrogenase and stops the pathway at step 6 (no net ATP; the two invested ATP are lost and the hexose bisphosphates accumulate). Arsenate replaces $\mathrm{P_i}$ at the same enzyme; the 1-arseno-3-phosphoglycerate hydrolyzes spontaneously to 3-phosphoglycerate, so the pathway continues but the ATP of step 7 is not made, and the net yield falls from 2 to 0 ATP per glucose. Fluoride inhibits enolase (as a $\ce{Mg^2+}$–fluorophosphate complex); 2- and 3-phosphoglycerate accumulate and the ATP of step 10 is not formed.

3. Using the erythrocyte values of the table in 18.2.1, explain why phosphoglycerate kinase can serve in gluconeogenesis while pyruvate kinase cannot, although both transfer a phosphoryl group to ADP.

   **Answer** In the cell, the GAPDH–phosphoglycerate kinase pair has $\Delta_{\mathrm{r}}G \approx -1.7\,\mathrm{kJ\,mol^{-1}}$: it is near equilibrium, and a modest change in the concentrations (more 3-phosphoglycerate, more ATP and NADH) reverses it. Pyruvate kinase operates at $\Delta_{\mathrm{r}}G \approx -17\,\mathrm{kJ\,mol^{-1}}$; by the flux–force relation ([7.1.17](/7.1.17#sec-17.3.3)) its reverse flux is less than 0.2% of the forward flux, and reversing it would require changing the mass-action ratio by more than three orders of magnitude. Gluconeogenesis therefore bypasses it with pyruvate carboxylase and PEP carboxykinase, at the cost of two extra high-energy phosphates (7.1.19).

4. A muscle works anaerobically on glycogen. How many ATP are gained per glucosyl unit converted to lactate, and per glucose taken up from the blood? Why is the difference not "free"?

   **Answer** From glycogen: phosphorolysis gives glucose 1-phosphate without ATP, so only PFK-1 consumes ATP and the yield is 3 ATP per glucosyl unit. From blood glucose: hexokinase consumes one more, 2 ATP. The saving is paid when the glycogen is made: incorporation of each glucose into glycogen costs one ATP for hexokinase and one UTP (equivalent to ATP) for UDP-glucose formation (7.1.19); storing glucose as glycogen thus costs about one ATP more than it saves on breakdown.

5. In the nonoxidative phase of the pentose phosphate pathway, verify the carbon balance of $6\,\mathrm{C_5} \to 5\,\mathrm{C_6}$ and write the net equation of mode 3, starting from six glucose 6-phosphates.

   **Answer** Carbon: $6 \times 5 = 30 = 5 \times 6$. Six glucose 6-phosphates pass through the oxidative phase: 6 G6P + 12 $\ce{NADP+}$ + 6 $\ce{H2O}$ → 6 Ru5P + 6 $\ce{CO2}$ + 12 NADPH + 12 $\ce{H+}$. The nonoxidative phase and triose phosphate isomerase, aldolase and fructose 1,6-bisphosphatase convert 6 Ru5P + $\ce{H2O}$ into 5 G6P + $\mathrm{P_i}$. Net: G6P + 12 $\ce{NADP+}$ + 7 $\ce{H2O}$ → 6 $\ce{CO2}$ + 12 NADPH + 12 $\ce{H+}$ + $\mathrm{P_i}$, the complete oxidation of one glucose 6-phosphate with all electrons in NADPH.

6. (Open question) Tumor cells often take up glucose much faster than they oxidize it and release most of its carbon as lactate. Using the energy and carbon accounts of this chapter, argue why this can be advantageous for a proliferating cell, and propose a measurement that would distinguish "defective respiration" from "biosynthetic demand" as the cause.

   **Answer** Outline: a dividing cell must double its biomass; making a palmitate or a nucleotide needs carbon skeletons and NADPH far in excess of the ATP required. A high glycolytic flux keeps the upstream intermediates (glucose 6-phosphate for the pentose phosphate pathway, 3-phosphoglycerate for serine and glycine, DHAP for glycerolipids) abundant and lets the cell regenerate $\ce{NAD+}$ cheaply by LDH; respiration would be limited by mitochondrial capacity and would push the NADH/NAD⁺ balance toward oxidation rather than synthesis. Measurement: compare oxygen consumption and its sensitivity to uncouplers and to oligomycin (an intact respiratory capacity argues against a defect), and trace ¹³C-glucose and ¹³C-glutamine into lipids, nucleotides and amino acids by mass spectrometry to quantify how much glucose carbon goes to biomass; a fall in aerobic glycolysis when proliferation stops, with respiration unchanged, would support the biosynthetic interpretation.
