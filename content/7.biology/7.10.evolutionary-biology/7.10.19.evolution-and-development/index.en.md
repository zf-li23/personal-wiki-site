---
title: "Evolution and Development: The Genetic Basis of Phenotypic Change"
description: "The evolutionary genetics of development: cis-regulatory and trans-regulatory change and how to tell them apart in hybrids; gain, loss and origin of enhancers (Drosophila wing spots and leg trichomes, transposon-derived enhancers); evolution of transcription factors (ftz); the domestication of maize (tb1, tga1); the loci of evolution and the role of pleiotropy; evolvability, modularity and phenotypic integration; robustness and cryptic genetic variation; developmental constraints and Fisher's geometric model; whether phenotypic plasticity leads evolution."
---

Darwin quoted Karl Ernst von Baer, who could not tell whether two unlabeled embryos in his collection were lizards, birds or mammals. The similarities of embryos and the shared developmental programs of different body parts and of the two sexes were among the strongest evidence for common descent, and they raise a question that population genetics alone does not answer: how does a change in DNA sequence become a change in form? Development is the proximate cause of a phenotype, the mechanism within the individual; natural selection and drift are its ultimate causes, acting on populations over generations ([7.10.1](/7.10.1)). The two explanations complement each other. Webbing between the digits is removed by programmed cell death in chickens and humans but kept in ducks; developmental biology explains how the difference arises, selection for swimming why ducks have it.

The developmental side of this subject is in [7.5.39](/7.5.39): von Baer's laws and the **phylotypic stage**, **modularity**, **co-option**, the conserved toolkit enlarged by duplication, **deep homology**, **heterochrony** and the other modes of developmental change, the case studies of stickleback pelves, insect germ bands, butterfly eyespots and limbs, **developmental constraints** and **genetic assimilation**. This chapter takes the view of evolutionary genetics. Which mutations change development, and where in the gene do they lie? Why are some kinds of mutation used more than others? How does the structure of development make some traits more evolvable than others, and what limits adaptation? And does the environment, through plasticity, lead the way? The quantitative-genetic background is in [7.10.9](/7.10.9); the evolution of genes and genomes, including the evolution of gene expression, in [7.10.18](/7.10.18).

## 19.1. Genes, Enhancers and Regulatory Change

### 19.1.1. The Regulatory Architecture of a Gene

Transcription of a eukaryotic gene by RNA polymerase II starts at its promoter, but where and when it happens is decided by enhancers, short stretches of DNA, often many kilobases away, bound by combinations of transcription factors ([7.2.14](/7.2.14)). A gene usually has several enhancers, each driving expression in particular cells at particular times. An enhancer is a **cis-acting element**: it regulates only the gene on the same DNA molecule. A transcription factor is a *trans*-acting product: encoded elsewhere, it acts on every gene whose enhancers it binds. Developmental genes form **gene regulatory networks** in which transcription factors regulate each other and their targets ([7.5.15](/7.5.15)).

Already in 1975, Mary-Claire King and Allan Wilson argued, from the near identity of human and chimpanzee proteins, that most of the morphological differences between the two species must be due to changes in gene regulation rather than in proteins. Methods of developmental genetics now make the hypothesis testable: transgenic reporter constructs that place an enhancer in front of a gene for a visible protein (β-galactosidase, GFP) show what the enhancer does; in situ hybridization and antibody staining show where a gene is expressed; RNA interference and CRISPR–Cas mutagenesis remove a gene's function in nonmodel species.

**Definition 19.1.1 (Cis-Regulatory Evolution)** **Cis-regulatory evolution** is evolutionary change in the expression of a gene caused by mutations in its own regulatory sequences (enhancers, promoters, silencers), as distinct from changes caused by mutations in *trans*-acting factors that regulate it, and from changes in the protein that it encodes.

### 19.1.2. Telling Cis from Trans

Suppose that a gene is expressed more strongly in species 1 than in species 2. The difference may lie in the gene's own enhancers or in the transcription factors that act on them. Wittkopp, Haerum and Clark (2004) separated the two in hybrids: in an F1 hybrid both alleles share the same nucleus, and hence the same *trans* environment, so any difference between the expression of the two alleles within the hybrid must be due to *cis* differences.

**Formula 19.1.1 (Cis and Trans Components of an Expression Difference)** Let $P = \log_2(E_1/E_2)$ be the ratio of expression of a gene in the two parental species and $H = \log_2(A_1/A_2)$ the ratio of the expression of the two alleles within F1 hybrids, measured by allele-specific sequencing. If *cis* and *trans* effects combine additively on the log scale,

$$
\text{cis} = H, \qquad \text{trans} = P - H.
$$

**Proof** In each parent, expression is the product of a *cis* factor of its allele and a *trans* factor of its genome, $E_k = c_k t_k$, so $P = \log_2(c_1/c_2) + \log_2(t_1/t_2)$. In the hybrid both alleles experience the same *trans* environment $t_{\mathrm{H}}$, so $A_1/A_2 = c_1 t_{\mathrm{H}}/(c_2 t_{\mathrm{H}}) = c_1/c_2$ and $H$ is the *cis* term. The remainder $P - H$ is the *trans* term. $\square$

Genes with purely *cis* differences lie on the diagonal $H = P$ of a plot of $H$ against $P$, purely *trans* differences on the horizontal axis $H = 0$. Genome-wide studies in *Drosophila*, yeast and mice find both kinds; *cis* differences account for a larger share of expression divergence between species than within species, where *trans* variation predominates. A plausible explanation is pleiotropy: a *trans* mutation affects many targets and is more often harmful, while a *cis* mutation affects one gene, so *cis* changes are more often fixed over long periods.

![Separating cis from trans effects with allele-specific expression in hybrids (Formula 19.1.1; simulated data). A: in each parent, expression of a gene depends on its own enhancer (cis) and on the transcription factors of its genome (trans); in the F1 hybrid the two alleles share one trans environment, so the ratio of their expression measures the cis difference alone. B: simulated genes plotted as hybrid allelic ratio H against parental ratio P (both log₂). Genes with only cis differences (blue) lie on the diagonal, genes with only trans differences (orange) on the horizontal axis, and genes with both (grey) between them.](./plots/cis-trans.py)

## 19.2. Cis-Regulatory Change

### 19.2.1. Losing and Gaining Enhancers

Because a gene's enhancers are modular, deleting one of them removes expression in one tissue and leaves the gene's other functions intact. The repeated reduction of the pelvis in freshwater sticklebacks by deletion of a pelvic enhancer of *Pitx1* is the textbook case ([7.5.39](/7.5.39#sec-39.5.1)). In humans, deletion of an enhancer of the androgen receptor gene removed its expression in the developing penis, and with it the small keratinized penile spines that chimpanzees and many other mammals have.

New expression domains can arise from small changes in an existing enhancer. *Drosophila guttifera* has a pattern of dark spots on its wings at the sites where the signaling gene *wingless* is expressed in the pupal wing, including around sensory structures and at the tips of veins; when a short regulatory fragment of the *D. guttifera* *wingless* gene is introduced into *D. melanogaster*, the spotted pattern of expression appears. Because the fragment differs only slightly between the species, a few mutations in one enhancer evidently created the new pattern.

### 19.2.2. A Novel Wing Spot

The males of *Drosophila biarmipes* have a dark spot near the tip of the wing, which they display during courtship. Pigmentation in *Drosophila* depends on genes for enzymes of melanin synthesis, among them *yellow*, which promotes black melanin. In *D. biarmipes*, an enhancer of *yellow* has acquired binding sites that make it respond to the transcription factor Distal-less, so *yellow* is expressed where Distal-less is; in a further step, Distal-less itself evolved a new, stronger expression in the region of the spot. The wing spot thus combines a *cis*-regulatory change in *yellow* with a change in the regulation of the *trans*-acting factor, an instance of the co-option of an existing factor (Distal-less, with older roles in appendage development) into a new network.

![Evolution of a wing spot in *Drosophila* by cis- and trans-regulatory change (after Futuyma and Kirkpatrick 2017, Fig. 15.17). Top: wings of an ancestral-type species without a spot, of intermediate species and of *D. biarmipes*. Bottom: the *yellow* gene and its wing enhancer. Ancestral: the enhancer does not bind Distal-less (Dll), and *yellow* is expressed uniformly at a low level. Co-option: mutations in the enhancer create Dll binding sites (orange), so *yellow* is expressed more strongly (brown shading) where Dll (orange dots) is present. Diversification: Dll itself evolves increased expression in one region of the wing, producing a concentrated patch of *yellow* expression and a dark spot.](./plots/wing-spot.py)

### 19.2.3. Where Enhancers Come From

New enhancers arise de novo by mutation of previously nonfunctional sequence, by duplication and divergence of existing enhancers, and, strikingly, from transposable elements, which carry their own binding sites for host transcription factors. In placental mammals, the cells of the endometrial stroma that support pregnancy express the hormone prolactin in response to cAMP. The cAMP-responsive enhancer of the prolactin gene in these cells is derived from a DNA transposon, MER20, and MER20-related sequences lie near hundreds of genes expressed in these cells and bind several transcription factors important in pregnancy. A family of selfish elements that spread through an ancestral mammalian genome thus supplied regulatory elements for a new tissue ([7.10.18](/7.10.18#sec-18.8.2)).

### 19.2.4. A Hox Gene as Micromanager

Hox genes specify the identities of whole body regions ([7.5.15](/7.5.15)), but they also act late in development on small details, and changes in their late expression contribute to fine-scale differences between species. In the pupal second leg of *Drosophila*, *Ultrabithorax* (*Ubx*) is expressed in a gradient on the femur, highest at its base, and represses the formation of fine hairs (trichomes): *D. melanogaster* has a small hairless ("naked") patch where *Ubx* is highest. Raising or lowering *Ubx* expression enlarges or shrinks the patch. *D. virilis*, with lower *Ubx* expression in the femur, has no naked patch; *D. simulans* has a larger one. Genetic analysis of hybrids between *D. simulans* and *D. melanogaster* showed that the *Ubx* locus contributes much of the difference, although the protein-coding sequences of *Ubx* are identical in the two species: the difference lies in the regulation of *Ubx*. In water striders, *Ubx* expression controls the length of the elongated middle legs with which the insects row on the water surface. A gene that decides whether a segment bears wings or halteres is also used to adjust leg hairs and leg proportions.

## 19.3. Trans-Regulatory and Coding Change

Transcription factors evolve too. The Hox protein Ubx of insects acquired a stretch of alanines that lets it repress the leg gene *Distal-less* in the abdomen, a change in the protein, not in its expression ([7.5.39](/7.5.39#sec-39.4.4)). The gene *fushi tarazu* (*ftz*) shows that a factor can change its role completely. *ftz* lies in the Hox cluster and in grasshoppers it still behaves as a homeotic gene, helping to specify segment identity through a short motif, YPWM, that binds the cofactor Extradenticle. In the ancestor of beetles and flies, Ftz gained a second motif, LXXLL, that binds the nuclear receptor Ftz-F1, and acquired a role in segmentation; in the lineage leading to *Drosophila*, YPWM was lost, so that *Drosophila* Ftz is a pair-rule segmentation gene with no homeotic function. Restoring the YPWM motif to *Drosophila* Ftz, or replacing it with the beetle gene, partly or completely transforms the antenna of a fly into a leg.

The DNA-binding domains of transcription factors such as the **homeobox** are among the most conserved sequences known, but the motifs by which they interact with other proteins can change, so networks evolve by new combinations of factor modules and enhancer modules. Changes in where a factor is expressed are a third route: most plants of the potato family (Solanaceae) express a MADS-box gene of the *STMADS16* group (*MPF2* in *Physalis*) only in vegetative tissues, but in the ground cherries (*Physalis*) it is expressed in the sepals after pollination, which grow into the inflated "lantern" that envelops the fruit, a **heterotopy** of expression.

## 19.4. The Domestication of Maize

The transformation of teosinte into maize by early farmers in Mexico is one of the best-understood cases of rapid morphological evolution. The two plants look so different that the identity of maize's wild ancestor was long disputed. Teosinte has many lateral branches, each tipped with a male tassel, and small ears of 5 to 12 kernels, each enclosed in a hard fruit case, that shatter at maturity; maize has a single main stem with a tassel at its tip, short lateral branches ending in ears, and ears with up to 500 exposed kernels that stay attached, so that maize cannot persist without people to shell and sow it. In the 1930s George Beadle and Ralph Emerson showed that maize and the annual teosinte *Zea mays* ssp. *mexicana* have chromosomes that look alike and form fully fertile hybrids. Molecular data identify the Balsas teosinte, *Z. mays* ssp. *parviglumis* of southwestern Mexico, as the closest wild relative, and indicate a single domestication about 9000 years ago, in agreement with archaeology.

**Example 19.4.1 (Beadle's Estimate of the Number of Genes)** Beadle grew about 50 000 F2 plants from a maize × teosinte cross and found that about 1 in 500 resembled maize and about 1 in 500 resembled teosinte. If the difference were due to $n$ unlinked loci, each with two alleles of equal frequency in the F2, a plant would resemble one parent only if it were homozygous for that parent's allele at all loci, which happens with probability $(1/4)^n$. Then $(1/4)^n = 1/500$ gives $n = \ln 500/\ln 4 \approx 4.5$: the differences are due mainly to four or five loci of large effect. The estimate is crude, since it ignores dominance, epistasis, linkage and loci of small effect, but it agreed well with later **QTL** mapping, which found six chromosomal regions with large effects on five of the ten chromosomes.

![Beadle's estimate of the number of genes that distinguish maize from teosinte (Example 19.4.1). Expected number of F2 plants out of 50 000 that resemble one parent, 50 000 · (1/4)ⁿ, for n = 1 to 8 independent loci (bars), compared with the observed number, about 100 (1 in 500; dashed line). The observation lies between n = 4 and n = 5. Inset: plant architecture of teosinte (many long lateral branches with tassels) and maize (one main stem, short lateral branches ending in ears); the difference is due mainly to *tb1*.](./plots/maize-beadle.py)

:::

One of the QTL regions, on chromosome 1, controls branching, with the teosinte state (many long branches) recessive. A recessive maize mutant, *teosinte branched1* (*tb1*), which branches like teosinte, maps to the same interval, and a **complementation test** showed that the QTL and the mutant are the same gene: plants with an otherwise maize genome but the teosinte version of the region branch like teosinte, and crossed with *tb1* mutants they still produce branched progeny. *tb1* encodes a transcription factor of the TCP family that represses the growth of the organs in which it is expressed, the axillary buds and lateral branches. The maize and teosinte proteins have no consistent amino acid differences, but the maize allele is expressed about twice as strongly in lateral branches, and the region upstream of the gene has little nucleotide variation in maize and much more in teosinte, the signature of a **selective sweep** on a regulatory variant ([7.10.8](/7.10.8#sec-8.3)). The causal variant turned out to be an insertion of a transposable element (*Hopscotch*) about 60 kb upstream of *tb1*, which enhances its expression; the insertion is older than domestication and segregates in wild teosinte, so the farmers selected **standing genetic variation**. Ancient DNA from maize cobs up to about 4400 years old already carries the maize *tb1* allele, while selection on a starch-debranching enzyme gene, *su1*, which affects the texture of the kernels, was still going on about 2000 years ago.

The hard fruit case of teosinte maps to another gene, *teosinte glume architecture1* (*tga1*), which encodes a transcription factor of the SBP family; here the change selected during domestication is a single amino acid substitution in the protein. Other traits, such as the shattering of the ear, are polygenic. Domestication in maize thus combined *cis*-regulatory and coding changes in a few genes of large effect with selection on many loci of small effect, mostly from variation already present in teosinte.

## 19.5. The Loci of Evolution

Case studies accumulated over three decades allow some generalizations about which mutations underlie phenotypic evolution.

| Trait | Gene | Kind of change |
|---|---|---|
| Pelvic reduction in sticklebacks | *Pitx1* | *cis* (enhancer deletion) |
| Armor plates in sticklebacks | *Eda* | *cis* (regulatory alleles; standing variation) |
| Penile spines lost in humans | androgen receptor | *cis* (enhancer deletion) |
| Wing spots in *Drosophila* | *wingless*, *yellow* | *cis*, with *trans* change in Distal-less |
| Leg hairs (trichomes) in *Drosophila* | *Ubx* | *cis* |
| Beak depth in Darwin's finches | *Bmp4*, calmodulin | expression (regulatory) |
| Leg repression in insects | *Ubx* | coding (protein motif) |
| Branching of maize | *tb1* | *cis* (transposon insertion) |
| Fruit case of maize | *tga1* | coding (one amino acid) |
| Human-specific odor detection in *Aedes* | *Or4* | coding and expression ([7.10.18](/7.10.18#sec-18.5)) |
| Melanism in many vertebrates | *Mc1r* | coding (convergent) |

Two patterns stand out. First, changes in morphology often involve *cis*-regulatory mutations in transcription factors and signaling genes, whereas changes in physiology often involve changes in proteins. The reason is **pleiotropy** ([7.10.4](/7.10.4#sec-4.4.1)). A developmental regulator acts in many tissues and stages; a mutation in its coding sequence changes all of them, and most such changes are harmful, while a mutation in one of its modular enhancers changes only one. *Cis*-regulatory mutations are often additive (codominant) in their effects, which also makes them visible to selection when rare. Genome scans of sticklebacks adapting to fresh water, in which only about 17 % of the regions under selection involve coding changes ([7.10.18](/7.10.18#sec-18.5)), agree. Second, evolution often uses the same genes repeatedly: *Pitx1* and *Eda* in independent stickleback populations, *Mc1r* in melanism of birds, lizards and mammals, the pigmentation genes *yellow* and *ebony* in many *Drosophila* species. Such evolutionary hotspots are genes that occupy key positions in networks, input–output nodes where a change has a large, specific effect with few side effects.

These generalizations are tendencies, not laws. The case studies are biased toward conspicuous traits controlled by genes of large effect and toward changes easy to find; coding changes are easier to detect and were once overrepresented, *cis*-regulatory changes now are; and many traits are highly polygenic ([7.10.9](/7.10.9#sec-9.8)). Coding changes in transcription factors (Ubx, Ftz) also contribute to morphological novelty.

## 19.6. Evolvability and Developmental Pathways

### 19.6.1. Pleiotropy, Integration and Modularity

The **evolvability** of a trait, its capacity to evolve under selection, depends on its additive genetic variance, but also on its genetic correlations with other traits, summarized by the **G matrix** ([7.10.9](/7.10.9#sec-9.6)). A correlation can constrain a response, when selection favors a combination of traits against the correlation, or speed it, when selection favors the combination that the correlation produces: the upper and lower parts of a bird's bill usually need to change together, and evolve more easily if they are positively correlated. Paleontologists Everett Olson and Robert Miller called the stronger correlation of functionally related parts morphological (now phenotypic) integration; Raissa Berg found that floral structures are more strongly correlated with each other than with vegetative structures. Rupert Riedl and later Günter Wagner proposed that selection shapes genetic correlations, so that evolvability itself evolves.

Development provides the mechanisms. The mouse gene *Hoxd13* is required for both the digits and the external genitalia; one of its enhancers drives expression in both structures, while two others drive it in only one or the other, so that the pleiotropy of the gene is a property of particular enhancers and can change. A mutation at one locus can modify the effects of another on two traits (a relationship QTL): in the butterfly *Bicyclus anynana* an allele at one locus reduces eyespots on both wings or only on the hindwing, depending on the allele at a second locus. Selection for small spots on one wing only would favor such a modifier, and the two spots would become separately evolving characters, modules. Conversely, fore- and hindlimbs of quadrupedal monkeys, which are used similarly, are more strongly correlated in length than those of apes, which use their arms for climbing and swinging; the weaker integration of ape limbs may have made possible the independent evolution of the long arms of gibbons and the long legs of humans.

### 19.6.2. Robustness and Cryptic Genetic Variation

Development shows **robustness** to many mutations and environmental perturbations ([7.6.40](/7.6.40)); the property of producing a constant phenotype is **canalization** ([7.5.1](/7.5.1)). Robustness has a consequence for evolution.

**Definition 19.6.1 (Cryptic Genetic Variation)** **Cryptic genetic variation** is genetic variation that has no effect on the phenotype under the usual genetic background and environment, but affects it when development is perturbed, by an unusual environment, a new mutation or a change in genetic background.

Because it is invisible to selection, cryptic variation accumulates almost neutrally, and it is released when canalization is weakened. In Waddington's classic experiments, treating *Drosophila* embryos with ether produced a few adults with enlarged, wing-like halteres; selection on such flies over many generations increased the frequency and severity of the phenotype until it appeared without ether; later work traced much of the variation in this response to *Ubx*, whose functionally different alleles segregate, hidden, in natural populations. The heat-shock chaperone Hsp90, which buffers the folding of many signaling proteins, can act as a capacitor that hides such variation and releases it under stress ([7.6.40](/7.6.40#sec-40.5)). The mechanism of selection on the released variation is that of genetic assimilation ([Formula 39.7.1](/7.5.39#fml-39.7.1)).

Futuyma and Kirkpatrick distinguish environmental canalization, the buffering of the phenotype against environmental variation, from genetic canalization, its buffering against mutations. Stabilizing selection should favor environmental canalization: the flowers of animal-pollinated plants, which must fit their pollinators, are less variable than their leaves. Genetic canalization is less likely to evolve by selection, because selection against deleterious mutations already keeps most individuals near the optimum, leaving little selection on modifiers that would hide the mutations; much genetic robustness may instead be a by-product of environmental robustness or of the structure of networks.

## 19.7. Constraints on Adaptive Evolution

### 19.7.1. Developmental and Genetic Constraints

Many imaginable organisms do not exist: no tetrapod has a third digit that is the shortest, no animal photosynthesizes on its own. A **developmental constraint** is a bias in the production of variant phenotypes caused by the structure of the developmental system ([Definition 39.6.1](/7.5.39#def-39.6.1)); it acts either through a lack of variation in some directions or through strong correlations among traits caused by pleiotropy, and so is a form of genetic constraint (**evolutionary constraint**, [Definition 9.6.3](/7.10.9#def-9.6.3)). When Pere Alberch and Emily Gale blocked cell division in developing limb buds with colchicine, frogs (*Xenopus*) lost their preaxial (front) digits and salamanders (*Ambystoma*) their postaxial (rear) digits, the last digits to form in each group; the same digits have been lost repeatedly in the evolution of each group. Almost all mammals, from giraffes to whales, have seven cervical vertebrae, unlike birds and reptiles; in human fetuses and infants, homeotic transformations of the cervical vertebrae are associated with malformations of other organs, and such pleiotropic costs may have kept the number fixed.

### 19.7.2. Fisher's Geometric Model

Ronald Fisher (1930) gave a simple argument for why adaptation proceeds by small steps, which has become a basic model of the genetics of adaptation.

**Definition 19.7.1 (Fisher's Geometric Model)** In **Fisher's geometric model**, a phenotype is a point $\boldsymbol{z}$ in an $n$-dimensional space of traits, fitness decreases with the distance $d = \lVert\boldsymbol{z} - \boldsymbol{z}^*\rVert$ from an optimum $\boldsymbol{z}^*$, and a mutation displaces the phenotype by a vector of length $r$ in a direction uniformly distributed on the sphere, independently of the position of the optimum. The number $n$ of independent dimensions under selection measures the organism's complexity.

**Formula 19.7.1 (Probability That a Mutation Is Beneficial)** A mutation of size $r$ is beneficial if and only if $U > r/(2d)$, where $U$ is the component, in the direction of the optimum, of a random unit vector in $\mathbb{R}^n$. For $n = 3$, $U$ is uniform on $[-1, 1]$ and

$$
P_{\mathrm{ben}} = \tfrac12\bigl(1 - \tfrac{r}{2d}\bigr) \quad (r \le 2d);
$$
for large $n$, $\sqrt{n}\,U$ is approximately standard normal and

$$
P_{\mathrm{ben}} \approx 1 - \Phi(x), \qquad x = \frac{r\sqrt{n}}{2d},
$$
where $\Phi$ is the standard normal distribution function.

**Proof** Put the optimum at the origin and let $\boldsymbol{u}$ be the unit direction of the mutation. The new distance satisfies $\lVert\boldsymbol{z} + r\boldsymbol{u}\rVert^2 = d^2 + r^2 + 2r\,\boldsymbol{z}\cdot\boldsymbol{u}$, which is smaller than $d^2$ if and only if $-\boldsymbol{z}\cdot\boldsymbol{u}/d > r/(2d)$; the left side is the component $U$ of $\boldsymbol{u}$ along the direction from $\boldsymbol{z}$ to the optimum. For $n = 3$, by Archimedes' theorem on the sphere, $U$ is uniform on $[-1, 1]$. For general $n$, $\boldsymbol{u} = \boldsymbol{g}/\lVert\boldsymbol{g}\rVert$ with $\boldsymbol{g}$ standard normal in $\mathbb{R}^n$; $\lVert\boldsymbol{g}\rVert/\sqrt{n} \to 1$ by the law of large numbers, so $\sqrt{n}\,U \approx g_1$ is approximately standard normal. $\square$

Very small mutations are beneficial with probability close to $1/2$, and the probability falls steeply with size, the more steeply the more dimensions there are: in a complex organism, a random large change is almost certain to make things worse. Fisher concluded that adaptation is built from mutations of small effect. Kimura (1983) noted that small beneficial mutations have small selection coefficients and are therefore usually lost by drift (fixation probability about $2s$, Theorem 6.3.1), so the mutations most likely to contribute to adaptation are of intermediate size, $x$ of order 1. Orr (1998, 2000) followed the model through a whole adaptive walk: the sizes of the substitutions fixed during adaptation to a new optimum are roughly exponentially distributed, a few of large effect early and many of small effect later, in accord with QTL studies such as those of maize; and the rate of adaptation falls with $n$, a "cost of complexity". As Barton and colleagues note, the argument is not decisive for real organisms, because the effective number of dimensions affected by a mutation may be small: modularity, which confines a mutation's effects to one part of the organism, reduces the effective $n$ and so raises evolvability.

![Fisher's geometric model (Definition 19.7.1). A: probability that a random mutation of size r is beneficial, against x = r√n/(2d), for n = 3, 10 and 50 dimensions; points are Monte Carlo estimates (20 000 mutations each), the line is the large-n approximation 1 − Φ(x), the dashed line the exact result for n = 3, (1 − r/2d)/2 (Formula 19.7.1). B: relative contribution of mutations of size x to adaptation, the expected selection coefficient of beneficial mutations, weighted by their fixation probability 2s (Gaussian fitness, n = 50; simulation): small mutations are often beneficial but have small effects and are often lost, large mutations are rarely beneficial, and intermediate ones contribute most.](./plots/fisher-geometric.py)

## 19.8. Phenotypic Plasticity and Evolution

### 19.8.1. Plasticity, Canalization and Genetic Assimilation

The evolution of reaction norms and of adaptive **phenotypic plasticity** is treated in [7.10.9](/7.10.9#sec-9.7): when the reaction norms of genotypes differ in slope (**genotype–environment interaction**), selection can change the mean plasticity, and the optimal slope depends on how reliably a cue predicts the environment of selection. Plastic responses range from rapidly reversible changes of physiology and behavior to developmental switches: caterpillars of the moth *Nemoria arizonaria* that hatch in spring resemble the oak catkins they eat, those that hatch in summer resemble twigs; leaves of the water crowfoot *Ranunculus aquatilis* are finely divided under water and broad in air. Plastic changes are themselves the product of gene regulation: environmental signals change hormone levels, which change the activity of transcription factors and their targets. Where a constant phenotype is best, selection favors canalization of the reaction norm instead.

### 19.8.2. Does Plasticity Lead Evolution?

In the standard view, reaction norms evolve by selection on mutations that alter the expression of a trait in different environments. Mary Jane West-Eberhard and others proposed a different order of events, "plasticity first": a new environment induces the prevalent genotype to produce a new, roughly adaptive phenotype by plasticity; selection on genetic variation in the response then refines it (genetic accommodation) and may make it constitutive (genetic assimilation, demonstrated in the laboratory by Waddington and, for the color of *Manduca* caterpillars, by Suzuki and Nijhout; [7.5.39](/7.5.39#sec-39.7)). Plasticity would then determine which variants are exposed to selection and guide the direction of evolution.

Some comparisons fit the hypothesis. Tadpoles of spadefoot toads (*Spea*) switch, when they eat shrimp, to a carnivorous form with a shorter gut and larger jaw muscles ([7.10.9](/7.10.9#sec-9.7)). Tadpoles of the related genus *Scaphiopus*, which normally eat only detritus, also develop a shorter gut when raised on shrimp, as if the plastic response was present in the common ancestor. But they develop smaller, not larger, jaw muscles. A plastic response to a new environment may be adaptive, neutral or maladaptive: many responses to stress, such as slower growth at low temperatures, are simply unavoidable consequences of physiology. Then selection favors genetic changes that oppose the plastic effect: tadpoles of the green frog (*Rana clamitans*) from cold mountain sites grow faster at low temperatures than those from warm lowlands, compensating for the slowing effect of cold (countergradient variation). How often plasticity leads adaptive evolution rather than following or opposing it is unresolved; plasticity may as easily slow genetic adaptation, by shielding genotypes from selection, as speed it.

![Plasticity may help, barely help or hinder adaptation to a new environment (after Futuyma and Kirkpatrick 2017, Fig. 15.28). Reaction norms of three genotypes, A, B and C, which all produce the phenotype that is optimal in environment 1 (star). When the population moves to environment 2, genotype A's plastic response brings it to the new optimum (triangle), genotype B's moves it only a little in the right direction, and genotype C's moves it away from the optimum, so that C would have been better off with no plasticity. Shaded curves: fitness functions in the two environments.](./plots/plasticity-direction.py)

## Summary

| Question | Answer | Key items |
|---|---|---|
| Where do mutations that change development lie? | in enhancers (*cis*), in transcription factors and signals (*trans*), in coding sequences | **cis-regulatory evolution** (Definition 19.1.1); Formula 19.1.1 separates *cis* from *trans* in hybrids |
| How do new expression patterns arise? | deletion, mutation, duplication and transposon origin of enhancers; co-option of factors | *Pitx1*, androgen receptor, *wingless* and *yellow* wing spots, MER20, *Ubx* leg hairs |
| Do transcription factors change? | yes, mostly in protein-interaction motifs, rarely in DNA-binding domains | Ubx poly-alanine, Ftz (YPWM lost, LXXLL gained), *Physalis* MPF2 |
| What happened in maize? | a few large-effect genes plus many small ones, mostly from standing variation | Example 19.4.1 ($n \approx 4.5$), *tb1* (*cis*, transposon), *tga1* (one amino acid) |
| Why so many *cis* changes in morphology? | modular enhancers avoid the pleiotropy of coding changes | evolutionary hotspots: *Pitx1*, *Eda*, *Mc1r*, *yellow* |
| What shapes evolvability? | genetic correlations, modularity, robustness | *Hoxd13* enhancers, relationship QTL, primate limbs; **cryptic genetic variation** (Definition 19.6.1) |
| What limits adaptation? | developmental bias, pleiotropy, complexity | Alberch and Gale, cervical vertebrae, **Fisher's geometric model** (Definition 19.7.1, Formula 19.7.1) |
| Does plasticity lead? | sometimes; plastic responses may also be maladaptive | genetic accommodation, *Spea* and *Scaphiopus*, countergradient variation |

## Questions

1. In an F1 hybrid between two *Drosophila* species, a gene is expressed 4 times more strongly in species 1 than in species 2, and within the hybrid the species-1 allele is expressed 2 times more strongly than the species-2 allele. Partition the difference into *cis* and *trans* components.

   **Answer** $P = \log_2 4 = 2$ and $H = \log_2 2 = 1$. By Formula 19.1.1, $\text{cis} = 1$ and $\text{trans} = 2 - 1 = 1$: a twofold difference is due to the gene's own regulatory sequences and another twofold difference, in the same direction, to *trans*-acting factors.

2. Why might *cis*-regulatory mutations contribute more to the evolution of morphology than mutations in the coding sequences of developmental regulators? Give one reason why this generalization may be exaggerated.

   **Answer** Developmental regulators act in many tissues and stages; a coding mutation changes the protein everywhere and so has many, mostly harmful, pleiotropic effects, while a mutation in one modular enhancer changes expression in one place only; *cis* mutations also tend to act additively, so selection sees them in heterozygotes. The generalization may be exaggerated because case studies are biased toward conspicuous traits and large-effect loci, because changes in noncoding DNA are now searched for preferentially, and because coding changes in protein-interaction motifs of transcription factors (Ubx, Ftz) have also produced morphological novelties.

3. In Fisher's geometric model with $n = 3$, what fraction of mutations of size $r = d$ (equal to the distance from the optimum) are beneficial? What is the approximate fraction in a model with $n = 25$ dimensions?

   **Answer** For $n = 3$, $P_{\mathrm{ben}} = \frac12(1 - \frac12) = \frac14$. For $n = 25$, $x = r\sqrt{n}/(2d) = 5/2 = 2.5$ and $P_{\mathrm{ben}} \approx 1 - \Phi(2.5) \approx 0.006$. In the more complex organism, a mutation of the same size is beneficial forty times less often.

4. How did geneticists show that *tb1* is the gene responsible for the maize branching QTL, and what evidence indicates that its change was regulatory and was selected?

   **Answer** The QTL and a recessive maize mutant with teosinte-like branching mapped to the same interval of chromosome 1, and in a complementation test plants carrying the teosinte version of the region, crossed with *tb1* mutants, gave branched progeny: the teosinte QTL allele failed to complement the mutation, so they are alleles of one gene. The protein shows no consistent amino acid differences between maize and teosinte, while the maize allele is expressed about twice as strongly in lateral branches; the upstream regulatory region has very low nucleotide diversity in maize compared with teosinte, the signature of a selective sweep; the causal variant is a transposon insertion upstream that increases expression.

5. Waddington's selection on ether-induced bithorax-like flies eventually produced the phenotype without ether. Explain this result without invoking the inheritance of acquired characteristics, and say what it reveals about natural populations.

   **Answer** The population carried genetic variation in the liability to develop enlarged halteres (here largely at *Ubx*), which was hidden under normal conditions because the phenotype appears only above a threshold. Ether pushed some genotypes over the threshold; breeding from them selected alleles that raise liability, and after enough generations some genotypes exceeded the threshold without ether. The result shows that natural populations harbor cryptic genetic variation that canalization hides and that perturbations can expose to selection.
