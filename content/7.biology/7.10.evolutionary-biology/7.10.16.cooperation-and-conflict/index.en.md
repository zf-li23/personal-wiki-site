---
title: Cooperation and Conflict
description: "When selection favors helping and when it favors harming: the four kinds of social action; cooperation among non-relatives (by-product benefits, reciprocity and the iterated prisoner's dilemma); evolutionarily stable strategies, the hawk–dove game and replicator dynamics; kin selection, Hamilton's rule derived from the Price equation, relatedness, green beards and spite; conflict in families (parental care, siblicide, parent–offspring conflict, genomic imprinting, eusociality); selfish genetic elements and organelles; multilevel selection and the major evolutionary transitions."
---

An ant colony consists of a mother and her many daughters, most of which never reproduce; they gather food, raise their sisters and die defending the nest. Yet in some ant species workers kill their brothers and even their mother. Within every genome, some genes cheat at meiosis at the expense of the others, while the trillions of cells of an animal cooperate so closely that the animal can be treated as a single individual. Cooperation and conflict occur at every level of biological organization, and natural selection, which favors whatever leaves more copies of itself, must explain both. This chapter develops the theory that does so: game theory for interactions whose payoffs depend on what others do, and kin selection, which accounts for the fact that interacting individuals often share genes.

The theory builds on the **levels of selection** introduced in 7.10.3, on **frequency-dependent selection** ([7.4.23](/7.4.23#sec-23.3.2)) and on the mathematics of **identity by descent** and the **kinship coefficient** (7.4.22, 7.4.24). It reappears in the theory of sex ratios (7.10.13), in host–parasite and mutualistic interactions between species (7.10.17), and in the evolution of genomes, where selfish DNA shapes genome size (7.10.18). The mechanisms of **selfish genetic elements**, **meiotic drive** and **genomic imprinting** are those of [7.4.17](/7.4.17#sec-17.6) and [7.4.18](/7.4.18#sec-18.2); here we treat their evolutionary logic. Behavioral details of social animals belong to animal behavior (7.18).

## 16.1. The Costs and Benefits of Social Actions

Classify an action by its effect on the fitness of the individual that performs it (the actor) and of the individual it affects (the recipient) (Hamilton 1964):

| | Recipient gains | Recipient loses |
|---|---|---|
| Actor gains | mutual benefit | selfishness |
| Actor loses | altruism | spite |

**Definition 16.1.1 (Altruism and Spite)** An action is **altruism** if it increases the lifetime fitness of the recipient and decreases that of the actor; it is **spite** if it decreases the fitness of both. An action that increases the fitness of the recipient, whatever its effect on the actor, is *cooperative*; an action that increases the actor's fitness at the recipient's expense is *selfish*.

These terms describe fitness consequences only, not intentions. They apply to bacteria and to genes as much as to animals: a "selfish gene" is a DNA sequence that increases in frequency at the expense of others, not one with motives. The evolutionary puzzle is that cooperators can be exploited by *cheaters*, individuals that receive benefits without paying the cost. The slime mold *Dictyostelium discoideum* shows the problem: when food runs out, single cells aggregate into a slug that forms a fruiting body, in which the cells of the stalk die so that those of the spore head can disperse. Cells carrying a mutation at the *chtA* locus contribute preferentially to the spores, and in mixtures with wild-type cells their frequency increased over successive cycles in the laboratory. Why, then, has cooperation not collapsed?

Before the 1960s many biologists explained such traits as adaptations "for the good of the group or the species", a view criticized by Williams (1966), Hamilton and Maynard Smith because selfish variants increase within each group and selection among groups is usually weaker (7.10.3). Several mechanisms can nevertheless favor cooperation; a key distinction among them is whether the interacting individuals are relatives.

## 16.2. Cooperation Among Unrelated Individuals

### 16.2.1. Direct Benefits

The simplest cooperation pays the actor directly. An individual that joins a flock, school or herd reduces its own risk of predation; European starlings threatened by a raptor pack into a dense flock in which each bird tries to reach the safe center. Wolves hunting together capture prey that one could not. Benefits may be delayed: in the lance-tailed manakin (*Chiroxiphia lanceolata*), a subordinate male joins an unrelated dominant male in a coordinated courtship display; females prefer well-coordinated pairs and mate almost only with the dominant, but the subordinate inherits the display site when the dominant dies, which may take as long as 13 years.

### 16.2.2. Reciprocity and the Prisoner's Dilemma

**Definition 16.2.1 (Reciprocal Altruism)** **Reciprocal altruism** (reciprocity) is cooperation in which an individual helps another at a cost and is later helped in return (Trivers 1971). It can evolve when the same individuals interact repeatedly, can recognize and remember each other, and when the benefit of being helped exceeds the cost of helping.

Its logic is captured by a game. In the *prisoner's dilemma*, two players can each cooperate ($C$) or defect ($D$); the payoffs to a player are $R$ (reward) if both cooperate, $P$ (punishment) if both defect, $T$ (temptation) for defecting against a cooperator and $S$ (sucker's payoff) for cooperating with a defector, with $T > R > P > S$. Whatever the other does, defection pays more, so in a single encounter both defect and receive $P$, although both would have done better with $R$. A convenient special case is the *donation game*: cooperating costs the actor $c$ and gives the partner $b > c$, so that $R = b - c$, $T = b$, $S = -c$, $P = 0$.

**Theorem 16.2.1 (Tit for Tat in the Iterated Prisoner's Dilemma)** In the donation game played repeatedly, with probability $w$ of a further round after each round, let *tit for tat* (TFT) cooperate in the first round and then copy the partner's previous move, and let *always defect* (ALLD) defect in every round. Then TFT cannot be invaded by ALLD if and only if
$$
w > \frac{c}{b}.
$$

**Proof** The expected number of rounds is $1/(1 - w)$. TFT against TFT cooperates throughout and gains $(b - c)/(1 - w)$. ALLD against TFT gains $b$ in the first round and nothing afterwards, since TFT then defects. TFT resists invasion by rare ALLD if $(b - c)/(1 - w) > b$, that is $b - c > b - bw$, or $w > c/b$. $\square$

ALLD can also never be invaded by rare TFT (TFT loses $c$ against ALLD), so the population is bistable: cooperation established among a cluster of reciprocators can spread, but it cannot start from a single mutant in a population of defectors unless interactions are clustered. In Axelrod's computer tournaments (Axelrod and Hamilton 1981), TFT was a successful strategy; with errors, more forgiving strategies, such as "win–stay, lose–shift", which repeats its last move after a good outcome and switches after a bad one, do better (Nowak and Sigmund 1993). Reciprocal cooperation has been described in several fishes, birds and mammals. Common vampire bats (*Desmodus rotundus*), which starve if they miss a blood meal for a few nights, regurgitate blood to roost-mates, including unrelated individuals with which they have long-term bonds; female yellow baboons (*Papio cynocephalus*) with strong social bonds to other females have offspring that survive better. In both, individuals interact repeatedly over long periods.

![Reciprocity in the iterated donation game (Theorem 16.2.1) with benefit b = 3 and cost c = 1. A: the expected payoffs per game to TFT and ALLD when TFT has frequency x in the population and the probability of another round is w = 0.8: TFT does better only above the unstable threshold x* (dashed). B: the threshold frequency of TFT needed for it to spread, as a function of w: it falls from 1 at w = c/b = 1/3 toward 0 as interactions become long-lasting](./plots/iterated-pd.py)

Cooperation can also be enforced. Partners may punish or impose *sanctions* on defectors, terminating the relationship or withholding benefits; policing by workers in social insects (Section 16.3.3) and the immune system's destruction of cancer cells, which are selfish members of the cooperative society of cells, are examples.

### 16.2.3. Evolutionarily Stable Strategies

When the payoff of a behavior depends on what others do, the optimization arguments of life history theory (7.10.15) no longer suffice: there is no "best" behavior independent of the population. Maynard Smith and Price (1973) introduced the concept that replaces the optimum.

**Definition 16.2.2 (Evolutionarily Stable Strategy)** Let $E(J, I)$ be the payoff (fitness) to an individual playing strategy $J$ against an opponent playing $I$. A strategy $I$ is an **evolutionarily stable strategy** (ESS) if for every other strategy $J \neq I$ either

1. $E(I, I) > E(J, I)$, or
2. $E(I, I) = E(J, I)$ and $E(I, J) > E(J, J)$.

A population in which almost everyone plays an ESS cannot be invaded by a rare mutant strategy.

The first condition says that the ESS does better against itself than any mutant does against it; the second deals with mutants that are equally good against the resident, which must then do worse against themselves. An ESS is a Nash equilibrium of the game with the additional stability condition; unlike the economic theory, evolutionary game theory requires no rationality, only that strategies with higher payoff increase in frequency.

**Definition 16.2.3 (Hawk–Dove Game)** In the **hawk–dove game**, two individuals contest a resource of value $V$. A *hawk* escalates and fights until injured or until the opponent retreats; a *dove* displays and retreats if the opponent escalates. Two hawks each win with probability $\tfrac12$ and pay an injury cost $C$ when they lose; two doves share the resource. The payoffs to the row player are

| | against Hawk | against Dove |
|---|---|---|
| Hawk | $(V - C)/2$ | $V$ |
| Dove | $0$ | $V/2$ |

**Theorem 16.2.2 (ESS of the Hawk–Dove Game)** (a) If $V \geq C$, Hawk is the ESS. (b) If $V < C$, there is no pure ESS; the ESS is the mixed strategy that plays Hawk with probability $p^* = V/C$, and a population of pure hawks and doves converges to a hawk frequency $p^* = V/C$ under the replicator dynamics
$$
\frac{\mathrm{d}p}{\mathrm{d}t} = p(1 - p)\left[W_H(p) - W_D(p)\right], \qquad W_H - W_D = \frac{V}{2} - \frac{C}{2}p .
$$

**Proof** (a) $E(H, H) = (V - C)/2 \geq 0 = E(D, H)$; if equality holds, $E(H, D) = V > V/2 = E(D, D)$. (b) If $V < C$, Dove invades Hawk ($0 > (V - C)/2$) and Hawk invades Dove ($V > V/2$). In a population with hawk frequency $p$, $W_H = p(V - C)/2 + (1 - p)V$ and $W_D = (1 - p)V/2$, so $W_H - W_D = V/2 - Cp/2$, which is zero at $p^* = V/C$, positive below and negative above: $p^*$ is a globally stable equilibrium of the replicator equation on $(0, 1)$. For a mixed strategy $I$ playing Hawk with probability $p^*$, every strategy $J$ has the same payoff against $I$ (the pure strategies earn equally), and one checks that $E(I, J) - E(J, J) = \tfrac{C}{2}(p^* - p_J)^2 > 0$ for $p_J \neq p^*$, so condition 2 holds. $\square$

The replicator equation is the continuous-time version of selection with frequency-dependent fitness (Taylor and Jonker 1978). Two lessons generalize. First, the ESS need not maximize the mean fitness of the population: a population of doves would do better than the mixed ESS, which pays the cost of fights. Second, the outcome depends on which strategies are possible. If contests are asymmetric and the asymmetry is visible, for example who owns a territory, the strategy "bourgeois", which plays Hawk as owner and Dove as intruder, is an ESS when $V < C$ and settles contests without escalation (Maynard Smith 1982); many animals do resolve contests by ritualized displays, and owners usually win. If there is no ESS, as in the rock–paper–scissors game, frequencies cycle: in the side-blotched lizards of 7.10.13 and in mixtures of colicin-producing, resistant and sensitive strains of *Escherichia coli*, in which the three types coexisted on agar plates, where interactions are local, but not in well-mixed flasks (Kerr et al. 2002). Whether a population actually reaches an ESS can depend on genetics: if the ESS phenotype is produced only by a heterozygote, the population stays polymorphic.

![Evolutionary games. A: payoff matrix of the hawk–dove game with V = 2, C = 3. B: replicator dynamics of the frequency of hawks from several initial frequencies; all converge to the mixed equilibrium p* = V/C = 2/3. C: the payoff difference W_H − W_D as a function of the hawk frequency; hawks do better when rare and worse when common](./plots/hawk-dove.py)

## 16.3. Kin Selection

### 16.3.1. Inclusive Fitness and Hamilton's Rule

Parents that feed their young at a cost to themselves are altruistic in the sense of Definition 16.1.1, yet no one finds their behavior puzzling: an allele that causes parental care increases its own transmission through the offspring that carry it. Haldane is said to have remarked that he would lay down his life for two brothers or eight cousins. Hamilton (1964) generalized the logic to all relatives.

**Definition 16.3.1 (Direct, Indirect and Inclusive Fitness; Kin Selection)** The **direct fitness** of an allele (or of the individual carrying it) is the reproduction of its carrier attributable to the carrier's own phenotype. Its **indirect fitness** is the additional reproduction of relatives caused by the carrier's behavior, weighted by their relatedness to the carrier. **Inclusive fitness** is the sum of direct and indirect fitness, counting only the effects caused by the focal individual. **Kin selection** is selection on the indirect component: the change in allele frequency that results from effects of an individual's behavior on the reproduction of its relatives.

**Theorem 16.3.1 (Hamilton's Rule)** Let each individual $i$ have a genetic value $g_i$ for a social behavior (for example its frequency of an allele, $0, \tfrac12$ or $1$), and let its fitness be
$$
w_i = w_0 - c\,g_i + b\,g_i' ,
$$
where $c$ is the cost of the behavior to the actor, $b$ the benefit to a recipient and $g_i'$ the genetic value of the individual(s) whose behavior affects $i$. If genetic values are transmitted without bias, the mean genetic value increases if and only if
$$
rb > c, \qquad r = \frac{\operatorname{Cov}(g', g)}{\operatorname{Var}(g)} ,
$$
where $r$, the **relatedness**, is the regression coefficient of the genetic value of social partners on that of the focal individual.

**Proof** By the Price equation (Definition 16.5.1) with no transmission bias, $\bar w\,\Delta\bar g = \operatorname{Cov}(w, g) = -c\operatorname{Var}(g) + b\operatorname{Cov}(g', g)$. Dividing by $\operatorname{Var}(g) > 0$, $\Delta\bar g > 0$ if and only if $-c + br > 0$. $\square$

The rule applies to any social behavior, not only to altruism: $b$ and $c$ may have either sign (a selfish act has $c < 0$, $b < 0$), and it predicts spite when $r < 0$. Relatedness in this sense is a measure of genetic similarity relative to the population, not of genealogy itself; for weak selection and a pedigree relationship it equals twice the coefficient of kinship ([7.4.24](/7.4.24#fml-24.4.1)), the probability that genes in the two individuals are identical by descent, which gives the familiar values. If an allele causes help to random members of the population, $r = 0$ and help is never favored. Hamilton's rule is a statement about the net effect of a behavior on an allele: through the recipient, the behavior increases the allele's transmission as if the actor had $rb$ more offspring of its own.

**Example 16.3.1 (Relatedness in Diploids and Haplodiploids)** For autosomal genes in an outbred diploid species, $r = \tfrac12$ between parent and offspring and between full siblings, $\tfrac14$ between half siblings, grandparent and grandchild or uncle and nephew, and $\tfrac18$ between first cousins. In haplodiploid species (Hymenoptera), males develop from unfertilized eggs and inherit only their mother's genes. A rare allele in a worker came from her mother with probability $\tfrac12$ and from her father with probability $\tfrac12$; her full sister carries it with probability $\tfrac12 \cdot \tfrac12 + \tfrac12 \cdot 1 = \tfrac34$ (all daughters receive the father's whole genome), and her brother with probability $\tfrac12 \cdot \tfrac12 = \tfrac14$. A female is related to her own offspring of either sex by $\tfrac12$.

**Example 16.3.2 (Coalitions of Brothers in Wild Turkeys)** Male wild turkeys (*Meleagris gallopavo*) display either alone or in pairs, and in pairs only the dominant male mates (Krakauer 2005). A subordinate raises the reproductive success of his dominant partner from 0.9 offspring (displaying alone) to 7, a benefit $b = 6.1$; his cost is the 0.9 offspring he would have had displaying alone, $c = 0.9$. Genetic analysis showed that partners are related by $r = 0.42$ on average, so $rb = 2.6 > c$: Hamilton's rule is satisfied, and the inclusive fitness gain is $rb - c = 1.7$ offspring.

:::

Kin selection can favor altruism only if help is directed preferentially to relatives. This can happen by recognition or by proximity. Female Mexican free-tailed bats (*Tadarida brasiliensis*) find their own pups in caves where millions roost at densities of about 4000 per square meter; ant colonies distinguish nestmates from strangers by odor; long-tailed tits (*Aegithalos caudatus*) that fail to breed help to rear the young of close relatives. Across birds and mammals, kin discrimination is stronger where the benefits of helping are greater, as Hamilton's rule predicts. Without recognition, limited dispersal keeps relatives together, and the alarm calls of ground squirrels and the cooperation within troops of primates are directed largely at kin. But limited dispersal also intensifies competition among relatives, which can cancel the benefit of helping them (Taylor 1992). In the bacterium *Pseudomonas aeruginosa*, cells secrete siderophores, iron-scavenging molecules that benefit all nearby cells, and nonproducing cheaters exploit them; in experimental cultures, producers increased only when relatedness was high and competition between relatives was weak, and cheaters won when relatedness was low and competition strong (Griffin, West and Buckling 2004).

A gene could also direct altruism to its own copies without kinship, if it caused both a recognizable label and help to individuals with the label, the *green-beard effect* (Hamilton 1964; Dawkins 1976). Such genes are rare, because a mutation that kept the label but dropped the help would cheat. In *Dictyostelium*, the *csA* gene encodes a homophilic cell-adhesion protein: cells that carry it adhere to one another and enter the fruiting body together, while knockout cells, which would otherwise cheat, are excluded from aggregates (Queller et al. 2003).

Spite requires negative relatedness, that is, harming individuals less related to the actor than the average member of the local population, and it is favored when harming them benefits others who are more closely related to the actor. Many bacteria release bacteriocins, toxins that kill susceptible cells; the producing cells often die when they release the toxin, and the resistance gene is tightly linked to the toxin gene, so the toxin kills only non-relatives and frees resources for the producer's clone-mates.

### 16.3.2. Conflict in the Family

Families are the setting of both the most intense cooperation and some of the most extreme conflict.

Conflict begins with parental care. Males and females both gain from the survival of their offspring, but each gains more if the other does the work. Parental care is favored when its benefit to the current offspring exceeds its cost in future reproduction. Models in which each parent's optimal effort decreases with the partner's effort predict an ESS of biparental care if the two response curves intersect and uniparental care otherwise, the parent with the lower cost of care ending up caring alone. In birds and mammals, where feeding the young is costly and keeps males from further matings, care is given by females or by both parents; in fishes and frogs, which guard eggs but do not feed them, a male can attract further females while guarding a nest, while a female must feed to make more eggs, and male-only care is common. This is a form of the **sexual conflict** of 7.10.13, in which **sexually antagonistic selection** acts on interacting traits of the two sexes.

Some family members kill others. Males that take over a group often kill the young sired by their predecessors, in lions, baboons and many other social mammals, most often in social species and least often in monogamous ones; parents themselves may reduce brood size by abandoning or killing some young when food is scarce, and plants abort seeds. In some eagles and boobies, the first-hatched chick regularly kills its sibling; the second egg is insurance against the failure of the first.

**Definition 16.3.2 (Parent–Offspring Conflict)** **Parent–offspring conflict** is the difference between the amount of parental investment that maximizes the inclusive fitness of a parent and the amount that maximizes the inclusive fitness of an offspring (Trivers 1974).

A parent is equally related to all its offspring and should invest in a given offspring as long as the benefit $B$ to it exceeds the cost $C$ to other (present or future) offspring, $B/C > 1$. The offspring is related to itself by 1 and to a full sibling by $\tfrac12$, so it should demand investment until $B/C$ falls to $\tfrac12$ (or $\tfrac14$ if its siblings are half siblings). Over the range $\tfrac12 < B/C < 1$ parent and offspring disagree, which can explain weaning conflict and the escalated begging of nestlings. Brood parasites such as cuckoos and cowbirds, which are unrelated to their nestmates, beg more intensely than host chicks. In humans the conflict extends into the womb: cells of the embryo invade the uterine spiral arteries and remodel their walls so that the mother cannot constrict them, which increases the flow of nutrients to the fetus (Haig 1993).

![Parent–offspring conflict (Definition 16.3.2). As an offspring grows, the benefit B of further investment to it declines relative to the cost C to its parent's other offspring. The parent favors investment while B/C > 1; an offspring favors it while B/C > r, the relatedness to the siblings that bear the cost (1/2 for full siblings, 1/4 for half siblings). The shaded intervals are periods of conflict, longer when the offspring's siblings are half siblings](./plots/parent-offspring-conflict.py)

The same conflict acts on genes within the offspring according to their parental origin. Paternally derived genes in an offspring are less likely than maternally derived genes to be present in the mother's other offspring, if those may have different fathers, and are not present in the mother at all. The *kinship theory of genomic imprinting* (Haig) predicts that paternally expressed genes should promote the extraction of maternal resources and maternally expressed genes restrain it. In mice and humans, *Igf2*, encoding a fetal growth factor, is expressed only from the paternal allele, and *Igf2r*, encoding a receptor that degrades it, only from the maternal allele (in mice), as predicted; many imprinted genes affect growth with the predicted sign, although imprinted genes do not evolve especially fast, as one might expect if they were engaged in a continual conflict. The mechanism of imprinting is described in [7.4.18](/7.4.18#sec-18.2).

### 16.3.3. Eusociality

**Definition 16.3.3 (Eusociality)** **Eusociality** is a social system with cooperative care of the young, overlapping generations of adults in the colony, and a reproductive division of labor in which some individuals (workers) reproduce little or not at all and help others (queens, and in termites kings) to reproduce.

Eusociality occurs in ants, many bees and wasps (all Hymenoptera), all termites, some aphids, thrips and snapping shrimps, and two African mole-rats, including the naked mole-rat (*Heterocephalus glaber*). It has evolved independently several times in Hymenoptera, always from ancestors in which a single mated female provisioned her young in a nest.

Hamilton (1964) noticed that because of haplodiploidy, a hymenopteran worker is more closely related to her full sisters ($r = \tfrac34$) than she would be to her own daughters ($\tfrac12$), which would make rearing sisters a better genetic investment than reproducing, the *haplodiploidy hypothesis*. The argument has well-known problems. A worker's relatedness to her brothers is only $\tfrac14$, so the average over a brood with equal investment in the two sexes is $\tfrac12$, no better than her own offspring, unless workers bias investment toward sisters (the Trivers–Hare conflict of 7.10.13). Queens of many species mate with several males and colonies may have several queens, which lowers relatedness among workers. Termites and mole-rats are diploid, and most haplodiploid lineages are not eusocial. Hughes et al. (2008) reconstructed the mating systems of the ancestors of eusocial lineages of bees, ants and wasps and found that in every case the ancestral queen mated with a single male, the *monogamy hypothesis* (Boomsma): with lifetime monogamy, a female's offspring and her siblings are equally related to her ($r = \tfrac12$), so that even a small advantage of helping makes staying to help favorable, and multiple mating evolved only later, in already eusocial lineages. Ecology supplied the advantage: nests that are costly to build and easy to defend, helpless larvae that must be fed, and the high risk of founding a new nest alone made a small increment of inclusive fitness from helping at home decisive.

Kin selection also explains many conflicts within colonies. A worker is related to her own sons by $\tfrac12$ and to her brothers (the queen's sons) by $\tfrac14$, so she would gain by laying male eggs; but in a colony whose queen mated several times, a worker is related to the sons of other workers (her half- or full nephews) by less than to her brothers, and workers then destroy each other's eggs, *worker policing*, as in the honeybee (*Apis mellifera*) (Ratnieks 1988). Queens also destroy worker-laid eggs. Policing illustrates that kin selection can favor selfishness and coercion as well as altruism.

## 16.4. Conflict Within Genomes

### 16.4.1. Selfish DNA

Mendelian inheritance is remarkably fair: each allele of a heterozygote is transmitted to half the gametes. A mutation that biased transmission in its own favor would spread even if it reduced the survival or fertility of its carriers, and many such **selfish genetic elements** ([Definition 17.6.1](/7.4.17#def-17.6.1)) are known.

The best-studied case is **meiotic drive**. In males, distorters often kill or disable the sperm that do not carry them. Some *t* haplotypes of the house mouse (*Mus musculus*) are transmitted to more than 90 percent of the offspring of heterozygous males, because they produce a toxin to which only the sperm that carry them are resistant; similar killer–resistance systems are found in *Drosophila* (*Segregation distorter*), stalk-eyed flies and fungi. Because a killer allele separated from its resistance allele by recombination would kill the sperm that carry it, such systems are found in regions of low recombination, such as inversions and sex chromosomes. The equilibrium of a driving allele that is harmful in homozygotes is derived in [Formula 17.6.2](/7.4.17#fml-17.6.2). In females, only one of the four products of meiosis becomes the egg, and chromosomes can compete to be that one: in monkeyflowers (*Mimulus*), chromosomes with a particular centromeric sequence enter the egg more often than their homologs. Such *centromere drive* can explain the rapid evolution of centromeric DNA and of the proteins that bind it.

Drive reduces the fitness of the rest of the genome, so suppressors at other loci are favored, and many distorter systems are found suppressed. When populations that have evolved different distorters and suppressors meet, hybrids may carry a distorter without its suppressor, which reduces their fertility; genetic conflict of this kind is a source of **Dobzhansky–Muller incompatibility** between populations (7.10.11). The same logic underlies *gene drives* engineered with CRISPR–Cas9, which copy themselves into the homologous chromosome and are transmitted to nearly all offspring; they could spread traits such as resistance to malaria through mosquito populations, but they raise questions about the risks of modifying natural populations.

**Transposons** insert copies of themselves elsewhere in the genome and increase in number even though most insertions are neutral or harmful ([7.4.17](/7.4.17#sec-17.6.1)). They make up about half of the human genome; the *Alu* element alone has more than a million copies. They persist not because they benefit the host but because they replicate faster than selection removes them, and their accumulation is a major determinant of genome size (7.10.18). Some selfish elements alter the sex ratio: the PSR ("paternal sex ratio") chromosome of the wasp *Nasonia vitripennis* is transmitted by sperm and causes the destruction of all the other paternal chromosomes in the fertilized egg, which therefore develops as a haploid male, the only sex through which PSR is transmitted.

### 16.4.2. Selfish Cytoplasmic Genes

Mitochondria and plastids are transmitted, in most species, only through the mother. Any mitochondrial mutation that increases female reproduction at the expense of male function is therefore favored, since the male route is a dead end for it. In gynodioecious plants such as thyme (*Thymus vulgaris*), some individuals are male-sterile and reproduce only as females, because of **cytoplasmic male sterility** caused by mitochondrial genes ([Definition 11.6.2](/7.4.11#def-11.6.2)): resources diverted from pollen to seeds increase the transmission of the sterility gene. Nuclear genes, which are transmitted through both sexes and are favored by a 1:1 allocation (Theorem 13.3.1), evolve restorers of male fertility, and the result is an arms race between mitochondrial and nuclear genes. Because mitochondrial mutations that harm only males are not removed by selection, they accumulate; mitochondrial variants that affect male fertility or male-specific traits have been found in humans, *Drosophila* and other species. Maternally inherited bacteria such as *Wolbachia* go further, manipulating host reproduction by killing males, feminizing them or making uninfected females incompatible with infected males (cytoplasmic incompatibility), all of which favor their own transmission.

Uniparental inheritance of organelles may itself have evolved to suppress such conflict: a nuclear gene that eliminates the organelles of one parent prevents selfish organelles from competing within the zygote, and once inheritance is uniparental, organelles are selected to be benign to their host. Fittingly, multiple mating types are found only in organisms, such as many fungi, in which mating involves no fusion of cytoplasm (7.10.14).

## 16.5. Levels of Selection

### 16.5.1. The Price Equation

**Definition 16.5.1 (Price Equation)** Let a population of individuals $i$ have character values $z_i$ (for example, allele frequencies) and fitnesses $w_i$ (numbers of offspring), and let $z_i'$ be the mean value among the offspring of $i$, $\Delta z_i = z_i' - z_i$. The **Price equation** (Price 1970) states that the change in the mean value from one generation to the next satisfies
$$
\bar w\,\Delta\bar z = \operatorname{Cov}(w_i, z_i) + \mathbb{E}[w_i\,\Delta z_i],
$$
where the covariance and expectation are taken over individuals in the parental generation.

**Proof** The offspring mean is $\bar z' = \sum_iw_iz_i'/\sum_iw_i$. Hence $\bar w\bar z' = \mathbb{E}[w_iz_i'] = \mathbb{E}[w_iz_i] + \mathbb{E}[w_i\Delta z_i]$, and $\bar w\,\Delta\bar z = \mathbb{E}[w_iz_i] - \bar w\bar z + \mathbb{E}[w_i\Delta z_i] = \operatorname{Cov}(w_i, z_i) + \mathbb{E}[w_i\Delta z_i]$. $\square$

The first term is selection, the second transmission (mutation, meiotic drive, recombination). The equation is an identity that holds for any entities and any character, which makes it a universal bookkeeping tool rather than a predictive model.

**Theorem 16.5.1 (Multilevel Partition)** If the population is divided into groups $k$ with mean character $Z_k$ and mean fitness $W_k$, and transmission is unbiased, then
$$
\bar w\,\Delta\bar z = \underbrace{\operatorname{Cov}_k(W_k, Z_k)}_{\text{between groups}} + \underbrace{\mathbb{E}_k\left[\operatorname{Cov}_{i \in k}(w_{ik}, z_{ik})\right]}_{\text{within groups}} ,
$$
with the group terms weighted by group size (Price 1972; Hamilton 1975).

**Proof** Apply the Price equation to individuals, and decompose the total covariance of $w$ and $z$ by the law of total covariance into the covariance of the group means and the mean of the within-group covariances. $\square$

For an altruistic trait, the within-group term is negative (altruists have lower fitness than their group-mates), and the between-group term is positive (groups with more altruists do better). The trait increases if the between-group term dominates, which requires variation among groups, that is, individuals more similar to their group-mates than to the population: relatedness in the sense of Theorem 16.3.1. For groups of size $n$ in which each altruist pays $c$ and gives $b$ shared among its $n - 1$ group-mates, the partition reduces to Hamilton's rule with $r$ the correlation of genetic values within groups.

![The multilevel partition of selection (Theorem 16.5.1). Groups of 10 individuals are formed with intraclass correlation ρ of altruist status (beta-binomial sampling, mean frequency 1/2); each altruist pays c = 1 and gives b = 3 shared among its group-mates. Monte Carlo estimates (10 000 groups per point) of the within-group term (negative: altruists do worse than their group-mates), the between-group term (positive: groups with more altruists do better) and their sum. The total is positive when ρ exceeds about c/b = 1/3, as Hamilton's rule predicts](./plots/price-multilevel.py)

### 16.5.2. Group Selection and Multilevel Selection

**Definition 16.5.2 (Multilevel Selection)** **Multilevel selection** is selection acting simultaneously at two or more levels of a biological hierarchy, for example among genes within individuals, among individuals within groups and among groups, analyzed by partitioning the total change as in Theorem 16.5.1.

Group selection in the restricted sense of differential extinction and founding of groups (7.10.3) can be effective in experiments. Wade (1976) selected among small populations (48 in each treatment) of the flour beetle *Tribolium castaneum* for large or small population size; after nine generations, populations selected for large size were on average nine times larger than those selected for small size, while within each population individual selection favored cannibalism of eggs and pupae, which lowered population size in all treatments. In nature, the evolution of virulence of the myxoma virus after its release against European rabbits in Australia in 1950 is an example: viruses within a rabbit that replicate fastest are favored, but rabbits infected by highly virulent strains died before the virus could be transmitted, and the virus evolved lower virulence (7.10.17).

The relation between kin selection and group selection has been controversial for decades and still is. The current state of the debate can be summarized as follows. (1) For most models in which both can be formulated, inclusive-fitness and multilevel accounts are mathematically equivalent ways of partitioning the same change in allele frequency: the Price equation can be split either by actor and relative or by group and individual, and both give the same prediction (Hamilton 1975; Queller 1992). (2) In 2010 Nowak, Tarnita and Wilson argued that inclusive-fitness theory is limited to special cases and unnecessary, and proposed population-genetic and group-selection models of eusociality instead; more than 130 researchers replied that inclusive fitness theory is general, well supported and productive (Abbot et al. 2011). Much of the disagreement concerns the assumptions under which Hamilton's rule holds exactly (weak selection, additivity of costs and benefits) and the meaning of $b$, $c$ and $r$ when they are defined by regression. (3) The partitions are not equally useful for every problem. Kin-selection accounts focus on the genetic relationships that drive the evolution of social behavior in families; multilevel accounts are natural when groups are discrete and have their own reproduction, as in microbial colonies, and philosophers distinguish selection on individual fitness within groups (multilevel selection 1) from selection on the reproduction of the groups themselves (multilevel selection 2) (Okasha 2006). (4) Whatever the partition, cooperation requires that the benefits of social actions fall disproportionately on individuals that carry the genes responsible, by relatedness, by spatial structure or by reciprocity. Neither side disputes the experimental evidence that selection among groups can change group traits.

## 16.6. Cooperation and the Major Transitions in Evolution

The history of life includes a few transitions in which previously independent replicators came to reproduce only as parts of a larger whole (Maynard Smith and Szathmáry 1995).

**Definition 16.6.1 (Major Evolutionary Transitions)** The **major evolutionary transitions** are changes in which entities that could replicate independently before the transition can replicate only as part of a larger unit after it, with a division of labor among the parts and new means of transmitting information: examples are the integration of replicating molecules into chromosomes, of prokaryotic cells into the eukaryotic cell with its organelles, of cells into multicellular organisms, and of individuals into eusocial colonies.

Each transition requires that conflict among the lower-level units be suppressed, so that selection at the higher level dominates. The origin of the eukaryotic cell involved the union of an archaeal host cell with a bacterium that became the mitochondrion, and later the capture of a cyanobacterium that became the plastid of algae and plants (**primary endosymbiosis**, 7.10.28). Vertical transmission linked the fate of the endosymbiont to that of its host: a symbiont transmitted only to the host's offspring maximizes its own fitness by maximizing the host's, while horizontally transmitted parasites can gain by exploiting the host (7.10.17).

The evolution of **multicellularity** (7.10.28) is the most familiar case. The cells of a multicellular organism arise by mitosis from one zygote and are genetically nearly identical ($r \approx 1$), so a cell that sacrifices its own reproduction for the organism propagates its genes through the germ cells. Genetic differences among cells, from mutations or from cells of another genotype joining the aggregate, lower this relatedness and create opportunities for cheaters: a mutation that increases the rate of cell division is favored within the organism but usually harms it, as in **cancer**. Several features of organisms can be read as mechanisms that suppress such conflict: development from a single cell, which maximizes relatedness among cells and the heritability of fitness at the level of the organism; early segregation of a germ line in animals, which keeps mutations in somatic cells from being transmitted; and the immune and tumor-suppressor systems that police cell proliferation. Fair meiosis, uniparental inheritance of organelles and worker policing are analogous mechanisms at other levels. The result of these transitions is the individual organism, the level at which most natural selection acts.

## Summary

| Topic | Key concepts | Key results and examples |
|---|---|---|
| Social actions | Mutual benefit, selfishness, **altruism**, **spite** (Definition 16.1.1) | Cheaters in *Dictyostelium* |
| Non-relatives | By-product benefits; **reciprocal altruism** (Definition 16.2.1) | TFT stable iff $w > c/b$ (Theorem 16.2.1); vampire bats, baboons |
| Games | **Evolutionarily stable strategy** (Definition 16.2.2); **hawk–dove game** (Definition 16.2.3) | Mixed ESS $p^* = V/C$; replicator dynamics (Theorem 16.2.2); bourgeois; rock–paper–scissors |
| Kin selection | **Direct fitness**, **indirect fitness**, **inclusive fitness**, **kin selection** (Definition 16.3.1) | **Hamilton's rule** $rb > c$ with $r = \operatorname{Cov}(g', g)/\operatorname{Var}(g)$ (Theorem 16.3.1); turkeys (Example 16.3.2); green beards; bacteriocins |
| Family | **Parent–offspring conflict** (Definition 16.3.2); sexual conflict over care; imprinting | Conflict zone $r < B/C < 1$; *Igf2*/*Igf2r* |
| Eusociality | **Eusociality** (Definition 16.3.3) | Haplodiploidy hypothesis and its problems; ancestral monogamy; worker policing |
| Genomic conflict | Meiotic drive, transposons, PSR, CMS, *Wolbachia* | Suppressors, arms races, incompatibilities |
| Levels | **Price equation** (Definition 16.5.1); **multilevel selection** (Definition 16.5.2) | Multilevel partition (Theorem 16.5.1); *Tribolium*; equivalence and continuing debate |
| Transitions | **Major evolutionary transitions** (Definition 16.6.1) | Eukaryotic cell, multicellularity, colonies; suppression of lower-level conflict |

## Questions

1. Haldane's remark refers to saving drowning relatives at the cost of one's own life. Using Hamilton's rule, explain why two brothers or eight cousins is the break-even point, and why the rule refers to reproductive value rather than to the number of lives.

   **Answer** Saving relatives at the cost $c$ of one's own expected reproduction is favored if $rb > c$. With $r = \tfrac12$ for brothers, saving two of them ($b = 2$ lives' worth of reproduction) gives $rb = 1 = c$; with $r = \tfrac18$ for cousins, eight are needed. The benefit and cost should be measured as expected future reproduction (reproductive value, 7.10.15), not lives: saving two old brothers past reproduction gives no indirect fitness, while saving a young cousin may be worth more than an old brother.

2. In the hawk–dove game with $V = 4$ and $C = 10$, find the ESS and the mean payoff at the ESS, and compare it with the payoff in a population of doves.

   **Answer** $p^* = V/C = 0.4$. At the ESS, hawks and doves earn the same: $W_D = (1 - p^*)V/2 = 0.6 \cdot 2 = 1.2$, which is the mean payoff. A population of doves would earn $V/2 = 2$ each. The ESS is not the group optimum; it is the state that no rare deviant can invade.

3. In the iterated donation game with $b = 5$, $c = 2$, what is the smallest probability of continuing interaction $w$ for which tit for tat resists invasion by always-defect? What is the expected number of rounds at that value?

   **Answer** $w > c/b = 0.4$; the expected number of rounds is $1/(1 - w) > 1/0.6 \approx 1.67$. Even a few repeated interactions suffice when the benefit is large relative to the cost.

4. Compute, for a haplodiploid species, the relatedness of a worker to her mother's sons and to the sons of a full-sister worker, and explain why worker policing is expected when queens mate multiply but not when they mate once.

   **Answer** A brother: $r = \tfrac14$. A full sister's son: a rare allele in the worker is in her full sister with probability $\tfrac34$ and passes to the sister's son with probability $\tfrac12$, so $r = \tfrac38$. With a singly mated queen, all workers are full sisters, so a worker is more related to her nephews ($\tfrac38$) than to her brothers ($\tfrac14$) and prefers workers to produce males: no policing. With many fathers, most workers are half sisters ($r = \tfrac14$), and a half-sister's son has $r = \tfrac18$, less than a brother; averaged over the colony, workers then prefer the queen's sons and are expected to destroy other workers' eggs, as observed in the honeybee.

5. Using the Price equation, show that if all groups have the same composition (no variation among groups), an altruistic trait cannot increase. What does this imply about the role of population structure?

   **Answer** If $Z_k$ is the same for all groups, $\operatorname{Cov}_k(W_k, Z_k) = 0$, and only the within-group term remains. Within each group, altruists pay the cost and share the benefit with everyone, so $\operatorname{Cov}_{i \in k}(w, z) < 0$; hence $\Delta\bar z < 0$. Altruism can increase only if groups differ in composition more than random sampling alone would produce, that is, if interacting individuals are positively correlated genetically. Population structure (kinship, limited dispersal, assortment) is therefore necessary, though, because it also increases competition among relatives, not sufficient.
