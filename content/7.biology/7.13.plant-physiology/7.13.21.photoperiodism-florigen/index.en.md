---
title: Photoperiodism and Florigen
description: The discovery of photoperiodism (Garner and Allard and the Maryland Mammoth tobacco); the astronomical day-length formula and the annual course of day length at different latitudes; long-day, short-day, day-neutral and dual-day-length plants, qualitative and quantitative responses, the critical day length; the decisive role of the dark period, the critical night length, night breaks and red/far-red reversibility; photoperiodic induction and leaf perception; the hourglass model, Bünning's clock hypothesis and the external coincidence model, CO–FT in Arabidopsis and Hd1–Hd3a in rice with a numerical simulation; temperature sensing; florigen from grafting experiments to the FT protein; photoperiod and geographic distribution, introduction of crops, off-season breeding and control of flowering time
source_hash: bca7d4777ca0
---

When a plant flowers determines whether it can pollinate and set seed in the most favorable season, and whether it flowers in synchrony with other individuals of its species so that outcrossing is possible. A plant can neither "read" a calendar nor consult a thermometer; the most reliable seasonal signal available to it is day length. At a given latitude the day length on a given date is the same every year, whereas temperature fluctuates strongly from year to year. This chapter discusses how plants measure day length and how the day-length signal measured in the leaf is converted into a command to flower at the shoot apex.

Photoperiod was one of the first environmental signals studied quantitatively in plant physiology. We first describe its discovery and the types of photoperiodic response (Sections 21.1 and 21.2), then ask whether it is the light period or the dark period that decides flowering (Section 21.3) and how the leaf perceives and "remembers" the photoperiod (Section 21.4). Next we discuss the timing mechanism, from the historical hourglass model to today's external coincidence model built from the circadian clock and photoreceptors (Section 21.5), and use an ordinary differential equation model to show how long-day and short-day plants obtain opposite responses from the same molecular parts. Section 21.6 traces florigen from a hypothetical substance in grafting experiments to the FT protein, and Section 21.7 treats photoperiod in relation to geographic distribution, the introduction of crops and the control of flowering time. The molecular properties of the photoreceptors (**phytochrome**, **cryptochrome**) are covered in [7.6.18](/7.6.18) and [7.13.16](/7.13.16), and the dynamics of the circadian clock in [7.6.33](/7.6.33#sec-33.6.1). The effects of low temperature (vernalization), plant age and hormones on flowering, and the integration of the flowering pathways, are the subject of the next chapter, [7.13.22](/7.13.22); floral organ morphology and the ABC model are covered in [7.12.27](/7.12.27).

## 21.1. The Discovery of Photoperiodism

### 21.1.1. Maryland Mammoth Tobacco

Around 1906, tobacco growers in Maryland noticed a mutant in their fields of tobacco (*Nicotiana tabacum*). Ordinary tobacco flowers after producing about twenty leaves, but the mutant continued vegetative growth, producing more than a hundred leaves and reaching a height of three to five meters, and did not flower until it was killed by the first frosts of early winter; only plants moved into a greenhouse for the winter flowered and set seed. This line later became known as "Maryland Mammoth." It has many leaves and a high yield, but no seed can be harvested from it in the field.

W. W. Garner and H. A. Allard at the Beltsville station of the US Department of Agriculture tested temperature, nutrition, humidity and other conditions, none of which made the plant flower in summer. They then moved summer field plants into a dark room every afternoon, artificially shortening the day, and the plants flowered promptly. Conversely, plants grown in a greenhouse in winter did not flower if the day was extended with lamps. A soybean cultivar sown in summer (Biloxi) behaved similarly: whenever it was sown, it flowered at the same time of year, when day length had decreased to a certain value. Garner and Allard reported these results in 1920 and proposed that day length is the main environmental factor controlling flowering.

**Definition 21.1.1 (Photoperiodism)** The alternation of light and dark periods within a 24-hour cycle is called the photoperiod; the response of the growth and development of an organism to changes in day length (or night length) is called **photoperiodism**.

Photoperiodism is not limited to flowering, nor to plants:

- Flowering: the best studied case and the subject of this chapter.
- Formation of storage organs: potato tubers form under short days, onion bulbs under long days, and the tuberous roots of dahlia under short days.
- Dormancy and leaf fall: temperate woody plants stop growing, form dormant buds and shed their leaves under the shortening days of autumn ([7.13.24](/7.13.24)).
- Vegetative propagation and morphology: strawberry produces runners under long days; photoperiod also affects branching, leaf shape and sex expression ([7.13.22](/7.13.22)).
- Animals: bird migration and reproduction, insect diapause and the molting of mammals are also controlled by day length.

### 21.1.2. Natural Variation of Day Length

Photoperiodism is reliable because day length is determined precisely by astronomy. Let $\phi$ be the latitude of a place and $\delta$ the declination of the sun (the latitude of the subsolar point: $+23.44^\circ$ at the summer solstice, $-23.44^\circ$ at the winter solstice and $0$ at the equinoxes). The hour angle $H_0$ of the sun at sunrise and sunset satisfies

$$
\cos H_0 = \frac{\sin h_0 - \sin\phi\sin\delta}{\cos\phi\cos\delta},
\qquad N = \frac{2H_0}{15^\circ}\ \mathrm{h}.
\tag{21.1}
$$

Here $h_0$ is the altitude of the center of the sun at sunrise and sunset, and $N$ is the day length (the Earth turns $15^\circ$ per hour). Taking $h_0 = 0$ (the sun treated as a point, atmospheric refraction ignored) gives the familiar simplified formula $\cos H_0 = -\tan\phi\tan\delta$. In meteorology sunrise is defined by the upper limb of the sun touching the horizon and refraction is included, giving $h_0 = -0.833^\circ$; if civil twilight is counted (the sun less than $6^\circ$ below the horizon, when the sky still has enough scattered light), $h_0 = -6^\circ$. The declination depends on the day of the year $d$ (1 January is $d = 1$) approximately as

$$
\delta \approx -23.44^\circ \cos\left[\frac{360^\circ}{365}(d + 10)\right].
\tag{21.2}
$$

**Example 21.1.1** Find the day length in Beijing ($\phi = 39.9^\circ$) at the summer solstice.

At the summer solstice $\delta = 23.44^\circ$. With the simplified formula: $\tan 39.9^\circ = 0.836$, $\tan 23.44^\circ = 0.433$, $\cos H_0 = -0.362$, $H_0 = 111.3^\circ$, and $N = 2 \times 111.3/15 = 14.8\ \mathrm{h}$. Including refraction and the radius of the solar disk ($h_0 = -0.833^\circ$) gives $15.0\ \mathrm{h}$, and including civil twilight ($h_0 = -6^\circ$) gives $16.1\ \mathrm{h}$. By the same method the day length at the winter solstice is $9.3\ \mathrm{h}$ (with twilight, $10.4\ \mathrm{h}$).

Which of these values matters to plants? The light intensity required for photoperiodic responses is very low (many plants respond to a few $\mu\mathrm{mol\,m^{-2}\,s^{-1}}$, far below the light compensation point of photosynthesis), and part of the twilight is counted as light period, so the effective day length perceived by plants is usually $0.5$–$1\ \mathrm{h}$ longer than the astronomical day length. This difference must be kept in mind when critical day lengths measured in growth chambers are applied in the field.

:::

Equation (21.1) yields several regularities (Figure 1):

1. At the equinoxes $\delta = 0$ and day and night are equal everywhere (about $12\ \mathrm{h}$).
2. In the summer half-year (equinox to equinox) the higher the latitude the longer the day, and in the winter half-year the higher the latitude the shorter the day. The annual amplitude of day length increases with latitude: near the equator it is about $12\ \mathrm{h}$ all year, in Haikou ($20.0^\circ\mathrm{N}$) it ranges from $10.9$ to $13.3\ \mathrm{h}$, in Harbin ($45.8^\circ\mathrm{N}$) from $8.7$ to $15.7\ \mathrm{h}$, and inside the Arctic Circle there are polar days and polar nights.
3. Day length changes fastest around the equinoxes (about $2$–$4\ \mathrm{min}$ per day at mid-latitudes) and slowest around the solstices. A plant therefore cannot distinguish spring from autumn from a single day length; it must combine day length with the direction of change in day length, with the experience of low temperature ([7.13.22](/7.13.22)) or with its developmental stage.

![Annual course of day length in Harbin, Beijing and Haikou (left), and day length at the summer solstice, winter solstice and equinoxes as a function of latitude (right), calculated from Eqs. (21.1) and (21.2) ($h_0 = -0.833^\circ$). The dashed line in the left panel is a critical day length of 13.5 h (as in a short-day soybean cultivar); the dots mark the dates after the summer solstice when day length falls below the critical value and the short-day condition begins to be met: about 21 August in Beijing and about 28 August in Harbin; in Haikou day length is below 13.5 h all year](./plots/daylength.py)

## 21.2. Types of Photoperiodic Response

### 21.2.1. Long-Day, Short-Day and Day-Neutral Plants

According to the day-length requirement for flowering, plants fall into three main classes.

**Definition 21.2.1 (Long-Day, Short-Day and Day-Neutral Plants)** In a 24-hour cycle, a plant that must have a day length longer than a certain critical value in order to flower, or that flowers markedly earlier under long days, is called a **long-day plant** (LDP); a plant that must have a day length shorter than a certain critical value in order to flower, or that flowers markedly earlier under short days, is called a **short-day plant** (SDP); a plant whose flowering is insensitive to day length and that flowers under any day length is called a **day-neutral plant** (DNP).

Common examples of each class:

| Type | Crops | Ornamentals and others | Natural flowering season |
|---|---|---|---|
| Long-day plants | Wheat, barley, rye, oat, rapeseed, spinach, radish, Chinese cabbage, cabbage, celery, sugar beet, carrot, onion | Henbane, *Arabidopsis*, black-eyed Susan (*Rudbeckia*), darnel, rose of Sharon | Late spring and summer |
| Short-day plants | Rice, maize, soybean, sorghum, sugarcane, cotton (most wild types), hemp, jute, tobacco (Maryland Mammoth), strawberry (most cultivars) | Cocklebur, perilla, chrysanthemum, poinsettia, Japanese morning glory (*Ipomoea nil*), begonia, flaming Katy (*Kalanchoe blossfeldiana*) | Late summer, autumn or winter |
| Day-neutral plants | Tomato, cucumber, eggplant, pepper, common bean, sunflower | Dandelion, rose, clivia | Flowers whenever the temperature is suitable |

The photoperiodic type of a crop often differs among cultivars. The ancestors of cultivated rice, maize, soybean and cotton were short-day plants; as people carried them to higher latitudes they selected variants insensitive to day length, so many early-maturing cultivars are nearly day-neutral (Section 21.7). In general, early-maturing cultivars of a crop are mostly long-day or day-neutral and late-maturing cultivars mostly short-day.

Responses are further divided by strictness into qualitative and quantitative. Some plants have a "qualitative" requirement: they never flower under an unsuitable day length (the obligate long-day plant henbane, the obligate short-day plant cocklebur, Maryland Mammoth tobacco), and are called qualitative (obligate) long-day or short-day plants. More plants respond "quantitatively": a suitable day length makes flowering earlier, but under an unsuitable day length they eventually flower after a longer time (*Arabidopsis*, wheat, many rice cultivars); these are called quantitative (facultative) long-day or short-day plants (Figure 2).

There are also dual-day-length and intermediate types: a few plants require two day lengths in sequence, or flower only within a certain range of day length:

| Type | Requirement | Examples |
|---|---|---|
| Long–short-day plants | Long days first, then short days (long days induce, flowers form only under short days) | *Kalanchoe daigremontiana*, aloe, night-blooming jasmine (*Cestrum nocturnum*) |
| Short–long-day plants | Short days first, then long days (short days induce, flowers develop only under long days) | Bellflower, orchard grass, white clover, *Orostachys* |
| Intermediate-day plants | Flower only at intermediate day lengths; remain vegetative if days are too long or too short | Some sugarcane cultivars (about 11.5–12.5 h) |
| Ambiphotoperiodic plants | Do not flower at intermediate day lengths; flower under both longer and shorter ones | Some types of foxtail millet |

Long–short-day plants flower when day length shortens in late summer, and short–long-day plants flower when day length increases in spring: the dual requirement is one way of distinguishing spring from autumn.

### 21.2.2. Critical Day Length

**Definition 21.2.2 (Critical Day Length)** In a light–dark cycle, the longest day length that still induces flowering in a short-day plant, or the shortest day length required to induce flowering in a long-day plant, is called the **critical day length**.

Critical day lengths of several plants and the minimum number of inductive cycles required (Section 21.4):

| Type | Plant | Critical day length / h | Minimum inductive cycles |
|---|---|---|---|
| Short-day plants | Cocklebur (*Xanthium strumarium*) | 15.5 | 1 |
| | Japanese morning glory (*Ipomoea nil*, "Violet" cultivar) | 14–15 | 1 |
| | Duckweed (*Lemna paucicostata* strain 6746) | about 14 | 1 |
| | Perilla (*Perilla frutescens* var. *crispa*, red-leaf cultivar) | about 14 | 12 |
| | Soybean (Biloxi cultivar) | 13.5–14 | 2–3 |
| | Kalanchoe (*Kalanchoe blossfeldiana*) | 12 | 2 |
| | Chrysanthemum (*Chrysanthemum morifolium*) | 16 | 12 |
| Long-day plants | Spinach (*Spinacia oleracea*) | 13 | 1 |
| | White mustard (*Sinapis alba*) | about 14 | 1 |
| | Darnel (*Lolium temulentum*) | 11 | 1 |
| | Henbane (*Hyoscyamus niger*) | 11.5 | 2–3 |
| | Scarlet pimpernel (*Anagallis arvensis*) | 12–12.5 | 1 |

The table contains a fact that is at first surprising: the critical day length of the long-day plant henbane (11.5 h) is shorter than that of the short-day plant cocklebur (15.5 h). Under day lengths of 12–15 h both flower (Figure 2). Evidently "long-day" and "short-day" do not refer to absolute day lengths but to the direction of the response: a long-day plant flowers when day length exceeds the critical value, and a short-day plant flowers when day length is shorter than the critical value.

Two further points deserve notice. Within the inductive range a long-day plant flowers earlier the longer the day, earliest under continuous light. A short-day plant, by contrast, does not do better the shorter the day: if the day is too short, photosynthate is insufficient, vegetative growth is poor and flowering is impaired (Section 21.3.3).

![Types of photoperiodic response. Left: percentage of flowering plants as a function of day length for an obligate long-day plant (henbane, critical day length about 11.5 h) and an obligate short-day plant (cocklebur, critical day length about 15.5 h); both flower in the shaded region (11.5–15.5 h). Right: days from sowing to flowering for a quantitative long-day plant, a quantitative short-day plant and a day-neutral plant. The curves are schematic](./plots/response-types.py)

## 21.3. The Decisive Role of the Dark Period

### 21.3.1. Critical Night Length

Under natural conditions the light and dark periods of a day trade off against each other. Does the photoperiodic response depend on the light period or on the dark period? In the late 1930s K. C. Hamner and J. Bonner performed a series of experiments with the short-day plant cocklebur in which the lengths of light and dark periods were varied so that a cycle was not 24 h. The following table shows typical results of such experiments:

| Light period / h | Dark period / h | Cycle / h | Does cocklebur flower? |
|---|---|---|---|
| 16 | 8 | 24 | No |
| 8 | 16 | 24 | Yes |
| 16 | 32 | 48 | Yes (the light period exceeds the critical day length, but the dark period is long enough) |
| 4 | 8 | 12 | No (the light period is short, but the dark period is too short) |

As long as the dark period is longer than about 8.5 h, cocklebur flowers, however long the light period; if the dark period is not long enough, it does not flower, however short the light period. Long-day plants show the opposite result: they flower as long as the dark period is shorter than a certain length.

**Definition 21.3.1 (Critical Night Length)** In a light–dark cycle, the shortest dark period required for flowering of a short-day plant, or the longest dark period permitting flowering of a long-day plant, is called the **critical night length**.

A short-day plant is therefore more properly a "long-night plant," and a long-day plant a "short-night plant." In a 24 h cycle the critical night length and the critical day length are complementary: flowering of a short-day plant requires a day length shorter than the critical day length and a dark period longer than the critical night length, and a long-day plant requires a day length longer than the critical day length and a dark period shorter than the critical night length.

### 21.3.2. Night Breaks and Red/Far-Red Reversibility

The strongest evidence for the dark-period view is the night break: a brief exposure to light in the middle of a long dark period cancels the effect of the long night, whereas inserting a period of darkness into a long light period has almost no effect on flowering.

**Definition 21.3.2 (Night Break)** A treatment in which a short exposure to light is given in the dark period of the photoperiod, interrupting the continuous darkness, is called a **night break**. A night break prevents flowering of short-day plants and makes long-day plants flower under short days.

Night breaks have three important features (Figure 3):

- The amount of light required is very small. Short-day plants such as cocklebur and Japanese morning glory need only a few minutes or even tens of seconds of weak light in the dark period; long-day plants usually need longer irradiation. This shows that the night break is a light-signal response and that photosynthesis does not supply the energy.
- Timing is critical. In a 16 h dark period, a night break is most effective about 8 h after the start of the dark period (the middle of the night) and has little effect at the beginning or end.
- Light quality and reversibility. A night break with red light (about $660\ \mathrm{nm}$) is most effective, and far-red light (about $730\ \mathrm{nm}$) given immediately afterward cancels the effect of the red light; when red and far-red are given alternately, the quality of the last irradiation determines the outcome. The peak of the action spectrum is at 620–640 nm in cocklebur (shifted by shading from chlorophyll) and at 660 nm in etiolated seedlings of Japanese morning glory, in agreement with the absorption peak of the Pr form of **phytochrome**; the reversing effect of far-red is greatest at about 725 nm (Hendricks, Borthwick and colleagues, 1950s–1960s). These results established phytochrome as the photoreceptor that measures the dark period.

Night breaks are used in production to control flowering time: lighting a chrysanthemum greenhouse at midnight delays flowering, and night lighting of sugarcane fields suppresses flowering and raises yield (Section 21.7).

![Night-break experiments (schematic). Left: responses of a short-day plant such as cocklebur and of a long-day plant under different photoperiods; in a cycle of 8 h light and 16 h dark, a flash of red light (R) in the middle of the night prevents flowering of the short-day plant and makes the long-day plant flower; a subsequent far-red (FR) irradiation reverses the effect of red, and when they are alternated the last light quality decides. Right: inhibition of flowering of a short-day plant by 1 h of red light given at different times in a 16 h dark period: the middle of the night is most effective (schematic curve)](./plots/night-break.py)

### 21.3.3. The Role of the Light Period

The length of the light period does not determine whether flowering occurs, but it is not dispensable. The light period supplies photosynthate and affects the number of flowers: in night-break experiments with the short-day plant soybean using an 8 h dark period, the longer the light period and the greater the light intensity, the more flowers form; in continuous darkness, even if the dark-period requirement is met, flowering does not occur, because the photosynthate is exhausted. Supplying sucrose during an artificially shortened light period can partly substitute for photosynthesis. In long-day plants the ratio of far-red to blue light in the light period also affects flowering (Section 21.5.3).

## 21.4. Photoperiodic Induction and Perception by the Leaf

### 21.4.1. Photoperiodic Induction

A plant does not need to live under a suitable photoperiod all the time in order to flower.

**Definition 21.4.1 (Photoperiodic Induction)** The phenomenon in which a plant that has reached a certain physiological age, after a sufficient number of days of suitable photoperiod, flowers even when subsequently transferred to an unsuitable photoperiod, because it retains the effect of the stimulus, is called **photoperiodic induction**. The minimum number of photoperiodic cycles required is called the number of inductive cycles.

The number of inductive cycles varies among plants: cocklebur, Japanese morning glory, duckweed, darnel and spinach need only 1 cycle, soybean 2–3, and chrysanthemum and perilla about 12 (the table in Section 21.2.2). With fewer than the minimum number of cycles flowering is not induced; with more, floral primordia develop faster and more flowers form. Plants that need only one photoperiod for induction (especially cocklebur, Japanese morning glory and darnel) became classic material for the study of floral induction, because the moment of induction is known exactly.

A plant must reach a certain age before it can respond to photoperiodic induction: plants in the juvenile phase do not flower under any photoperiodic treatment ([7.13.22](/7.13.22)). Some plants have an extremely short juvenile phase; Japanese morning glory seedlings at the cotyledon stage can be induced to flower by a single short-day cycle.

### 21.4.2. Perception of Photoperiod by the Leaf

It is the leaf, not the shoot apex, that receives the photoperiodic stimulus. M. Chailakhyan (1937) treated the short-day plant chrysanthemum in four groups: whole plant under short days; whole plant under long days; leaves under short days with the apex under long days; and leaves under long days with the apex under short days. Only the two groups with leaves under short days flowered, regardless of the photoperiod of the apex. A cocklebur plant flowers if it has even one leaf, or even part of one leaf, under short days while the rest is under long days; plants stripped of all leaves do not respond to photoperiod.

The sensitivity of a leaf depends on its development: leaves from just expanding to fully expanded are the most sensitive, and young and senescent leaves are less sensitive.

Perception takes place in the leaf, whereas flowers form at the shoot apex, so a signal must travel from the leaf to the apex. Experiments with perilla show that this signal can be "remembered" in the leaf: a perilla leaf induced under short days and then detached and grafted onto an uninduced stock growing under long days makes the stock flower; the same induced leaf can be grafted successively onto several stocks, inducing flowering each time over a period of months (Zeevaart). Once a leaf has been induced, it stably maintains the state of producing the flowering stimulus. In cocklebur the induced state can even be transmitted between shoot tips: grafting buds taken from flowering plants also induces flowering in the recipient. These experiments led to the concept of florigen (Section 21.6).

## 21.5. The Mechanism of Photoperiodic Timing

### 21.5.1. The Hourglass Model

Since it is the length of the dark period that decides flowering, a plant needs a "timer" that measures the night. After the discovery of phytochrome, the hourglass model was proposed: at the end of the light period most of the phytochrome in the leaf is in the Pfr form; in darkness Pfr is gradually degraded or reverts to Pr, like sand slowly running out of an hourglass; the critical night length is the time required for Pfr to fall to a threshold. A short-day plant requires a low Pfr level and therefore a long night; a long-day plant requires a higher Pfr level and therefore the night must not be long; red light in a night break converts Pr to Pfr, equivalent to turning the hourglass over.

The model is simple and intuitive and was long found in textbooks, but it disagrees with two kinds of fact:

1. Pfr disappears in darkness much faster than the critical night length. In Japanese morning glory and other plants Pfr falls to a very low level 2–4 h after the start of the dark period, whereas the critical night length is as long as 9–10 h; giving far-red light at the start of the night to convert Pfr back to Pr immediately does not shorten the critical night length.
2. Sensitivity to night breaks changes periodically, not monotonically. The classic case is the soybean "resonance" experiment (Nanda and Hamner, 1958): Biloxi soybean was given an 8 h light period followed by dark periods of different lengths, so that the total cycle length varied from 24 h to 72 h. Flowering was greatest at total cycle lengths of 24 h, 48 h and 72 h and almost absent at 36 h and 60 h. If the plant merely accumulated the length of the dark period, a longer night would always be more favorable and no oscillation with a 24 h period would appear. When night breaks were given at different times in an extended 72 h dark period, the inhibitory effect likewise recurred with a period of about 24 h.

These results show that photoperiodic timing depends on an endogenous oscillator with a period of about 24 h, the circadian clock. The role of phytochrome in it is not timing but sensing light and, as in other physiological processes regulated by phytochrome, providing input to the oscillator (**entrainment**) and "gating" its output.

### 21.5.2. The Circadian Clock and Bünning's Hypothesis

Many physiological processes in plants have rhythms of approximately 24 h: the opening of leaves by day and closing by night (nyctinasty), stomatal aperture, the rate of photosynthesis, the time of flower opening and release of floral scent, and the expression of thousands of genes. When plants are transferred to constant light (or darkness) and temperature, these rhythms continue to run for several days with a period close to but not exactly 24 h, the free-running period of the **circadian rhythm**. The three properties of the clock (autonomous running, temperature compensation and the ability to be reset in phase by light and temperature) and the dynamics of its transcription–translation feedback loops are described in [7.6.33](/7.6.33#sec-33.6.1). In *Arabidopsis* the core of the clock is a circuit in which transcription factors expressed in the morning (CCA1 and LHY) and in the evening (TOC1 and the evening complex, ELF3, ELF4 and LUX) repress one another.

In 1936 E. Bünning proposed that photoperiodic timing is a function of the circadian clock. The clock divides the day into two phases, the "photophile phase" (corresponding to subjective day) and the "scotophile phase" (corresponding to subjective night); light acts only in the scotophile phase. When the day is short, light falls only within the photophile phase and the plant "sees" short days; when the day is long, light extends into the scotophile phase and the plant "sees" long days. Light falling in the scotophile phase induces flowering in long-day plants and inhibits it in short-day plants. This hypothesis explains why a night break is most effective in the middle of the night (which is the center of the scotophile phase) and accounts for the 24 h period in the resonance experiment.

### 21.5.3. The External Coincidence Model

Bünning's hypothesis was later developed into the external coincidence model and has been confirmed at the molecular level in *Arabidopsis*.

**Definition 21.5.1 (External Coincidence Model)** A model in which the circadian clock controls a light-sensitive internal process so that it occurs during a certain period of the day, and a photoperiodic signal is generated only when external light coincides with this period, is called the **external coincidence model**. The contrasting internal coincidence model holds that day length changes the phase relationship between two internal rhythms controlled by the clock, and that the signal depends on whether these two rhythms coincide.

In the long-day plant *Arabidopsis* the key component is the *CONSTANS* (*CO*) gene, which encodes a transcriptional regulator with B-box zinc fingers; *co* mutants flower late under long days and are insensitive to photoperiod. External coincidence is implemented at two levels:

1. Transcription is controlled by the clock. CDF-type transcription factors (such as CDF1), regulated by the clock, repress *CO* transcription in the morning; in the afternoon the clock-controlled GI and the blue-light receptor FKF1 form a complex in the light, which causes ubiquitination and degradation of CDF1, and *CO* mRNA begins to rise. *CO* mRNA therefore starts to accumulate about 12 h after dawn, peaks during the night and decreases the next morning. Under long days (16 h) the rising phase of *CO* mRNA coincides with the last hours of the light period; under short days (8 h) *CO* mRNA accumulates in darkness.
2. Protein stability is controlled by light. In darkness CO protein is tagged by the E3 ubiquitin ligase complex COP1–SPA and rapidly degraded by the 26S **proteasome**; in the morning phytochrome B promotes CO degradation; and in the light from afternoon to evening, phytochrome A and the cryptochromes (CRY1, CRY2) inhibit COP1–SPA so that CO protein accumulates stably. Only in the evening of a long day, when *CO* mRNA coincides with light, can CO protein accumulate to a sufficient level.

CO protein directly activates transcription of the *FLOWERING LOCUS T* (*FT*) gene in the **companion cells** of the leaf vascular bundles. FT protein is the flowering signal produced in the leaf and transported to the shoot apex (Section 21.6). The genetic evidence for photoreceptors agrees with this: *phyA* and *cry2* mutants flower late under long days, whereas *phyB* mutants flower early.

The short-day plant rice uses the same set of components, but the sign of the output is reversed. The rice genes *Heading date 1* (*Hd1*) and *Hd3a* are homologs of *CO* and *FT*, respectively; *Hd1* mRNA also shows a circadian rhythm like that of *CO*, and *Hd3a*, like *FT*, is a strong promoter of flowering: rice overexpressing *Hd3a* and *Arabidopsis* overexpressing *FT* flower rapidly under any day length. The difference is that under long days Hd1 protein, coinciding with light (and under the influence of phytochrome), represses *Hd3a* transcription and rice remains vegetative; under short days *Hd1* mRNA is expressed only in darkness, Hd1 does not repress, *Hd3a* is expressed and rice flowers. Rice also has a pathway absent from *Arabidopsis*: *Early heading date 1* (*Ehd1*) is induced by blue light in the morning of short days and activates *Hd3a* and another *FT* homolog, *RFT1*. Mutation of the phytochrome chromophore synthesis gene *Se5* makes rice flower rapidly under any day length, which likewise shows that in short-day plants phytochrome transmits the message "inhibit flowering."

The logic of external coincidence can be expressed in the simplest mathematical model, written as a few ordinary differential equations ([2.4](/2.4)). Let $m(t)$ be the clock-driven level of *CO* mRNA (peaking about 14 h after dawn each day), let $L(t)$ be 1 in the light and 0 in the dark, and let the CO protein $P$ and *FT* mRNA $F$ satisfy

$$
\frac{\mathrm{d}P}{\mathrm{d}t} = k_{\mathrm{s}}\,m(t) - k_{\mathrm{d}}(t)\,P,
\qquad
\frac{\mathrm{d}F}{\mathrm{d}t} = v\,\frac{P^n}{K^n + P^n} - \gamma F,
\tag{21.3}
$$

where the degradation rate constant $k_{\mathrm{d}}(t)$ is large in darkness (COP1–SPA), intermediate in morning light (phyB) and small in afternoon light (phyA, CRY); $K$ is the half-saturation concentration for activation of *FT* by CO and the Hill coefficient $n$ describes the cooperativity of activation ([7.6.4](/7.6.4)). For rice the activation term is replaced by a term for repression of *Hd3a* by Hd1 in the light, $v K_{\mathrm{r}}^n/(K_{\mathrm{r}}^n + (L P)^n)$. The numerical solution (Figure 4) shows:

- Under long days CO protein shows a sharp peak in the evening and disappears quickly after nightfall, and *FT* mRNA peaks in the evening accordingly; under short days, although the peak of *CO* mRNA is equally high, CO protein stays low throughout and *FT* is hardly expressed.
- The daily mean of *FT* expression increases sigmoidally with photoperiod, rising rapidly between 12 and 14 h, which corresponds to a "critical day length"; *Hd3a*, in contrast, decreases as the photoperiod lengthens. The critical day length is not the direct value of any single parameter but an emergent property determined jointly by the phase of the clock (the time of the peak of $m$), the degradation kinetics and the activation threshold: if the time of the peak of $m$ is changed (a mutation of clock phase or period), the critical day length shifts accordingly. This is why many clock mutants alter flowering time.

![Numerical simulation of the external coincidence model (Eq. 21.3; parameters are illustrative). A, B: diel changes of clock-driven CO mRNA, CO protein and FT mRNA in an *Arabidopsis* leaf under a 16 h light period (A) and an 8 h light period (B) (gray is the dark period; each quantity is scaled to its peak under long days). On a long day CO mRNA coincides with light in the evening, CO protein accumulates and activates FT; on a short day CO mRNA accumulates only in darkness and CO protein is degraded. C: relative daily mean levels of FT (*Arabidopsis*, a long-day plant) and Hd3a (rice, a short-day plant; Hd1 in the light represses Hd3a) as a function of photoperiod](./plots/coincidence.py)

### 21.5.4. Effects of Temperature on the Photoperiodic Response

Temperature affects not only the rate of flower development but can also change the day-length requirement of a plant:

- Lowering the temperature can make long-day plants flower under shorter days. Pea, rye, alfalfa, cabbage and others lose their sensitivity to day length at lower night temperatures and behave as day-neutral plants; sugar beet normally flowers only under long days, but at a lower night temperature of 10–18 °C it flowers even under 8 h days.
- Lowering the night temperature can also make some short-day plants flower under longer days. A short-day tobacco cultivar requires short days at a night temperature of 18 °C, but at 13 °C it flowers even under 16–18 h long days; Japanese morning glory is a short-day plant at 21–23 °C but behaves as a long-day plant at 13 °C.
- Many plants that require vernalization also require long days after the cold (winter cereals, sugar beet, Chinese cabbage and other biennials, [7.13.22](/7.13.22)).

At the molecular level, temperature and light signals share components. The Pfr form of phytochrome B reverts spontaneously to the Pr form in darkness (dark reversion), and the rate of this thermal reversion increases with temperature, so phyB is both a photoreceptor and a temperature sensor (Jung et al., 2016; Legris et al., 2016, *Science*). The scaffold protein ELF3 of the evening complex has a prion-like domain; when the temperature rises, ELF3 condenses into puncta by phase separation and loses its ability to repress target genes (Jung et al., 2020, *Nature*). Both relieve repression of the transcription factor PIF4, which at higher temperatures binds the *FT* promoter directly and promotes its transcription; this is one reason why *Arabidopsis* flowers earlier at 27 °C than at 22 °C (Kumar et al., 2012). Other effects of ambient temperature on flowering are discussed in [7.13.22](/7.13.22).

## 21.6. Florigen

### 21.6.1. Grafting Experiments and the Florigen Hypothesis

The leaf perceives photoperiod and the shoot apex forms flowers, so there must be a mobile signal between them. **Grafting** experiments demonstrated this and revealed several of its properties:

1. It can be transmitted between plants by grafting. Chailakhyan joined several cocklebur plants in a chain by approach grafting and kept only one leaf of the first plant under short days with all the others under long days; all of the plants flowered (Figure 5A). The grafting of induced perilla leaves (Section 21.4.2) also shows this (Figure 5B).
2. It is transported through the phloem. Killing the phloem of the petiole with steam or treating it with an anesthetic, or blocking export of assimilates from the leaf, prevents the flowering stimulus from leaving; the stimulus moves in the same direction as assimilates, from source leaves to sinks such as the shoot apex ([7.13.11](/7.13.11)).
3. It is the same among plants of different photoperiodic types. When the long-day plant henbane is grafted onto the short-day plant Maryland Mammoth tobacco, both flower under long days; conversely, tobacco induced under short days can also make a henbane grafted onto it flower under short days (Figure 5C). Grafts among day-neutral, long-day and short-day plants all transmit the flowering stimulus, even across species and genera.

In 1936 Chailakhyan named this hypothetical flowering hormone **florigen**. In the following decades attempts to extract florigen from induced leaves all failed, and florigen became for a time "the most famous nonexistent hormone" in plant physiology. During this period Chailakhyan (1958) also proposed that florigen consists of two parts, gibberellin and "anthesin": day-neutral plants have both; long-day plants have anthesin, and gibberellin is synthesized only under long days; short-day plants have gibberellin, and anthesin is synthesized only under short days. The hypothesis is of historical interest only today, but it already noted the effect of gibberellin on flowering of long-day plants ([7.13.22](/7.13.22)).

Grafting experiments also revealed an opposite signal. In some plants, leaves under a non-inductive photoperiod inhibit flowering, and removal of these leaves promotes flowering, suggesting the existence of an "antiflorigen." Most antiflorigens are now known to be proteins of the FT family as well: in chrysanthemum under non-inductive long days, the AFT protein synthesized in the leaves moves to the shoot apex and inhibits flowering (Higuchi et al., 2013); proteins such as ATC and TFL1 of *Arabidopsis* compete with FT for the same binding partners.

![Classic grafting experiments on florigen (schematic). A: Chailakhyan's cocklebur experiment: five cocklebur plants are joined by approach grafting (squares are graft unions); only one leaf of the first plant is under short days (dark box) and the rest are under long days, and all five plants flower. B: a perilla leaf induced under short days is grafted onto a stock under long days, and the stock flowers; a leaf from a plant under long days cannot induce flowering. C: a scion of the long-day plant henbane is grafted onto the short-day plant Maryland Mammoth tobacco; under long days the tobacco stock also flowers, showing that the flowering stimuli of long-day and short-day plants are interchangeable](./plots/grafting.py)

**Definition 21.6.1 (Florigen)** A signaling substance that is produced in the leaf under a suitable photoperiod, transported through the phloem to the shoot apical meristem to induce flowering, and transmissible between plants by grafting is called **florigen**. Its main component is now known to be the FT protein and its homologous proteins in various plants.

### 21.6.2. The FT Protein

In 1999 two laboratories cloned the *Arabidopsis* *FT* gene (Kardailsky et al.; Kobayashi et al.). It encodes a small globular protein of about 20 kDa (175 amino acids) belonging to the phosphatidylethanolamine-binding protein (PEBP) family; this family also has members in bacteria, fungi and animals (such as mammalian RKIP), but the function of FT in flowering is unique to plants. *ft* mutants flower very late under long days, and expression of *FT* specifically in companion cells is enough to make plants flower under short days. The subsequent work had to answer a question: is it *FT* mRNA or FT protein that moves from the leaf to the shoot apex?

- A 2005 paper in *Science* reported that after heat-shock induction of *FT* expression in a single leaf, *FT* mRNA moved from the leaf to the shoot apex. This paper was later retracted, in 2007, because of problems in data handling.
- In 2007 results from several laboratories corroborated one another. In *Arabidopsis*, an FT–GFP fusion protein expressed specifically in companion cells appeared at the shoot apex while its mRNA did not leave the vascular bundle (Corbesier et al., *Science*; Jaeger and Wigge; Mathieu et al.). In rice, Hd3a–GFP protein moved from the leaf vascular bundle to the shoot apical meristem (Tamaki et al., *Science*). In cucurbits, FT protein was detected directly in phloem sap, and expression of FT in leaves from a viral vector induced flowering of short-day squash under long days, while neither the virus nor *FT* mRNA entered the shoot apex (Lin et al., *Plant Cell*). The action of tomato *SFT* (*SINGLE FLOWER TRUSS*, a homolog of *FT*) can also be transmitted to mutants by grafting and can make tobacco and *Arabidopsis* flower (Lifschitz et al., 2006).
- A 2018 study (Chen et al., *PNAS*) found in both *Arabidopsis* and Maryland Mammoth tobacco that *FT* mRNA is synthesized mainly in phloem companion cells of the distal minor veins of the leaf, which is exactly where phloem loading occurs.

The florigen pathway can therefore be described as follows: in leaf companion cells CO activates *FT* transcription; FT protein enters the sieve elements through **plasmodesmata** (a step that requires the assistance of the endoplasmic reticulum membrane protein FTIP1 and others); it is carried with assimilates in the **phloem** to the shoot apex; there it moves from cell to cell through plasmodesmata and enters the nuclei of cells of the apical meristem. In the nucleus FT forms the "florigen activation complex" with the bZIP transcription factor FD and a 14-3-3 protein (Taoka et al., 2011), which activates genes such as *APETALA1* (*AP1*) and *SOC1* and converts the vegetative meristem into an inflorescence meristem ([7.13.22](/7.13.22)).

The conservation of florigen explains Chailakhyan's finding: long-day and short-day plants measure day length in opposite ways, but the signal produced in the leaf is the same protein, so the flowering stimulus can be exchanged among photoperiodic types. FT-family proteins are also involved in other photoperiodically controlled processes: potato forms tubers under short days, and the tuberization signal produced in the leaf and transported to the stolon tip is the FT homolog StSP6A (Navarro et al., 2011); an FT homolog of poplar participates in the control of growth cessation and bud dormancy in autumn. FT can therefore be regarded as a class of "mobile developmental switches," of which florigen was the first function to be recognized.

## 21.7. Photoperiod, Geographic Distribution, Introduction of Crops and Control of Flowering Time

### 21.7.1. Photoperiod and Geographic Distribution

The photoperiodic response type of a plant is the result of long-term adaptation to the natural photoperiod of its place of origin:

- At low latitudes (tropics and subtropics) day length is close to 12 h all year, the seasonal change in day length is small, and the rainy and dry seasons matter more than day length; plants native here are mostly short-day plants (the wild ancestors of rice, maize, soybean, sugarcane and cotton) or day-neutral plants.
- At high latitudes summer days are very long and the growing season is short; plants must flower and set seed rapidly in the brief summer, and are mostly long-day plants (cereals, rapeseed, spinach and others native to the northern temperate zone).
- At mid-latitudes long-day and short-day plants coexist. At the same latitude long-day plants mostly flower in late spring and summer when days are longer (wheat), and short-day plants mostly flower in late summer and autumn when days are shorter (chrysanthemum, soybean).

### 21.7.2. Introduction of Crops

When a plant is introduced from one place to another, the difference in photoperiod between the two places must be considered, together with temperature conditions (low-temperature vernalization, [7.13.22](/7.13.22)). Figure 1 yields the rule for introductions: in the growing season in China (roughly equinox to equinox), on the same date the day length in the north is longer than in the south.

| Plant type | Direction of introduction | Effect on flowering | If seed or fruit is to be harvested |
|---|---|---|---|
| Short-day plants | North → south | Short-day conditions appear earlier, flowering is earlier, the growth period is shortened | Choose late-maturing cultivars |
| | South → north | Short-day conditions appear later, flowering is delayed, and the crop may not mature before frost | Choose early-maturing cultivars |
| Long-day plants | North → south | Long-day conditions are insufficient or appear later, flowering is delayed (or does not occur) | Choose early-maturing cultivars |
| | South → north | Long-day conditions appear earlier, flowering is earlier | Choose late-maturing cultivars |

For example, soybean is a short-day plant: a southern soybean cultivar planted in Beijing flowers too late, the weather is already cold at flowering and pod set, and few seeds are produced; a northeastern soybean cultivar planted in Beijing flowers earlier, its growth period is greatly shortened and its yield is also low. In the 1950s winter wheat from Henan introduced to Guangdong could not flower and set seed, because it had neither enough low temperature for vernalization nor long days.

**Example 21.7.1** A short-day soybean cultivar has a critical day length of 13.5 h (astronomical day length with $h_0 = -0.833^\circ$). Compare when the short-day condition is met after sowing in Harbin, Beijing and Haikou.

Calculating day by day with Eqs. (21.1) and (21.2) (Figure 1): in Harbin day length at the summer solstice is 15.7 h and falls below 13.5 h around 28 August; in Beijing it is 15.0 h at the summer solstice and falls below 13.5 h around 21 August; in Haikou it is only 13.3 h at the summer solstice, shorter than the critical day length all year. This cultivar sown in spring in Harbin therefore starts to be induced only at the end of August, a week earlier in Beijing; in Haikou the seedlings begin to flower as soon as they pass the juvenile phase, vegetative growth is insufficient, and plants are small and yields very low. If twilight is considered to increase the effective day length by about 0.5–1 h, the dates when the short-day condition is met are delayed by a few days to a week or two at each place.

:::

In actual breeding, the expansion of soybean to low latitudes has depended on alleles of photoperiod insensitivity or a long juvenile phase: for example, loss of function of *E1* (a transcription factor that represses *FT* homologs) and mutation of *J* (a homolog of *Arabidopsis* *ELF3*; the "long juvenile" trait) allow soybean to obtain enough vegetative growth at low latitudes such as in Brazil (Lu et al., 2017). Photoperiod-insensitive alleles of wheat such as *Ppd-D1a* allow winter wheat to head on time at lower latitudes, and together with dwarfing genes they underlie the adaptation of Green Revolution cultivars to wide areas ([7.13.28](/7.13.28)).

### 21.7.3. Off-Season Breeding (South in Winter, North in Summer)

Using the differences in photoperiod and temperature among regions, several generations can be grown in one year to speed up breeding:

- The short-day crops rice and maize are propagated in winter on Hainan Island: the day length in Haikou at the winter solstice is about 10.9 h (Eq. 21.1), flowering is rapid under short days, and winter temperatures are still sufficient for growth, so material bred in the north can be harvested locally and grown for one more generation in Hainan in winter.
- The long-day crop wheat is grown in summer in Heilongjiang and in winter in Yunnan, which satisfies both light and temperature requirements and allows 2–3 generations per year.

### 21.7.4. Control of Flowering Time

Artificial control of photoperiod (shading to shorten the day, supplementary lighting to extend the day or a night break) can make plants flower earlier or later:

- Flower production. Chrysanthemum is a short-day plant that flowers in autumn under natural conditions; shading it with black cloth in summer so that day length is shorter than the critical value makes it flower earlier, in summer; extending the light or lighting at night before short days arrive delays it to winter or the Spring Festival. Long-day ornamentals such as azalea and camellia flower earlier with supplementary lighting extending the day. Poinsettia can be brought to market before Christmas by shading.
- Resolving asynchrony of flowering. When the flowering times of hybrid parents are too far apart, the photoperiod can be adjusted so that both parents flower at the same time. In crosses between early and late rice, shading the late-rice seedlings at the 4–7 leaf stage makes them flower earlier, to pollinate the early rice.
- Balancing vegetative and reproductive growth. For crops harvested mainly for their vegetative parts, suppressing flowering can raise yield: short-day tobacco cultivars (such as Maryland Mammoth) are sown earlier in spring in temperate regions to exploit the long days, high temperature and rainfall of summer, which gives vigorous vegetative growth and raises leaf yield; when short-day fiber crops are moved from south to north, flowering is delayed and the stems are longer, which improves the yield and quality of fiber, and seed is produced by giving short-day treatment at the seedling stage in the seed field; night lighting (a night break) of sugarcane fields suppresses flowering and raises sugar yield.

## Summary

| Concept | Key points |
|---|---|
| Photoperiodism | Definition 21.1.1; discovered by Garner and Allard (1920) with Maryland Mammoth tobacco and Biloxi soybean; also controls tubers, bulbs, dormancy and leaf fall |
| Response types | Long-day, short-day and day-neutral plants (Definition 21.2.1); qualitative (obligate) and quantitative (facultative) responses; long–short-day, short–long-day, intermediate-day and ambiphotoperiodic plants |
| Critical day length | Definition 21.2.2; the critical day length of a long-day plant can be shorter than that of a short-day plant (henbane 11.5 h, cocklebur 15.5 h) |
| Critical night length | Definition 21.3.1; the dark period is decisive: short-day plants are "long-night plants" and long-day plants are "short-night plants" |
| Night break | Definition 21.3.2; effective with weak light and short exposures, most effective in the middle of the night; red is effective and far-red reverses, the last light quality decides: phytochrome |
| Photoperiodic induction | Definition 21.4.1; minimum number of inductive cycles (cocklebur 1, soybean 2–3, perilla and chrysanthemum about 12); perceived by the leaf, and an induced leaf stably maintains the induced state |
| Timing mechanism | The hourglass model (Pfr decay) disagrees with the facts; the resonance experiment and the periodicity of night-break sensitivity show that the clock is responsible; Bünning's hypothesis → external coincidence model (Definition 21.5.1) |
| *Arabidopsis* (long-day) | The clock (CDF1, GI–FKF1) controls *CO* transcription; CO protein is degraded in the dark by COP1–SPA and stabilized in the evening light by phyA and CRY; CO activates *FT* in companion cells |
| Rice (short-day) | Hd1 (CO homolog) represses *Hd3a* (FT homolog) in long-day light; *Hd3a* and *RFT1* are expressed under short days; *Ehd1* pathway |
| Temperature | Changes the day-length requirement; phyB thermal reversion and ELF3 phase separation → PIF4 → *FT* |
| Florigen | Definition 21.6.1; transmissible by grafting, moves through the phloem, common to all photoperiodic types (Chailakhyan 1936); FT protein (confirmed in 2007) is synthesized in companion cells, moves through sieve tubes to the shoot apex and forms an activation complex with FD and 14-3-3, activating *AP1* and *SOC1*; antiflorigens (AFT, ATC) |
| Applications | Short-day plants are more common at low latitudes and long-day plants at high latitudes; rules for introductions (short-day plants: choose late-maturing cultivars from north to south and early-maturing from south to north; the opposite for long-day plants); off-season breeding; shading, supplementary light and night breaks to control flowering time |

Main equations:

| Equation | Meaning |
|---|---|
| Eq. (21.1) $\cos H_0 = (\sin h_0 - \sin\phi\sin\delta)/(\cos\phi\cos\delta)$, $N = 2H_0/15^\circ$ | Day length; $\cos H_0 = -\tan\phi\tan\delta$ for $h_0 = 0$; $h_0 = -0.833^\circ$ (sunrise and sunset), $-6^\circ$ (civil twilight) |
| Eq. (21.2) $\delta \approx -23.44^\circ\cos[360^\circ(d+10)/365]$ | Variation of solar declination with day of year |
| Eq. (21.3) $\dot P = k_{\mathrm{s}}m(t) - k_{\mathrm{d}}(t)P$, $\dot F = vP^n/(K^n + P^n) - \gamma F$ | External coincidence: clock-driven *CO* mRNA × light-dependent CO stability → *FT*; the critical day length is an emergent property |

## Questions

1. Using the simplified form of Eq. (21.1), calculate the day length at the summer solstice in Harbin ($45.8^\circ\mathrm{N}$) and Haikou ($20.0^\circ\mathrm{N}$), and explain why short-day rice cultivars flower especially fast when seed is multiplied in winter in Hainan.

   **Answer** At the summer solstice $\delta = 23.44^\circ$ and $\tan\delta = 0.4334$. Harbin: $\tan 45.8^\circ = 1.028$, $\cos H_0 = -0.4456$, $H_0 = 116.5^\circ$, $N = 15.5\ \mathrm{h}$ (about 15.7 h with refraction). Haikou: $\tan 20.0^\circ = 0.364$, $\cos H_0 = -0.158$, $H_0 = 99.1^\circ$, $N = 13.2\ \mathrm{h}$ (about 13.3 h with refraction). The day length in Haikou at the winter solstice is only about 10.9 h, far shorter than the critical day length of most rice cultivars, while winter temperature is still around 20 °C and sufficient for growth; under these conditions a short-day plant is induced as soon as the seedling passes the juvenile phase and heads very quickly, so breeding material from the north can be multiplied for one generation in Hainan in winter.

2. A short-day plant has a critical night length of 9 h. Which of the following treatments make it flower? (a) 14 h light + 10 h dark; (b) 10 h light + 14 h dark, with 5 min of red light at hour 7 of the dark period; (c) as (b), with 5 min of far-red light immediately after the red light; (d) 16 h light + 20 h dark (36 h cycle); (e) 8 h light + 16 h dark, with 2 h of darkness inserted in the middle of the light period.

   **Answer** (a) The 10 h dark period is longer than the critical night length: flowering. (b) The red flash divides the 14 h dark period into two parts of 7 h and 7 h, both shorter than 9 h: no flowering. (c) Far-red reverses the effect of red, which is equivalent to a continuous 14 h dark period: flowering. (d) The 20 h dark period meets the requirement by itself, but the cycle is 36 h: according to the resonance experiment (Section 21.5.1), the light period then falls in the scotophile phase of the clock, and a short-day plant flowers little or not at all; judging by the length of the dark period alone would give the wrong conclusion "flowering." (e) Inserting darkness into the light period has almost no effect on the photoperiodic response, and the 16 h dark period meets the requirement: flowering.

3. Why can the "hourglass model" not explain photoperiodic timing? How does the external coincidence model explain why "a night break is most effective in the middle of the night"?

   **Answer** The hourglass model holds that the critical night length is the time required for Pfr to decay to a threshold in darkness. But Pfr disappears within a few hours of the start of the dark period, much faster than the critical night length of 9–10 h; removing Pfr with far-red at the start of the dark period does not shorten the critical night length; and in an extended dark period, sensitivity to night breaks oscillates with a period of about 24 h, with light–dark cycles of 24, 48 and 72 h most favorable for flowering of short-day plants. All this shows that timing is done by the circadian clock and not by a monotonically decaying process. According to the external coincidence model, the clock causes a light-sensitive process (in *Arabidopsis* the expression of *CO* and the light stabilization of CO protein, in short-day plants the light activation of a flowering repressor) to occur in a certain part of the subjective night; light given in the middle of the dark period coincides with this window and generates a "long-day" signal, so it inhibits flowering of short-day plants and promotes flowering of long-day plants; light given at the beginning or end of the dark period does not coincide with the sensitive window and has little effect.

4. According to the model of Eq. (21.3), how would the flowering time of *Arabidopsis* under a 12 h photoperiod change if a clock mutation advanced the peak of *CO* mRNA from 14 h to 10 h after dawn? Why? What does this conclusion imply for understanding photoperiodic adaptation of crops?

   **Answer** With the earlier peak, *CO* mRNA reaches a high level already within the 12 h light period, its coincidence with light increases, CO protein accumulates in the light, *FT* expression rises, and the plant flowers earlier under the originally "non-inductive" 12 h photoperiod, which is equivalent to a shorter critical day length (some short-period clock mutants of *Arabidopsis* do flower early under short days). This shows that the critical day length is determined jointly by clock phase, protein degradation kinetics and the activation threshold, and any allele that changes clock phase or CO/FT regulation may change the photoperiodic response of a cultivar. Many flowering-time genes selected as crops spread to different latitudes (such as *J* and *E1* in soybean, *Hd1* and *Ehd1* in rice and *Ppd-1* in wheat) are natural variants of exactly such components.

5. Design an experiment to determine whether the florigen transported from the leaf to the shoot apex is *FT* mRNA or FT protein.

   **Answer** The idea is to express *FT* only in companion cells of the leaf and to follow its mRNA and protein separately. For example, express an FT–fluorescent protein fusion in an *ft* mutant from a companion-cell-specific promoter (such as the *SUC2* promoter), or induce expression in a single leaf; check by fluorescence microscopy whether the fusion protein appears in the shoot apex, check by in situ hybridization or RT-PCR whether the mRNA is present there, and at the same time observe flowering. A more direct approach is to make the protein immobile while leaving the mRNA unchanged: fuse FT to a large protein or to a nuclear-localization or membrane-anchoring domain so that it cannot pass through plasmodesmata; if the plant then no longer flowers, while direct expression of the same fusion protein in the shoot apex still allows flowering, the protein is what must move. Grafting can also be used: graft a scion expressing *FT* in companion cells onto an *ft* stock and examine protein and mRNA in the stock's shoot apex. The 2007 experiments used just these approaches, and the result was that FT protein moves and the mRNA does not.
