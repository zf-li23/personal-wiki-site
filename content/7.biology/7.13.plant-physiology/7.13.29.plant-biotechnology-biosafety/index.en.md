---
title: Plant Biotechnology and Biosafety
description: Applications of plant tissue culture (rapid propagation, virus elimination, haploid breeding, germplasm conservation); the development of crop-improvement technologies (conventional breeding, mutagenesis, molecular markers, transgenesis, genome editing); the physiology of released traits (insect resistance, herbicide tolerance, virus resistance, quality improvement); principles of biosafety assessment (substantial equivalence, case-by-case analysis, step-by-step evaluation) and regulatory frameworks; and a population-genetic model of resistance management with refuges
source_hash: 0ba6333ea94a
---

The preceding chapters described how plants grow, develop, and respond to their environment; this chapter asks how people use that knowledge to modify plants. The totipotency of plant cells allows a small piece of tissue to regenerate a whole plant, and this is the starting point of plant biotechnology: it underlies rapid propagation and virus elimination, and it is equally the common basis of haploid breeding, germplasm conservation, and genetic transformation. On this foundation, crop improvement has passed through successive stages, from selection, crossing, and mutagenesis to molecular markers, transgenesis, and genome editing. The transgenic traits that are grown on a large scale are mainly insect resistance, herbicide tolerance, virus resistance, and quality improvement. Each works because of a clear physiological basis, and each also raises new questions: whether such crops are safe for people and the environment, how they should be assessed and regulated, and whether insect resistance will fail as pests evolve.

We discuss, in turn, applications of plant tissue culture (Section 29.1), the development of crop-improvement technologies (Section 29.2), the physiology of released traits (Section 29.3), the principles and regulatory frameworks of biosafety assessment (Section 29.4), and resistance management (Section 29.5). The chapter deals with concepts and principles only, not with laboratory procedures. Its boundaries with other chapters are as follows: the physiological basis of tissue culture (totipotency, the auxin-to-cytokinin ratio, regeneration pathways) is in [7.13.18](/7.13.18#sec-18.9); artificial propagation of vegetative organs and the definition of micropropagation are in [7.12.24](/7.12.24#sec-24.7.4); the overall course of crop domestication and breeding 1.0–4.0 is in [7.13.28](/7.13.28#sec-28.10); the general theory of the evolution of resistance is in [7.10.34](/7.10.34#sec-34.4.2); and the molecular principles of transgenesis and genome editing are treated in the chapters on molecular biology and genetics.

## 29.1. Applications of Plant Tissue Culture

In plant tissue culture ([7.12.24](/7.12.24#sec-24.7.4)), explants are placed on sterile artificial medium, and the ratio of auxin to cytokinin directs proliferation and differentiation ([7.13.18](/7.13.18#sec-18.9)). Regeneration follows one of two routes: organogenesis (adventitious shoots and roots formed from callus or directly) and somatic embryogenesis. This section discusses four classes of applications.

### 29.1.1. Rapid Propagation

Micropropagation has a multiplication rate that is independent of site and season. Suppose that in each subculture cycle every culture multiplies on average into $m$ divisible shoots, and that there are $n$ cycles. The number of plantlets obtained from one explant is then

$$
N_n = N_0\, m^{\,n}. \tag{29.1}
$$

**Example 29.1.1** A cultivar is subcultured every 4 weeks, and each culture vessel is divided on average into 3 new cultures each time. A year has about 13 cycles, so $N_{13} = 3^{13} \approx 1.6 \times 10^6$. In practice, contamination, vitrification, and a multiplication rate that declines with the number of subcultures, together with the fact that only a fraction of cultures proceed to rooting and acclimatization, make the number of plants obtained much lower than the theoretical value of Eq. (29.1). It is still several orders of magnitude higher than that obtained by cuttings or division.

:::

Micropropagation is suited to several kinds of material: heterozygous material that cannot be propagated by seed (banana, many ornamentals and fruit-tree rootstocks); species with tiny seeds that germinate poorly (orchids); cultivars whose clonal uniformity must be maintained; and forest trees, for which producing planting stock is much faster than field propagation. Its costs are equipment and labor, and the negative consequence of clonal uniformity: the genetic base is narrow, so that when a new disease appears the whole clone is susceptible ([7.13.25](/7.13.25#sec-25.7)).

Long-term subculture may also produce somaclonal variation: chromosomal rearrangements, transposon activation, and epigenetic changes during culture make regenerated plants not quite identical to the parent. In rapid propagation this is a defect to be avoided (so subculture should not continue indefinitely, and excessively strong growth regulators should be avoided), but in breeding it has been used as a source of variation: disease-resistant and salt-tolerant lines selected from somaclonal variants are a form of breeding that does not involve crossing.

### 29.1.2. Virus Elimination

Viruses spread within the plant through the vascular tissue and plasmodesmata ([7.13.25](/7.13.25#sec-25.6)). The shoot apical meristem has no mature vascular tissue and its cells divide rapidly, so viral replication and movement cannot keep pace, and the very tip is often virus-free. If such a small shoot tip is cultured into a plantlet and tested to confirm the absence of virus, a virus-free plant is obtained. The method is especially useful for vegetatively propagated crops: in potato, sweet potato, strawberry, garlic, and many fruit trees, viruses accumulate generation after generation through tubers, storage roots, and cuttings, so yield and quality decline year by year, and replacing the planting stock with virus-free material often gives a marked increase in yield.

Virus elimination only makes the plant virus-free for the time being; it does not confer resistance. Plants in the field are infected again by insect vectors, so virus-free stock is usually multiplied for several generations under isolation, and in production it must be renewed regularly. Shoot-tip culture is sometimes combined with heat treatment (higher temperature suppresses viral replication) or chemical treatment, which allows larger shoot tips to be used. The underlying fact is the uneven distribution of viruses in the plant body, which is linked to RNA silencing and plasmodesmatal transport in 7.13.25: silencing is active in the meristem and viral movement is restricted.

### 29.1.3. Haploid Breeding

Under suitable conditions, anthers or microspores can change their developmental fate without fertilization and form haploid embryoids or callus, from which haploid plants regenerate. Haploid plants are sterile, but chromosome doubling yields fully homozygous doubled haploids (DH). A pure line is thus obtained in one generation, whereas in conventional breeding heterozygosity is halved in each generation of selfing:

$$
H_n = H_0\left(\tfrac{1}{2}\right)^{n}, \tag{29.2}
$$

After 6 generations of selfing, $1/64 \approx 1.6\%$ of loci are still heterozygous. A single anther culture from a hybrid progeny therefore has the effect of several generations of selfing and shortens the breeding period by about half; recessive traits are expressed directly in haploids, which facilitates selection. Doubled haploids are also basic material for genetic mapping populations and for breeding. In China, anther-culture cultivars of wheat, rice, rapeseed, and tobacco were widely released after the 1970s. The efficiency of anther culture varies greatly with genotype, and many *indica* rice lines and some legumes are difficult to induce; in maize and other crops, crossing with inducer lines that trigger maternal haploids has replaced anther culture as the main way to produce doubled haploids on a large scale (the genetics of haploids and doubled haploids is in [7.4.16](/7.4.16)).

### 29.1.4. Germplasm Conservation

The genetic diversity of crops is the raw material of breeding ([7.13.28](/7.13.28#sec-28.9)). Species whose seeds can be stored dry (orthodox seeds) can be conserved in low-temperature gene banks. Two kinds of material cannot be handled this way: vegetatively propagated crops (potato, sweet potato, banana, cassava) and species whose seeds are sensitive to desiccation (cacao, rubber, mango, many tropical fruit trees; these have recalcitrant seeds). Three options exist for them. Field gene banks are costly and vulnerable to pests, diseases, and natural disasters. In vitro conservation keeps sterile cultures under low temperature, low light, or osmotic agents to restrict growth, with subculture at long intervals. Cryopreservation treats shoot tips or embryos with protectants, dehydrates them, and places them in liquid nitrogen (about $-196\,^\circ\mathrm{C}$), where metabolism almost completely stops and conservation is in principle indefinite. Regeneration ability and genetic stability after recovery are the criteria of evaluation. These three methods complement seed banks to form a conservation system.

## 29.2. Development of Crop-Improvement Technologies

The aim of crop improvement has always been to select, from variation, individuals that meet human needs and to make them heritable and stable; the stages differ only in where the variation comes from and on what selection is based. The overall framework of breeding 1.0–4.0 is in 7.13.28 ([7.13.28](/7.13.28#sec-28.10)); here we review it again by source of variation, with emphasis on the technologies between 3.0 and 4.0.

| Stage | Source of variation | Means of selection | Examples | Limitations |
|---|---|---|---|---|
| Domestication and selection | Natural variation | Phenotype; farmers save seed | Landraces | Limited variation, long cycle |
| Cross breeding | Recombination between parents; closely related species | Phenotype, pedigree, and statistical design | Hybrid maize, hybrid rice, semidwarf cultivars | Only genes of the same or closely related species; linkage drag; many generations of backcrossing for each trait |
| Mutation breeding | Random mutations induced by radiation or chemical mutagens | Phenotypic screening of large progeny | Mutant cultivars for disease resistance, early maturity, dwarfism | Mutations are random and mostly deleterious; large populations needed |
| Marker-assisted selection | As in crossing | DNA markers and genotype | Backcross introgression of the submergence-tolerance gene *Sub1* | The target trait must have a known marker |
| Transgenesis | Introduction of one or a few genes from any species | Screening for the introduced trait | Bt cotton, herbicide-tolerant soybean, virus-resistant papaya | Regulation and public acceptance; each event must be assessed separately |
| Genome editing | Deletions, base substitutions, or small insertions at specified sites in endogenous genes | Sequencing to verify the edit | Edited quality and disease-resistance traits | Off-target effects must be assessed; multiple loci may need editing when a trait is polygenic |

**Mutation breeding** uses ionizing radiation ($\gamma$ rays, X-rays, heavy-ion beams) or chemical mutagens (such as ethyl methanesulfonate) to produce random point mutations and deletions in DNA, and favorable variants are screened from a large progeny. Since the mid-twentieth century, thousands of mutant cultivars have been registered worldwide, in rice, wheat, barley, cotton, soybean, and many ornamentals. Its characteristic is that it generates new alleles without introducing foreign DNA, and it has therefore long been regarded as conventional breeding; its limitation is that mutations occur throughout the genome, and several generations of backcrossing are needed to remove unrelated mutations.

**Transgenic** breeding introduces genes from any species into a crop. It breaks the species barrier of sexual crossing and can add a single trait precisely without bringing in other genes of the donor parent, so that many generations of backcrossing are unnecessary; at the same time, the position at which a foreign gene inserts into the genome is random, so every transformation event is different and must be characterized and assessed one by one (Section 29.4). **Genome editing** uses sequence-specific nucleases (zinc-finger nucleases, transcription activator-like effector nucleases, and more recently **CRISPR–Cas9** and its derivatives, base editing and prime editing) to make changes at specified positions in endogenous genes, with the cell's own DNA repair machinery completing the change. Its products may be indistinguishable from natural mutations or those induced by mutagens, and the foreign DNA of the editing tools can be removed by segregation; its regulation is therefore discussed separately from that of transgenesis (Section 29.4.4). The molecular principles of both are treated in the chapters on genetics and molecular biology.

Whatever the technology, a transformed or edited crop must follow a common route to become a cultivar: regenerated plants carrying the trait are obtained; events with a single insertion site, genetic stability, and the expected performance are identified; the trait is introduced into the background of a leading cultivar through several generations of backcrossing; and only then come safety assessment and cultivar registration. The ability to regenerate and be transformed is the bottleneck for many crops (most cereals, legumes, and many forest trees), and it is directly tied to the physiology of tissue culture: expressing developmental regulators involved in cell division and meristem formation can raise the efficiency of regeneration and transformation of recalcitrant genotypes ([7.13.18](/7.13.18#sec-18.9)), which is currently one of the research priorities of plant biotechnology.

## 29.3. Physiology of Released Traits

The transgenic crops grown commercially on a large scale in the world are mainly soybean, maize, cotton, and canola, and the traits are concentrated in insect resistance and herbicide tolerance, which are often stacked in the same cultivar. This section discusses only the physiological basis of the traits in the plant and what they have, and have not, brought to crop performance.

### 29.3.1. Insect Resistance: Bt Toxins

*Bacillus thuringiensis* produces insecticidal crystal proteins (Cry proteins; also Vip proteins secreted during vegetative growth) when it sporulates. Expressing the genes for these proteins in a crop makes the plant synthesize its own insecticidal substance. The mechanism of action of Bt toxins on Lepidoptera, Coleoptera, and other insects is as follows. After ingestion, the crystal protein dissolves in the alkaline midgut (pH about 10 in lepidopteran larvae) and is cleaved by midgut proteases into active toxin fragments. These bind to specific receptors on the membranes of midgut epithelial cells, then oligomerize and insert into the membrane to form pores, which disrupt the ionic balance of the cells. The epithelial cells lyse, and the insect stops feeding and dies.

This mechanism explains two properties. The first is selectivity: the toxin acts only if a suitable receptor is present, and different Cry proteins target different groups of insects, whereas the mammalian stomach is strongly acidic (the toxin degrades there) and the intestinal epithelium has no receptor that binds the toxin, so acute toxicity to humans and livestock is very low. The second is a narrow target: it acts only on the target pests that feed on the crop (cotton bollworm, corn borer, pink bollworm, and so on), and has little effect on beneficial insects that do not feed on the crop; whether species outside the target are affected, however, must be verified one by one in case-by-case assessment (Section 29.4).

The significance for the crop is to protect yield, not to raise yield potential: its effect is to reduce the loss of leaf area and grain caused by insect feeding, so that the plant comes closer to the photosynthetic and yield capacity it would have without insect damage ([7.13.9](/7.13.9), [7.13.11](/7.13.11)). Its benefit therefore depends on pest pressure: yield gains are large in years and regions with heavy infestation, and there is no benefit to yield when there is no infestation. Another benefit is reduced use of chemical insecticides, most evident in crops such as cotton that were formerly sprayed heavily; control of stem-boring pests also reduces plant wounds and so indirectly reduces ear rot and mycotoxin contamination (fumonisins and aflatoxins in maize are associated with insect damage). These benefits presuppose that the pests do not evolve resistance to the toxin; resistance management is the subject of Section 29.5.

### 29.3.2. Herbicide Tolerance

Herbicide-tolerance traits allow a broad-spectrum herbicide to be sprayed during crop growth without harming the crop, which has changed the way weeds are managed. The target enzymes of the two main herbicides are both in nitrogen or amino acid metabolism:

- Glyphosate inhibits 5-enolpyruvylshikimate-3-phosphate synthase (EPSPS, a chloroplast enzyme) of the shikimate pathway. Aromatic amino acids (phenylalanine, tyrosine, tryptophan) and the many secondary metabolites derived from them (lignin, anthocyanins, tryptophan as the precursor of auxin) can no longer be synthesized, and together with the accumulation of shikimate, the plant dies slowly. Glyphosate-tolerant crops express an EPSPS variant insensitive to glyphosate, so that the shikimate pathway keeps running.
- Glufosinate (phosphinothricin) inhibits glutamine synthetase ([7.13.6](/7.13.6#sec-6.3)). Ammonium assimilation is blocked, $\ce{NH4+}$ accumulates in large amounts, and the reassimilation of ammonia in photorespiration fails, so photosynthesis is inhibited within hours. Glufosinate-tolerant crops express an enzyme that acetylates and thereby inactivates glufosinate.

These traits do not alter photosynthesis, water use, or nutrient uptake of the crop: they raise tolerance to a herbicide, not productivity. Their significance is in management: weeds can be controlled in one operation at a later stage, which favors no-till and conservation tillage and reduces soil erosion and the energy spent on tillage. The drawbacks are that long-term exclusive use of the same herbicide selects for resistant weeds (Section 29.5.3) and concentrates herbicide use on a few compounds.

### 29.3.3. Virus Resistance

Virus-resistant papaya was made by transforming papaya with a fragment of the viral coat protein gene, which confers resistance to papaya ringspot virus. The principle is RNA silencing ([7.13.25](/7.13.25#sec-25.6)): RNA of the viral sequence produced by the transgene is cleaved into small interfering RNAs, which pair with incoming viral RNA and degrade it through a sequence-specific pathway, so that the virus cannot accumulate. Because resistance depends on sequence homology, it is effective only against virus strains with similar sequences, and resistance may decline when the virus strain varies. The importance of this example is that, when papaya ringspot virus nearly destroyed the Hawaiian papaya industry, transgenic papaya was the only effective remedy at the time.

### 29.3.4. Quality Improvement

These traits change the chemical composition of the product and do not involve the physiology of yield. Examples include:

- High-oleic soybean: the fatty acid desaturase (FAD2) that converts oleic acid to linoleic acid is suppressed, raising the oleic acid content from about 20% to about 80%. The oxidative stability of the oil increases, hydrogenation is unnecessary, and *trans* fats are reduced.
- Delayed-ripening tomato: the activity of a cell-wall-degrading enzyme in the fruit (polygalacturonase) or ethylene synthesis ([7.13.15](/7.13.15#sec-15.5)) is reduced, which delays softening so that fruit can be harvested at a more advanced stage of ripeness and transported.
- Carotenoid-enriched rice ("Golden Rice"): rice endosperm can synthesize geranylgeranyl pyrophosphate but lacks several enzymes that convert it to carotenoids. Introducing the corresponding enzyme genes from daffodil or bacteria makes the endosperm accumulate $\beta$-carotene (provitamin A), to alleviate vitamin A deficiency in populations that depend on rice as a staple. It illustrates the logic of metabolic engineering: first find out which step of the pathway is missing, then supply it.
- Other examples are potatoes with reduced allergenic proteins and low acrylamide precursors (silencing asparagine synthetase and vacuolar invertase) and rice with low cadmium accumulation.

What these traits have in common is that they require an understanding of the whole metabolic network: when one enzyme is changed, metabolic flux is redirected elsewhere ([7.13.8](/7.13.8), [7.13.12](/7.13.12)), so changes in composition must be measured across many lines and environments, not only for the target compound.

## 29.4. Principles of Biosafety Assessment and Regulatory Frameworks

The products of plant biotechnology must undergo biosafety assessment and administrative approval before entering the market. We discuss here the general approach to assessment and the institutional framework; the specific regulations differ among countries and are continually updated.

### 29.4.1. Risk and Principles of Assessment

The logic of assessment distinguishes hazard (under what conditions a substance or trait may cause adverse effects) from risk (the probability of such effects and their magnitude): there is risk only when hazard and exposure are both present, and risk assessment is the joint evaluation of the two. The aim of assessment is not to prove "absolute safety" but to judge whether the risk is acceptable and manageable, and to compare it with conventional cultivars used in the same way.

**Definition 29.4.1 (Substantial Equivalence)** A transgenic crop and its products are compared with a conventional comparator cultivar that has a history of safe use as food. If, apart from the introduced trait and its direct consequences, there is no meaningful difference in agronomic characteristics, nutritional composition, and so on, the crop is said to be in **substantial equivalence** with the comparator.

Substantial equivalence is the starting point of assessment, not its conclusion: it focuses attention on where differences exist, namely the introduced gene product itself and the unintended changes that the trait may cause. If meaningful differences are found (for example, a change in nutritional composition), the difference itself must be assessed further toxicologically and nutritionally. Critics point out that the concept is easily understood as "no assessment is needed" and that compositional comparison can detect only known changes; current schemes therefore add a separate assessment of the new protein and, where necessary, use omics methods.

Assessment follows several principles:

1. Case-by-case analysis: each transformation event, and each combination of crop and trait, is assessed separately. The same gene inserted at different sites or expressed in different crops gives different events.
2. Step-by-step evaluation: laboratory studies, contained greenhouse trials, small-scale field trials, larger-scale environmental release, and productive trials, with each step based on the data of the previous one and the scope widening gradually.
3. Comparison with a comparator: the corresponding conventional cultivar is the benchmark, not zero risk; the risks of the alternative practices that would be used without the technology (for example, more insecticide spraying) are also considered.
4. Science-based judgment and precaution: judgments rest on data, and when serious or irreversible harm is possible but scientific evidence is insufficient, precautionary measures may be taken, which is the meaning of the precautionary principle in international protocols.

### 29.4.2. Food and Feed Safety Assessment

Food safety assessment usually includes the following aspects:

| Aspect | What is assessed | Rationale |
|---|---|---|
| Molecular characterization | Copy number, insertion site, sequence, expression level, and stability of the introduced gene | Establish what was introduced and whether an endogenous gene was disrupted |
| Introduced protein | Source and history of consumption; stability in simulated gastric fluid; amino acid sequence similarity to known toxins and allergens | Proteins that are readily digested and heat-labile pose lower risk |
| Toxicology | Acute toxicity of the introduced protein; subchronic feeding trials with the whole food (in some cases) | Identify possible toxicity and determine the no-effect dose |
| Allergenicity | Sequence comparison and digestive stability; genes from known allergen sources need special assessment | Avoid transferring allergens into food, as with a protein from Brazil nut (research was stopped for this reason) |
| Nutrition and composition | Major nutrients, antinutritional factors, natural toxins, and key metabolites compared with the comparator across many sites and years | Judge whether there are changes beyond the natural variation of conventional cultivars |
| Unintended effects | Metabolic changes that insertion of the foreign gene may cause | May be detected by compositional comparison |

For feed, nutritional value trials in animals are also carried out. The basic requirement of this framework is that every new component introduced have toxicological and allergenicity data, and that the composition of the whole food be comparable to that of conventional cultivars within natural variation. For traits already assessed (insect resistance, herbicide tolerance), assessments in most countries have concluded that the proteins can be used safely, but these conclusions apply only to the assessed events and uses.

### 29.4.3. Environmental Risk Assessment

Environmental assessment concerns the behavior of the trait in the field and in ecosystems. It addresses the following questions in turn:

1. Whether the crop itself could become a weed or an invasive species: most crops depend heavily on human management (non-shattering, loss of dormancy, [7.13.28](/7.13.28#sec-28.3)) and cannot establish populations in the wild; new traits (for example, tolerance of salt or drought, or stress resistance), however, may raise fitness and must be assessed.
2. **Gene flow**: whether the introduced gene can pass by pollen to non-transgenic crops of the same species, weedy forms, or wild relatives. The assessment needs to know whether the crop is self-pollinating or outcrossing, wind- or insect-pollinated, whether there are relatives with which it can hybridize nearby (for example, rice with weedy rice and common wild rice, or rapeseed with turnip and wild mustard), and whether the trait would make hybrid progeny better adapted to the wild. Gene flow itself is not a risk; the risk depends on whether the trait raises fitness in wild populations ([7.10.7](/7.10.7)). For crops with important wild relatives in their centers of origin, stricter measures are usually adopted.
3. Effects on non-target organisms: pollinators, natural enemies, soil microorganisms, and organisms that feed on plant residues. The assessment rests on the expression level of the toxin in different plant parts, its concentration in the environment, the routes of exposure of the organisms, and toxicological data.
4. Evolution of resistance: resistance of target pests to insect-resistance traits and of weeds to herbicides. It is an evolutionary risk, not a toxicity risk, and is managed through resistance-management plans (Section 29.5).
5. Indirect effects on agricultural management and biodiversity: changes in herbicide-use patterns, secondary pests rising to major-pest status (mirid bugs, which appeared in some cotton regions after broad-spectrum insecticides were greatly reduced), and changes in farmland weeds and in food sources for birds and insects.

Risk assessment and risk management must be kept separate: assessment provides the scientific evidence, and management chooses the measures (isolation distances, buffer zones, monitoring, resistance management, and, where necessary, restrictions on the area), including post-market monitoring.

### 29.4.4. Approval, Labeling, and International Frameworks

Internationally, most countries use an approval system based on risk assessment; the differences lie mainly in what is regulated. A product-based approach (the United States, Argentina, and many regulations in Canada) looks at the characteristics and risks of the final product, regardless of the technology used to obtain it; a process-based approach (the European Union) makes the use of transgenic technology itself the trigger of regulation. This difference is most prominent for genome editing: in recent years, many countries have provided that changes produced by editing that cannot be distinguished from natural mutations or conventional mutagenesis, and that contain no foreign DNA, are not regulated as transgenic but are treated as conventional cultivars or given a simplified review, while others still regulate them as transgenic.

Two basic international instruments exist: the Cartagena Protocol on Biosafety (2000) under the United Nations Convention on Biological Diversity, which governs the transboundary movement of living modified organisms and requires advance informed agreement and the precautionary principle; and the guidelines of the Codex Alimentarius Commission on the safety assessment of foods derived from genetically modified plants (from 2003), which provide a scientific basis for national food safety assessments.

China operates a safety assessment and approval system for agricultural genetically modified organisms: in 2001 the State Council issued the Regulations on the Safety Administration of Agricultural Genetically Modified Organisms, which require that research, testing, production, processing, marketing, and import and export of such organisms be assessed and approved as prescribed. Safety assessment proceeds in stages: laboratory research, intermediate trials, environmental release, and productive trials, and finally an application for a biosafety certificate; after that, procedures such as cultivar registration and production and marketing licenses must be completed before commercial planting. For gene-edited plants, separate safety assessment guidelines have been issued in recent years, with assessment classified by the type of edit and whether foreign genes are present.

Labeling is another part of regulation: its function is to safeguard consumers' right to know and to choose, not to indicate a difference in safety (approved products have passed safety assessment). Labeling systems differ among countries, and the main differences are which products must be labeled (a list system, or all products containing transgenic material), whether there is a threshold of content (the European Union allows adventitious presence of up to 0.9% without labeling), and whether labeling is by product or by production process. China applies qualitative labeling by list.

## 29.5. Resistance Management

When insect-resistance and herbicide-tolerance traits are used in the field over the long term, they impose strong selection pressure on pests and weeds, just as insecticides and antibiotics do ([7.10.34](/7.10.34#sec-34.4.2)): resistance alleles are very rare at first but increase rapidly under strong selection and make the trait ineffective. Resistance management is therefore part of the management of transgenic crops, and it is the fourth type of question in the environmental assessment of Section 29.4.3.

### 29.5.1. The High-Dose/Refuge Strategy

The **refuge strategy** applies to insect-resistant crops: a certain proportion of crop without the trait (the refuge) is planted next to the insect-resistant crop. Pests in the refuge are not selected and remain susceptible to the toxin, while the few resistant homozygotes that survive on the insect-resistant crop mate with the large number of susceptible individuals from the refuge, so that their progeny are mostly heterozygous. If the toxin dose is high enough to kill heterozygotes as well (resistance is functionally recessive), the resistance allele is diluted and the rate of its increase is greatly reduced. This strategy requires several conditions: high expression, so that resistance is functionally recessive; a very low initial frequency of resistance genes; random mating between resistant individuals and susceptible individuals from the refuge; and no marked advantage of resistance.

### 29.5.2. A Single-Locus Model

Suppose that resistance in the pest is controlled by a single locus, that the frequency of the resistance allele $R$ is $q$ and that of the susceptible allele $S$ is $p = 1 - q$, and that mating is random, so that the genotypes $SS$, $SR$, and $RR$ have frequencies $p^2$, $2pq$, and $q^2$ (Hardy–Weinberg proportions, [7.4.22](/7.4.22)). Let $r$ be the proportion of the refuge in the whole habitat. All genotypes in the refuge have fitness 1, and genotype $g$ on the insect-resistant crop has fitness $w_g^{\mathrm{Bt}}$; averaged over the whole habitat, the effective fitness of each genotype is then

$$
w_g = r + (1 - r)\, w_g^{\mathrm{Bt}}, \tag{29.3}
$$

and after selection followed by one generation of random mating, the frequency of the resistance allele becomes

$$
q' = \frac{w_{RR}\, q^2 + w_{SR}\, pq}{w_{SS}\, p^2 + 2 w_{SR}\, pq + w_{RR}\, q^2}. \tag{29.4}
$$

On a high-dose insect-resistant crop, nearly all susceptible homozygotes die. Take $w_{SS}^{\mathrm{Bt}} = 0.01$ and $w_{RR}^{\mathrm{Bt}} = 1$, with heterozygote fitness $w_{SR}^{\mathrm{Bt}} = w_{SS}^{\mathrm{Bt}} + h\,(w_{RR}^{\mathrm{Bt}} - w_{SS}^{\mathrm{Bt}})$, where $h$ is the dominance of resistance ($h = 0$ is completely recessive). The initial frequency is $q_0 = 0.001$, and resistance has no cost.

![Evolution of resistance in an insect-resistant crop with a refuge in the single-locus model. A: with recessive resistance ($h = 0$), the frequency of the resistance allele over generations with no refuge, a 5% refuge, and a 20% refuge. B: the number of generations required for the resistance allele frequency to exceed 0.5, as a function of the refuge proportion; the three lines are different dominance values ($h = 0$, $0.1$, $0.5$).](./plots/refuge-resistance.py)

The model gives three results. First, when resistance is recessive, a refuge delays resistance considerably: with no refuge, $q$ exceeds 0.5 in about 15 generations; a 5% refuge extends this to about 70 generations, a 20% refuge to about 270, and a refuge of half the habitat to more than 1000. Second, when resistance is not recessive, the effect of the refuge is much weaker: with $h = 0.1$, even a 20% refuge gives only 17 generations, and with $h = 0.5$ only 8. Third, all curves stay at a very low frequency for a long time and then rise rapidly; resistance is invisible at first, and by the time it is detected it is often hard to reverse.

The result can be understood from the small-$q$ approximation of Eq. (29.4). When resistance is recessive ($w_{SR} = w_{SS}$) and $q$ is very small, $q' \approx q\,[\,1 + (w_{RR}/w_{SS} - 1)\,q\,]$: growth of the resistance allele depends on $q^2$, because only homozygotes benefit, and at low frequency nearly all $R$ alleles are "hidden" in heterozygotes. By Eq. (29.3), the ratio is $w_{RR}/w_{SS} = 1/[\,r + 0.01\,(1 - r)\,]$. The larger the refuge, the smaller the ratio and the growth coefficient, and the more generations $q$ needs to leave the low-frequency region, roughly in proportion to $1/[(w_{RR}/w_{SS} - 1)\,q_0]$.

### 29.5.3. Resistance Management in Practice

The assumptions of the theoretical model do not necessarily hold in the field, so practical measures are broader:

- Gene stacking: expressing in the same cultivar several toxins that act on different receptors (Cry1 and Cry2, Vip). For pests to become resistant to several toxins at once, the probability is about the product of the individual probabilities, so when the resistance alleles to the different toxins are independent, stacking greatly delays the appearance of resistance; this presupposes that there is no cross-resistance among the toxins.
- Forms of refuge: structured refuges (separate fields), seed-mix refuges (a small amount of non-transgenic seed mixed with transgenic seed), and natural refuges provided by other host plants (the cotton bollworm also feeds on maize, soybean, and other weeds, and Chinese cotton regions have obtained many natural refuges this way).
- Monitoring and response: monitoring changes in the susceptibility of field pest populations to the toxin, and drawing up response plans for when the resistance frequency reaches a threshold (replacing the trait, adding control measures).
- Integrated management: combining the trait with natural enemies, crop rotation, cultural practices, and, when necessary, pesticides, rather than relying on a single trait.
- Weed resistance: since glyphosate-tolerant crops were planted, many weed species have evolved resistance to glyphosate, through mutation and gene amplification of the target enzyme EPSPS and through changes in uptake, translocation, and sequestration. Their evolutionary dynamics are similar to those of the model above, but the seed bank and pollen dispersal of weeds make the problem more complex. The principle of management is to rotate and mix several herbicides with different modes of action, together with crop rotation and tillage practices, rather than to use a single herbicide repeatedly.

Resistance management illustrates the link between plant biotechnology and evolutionary biology: the useful life of a technology is determined by the evolutionary dynamics of pest and weed populations, and the goal of management is to match changes in selection pressure to the speed of evolution.

## Summary

| Topic | Key points | Main examples and values |
|---|---|---|
| Tissue culture: rapid propagation | Eq. (29.1): $N_n = N_0 m^n$; clonal uniformity; somaclonal variation | Example 29.1.1: $3^{13} \approx 1.6 \times 10^6$; banana, orchid, potato |
| Virus elimination | The shoot apical meristem has no mature vasculature, so virus is excluded; virus elimination is not resistance and needs regular renewal | Potato, sweet potato, strawberry |
| Haploid breeding | Anther or microspore culture followed by doubling gives a pure line in one generation; selfing halves heterozygosity: Eq. (29.2) | About 1.6% heterozygosity remains after 6 generations of selfing |
| Germplasm conservation | Seed banks, field gene banks, in vitro conservation, and cryopreservation complement one another | Cryopreservation for recalcitrant seeds and vegetatively propagated crops |
| Development of improvement technologies | Sources of variation: natural variation, recombination, random mutation, introduced foreign genes, targeted editing | Crossing → mutagenesis → marker-assisted selection → transgenesis → genome editing; products may be indistinguishable from natural mutations |
| Insect resistance (Bt) | Alkaline solubilization in the midgut, protease activation, receptor binding, pore formation; high selectivity; protects yield rather than raising potential | Less insecticide; fewer wounds and less toxin contamination |
| Herbicide tolerance | Glyphosate inhibits EPSPS and glufosinate inhibits glutamine synthetase; tolerance through target-enzyme variants or detoxifying enzymes | No-till and conservation tillage; resistant weeds |
| Virus resistance and quality | RNA silencing; metabolic engineering supplies a missing step of a pathway | Virus-resistant papaya; high-oleic soybean; Golden Rice |
| Principles of assessment | Definition 29.4.1 (substantial equivalence) as the starting point; case-by-case analysis, step-by-step evaluation, comparison with a comparator, precaution | Molecular characterization, toxicology, allergenicity, compositional comparison |
| Environmental assessment | Weediness, gene flow, non-target organisms, evolution of resistance, indirect effects | Stricter requirements in centers of origin with wild relatives |
| Regulatory framework | Product-based versus process-based; protocol and Codex; staged approval; labeling | Cartagena Protocol (2000); EU 0.9% |
| Refuge strategy | Eqs. (29.3), (29.4); high dose makes resistance functionally recessive; refuge dilutes resistance | $h = 0$: 15 generations with no refuge, 270 with a 20% refuge; only 8 when $h = 0.5$ |
| Resistance management | Gene stacking, multiple forms of refuge, monitoring, integrated management; herbicide rotation and mixing | The time to resistance depends on $q_0$ and the strength of selection |

## Questions

1. An orchid cultivar is micropropagated, subcultured every 6 weeks with an average multiplication of 2.5-fold each time. Starting from one explant and ignoring losses, how many cultures can be obtained in one year (52 weeks, taking the whole number of cycles)? Why is the actual number much lower?

   **Answer** A year contains $\lfloor 52/6 \rfloor = 8$ cycles, and by Eq. (29.1), $N_8 = 2.5^8 \approx 1.5 \times 10^3$, about 1500. The actual number is lower for several reasons: some cultures are discarded because of contamination or vitrification; the multiplication rate varies with the number of subcultures and the culture conditions and is not constant; there are further losses at rooting and acclimatization; to avoid somaclonal variation, subculture is usually not continued indefinitely and fresh material must be taken regularly from the original mother plant; and a portion must be set aside as conserved material.

2. An $F_1$ hybrid is heterozygous at a locus, and one round of anther culture of the $F_1$ gives doubled haploids. This is equivalent to how many generations of continuous selfing before the heterozygosity at the locus falls below 1%? If a breeding scheme requires individuals homozygous at 3 independent loci simultaneously, compare 4 generations of selfing with one round of doubled haploid production.

   **Answer** By Eq. (29.2), $(1/2)^n < 0.01$, so $n > \log_2 100 \approx 6.64$; 7 generations of selfing are needed to fall below 1%, whereas doubled haploids are completely homozygous in one generation. With 3 independent heterozygous loci, after 4 generations of selfing the homozygosity at each locus is $1 - 1/16 = 15/16$, and the probability that all three loci are homozygous is $(15/16)^3 \approx 0.82$, so about 18% of individuals are still heterozygous at one locus at least. The homozygous individuals also include all combinations of the two homozygous classes at each locus (8 classes in all, each about $1/8$), and obtaining a particular homozygous combination requires further selection among these progeny. Doubled haploids give fully homozygous individuals in one generation: the 8 genotypes of $F_1$ gametes each make up $1/8$, so the target genotype can be obtained as long as the population is large enough, in a shorter time.

3. On a Bt crop let $w_{SS}^{\mathrm{Bt}} = 0.01$ and $w_{RR}^{\mathrm{Bt}} = 1$, with completely recessive resistance ($h = 0$) and $q_0 = 10^{-3}$. (a) Find the ratio $w_{RR}/w_{SS}$ when the refuge is 10%. (b) Use the small-$q$ approximation $q' \approx q\,[\,1 + (w_{RR}/w_{SS} - 1)\,q\,]$ to estimate the number of generations for the resistance frequency to rise appreciably, $t \approx 1/[(w_{RR}/w_{SS} - 1)\,q_0]$, and compare it with the value in the figure (about 129 generations to exceed 0.5). (c) What is the estimate when the refuge is raised to 20%?

   **Answer** (a) By Eq. (29.3), $w_{SS} = 0.1 + 0.9 \times 0.01 = 0.109$ and $w_{RR} = 1$, so the ratio is $1/0.109 \approx 9.2$. (b) $t \approx 1/[(9.2 - 1) \times 10^{-3}] \approx 1/(8.2 \times 10^{-3}) \approx 122$ generations, close to the numerical value of 129 generations (the approximation ignores the feedback as $q$ increases and assumes $w_{SR} = w_{SS}$, so it is slightly low). (c) For $r = 0.2$, $w_{SS} = 0.2 + 0.8 \times 0.01 = 0.208$, the ratio is $\approx 4.8$, and $t \approx 1/(3.8 \times 10^{-3}) \approx 263$ generations, against a numerical result of about 270. Doubling the refuge about doubles the delay, because $t$ is inversely proportional to $w_{RR}/w_{SS} - 1$.

4. (Open question) Some argue that "transgenic crops are substantially equivalent to conventional crops, so no safety assessment is needed," while others argue that "transgenic crops are something new, so zero risk must be demonstrated." Comment on both views in light of this chapter and explain how assessment should proceed.

   **Answer** Outline: both views misunderstand the logic of assessment. The first treats substantial equivalence as the conclusion of assessment; in fact it is only the starting point of comparison, used to identify the differences that need further assessment: a newly introduced protein needs independent toxicological and allergenicity assessment, differences in composition must also be assessed, and since every transformation event is different, assessment is case by case and the scope is widened in stages. The second demands "zero risk," which cannot be demonstrated (no thing, including conventional cultivars and foods with a history of use, can be proved absolutely free of risk) and also lacks a comparator cultivar and alternative practices as the benchmark. A reasonable approach is to take the conventional comparator as the benchmark, identify hazards and assess exposure, sort risks into those that are acceptable and those that need management, manage them through approval, isolation, monitoring, and labeling, continue monitoring after release, and update conclusions as scientific evidence develops; that assessment targets the traits of the product rather than the technology itself is also the core of the discussion on regulating genome editing.
