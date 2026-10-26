---
title: Hormonal Regulation and Integration of Mammalian Metabolism
description: Hormones, their chemical classes and receptors, the top-down hypothalamic–pituitary hierarchy and bottom-up signals from gut and fat; the metabolic division of labor among liver, adipose tissue (white, brown, beige), skeletal and heart muscle, brain and blood; insulin, glucose sensing by β cells, glucagon, epinephrine and cortisol, the fed, fasting and starving states and the hormone–tissue matrix; Bergman's minimal model of glucose tolerance; obesity, adipokines (leptin, adiponectin), AMPK, mTORC1, PPARs, ghrelin, incretins, the gut microbiota and acetylation of metabolic enzymes; type 1 and type 2 diabetes, ketoacidosis, HbA1c as a time average of glucose, lipotoxicity and the drugs that treat diabetes.
---

The chapters on individual pathways treated **metabolism** as the business of one cell, regulated by **substrates**, **allosteric effectors** and covalent modification of its own **enzymes** ([7.1.17](/7.1.17)). In a mammal the cells are specialized and their pathways are divided among organs: the liver makes glucose and **ketone bodies** for others, adipose tissue stores fat for the whole body, muscle spends ATP on work, and the brain, which has no fuel stores of its own, must be supplied continuously. Hormones carry the information that coordinates this division of labor. This chapter, the last of Part II, puts the pathways together: it describes the chemistry and the hierarchy of hormones, the metabolic profile of each tissue, the actions of insulin, glucagon, epinephrine and cortisol in the fed, fasting and starving states, and how body mass is regulated by signals from fat, gut and brain converging on two kinase hubs, AMPK and mTORC1; it ends with diabetes mellitus, the disease that results when insulin signaling fails. The **receptor** and second-messenger mechanisms themselves are in [7.1.14](/7.1.14) and [7.1.15](/7.1.15) and are only recalled here; the physiology of the endocrine glands, of digestion and of the kidney belongs to animal physiology (7.14).

## 29.1. Hormone Structure and Action

### 29.1.1. Hormones and the Neuroendocrine System

**Definition 29.1.1 (Hormone)** A **hormone** is a small molecule or protein produced by one tissue, carried in the blood (or diffusing through the extracellular space) to target cells, where it acts through specific receptors to change cellular activity. Hormones are *endocrine* when they are released into the blood and act on distant tissues (insulin, glucagon), *paracrine* when they diffuse to neighboring cells (eicosanoids), and *autocrine* when they act on the cell that released them.

Neuronal and endocrine signaling differ mainly in anatomy: a neurotransmitter crosses a synaptic cleft a fraction of a micrometer wide, a hormone may travel a meter in the blood, but both act through receptors, and the same molecule can serve as both (epinephrine and norepinephrine are neurotransmitters in the brain and at smooth-muscle junctions, and hormones of the adrenal medulla). The coordination of metabolism is therefore the work of a single neuroendocrine system.

### 29.1.2. Receptors Determine Speed and Amplification

Hormones act at concentrations of $10^{-12}$ to $10^{-9}\,\mathrm{M}$ because their receptors bind them with high affinity. The four mechanisms of [7.1.14](/7.1.14#sec-14.1.3) apply: a **second messenger** (**cAMP**, cGMP, $\mathrm{IP_3}$, $\ce{Ca^2+}$) produced by an enzyme that a **G protein–coupled receptor** controls; a **receptor tyrosine kinase** such as the **insulin receptor**; a **gated ion channel**; and a **nuclear receptor** that regulates **transcription**. Two consequences matter for metabolism:

| | Water-soluble hormones (**peptides**, catecholamines) | Lipid-soluble hormones (steroids, thyroid hormones, retinoids, **vitamin** D) |
|---|---|---|
| Receptor | plasma membrane (**GPCR**, **RTK**) | intracellular, mostly nuclear |
| Effect | change in activity of existing enzymes (phosphorylation, allostery) | change in the amount of enzymes (transcription) |
| Time to response | seconds to minutes | hours to days |
| Amplification | receptor → many second-messenger molecules → kinase cascade | one hormone–receptor complex → many **mRNA** and **protein** molecules |

A single hormone–receptor complex activates a catalyst, so the receptor is both transducer and amplifier; in the glycogenolytic cascade one epinephrine molecule can mobilize thousands to millions of glucose units ([7.1.14](/7.1.14#sec-14.2.3)).

### 29.1.3. Hormones Are Chemically Diverse

| Class | Example | Receptor | Mode of action |
|---|---|---|---|
| peptide | insulin, glucagon, leptin | plasma membrane (RTK, GPCR, cytokine receptor) | **second messengers**, kinase cascades |
| catecholamine | epinephrine | plasma membrane (adrenergic GPCRs) | cAMP, $\ce{Ca^2+}$ |
| **eicosanoid** | **prostaglandin** $\mathrm{E_1}$ | plasma membrane (GPCR) | second messengers |
| endocannabinoid | anandamide, 2-arachidonoylglycerol | plasma membrane (CB1, CB2) | GPCR signaling |
| steroid | cortisol, testosterone | nuclear | transcription |
| vitamin D | calcitriol | nuclear | transcription |
| retinoid | retinoic acid | nuclear | transcription |
| thyroid hormone | thyroxine ($\mathrm{T_4}$), triiodothyronine ($\mathrm{T_3}$) | nuclear | transcription |
| nitric oxide | NO | cytosolic **guanylyl cyclase** | cGMP |

(Lehninger 8e, Table 23-1.) Peptide hormones range from three **residues** (thyrotropin-releasing hormone, pyroGlu–His–Pro-$\ce{NH2}$, whose blocked termini remove the charges that would dominate so small a molecule) to more than 200. They are synthesized as inactive precursors and activated by proteolysis on secretion, as are the **zymogens** of digestion. Insulin is made as preproinsulin (110 residues); removal of the **signal peptide** in the endoplasmic reticulum and formation of three disulfide bonds give proinsulin, which is stored in secretory granules, where the prohormone convertases PC1/3 and PC2 and carboxypeptidase E excise the connecting C peptide (31 residues) and leave mature insulin, an A chain (21 residues) and a B chain (30 residues) joined by two disulfide bonds. Insulin and C peptide are secreted in equimolar amounts; because the liver removes about half of the insulin on its first pass but not the C peptide, plasma C peptide is the better measure of the patient's own insulin secretion, also in diabetics who inject insulin. A single precursor can give several hormones: pro-opiomelanocortin (POMC) is cut at pairs of basic residues into ACTH, three melanocyte-stimulating hormones (α-, β-, γ-MSH), β-endorphin and others, with different products in different tissues.

Because their concentrations are so low, hormones were first measured by radioimmunoassay (Rosalyn Yalow and Solomon Berson, 1959, with insulin), a competition between the unlabeled hormone of the sample and a radiolabeled standard for an **antibody**; today they are measured mainly by **ELISA** and its variants ([7.1.7](/7.1.7#sec-7.4.4)) and by mass spectrometry.

### 29.1.4. The Top-Down Hierarchy

What sets the level of each hormone? The central nervous system receives information from internal and external sensors (danger, hunger, blood composition, temperature) and commands the endocrine tissues through a hierarchy. The hypothalamus, a pea-sized region at the base of the brain, is its coordination center: it secretes releasing factors into portal blood vessels that lead directly to the anterior pituitary, which in response releases tropic hormones into the general circulation; these act on the peripheral glands, whose hormones act on the target tissues (the posterior pituitary instead stores oxytocin and vasopressin made in hypothalamic neurons). For cortisol the chain is hypothalamus (corticotropin-releasing hormone, CRH) → anterior pituitary (corticotropin, ACTH) → adrenal cortex (cortisol). Each level amplifies: nanograms of CRH release micrograms of ACTH, which release milligrams of cortisol. And each level is inhibited by the final hormone, so that its concentration is held near a set value, the same logic as **feedback inhibition** of the first enzyme of a biosynthetic pathway ([7.1.28](/7.1.28#sec-28.2.4)).

![The hypothalamic–pituitary–adrenal axis. A stress sensed by the central nervous system makes the hypothalamus release corticotropin-releasing hormone (CRH, nanograms), which makes the anterior pituitary release ACTH (micrograms), which makes the adrenal cortex release cortisol (milligrams): an amplification of about a millionfold (right). Cortisol acts through a nuclear receptor on liver (induction of gluconeogenic enzymes such as PEP carboxykinase), muscle (proteolysis), adipose tissue (lipolysis) and immune cells (suppression of inflammation). Dashed bars: cortisol inhibits the release of ACTH and CRH (negative feedback)](./plots/hpa-cascade.py)

### 29.1.5. Bottom-Up Signals from the Body

Peripheral tissues also report their state to the brain. The hypothalamus integrates signals from fat (leptin, adiponectin), gut (ghrelin, incretins, PYY), pancreas (insulin) and muscle, and responds with feeding behavior and with signals through the autonomic nervous system:

| Hormone | Made in | Target | Action |
|---|---|---|---|
| insulin | pancreatic β cells | muscle, adipose, liver; hypothalamus | glucose uptake, storage as **glycogen** and fat; satiety |
| glucagon | pancreatic α cells | liver | **gluconeogenesis**, glucose release |
| leptin | adipose tissue | hypothalamus | reduces appetite, raises energy expenditure |
| adiponectin | adipose tissue | muscle, liver, brain | insulin sensitivity, fat oxidation |
| ghrelin | stomach | hypothalamus | hunger before meals |
| incretins (GLP-1, GIP) | intestine | pancreas, brain | amplify insulin secretion; satiety (GLP-1) |
| $\mathrm{PYY_{3-36}}$ | intestine (ileum, colon) | hypothalamus | satiety after meals |
| neuropeptide Y | hypothalamus | brain | stimulates feeding |

(After Lehninger 8e, Table 23-2.) The muscle hormone irisin, proposed to convert white to beige fat after exercise, is listed in Lehninger; its existence and role in humans remain disputed.

## 29.2. Tissue-Specific Metabolism

### 29.2.1. The Liver Processes and Distributes Nutrients

The portal vein brings the products of digestion first to the liver: the hepatocytes see the meal before any other tissue, and all other tissues are, in this sense, "extrahepatic". The liver adapts its enzyme content to the diet within hours (liver enzymes turn over five to ten times faster than those of muscle), and distributes fuels in the proportions other tissues need.

Glucose enters hepatocytes freely through GLUT2, so the intracellular concentration follows the blood, and is phosphorylated by **glucokinase** ($K_{0.5} \approx 10\,\mathrm{mM}$, no product inhibition; [7.1.19](/7.1.19#sec-19.2.2)), which therefore traps glucose in the liver only when blood glucose is high. Glucose 6-phosphate is the crossroads with five fates:

1. dephosphorylation by glucose 6-phosphatase and export, the main fate when glucose is scarce (the brain needs a blood glucose of about 4–5 mM);
2. storage as glycogen ([7.1.19](/7.1.19));
3. **glycolysis** and oxidation, though the liver normally prefers **fatty acids** as its own fuel;
4. glycolysis to acetyl-CoA for the synthesis of fatty acids and **cholesterol**, exported in **lipoproteins** ([7.1.26](/7.1.26));
5. the **pentose phosphate pathway**, for **NADPH** (**lipid** synthesis, detoxification of xenobiotics by **cytochrome P-450** enzymes) and ribose 5-phosphate.

Amino acids are used for the liver's own proteins (half-lives of hours to days) and for the plasma proteins, passed to other tissues, used for nucleotides, hormones and other nitrogenous compounds, or degraded: their nitrogen becomes urea, their carbon skeletons pyruvate and **citric acid cycle** intermediates for glucose or ketone bodies ([7.1.22](/7.1.22)); between meals muscle sends amino groups as alanine (the **glucose–alanine cycle**). Fatty acids are esterified to the liver's lipids, oxidized by **β oxidation** as the liver's main fuel, converted to **ketone bodies** for export ([7.1.21](/7.1.21#sec-21.6)), or packaged as triacylglycerols in **VLDL** for adipose tissue and muscle.

### 29.2.2. Adipose Tissue Stores and Supplies Fatty Acids

White adipose tissue (about 15% of the mass of a lean young adult) consists of adipocytes 30–70 µm across, each filled by a single lipid droplet that pushes the nucleus and mitochondria to the rim. Adipocytes take up fatty acids released by **lipoprotein lipase** from **chylomicrons** and VLDL after meals, and to a smaller extent (in humans) make fatty acids from glucose. Between meals they hydrolyze the stored triacylglycerol in three steps (adipose triglyceride lipase, **hormone-sensitive lipase** and monoacylglycerol lipase) under hormonal control: catecholamines, through cAMP and **protein kinase A**, phosphorylate perilipin and **hormone-sensitive lipase** and give the lipases access to the droplet; insulin opposes this by activating the **phosphodiesterase** PDE3B, which lowers cAMP ([7.1.21](/7.1.21#sec-21.1.3)). Up to 70% of the fatty acids released are re-esterified within the adipocyte, a **substrate cycle** that costs ATP and makes heat. Because adipocytes lack glycerol kinase, they cannot reuse the released glycerol; they make glycerol 3-phosphate from pyruvate by **glyceroneogenesis**, through the cytosolic PEP carboxykinase. Adipose tissue is also an endocrine organ (29.4).

**Definition 29.2.1 (Beige Adipose Tissue)** **Beige adipose tissue** consists of thermogenic adipocytes that appear within white adipose depots after prolonged cold exposure or β-adrenergic stimulation; like brown adipocytes they contain many small lipid droplets, many mitochondria and the uncoupling protein UCP1, but they develop from a different precursor lineage.

**Brown adipose tissue**, rich in mitochondria and in **thermogenin** (**UCP1**), oxidizes fat to make heat rather than ATP ([7.1.23](/7.1.23#sec-23.5.1)). It forms 1–5% of body mass at birth, located around the great vessels, the kidneys and the spine, and declines with age; adults retain small deposits above the clavicles and along the spine, which take up large amounts of glucose and fatty acids when activated by cold (as shown by positron emission tomography with [¹⁸F]fluorodeoxyglucose). Recruiting brown and beige fat is a possible way of spending surplus energy, and the transcription factor PPARγ (29.4.6) and sympathetic stimulation through β-adrenergic receptors (β3 in rodents, also β2 in humans) control it.

### 29.2.3. Muscle Uses ATP for Work

Skeletal muscle consists of two main fiber types: slow-twitch (red) fibers, rich in mitochondria, capillaries and myoglobin, which develop low tension but resist fatigue and make ATP by **oxidative phosphorylation**; and fast-twitch (white) fibers, with fewer mitochondria, which develop high tension quickly, rely on glycolysis, and fatigue fast. The fuel depends on the intensity of work:

| Activity | Main source of ATP | Approximate duration |
|---|---|---|
| rest | oxidation of fatty acids from adipose tissue (and ketone bodies) | indefinite |
| light to moderate work | fatty acids plus blood glucose, oxidized | hours |
| maximal burst (sprint) | ATP and **phosphocreatine** stores (10–30 mM **phosphocreatine**) | a few seconds |
| maximal work beyond seconds | glycogen → lactate (**lactic acid fermentation**), 3 ATP per glucose unit because **phosphorolysis** bypasses hexokinase | about 1–2 minutes |

Creatine kinase keeps [ATP] nearly constant at the start of exercise by phosphorylating ADP from phosphocreatine ($^{31}\mathrm{P}$ NMR of working muscle shows phosphocreatine falling while ATP barely changes), and a mitochondrial **isozyme** probably shuttles energy as phosphocreatine from mitochondria to the myofibrils ([7.1.16](/7.1.16#sec-16.3.3)). Epinephrine stimulates both muscle glycogenolysis and the release of glucose by the liver. After a sprint, the extra oxygen consumed ("oxygen debt") supports gluconeogenesis from the lactate in the liver, the **Cori cycle**, which returns glucose to the muscle ([7.1.19](/7.1.19#sec-19.1.6)). Muscle also makes heat by shivering. Muscle glycogen (about 1% of muscle mass) serves only the muscle itself: muscle lacks glucose 6-phosphatase and has no glucagon receptors.

Heart muscle works continuously and is strictly aerobic: mitochondria fill a third to a half of the cell volume, the main fuel is fatty acids, with glucose, lactate and ketone bodies, and the heart stores little glycogen or fat. When a coronary artery is blocked by an atherosclerotic plaque or a thrombus, the affected muscle dies within hours (myocardial infarction). The enzymes it releases into the blood were the first diagnostic markers: creatine kinase MB rises within 2–6 hours and peaks at about a day; today cardiac troponins (I and T), which are more specific and remain elevated longer, are the standard.

### 29.2.4. The Brain Needs a Continuous Supply of Glucose

The brain (2% of body mass) uses about 20% of the oxygen consumed at rest and about 120 g of glucose per day, which enters through GLUT1 of the blood–brain barrier and GLUT3 of neurons. Neurons spend most of their ATP on the **Na⁺/K⁺-ATPase**, which maintains the membrane potential that action potentials discharge ([7.1.14](/7.1.14#sec-14.5)). The brain stores almost no glycogen, and neurons cannot oxidize fatty acids, which cross the blood–brain barrier poorly (astrocytes can oxidize some). In prolonged fasting the brain adapts by oxidizing β-hydroxybutyrate and acetoacetate, taken up by monocarboxylate **transporters**, which then supply up to about 60% of its energy ([7.1.21](/7.1.21#sec-21.6.2)). Because the brain depends on blood glucose minute by minute, maintaining it is the overriding priority of fuel metabolism:

| Plasma glucose | State |
|---|---|
| 3.9–5.5 mM (70–100 mg/dL) | normal after an overnight fast |
| below about 3.9 mM | counterregulation: glucagon and epinephrine released, insulin suppressed |
| about 3 mM | sweating, trembling, hunger, palpitations (epinephrine), confusion |
| below about 2.5 mM | lethargy, convulsions, coma; prolonged severe hypoglycemia causes irreversible brain damage |

(To convert from mg/dL to mM divide by 18; Lehninger quotes whole-blood glucose, which is about 14% lower than plasma glucose.)

### 29.2.5. Blood Connects the Tissues

The 5–6 L of blood of an adult are almost half cells by volume (erythrocytes, leukocytes, platelets) and half plasma, which is 90% water. The plasma solutes are proteins (about 70% of the solids: albumin, which carries fatty acids and many drugs, immunoglobulins, **apolipoproteins**, transferrin, clotting factors), small organic molecules (glucose, amino acids, lactate, lipids, urea) and inorganic ions ($\ce{Na+}$ about 140 mM, $\ce{K+}$ about 4–5 mM, total calcium about 2.5 mM, $\ce{Cl-}$, $\ce{HCO3-}$). Their concentrations are kept in a **dynamic steady state** by the balance of intake, exchange with tissues and renal excretion, which is why plasma measurements are the main tool of clinical biochemistry. Erythrocytes, which lose their nucleus and mitochondria, depend entirely on glycolysis and return lactate to the liver.

| Tissue | Stored fuel | Fuel used | Exported | Special enzymes or features |
|---|---|---|---|---|
| liver | glycogen (up to about 10% of its mass), some TAG | fatty acids, amino acids, glucose | glucose, ketone bodies, VLDL, urea, plasma proteins | **glucokinase**, glucose 6-phosphatase, HMG-CoA synthase, **urea cycle** |
| white adipose | TAG (about 590 MJ in a lean adult) | glucose, fatty acids | fatty acids, glycerol, adipokines | hormone-sensitive lipase, LPL, no glycerol kinase |
| brown and beige adipose | TAG (small droplets) | fatty acids, glucose | heat | UCP1 |
| skeletal muscle | glycogen, phosphocreatine, protein | fatty acids, glucose, ketone bodies; glycogen in bursts | lactate, alanine, glutamine | GLUT4, creatine kinase, no glucose 6-phosphatase |
| heart | little | fatty acids, ketone bodies, lactate, glucose | — | strictly aerobic |
| brain | almost none | glucose; ketone bodies in starvation | — | GLUT1, GLUT3; no fatty acid oxidation in neurons |
| erythrocytes | none | glucose (glycolysis only) | lactate | no mitochondria |

## 29.3. Hormonal Regulation of Fuel Metabolism

The blood glucose is held near 4.5–5 mM by four hormones with distinct messages: insulin signals that glucose is high, glucagon that it is low, epinephrine that activity is imminent, and cortisol that the body is under stress.

### 29.3.1. Insulin and the Well-Fed State

**Definition 29.3.1 (Insulin)** **Insulin** is the peptide hormone of the β cells of the pancreatic islets (51 residues in two chains, $M_{\mathrm{r}} \approx 5800$), secreted when blood glucose rises, which acts through the insulin receptor tyrosine kinase ([7.1.15](/7.1.15#sec-15.1.1)) to promote the uptake of glucose by muscle and adipose tissue and the storage of fuel as glycogen, triacylglycerol and protein, while inhibiting glucose production by the liver and the mobilization of fat.

After a carbohydrate-rich meal blood glucose rises to 7–8 mM, and insulin rises several-fold. Through the **PI3K**–**PKB** branch ([7.1.15](/7.1.15#sec-15.1.5)) insulin moves GLUT4 transporters from intracellular vesicles to the plasma membrane of muscle and adipocytes, which increases their glucose uptake up to tenfold; inactivates **GSK3**, so that **glycogen synthase** is dephosphorylated and active; activates the phosphodiesterase PDE3B, lowering cAMP and so reversing the actions of glucagon and epinephrine; and, through mTORC1 and the transcription factor SREBP-1c, induces the enzymes of lipogenesis. In the liver, the excess glucose is stored as glycogen, oxidized to acetyl-CoA and made into fatty acids, which leave as VLDL triacylglycerols for adipose tissue: in the well-fed state the liver is lipogenic.

| Metabolic effect of insulin | Target enzyme or protein |
|---|---|
| ↑ glucose uptake (muscle, adipose) | ↑ GLUT4 at the plasma membrane |
| ↑ glucose uptake (liver) | ↑ glucokinase (expression; release from its regulatory protein) |
| ↑ glycogen synthesis (liver, muscle) | ↑ glycogen synthase (GSK3 inhibited, PP1 activated) |
| ↓ glycogen breakdown | ↓ **glycogen phosphorylase** |
| ↑ glycolysis, acetyl-CoA production (liver) | ↑ PFK-1 (through PFK-2 and **fructose 2,6-bisphosphate**), ↑ **pyruvate dehydrogenase complex** |
| ↓ gluconeogenesis (liver) | ↓ PEP carboxykinase and glucose 6-phosphatase (transcription) |
| ↑ fatty acid synthesis (liver) | ↑ **acetyl-CoA carboxylase** |
| ↑ TAG storage (adipose); ↓ lipolysis | ↑ **lipoprotein lipase**; ↓ hormone-sensitive lipase (PDE3B) |

### 29.3.2. Glucose Sensing by β Cells

The islets of Langerhans (1–2% of pancreatic mass, about a million in a human pancreas) contain α cells (glucagon), β cells (insulin, the majority), δ cells (somatostatin) and a few others. A β cell couples secretion to glucose metabolism itself rather than to a glucose receptor:

**Definition 29.3.2 (ATP-Sensitive K⁺ Channel)** The **ATP-sensitive K⁺ channel** ($\mathrm{K_{ATP}}$) is an octameric $\ce{K+}$ channel of four pore-forming Kir6.2 subunits and four regulatory sulfonylurea receptor subunits (SUR1 in β cells, an ABC protein) that is closed by ATP binding to Kir6.2 and opened by Mg-ADP acting on SUR1; it links the membrane potential to the cell's ratio [ATP]/[ADP].

1. Glucose enters the β cell through a glucose transporter of high capacity (GLUT2 in rodents, mainly GLUT1 in humans), so its intracellular concentration follows the blood.
2. Glucokinase phosphorylates it at a rate that rises with the glucose concentration over the physiological range (its $K_{0.5}$ is about 8 mM and its **Hill coefficient** about 1.7); glucokinase is the glucose sensor of the β cell, and its flux sets the rate of glycolysis and mitochondrial oxidation, which raise [ATP]/[ADP].
3. The rise of [ATP]/[ADP] closes the $\mathrm{K_{ATP}}$ channels, which at low glucose keep the membrane hyperpolarized.
4. The membrane depolarizes and voltage-gated $\ce{Ca^2+}$ channels open.
5. $\ce{Ca^2+}$ entry triggers exocytosis of insulin granules; the response is biphasic, a first phase of granules already docked at the membrane within minutes and a sustained second phase.

The incretins GLP-1 and GIP, released by the gut after a meal, act through $\mathrm{G_s}$-coupled receptors and cAMP (protein kinase A and the exchange factor Epac2) to amplify the $\ce{Ca^2+}$-triggered secretion; they do not trigger it by themselves, which is why the same oral glucose load releases more insulin than an intravenous one, and why incretin-based drugs rarely cause hypoglycemia. Insulin lowers blood glucose, the β cell senses less glucokinase flux, and secretion slows: a simple negative feedback loop. Parasympathetic signals stimulate and sympathetic signals inhibit secretion.

![Glucose-stimulated insulin secretion by a β cell. (1) Glucose enters through a glucose transporter (GLUT2 in rodents, mainly GLUT1 in humans). (2) Glucokinase phosphorylates it in proportion to its concentration; glycolysis and mitochondrial oxidation raise [ATP]/[ADP]. (3) ATP closes the K_ATP channel (Kir6.2 with SUR1), the target of the sulfonylurea drugs, and K⁺ efflux stops. (4) The membrane depolarizes and voltage-gated Ca²⁺ channels open. (5) Ca²⁺ entry triggers the exocytosis of insulin granules, which release insulin and C peptide. The incretin GLP-1 acts through a Gs-coupled receptor and cAMP to amplify the Ca²⁺-triggered release](./plots/beta-cell-secretion.py)

The molecular chain explains several diseases and drugs. Sulfonylureas (glibenclamide, glipizide, glimepiride) bind SUR1 and close the channel; diazoxide opens it. Activating **mutations** of Kir6.2 or SUR1 that keep the channel open cause neonatal diabetes, and many such patients have been switched from insulin injections to sulfonylurea tablets; inactivating mutations cause congenital hyperinsulinism with severe hypoglycemia. Heterozygous loss-of-function mutations of glucokinase raise the glucose threshold for secretion and cause a mild, stable hyperglycemia (maturity-onset diabetes of the young, MODY2), and activating ones cause hypoglycemia, which shows how precisely the enzyme's kinetics set the blood glucose.

### 29.3.3. Glucagon and the Fasting State

**Definition 29.3.3 (Glucagon)** **Glucagon** is the 29-residue peptide hormone of the pancreatic α cells, secreted when blood glucose falls, which acts mainly on the liver through a $\mathrm{G_s}$-coupled receptor, cAMP and protein kinase A to stimulate glycogenolysis, gluconeogenesis and ketogenesis and to inhibit glycolysis and glycogen synthesis.

A few hours after a meal glucose falls slightly, insulin secretion slows and glucagon secretion rises. Protein kinase A phosphorylates the regulated enzymes of the hepatocyte: it activates **phosphorylase kinase** and so glycogen phosphorylase and inactivates glycogen synthase ([7.1.19](/7.1.19#sec-19.5)); it phosphorylates the bifunctional PFK-2/FBPase-2, lowering **fructose 2,6-bisphosphate**, which relieves the inhibition of FBPase-1 and removes the activation of PFK-1 ([7.1.19](/7.1.19#sec-19.2.3)); it inactivates the liver isozyme of pyruvate kinase, so that phosphoenolpyruvate is not lost to pyruvate; and through the transcription factor CREB and its **coactivator** CRTC2 it induces PEP carboxykinase and glucose 6-phosphatase. Glucagon also inactivates acetyl-CoA carboxylase, so that **malonyl-CoA** falls and fatty acids enter mitochondria for **β oxidation** and ketogenesis. The liver becomes **glucogenic**: it exports glucose made from glycogen, from lactate, glycerol and amino acids, and fuels itself with fatty acids.

| Metabolic effect of glucagon (liver) | Target enzyme |
|---|---|
| ↑ glycogen breakdown | ↑ glycogen phosphorylase |
| ↓ glycogen synthesis | ↓ glycogen synthase |
| ↓ glycolysis | ↓ PFK-1 (fructose 2,6-bisphosphate ↓), ↓ pyruvate kinase |
| ↑ gluconeogenesis | ↑ FBPase-1, ↑ PEP carboxykinase (transcription) |
| ↑ fatty acid oxidation, ketogenesis | ↓ acetyl-CoA carboxylase (malonyl-CoA ↓) |

(Glucagon receptors are scarce on human adipocytes and absent from muscle; the mobilization of fat in fasting is driven mainly by the fall of insulin and by catecholamines.)

![Fuel fluxes between organs in the well-fed and the fasting state. A: after a meal (insulin high, glucagon low) glucose and amino acids reach the liver through the portal vein, dietary fat reaches adipose tissue and muscle as chylomicrons through the lymph; the liver stores glycogen, makes fatty acids and exports them as VLDL, and passes glucose to the brain and to muscle, which takes it up through GLUT4. B: in fasting (glucagon high, insulin low) adipose tissue releases fatty acids and glycerol, muscle releases alanine, glutamine and lactate; the liver makes glucose by glycogenolysis and gluconeogenesis, oxidizes fatty acids and exports ketone bodies, which brain and muscle oxidize; in prolonged fasting the kidney adds gluconeogenesis and excretes ammonium](./plots/fed-fasted-fluxes.py)

### 29.3.4. Fasting and Starvation

A healthy adult has three fuel reserves:

| Fuel | Mass / kg | Energy / MJ |
|---|---|---|
| triacylglycerol (adipose tissue) | 15 (obese 140 kg man: 80) | 590 (3100) |
| protein, mainly muscle | 6 (8) | 100 (130) |
| glycogen (muscle, liver) | 0.23 | 3.8 |
| circulating fuels (glucose, fatty acids, TAG) | 0.023 | 0.4 |

(Lehninger 8e, Table 23-5, for a 70 kg man and a 140 kg man.) At a basal expenditure of about 7.5 MJ per day, the fat of a lean adult lasts about three months and that of a very obese adult more than a year; the glycogen lasts less than a day. The body uses about 160 g of glucose per day, 120 g of it in the brain, and has about 20 g of circulating glucose and 190 g of glycogen, so it must start making glucose within a day. Since fatty acids cannot be converted into glucose ([7.1.21](/7.1.21)), the carbon must come from glycerol, lactate and the amino acids of protein. The metabolic response to fasting is a sequence of shifts that spare protein:

1. Hours 2–24 (postabsorptive): liver glycogen supplies most of the blood glucose; insulin falls and glucagon rises; adipose tissue releases fatty acids, which become the main fuel of muscle and liver.
2. Days 1–3 (early fasting): liver glycogen is exhausted; gluconeogenesis from amino acids (muscle protein breakdown, about 75 g per day), glycerol and lactate supplies the brain. Oxaloacetate in the hepatocyte mitochondria is withdrawn for gluconeogenesis, so the acetyl-CoA from β oxidation cannot enter the citric acid cycle and goes into ketone bodies.
3. Days 3 to weeks (prolonged starvation): ketone bodies rise from almost zero to 5–7 mM, the brain derives up to about 60% of its energy from them and its glucose need falls to about 40 g per day; protein breakdown falls to about 20 g per day, and the kidney contributes gluconeogenesis from glutamine while excreting $\ce{NH4+}$ that buffers the ketoacids ([7.1.22](/7.1.22#sec-22.1.5)).
4. When the fat is exhausted, essential proteins are degraded, heart and liver fail and death follows. Survival on a fast requires vitamins, minerals and water, but not energy, as long as fat lasts.

![Metabolic adaptation to total fasting. A: plasma fuels during six weeks of starvation (schematic curves through the magnitudes measured by Cahill): glucose falls within two days to 3.5–4 mM and then stays constant; fatty acids rise to about 1.5 mM; β-hydroxybutyrate rises from almost zero to about 6 mM over two to three weeks and acetoacetate to about 1.5 mM, so that ketone bodies supplement glucose for the brain. B: a reserve-depletion model with the fuel stores of the table above and an expenditure of 7.5 MJ per day, in which the protein share of energy falls from about 16% to 4% as ketone bodies spare glucose (and is smaller for a larger fat store): fat lasts about 83 days for the lean and about 14 months for the obese man, consistent with Lehninger's estimates of three and fourteen months; by then the lean man has lost about a third of his protein](./plots/starvation-time-course.py)

The insulin that remains in fasting is essential: by restraining lipolysis and ketogenesis it keeps the ketone bodies near 5–7 mM, within the capacity of the bicarbonate buffer. In its absence (untreated type 1 diabetes, 29.5.3) the same pathways run without a brake.

### 29.3.5. Epinephrine and Cortisol

**Definition 29.3.4 (Epinephrine and Cortisol)** **Epinephrine** (adrenaline) is the catecholamine of the adrenal medulla, released with norepinephrine on sympathetic stimulation, that prepares the body for activity ("fight or flight") through α- and β-adrenergic receptors. **Cortisol** is the glucocorticoid of the adrenal cortex, released through the hypothalamic–pituitary–adrenal axis in response to stress (including hypoglycemia, fasting, infection, pain and anxiety), that acts through the glucocorticoid receptor, a nuclear receptor, on the expression of metabolic enzymes.

Epinephrine acts within seconds. It raises heart rate, blood pressure and airway diameter, and mobilizes fuel: glycogenolysis in liver and muscle (through cAMP and, in liver, also $\ce{Ca^2+}$ via α1 receptors), glycolysis in muscle, lipolysis in adipose tissue; it stimulates glucagon and inhibits insulin secretion, which reinforces mobilization ([7.1.14](/7.1.14#sec-14.2.2)). Cortisol acts over hours: it induces PEP carboxykinase, glucose 6-phosphatase and the enzymes of amino acid **catabolism** in the liver, promotes the breakdown of muscle protein and the release of fatty acids and glycerol from adipose tissue, and so raises blood glucose and liver glycogen; its actions counter those of insulin. Sustained excess, as in Cushing's syndrome (a pituitary tumor making ACTH, an adrenal tumor, or long-term glucocorticoid drugs), causes hyperglycemia, muscle wasting, central obesity and osteoporosis; its deficiency, in Addison's disease, causes hypoglycemia and inability to withstand stress and is treated with hydrocortisone (the pharmaceutical name of cortisol).

The four hormones and three tissues form the memory table of the chapter (↑ stimulated, ↓ inhibited):

| | Liver | Skeletal muscle | Adipose tissue |
|---|---|---|---|
| Insulin (fed) | glucose uptake (glucokinase) ↑, glycogen synthesis ↑, glycolysis ↑, fatty acid and TAG synthesis ↑ (VLDL), gluconeogenesis ↓, glycogenolysis ↓, ketogenesis ↓ | GLUT4 glucose uptake ↑, glycogen synthesis ↑, protein synthesis ↑, proteolysis ↓ | GLUT4 glucose uptake ↑, LPL ↑, TAG synthesis ↑, lipolysis ↓ |
| Glucagon (fasting) | glycogenolysis ↑, gluconeogenesis ↑ (PEPCK), ketogenesis ↑, glycolysis ↓ (F2,6BP ↓, pyruvate kinase ↓), glycogen synthesis ↓, fatty acid synthesis ↓ | no receptors | (minor in humans) |
| Epinephrine (activity) | glycogenolysis ↑, gluconeogenesis ↑ | glycogenolysis ↑, glycolysis ↑ | lipolysis ↑ |
| Cortisol (stress) | gluconeogenesis ↑ (enzyme induction), glycogen storage ↑ | proteolysis ↑, glucose uptake ↓ | lipolysis ↑ |

### 29.3.6. A Minimal Model of Glucose Tolerance

The feedback between glucose and insulin can be written as a small dynamical system, and the model is used in clinical research to measure insulin sensitivity from a single intravenous glucose tolerance test (IVGTT).

**Example 29.3.1 (Bergman's Minimal Model)** Let $G(t)$ be the plasma glucose, $I(t)$ the plasma insulin, and $X(t)$ the action of insulin in a remote compartment (interstitial fluid, where insulin must go to reach its receptors), and let $G_{\mathrm{b}}, I_{\mathrm{b}}$ be the basal values. Richard Bergman's minimal model (1979) is

$$
\begin{aligned}
\frac{\mathrm{d}G}{\mathrm{d}t} &= -(S_{\mathrm{G}} + X)\,G + S_{\mathrm{G}}G_{\mathrm{b}},\\
\frac{\mathrm{d}X}{\mathrm{d}t} &= -p_2 X + p_2 S_{\mathrm{I}}\,(I - I_{\mathrm{b}}),
\end{aligned}
\tag{29.1}
$$
in which $S_{\mathrm{G}}$ (glucose effectiveness, about $0.025\,\mathrm{min^{-1}}$) is the ability of glucose itself to promote its own uptake and suppress its production at basal insulin, $p_2$ the rate constant with which insulin action rises and decays, and $S_{\mathrm{I}}$ the insulin sensitivity, the increase of fractional glucose disappearance per unit of insulin above basal (in min⁻¹ per pmol L⁻¹). In the IVGTT, glucose (0.3 g per kg) is injected, insulin is measured, and $S_{\mathrm{G}}, p_2, S_{\mathrm{I}}$ are estimated by **nonlinear regression** of Eq. (29.1) on the glucose curve. To simulate the test we add a model of secretion: a first-phase release $\Phi_1$ at $t = 0$ and $\mathrm{d}I/\mathrm{d}t = -n(I - I_{\mathrm{b}}) + \gamma\max(G - G_{\mathrm{b}}, 0)$, with clearance $n \approx 0.15\,\mathrm{min^{-1}}$. A subject who is four times less sensitive to insulin but secretes four times more insulin clears the glucose exactly like a normal subject (in this model the product $S_{\mathrm{I}}(I - I_{\mathrm{b}})$ is what matters), whereas the same insulin resistance with failing secretion gives a slow, diabetic glucose curve. The product $S_{\mathrm{I}}\Phi_1$, the disposition index, is roughly constant among people with normal glucose tolerance (Kahn, 1993): the β cells compensate for insulin resistance by secreting more, along a hyperbola, and type 2 diabetes appears when they can no longer do so.

![Simulation of Bergman's minimal model (Example 29.3.1) for an intravenous glucose tolerance test with illustrative parameters. A: plasma glucose after a bolus raising it to 16 mM, for a normal subject (insulin sensitivity S_I = 1.0 × 10⁻⁴ min⁻¹ per pmol L⁻¹), an insulin-resistant subject compensated by fourfold higher secretion (the two curves coincide) and an insulin-resistant subject with failing β cells; K_G is the fractional rate of glucose disappearance between 10 and 40 min, used clinically as an index of glucose tolerance. B: plasma insulin (logarithmic scale), the compensated subject with hyperinsulinemia. C: first-phase insulin against insulin sensitivity; subjects on the hyperbola of constant disposition index tolerate glucose equally well, the subject below it has diabetes](./plots/minimal-model.py)

The model is minimal in the sense of having the fewest parameters that still fit an IVGTT; larger models of glucose homeostasis are used to test insulin pumps and closed-loop controllers ("artificial pancreas") in silico. Tools: the solution of nonlinear ordinary differential equations and their stability ([2.4](/2.4)), and parameter estimation by nonlinear least squares ([3.3](/3.3)).

## 29.4. Obesity and the Regulation of Body Mass

Obesity is defined by the body mass index (BMI, body mass in kilograms divided by the square of height in meters): 18.5–25 is normal, 25–30 overweight, above 30 obese, above 40 severely obese. More than 40% of adults in the United States are obese, and obesity greatly raises the risk of type 2 diabetes, cardiovascular disease and several cancers. To a first approximation obesity results from taking in more energy than is spent; an excess can be stored as fat, burnt in extra activity, or wasted as heat by uncoupled mitochondria. Body mass is nonetheless remarkably stable in most adults, which suggests regulation around a set point: when fat mass rises, a signal from adipose tissue should reduce feeding and raise expenditure, and the reverse when it falls (the adiposity negative-feedback model). The search for this signal revealed that adipose tissue is an endocrine organ.

### 29.4.1. Adipokines

**Definition 29.4.1 (Adipokine)** An **adipokine** is a peptide hormone or cytokine secreted by adipose tissue that signals the state of the fat stores to other tissues and to the brain; adipokines made by adipocytes include leptin, adiponectin, resistin, visfatin (NAMPT), apelin, omentin and chemerin, and adipose tissue also releases cytokines and factors shared with other systems, such as interleukin-6, tumor necrosis factor α, monocyte chemoattractant protein 1 (MCP-1) and plasminogen activator inhibitor 1.

### 29.4.2. Leptin

**Definition 29.4.2 (Leptin)** **Leptin** (Greek *leptos*, thin) is the 16 kDa adipokine (167 residues including its signal peptide), product of the *OB* (*LEP*) gene, secreted by adipocytes in proportion to their number and size, which signals to the hypothalamus that the fat stores are adequate and so reduces feeding and increases energy expenditure.

Leptin was discovered in 1994 by Jeffrey Friedman's group by positional cloning of the mouse *ob* **gene**. *ob/ob* mice, which make no functional leptin, behave as if constantly starved: they eat without restraint, are cold-intolerant, infertile and insulin-resistant, and weigh up to three times as much as normal mice; daily injections of leptin make them eat less, move more and lose weight. *db/db* mice, equally obese and diabetic, lack the leptin receptor, a cytokine-type receptor without its own enzyme activity that signals through the **JAK–STAT pathway** ([7.1.15](/7.1.15#sec-15.2)): leptin binding dimerizes the receptor, JAK2 phosphorylates it and STAT3, and STAT3 dimers enter the nucleus.

In the arcuate nucleus of the hypothalamus two antagonistic populations of neurons respond to leptin (and insulin). Anorexigenic (appetite-suppressing) POMC neurons are stimulated and release α-MSH, cleaved from POMC, which acts on melanocortin-4 receptors (MC4R) of second-order neurons: eat less, spend more. Orexigenic (appetite-stimulating) neurons, which release neuropeptide Y and agouti-related peptide (an **antagonist** of MC4R), are inhibited. Leptin also increases sympathetic outflow to brown and beige fat, where norepinephrine, through β-adrenergic receptors and protein kinase A, mobilizes fatty acids and induces UCP1, so that fat is burnt as heat. When fat mass falls, leptin falls, NPY rises, appetite increases and thermogenesis and fat mobilization slow: the system defends the fat store against loss more strongly than against gain, which is one reason why weight lost by dieting tends to be regained.

Human obesity, however, is rarely leptin deficiency. Obese people have high leptin, in proportion to their fat mass, and are resistant to it; suppressor of cytokine signaling 3 (SOCS3), induced by leptin itself, and the phosphatase PTP1B inhibit the receptor, and inflammation of the hypothalamus contributes. Leptin injections do not make obese people lose weight, except the very rare patients with congenital leptin deficiency, in whom recombinant leptin (metreleptin, also used for the lipodystrophies, in which a lack of fat causes leptin deficiency) has dramatic effects. Mutations of MC4R are the most common monogenic cause of human obesity, and an MC4R **agonist** (setmelanotide) treats some genetic obesity syndromes.

### 29.4.3. Adiponectin

**Definition 29.4.3 (Adiponectin)** **Adiponectin** is the adipokine (244 residues, about 30 kDa) secreted almost exclusively by adipocytes and abundant in plasma (5–30 µg/mL, about 0.01% of plasma protein), whose level is inversely related to fat mass and which increases the insulin sensitivity of liver and muscle and the oxidation of fatty acids.

Adiponectin has four regions: an N-terminal signal peptide, a short hypervariable region, a collagen-like **domain** of 22 Gly–X–Y repeats, and a C-terminal globular domain homologous to complement C1q (and structurally to tumor necrosis factor). Three monomers form a trimer through their collagen-like domains (the low-molecular-weight form); two trimers joined by a disulfide bond through Cys39 of the hypervariable region form a hexamer (the middle-molecular-weight form); and 12- to 18-mers form the high-molecular-weight (HMW) form. Assembly in the endoplasmic reticulum requires the hydroxylation and **glycosylation** of lysines of the collagen-like domain and the disulfide-forming machinery of the ER, and ER oxidoreductases control the secretion of the **multimers** (ERp44 retains them, Ero1-Lα releases them, and DsbA-L promotes multimerization). The HMW form is the most active on insulin sensitivity, and the proportion of HMW adiponectin is a better marker of insulin sensitivity than total adiponectin.

Adiponectin acts through two receptors, AdipoR1 (abundant in muscle) and AdipoR2 (in liver), which have seven transmembrane helices but the opposite topology to GPCRs (intracellular N-terminus) and belong to a family of membrane hydrolases (PAQR) with ceramidase activity; they are not **G protein**–coupled. Through the adaptor APPL1 and LKB1, AdipoR1 activates AMPK (29.4.4), and AdipoR2 activates PPARα (29.4.6). The results are increased fatty acid uptake and β oxidation in muscle, inhibition of gluconeogenesis and lipogenesis in the liver, and increased glucose uptake. Adiponectin also acts on the brain, where it increases food intake when fat stores are low (Lehninger's "fat tissue depleted" signal). Plasma adiponectin falls in obesity, type 2 diabetes, the metabolic syndrome, hypertension and coronary artery disease, and rises with weight loss, caloric restriction and treatment with thiazolidinediones, which act on PPARγ in adipocytes; it has insulin-sensitizing, anti-inflammatory and anti-atherogenic actions.

### 29.4.4. AMPK, the Energy Sensor

**Definition 29.4.4 (AMP-Activated Protein Kinase)** **AMP-activated protein kinase** (AMPK) is the heterotrimeric Ser/Thr protein kinase (catalytic α, scaffolding β and nucleotide-binding γ subunits) that is activated when the ratios [AMP]/[ATP] and [ADP]/[ATP] rise, and that restores cellular energy by phosphorylating enzymes and transcription factors so as to stimulate ATP-producing and inhibit ATP-consuming pathways.

The γ **subunit** has four cystathionine β-synthase (CBS) repeats that bind AMP, ADP or ATP competitively. Because **adenylate kinase** keeps $2\,\mathrm{ADP} \rightleftharpoons \mathrm{ATP} + \mathrm{AMP}$ near equilibrium, [AMP] varies roughly as the square of [ADP], so a small fall of [ATP] produces a large relative rise of [AMP], a sensitive signal of energy stress ([7.1.17](/7.1.17#sec-17.3.5)). AMP activates AMPK in three ways: allosterically (up to about tenfold), by promoting the phosphorylation of Thr172 of α by the upstream kinase LKB1, and by protecting Thr172 from phosphatases (ADP shares the last two effects); phosphorylation of Thr172 increases activity more than a hundredfold. A rise of cytosolic $\ce{Ca^2+}$ activates AMPK through a second upstream kinase, CaMKK2, without a change of nucleotides, and low glucose activates it through a lysosomal pathway in which aldolase, free of its substrate fructose 1,6-bisphosphate, assembles AXIN and LKB1 with AMPK. AMPK is thus activated by exercise, fasting, hypoxia, metabolic poisons and adiponectin, and inhibited by plenty.

| AMPK target | Effect of phosphorylation | Metabolic result |
|---|---|---|
| acetyl-CoA carboxylase (ACC1 in liver and fat, ACC2 in muscle) | inactivation | malonyl-CoA ↓: fatty acid synthesis ↓, CPT1 disinhibited, β oxidation ↑ ([7.1.21](/7.1.21#sec-21.5.1)) |
| **HMG-CoA reductase** | inactivation | cholesterol synthesis ↓ |
| glycerol-3-phosphate acyltransferase | inactivation | TAG and phospholipid synthesis ↓ |
| glycogen synthase | inactivation | glycogen synthesis ↓ |
| TBC1D1 (muscle) | inactivation of its **GAP** activity | GLUT4 translocation and glucose uptake ↑ (insulin-independent, in exercise) |
| SREBP-1c, ChREBP | inhibition | lipogenic gene expression ↓ |
| PGC-1α | activation | mitochondrial biogenesis ↑ |
| TSC2, raptor | activation, inhibition | mTORC1 ↓: protein synthesis ↓ |
| ULK1 | activation | autophagy ↑ |

In the hypothalamus AMPK integrates the bottom-up signals: ghrelin, adiponectin and low glucose activate it and increase feeding, leptin and insulin inhibit it.

![AMPK and mTORC1, the energy and nutrient sensors (activity-flow diagram; green open arrows activation, red bars inhibition). AMPK is activated by a rise of AMP and ADP (exercise, fasting, hypoxia), by LKB1, which phosphorylates Thr172, by adiponectin and, indirectly, by metformin. It inactivates acetyl-CoA carboxylase (ACC), HMG-CoA reductase (HMGR), glycerol-3-phosphate acyltransferase (GPAT) and glycogen synthase, promotes GLUT4 translocation through TBC1D1 and mitochondrial biogenesis through PGC-1α, activates ULK1 (autophagy), and inhibits mTORC1 by activating TSC2 and phosphorylating raptor. mTORC1 is activated by amino acids through the Rag GTPases and by Rheb·GTP when insulin, through PKB, inhibits TSC2, the GTPase-activating protein of Rheb; it stimulates protein synthesis (S6K, 4E-BP), lipid synthesis (SREBP) and nucleotide synthesis (CAD, ATF4) and inhibits autophagy](./plots/ampk-mtor.py)

### 29.4.5. mTORC1, the Nutrient Sensor

**Definition 29.4.5 (mTORC1)** **mTORC1** (mechanistic target of rapamycin complex 1) is the complex of the Ser/Thr kinase mTOR with the scaffold raptor and other proteins that, on the cytosolic surface of lysosomes, integrates signals of amino acid sufficiency, growth factors and insulin, energy and oxygen, and when they are favorable phosphorylates the proteins that drive anabolism and cell growth.

mTORC1 is recruited to the lysosome by the Rag GTPases, which are loaded according to the amino acids sensed in the cytosol and in the lysosome (leucine, arginine, methionine through **SAM**) and are anchored by the Ragulator complex, and is activated there by the **small G protein** Rheb in its GTP form. Rheb is switched off by the TSC complex, its **GTPase-activating protein**; insulin, through PKB, phosphorylates and inhibits TSC2, so that Rheb·GTP accumulates, while AMPK activates TSC2 and phosphorylates raptor. Active mTORC1 phosphorylates S6 kinase and the 4E-binding proteins, which accelerates **translation** ([7.2.20](/7.2.20#sec-20.4)), activates **SREBP** (lipid and cholesterol synthesis) and HIF-1α (glycolysis), stimulates nucleotide synthesis (CAD through S6K and the mitochondrial folate cycle through ATF4, [7.1.28](/7.1.28#sec-28.3.3)), and inhibits autophagy and lysosome biogenesis (ULK1, TFEB). The lysosome, where **macromolecules** are recycled, is thus the place where the cell decides whether it has the parts to grow. Fasting inactivates mTORC1 (through AMPK and the absence of insulin and amino acids), so proteins and glycogen are broken down; chronic activation by overeating promotes fat deposition in liver and muscle, and S6K phosphorylates the **insulin receptor** substrate IRS1 on serine, a negative feedback that contributes to insulin resistance. Activating mutations in the pathway (PI3K, loss of PTEN or TSC) are common in cancer, and rapamycin analogs are used as immunosuppressants and anticancer drugs.

### 29.4.6. PPARs: Diet Regulates Gene Expression

**Definition 29.4.6 (PPAR)** The **PPARs** (peroxisome proliferator-activated receptors) are nuclear receptors activated by fatty acids and their derivatives that, as heterodimers with the retinoid X receptor RXR, bind response elements of DNA and regulate the transcription of genes of lipid and glucose metabolism; they were named for their ability to cause peroxisome proliferation in rodent liver.

| Isoform | Main tissues | **Ligands** and drugs | Genes and effects |
|---|---|---|---|
| PPARα | liver, heart, kidney, muscle, brown fat | fatty acids, eicosanoids; fibrates | fatty acid uptake, β oxidation, ketogenesis (activated in fasting) |
| PPARγ | adipose tissue (also macrophages) | fatty acids, prostaglandin derivatives; thiazolidinediones | adipocyte differentiation, lipid storage, adiponectin; whole-body insulin sensitivity |
| PPARδ (β) | muscle, liver, widely | fatty acids | fatty acid oxidation and uncoupling; fat depletion, endurance |

Thiazolidinediones (pioglitazone, rosiglitazone) improve insulin sensitivity by activating PPARγ: more, smaller adipocytes store more fat safely, the release of fatty acids falls, and adiponectin rises (29.5.4).

### 29.4.7. Short-Term Control: Ghrelin, Gut Hormones and Endocannabinoids

Leptin and insulin report the size of the fat store over days; meals are regulated by signals over minutes and hours.

- Ghrelin, a 28-residue peptide of the stomach whose Ser3 is octanoylated by ghrelin O-acyltransferase (GOAT), acts on a GPCR (via $\mathrm{G_q}$ and $\mathrm{IP_3}$) of the hypothalamic NPY neurons and is the only known circulating hormone that stimulates appetite. Its plasma level rises before habitual meals and falls sharply after them; injected into people, it causes intense hunger. In Prader–Willi syndrome very high ghrelin accompanies uncontrollable appetite and severe obesity.
- $\mathrm{PYY_{3-36}}$ (34 residues), secreted by endocrine cells of the ileum and colon in proportion to the meal, inhibits the NPY neurons through Y2 receptors; GLP-1 and cholecystokinin also signal satiety. GLP-1 is cut from proglucagon by PC1/3 in intestinal L cells (PC2 in α cells gives glucagon instead), and is inactivated within minutes by dipeptidyl peptidase-4 (DPP-4).
- Endocannabinoids (anandamide and 2-arachidonoylglycerol, lipid messengers derived from arachidonate) act on cannabinoid receptors (CB1 in the brain, CB2 in the periphery) to increase appetite and the reward of palatable, fatty food; Δ⁹-tetrahydrocannabinol of cannabis acts on the same receptors. The CB1 antagonist rimonabant reduced weight but was withdrawn in 2008 because of depression and suicidal thoughts, an example of how closely appetite is tied to mood.
- The gut microbiota (about $10^{14}$ cells) ferments indigestible carbohydrate to short-chain fatty acids (acetate, propionate, butyrate), which are fuels and signals acting through GPCRs (FFAR2 and FFAR3), and converts primary to secondary **bile acids**, which act through the **nuclear receptor** FXR and the GPCR TGR5 on metabolism and thermogenesis; microbial conversion of choline and carnitine to trimethylamine, oxidized in the liver to trimethylamine N-oxide, is associated with atherosclerosis. Mice colonized with the microbiota of obese donors gain more fat than those colonized with lean donors' microbiota, but the causal role of the microbiota in human obesity is still being defined.

The redundancy and asymmetry of these controls (many signals defending against starvation, few against excess) probably reflect an evolutionary history in which famine was the main threat.

### 29.4.8. Acetylation of Metabolic Enzymes

Phosphorylation is not the only covalent modification that coordinates metabolism. Proteomic surveys (Zhao and colleagues, 2010) found that nearly every enzyme of glycolysis, gluconeogenesis, the citric acid cycle, the urea cycle, fatty acid metabolism and glycogen metabolism in human liver is acetylated on lysine residues, and that the extent of acetylation changes with the supply of glucose, amino acids and fatty acids. Examples: acetylation activates malate dehydrogenase and the enoyl-CoA hydratase/3-hydroxyacyl-CoA dehydrogenase of β oxidation, inhibits argininosuccinate lyase, and targets PEP carboxykinase for **ubiquitination** and degradation. Two features make acetylation a natural metabolic signal:

- its donor is acetyl-CoA, a central intermediate produced and consumed by many pathways, whose concentration reflects the nutrient state; in the mitochondrial matrix, where acetyl-CoA is abundant and the pH is high, much acetylation is nonenzymatic;
- its removal by the sirtuins, deacetylases that use $\ce{NAD+}$ as cosubstrate, couples it to the redox state: in fasting the mitochondrial sirtuin SIRT3 deacetylates and activates enzymes of fat oxidation and ketogenesis (long-chain acyl-CoA dehydrogenase, HMG-CoA synthase 2).

Because **metabolic pathways** form a network with shared intermediates, a single modification that tracks acetyl-CoA and $\ce{NAD+}$ and acts on many enzymes at once can coordinate several pathways, as the slides of the course emphasize.

## 29.5. Diabetes Mellitus

**Definition 29.5.1 (Diabetes Mellitus)** **Diabetes mellitus** is a group of metabolic diseases characterized by chronic hyperglycemia resulting from defective insulin secretion, insulin action, or both. In **type 1 diabetes** autoimmune destruction of the β cells causes absolute insulin deficiency; in **type 2 diabetes** insulin resistance is combined with a progressive, relative failure of insulin secretion.

The name means "excessive excretion of sweet urine": when plasma glucose exceeds the renal threshold of about 10 mM (180 mg/dL), glucose appears in the urine and draws water with it. About one adult in ten worldwide has diabetes, about 90% of it type 2. Other forms include gestational diabetes, monogenic diabetes (MODY, neonatal diabetes, 29.3.2) and diabetes secondary to pancreatic disease or drugs.

### 29.5.1. Type 1 and Type 2

| | Type 1 | Type 2 |
|---|---|---|
| Cause | autoimmune destruction of β cells (autoantibodies to insulin, GAD65, IA-2, ZnT8); genetic risk mainly from HLA class II alleles | insulin resistance of muscle, liver and fat plus β-cell dysfunction; many common variants of small effect (TCF7L2 the strongest) and environment |
| Onset | usually in childhood or youth (can occur at any age), often abrupt | usually in adulthood, gradual, often unnoticed for years |
| Body weight | usually normal or low | about 80–90% overweight or obese |
| Insulin | absent (C peptide undetectable) | normal or high early, falling later |
| Ketoacidosis | common without insulin | rare (residual insulin restrains lipolysis) |
| Treatment | insulin (injections, pumps, closed-loop systems), islet transplantation | lifestyle, oral and injectable drugs, insulin when secretion fails |

The history of insulin is one of the great stories of biochemistry: in 1889 Oskar Minkowski and Josef von Mering found that removal of the pancreas makes dogs diabetic; in 1921–1922 Frederick Banting and Charles Best, in the laboratory of J. J. R. Macleod, with the biochemist James Collip, prepared an active pancreatic extract and treated the first patient, the 14-year-old Leonard Thompson (Nobel Prize 1923); Frederick Sanger sequenced insulin, the first protein sequence (1955); and recombinant human insulin, from 1982, was the first product of genetic engineering.

### 29.5.2. Diagnosis: Glucose Tolerance and HbA1c

The diagnostic criteria (American Diabetes Association and WHO) are any one of: fasting plasma glucose ≥ 7.0 mM (126 mg/dL); plasma glucose ≥ 11.1 mM (200 mg/dL) two hours after an oral load of 75 g of glucose (the oral glucose tolerance test); HbA1c ≥ 6.5% (48 mmol/mol); or a random glucose ≥ 11.1 mM with symptoms. In a healthy person the oral load raises glucose to no more than about 8–10 mM and it returns to the fasting level within two hours, with no glucose in the urine; in diabetes the curve rises higher and falls slowly. Blood glucose is measured enzymatically, with glucose oxidase (glucose + $\ce{O2}$ → gluconolactone + $\ce{H2O2}$, the peroxide read by a coupled dye or electrode) or glucose dehydrogenase ([7.1.10](/7.1.10#sec-10.1.3)).

**Definition 29.5.2 (Glycated Hemoglobin)** **Glycated hemoglobin** (HbA1c) is hemoglobin A carrying glucose on the N-terminal valine of a β chain, formed by nonenzymatic **glycation** (a Schiff base rearranged to a stable Amadori ketoamine) at a rate proportional to the glucose concentration; expressed as a fraction of total hemoglobin it integrates blood glucose over the lifespan of erythrocytes (about 120 days).

Normal HbA1c is about 4–5.6%; 5.7–6.4% indicates prediabetes, ≥ 6.5% diabetes, and treatment usually aims at about 7%. The relation to mean glucose is nearly linear: the ADAG study (Nathan and colleagues, 2008) found estimated average glucose (mg/dL) = 28.7 × A1C(%) − 46.7, so that 5% corresponds to about 5.4 mM (97 mg/dL), 7% to 8.6 mM (154 mg/dL) and 12% to 16.5 mM (298 mg/dL).

**Example 29.5.1 (HbA1c as a Moving Average)** Erythrocytes are made at a constant rate and removed at age $T \approx 120$ days, so their ages are uniformly distributed on $(0, T)$. Inside a cell, **glycation** is pseudo-first-order in glucose with rate constant $k$, so a cell of age $a$ has a glycated fraction $h = 1 - \exp\bigl(-k\int_{t-a}^{t} G(s)\,\mathrm{d}s\bigr)$, and HbA1c is the average of $h$ over ages:

$$
\mathrm{A1c}(t) = \frac{1}{T}\int_0^T \Bigl[1 - \exp\Bigl(-k\int_{t-a}^{t} G(s)\,\mathrm{d}s\Bigr)\Bigr]\mathrm{d}a \approx \frac{k}{T}\int_0^T (T - s)\,G(t - s)\,\mathrm{d}s. \tag{29.2}
$$
The approximation (small glycated fractions, order of integration exchanged) shows that HbA1c is a weighted average of past glucose with weights decreasing linearly from today to $T$ days ago. The glucose of the last 30 days thus contributes $1 - (1 - 30/120)^2 \approx 44\%$ of the value, and after a step change of glucose half of the change of HbA1c is reached after $T(1 - 1/\sqrt{2}) \approx 35$ days and all of it after a full lifespan. With constant glucose, $\mathrm{A1c} \approx kGT/2$; $k \approx 1.4\times10^{-4}$ per mM per day reproduces 7% at 8.6 mM. The model has no intercept, unlike the empirical regression, and HbA1c is misleading when erythrocyte survival is abnormal (hemolytic anemia, recent transfusion, iron deficiency) or a hemoglobin variant is present.

![HbA1c as a time-averaging sensor of blood glucose (Example 29.5.1). A: steady-state HbA1c of the erythrocyte-lifespan model against mean glucose, compared with the empirical ADAG regression (estimated average glucose = 28.7 A1C − 46.7 mg/dL), with the normal range and the diagnostic threshold of 6.5% shaded. B: response of HbA1c to an improvement of control, mean glucose falling from 12 to 7 mM on day 0: half of the change takes about 35 days and the new value is reached only after a full erythrocyte lifespan](./plots/hba1c-model.py)

### 29.5.3. Ketoacidosis

**Definition 29.5.3 (Ketoacidosis)** **Ketoacidosis** is the metabolic acidosis caused by the overproduction of the ketone bodies acetoacetate and β-hydroxybutyrate, carboxylic acids ($\mathrm{p}K_{\mathrm{a}}$ about 3.6 and 4.4) that release protons faster than the **bicarbonate buffer system** can neutralize them; in diabetic ketoacidosis ketone bodies exceed about 3 mM (often 10–25 mM), plasma bicarbonate falls below about 15–18 mM and the blood pH below 7.3.

Without insulin, and with glucagon unopposed, three brakes fail at once ([7.1.21](/7.1.21#sec-21.6.3)): hormone-sensitive lipase releases fatty acids from adipose tissue without restraint; in the liver malonyl-CoA falls, so CPT1 lets all fatty acids into the mitochondria; and gluconeogenesis withdraws oxaloacetate, while the high [**NADH**]/[$\ce{NAD+}$] of β oxidation slows the citric acid cycle, so acetyl-CoA goes to ketone bodies faster than extrahepatic tissues can oxidize them. At the same time glucose production rises and its uptake falls. Glucose and ketone bodies spill into the urine with water and sodium, causing dehydration; acetone, formed by spontaneous decarboxylation of acetoacetate, gives the breath a fruity smell; and the deep, rapid breathing (Kussmaul respiration) is the respiratory compensation of the **acidosis** ([7.1.2](/7.1.2#sec-2.3.4)). Untreated, ketoacidosis leads to coma and death. Treatment is insulin, fluid and potassium replacement (insulin drives $\ce{K+}$ into cells); bicarbonate is reserved for very severe acidosis. The contrast with starvation is instructive: in starvation the residual insulin keeps ketone bodies near 5–7 mM and the pH normal (29.3.4). SGLT2 inhibitors can cause ketoacidosis with near-normal glucose (euglycemic ketoacidosis), because they lower glucose, and with it insulin, while glucagon rises.

### 29.5.4. Insulin Resistance and Lipotoxicity

**Definition 29.5.4 (Insulin Resistance)** **Insulin resistance** is a state in which more insulin than normal is needed to produce a given biological effect, in particular glucose uptake by muscle and adipose tissue and suppression of glucose production by the liver.

Type 2 diabetes develops in stages. Insulin resistance, typically associated with abdominal obesity and inactivity, is first compensated by β cells that secrete more insulin (hyperinsulinemia, Example 29.3.1); glucose stays normal or nearly so. The intermediate stage is often accompanied by the metabolic syndrome:

**Definition 29.5.5 (Metabolic Syndrome)** The **metabolic syndrome** is a cluster of risk factors for type 2 diabetes and cardiovascular disease in one individual, diagnosed when at least three of the following are present: abdominal obesity, elevated fasting glucose, high plasma triacylglycerol, low HDL cholesterol and high blood pressure; it is often accompanied by markers of a prothrombotic and inflammatory state (high fibrinogen, high C-reactive protein).

Finally the β cells fail (through glucotoxicity, lipotoxicity, ER stress, **amyloid** deposits of islet amyloid **polypeptide**, and a genetic predisposition: most genetic variants associated with type 2 diabetes act on β-cell function), and hyperglycemia appears. The lipid-toxicity hypothesis explains the link with obesity (after Lehninger 8e, Fig. 23-42, where the receptor regulating adipocyte storage should read PPARγ):

1. In healthy adipose tissue, PPARγ keeps adipocytes insulin-sensitive and able to store triacylglycerol.
2. When caloric excess fills the adipocytes, adipose tissue can no longer expand safely; hypertrophic adipocytes release MCP-1, which attracts macrophages (up to half of the cells of obese adipose tissue), whose TNF-α impairs storage and promotes lipolysis.
3. Fatty acids released into the blood enter liver and muscle, which store them as ectopic triacylglycerol droplets and accumulate lipid intermediates.
4. **Diacylglycerol** activates novel **protein kinase C** isoforms (PKCε in liver, PKCθ in muscle), which phosphorylate the insulin receptor or IRS1 on serine and threonine; **ceramides** inhibit PKB; and inflammatory kinases (JNK, IKKβ) add further inhibitory phosphorylation. The PI3K–PKB signal is weakened, GLUT4 translocation and glycogen synthesis fall in muscle, and the liver keeps making glucose (and, paradoxically, fat, because the lipogenic branch of insulin signaling remains sensitive).

Only a minority of obese people develop diabetes, and the hypothesis explains why the location of fat matters: subcutaneous fat that can expand is protective, visceral and ectopic fat is harmful; in lipodystrophy, with no adipose tissue at all, severe insulin resistance develops even without obesity. Adiponectin falls in obesity and rises with weight loss, linking fat mass to insulin sensitivity through AMPK (29.4.3).

Chronic hyperglycemia damages small and large blood vessels, giving the complications of diabetes: retinopathy (a leading cause of blindness), nephropathy (the leading cause of kidney failure), neuropathy (loss of sensation, foot ulcers), and atherosclerosis with heart attack and stroke. The mechanisms include the formation of advanced glycation end products and their receptor RAGE ([7.1.10](/7.1.10#sec-10.1.3)), the polyol pathway (aldose reductase reducing glucose to sorbitol, consuming NADPH), activation of protein kinase C by diacylglycerol made from glycolytic intermediates, flux into the hexosamine pathway, and mitochondrial production of **reactive oxygen species** ([7.1.23](/7.1.23#sec-23.1.9)). Large trials showed that lowering HbA1c reduces the microvascular complications, which is why HbA1c is the target of treatment.

### 29.5.5. Treatment of Type 2 Diabetes

| Intervention | Molecular target | Effect |
|---|---|---|
| weight loss (diet), exercise | lipid burden of adipocytes, liver and muscle; AMPK and insulin-independent GLUT4 translocation in exercising muscle | restores insulin sensitivity; remission in many recent cases with large weight loss |
| metformin (biguanide) | mitochondrial respiration (**complex I**) and the redox state of hepatocytes; AMPK activation, partly through a lysosomal pathway at low doses | hepatic glucose production ↓; weight-neutral, no hypoglycemia; first-line drug |
| sulfonylureas (glipizide, glibenclamide, glimepiride) | SUR1 of the β-cell $\mathrm{K_{ATP}}$ channel | insulin secretion ↑, independent of glucose (risk of hypoglycemia) |
| thiazolidinediones (pioglitazone) | PPARγ in adipocytes | insulin sensitivity ↑, adiponectin ↑; weight gain, fluid retention |
| DPP-4 inhibitors (sitagliptin) | dipeptidyl peptidase-4 | endogenous GLP-1 and GIP ↑: glucose-dependent insulin secretion ↑, glucagon ↓ |
| GLP-1 receptor agonists (liraglutide, semaglutide, dulaglutide); dual GIP/GLP-1 agonist (tirzepatide) | GLP-1 (and GIP) receptors of β cells, α cells and brain | insulin ↑, glucagon ↓, gastric emptying slowed, appetite ↓: weight loss of about 10–20%; cardiovascular benefit |
| SGLT2 inhibitors (empagliflozin, dapagliflozin) | $\ce{Na+}$–glucose **cotransporter** 2 of the proximal tubule | urinary glucose loss (tens of grams per day) ↑; heart failure and kidney disease ↓ |
| insulin and its analogs (fast-acting lispro, long-acting glargine) | insulin receptor | replaces failing secretion |
| bariatric surgery (Roux-en-Y gastric bypass, sleeve gastrectomy) | gut hormones (GLP-1, PYY) and food intake | large weight loss; diabetes often remits, sometimes before weight is lost |

(After Lehninger 8e, Table 23-7, updated.) The two newest classes have changed the field: GLP-1-based drugs, developed from the incretin physiology of 29.3.2 (exenatide comes from the venom of the Gila monster), produce weight loss approaching that of surgery, and SGLT2 inhibitors, developed from phlorizin, a glucoside of apple bark that blocks renal glucose reabsorption, protect heart and kidney beyond their effect on glucose.

## Summary

| Topic | Key points |
|---|---|
| Hormones (29.1) | Definition 29.1.1; surface receptors fast (activity), nuclear receptors slow (amount); classes from peptides to NO; prohormones (proinsulin → insulin + C peptide, POMC); RIA, **ELISA** |
| Hierarchy (29.1.4–29.1.5) | CNS → hypothalamus (releasing hormones) → anterior pituitary (tropic hormones) → glands; ng → µg → mg; **feedback inhibition** by the final hormone; bottom-up signals from fat, gut, pancreas |
| Tissues (29.2) | liver: G6P five fates, glucose and ketone body export, urea, VLDL; white fat: storage, lipolysis by ATGL, HSL, MGL under PKA/insulin control, **glyceroneogenesis**; brown and beige fat (Definition 29.2.1): UCP1; muscle: fiber types, phosphocreatine, glycogen → lactate, **Cori cycle**; heart: aerobic, fatty acids; brain: 120 g glucose per day, ketone bodies in starvation; blood |
| Insulin and β cells (29.3.1–29.3.2) | Definition 29.3.1; GLUT4, GSK3, PDE3B, SREBP-1c; lipogenic liver; glucose → glucokinase → ATP/ADP ↑ → $\mathrm{K_{ATP}}$ closed (Definition 29.3.2) → depolarization → $\ce{Ca^2+}$ → exocytosis; incretins amplify; sulfonylureas, neonatal diabetes, MODY2 |
| Glucagon, fasting (29.3.3–29.3.4) | Definition 29.3.3; PKA: phosphorylase ↑, synthase ↓, F2,6BP ↓, PK-L ↓, PEPCK induced, ACC ↓; glucogenic liver; reserves 590 MJ fat, 100 MJ protein, 3.8 MJ glycogen; protein sparing by ketone bodies |
| Epinephrine, cortisol (29.3.5) | Definition 29.3.4; fast mobilization vs slow enzyme induction; hormone–tissue matrix |
| Model (29.3.6) | minimal model Eq. (29.1): $S_{\mathrm{G}}$, $p_2$, $S_{\mathrm{I}}$; compensation by secretion; disposition index (Example 29.3.1) |
| Body mass (29.4) | adipokines (Definition 29.4.1); leptin (Definition 29.4.2): *ob*, *db*, JAK–STAT, POMC/α-MSH vs NPY/AgRP, leptin resistance; adiponectin (Definition 29.4.3): LMW, MMW, HMW multimers, AdipoR1/R2 (not GPCRs), AMPK, PPARα |
| Kinase hubs (29.4.4–29.4.5) | AMPK (Definition 29.4.4): γ senses AMP/ADP, LKB1 Thr172, targets ACC, HMGR, GPAT, glycogen synthase, TBC1D1, TSC2/raptor, ULK1; mTORC1 (Definition 29.4.5): Rag, Rheb, TSC; translation, lipid and nucleotide synthesis, autophagy ↓ |
| Gene expression and appetite (29.4.6–29.4.8) | PPARα, γ, δ (Definition 29.4.6); ghrelin, PYY, GLP-1, endocannabinoids, microbiota; acetylation by acetyl-CoA, deacetylation by $\ce{NAD+}$-dependent sirtuins |
| Diabetes (29.5) | Definition 29.5.1; type 1 vs type 2; diagnosis (FPG ≥ 7.0 mM, OGTT ≥ 11.1 mM, HbA1c ≥ 6.5%); HbA1c (Definition 29.5.2) as a 120-day weighted average (Example 29.5.1, Eq. (29.2)); ketoacidosis (Definition 29.5.3); insulin resistance (Definition 29.5.4), metabolic syndrome (Definition 29.5.5), lipotoxicity (DAG → PKC); complications; drugs (metformin, sulfonylureas, TZDs, incretin drugs, SGLT2 inhibitors) |

## Questions

1. Why does glycogen breakdown give glucose in the liver but lactate in muscle during a fight-or-flight response, and what is the advantage to the animal?

   **Answer** The liver has glucose 6-phosphatase and exports free glucose; its job in an emergency is to keep blood glucose up for the brain and to supply working muscle. Muscle lacks glucose 6-phosphatase, so glucose 6-phosphate from phosphorolysis stays in the cell and enters glycolysis; under maximal work the oxygen supply is insufficient and pyruvate is reduced to lactate. Glycolysis from glycogen gives 3 ATP per glucose unit within seconds, far faster than oxidative phosphorylation can be increased, and phosphorolysis saves the ATP of hexokinase. The lactate goes to the liver, which converts it back into glucose after the emergency (Cori cycle), so the cost of anaerobic speed is paid later by the liver.

2. Explain how the sulfonylureas lower blood glucose, why patients with Kir6.2 mutations that keep the $\mathrm{K_{ATP}}$ channel open have neonatal diabetes, and why many of them can be treated with sulfonylureas instead of insulin.

   **Answer** In the β cell a rise of [ATP]/[ADP] closes $\mathrm{K_{ATP}}$, the membrane depolarizes, voltage-gated $\ce{Ca^2+}$ channels open and insulin granules are released. Sulfonylureas bind SUR1 and close the channel independently of ATP, so they trigger insulin release (even at low glucose, hence the risk of hypoglycemia). Activating mutations of Kir6.2 reduce its inhibition by ATP; the channel stays open, the β cell remains hyperpolarized, and glucose cannot trigger secretion, although the cells and their insulin are intact. Because SUR1 is still present and sulfonylureas close the channel by a different site, high doses can override the mutation in many patients, restoring glucose-regulated secretion with tablets. This was one of the first examples of treatment chosen from the molecular diagnosis.

3. In prolonged starvation, protein breakdown falls from about 75 to about 20 g per day although the brain continues to need energy. Explain, and estimate how much protein would be lost per day if the brain continued to use 120 g of glucose per day from amino acids only (assume about 1.7 g protein per g glucose).

   **Answer** After a few days the liver produces ketone bodies at high rates from fatty acids (oxaloacetate is withdrawn for gluconeogenesis, acetyl-CoA accumulates), their plasma level rises to 5–7 mM, and the brain takes them up through monocarboxylate transporters and oxidizes them through succinyl-CoA:acetoacetate CoA transferase, obtaining up to about 60% of its energy from them. Its glucose need falls from about 120 to about 40 g per day, and glycerol from lipolysis covers part of the rest, so much less amino acid carbon is needed. Without this adaptation, 120 g glucose per day from amino acids would require about 200 g of protein per day; the whole 6 kg of body protein would last only about a month, and the loss of about a third of it, which is fatal, would come within about ten days, long before the fat is used up. Ketone bodies thus allow the fat store, not the protein store, to set the duration of survival.

4. Use the minimal model (Example 29.3.1) to explain why a person can have normal glucose tolerance despite marked insulin resistance, and what change marks the transition to type 2 diabetes.

   **Answer** In Eq. (29.1) the effect of insulin on glucose disappearance is $X$, which at quasi-steady state equals $S_{\mathrm{I}}(I - I_{\mathrm{b}})$. If $S_{\mathrm{I}}$ falls fourfold but the β cells secrete four times more insulin, $X$, and so the glucose curve, is unchanged (figure, the compensated and normal curves coincide). Clinically this appears as hyperinsulinemia with normal glucose. The product of sensitivity and secretion, the disposition index, describes β-cell function adjusted for insulin resistance. Type 2 diabetes appears when secretion can no longer rise in proportion to the resistance: the subject falls below the hyperbola, $X$ is too small, and glucose disappearance slows (the third curve). This explains why most insulin-resistant obese people are not diabetic and why β-cell failure, not insulin resistance alone, is decisive.

5. A patient's mean blood glucose falls from 12 mM to 7 mM when treatment starts. Using Example 29.5.1, predict HbA1c at the start, after one month and after four months, and explain why HbA1c is not used to judge a change of treatment after two weeks.

   **Answer** With $\mathrm{A1c} \approx kGT/2$ and $k = 1.42\times10^{-4}$ per mM per day: at 12 mM, about $1.42\times10^{-4}\times12\times60 \approx 10\%$ (9.6% with the exact formula); at 7 mM, about 6% (5.7%). After a step change, the fraction of the change completed after time $\tau$ is $1 - (1 - \tau/T)^2$: after 30 days $1 - 0.75^2 = 0.44$, so HbA1c is about $9.6 - 0.44\times3.9 \approx 7.9\%$; after 120 days the change is complete (about 5.7%). After two weeks only $1 - (106/120)^2 \approx 22\%$ of the change has occurred, too little to distinguish from measurement scatter, so HbA1c is checked every three months; day-to-day control is judged by glucose measurements or continuous glucose monitoring.

6. Compare **ketosis** in a person on a prolonged fast and ketoacidosis in a person with untreated type 1 diabetes: ketone body levels, pH, plasma glucose and the role of insulin.

   **Answer** Fasting: insulin is low but present; glucagon is moderately high. Lipolysis and ketogenesis are active but restrained by the remaining insulin (and ketone bodies themselves stimulate a little insulin secretion), so β-hydroxybutyrate and acetoacetate reach about 5–7 mM, the bicarbonate buffer and renal ammonium excretion compensate, and pH stays normal; plasma glucose is low-normal (3.5–4 mM). Untreated type 1 diabetes: insulin is absent and glucagon is unopposed. Lipolysis is unrestrained, malonyl-CoA falls and CPT1 is fully open, oxaloacetate is drained by gluconeogenesis, and ketone bodies rise to 10–25 mM; their protons exceed the buffer, bicarbonate falls and the pH drops below 7.3 (ketoacidosis). Glucose is very high (often above 15–20 mM) because production is unchecked and muscle and fat cannot take it up; osmotic diuresis dehydrates the patient. The difference is a matter of the insulin level: a small amount of insulin is the brake that keeps ketosis physiological.

7. (Open question) Leptin injections cure the obesity of *ob/ob* mice but not common human obesity, and GLP-1 receptor agonists cause large weight loss in most obese people. Discuss what these observations say about the regulation of body mass, and what kinds of experiments would test whether body mass has a set point.

   **Answer** Outline: (1) *ob/ob* mice lack the signal, so supplying it restores the feedback; common obesity has high leptin and resistance downstream (SOCS3, PTP1B, hypothalamic inflammation), so more signal does nothing; the leptin system defends mainly against low fat (falling leptin is a strong starvation signal), and is asymmetric. (2) GLP-1 agonists act on a different input (satiety, gastric emptying, reward circuits in the brainstem and hypothalamus) at pharmacological concentrations, which overrides the defended level; weight returns when they are stopped, which suggests that the regulated level is shifted while the drug is present rather than reset. (3) Tests of a set point: perturbation experiments (overfeeding and underfeeding with measurement of adaptive changes in energy expenditure and appetite, as in the Minnesota and Vermont studies, and in "Biggest Loser" follow-ups); parabiosis and fat transplantation in rodents; time course of recovery after perturbation (a set point predicts return to the same value, a "settling point" model depends on environment); genetic studies of MC4R and other pathway genes. A good answer distinguishes a set point (active regulation to a target) from a settling point (passive equilibrium of intake and expenditure) and argues that the data support asymmetric regulation.
