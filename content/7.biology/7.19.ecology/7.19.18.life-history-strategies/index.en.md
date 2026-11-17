---
title: Life History Strategies
description: "Life histories and life history strategies; the Darwinian demon, allocation and trade-offs, and why trade-offs are hidden by variation in acquisition (the Y model); reproductive effort, residual reproductive value, options sets and fitness contours in high and low cost-of-reproduction habitats; semelparity and iteroparity, terminal investment and age at maturity; offspring size and number, the Lack clutch size and its correction for the cost of reproduction; body size and phylogenetic constraints; r/K selection, Winemiller–Rose and CSR triangles and the fast–slow continuum; bet hedging and the evolution of senescence."
---

The demographic models of [7.19.9](/7.19.9)–[7.19.15](/7.19.15) take the schedules of survival and reproduction as given. Those schedules are themselves products of natural selection: when to start breeding, how much to invest in each bout of reproduction, how many offspring to make and how large, how long to live. This chapter asks why organisms differ in these respects, and how their life histories match the habitats in which they live. The evolutionary theory of life histories, with the Euler–Lotka equation, reproductive value, Hamilton's forces of selection, Cole's paradox and the Smith–Fretwell model, is developed in [7.10.15](/7.10.15), and the physiology and mechanisms of aging in [7.5.37](/7.5.37); we use their results and concentrate on the ecological side: how habitats shape the costs and benefits of reproduction, how life histories are classified, and what the classifications predict for population dynamics and conservation. Dormancy, migration and complex life cycles, which are life history strategies in time and space, follow in [7.19.19](/7.19.19), and the genetic measurement of populations in [7.19.20](/7.19.20).

## 18.1. Life Histories and Their Components

### 18.1.1. Life History Strategies

A **life history** ([Definition 15.1.1](/7.10.15#def-15.1.1) of 7.10.15) is the schedule of survival and reproduction of an organism from birth to death. A tapeworm such as *Taenia solium* shows how complicated it can be: eggs passed in the feces of a human host are eaten by a pig (or, accidentally, by a human), hatch in the intestine, penetrate the gut wall and travel in the blood to the muscles, where they develop into cysticerci; a human who eats undercooked infected pork becomes the host of the adult tapeworm, whose proglottids, each full of eggs, are released into the feces again. Each stage has its own mortality and its own requirements, and the life history is the whole sequence ([7.19.19](/7.19.19)).

**Definition 18.1.1 (Life History Strategy)** A **life history strategy** is the combination of life history traits (age and size at maturity, number, size and timing of offspring, reproductive effort, life span, and the timing of dormancy and movement) that has evolved in a population in response to the conditions of its habitat. It is often divided into a *reproductive strategy*, a *feeding* (foraging) strategy, a *movement* strategy and a *body-size* strategy.

"Strategy" does not imply conscious choice: a strategy is an inherited set of traits, or of rules for adjusting traits to conditions, that has been favored by selection. To see why life histories differ at all, imagine an organism free of constraints.

**Definition 18.1.2 (Darwinian Demon)** A **Darwinian demon** is a hypothetical organism that maximizes all components of fitness at once: it matures immediately after birth at a large adult size, produces many large offspring continually, and lives forever.

Darwinian demons do not exist, because resources are finite: energy and nutrients allocated to one function are not available for another. This principle of allocation is the source of the **trade-offs** ([7.10.3](/7.10.3)) between life history traits, and life history theory is the study of how trade-offs and the environment together determine the optimal combination of traits.

### 18.1.2. Allocation and Trade-offs

The simplest model of allocation is the *Y model*: an individual acquires an amount $A$ of resources and allocates a fraction $p$ to reproduction, $R = pA$, and the rest to survival, maintenance or growth, $S = (1 - p)A$. For a single individual, $R$ and $S$ trade off along the line $R + S = A$. Trade-offs have been documented in many ways:

- growth and reproduction: in Douglas fir (*Pseudotsuga menziesii*), years of heavy cone production are years of narrow growth rings; non-breeding female woodlice grow much more than breeding females;
- reproduction and survival: red deer hinds (*Cervus elaphus*) on the Isle of Rum that raised a calf had higher winter mortality than hinds that did not breed (Clutton-Brock et al. 1983);
- number and size of offspring: across clutches of many species of lizards and birds, larger clutches consist of smaller eggs (Section 18.4).

Yet across individuals of a population, reproduction and survival are often positively correlated: individuals in good condition, in good territories, both reproduce more and survive better. Van Noordwijk and de Jong (1986) showed that this is no contradiction.

**Proposition 18.1.1 (Acquisition and Allocation)** In the Y model, let $A$ and $p$ vary independently among individuals, with means $\mu_A, \mu_p$ and variances $\sigma_A^2, \sigma_p^2$. Then

$$
\operatorname{Cov}(R, S) = \mu_p(1 - \mu_p)\sigma_A^2 - \sigma_p^2\left(\sigma_A^2 + \mu_A^2\right),
$$
so the observed correlation of reproduction and survival is positive when variation in acquisition dominates, $\mu_p(1 - \mu_p)\sigma_A^2 > \sigma_p^2(\sigma_A^2 + \mu_A^2)$, and negative when variation in allocation dominates.

**Proof** By independence, $\mathbb{E}[RS] = \mathbb{E}[p(1 - p)]\,\mathbb{E}[A^2] = \bigl(\mu_p(1 - \mu_p) - \sigma_p^2\bigr)(\sigma_A^2 + \mu_A^2)$ and $\mathbb{E}[R]\,\mathbb{E}[S] = \mu_p(1 - \mu_p)\mu_A^2$. Subtracting gives the result. $\square$

The trade-off is a property of individuals, but correlations among individuals reveal it only if individuals differ more in how they allocate than in how much they acquire (Figure 1). This is why trade-offs are best demonstrated by experiments that manipulate allocation (adding eggs to clutches, removing flowers, hormone treatments), rather than by correlations in unmanipulated populations, and why trade-offs are often clearest in poor years, when differences in acquisition are small relative to the cost of reproduction.

![The Y model of acquisition and allocation (Proposition 18.1.1), 400 simulated individuals per panel. A: individuals differ mainly in the resources they acquire (coefficient of variation 0.4) and little in the fraction allocated to reproduction: reproduction and survival are positively correlated, although each individual faces a trade-off along its own line R + S = A (dashed, three examples). B: individuals differ mainly in allocation: the trade-off appears as a negative correlation. C: the correlation of R and S against the ratio of variation in acquisition to variation in allocation (points: simulation; line: the formula of Proposition 18.1.1)](./plots/acquisition-allocation.py)

## 18.2. Reproductive Effort and the Cost of Reproduction

### 18.2.1. Residual Reproductive Value

Every bout of reproduction has a **cost of reproduction** ([Definition 15.1.2](/7.10.15#def-15.1.2) of 7.10.15): it reduces survival, growth or future fecundity. The future contribution at stake is measured by **reproductive value** ([Definition 15.1.6](/7.10.15#def-15.1.6) of 7.10.15). For an individual of age $x$ about to breed, Fisher's reproductive value can be split into present and future parts,

$$
v_x = m_x + \sum_{y > x}\frac{l_y}{l_x}\lambda^{-(y - x)}m_y = m_x + p_x\frac{v_{x+1}}{\lambda},
$$
where $m_x$ is the present fecundity, $p_x = l_{x+1}/l_x$ the probability of surviving to the next breeding season and $\lambda$ the finite rate of increase. The second term is the *residual reproductive value*: the expected future reproduction of an individual that survives the present breeding attempt (Williams 1966). Reproduction is favored to the point at which a further increase of present fecundity $m_x$ costs as much in residual reproductive value as it gains. Reproductive value rises from birth to the age of first reproduction, as juveniles survive the dangerous early stages, and then declines with age; in the perennial phlox *Phlox drummondii*, for example, it peaks early in the reproductive season.

### 18.2.2. Options Sets and Fitness Contours

The trade-off between present reproduction and residual reproductive value can be represented geometrically (Sibly and Calow 1983). The *options set* is the set of combinations of present reproduction $b$ and future survival $s$ that an organism can achieve; its outer boundary is the trade-off curve. *Fitness contours* join combinations of equal fitness. With a census before breeding, an iteroparous individual that produces $b$ surviving offspring and survives with probability $s$ contributes $\lambda = b + Vs$ to the next census, where $V$ is the value of a surviving adult relative to a newborn. The fitness contours are therefore straight lines of slope $-1/V$, and the optimum is the point of the options set on the highest contour.

**Theorem 18.2.1 (Optimal Reproductive Effort)** Let the trade-off curve be $s = g(b)$, $0 \le b \le B$, with $g$ decreasing and twice differentiable, and let fitness be $\lambda(b) = b + Vg(b)$.

1. If the options set is convex outward ($g'' < 0$), $\lambda$ is concave and has a unique maximum; it lies in the interior $0 < b^* < B$, at the point where $g'(b^*) = -1/V$, whenever $g'(0) > -1/V > g'(B)$. The optimal reproductive allocation $b^*$ decreases as $V$ increases.
2. If the options set is concave outward ($g'' > 0$), $\lambda$ is convex and its maximum lies at an endpoint: either no present reproduction ($b = 0$) or maximal reproduction ($b = B$, followed by little or no survival: semelparity).

**Proof** $\lambda'(b) = 1 + Vg'(b)$ and $\lambda''(b) = Vg''(b)$. In case 1, $\lambda'$ decreases from $1 + Vg'(0) > 0$ to $1 + Vg'(B) < 0$, so it has a unique zero $b^*$, where $g'(b^*) = -1/V$; this is the tangency of the trade-off curve with a contour. Differentiating $g'(b^*) = -1/V$ with respect to $V$ gives $g''(b^*)\,\mathrm{d}b^*/\mathrm{d}V = 1/V^2$, and since $g'' < 0$, $\mathrm{d}b^*/\mathrm{d}V < 0$. In case 2, a convex function on an interval attains its maximum at an endpoint. $\square$

The value of a surviving adult, $V$, is what distinguishes habitats. Begon and colleagues call habitats in which present reproduction substantially reduces residual reproductive value *high CR* (high cost of reproduction): for example habitats with intense competition among adults, in which only large individuals breed successfully (red deer males), or with predators that take mainly small adults. In *low CR* habitats, residual reproductive value is little affected by present reproduction, either because adult mortality is high and indiscriminate (temporary ponds that dry out, regularly mown or trampled ground), or because the habitat is so benign that adults survive well whatever they do (newly colonized habitat). The classification is comparative. By Theorem 18.2.1, high CR habitats (shallow contours, large $V$) favor low reproductive allocation, delayed maturity and growth, whereas low CR habitats (steep contours) favor high allocation, early maturity and, with concave trade-offs, semelparity (Figure 2).

![Options sets and fitness contours (Theorem 18.2.1). Fitness λ = b + Vs, where b is present reproduction and s survival to the next season; contours (lines) are steep in a low cost-of-reproduction habitat (V = 1, red) and shallow in a high-CR habitat (V = 5, blue). A: with a convex-outward trade-off the optimum (points, where a contour touches the boundary) is intermediate and shifts toward higher reproduction in the low-CR habitat (from b/B = 0.62 to 0.97). B: with a concave-outward trade-off the optimum is at an extreme: no present reproduction in the high-CR habitat, all-out reproduction in the low-CR habitat. C: fitness along the trade-off curves against the reproductive allocation b/B](./plots/options-sets.py)

### 18.2.3. Evidence

Three populations of the dandelion *Taraxacum officinale* in Michigan, on a frequently trampled footpath (indiscriminate adult mortality: low CR), in an old undisturbed pasture with intense competition among adults (high CR) and at an intermediate site, consisted of clones belonging to four biotypes (Solbrig and Simpson 1974). The biotype that dominated the footpath made the largest reproductive allocation and the biotype that dominated the pasture the smallest, whichever site the plants came from. In a later experiment, dandelions kept for five years either in crowded multispecies swards or weeded out twice a year, so that they had to regrow from root stumps or seed, diverged in the direction predicted: plants from the weeded (low CR) treatment were smaller, flowered earlier, and produced more but smaller seeds when grown side by side.

The guppies (*Poecilia reticulata*) of Trinidad provide the best-known case ([7.10.15](/7.10.15)). In streams where the main predator is the cichlid *Crenicichla alta*, which takes guppies of all sizes and keeps their populations sparse, the habitat is low CR; where the main predator is the killifish *Rivulus hartii* (now *Anablepsoides hartii*), which takes mainly small juveniles, populations are crowded and growth to a large size pays (high CR). Guppies from cichlid sites mature earlier, at a smaller size, and make a larger reproductive allocation; 200 guppies transplanted from a cichlid site to a killifish site evolved the high-CR life history within 11 years, about 30–60 generations, and the differences persisted in the laboratory (Reznick et al. 1990). The killifish themselves show the same contrast among sites with and without other piscivorous fish (Walsh and Reznick 2008).

### 18.2.4. Reproductive Effort Over a Lifetime

As an organism ages, its residual reproductive value falls, so the cost of present reproduction falls with it and its fitness contours steepen: the *terminal investment hypothesis* (Williams 1966) predicts that reproductive effort should increase toward the end of life. Against this, aging individuals senesce and their options sets shrink, so that the absolute reproductive effort may fall. Both effects are found. Old male blue-footed boobies (*Sula nebouxii*) normally rear fewer fledglings than young males, but after an immune challenge that signals a shortened life they increased their reproductive success, whereas young males reduced it (Velando et al. 2006). In reindeer (*Rangifer tarandus*), calf birth mass declined from about 5.5 years of age to the end of life, a sign of senescence rather than terminal investment (Weladji et al. 2010), and Californian oaks showed neither effect in their final years (Koenig et al. 2017).

Age at maturity follows the same logic: delayed maturity is favored where growth increases future fecundity or survival (high CR) and where adult survival is high relative to juvenile survival. The semelparous lobelia *Lobelia inflata* in Canada flowers once and dies, the end of flowering being set by the first frosts in October. Plants experimentally germinated later in the season, with less time ahead of them and hence a lower cost of reproduction, started flowering sooner and at a smaller size and compressed their reproduction into a shorter, more intense burst, although their total output was similar (Hughes and Simons 2014): semelparity and iteroparity form a continuum.

## 18.3. Semelparity and Iteroparity

**Semelparity** and **iteroparity** ([Definition 15.3.1](/7.10.15#def-15.3.1) of 7.10.15) differ in the timing of reproductive effort: a single, terminal bout of reproduction, or repeated bouts with continued investment in survival. Annual plants of arable fields, Pacific salmon (*Oncorhynchus*), agaves and many bamboos, which flower synchronously after decades of clonal growth and then die, are semelparous; most perennial plants, birds and mammals are iteroparous. The distinction does not coincide with life span: the groundsel *Senecio vulgaris* is an iteroparous annual that flowers continuously until killed by frost, and the white sweet clover *Melilotus albus* is a strict biennial that dies after flowering in its second summer.

Cole (1954) observed that an annual would grow as fast as a perennial if it produced just one more offspring per year, and asked why perennials exist at all. The resolution (Charnov and Schaffer 1973; [Theorem 15.3.1](/7.10.15#thm-15.3.1) of 7.10.15) is that semelparity is favored only if the annual's fecundity $B_a$ exceeds the perennial's $B_p$ by more than $p/c$, where $p$ is adult and $c$ juvenile survival. Two numerical examples show how strongly the ratio of survival rates matters:

**Example 18.3.1** A perennial herb produces $B_p = 50$ seeds a year; a seed becomes a breeding adult with probability $c = 0.02$, and adults survive the winter with probability $p = 0.8$. Its finite rate of increase is $\lambda_p = cB_p + p = 1.8$. An annual with the same juvenile survival must produce $B_a > B_p + p/c = 50 + 40 = 90$ seeds to grow faster. If instead juvenile survival is high, $c = 0.5$, and adult survival low, $p = 0.2$, then $p/c = 0.4$ and an annual producing one more seed than the perennial wins.

:::

In the options-set picture, semelparity is favored when the trade-off is concave outward (Theorem 18.2.1, case 2): when any reproduction at all carries a large, fixed cost, so that further increases in reproduction cost little additional survival. Salmon illustrate this: the dangerous upstream migration to the spawning grounds and the physiological changes that accompany it are costs that do not depend on how many eggs a female lays, and once paid, all-out reproduction is optimal. In fluctuating environments, iteroparity is also a way of spreading risk across years, a form of bet hedging (Section 18.7): if adults survive well but recruitment fails in some years, a perennial that reproduces repeatedly is less likely to lose all its reproduction to one bad year.

## 18.4. The Size and Number of Offspring

### 18.4.1. Offspring Size

For a given reproductive allocation, a parent can make many small offspring or a few large ones. The Smith–Fretwell model ([Theorem 15.3.2](/7.10.15#thm-15.3.2) of 7.10.15) predicts the optimal size $s^*$ from the tangent to the curve of offspring fitness $f(s)$ through the origin, independently of the total resources available. The shape of $f$ depends on the habitat: in *offspring-size-insensitive* habitats, where mortality of young is indiscriminate or resources superabundant, $f$ saturates at small sizes and many small offspring are favored; in *offspring-size-sensitive* habitats, where young compete or are vulnerable to size-selective mortality, large offspring are favored. Guppies from killifish sites (crowded, high competition) produce larger young than those from cichlid sites, and in experimental tanks at high density the smallest newborns, especially those from high-competition populations, grew most slowly. The annual speedwell *Veronica peregrina* in vernal pools in California produces fewer, heavier seeds in the crowded, stable center of a pool and more, lighter seeds at its unstable margins (Linhart 1974).

Large offspring can also become a trap when the environment changes. New Zealand kiwis (*Apteryx*) lay a single egg about six times as large as that of a hen of similar size, an adaptation to a habitat without mammalian predators. Introduced stoats (*Mustela erminea*) now kill most eggs and chicks on the mainland, and no egg size would make the chicks safe. *Operation Nest Egg* takes eggs from the wild and rears the chicks in crèches until they weigh about 1200 g and are safe from stoats; survival of brown kiwis (*A. mantelli*) to six months rose to 81 %, compared with 11 % in unmanaged populations and about 20 % needed for population persistence (Colbourne et al. 2005).

### 18.4.2. Clutch Size

Lack (1947), working on birds, proposed that clutch size is not the largest a female can lay but the one that yields the greatest number of surviving young, because parents cannot feed large broods adequately. The survival of each nestling, $s(n)$, decreases with brood size $n$, and the number of recruits $ns(n)$ is maximal at an intermediate **Lack clutch size**. Lack also explained the asynchronous hatching of many birds, in which the parents preferentially feed the first-hatched, largest chicks, as an adaptation that matches brood size to food supply: in bad years the youngest chicks die quickly (brood reduction) rather than all chicks starving slowly.

Experimental manipulations of clutch size have often found that enlarged broods fledge more young than natural ones (by 0.55 eggs on average in a meta-analysis; Vander Werf 1992), apparently contradicting Lack. Two corrections resolve most of the discrepancy. First, fledging is not recruitment: in a long-term study of great tits (*Parus major*) near Oxford, nests with added eggs fledged 10.96 young on average, control nests 8.68 and nests with eggs removed 5.68, but the number of young recruited as breeding adults was highest from unmanipulated nests. Second, Lack's argument ignores the cost of reproduction to the parents.

**Proposition 18.4.1 (Clutch Size with a Cost of Reproduction)** Let each of $n$ young survive to breed with probability $s(n) = s_0(1 - n/N)$, and let the parent survive to breed again with probability $P(n) = P_0 - cn$, a surviving parent being worth $V$ recruits. The Lack clutch size, which maximizes $ns(n)$, is $n_{\mathrm{L}} = N/2$. The clutch size that maximizes total fitness $W(n) = ns(n) + VP(n)$ is

$$
n^* = \frac{N}{2}\left(1 - \frac{cV}{s_0}\right) < n_{\mathrm{L}} .
$$

**Proof** $W'(n) = s_0(1 - 2n/N) - cV$ and $W''(n) = -2s_0/N < 0$, so $W$ is maximal where $1 - 2n/N = cV/s_0$. Setting $c = 0$ gives the Lack clutch. $\square$

The optimal clutch is smaller than the Lack clutch by an amount proportional to the cost per egg and to the residual reproductive value of the parent: long-lived species with high adult survival should lay fewer eggs than the number that would maximize their present success (Figure 3). Experiments with bank voles (*Myodes glareolus*) treated with gonadotropins to produce larger litters confirm the cost: treated females weaned more young, but suffered higher mortality during nursing, gained less mass and were less likely to produce another litter (Oksanen et al. 2002). In Eurasian lynx (*Lynx lynx*) in Sweden and Norway, followed for 7–13 years with radio collars, litters of two were both the most common and the most productive, whatever the mass and experience of the female, close to the simple Lack prediction.

Clutch size also varies geographically. Birds of temperate regions lay larger clutches than related tropical species, and mammals of high latitudes have larger litters; explanations include the longer days and seasonal flush of food available for feeding young at high latitudes, the higher adult survival (and hence larger $V$) of many tropical birds, and higher nest predation in the tropics, which favors smaller clutches and more breeding attempts.

![Lack's clutch size and the cost of reproduction (Proposition 18.4.1). A: the survival of each nestling, s(n) = s₀(1 − n/N), and the survival of the parent, P(n) = P₀ − cn, decline with clutch size (s₀ = 0.5, N = 16, P₀ = 0.6, c = 0.04). B: recruits per brood ns(n) are maximal at the Lack clutch size 8; adding the value V = 2 of a surviving parent, total fitness is maximal at 6.7 eggs. C: the optimal clutch size falls with the residual reproductive value V of the parent, the more steeply the larger the cost c per egg](./plots/lack-clutch.py)

## 18.5. Body Size, Allometry and Phylogeny

Body size is the most obvious life history trait and is correlated with almost all others. Across organisms from bacteria to whales, generation time, life span and age at maturity scale roughly as $M^{1/4}$ and the maximum per capita rate of increase $r_{\max}$ as $M^{-1/4}$, consequences of the scaling of metabolic rate ([7.19.6](/7.19.6)): whole-body metabolic rate scales approximately as $M^{3/4}$ (Kleiber's rule), so metabolic rate per unit mass falls as $M^{-1/4}$, the "mouse-to-elephant curve" of mass-specific oxygen consumption, from shrews and harvest mice to dogs, humans and elephants. Small organisms have high mass-specific metabolic rates, short lives and high $r_{\max}$; large ones live long, mature late and grow slowly as populations (Southwood 1976). Large size brings competitive ability, lower predation risk and buffering against fluctuations; small size brings short generations, rapid population growth and, over evolutionary time, rapid adaptation.

Because so many traits scale with size, comparisons of life histories must be made relative to the allometric relationship. In salamanders, clutch volume scales allometrically with body volume across 74 species. Two species of *Ambystoma*, *A. tigrinum* and *A. opacum*, have the same ratio of clutch to body volume (13.6 %), which would suggest that they do not differ; but *A. opacum* lies on the general salamander relationship, whereas *A. tigrinum*, being larger, has a clutch almost twice as large as expected for its size (Kaplan and Salthe 1979). The ecologically interesting difference is the deviation from the allometry.

Life histories are also constrained by phylogeny. All albatrosses, petrels and shearwaters (Procellariiformes) lay a single egg and have a single brood patch with which to incubate it; a larger clutch would require concurrent changes in many developmental processes. In mammals, a nested analysis of variance of seven life history traits found that only 3–11 % of the variance lay between species within genera, whereas 55–71 % lay between orders (Read and Harvey 1989): comparing two species from different orders is in effect comparing the orders. Comparative studies therefore use methods that account for shared ancestry, such as phylogenetically independent contrasts and phylogenetic regression ([7.10.26](/7.10.26)).

## 18.6. Classifying Life Histories

### 18.6.1. r- and K-Selection

The most influential classification is that of **r-selection** and **K-selection** ([Definition 15.2.1](/7.10.15#def-15.2.1) of 7.10.15), proposed by MacArthur and Wilson (1967) and elaborated by Pianka (1970). It contrasts populations kept below **carrying capacity** by frequent density-independent mortality in unpredictable or ephemeral habitats with crowded populations near carrying capacity in stable habitats.

| Feature | r-selection | K-selection |
|---|---|---|
| habitat | variable, unpredictable, short-lived | constant or predictable |
| mortality | often catastrophic, density independent | density dependent |
| population size | variable, often below $K$ | near $K$, fairly constant |
| competition | weak, variable | intense |
| development | rapid | slow |
| maturity | early | late |
| body size | small | large |
| reproduction | often semelparous, high allocation | iteroparous, low allocation |
| offspring | many, small, little care | few, large, much care |
| life span | short, usually under a year | long, more than a year |
| leads to | productivity | efficiency |

In the terms of Section 18.2, an r-selecting habitat is both low CR and offspring-size insensitive, a K-selecting habitat both high CR and offspring-size sensitive. Species near the r end recover quickly from losses, disperse well and are typical of early successional stages and of pests; species near the K end are good competitors with stable populations, but when reduced they recover slowly, so large K-selected mammals such as elephants, tigers and giant pandas are particularly vulnerable to overexploitation ([7.19.15](/7.19.15), [7.19.53](/7.19.53)). In the logistic picture, a K-strategist's population has a stable equilibrium near $K$ and an extinction threshold at low density (an Allee effect), whereas an r-strategist's population can recover from very low densities but fluctuates widely.

The scheme is a comparison, not an absolute classification, and it explains perhaps half of the observed patterns: reviews since Stearns (1977) found roughly equal numbers of studies that conformed to it and contradicted it. The periwinkle *Littorina saxatilis* on British shores shows why. In populations living in rock crevices, which protect the snails from waves and predators but offer limited space and intense competition, snails are small and thin-shelled, mature early with a high reproductive allocation, but produce few large young; in populations on boulder shores, where small snails are crushed at random by moving boulders but large, thick-shelled adults are safe, snails grow large before maturing, have a low reproductive allocation and produce many small young (Hart and Begon 1982). Neither population fits r or K: the crevice population combines "r" adult traits with "K" offspring, as expected from a habitat that is low CR for adults but offspring-size sensitive. Mortality that depends on size, rather than density, is the driving force, and the scheme is best regarded as a special case of the demographic theory of Section 18.2 and of [7.10.15](/7.10.15).

### 18.6.2. Triangular Schemes

Two classifications with three corners replace the dichotomy. For fishes, Winemiller and Rose (1992) found that life histories lie in a triangle in the space of age at maturity, fecundity and juvenile survival (Figure 4C): opportunistic species (small, early-maturing fishes with small clutches and repeated spawning, which can colonize habitats repeatedly disturbed), periodic species (large, late-maturing fishes with enormous fecundity and low juvenile survival, such as cod and sturgeons, which exploit large-scale and periodic variation, for example good recruitment years), and equilibrium species (late-maturing fishes with few large young and parental care or live birth, such as many sharks, which do well in stable, resource-limited environments).

For plants, Grime (1974, 1979) classified habitats by two forces: *stress*, conditions that limit production (shortage of light, water or nutrients, low temperature), and *disturbance*, the destruction of plant biomass (grazing, trampling, mowing, fire, frost). Three of the four combinations support plants (Figure 4A).

**Definition 18.6.1 (CSR Triangle)** Grime's **CSR triangle** classifies plant strategies by the relative importance of three primary strategies: *competitors* (C), selected in productive, rarely disturbed habitats, with rapid growth, tall stature, lateral spread and high resource capture; *stress tolerators* (S), selected in unproductive habitats with little disturbance, with slow growth, long-lived tissues and conservative use of resources; and *ruderals* (R), selected in productive but frequently disturbed habitats, with short lives, rapid growth and high allocation to seeds. Every species is placed in the triangle by the proportions of the three strategies; intermediate strategies (CR, CS, SR, CSR) lie between the corners.

Ruderals resemble r-strategists, competitors share features of K-strategists (more growth than reproduction), and stress tolerators have no equivalent in the r/K scheme: they invest in tolerating harsh conditions rather than in holding ground against competitors. Pierce et al. (2017) placed 3068 vascular plant species worldwide in the triangle using three leaf traits: leaf area, which separates competitors (large leaves) from the rest, and specific leaf area and leaf dry matter content, which separate the acquisitive leaves of ruderals (high SLA, low LDMC) from the conservative leaves of stress tolerators. Tropical and subtropical moist forests were dominated by CS strategies with few ruderals, whereas Mediterranean shrublands spanned the triangle. In Denmark, plants that were absent from much of their potentially suitable habitat ("dark diversity") tended to be ruderal, stress-intolerant species of low-light, low-nutrient habitats and poor dispersers, suggesting that restoring bare ground for germination would help them (Moeslund et al. 2017).

![Triangular classifications of life histories (schematic). A: Grime's classification of plant habitats by stress and disturbance: three combinations select the competitive (C), stress-tolerant (S) and ruderal (R) strategies; habitats with both severe stress and frequent disturbance support no plants. B: the CSR triangle: species are placed by the relative importance of the three strategies; intermediate types lie between the corners. C: Winemiller and Rose's triangle for fishes, defined by age at maturity, fecundity and juvenile survival, with the opportunistic, periodic and equilibrium strategies at its corners](./plots/strategy-triangles.py)

### 18.6.3. The Fast–Slow Continuum

**Definition 18.6.2 (Fast–Slow Continuum)** The *fast–slow continuum* (Stearns 1983) is the main axis of covariation of life history traits across species: from "fast" life histories, with early maturity, high fecundity, short generation time and short life, to "slow" ones, with late maturity, low fecundity, long generation time and long life, in which allocation shifts from reproduction to survival.

The continuum is related to the r/K scheme but differs from it in two respects: it is derived empirically from the covariation of traits, typically by principal component or factor analysis, rather than postulated from habitat types, and habitat correlates are sought only afterward. In 418 plant species, the first axis of variation among their demographic traits (from matrix population models, [7.19.14](/7.19.14)) was a fast–slow continuum, and a second, independent axis described reproductive strategy: the degree of iteroparity and the spreading of reproduction over time (Salguero-Gómez et al. 2016). In mammals, a fast–slow factor (age at weaning, age at maturity, interbirth interval) and a factor for offspring size and number (neonatal mass, gestation length and litter size) together explained 53–78 % of the variation in different groups (Bielby et al. 2007).

Position on the continuum predicts how a population responds to perturbation, which is the main reason for its use in conservation. In sharks, elasticity analyses of 41 populations of 38 species showed that "fast" species such as the bonnethead (*Sphyrna tiburo*) can compensate for a 10 % decrease in adult or juvenile survival by increased fecundity, whereas large, slow species such as the bull shark (*Carcharhinus leucas*) cannot (Cortés 2002); of the world's skates, the few species that have suffered local extinctions are among the largest (Dulvy and Reynolds 2002), and the mammals that have gone extinct in Australia in the last two centuries are concentrated in intermediate to large body sizes. For slow species, population growth is most sensitive to adult survival ([7.19.14](/7.19.14)), and conservation must focus on it.

## 18.7. Bet Hedging

In a variable environment, the fitness of a genotype is not its mean rate of increase. If a lineage multiplies by $\lambda_t$ in year $t$, its size after $T$ years is $N_0\prod_t\lambda_t$, and its long-run growth rate is the geometric mean of the $\lambda_t$ (Theorem 15.2.1 of [7.19.15](/7.19.15#thm-15.2.1)):

$$
\lim_{T\to\infty}\frac1T\ln\frac{N_T}{N_0} = \mathbb{E}[\ln\lambda] \le \ln\mathbb{E}[\lambda],
$$
by Jensen's inequality, with a deficit approximately $\operatorname{Var}(\lambda)/(2\mathbb{E}[\lambda]^2)$ for small variation. Reducing the variance of fitness across years can therefore raise long-run fitness even at the cost of a lower mean, which is the principle of **bet hedging** ([Definition 17.1.2](/7.9.17#def-17.1.2) of 7.9.17).

**Example 18.7.1** In a habitat where good and bad years occur with equal probability, a genotype that breeds all at once multiplies by 3 in good years and by 0.1 in bad years: arithmetic mean 1.55, geometric mean $\sqrt{0.3} = 0.55$, so it declines. A genotype that spreads its reproduction so as to multiply by 1.6 in good years and 0.8 in bad ones has a lower arithmetic mean, 1.2, but a geometric mean $\sqrt{1.28} = 1.13$, and increases.

:::

Bet hedging is *conservative* when a genotype adopts a single low-risk phenotype (smaller clutches than the Lack clutch in variable environments, iteroparity) and *diversified* when it produces a spread of phenotypes, of which some will do well whatever happens: seeds that germinate in different years (the seed bank model of [7.19.19](/7.19.19)), offspring of different sizes, or eggs laid in several places. Iteroparity spreads reproduction across years, and in a variable environment it can be favored even when Cole's criterion favors semelparity in a constant one (Orzack and Tuljapurkar 1989). Bet hedging must be distinguished from *adaptive plasticity*, in which individuals sense the environment and respond (for example by adjusting clutch size to food supply): bet hedging is the strategy for environments that cannot be predicted from available cues.

## 18.8. The Evolution of Senescence

**Aging** ([Definition 37.1.1](/7.5.37#def-37.1.1) of 7.5.37), the decline of survival and fecundity with age, is a life history trait, and its evolution follows from Hamilton's result that the force of selection on survival and fecundity declines after the age of first reproduction ([Theorem 15.1.2](/7.10.15#thm-15.1.2) of 7.10.15). Even without aging, an individual's chance of being alive declines with age because of extrinsic mortality (predation, accidents, disease), so mutations that act late in life affect fewer individuals and are less strongly selected. Two genetic mechanisms follow ([Definition 37.2.1](/7.5.37#def-37.2.1) of 7.5.37): **mutation accumulation** (Medawar 1952), the accumulation of deleterious mutations whose effects appear only late in life, and **antagonistic pleiotropy** (Williams 1957), the spread of alleles that benefit early reproduction at the cost of later survival. The *disposable soma* theory (Kirkwood 1977) is the life history version of antagonistic pleiotropy: resources allocated to reproduction are not available for maintenance and repair, so the optimal investment in somatic maintenance is less than that required to avoid aging, the more so the higher the extrinsic mortality.

The central ecological prediction is that populations exposed to high extrinsic mortality evolve faster aging. Virginia opossums (*Didelphis virginiana*) on Sapelo Island, Georgia, isolated for about 4500 years from mainland predators, age more slowly than mainland opossums: they live longer, reproduce for a second year more often, and their tendon collagen ages more slowly (Austad 1993). Flying, which reduces predation, is associated with long life: bats and birds live much longer than terrestrial mammals of the same size. But the prediction is not universal. Guppies from high-predation sites did not age faster than those from low-predation sites; they maintained reproduction and survival to later ages under laboratory conditions (Reznick et al. 2004), probably because predation also selects for physiological performance that slows aging, and because mortality that falls on particular ages or conditions changes the force of selection in more complex ways than uniform extrinsic mortality (Abrams 1993). Many modular organisms, such as clonal plants and some trees, show little or no senescence of the whole organism, because the meristems are continually renewed ([7.19.8](/7.19.8)).

## Summary

- A life history strategy (Definition 18.1.1) is the set of traits evolved in response to a habitat. No Darwinian demon (Definition 18.1.2) exists, because allocation creates trade-offs; correlations among individuals can hide them when acquisition varies more than allocation (Proposition 18.1.1).
- Reproduction is weighed against residual reproductive value. With options sets and fitness contours (Theorem 18.2.1), high cost-of-reproduction habitats favor low allocation and delayed maturity, low-CR habitats high allocation, and concave trade-offs semelparity (dandelion biotypes, Trinidad guppies, *Lobelia*). Terminal investment and senescence compete late in life (boobies, reindeer).
- Semelparity requires $B_a > B_p + p/c$ (Example 18.3.1): high juvenile and low adult survival, or a large fixed cost of reproduction (salmon).
- Offspring size depends on how strongly offspring fitness depends on size (guppies, *Veronica*, kiwi). The Lack clutch is reduced by the cost of reproduction to $n^* = n_{\mathrm{L}}(1 - cV/s_0)$ (Proposition 18.4.1; great tits, bank voles, lynx).
- Body size sets many traits allometrically (times $\propto M^{1/4}$, $r_{\max} \propto M^{-1/4}$), and phylogeny constrains them; comparisons must use deviations from allometries and phylogenetic methods.

| Scheme | Axes | Types |
|---|---|---|
| r/K | density, habitat stability | r: fast, many small young; K: slow, few large young |
| Winemiller–Rose (fish) | maturity, fecundity, juvenile survival | opportunistic, periodic, equilibrium |
| CSR (plants, Definition 18.6.1) | stress, disturbance | competitor, stress tolerator, ruderal |
| fast–slow (Definition 18.6.2) | empirical first axis | fast to slow; second axis reproductive strategy |

- In variable environments, fitness is the geometric mean growth rate, and bet hedging (Example 18.7.1) trades mean for variance.
- Senescence evolves because the force of selection declines with age (mutation accumulation, antagonistic pleiotropy, disposable soma); high extrinsic mortality usually, but not always, accelerates it (Sapelo opossums, guppies).

## Questions

1. Use the Y model to explain why a field study finds that female birds that lay larger clutches also survive better, and design an experiment that would reveal the cost of reproduction.

   **Answer** By Proposition 18.1.1, if females differ mostly in the resources they acquire (territory quality, age, condition), both clutch size and survival increase with acquisition, and the covariance is positive even though each female trades one against the other. The cost is revealed by manipulating allocation independently of acquisition: add or remove eggs (or nestlings) at random among females and compare the subsequent survival and future reproduction of females with enlarged, control and reduced broods. Randomization breaks the link with condition, so differences in survival are caused by the manipulation; measuring recruitment of the young as well as parental survival gives the total fitness consequence.

2. For the trade-off curve $s = \sqrt{1 - (b/B)^2}$ and fitness $\lambda = b + Vs$, find the optimal reproductive allocation as a function of $V$ and $B$, and check the values of Figure 2A.

   **Answer** Let $x = b/B$. Then $\lambda = Bx + V\sqrt{1 - x^2}$ and $\mathrm{d}\lambda/\mathrm{d}x = B - Vx/\sqrt{1 - x^2} = 0$ gives $x/\sqrt{1 - x^2} = B/V$, so $x^* = B/\sqrt{B^2 + V^2}$. For $B = 4$: $V = 5$ gives $x^* = 4/\sqrt{41} = 0.62$, and $V = 1$ gives $x^* = 4/\sqrt{17} = 0.97$, as in the figure. The allocation decreases as the value of a surviving adult increases (Theorem 18.2.1).

3. In Proposition 18.4.1 with $s_0 = 0.5$, $N = 16$ and $c = 0.04$, how large must the residual reproductive value $V$ be for the optimal clutch to be half the Lack clutch? Interpret this for short-lived and long-lived birds.

   **Answer** $n^* = n_{\mathrm{L}}/2$ requires $cV/s_0 = 1/2$, i.e. $V = s_0/(2c) = 6.25$ recruits. A short-lived passerine, whose future reproduction is worth little relative to the present brood (small $V$), should lay close to the Lack clutch; a long-lived seabird, with many future breeding seasons (large $V$), should lay far fewer eggs than it could raise in one season, so as not to jeopardize its own survival. This is consistent with the small clutches of long-lived birds such as albatrosses (where phylogenetic constraint also acts).

4. Classify the following by the CSR scheme and justify: (a) a lichen on alpine rock; (b) an annual weed of cultivated fields; (c) a tall clonal perennial such as stinging nettle on nutrient-rich river banks; (d) a plant of trampled paths that grows in rosettes.

   **Answer** (a) S: severe stress (cold, drought, few nutrients), little disturbance; slow growth, long-lived thalli. (b) R: productive but repeatedly disturbed habitat; short life, rapid growth, high seed output and a persistent seed bank. (c) C: productive, rarely disturbed habitat; tall, laterally spreading, rapid resource capture. (d) Intermediate, roughly SR or CR depending on nutrients: disturbance by trampling is frequent, and the rosette habit tolerates damage; plants of paths are usually placed toward R with some S. The exercise shows that most species lie away from the corners.

5. Explain with Example 18.7.1 why a genotype with a higher arithmetic mean fitness can lose to one with a lower mean. What would happen to the comparison if the environment were the same every year?

   **Answer** Long-run growth is the product of yearly factors, so it is governed by the geometric mean (the mean of $\ln\lambda$); a single bad year with $\lambda = 0.1$ cancels the gains of more than two good years with $\lambda = 3$. The risk-spreading genotype has a lower arithmetic mean (1.2 versus 1.55) but a higher geometric mean (1.13 versus 0.55). In a constant environment, the geometric and arithmetic means coincide, so the genotype with the higher $\lambda$ in that environment wins: in good years only, the all-at-once genotype (3) beats the risk-spreader (1.6), and in bad years only, the risk-spreader wins. Bet hedging is favored only by unpredictable variation.

6. (Open question) The giant panda is often described as a K-strategist. Discuss whether this label is useful for its conservation, and which more specific life history information would be needed.

   **Answer** Key points: pandas have late maturity (about 4–7 years), small litters (usually one surviving cub), long interbirth intervals, high adult survival and long lives, so they lie at the slow end of the fast–slow continuum; the K label correctly predicts slow recovery from losses and high sensitivity of population growth to adult survival. But the label adds little beyond these demographic facts and hides the important specifics: the elasticities of $\lambda$ to adult and juvenile survival and to fecundity ([7.19.14](/7.19.14)), the dependence on bamboo and the risk of synchronous bamboo flowering, the fragmentation of populations into small units subject to demographic and genetic stochasticity ([7.19.15](/7.19.15), [7.19.20](/7.19.20)), and the role of habitat corridors. Useful conservation planning needs a stage-structured matrix model with estimated vital rates, a population viability analysis and spatial habitat data, not a category.
