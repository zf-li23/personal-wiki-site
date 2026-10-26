---
title: Gluconeogenesis, Glycogen Metabolism, and the Coordinated Regulation of Carbohydrate Metabolism
description: Gluconeogenesis and its three bypasses, energy cost and precursors; the Cori cycle; reciprocal regulation of glycolysis and gluconeogenesis by hexokinase isozymes, fructose 2,6-bisphosphate (with a quantitative model of the bifunctional enzyme), acetyl-CoA and transcription; substrate cycles; glycogen structure, breakdown and synthesis, the optimization model of the glycogen particle, glycogen storage diseases; the kinase cascade and phosphatase that regulate glycogen phosphorylase and synthase in liver and muscle; pathway cards of gluconeogenesis and glycogen metabolism.
---

Glycolysis ([7.1.18](/7.1.18)) runs in every cell; this chapter is about the opposite direction. The brain uses about 120 g of glucose a day, erythrocytes, the renal medulla, the lens and the testes depend on it almost entirely, and between meals the only sources of blood glucose are the liver's glycogen and the glucose the liver (and kidney) makes from smaller molecules. Animals therefore need two systems that run against glycolysis: gluconeogenesis, which builds glucose from pyruvate, lactate, glycerol and amino acids, and glycogen metabolism, which stores glucose as a polymer and releases it on demand. Both are read with the method of Part II ([7.1.16](/7.1.16#sec-16.1.3), [7.1.17](/7.1.17)): opposing pathways share their near-equilibrium steps, differ at the irreversible ones, and are switched by reciprocal regulation, so that the cell does not hydrolyze ATP in futile cycles. The same hormones (insulin, glucagon, epinephrine) and the same second messenger, cAMP ([7.1.14](/7.1.14#sec-14.2.2)), act on both systems; the integration with fat and amino acid metabolism in the whole body is the subject of [7.1.29](/7.1.29), and the plant counterpart (starch, sucrose, gluconeogenesis from seed oils) is in [7.1.25](/7.1.25).

## 19.1. Gluconeogenesis

### 19.1.1. Three Bypasses

**Definition 19.1.1 (Gluconeogenesis)** **Gluconeogenesis** is the synthesis of glucose from noncarbohydrate precursors (pyruvate, lactate, glycerol, glucogenic amino acids, propionate). Seven of its ten steps from pyruvate are the reverse of near-equilibrium steps of glycolysis; the three irreversible steps of glycolysis (hexokinase, PFK-1, pyruvate kinase) are bypassed by different, exergonic reactions.

Gluconeogenesis occurs in animals, plants, fungi and microorganisms with essentially the same reactions. In mammals it takes place mainly in the liver, to a smaller extent in the renal cortex (which becomes important in prolonged starvation and acidosis) and in the small intestine; only these tissues have glucose 6-phosphatase and can release glucose into the blood.

![Opposing pathways of glycolysis and gluconeogenesis in the liver. The seven shared steps operate near equilibrium in the cell (double heads). At the three irreversible steps of glycolysis (orange arcs, left) gluconeogenesis uses other enzymes (blue, right): glucose 6-phosphatase, whose active site faces the lumen of the endoplasmic reticulum; fructose 1,6-bisphosphatase (FBPase-1); and the two-step bypass of pyruvate kinase, in which pyruvate enters the mitochondrion (mitochondrial pyruvate carrier, MPC), is carboxylated to oxaloacetate by pyruvate carboxylase, reduced to malate, exported, reoxidized in the cytosol, and converted to phosphoenolpyruvate by PEP carboxykinase. When lactate is the precursor (dashed), the cytosol already has NADH from lactate dehydrogenase, and oxaloacetate is converted to PEP by the mitochondrial isozyme of PEP carboxykinase. Lactate, alanine (alanine aminotransferase, ALT) and glycerol (glycerol kinase and glycerol 3-phosphate dehydrogenase) enter on the left](./plots/glycolysis-gluconeogenesis.py)

### 19.1.2. From Pyruvate to Phosphoenolpyruvate

The pyruvate kinase reaction cannot be reversed ($\Delta_{\mathrm{r}}G \approx -17\,\mathrm{kJ\,mol^{-1}}$ in cells, [7.1.18](/7.1.18#sec-18.2.1)). Gluconeogenesis phosphorylates pyruvate by a roundabout route through oxaloacetate, a carboxylation followed by a decarboxylation.

1. In the mitochondrial matrix, pyruvate carboxylase, a **biotin** enzyme ([7.1.17](/7.1.17#sec-17.2.4)), carboxylates pyruvate:

   $$
   \text{pyruvate} + \ce{HCO3-} + \ce{ATP} \to \text{oxaloacetate} + \ce{ADP} + \mathrm{P_i}.
   $$
   Bicarbonate is first activated by ATP as carboxyphosphate and transferred to biotin; the biotinyl-Lys arm carries the carboxyl group to a second active site, on the neighboring subunit of the tetramer, where it is transferred to the enolate of pyruvate. Pyruvate carboxylase is the first regulatory enzyme of gluconeogenesis: it is almost inactive without its allosteric activator acetyl-CoA, the product of fatty acid oxidation (19.2.5). The same reaction replenishes the citric acid cycle ([7.1.20](/7.1.20)).
2. Phosphoenolpyruvate carboxykinase (PEPCK) decarboxylates and phosphorylates oxaloacetate with GTP ($\ce{Mg^2+}$):

   $$
   \text{oxaloacetate} + \ce{GTP} \rightleftharpoons \text{PEP} + \ce{CO2} + \ce{GDP}.
   $$
   The $\ce{CO2}$ fixed by pyruvate carboxylase is the one released here: the carboxylation–decarboxylation sequence activates pyruvate, because the loss of $\ce{CO2}$ drives the formation of the enolate that attacks GTP. The same trick activates acetyl-CoA for fatty acid synthesis (malonyl-CoA, [7.1.26](/7.1.26)).

The sum is

$$
\text{pyruvate} + \ce{ATP} + \ce{GTP} + \ce{HCO3-} \to \text{PEP} + \ce{ADP} + \ce{GDP} + \mathrm{P_i} + \ce{CO2}, \qquad \Delta_{\mathrm{r}}G'^{\circ} = +0.9\,\mathrm{kJ\,mol^{-1}}; \tag{19.1}
$$
two high-energy phosphates are spent to make one PEP, where glycolysis makes only one ATP from it. In the cell $\Delta_{\mathrm{r}}G \approx -25\,\mathrm{kJ\,mol^{-1}}$, because PEP is consumed as fast as it is made.

Two routes connect the two enzymes, and the choice between them is dictated by the redox balance of the cytosol. Gluconeogenesis needs one cytosolic NADH per triose (to reverse glyceraldehyde 3-phosphate dehydrogenase), but the free $[\mathrm{NADH}]/[\ce{NAD+}]$ of the cytosol is about $10^{-3}$, several orders of magnitude lower than in the matrix ([7.1.16](/7.1.16#sec-16.5.1)).

- From pyruvate or alanine: the inner mitochondrial membrane has no carrier for oxaloacetate, so mitochondrial malate dehydrogenase reduces it to malate with matrix NADH; malate leaves on the malate–α-ketoglutarate carrier and is reoxidized to oxaloacetate in the cytosol, producing there the NADH that gluconeogenesis needs. Cytosolic PEPCK then makes PEP. This route exports reducing equivalents together with carbon.
- From lactate: lactate dehydrogenase already produces cytosolic NADH. Pyruvate enters the mitochondrion, is carboxylated, and the mitochondrial isozyme of PEPCK converts oxaloacetate to PEP, which is exported. The two PEPCK isozymes are encoded by separate nuclear genes; their proportions differ between species (in humans and most mammals both are substantial, in the rat liver the cytosolic enzyme predominates).

### 19.1.3. The Two Phosphatases

The other two bypasses are simple hydrolyses of phosphate esters, not phosphoryl transfers to ADP:

$$
\begin{aligned}
&\text{fructose 1,6-bisphosphate} + \ce{H2O} \to \text{fructose 6-phosphate} + \mathrm{P_i}, && \Delta_{\mathrm{r}}G'^{\circ} = -16.3\,\mathrm{kJ\,mol^{-1}} \quad (\text{FBPase-1, } \ce{Mg^2+}),\\
&\text{glucose 6-phosphate} + \ce{H2O} \to \text{glucose} + \mathrm{P_i}, && \Delta_{\mathrm{r}}G'^{\circ} = -13.8\,\mathrm{kJ\,mol^{-1}} \quad (\text{glucose 6-phosphatase}).
\end{aligned}
$$
Glucose 6-phosphatase is an integral membrane protein of the endoplasmic reticulum of hepatocytes, renal cells and enterocytes, with its active site in the lumen. Glucose 6-phosphate is carried into the lumen by a specific transporter (T1, G6PT), and glucose and $\mathrm{P_i}$ return to the cytosol on other carriers; glucose leaves the cell on GLUT2 ([7.1.13](/7.1.13#sec-13.4.1)). Placing the phosphatase behind a membrane separates it from cytosolic glycolysis, which it would otherwise undo. Muscle, brain and adipose tissue lack the enzyme and keep their glucose 6-phosphate for themselves.

### 19.1.4. The Price of Making Glucose

Adding up the ten steps from two pyruvates (two of everything from PEP to triose phosphates),

$$
2\,\text{pyruvate} + 4\,\ce{ATP} + 2\,\ce{GTP} + 2\,\ce{NADH} + 2\,\ce{H+} + 4\,\ce{H2O} \to \text{glucose} + 4\,\ce{ADP} + 2\,\ce{GDP} + 6\,\mathrm{P_i} + 2\,\ce{NAD+}. \tag{19.2}
$$
Gluconeogenesis costs six high-energy phosphates (four ATP, two GTP) and two NADH per glucose; glycolysis returns two ATP and two NADH. The difference, four high-energy phosphates per glucose, is the cost of having both directions irreversible: under intracellular conditions $\Delta_{\mathrm{r}}G$ is about $-16\,\mathrm{kJ\,mol^{-1}}$ for gluconeogenesis and at least $-63\,\mathrm{kJ\,mol^{-1}}$ for glycolysis (Lehninger 8e; the erythrocyte concentrations of [7.1.18](/7.1.18#sec-18.2.4) give about $-100$). It is a price worth paying: pyruvate or lactate excreted would carry away more than ten ATP each of potential aerobic oxidation (7.1.20), and the alternative of a reversible pathway would leave the direction of flux to chance. In the liver the ATP comes mostly from the oxidation of fatty acids, which are abundant when gluconeogenesis is needed (7.1.21).

### 19.1.5. Precursors

Any compound that can be converted to pyruvate or oxaloacetate can be made into glucose.

| Precursor | Entry | Source |
|---|---|---|
| lactate | pyruvate (LDH) | anaerobic glycolysis in muscle and erythrocytes (Cori cycle, 19.1.6) |
| alanine, and other amino acids degraded to pyruvate (Cys, Gly, Ser, Thr, Trp) | pyruvate | muscle protein in fasting (glucose–alanine cycle) |
| amino acids degraded to citric acid cycle intermediates (Arg, Glu, Gln, His, Pro → α-ketoglutarate; Ile, Met, Thr, Val → succinyl-CoA; Phe, Tyr → fumarate; Asn, Asp → oxaloacetate) | oxaloacetate via the cycle | glutamine from muscle is the main precursor for the kidney |
| glycerol | dihydroxyacetone phosphate (glycerol kinase, glycerol 3-phosphate dehydrogenase) | lipolysis in adipose tissue (7.1.21) |
| propionate | succinyl-CoA (7.1.21) | rumen fermentation; odd-chain fatty acids |

All the common amino acids except leucine and lysine are glucogenic (several are both glucogenic and ketogenic, [7.1.22](/7.1.22)).

Mammals cannot make glucose from fatty acids with an even number of carbons. Their oxidation yields only acetyl-CoA, the pyruvate dehydrogenase reaction is irreversible (7.1.20), and in the citric acid cycle the two carbons of acetyl-CoA are matched by two carbons lost as $\ce{CO2}$, so there is no net formation of oxaloacetate. Plants, fungi and many bacteria have the glyoxylate cycle, which bypasses the two decarboxylations and does make glucose from fat ([7.1.20](/7.1.20), [7.1.25](/7.1.25)). Only the glycerol of triacylglycerols, about 5% of their energy, is glucogenic in animals.

Adipocytes have little glycerol kinase, yet need glycerol 3-phosphate to re-esterify fatty acids into triacylglycerols. They make it by *glyceroneogenesis*, a truncated gluconeogenesis from pyruvate (pyruvate carboxylase and PEPCK) to dihydroxyacetone phosphate, which is reduced to glycerol 3-phosphate ([7.1.26](/7.1.26)).

### 19.1.6. The Cori Cycle

**Definition 19.1.2 (Cori Cycle)** The **Cori cycle** is the metabolic cooperation in which lactate formed by glycolysis in skeletal muscle (and in erythrocytes) is carried by the blood to the liver, converted there to glucose by gluconeogenesis, and returned to the blood for use by muscle and other tissues.

The muscle gains 2 ATP per glucose (3 per glucosyl unit from glycogen), and the liver spends 6; the cycle therefore costs the body at least 4 high-energy phosphates per turn, paid for by oxidative metabolism in the liver. It allows muscle to work anaerobically in bursts and moves the oxygen debt to the liver; Carl and Gerty Cori described it in the 1920s–1930s. The glucose–alanine cycle is the analogous circuit for nitrogen: muscle transaminates pyruvate to alanine, which carries both carbon and amino groups to the liver, where the carbon becomes glucose and the nitrogen urea ([7.1.22](/7.1.22)).

## 19.2. Coordinated Regulation of Glycolysis and Gluconeogenesis

### 19.2.1. Three Pairs of Opposing Enzymes

At each bypass, the glycolytic and the gluconeogenic enzyme are both present in the hepatocyte cytosol. If both worked at full rate, the pair PFK-1 and FBPase-1 would simply hydrolyze ATP,

$$
\text{F6P} + \ce{ATP} \to \text{F1,6BP} + \ce{ADP}, \qquad \text{F1,6BP} + \ce{H2O} \to \text{F6P} + \mathrm{P_i}; \qquad \text{sum: } \ce{ATP} + \ce{H2O} \to \ce{ADP} + \mathrm{P_i} + \text{heat},
$$
a **substrate cycle** ([7.1.17](/7.1.17#sec-17.3.4)). The cell prevents it by regulating the two enzymes of a pair with the same signals in opposite directions.

**Definition 19.2.1 (Reciprocal Regulation)** **Reciprocal regulation** is the control of the two opposing enzymes of a substrate cycle, or of two opposing pathways, by common effectors or covalent modifications that activate one while inhibiting the other.

| Pair (glycolysis / gluconeogenesis) | Allosteric signals | Covalent and hormonal control | Transcription |
|---|---|---|---|
| hexokinase IV (glucokinase) / glucose 6-phosphatase | glucose; fructose 6-phosphate via the regulatory protein (19.2.2) | — | insulin induces glucokinase; glucagon and cortisol induce glucose 6-phosphatase |
| PFK-1 / FBPase-1 | AMP and fructose 2,6-bisphosphate activate PFK-1, inhibit FBPase-1; ATP and citrate inhibit PFK-1 | glucagon lowers fructose 2,6-bisphosphate (19.2.3) | insulin induces PFK-1 and PFK-2 |
| pyruvate kinase L / pyruvate carboxylase + PEPCK | fructose 1,6-bisphosphate activates, ATP and alanine inhibit pyruvate kinase; acetyl-CoA activates pyruvate carboxylase | PKA phosphorylates and inactivates pyruvate kinase L | glucagon induces PEPCK; insulin represses it |
| pyruvate dehydrogenase (oxidation) / pyruvate carboxylase | acetyl-CoA inhibits PDH, activates pyruvate carboxylase | PDH kinase (7.1.20) | — |

The three irreversible steps are the only places where the direction of flux can be set; the seven near-equilibrium enzymes follow whatever the ends impose ([7.1.17](/7.1.17#sec-17.3.3)).

### 19.2.2. Hexokinase Isozymes and the Glucose Sensor of the Liver

The **isozymes** of hexokinase suit the different roles of muscle and liver ([7.1.18](/7.1.18#sec-18.5.2)). Muscle consumes glucose: hexokinases I and II have $K_{\mathrm{M}} \approx 0.1\,\mathrm{mM}$, are saturated at the 4–5 mM of blood glucose, and are inhibited by their product. The liver buffers blood glucose, taking it up after a meal and releasing it in fasting.

**Definition 19.2.2 (Glucokinase)** **Glucokinase** (hexokinase IV) is the hexokinase isozyme of hepatocytes and pancreatic β cells. It has a half-saturating glucose concentration $K_{0.5}$ of about 8–10 mM, above the normal blood glucose, a sigmoid response to glucose (Hill coefficient about 1.7) although it is a monomer, no inhibition by glucose 6-phosphate, and it is inhibited by sequestration in the nucleus by the glucokinase regulatory protein (GKRP).

GLUT2, a high-capacity transporter, equilibrates hepatocyte glucose with the portal blood, which after a meal reaches 10 mM and more. Because glucokinase is far from saturation, its rate follows the glucose concentration: its elasticity ([7.1.17](/7.1.17#sec-17.4.1)) is above 1 in the physiological range, that of hexokinase I nearly zero. The sigmoid kinetics of a monomer, a rare case of kinetic **cooperativity** without multiple sites, arise from a slow conformational transition between a low-affinity and a high-affinity form (mnemonic kinetics).

![Hexokinase I and glucokinase. A: relative rate against glucose for hexokinase I (Michaelis–Menten, K_M = 0.1 mM) and glucokinase (Hill equation, K₀.₅ = 8 mM, n_H = 1.7); shaded, the range of blood glucose after an overnight fast and of portal blood after a carbohydrate meal. Hexokinase I is saturated in both, glucokinase is not. B: elasticity of the rate to glucose, the fractional change of rate for a fractional change of glucose: about 1.1–1.3 for glucokinase at fasting glucose, below 0.03 for hexokinase I](./plots/hexokinase-isozymes.py)

GKRP adds a second, faster switch. Fructose 6-phosphate promotes the binding of glucokinase to GKRP, which anchors it in the nucleus, away from the glycolytic enzymes; glucose (and fructose 1-phosphate, from dietary fructose) promotes its release, and glucokinase returns to the cytosol within minutes after a meal. In fasting the liver thus stops phosphorylating glucose and does not compete with the brain. Over hours, insulin induces the synthesis of glucokinase. In the β cell, glucokinase is the glucose sensor that sets the threshold for insulin secretion: heterozygous inactivating mutations of *GCK* cause a mild, lifelong fasting hyperglycemia (GCK-MODY), activating mutations hypoglycemia from excess insulin, and pharmacological glucokinase activators are used in type 2 diabetes ([7.1.29](/7.1.29)).

### 19.2.3. Fructose 2,6-Bisphosphate

The special task of the liver, to keep blood glucose constant whatever its own needs, requires a signal that is set by hormones rather than by the cell's energy state. This signal is a regulatory molecule that is not an intermediate of either pathway.

**Definition 19.2.3 (Fructose 2,6-Bisphosphate)** **Fructose 2,6-bisphosphate** (F2,6BP) is an allosteric regulator, present at micromolar concentrations, that activates PFK-1 and inhibits FBPase-1. It is made from fructose 6-phosphate and ATP by phosphofructokinase-2 (PFK-2) and hydrolyzed to fructose 6-phosphate and $\mathrm{P_i}$ by fructose 2,6-bisphosphatase (FBPase-2); the two activities reside in separate domains of a single bifunctional polypeptide, PFK-2/FBPase-2.

```smiles
O=P([O-])([O-])OC[C@H]1O[C@](O)(COP(=O)([O-])[O-])[C@@H](O)[C@@H]1O F6P
O=P([O-])([O-])OC[C@H]1O[C@@](OP(=O)([O-])[O-])(CO)[C@@H](O)[C@@H]1O F2,6BP
```

F2,6BP (discovered by Hers, Van Schaftingen and Uyeda around 1980) differs from fructose 6-phosphate by a phosphate on the anomeric hydroxyl of the β-furanose. It raises the affinity of PFK-1 for fructose 6-phosphate and lowers its sensitivity to ATP and citrate: in Lehninger's data the $K_{0.5}$ of PFK-1 for fructose 6-phosphate falls from 2 mM without F2,6BP to 0.08 mM with 0.13 µM, and at physiological concentrations of the other effectors PFK-1 is nearly inactive without it ([7.1.18](/7.1.18#sec-18.5.1)). On FBPase-1 it acts in the opposite sense: 1 µM inhibits, 25 µM raises $K_{0.5}$ for fructose 1,6-bisphosphate from 5 µM to more than 70 µM, and F2,6BP makes FBPase-1 more sensitive to inhibition by AMP.

The level of F2,6BP is set by the balance of the two activities of the bifunctional enzyme, and that balance by hormones. Glucagon, through cAMP and protein kinase A (PKA), phosphorylates the liver isoform on Ser32 near its N-terminus: the kinase activity falls, the bisphosphatase rises, F2,6BP falls, PFK-1 slows and FBPase-1 speeds up; the liver turns from consuming glucose to making it. Insulin has the opposite effect, by favoring the dephosphorylation of the enzyme by a phosphoprotein phosphatase. After a carbohydrate meal, xylulose 5-phosphate, formed in the pentose phosphate pathway, has been proposed to activate protein phosphatase 2A (PP2A), which dephosphorylates PFK-2/FBPase-2 and raises F2,6BP. The isoforms in heart and other tissues are regulated differently (the cardiac isoform is activated by phosphorylation by AMPK and other kinases during ischemia), consistent with the role of these tissues as consumers of glucose.

![Control of the glycolytic and gluconeogenic flux in the hepatocyte by fructose 2,6-bisphosphate, in SBGN process description notation. Glucagon, through cAMP, activates PKA, which phosphorylates PFK-2/FBPase-2; the phosphorylated form is a bisphosphatase, the dephosphorylated form a kinase. PP2A (activated by xylulose 5-phosphate; insulin acts indirectly in the same direction) dephosphorylates it. Fructose 2,6-bisphosphate stimulates PFK-1 and inhibits FBPase-1; AMP acts in the same sense, citrate inhibits PFK-1. Squares: processes; open circles: catalysis; open arrowheads: stimulation; bars: inhibition; hexagons: outcomes](./plots/f26bp-control.py)

### 19.2.4. A Model of the Hormonal Switch

The logic of the system becomes clear in a minimal model. Let $\varphi$ be the fraction of the bifunctional enzyme phosphorylated by PKA. With first-order phosphorylation ($k_{\mathrm{p}}$, proportional to PKA activity) and dephosphorylation ($k_{\mathrm{d}}$, proportional to phosphatase activity), the steady state is $\varphi = s/(1 + s)$ with $s = k_{\mathrm{p}}/k_{\mathrm{d}}$.

**Formula 19.2.1 (Bifunctional-Enzyme Model)** With $X = [\text{F2,6BP}]$ and $F = [\text{F6P}]$,

$$
\frac{\mathrm{d}X}{\mathrm{d}t} = V_{\mathrm{K}}(\varphi)\,\frac{F}{K_{\mathrm{F}} + F} - V_{\mathrm{B}}(\varphi)\,\frac{X}{K_{X} + X}, \qquad
V_{\mathrm{K}} = V_{\mathrm{K}}^0\,[(1 - \varphi) + a\varphi], \quad V_{\mathrm{B}} = V_{\mathrm{B}}^0\,[b(1 - \varphi) + \varphi], \tag{19.3}
$$
where $a < 1$ and $b < 1$ express that phosphorylation inhibits the kinase and activates the bisphosphatase. The steady state is

$$
X^* = K_X\,\frac{V_{\mathrm{K}}\,F/(K_{\mathrm{F}} + F)}{V_{\mathrm{B}} - V_{\mathrm{K}}\,F/(K_{\mathrm{F}} + F)}, \tag{19.4}
$$
and the relative activities of the substrate cycle are $\mathrm{PFK\text{-}1} = (f_0 + X/K_{\mathrm{a}})/(1 + X/K_{\mathrm{a}})$ and $\mathrm{FBPase\text{-}1} = 1/[1 + (X/K_{\mathrm{i}})^{n}]$, with net glycolytic flux $J = \mathrm{PFK\text{-}1} - \mathrm{FBPase\text{-}1}$.

Each parameter has a biological meaning: $V_{\mathrm{K}}^0$ and $V_{\mathrm{B}}^0$ are the amounts of the two activities (set by transcription over hours), $a$ and $b$ the effect of phosphorylation, $K_{\mathrm{a}}$ and $K_{\mathrm{i}}$ the affinities of PFK-1 and FBPase-1 for the regulator, and $s$ the hormonal state, glucagon versus insulin. Because one protein carries both activities, a single covalent modification moves the two rates in opposite directions, and $X^*$ changes about a hundredfold over the physiological range of $s$; the two target enzymes, acting in opposite senses, turn this into a reversal of the net flux, $J$ changing sign at a threshold. The response time is set by the turnover of the small pool of F2,6BP ($K_X/V_{\mathrm{B}}$, minutes), much faster than changes in enzyme amount.

![A minimal model of the switch (Formula 19.2.1; illustrative parameters V_K⁰ = 0.15 and V_B⁰ = 1.0 µM min⁻¹, a = 0.1, b = 0.2, [F6P] = 0.05 mM, K_F = 0.03 mM, K_X = 5 µM, K_a = 0.5 µM, f₀ = 0.05, K_i = 1 µM, n = 1.5). A: steady-state [F2,6BP] against the ratio of PKA to phosphatase activity, from about 4 µM in the insulin-dominated fed state to about 0.05 µM in the glucagon-dominated fasted state. B: relative activities of PFK-1 and FBPase-1 and the net flux through the fructose 6-phosphate/fructose 1,6-bisphosphate cycle, which changes sign near a ratio of 0.5. C: time course after glucagon is applied (t = 10–60 min; k_p raised from 0.05 to 5 min⁻¹, k_d = 0.5 min⁻¹): phosphorylation is fast, F2,6BP falls within about 10 min and the cycle turns to gluconeogenesis; after glucagon is withdrawn, F2,6BP recovers over tens of minutes](./plots/f26bp-model.py)

### 19.2.5. The Fate of Pyruvate and Pyruvate Kinase

In liver mitochondria the first control point decides whether pyruvate is oxidized (pyruvate dehydrogenase, 7.1.20) or carboxylated (pyruvate carboxylase). When fatty acids are abundant, their β oxidation (7.1.21) yields acetyl-CoA and NADH; acetyl-CoA inhibits the pyruvate dehydrogenase complex (by activating PDH kinase) and activates pyruvate carboxylase, so pyruvate is spared for gluconeogenesis and the oxidation of fat supplies its ATP. Pyruvate carboxylase is therefore both the entry to gluconeogenesis and the main anaplerotic enzyme of the liver; acetyl-CoA asks for oxaloacetate in either role.

The liver isozyme of pyruvate kinase (L) is the third control point. Glucagon, through PKA, phosphorylates and inactivates it, so that PEP made by PEPCK is not converted back to pyruvate; ATP, acetyl-CoA, long-chain fatty acids and alanine inhibit it allosterically, fructose 1,6-bisphosphate activates it (feedforward). PEPCK itself has no known allosteric regulator; it is regulated by the amount of enzyme.

### 19.2.6. Transcriptional Control

Allosteric and covalent regulation act within seconds to minutes; a change in diet or a prolonged fast changes the amount of the enzymes within hours ([7.1.17](/7.1.17#sec-17.3.2)). Insulin, through its receptor, PI3K–PKB and other kinases ([7.1.15](/7.1.15#sec-15.1.5)), regulates the transcription of more than 150 genes. It induces the enzymes that use glucose (hexokinase II and IV, PFK-1, PFK-2/FBPase-2, pyruvate kinase), those that make NADPH and acetyl-CoA for fat synthesis (glucose 6-phosphate dehydrogenase, malic enzyme, ATP-citrate lyase, PDH) and those of fat synthesis (acetyl-CoA carboxylase, fatty acid synthase), and it represses PEPCK and the catalytic subunit of glucose 6-phosphatase.

- Glucagon (through cAMP, PKA and the transcription factor CREB with its coactivator CRTC2) and glucocorticoids induce PEPCK and glucose 6-phosphatase; the coactivator PGC-1α, itself induced in fasting, coordinates the gluconeogenic program. Insulin opposes this: PKB phosphorylates the transcription factor FOXO1, which is then excluded from the nucleus.
- The carbohydrate response element binding protein (ChREBP), with its partner Mlx, induces pyruvate kinase L and the enzymes of fat synthesis when glucose is abundant. Lehninger 8e presents its activation by xylulose 5-phosphate and PP2A, which dephosphorylate it and allow it to enter the nucleus; more recent work indicates that glucose 6-phosphate and other glucose metabolites activate ChREBP directly through a glucose-sensing module, and the relative importance of the two mechanisms is debated.

### 19.2.7. Substrate Cycles Quantitatively

Reciprocal regulation does not stop the opposing enzymes completely: in liver the PFK-1/FBPase-1 and glucose/glucose 6-phosphate cycles run at measurable rates, a few to some tens of percent of the net flux, as shown with isotopes. Equation (17.2) of [7.1.17](/7.1.17#sec-17.3.4) gives the benefit. Write $v_{\mathrm{r}} = r v_{\mathrm{f}}$; an effector that changes both enzymes by the same fraction $a$, in opposite directions, gives

$$
\frac{J(a)}{J(0)} = \frac{(1 + a) - r(1 - a)}{1 - r}, \qquad \frac{\Delta J}{J} = a\,\frac{1 + r}{1 - r}, \qquad \frac{\text{ATP hydrolyzed by cycling}}{\text{net flux}} = \frac{r}{1 - r}. \tag{19.5}
$$
The amplification and the cost grow together. At $r = 0.5$ the amplification is 3 for a cost of one extra ATP per unit of net flux; at $r = 0.9$ it is 19 for a cost of 9. A cell can afford high cycling only where the ATP is cheap or the heat is useful. Newsholme and Crabtree, who developed this argument, pointed to the flight muscle of bumblebees, which was reported to have a high FBPase-1 activity and to cycle fructose 6-phosphate for heat production in the cold; later measurements found little FBPase-1 activity in most bumblebee species, and the thermogenic role is now doubted. Mammalian thermogenesis uses uncoupling in brown fat instead (7.1.23). The same amplification, without cycling cost, is obtained by **zero-order ultrasensitivity** in covalent modification cycles ([7.1.9](/7.1.9#sec-9.6.1)), a cycle of the enzyme rather than of the metabolite.

![Sensitivity amplification by a substrate cycle (Eq. (19.5)). A: net flux J relative to its initial value, when an effector changes the forward and reverse enzymes by the fraction a in opposite directions, for cycling ratios r = v_r/v_f of 0 (no cycling), 0.5, 0.8 and 0.9: a 10% change in the enzymes changes J by 10%, 30%, 90% and 190%. B: the amplification factor (1 + r)/(1 − r) and the ATP hydrolyzed by cycling per unit of net flux, r/(1 − r), against r; the two rise together, steeply as r approaches 1](./plots/substrate-cycle.py)

## 19.3. Glycogen Structure and Breakdown

### 19.3.1. The Glycogen Particle

**Glycogen** ([7.1.10](/7.1.10#sec-10.3.2)) is stored in the cytosol, mainly in liver (5–10% of the wet weight after a meal; about 100 g in an adult) and in skeletal muscle (1–2%, but up to about 400 g in total because of the mass of muscle). The energy stored as glycogen is about 1% of that stored as fat, but glycogen has two advantages that fat lacks: it can be mobilized within seconds, and its glucose can be used anaerobically. Liver glycogen maintains blood glucose between meals; muscle glycogen fuels the muscle itself. Storing the same glucose as monomers would raise the cytosolic osmolarity by about 0.4 M ([7.1.10](/7.1.10#sec-10.3.2), Example 10.3.1).

The unit of storage is the β particle, about 20–30 nm in diameter in muscle, with up to about 55 000 glucose residues ($M_{\mathrm{r}} \approx 10^7$). At its core is a dimer of the protein glycogenin (19.4.3), from which chains of about 13 (α1→4)-linked residues radiate in tiers: inner B chains carry two (α1→6) branches each, outer A chains are unbranched and make up about half of all chains. In the liver, 20–40 β particles cluster into α particles of up to 300 nm, which are visible in the electron microscope after a meal and disappear after a day of fasting. The enzymes of synthesis and degradation and their regulators are bound to the particles.

### 19.3.2. Glycogen Phosphorylase

**Definition 19.3.1 (Phosphorolysis and Glycogen Phosphorylase)** **Phosphorolysis** is the cleavage of a bond by attack of inorganic phosphate, which becomes attached to one of the products. **Glycogen phosphorylase** catalyzes the phosphorolysis of the terminal (α1→4) **glycosidic bond** at a nonreducing end of glycogen, releasing α-D-glucose 1-phosphate:

$$
(\text{glucose})_n + \mathrm{P_i} \rightleftharpoons (\text{glucose})_{n-1} + \text{glucose 1-phosphate}.
$$
It acts repeatedly on the same chain and stops four residues from an (α1→6) branch point.

Phosphorolysis conserves part of the energy of the glycosidic bond in the phosphate ester, so the glucose residue enters glycolysis without spending ATP ([7.1.18](/7.1.18#sec-18.3.1)). The reaction is nearly balanced ($\Delta_{\mathrm{r}}G'^{\circ} = +3.1\,\mathrm{kJ\,mol^{-1}}$); it runs toward breakdown in the cell because $[\mathrm{P_i}]/[\text{glucose 1-phosphate}]$ is above 100 (Question 2). The coenzyme is **pyridoxal phosphate**, bound as a Schiff base to Lys680, but in an unusual role ([7.1.17](/7.1.17#sec-17.2.3)): its phosphate group acts as a general acid–base catalyst that protonates the incoming $\mathrm{P_i}$, which in turn protonates the glycosidic oxygen; the departing glycogen chain leaves an oxocarbenium-like glucosyl cation, which $\mathrm{P_i}$ attacks with retention of the α configuration.

Glycogen phosphorylase is a dimer of 97 kDa subunits and one of the first enzymes shown to be allosterically regulated (Cori, 1930s), the first shown to be regulated by reversible phosphorylation (Krebs and Fischer, 1955–1959), and among the first whose active and inactive conformations were solved by crystallography; its regulation is the subject of 19.5.

### 19.3.3. The Debranching Enzyme

**Definition 19.3.2 (Debranching Enzyme)** The glycogen **debranching enzyme** is a bifunctional enzyme with two activities. Its oligo(α1→6) to (α1→4) glucantransferase activity moves a block of three glucose residues from a branch that phosphorylase has shortened to four residues onto a nearby nonreducing end, joining them in (α1→4) linkage; its amylo-(α1→6)-glucosidase activity then hydrolyzes the single residue left at the branch point, releasing free glucose.

About one residue in ten of glycogen (the branch points) is thus released as glucose rather than glucose 1-phosphate. Starch phosphorylase and debranching enzymes do the same work in plants (7.1.25).

![The enzymes that act on glycogen chains, drawn with the SNFG symbol for glucose (blue circles); chains run from the reducing end on the left to nonreducing ends on the right, vertical links are (α1→6) branch points, dashed outlines are residues removed in the step shown. A: glycogen phosphorylase phosphorolyzes the terminal residues of the outer chains to glucose 1-phosphate and stops four residues from a branch point. B: the transferase activity of the debranching enzyme moves three of the four residues of the limit branch to a nonreducing end. C: its (α1→6)-glucosidase activity hydrolyzes the remaining residue to free glucose, leaving an unbranched chain. D: glycogen synthase lengthens chains from UDP-glucose; when a chain has at least 11 residues, the branching enzyme moves its terminal 6–7 residues (outlined) to the C-6 hydroxyl of a residue farther in, creating a new branch and a new nonreducing end](./plots/glycogen-enzymes.py)

### 19.3.4. The Fates of Glucose 1-Phosphate

Phosphoglucomutase converts glucose 1-phosphate to glucose 6-phosphate ($K' = 19$, Example 16.2.1 of [7.1.16](/7.1.16#sec-16.2.1)). Its active-site Ser is phosphorylated; it transfers this phosphoryl group to C-6, forming glucose 1,6-bisphosphate, and takes back the phosphoryl group from C-1. In muscle, glucose 6-phosphate enters glycolysis; in liver, it is hydrolyzed by glucose 6-phosphatase in the ER and leaves the cell as glucose (19.1.3). The two tissues thus use the same polymer for opposite purposes: the muscle is selfish, the liver altruistic.

### 19.3.5. Glycogen Storage Diseases

**Definition 19.3.3 (Glycogen Storage Disease)** A **glycogen storage disease** is an inherited defect of an enzyme or transporter of glycogen metabolism that causes abnormal amounts or structure of glycogen in liver, muscle or both.

Gerty Cori identified the enzyme defects of several of them in biopsy samples in the 1950s, the first diseases explained by a missing enzyme activity.

| Type (name) | Defect | Organ | Main features |
|---|---|---|---|
| 0 | glycogen synthase (liver) | liver | fasting hypoglycemia, ketosis; little glycogen |
| Ia (von Gierke) | glucose 6-phosphatase | liver, kidney | severe fasting hypoglycemia, lactic acidosis, hyperuricemia, enlarged liver and kidneys |
| Ib | glucose 6-phosphate transporter (T1) | liver; neutrophils | as Ia, with neutropenia and infections |
| II (Pompe) | lysosomal α-glucosidase (acid maltase) | all tissues, mainly heart and skeletal muscle | infantile form: cardiomyopathy, death in the first years without treatment; later forms: myopathy; treated by enzyme replacement |
| III (Cori, Forbes) | debranching enzyme | liver, muscle | enlarged liver, hypoglycemia, myopathy; glycogen with short outer chains |
| IV (Andersen) | branching enzyme | liver, muscle | glycogen with long unbranched chains; liver cirrhosis |
| V (McArdle) | muscle phosphorylase | skeletal muscle | exercise intolerance, cramps, myoglobinuria; no rise of blood lactate on ischemic exercise |
| VI (Hers) | liver phosphorylase | liver | enlarged liver, mild hypoglycemia |
| VII (Tarui) | muscle PFK-1 | muscle, erythrocytes | as V, with hemolysis |
| IX | phosphorylase kinase | liver, muscle | enlarged liver (liver forms); usually mild |
| XI (Fanconi–Bickel) | GLUT2 | liver, kidney, intestine | glycogen in liver and kidney, renal tubular dysfunction |

The pattern of symptoms follows from the roles of the two tissues: liver defects cause fasting hypoglycemia and an enlarged liver; muscle defects cause weakness and cramps on exercise. In von Gierke disease, glucose 6-phosphate that cannot be hydrolyzed is diverted into glycolysis (lactate), the pentose phosphate pathway and nucleotide synthesis (uric acid) and fat synthesis (hyperlipidemia); the patients are treated with frequent meals and slowly digested starch.

## 19.4. Glycogen Synthesis

### 19.4.1. Sugar Nucleotides

Glycogen phosphorylase is reversible in vitro, and the Coris used it in 1939 to make glycogen from glucose 1-phosphate, the first synthesis of a macromolecule in a test tube. But the [Pi]/[glucose 1-phosphate] ratio in cells excludes it as the route of synthesis, and opposing pathways need different enzymes. Luis Leloir found that the activated form of glucose is a nucleotide (Nobel Prize in Chemistry 1970): UDP-glucose was identified around 1950 as the coenzyme of galactose epimerization ([7.1.18](/7.1.18#sec-18.3.2)), and in 1957 Leloir and Cardini showed that glycogen is synthesized from UDP-glucose.

**Definition 19.4.1 (Sugar Nucleotide)** A **sugar nucleotide** is a compound in which the anomeric carbon of a sugar is esterified through a pyrophosphate bridge to a nucleoside 5′-monophosphate (UDP-glucose, ADP-glucose, GDP-mannose, CMP-sialic acid with a single phosphate). Sugar nucleotides are the donors in the synthesis of polysaccharides and glycoconjugates and the substrates of sugar interconversions.

```smiles
OC[C@H]1O[C@H](OP(=O)([O-])OP(=O)([O-])OC[C@H]2O[C@@H](n3ccc(=O)[nH]c3=O)[C@H](O)[C@@H]2O)[C@H](O)[C@@H](O)[C@@H]1O UDP-glucose
```

UDP-glucose pyrophosphorylase (named for the reverse reaction) makes it from glucose 1-phosphate and UTP:

$$
\text{glucose 1-phosphate} + \ce{UTP} \rightleftharpoons \text{UDP-glucose} + \mathrm{PP_i}, \qquad \mathrm{PP_i} + \ce{H2O} \to 2\,\mathrm{P_i} \quad (\Delta_{\mathrm{r}}G'^{\circ} = -19.2\,\mathrm{kJ\,mol^{-1}}).
$$
The condensation itself is nearly balanced; the hydrolysis of pyrophosphate by inorganic pyrophosphatase keeps $[\mathrm{PP_i}]$ low and pulls it forward, a strategy common to biosynthetic polymerizations ([7.1.16](/7.1.16#sec-16.3.4)). Sugar nucleotides suit their role for four reasons: their formation is made irreversible by $\mathrm{PP_i}$ hydrolysis; the nucleotide provides binding energy for the enzymes ([7.1.8](/7.1.8#sec-8.3.1)); the nucleoside diphosphate is a good leaving group; and the tag sets aside a pool of hexoses for one purpose, separate from the hexose phosphates of glycolysis.

### 19.4.2. Glycogen Synthase and the Branching Enzyme

**Definition 19.4.2 (Glycogen Synthase and Branching Enzyme)** **Glycogen synthase** transfers the glucosyl residue of UDP-glucose to the C-4 hydroxyl of a nonreducing end of glycogen, forming an (α1→4) linkage; it needs a primer of at least four residues. The **branching enzyme** (glycogen-branching enzyme, amylo-(1→4) to (1→6) transglycosylase) transfers a terminal segment of 6 or 7 residues from a chain of at least 11 residues to the C-6 hydroxyl of a residue farther inside the same or another chain, creating an (α1→6) branch.

The overall path from glucose 6-phosphate,

$$
\text{G6P} \rightleftharpoons \text{G1P}, \quad \text{G1P} + \ce{UTP} \to \text{UDP-glucose} + 2\,\mathrm{P_i}, \quad \text{UDP-glucose} + (\text{glucose})_n \to (\text{glucose})_{n+1} + \ce{UDP},
$$
costs one UTP per residue (regenerated from UDP by **nucleoside diphosphate kinase** at the cost of one ATP), and one more ATP if the glucose comes from the blood (hexokinase). Synthesis and breakdown together lose one high-energy phosphate per residue cycled (Question 4 of [7.1.18](/7.1.18)). Branching serves both directions: it increases the number of nonreducing ends at which synthase and phosphorylase act, and the solubility of the polymer.

### 19.4.3. Glycogenin

Glycogen synthase cannot start a chain. The primer is a protein.

**Definition 19.4.3 (Glycogenin)** **Glycogenin** is a glycosyltransferase that is both the primer and the catalyst of the first steps of glycogen synthesis. Each subunit of the glycogenin dimer transfers a glucose residue from UDP-glucose to Tyr194 of the other subunit, and then extends the chain to about eight (α1→4)-linked residues, after which glycogen synthase, bound to glycogenin, continues.

The transfer to Tyr194 keeps the configuration at C-1 of the glucose, which suggests two successive displacements (an inverting attack by an Asp residue and a second inversion by the Tyr); the UDP leaving group is stabilized by $\ce{Mn^2+}$. Glycogenin remains at the core of the particle, attached to its reducing ends, so a glycogen particle has as many reducing ends as glycogenin subunits.

### 19.4.4. Why Glycogen Is Built as It Is

The structure of the β particle is close to the best possible for its function, as Meléndez-Hevia, Waddell and Shelton (1993) showed with a simple model. Consider a particle of $t$ tiers, each chain with $g_{\mathrm{c}}$ residues, every inner chain branched twice. Counting chains tier by tier (1, 2, 4, … with the primer counted as one chain) gives the number of outer A chains, accessible to phosphorylase, the total number of chains and residues, and the glucose phosphorylase can release from the outer tier before debranching (it stops four residues from a branch point):

$$
C_{\mathrm{A}} = 2^{t-1}, \qquad C_{\mathrm{T}} = 2^{t} - 1, \qquad G_{\mathrm{T}} = g_{\mathrm{c}}(2^{t} - 1), \qquad G_{\mathrm{PT}} = (g_{\mathrm{c}} - 4)\,2^{t-1}.
$$
Each tier is $0.12\,g_{\mathrm{c}} + 0.35\,\mathrm{nm}$ thick, so the particle has the volume $V_{\mathrm{s}} = \tfrac43\pi t^{3}(0.12\,g_{\mathrm{c}} + 0.35)^{3}\,\mathrm{nm^3}$.

**Formula 19.4.1 (Quality Function of the Glycogen Particle)** A good store holds much glucose ($G_{\mathrm{T}}$), offers many ends for rapid mobilization ($C_{\mathrm{A}}$) and much immediately available glucose ($G_{\mathrm{PT}}$), in a small volume:

$$
f = \frac{G_{\mathrm{T}}\,C_{\mathrm{A}}\,G_{\mathrm{PT}}}{V_{\mathrm{s}}} = \frac{3\,(2^{t} - 1)\,4^{t-1}}{4\pi t^{3}} \cdot \frac{g_{\mathrm{c}}(g_{\mathrm{c}} - 4)}{(0.12\,g_{\mathrm{c}} + 0.35)^{3}}. \tag{19.6}
$$

The function factors into a part depending only on $t$ and a part depending only on $g_{\mathrm{c}}$, so the optimal chain length is independent of the number of tiers. Setting the derivative of $g(g - 4)/(0.12g + 0.35)^3$ to zero gives $0.12g^2 - 1.66g + 1.4 = 0$, $g_{\mathrm{c}} \approx 12.9$: short chains waste the outer tier on branch points, long chains make the particle bulky without adding ends. The measured chain length of glycogen is 12–14. Two branches per chain is also optimal: one branch per chain gives too few ends, and more than two crowd the inner tiers. The number of tiers is limited by crowding. The number of residues in the outer tier doubles with each tier, while its volume grows only as $t^2$; with 0.18 nm³ per residue (density about 1.5 g cm⁻³), the outermost tier would be 40% filled with glucose at 12 tiers, 70% at 13 and impossibly more than 100% at 14, leaving no room for the enzymes, which work at the surface. A complete particle of 12 tiers holds $13(2^{12} - 1) \approx 53\,000$ residues, close to the 55 000 observed, with a radius of $12 \times 1.91 \approx 23\,\mathrm{nm}$.

![The optimization model of the glycogen particle (Formula 19.4.1). A: schematic of a particle with five tiers around the glycogenin core: inner B chains (blue) branch twice, the outer tier consists of unbranched A chains (green). B: the quality function f = G_T C_A G_PT / V_s against the chain length g_c, normalized to its maximum; the optimum at g_c ≈ 12.9 does not depend on the number of tiers and falls within the observed range (shaded). C: glucose residues per particle (log scale; 53 000 at 12 tiers) and the estimated fraction of the volume of the outermost tier occupied by glucose residues (right scale), for g_c = 13; above 13 tiers the outer tier would have to be more than full](./plots/glycogen-optimization.py)

The argument is an example of a style of reasoning that recurs in biology: a structure produced by natural selection can be compared with the solution of an optimization problem, and agreement suggests which constraints selection has acted on. Amylopectin, which is not mobilized as fast, has longer chains and a different, clustered organization (7.1.25).

## 19.5. Coordinated Regulation of Glycogen Metabolism

### 19.5.1. Phosphorylase a and b and the Kinase Cascade

Glycogen phosphorylase exists in two interconvertible forms ([7.1.9](/7.1.9#sec-9.5.3)): the more active phosphorylase *a*, phosphorylated on Ser14 of each subunit, and the less active phosphorylase *b*. Phosphorylation shifts the T ⇌ R equilibrium of the dimer toward the active **R state** ([7.1.7](/7.1.7)); allosteric effectors act on the same equilibrium.

**Definition 19.5.1 (Phosphorylase Kinase)** **Phosphorylase kinase** is the protein kinase that phosphorylates Ser14 of glycogen phosphorylase *b*, converting it to phosphorylase *a*. It is a large complex $(\alpha\beta\gamma\delta)_4$ of 1.3 MDa in which γ is the catalytic subunit, δ is calmodulin, and α and β are regulatory subunits that are phosphorylated by PKA; it is fully active only when both phosphorylated and bound to $\ce{Ca^2+}$.

Epinephrine (in muscle and liver) and glucagon (in liver) act through receptors coupled to $\mathrm{G_s}$, adenylyl cyclase, cAMP and PKA ([7.1.14](/7.1.14#sec-14.2.2)). PKA phosphorylates phosphorylase kinase, which phosphorylates phosphorylase. This **enzyme cascade**, a catalyst activating a catalyst activating a catalyst, was the first described (Sutherland discovered cAMP while studying the effect of epinephrine on liver phosphorylase, Nobel Prize 1971; Krebs and Fischer discovered phosphorylase kinase, Nobel Prize 1992). Each stage amplifies the signal by the number of substrate molecules one enzyme converts during its active lifetime ([7.1.9](/7.1.9#sec-9.6.2)), so that a few hormone molecules mobilize millions of glucose residues within seconds. When the signal ends, phosphoprotein phosphatase 1 (PP1) dephosphorylates phosphorylase *a* and phosphorylase kinase.

![Reciprocal covalent regulation of glycogen breakdown and synthesis, in SBGN process description notation. Left: epinephrine or glucagon raises cAMP and activates PKA, which phosphorylates phosphorylase kinase; phosphorylase kinase, also activated by Ca²⁺, converts phosphorylase b to the active phosphorylase a. AMP activates phosphorylase b allosterically (muscle); glucose binding to phosphorylase a (liver) promotes its dephosphorylation. Right: GSK3, after priming phosphorylation by casein kinase II (CKII), converts glycogen synthase a to the inactive b form; insulin, through PKB, phosphorylates and inactivates GSK3. Bottom: PP1, activated by insulin (and inhibited by phosphorylase a in the liver), dephosphorylates phosphorylase a and glycogen synthase b; glucose 6-phosphate stimulates the dephosphorylation of glycogen synthase and activates synthase b allosterically. Hexagons: outcomes](./plots/glycogen-cascade.py)

### 19.5.2. Allosteric Control: Muscle and Liver

Superimposed on the hormonal control are allosteric signals, different in the two tissues because the isozymes of phosphorylase (encoded by different genes) have different regulatory sites.

- In muscle, the signals report contraction and energy state. $\ce{Ca^2+}$, released into the cytosol at each nerve impulse, binds the calmodulin subunit of phosphorylase kinase and activates it, so that glycogen breakdown starts with contraction even without epinephrine. AMP, which rises steeply when ATP is consumed ([7.1.17](/7.1.17#sec-17.3.5)), activates phosphorylase *b* by binding to its nucleotide site; ATP and glucose 6-phosphate compete with AMP and inhibit. Muscle phosphorylase *b* is therefore active during intense exercise even without phosphorylation, and McArdle patients, who lack it, cannot raise their glycolytic flux.
- In liver, the signal is blood glucose. Glucose binds an inhibitory site of phosphorylase *a*, favors the T state and exposes phospho-Ser14 to PP1, which converts it to the almost inactive *b* form. Liver phosphorylase thus acts as its own glucose sensor: when blood glucose is restored, glycogen breakdown stops. Liver phosphorylase *b* does not respond to AMP.

### 19.5.3. Glycogen Synthase and GSK3

Glycogen synthase is regulated in the opposite sense: its active form, glycogen synthase *a*, is dephosphorylated, and phosphorylation at up to nine sites converts it to the *b* form, which is inactive unless its allosteric activator glucose 6-phosphate is present.

**Definition 19.5.2 (Glycogen Synthase Kinase 3)** **Glycogen synthase kinase 3** (GSK3) is a constitutively active Ser/Thr protein kinase that phosphorylates three Ser residues near the C-terminus of glycogen synthase, inactivating it. It phosphorylates only substrates that have been primed by a previous phosphorylation four residues C-terminal to the target site (a phosphoserine at position +4), and it is inhibited when PKB (or PKA) phosphorylates its N-terminal Ser9.

The priming is hierarchical: casein kinase II (CKII) phosphorylates Ser656; GSK3 binds this phosphoserine through a positively charged pocket (Arg96, Arg180, Lys205) and phosphorylates the Ser four residues N-terminal to it, which then primes the next site, so that GSK3 walks along the chain (sites 4, 3c, 3b, 3a). When PKB phosphorylates Ser9 of GSK3, its N-terminus becomes a pseudosubstrate that occupies the priming pocket ([7.1.15](/7.1.15#sec-15.3.2)). Insulin thus activates glycogen synthase by switching off its kinase, and in parallel by activating PP1. PKA and AMP-activated protein kinase (which binds glycogen through a carbohydrate-binding domain) also phosphorylate glycogen synthase, so that synthesis stops during stress and energy depletion. Glucose 6-phosphate, by binding to glycogen synthase *b*, both activates it and makes it a better substrate for PP1: glycogen synthase is a sensor of glucose 6-phosphate, as liver phosphorylase is a sensor of glucose. GSK3 has many other substrates (β-catenin in Wnt signaling, tau, transcription factors); its name records only the first one found.

The multisite phosphorylation of glycogen synthase is a graded control, not a switch: activity falls progressively with the number of phosphates, and the allosteric activation by glucose 6-phosphate restores activity of the phosphorylated forms. Control analysis in muscle shows that the flux of glycogen synthesis is controlled mostly by glucose transport and hexokinase, not by glycogen synthase: the elaborate regulation of the synthase mainly keeps the concentration of glucose 6-phosphate constant while the flux changes (the supply–demand view of [7.1.17](/7.1.17#sec-17.4.4); Shulman and colleagues, ¹³C NMR in human muscle).

### 19.5.4. Phosphoprotein Phosphatase 1

PP1 removes the phosphoryl groups from all three enzymes phosphorylated in response to glucagon and epinephrine: phosphorylase kinase, glycogen phosphorylase and glycogen synthase. Its catalytic subunit does not occur free but bound to one of a family of glycogen-targeting subunits ($\mathrm{G_M}$ in muscle, $\mathrm{G_L}$ in liver, and others), which bind glycogen, PP1 and the target enzymes, and are themselves regulated.

- Insulin activates PP1 (in muscle partly by phosphorylation of $\mathrm{G_M}$ at site 1), and so activates synthesis and stops breakdown.
- Epinephrine, through PKA, phosphorylates $\mathrm{G_M}$ at site 2, which releases PP1 from the glycogen particle, and phosphorylates inhibitor 1, a protein that then inhibits PP1; the kinase cascade and the inhibition of the phosphatase reinforce each other.
- In liver, phosphorylase *a* binds $\mathrm{G_L}$ and inhibits PP1 bound to it. Synthase can therefore be activated only after phosphorylase has been inactivated: when glucose converts phosphorylase *a* to *b*, PP1 is released to dephosphorylate synthase. Breakdown stops before synthesis starts, a built-in delay that prevents futile cycling of glycogen.

### 19.5.5. The Two Tissues

| | Liver | Skeletal muscle |
|---|---|---|
| Role of glycogen | supply blood glucose (altruistic) | fuel for its own contraction (selfish) |
| Hormones | glucagon (fasting), epinephrine, insulin | epinephrine, insulin; no glucagon receptors |
| Glucose uptake | GLUT2, always in the membrane; glucokinase | GLUT4, recruited by insulin and contraction; hexokinase II |
| Phosphorylase | inhibited by glucose (glucose sensor); not activated by AMP | activated by AMP and, through phosphorylase kinase, by $\ce{Ca^2+}$ |
| Glycogen synthase | activated by G6P; PP1 released when phosphorylase *a* is inactivated | activated by G6P, insulin (GSK3, PP1) |
| Glycolysis under cAMP | inhibited (PFK-2/FBPase-2, pyruvate kinase L phosphorylated) | stimulated (glycogen breakdown; pyruvate kinase M not phosphorylated) |
| Gluconeogenesis | yes | no (no glucose 6-phosphatase) |

In the liver, glucagon and PKA thus coordinate four switches at once: phosphorylase on, glycogen synthase off, F2,6BP down (PFK-1 off, FBPase-1 on), pyruvate kinase off; the liver makes glucose 6-phosphate by glycogenolysis and gluconeogenesis and exports glucose. After a carbohydrate meal, insulin reverses each of them, glucokinase is released from GKRP, and glucose is stored as glycogen (up to about 10% of liver weight) and, beyond that, converted to fat. In muscle, epinephrine stimulates glycogen breakdown and glycolysis together, for the fight-or-flight response, and insulin stimulates glucose uptake, glycogen synthesis and glycolysis. The integration of these responses with fat metabolism, and their failure in diabetes, are the subject of [7.1.29](/7.1.29).

## Summary

The pathway cards ([7.1.16](/7.1.16#sec-16.1.3)):

| Field | Gluconeogenesis | Glycogen metabolism |
|---|---|---|
| Location | liver (renal cortex, intestine); pyruvate carboxylase in the matrix, glucose 6-phosphatase in the ER lumen, the rest in the cytosol | cytosolic glycogen particles of liver and muscle (all cells in small amounts) |
| Net reaction | 2 pyruvate + 4 ATP + 2 GTP + 2 NADH + 2 $\ce{H+}$ + 4 $\ce{H2O}$ → glucose + 4 ADP + 2 GDP + 6 $\mathrm{P_i}$ + 2 $\ce{NAD+}$ (Eq. (19.2)) | breakdown: $(\text{Glc})_n$ + $\mathrm{P_i}$ → $(\text{Glc})_{n-1}$ + Glc 1-P (Definition 19.3.1); synthesis: Glc 1-P + UTP + $(\text{Glc})_n$ → $(\text{Glc})_{n+1}$ + UDP + 2 $\mathrm{P_i}$ |
| Energy account | 6 high-energy phosphates and 2 NADH per glucose (glycolysis returns 2 ATP); $\Delta_{\mathrm{r}}G \approx -16\,\mathrm{kJ\,mol^{-1}}$ in cells | 1 UTP per residue stored (+1 ATP from blood glucose); breakdown gives Glc 1-P without ATP, 10% as free glucose; net loss of 1 ATP per residue cycled |
| Committed and regulated steps | pyruvate carboxylase, PEPCK (Eq. (19.1)), FBPase-1, glucose 6-phosphatase | glycogen phosphorylase; glycogen synthase |
| Activators | pyruvate carboxylase: acetyl-CoA | phosphorylase: AMP (muscle), phosphorylase kinase ($\ce{Ca^2+}$, PKA); synthase: glucose 6-phosphate |
| Inhibitors | FBPase-1: AMP, fructose 2,6-bisphosphate (Definition 19.2.3) | phosphorylase: ATP, G6P (muscle), glucose (liver); synthase: phosphorylation by GSK3 (Definition 19.5.2), PKA, AMPK |
| Covalent, hormonal and transcriptional control | glucagon/PKA lowers F2,6BP (Formula 19.2.1), inactivates pyruvate kinase L; glucagon, cortisol (CREB, PGC-1α) induce PEPCK and glucose 6-phosphatase; insulin (FOXO1) represses them | epinephrine, glucagon → PKA → phosphorylase kinase (Definition 19.5.1) → phosphorylase *a*; insulin → PKB ⊣ GSK3, insulin → PP1 → synthase *a*; PP1 targeting subunits |
| Opposing pathway | glycolysis: reciprocal regulation at three pairs (Definition 19.2.1; table in 19.2.1) | the two directions use different enzymes and are reciprocally phosphorylated |
| Coenzymes (vitamins) | biotin ($\mathrm{B_7}$), NAD (niacin) | pyridoxal phosphate ($\mathrm{B_6}$) in phosphorylase |
| Diseases and drugs | von Gierke disease (fasting hypoglycemia); metformin lowers hepatic gluconeogenesis (7.1.29); alcohol inhibits gluconeogenesis (cytosolic NADH) | glycogen storage diseases (Definition 19.3.3, table in 19.3.5) |

| Topic | Key points |
|---|---|
| Bypasses (19.1) | pyruvate → OAA → PEP (biotin, ATP; GTP), two routes set by the need for cytosolic NADH; FBPase-1; glucose 6-phosphatase in the ER; Cori cycle (Definition 19.1.2) costs ≥ 4 ATP; no glucose from even-chain fatty acids in animals |
| Glucokinase (Definition 19.2.2) | $K_{0.5} \approx 8$–10 mM, $n_{\mathrm{H}} \approx 1.7$, no G6P inhibition, GKRP; rate follows blood glucose; β-cell glucose sensor |
| F2,6BP (Definition 19.2.3, Formula 19.2.1) | bifunctional PFK-2/FBPase-2; one phosphorylation moves both activities oppositely; [F2,6BP] spans ~100-fold; the net flux of the F6P/F1,6BP cycle changes sign |
| Substrate cycles (Eq. (19.5)) | amplification $(1 + r)/(1 - r)$ at cost $r/(1 - r)$ ATP per unit of net flux |
| Glycogen (19.3–19.4) | phosphorylase (PLP phosphate as acid), debranching enzyme (Definition 19.3.2), UDP-glucose (Definition 19.4.1), synthase and branching enzyme (Definition 19.4.2), glycogenin (Definition 19.4.3); optimum chain length 13 and ≤ 12 tiers (Formula 19.4.1) |
| Regulation (19.5) | cascade PKA → phosphorylase kinase → phosphorylase; GSK3 with priming; PP1 and targeting subunits; muscle (Ca²⁺, AMP) versus liver (glucose sensor) |

## Questions

1. Lactate is converted to glucose in the liver. Count the high-energy phosphates and the NADH needed per glucose, and explain why the lactate route uses mitochondrial PEPCK while the pyruvate route exports malate.

   **Answer** Two lactates are oxidized to two pyruvates by LDH, producing 2 NADH in the cytosol, exactly the NADH needed to reduce two 1,3-bisphosphoglycerates. The cost is that of Eq. (19.2): 4 ATP + 2 GTP = 6 high-energy phosphates. Because cytosolic NADH is already supplied, oxaloacetate need not leave the mitochondrion as malate (which would carry reducing equivalents out); it is converted to PEP by the mitochondrial PEPCK and PEP is exported. Starting from pyruvate (or alanine), no cytosolic NADH is produced, so oxaloacetate is reduced to malate with matrix NADH, exported, and reoxidized in the cytosol, delivering the NADH there.

2. Glycogen phosphorylase has $\Delta_{\mathrm{r}}G'^{\circ} = +3.1\,\mathrm{kJ\,mol^{-1}}$. What is the ratio $[\mathrm{P_i}]/[\text{glucose 1-phosphate}]$ at equilibrium, and what is $\Delta_{\mathrm{r}}G$ in a myocyte where the ratio is 100 (25 °C)?

   **Answer** The concentration of glycogen ends does not change when one residue is removed, so $K' = [\text{G1P}]/[\mathrm{P_i}] = \mathrm{e}^{-3.1/2.48} = 0.29$, and $[\mathrm{P_i}]/[\text{G1P}] = 3.5$ at equilibrium. With a ratio of 100, $\Delta_{\mathrm{r}}G = 3.1 + 2.48\ln(1/100) = 3.1 - 11.4 = -8.3\,\mathrm{kJ\,mol^{-1}}$: breakdown is favored, because phosphoglucomutase and glycolysis remove glucose 1-phosphate. This is also why phosphorylase cannot serve for synthesis in the cell.

3. Using Formula 19.4.1, show that the optimal chain length does not depend on the number of tiers, find it, and explain qualitatively why chains of 5 and of 40 residues are both poor.

   **Answer** $f$ is a product of a function of $t$ and $h(g) = g(g - 4)/(0.12g + 0.35)^3$, so its maximum in $g$ is the same for every $t$. $h'(g) = 0$ means $(2g - 4)/[g(g - 4)] = 3 \times 0.12/(0.12g + 0.35)$, i.e. $(2g - 4)(0.12g + 0.35) = 0.36\,g(g - 4)$, or $0.12g^2 - 1.66g + 1.4 = 0$, whose positive root above 4 is $g = (1.66 + \sqrt{1.66^2 - 0.672})/0.24 \approx 12.9$. With 5 residues per chain, only one residue per A chain is accessible before the branch-point limit, and most of the particle is branch points: little glucose is available. With 40 residues per chain, the tiers are thick, the volume grows as $g^3$ while stored glucose and accessible glucose grow only as $g^2$, and there are few ends per volume: the store is bulky and slow to mobilize.

4. A gamebird's flight muscle contains 0.35% glycogen by weight and breaks it down at 120 µmol glucose 1-phosphate per minute per gram during a panic flight. How long can it fly on glycogen? What does the answer say about the role of glycogen compared with fat?

   **Answer** 0.35% is 3.5 mg per gram, or $3.5/162 = 21.6\,\mu\mathrm{mol}$ glucosyl units per gram; at 120 µmol min⁻¹ g⁻¹ this lasts about 0.18 min, roughly 11 s. Glycogen supports short anaerobic bursts at a very high rate (pheasants and quail fly only short distances); sustained flight, as in migrating birds, is fueled by the oxidation of fatty acids (7.1.21), which store far more energy per gram but deliver it more slowly and only aerobically.

5. Predict the effect on blood glucose and on liver glycogen of (a) a loss-of-function mutation of glucokinase in the liver, (b) a constitutively active FBPase-2 in the liver, (c) loss of the glucose-binding site of liver phosphorylase.

   **Answer** (a) After a meal the liver takes up and phosphorylates little glucose: blood glucose stays high longer, liver glycogen synthesis from glucose is reduced (some glycogen is still made from gluconeogenic precursors, the indirect pathway). (b) F2,6BP stays low: PFK-1 is inhibited and FBPase-1 active even in the fed state, so the liver keeps making glucose; blood glucose is raised, and glycolysis and fat synthesis in the liver are reduced. (c) Glucose can no longer inactivate phosphorylase *a* and release PP1: after a meal, glycogen breakdown continues and glycogen synthase is not activated efficiently, so the liver stores less glycogen and the rise of blood glucose after a meal is exaggerated.

6. (Open question) In the model of Formula 19.2.1, the PFK-1/FBPase-1 cycle reverses its net flux at a threshold of the hormonal ratio. Which parameters set the threshold, and how would you test with the model whether the bifunctional nature of PFK-2/FBPase-2 (one protein with both activities) matters, compared with two separate, independently regulated enzymes?

   **Answer** Outline: the threshold is where PFK-1 and FBPase-1 activities are equal; it depends on $K_{\mathrm{a}}$, $K_{\mathrm{i}}$, $n$ and $f_0$ (which fix the F2,6BP concentration at which the two curves cross) and on $V_{\mathrm{K}}^0$, $V_{\mathrm{B}}^0$, $a$, $b$, $K_X$ (which map the hormonal ratio onto F2,6BP through Eq. (19.4)). To test the role of bifunctionality, replace the coupled terms by a kinase whose activity depends on $\varphi_1$ and a phosphatase depending on an independently regulated $\varphi_2$, and compare the gain $\mathrm{d}\ln X^*/\mathrm{d}\ln s$ and the robustness of the threshold to changes in total enzyme: in the bifunctional case the ratio of the two activities depends only on $\varphi$, so changes in the amount of the protein (transcription, cell-to-cell variation) shift both rates together and, to a first approximation, leave $X^*$ unchanged when $K_X \gg X$, whereas separate enzymes would make $X^*$ sensitive to their individual amounts. This robustness argument has been proposed for bifunctional regulators in general (e.g. the bacterial isocitrate dehydrogenase kinase/phosphatase, 7.1.20).
