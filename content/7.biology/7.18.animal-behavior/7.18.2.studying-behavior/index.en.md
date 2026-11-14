---
title: "Studying Behavior: Description, Measurement and Hypothesis Testing"
description: "How behavior is described and measured: ethograms and the classification of behavior, sampling rules (ad libitum, focal, scan and behavior sampling) and recording rules (continuous, instantaneous and one–zero), their biases, reliability, and automated tracking and pose estimation; how hypotheses are tested by comparison (gulls and kittiwakes, weaverbirds, African ungulates, primates, independent contrasts) and by experiment (house finch plumage, eggshell removal), with optimality models, observer effects, ethics and the main statistical pitfalls."
---

Every study of behavior rests on two activities: describing and measuring what animals do, and testing explanations of why they do it. Neither is as simple as it looks. Behavior is a continuous stream of movement that the observer must divide into units; the units must be recorded by rules that do not bias the result; and the resulting numbers must be analyzed with a design that can actually distinguish between hypotheses. This chapter treats these methods. The first half covers description and measurement, from the ethogram of the classical ethologists to machine-learning analysis of video. The second half covers hypothesis testing: the comparative method, illustrated with the classic studies of gulls, weaverbirds and antelopes and its modern phylogenetic form, the experimental method, illustrated with plumage manipulation in house finches and eggshell removal in gulls, and quantitative optimality models. We end with the effects of observers on animals, the ethics of research, and the statistical errors most common in behavioral studies.

The chapter builds on [7.18.1](/7.18.1), which introduced the observational, experimental and comparative approaches with the example of mobbing in gulls. The statistical tools are those of [7.7.6](/7.7.6) (testing and effect sizes) and [7.7.12](/7.7.12) (experimental design and **pseudoreplication**), and the phylogenetic comparative methods are developed in [7.10.26](/7.10.26).

## 2.1. Describing Behavior

### 2.1.1. The Ethogram

The first step in studying any species is to find out what it does. The classical ethologists began every study with a catalog of the species' behavior patterns.

**Definition 2.1.1 (Ethogram)** An **ethogram** is a catalog of the behavior patterns of a species, each defined clearly enough that different observers would classify the same act in the same way.

An ethogram can be complete, aiming to list every behavior the species shows, or restricted to the behaviors relevant to a question (for example, the courtship of the male three-spined stickleback). Each entry needs a name, a definition and, if possible, criteria for when the behavior starts and ends. A fragment of an ethogram for the courtship and parental behavior of the male three-spined stickleback (*Gasterosteus aculeatus*) might read:

| Behavior | Definition |
|---|---|
| Digging | Male takes sand into the mouth at the nest site and spits it out a few centimeters away, forming a shallow pit |
| Gluing | Male moves slowly over the nest material, pressing the cloaca against it and secreting a sticky kidney secretion |
| Zigzag dance | Alternating sideways leaps toward and away from a female, with mouth open, at a rate of about 2 per second |
| Leading | Male swims toward the nest with the dorsal spines erect, looking back at the female |
| Showing the entrance | Male lies on his side at the nest, snout pointing into the entrance |
| Fanning | Male hangs over the nest entrance and beats the pectoral fins alternately, driving water through the nest |

The stickleback is a good example because its behavior changes conspicuously through the year. In winter the fish live in schools and are dull gray; in spring each male claims a territory, digs a pit, builds a tunnel-shaped nest of algae glued with a secretion of the kidneys, and develops a red throat and belly and bright blue eyes. The courtship sequence that follows, and the stimuli that release each step, became one of the founding examples of ethology ([7.18.3](/7.18.3)).

### 2.1.2. Units and Categories

Behavior can be described in two ways. A description by *structure* specifies the form of the movement: the posture, the sequence of muscle contractions, the sounds produced ("tail raised to vertical, wings drooped, head forward"). A description by *consequence* specifies the effect of the action on the environment or on other individuals, regardless of how it is achieved ("approach", "obtains food", "presses lever"). Structural descriptions are more objective and allow comparison of the form of displays between species; descriptions by consequence are more economical and capture actions that vary in form but have the same effect. The behaviorist's lever press is a description by consequence: the rat may press the lever with a paw, its nose or its tail.

Behavioral categories are also distinguished by their time structure. *Events* are behaviors of short duration that can be counted as points in time (a peck, a call, a wing flick); *states* are behaviors of appreciable duration (sleeping, feeding, incubating) that are measured by their duration and frequency. Common measures are:

| Measure | Definition | Example |
|---|---|---|
| Latency | Time from a reference event to the first occurrence of the behavior | Time from the presentation of a female to the first zigzag |
| Frequency (rate) | Number of occurrences per unit time | Songs per hour |
| Duration | Length of a single occurrence, or total time spent | Mean bout length of feeding; proportion of time incubating |
| Intensity | Strength of the behavior, often scored on a scale | Number of components of a threat display shown |
| Sequence | Order in which behaviors follow each other | Transition probabilities between courtship elements |

Many behaviors occur in *bouts*, clusters of occurrences separated by longer gaps (a bird pecks several times, pauses, pecks again). Defining bouts requires a criterion for the gap that ends a bout, usually found from the distribution of the intervals between occurrences: within-bout and between-bout intervals form two distributions that can be separated by plotting the log-survivorship curve of intervals or by fitting a mixture model.

### 2.1.3. Classifying Behavior

Behaviors are grouped into broader classes for convenience. Traditional functional classes include maintenance behavior (feeding, drinking, grooming, resting), defense against predators, agonistic behavior (attack, threat, submission, flight), sexual behavior, parental behavior, and social behavior more generally. Older classifications also distinguished "innate" and "learned" behavior and "simple" reflexes, kineses and taxes from "complex" instinctive and intelligent behavior. Such classes are useful as headings, but they mix structure, mechanism and function and should not be mistaken for natural kinds. A behavior such as preening can be maintenance in one context and a displacement activity in another ([7.18.3](/7.18.3)); the orientation behaviors (kineses and taxes) are treated in [7.18.12](/7.18.12).

## 2.2. Measuring Behavior

### 2.2.1. Sampling Rules and Recording Rules

An observer cannot record everything that every animal does. Two decisions are required: which animals to watch and when (the *sampling rule*), and how to record what they do (the *recording rule*). The terminology follows Jeanne Altmann's classic review (1974), which showed that many published behavioral data were biased by poorly chosen methods.

**Definition 2.2.1 (Sampling and Recording Rules)** The main sampling rules are **ad libitum sampling**, recording whatever is visible and seems relevant, with no systematic constraint; **focal sampling** (focal animal sampling), watching one individual (or one pair or group) for a specified period and recording all instances of the behaviors of interest; **scan sampling**, scanning a whole group at regular intervals and recording the behavior of each individual at that instant; and **behavior sampling**, watching the whole group and recording each occurrence of a particular behavior and the individuals involved. The recording rules are **continuous recording** (all-occurrences recording), which records every occurrence and its start and end times; and time sampling, either **instantaneous sampling** (point sampling), which records at regular sample points whether the behavior is occurring at that instant, or **one–zero sampling**, which records at the end of each sample interval whether the behavior occurred at any time during the interval.

Each method has its uses and biases.

| Method | Gives | Main bias or limitation |
|---|---|---|
| Ad libitum | Rare or unexpected events; preliminary observations | Biased toward conspicuous behaviors and individuals; no valid rates |
| Focal sampling with continuous recording | True frequencies, durations, latencies and sequences for one individual | Focal animal may move out of view (time out of sight must be recorded); few individuals per session |
| Scan sampling with instantaneous recording | Proportion of time spent in each state by all group members; activity budgets | Conspicuous behaviors are noticed more readily during a scan; scans must be quick; events are missed |
| Behavior sampling | Rare but important events (fights, copulations) in the whole group | Only for conspicuous behaviors; no information on other behaviors |
| Instantaneous sampling | Unbiased estimate of the proportion of time spent in a state if the interval is short relative to bouts | Not suitable for events; poor estimate of frequency |
| One–zero sampling | Simple to score; a rough index of how often a behavior occurs | Systematically biased: overestimates the time spent in a state and underestimates frequency, more so with long intervals |

The bias of one–zero sampling is easy to see. An interval is scored as "yes" if the behavior occupied any part of it, so a state that fills only a small fraction of an interval counts as if it filled all of it; the estimated proportion of time therefore exceeds the true proportion, and the error grows with the length of the interval. Instantaneous sampling, by contrast, is an unbiased estimator of the proportion of time, because each sample point is a random sample of the time line, but its variance is high if points are few and it misses events altogether. Continuous recording avoids both problems but is demanding: an observer can record continuously only a few behaviors of one animal at a time.

![Recording rules applied to the same simulated stream of behavior (feeding bouts with exponentially distributed durations, mean 20 s, separated by non-feeding gaps with mean 40 s; true proportion of time feeding 1/3). A: a 10-minute session. Continuous recording (top) captures every bout; instantaneous sampling every 30 s scores the state at each point (filled: feeding); one–zero sampling scores each 30-s interval as positive if feeding occurred at any time in it (shaded). B: mean estimate of the proportion of time feeding over 400 simulated sessions, as a function of the sample interval. Instantaneous sampling is unbiased at all intervals; one–zero sampling overestimates the proportion, increasingly so as the interval lengthens](./plots/sampling-methods.py)

The choice of method depends on the question. For an activity budget of a whole troop of baboons, scan sampling with instantaneous recording is efficient. For the rate of aggressive interactions given and received by each individual, focal sampling with continuous recording is needed. For copulations, which are rare and conspicuous, behavior sampling of the whole group gives the most data. The sampling schedule itself must avoid bias: focal individuals should be chosen in a predetermined random or rotating order, and observation sessions should be spread across times of day and seasons, since behavior varies with both.

### 2.2.2. Reliability and Validity

A measurement is *reliable* if it is repeatable: the same observer, or different observers, scoring the same behavior obtain the same result. A measurement is *valid* if it measures what it is supposed to measure: the number of songs per hour may or may not be a valid measure of a male's "motivation to court". Reliability is tested by having two observers score the same sample independently, for instance from video, and computing an agreement statistic. The proportion of agreements is inflated by chance agreement when one category is common, so the preferred statistic for categorical data is Cohen's kappa, $\kappa = (p_{\mathrm{o}} - p_{\mathrm{e}})/(1 - p_{\mathrm{e}})$, where $p_{\mathrm{o}}$ is the observed proportion of agreement and $p_{\mathrm{e}}$ the proportion expected by chance from the marginal frequencies; for continuous measures, the correlation between observers or the intraclass correlation is used. Reliability should be checked repeatedly during a long study, because an observer's criteria can change gradually without his noticing (observer drift).

Observers are also subject to expectation. An observer who knows which treatment an animal received, or which result is predicted, can unconsciously score ambiguous behavior in the expected direction, the lesson of Clever Hans ([7.18.1](/7.18.1)). The remedy is blind scoring: the person who scores behavior does not know the treatment, for example by scoring coded video files in random order. Surveys of the behavioral literature have found that only a small minority of studies report blind observation (Burghardt and colleagues, 2012), and across the life sciences, studies that were not blind tend to report larger effects than blind studies of the same question (Holman and colleagues, 2015).

### 2.2.3. From Stopwatches to Machine Learning

Until the 1990s, behavior was recorded with check sheets, stopwatches and event recorders, and sound with tape recorders. Today, much of the recording is automated. Video tracking software follows the position of one or many animals in a frame and computes speed, distances and interactions; radio telemetry, GPS loggers, accelerometers and other biologgers record the location, movement and even the heart rate of free-living animals over months ([7.18.20](/7.18.20)); passive integrated transponder (PIT) tags register individuals at feeders and nest boxes; and arrays of microphones record and localize vocalizations.

The most recent advance is *pose estimation*: deep neural networks trained on a few hundred hand-labeled frames locate body parts (the nose, the joints of each leg, the tip of the tail) in every frame of a video, for many individuals and from several camera angles (DeepLabCut, Mathis et al. 2018; SLEAP, Pereira et al. 2022). From the time series of body-part positions, behaviors can be classified by supervised learning from examples labeled by a human, or discovered without labels by unsupervised methods that segment the continuous pose trajectory into recurring motifs. Applied to mice moving freely in an arena, such methods (for instance motion sequencing, MoSeq, Wiltschko et al. 2015) decompose behavior into short "syllables" of about a third of a second, organized by a grammar of transitions, and reveal changes in behavior after drugs or genetic manipulations that human observers had missed. The methods are described with the other techniques of neuroscience in [7.16.3](/7.16.3#sec-3.7).

Automation does not remove the need for an ethogram. The categories found by an algorithm must still be interpreted biologically, and a classifier trained in one setting may fail in another (a different arena, lighting or strain). Nor does it remove the need for direct observation in the field, where much behavior happens out of sight of cameras and where the natural history of a species suggests the questions worth asking.

## 2.3. Testing Hypotheses by Comparison

### 2.3.1. The Comparative Approach

The **comparative method** tests hypotheses about adaptation by relating differences in behavior among species to differences in their ecology. Its logic was introduced in [7.18.1](/7.18.1): closely related species tend to be similar because of shared ancestry, so when related species differ, the difference may reveal the effect of a different selective pressure; and unrelated species that live under similar conditions may converge on similar adaptations.

The founding example is Esther Cullen's (1957) comparison of the black-legged kittiwake with ground-nesting gulls. Kittiwakes nest on narrow ledges of steep cliffs, where predation on eggs and chicks is low. Cullen found that a whole suite of kittiwake traits differs from those of ground-nesting gulls, and that most differences make sense as consequences of cliff nesting:

| Trait | Ground-nesting gulls (e.g., black-headed gull) | Kittiwake (cliff ledges) | Interpretation |
|---|---|---|---|
| Alarm calls and mobbing | Frequent | Rare | Little predation on nests |
| Removal of eggshells | Shells carried away after hatching | Shells left at the nest | No need to maintain camouflage |
| Eggs and chicks | Camouflaged | Less camouflaged | No need for crypsis |
| Nest | Simple scrape | Elaborate nest of mud and weed, with a deep cup | Prevents eggs and chicks from falling |
| Chicks | Run and hide when disturbed | Stay still in the nest, face the cliff | Running on a ledge is fatal |
| Fighting | Pulling and pecking, from above | Grabbing the bill and twisting | Fighting on a narrow ledge |
| Clutch size | Usually 3 | Usually 2 | Space and food limits on a ledge |
| Feeding of chicks | Food regurgitated on the ground | Chicks take food from the parent's throat | Food dropped on a ledge is lost |

The comparison is compelling because many independent traits change in the direction predicted by a single difference in nest site. It is also an example of the general point that behavior is an integrated part of an animal's design: changing one feature of the ecology changes many behaviors at once.

### 2.3.2. Comparisons across Many Species

The next step was to compare many species at once. John Crook (1964) classified about 90 species of weaverbirds (Ploceidae) in Africa and Asia by diet, habitat, nest dispersion and mating system, and found a striking association. Species living in forest mostly eat insects, nest solitarily in defended territories, build cryptic nests, and are monogamous, with males and females similar in color. Species of the open savanna mostly eat seeds, nest in colonies, often in thorny trees, and are often polygynous, with males brightly colored and females dull. Crook interpreted these patterns as follows. In forest, insects are scattered and both parents are needed to provide enough food for the young, which favors monogamy; scattered cryptic nests reduce predation. In savanna, seeds are patchily distributed but locally abundant, so birds forage in flocks; nest sites safe from predators are scarce, so birds nest in colonies in the few suitable trees; and because food is abundant enough for a female to feed the young alone, some males can attract several females and the others none ([7.18.30](/7.18.30)).

Peter Jarman (1974) made a similar analysis of African antelopes and buffalo. Small species such as dik-diks (*Madoqua*) live in forest and dense bush, are selective browsers on high-quality but scattered plant parts (buds, fruits, young leaves), live singly or in pairs and defend small territories year-round. Medium-sized species such as gazelles and impala feed on grass and browse in more open country and live in herds of moderate size, with males defending temporary territories or harems. The largest grazers, such as wildebeest and African buffalo, eat abundant low-quality grass on open plains, form large herds, sometimes of thousands, and males compete for females within the herd. Jarman's explanation linked body size, diet and grouping: small animals have high metabolic needs per unit mass, which requires high-quality food that is scattered and cannot support groups; large animals can digest abundant poor food, which allows large groups, and in the open, large groups offer protection from predators.

Clutton-Brock and Harvey (1977) and later studies applied the same approach to primates, quantitatively. Across species, the home range of a group increases with the total body weight of the group, and more steeply in leaf-eaters than in fruit-eaters, because fruit is more scattered than leaves. Combined testis weight, relative to body weight, is larger in species in which several males mate with each female (chimpanzees, many macaques) than in species with one breeding male per group (gorillas) or monogamous pairs (gibbons), as predicted if large testes evolve under **sperm competition** (Harcourt et al. 1981; [7.18.28](/7.18.28)). The degree of sexual dimorphism in body size is larger in species in which males compete for harems.

### 2.3.3. Limitations of Early Comparative Studies

These studies were influential, but they had four weaknesses that later work corrected.

1. *Categories were subjective.* Classifying a species as "forest" or "savanna", "insectivorous" or "granivorous" loses information and depends on the investigator's judgment. Modern studies measure variables quantitatively.
2. *Confounding variables.* Many ecological variables covary. Did coloniality in weaverbirds evolve because of the distribution of food or the scarcity of safe nest sites? Since the two go together in savanna, the comparison alone cannot separate them. Like any observational study, a comparison establishes association, not causation (**confounding**, [3.8.2](/3.8.2)).
3. *Alternative explanations of the same correlation.* A correlation between two traits can arise because one causes the other, because both are caused by a third, or because both are consequences of the same history.
4. *Species are not independent data points.* This is the most serious problem. Closely related species share traits by common descent, so ten species of savanna weavers descended from one colonial, seed-eating ancestor may provide only one independent instance of the association between savanna, seeds and colonies, not ten. Treating species as independent inflates the apparent sample size and the rate of false positives.

The last problem is solved by phylogenetic comparative methods ([7.10.26](/7.10.26)). Felsenstein's (1985) method of **phylogenetically independent contrasts** computes, at each node of a phylogeny, the difference between the trait values of its two descendant lineages, scaled by the branch lengths; under a model of Brownian-motion evolution, these contrasts are independent of each other and can be analyzed by standard regression through the origin. The question changes from "do species with trait $X$ also have trait $Y$?" to "when $X$ evolved to be larger, did $Y$ also evolve to be larger?". An equivalent approach is phylogenetic generalized least squares, which incorporates the expected covariance between species due to shared history into a regression. For discrete traits, such as the presence or absence of a behavior, methods such as Pagel's (1994) test whether changes in one trait along the phylogeny are associated with changes in another.

![Why species are not independent data points. Two traits were simulated by independent Brownian motion on a phylogeny of 16 species in two clades separated by a long internal branch; the traits are truly uncorrelated. A: one simulation, species colored by clade. Because the clades differ by chance in both traits, the species appear correlated, although within each clade there is no association. B: distribution of the correlation coefficient over 2000 simulations, computed from species values (wide) and from Felsenstein's independent contrasts (narrow, centered on zero). The proportions of simulations significant at the 5% level are given; analyzing raw species values inflates the rate of false positives far above 5%](./plots/comparative-nonindependence.py)

A modern example is the evolution of song complexity in European warblers. Across species, the size of the song repertoire correlates with the volume of the song-control nucleus HVC in the brain. Using independent contrasts, Székely, Catchpole and colleagues (1996) showed that the correlation persists among contrasts: where repertoire size increased during the evolution of warblers, HVC volume increased too, so the association is not an artifact of shared ancestry ([7.18.17](/7.18.17)). The comparative method can also reconstruct the order of events. For example, analyses of primates using Pagel's method suggested that the exaggerated sexual swellings of females evolved repeatedly in species living in multimale groups, consistent with the hypothesis that swellings advertise fertility in mating systems with intense competition among males (Nunn 1999).

## 2.4. Testing Hypotheses by Experiment

### 2.4.1. The Logic of Experiments

Comparisons and observations reveal associations; experiments test causation. In an experiment the researcher manipulates one variable (the treatment), keeps others constant or randomizes them across treatments, and measures the effect on behavior. The key elements are a control group that experiences everything except the treatment (including a sham manipulation, when the manipulation itself might have effects), random assignment of individuals to treatments (**randomization**), replication with independent units, and blind recording. Field experiments combine the control of manipulation with the realism of natural conditions and are a hallmark of behavioral ecology.

### 2.4.2. Plumage Color in House Finches

Male house finches (*Haemorhous mexicanus*, formerly *Carpodacus mexicanus*) vary greatly in the color of the plumage of the head and breast, from pale yellow through orange to bright red. The red color comes from carotenoid pigments that the birds cannot synthesize and must obtain from their food, so males in good nutritional condition can grow redder feathers. Geoffrey Hill (1990, 1991) found in observations of a wild population in Michigan that redder males paired earlier in the breeding season, and in aviary choice tests that females preferred redder males. But observations cannot separate the effect of color from that of correlated male qualities (redder males might also be healthier, older or hold better territories). Hill therefore manipulated color directly. Before the breeding season he captured males and either brightened their plumage with red hair dye, lightened it with a bleaching agent, or treated it with a sham dye that did not change its color, and released them.

| Male characteristic | Brightened ($n = 40$) | Sham control ($n = 20$) | Lightened ($n = 40$) | $p$ |
|---|---|---|---|---|
| Original plumage score | 140.7 | 139.9 | 141.0 | 0.95 |
| Manipulated plumage score | 161.6 | 139.9 | 129.4 | 0.0001 |
| Proportion paired | 1.00 | 0.60 | 0.27 | 0.0001 |
| Time to pair (days) | 12.1 | 20.2 | 27.8 | 0.07 |

The design has several features worth noting. Before manipulation the three groups did not differ in plumage (the first row), so any difference afterward is due to the treatment; the sham control controls for capture, handling and the smell of dye; and because males were assigned to treatments at random, other male qualities are on average equal across groups. The result was clear: all brightened males obtained mates, compared with 60% of controls and 27% of lightened males. The difference in the time to pair was in the same direction but not statistically significant at the 5% level, which illustrates that a non-significant result is not evidence of no effect (**statistical power**, [7.7.6](/7.7.6#sec-6.4)). Together, the observations and the experiment show that female house finches choose mates by plumage color, a result that became central to the theory that ornaments signal male condition ([7.18.29](/7.18.29), [7.18.39](/7.18.39)).

![Hill's (1991) plumage manipulation in male house finches. Males were captured before the breeding season and their plumage was brightened with dye, treated with a colorless sham dye, or lightened. A: proportion of males that obtained a mate. B: mean number of days from the start of the season to pairing, for males that paired. Data from Hill (1991)](./plots/hill-house-finch.py)

### 2.4.3. Eggshell Removal in Gulls

A classic field experiment of Tinbergen and colleagues (1962) asked why black-headed gulls carry the broken eggshell away from the nest soon after a chick hatches. The eggs and chicks are camouflaged, but the inside of the shell is white and conspicuous. To test whether the shell attracts predators, Tinbergen painted hens' eggs to resemble gull eggs, laid them out singly in the dunes near the colony, and placed a broken shell 5 cm from half of them. Of 60 eggs with a shell nearby, 65% were taken by predators (mostly carrion crows and herring gulls), compared with 22% of 60 eggs without a shell. Further experiments showed that the risk decreased as the shell was placed farther away.

The experiment also revealed a trade-off. Gulls do not remove the shell immediately, but wait an hour or more after hatching. Tinbergen observed that a newly hatched chick, still wet, is easily swallowed by cannibalistic neighbors, whereas a dry, fluffy chick is not. A parent that leaves to remove the shell exposes its chick to cannibalism; the delay balances the benefit of camouflage against this cost. The oystercatcher (*Haematopus ostralegus*), a solitary ground-nesting bird whose neighbors pose no such threat, removes the shell almost immediately, as the trade-off hypothesis predicts. This is a comparison that tests an experimental conclusion, and shows how experimental and comparative approaches complement each other.

### 2.4.4. Optimality Models

The trade-off hypothesis for eggshell removal makes only a qualitative prediction: it would be consistent with removal after one hour or after four. A sharper test requires a quantitative prediction, which is the purpose of an optimality model.

**Definition 2.4.1 (Optimality Model)** An **optimality model** predicts the behavior that maximizes a specified currency (such as net rate of energy gain, survival or offspring production), given explicit assumptions about the options available to the animal (the decision variable) and the constraints that limit its performance.

An optimality model is not a claim that animals are perfect. It is a tool for generating testable predictions: if the observed behavior departs from the prediction, one of the assumptions (about the currency, the constraints or the options) is wrong, and the discrepancy shows where. A classic example is the analysis of whelk dropping by northwestern crows (*Corvus caurinus*) on the coast of British Columbia by Reto Zach (1979). Crows search the shore at low tide for whelks (*Nucella lamellosa*), fly up, and drop them onto rocks to break the shell. Zach observed that crows chose only the largest whelks, flew up to an average height of about 5.2 m, and dropped each whelk repeatedly until it broke. By dropping whelks himself from various heights, he found that the number of drops needed to break a large whelk decreased steeply with height up to about 5 m and only slowly beyond. Since flying upward is costly, the crow should minimize the total upward flight per whelk, the product of the height per drop and the number of drops, which is minimized near the observed height. Small whelks needed so many drops that eating them would have cost more energy than they yield; the crows ignored them, even when they were offered on the beach.

![An optimality model of whelk dropping by northwestern crows, illustrating Zach's (1979) argument with an illustrative breakage function $N(h) = 1 + k/(h - h_0)$ with $h_0 = 1.2$ m and $k = 12$ m, chosen to resemble his data for large whelks. A: number of drops needed to break a whelk as a function of drop height. B: total upward flight per whelk, $h N(h)$, which has a minimum near 5 m; the dashed line marks the mean height observed in crows (about 5.2 m)](./plots/crow-whelk.py)

For the model with breakage function $N(h) = 1 + k/(h - h_0)$, the total height $H(h) = h + kh/(h - h_0)$ has derivative $H'(h) = 1 - k h_0/(h - h_0)^2$, which vanishes at $h^* = h_0 + \sqrt{k h_0}$; with the values in the figure, $h^* \approx 5.0$ m. Optimality models of foraging are developed systematically in [7.18.22](/7.18.22) and [7.18.23](/7.18.23), and models of strategic interactions, in which the best behavior depends on what others do, in [7.18.25](/7.18.25).

## 2.5. Observers, Animals and Ethics

### 2.5.1. Observer Effects

Observing animals can change their behavior. Wild animals may flee, freeze, stop feeding or give alarm calls in the presence of an observer. The usual remedy is habituation: animals are exposed to the observer repeatedly until they ignore him, as Jane Goodall's chimpanzees did ([7.18.1](/7.18.1)). Habituation has its own costs: habituated animals may become less wary of poachers, and the presence of observers can attract or repel predators. Alternatives are observation from a hide or from a distance with optics, remote cameras and automatic recorders.

The methods used to identify individuals can also alter behavior. In a famous series of aviary experiments, Nancy Burley (1981, 1986) found that the colored plastic leg bands used to identify zebra finches (*Taeniopygia castanotis*) affected their attractiveness: females preferred males wearing red bands and males preferred females wearing black or pink bands, and birds with attractive bands had higher reproductive success. Marking schemes must therefore be balanced across treatments or chosen to avoid such effects. Radio collars and loggers add weight and drag (a rule of thumb is to keep devices below 3–5% of body mass for flying animals), and capture and handling cause stress responses that can last for hours.

### 2.5.2. Ethics and the Three Rs

Research on animals requires a justification proportional to the harm it may cause. The guiding principles are the *three Rs* proposed by William Russell and Rex Burch (1959): replacement of animal experiments by methods that do not use live animals where possible; reduction of the number of animals used to the minimum needed for a valid result (which requires adequate statistical design, since an underpowered study wastes all the animals it uses); and refinement of procedures to minimize pain and distress. Behavioral research is often less invasive than other animal research, but it raises its own issues: staged encounters between predators and prey or between rival males, social isolation, food deprivation, manipulation of nests and young, and disturbance of endangered species. Professional societies publish guidelines for the treatment of animals in behavioral research, and most countries require ethical review of studies before they begin. Some classic experiments, such as the social isolation of infant rhesus monkeys ([7.18.5](/7.18.5)), would not be approved today.

## 2.6. Statistical Pitfalls

Behavioral studies are prone to a few statistical errors, which are treated in detail in the statistics courses.

- **Pseudoreplication** (Hurlbert 1984; [7.7.12](/7.7.12#sec-12.7.4)): treating non-independent observations as independent replicates. Examples are counting repeated observations of the same individual as separate data points, testing many birds from the same few colonies as though each bird were an independent replicate of a colony-level treatment, and using a single recording of a song in a playback experiment to many males, so that any effect might be due to that particular recording rather than the class of songs it represents (McGregor and colleagues, 1992). The remedy is to identify the experimental unit (the unit to which the treatment is independently applied), to replicate at that level, and to use statistical models with random effects for individuals, groups or stimuli.
- Confusing statistical significance with biological importance. A $p$-value measures the compatibility of the data with the **null hypothesis**, not the size of an effect. Studies should report **effect sizes** with confidence intervals ([7.7.6](/7.7.6#sec-6.8.3)).
- Low **statistical power**. Small samples, common in behavioral studies of wild animals, give a high chance of missing real effects and, among the significant results that are published, exaggerated estimates of the effect.
- Multiple testing. Measuring many behaviors and testing each against the treatment inflates the chance of false positives; the hypotheses and the primary measures should be specified in advance, ideally preregistered, and corrections for multiple comparisons applied.
- Correlational data treated as causal. A correlation between behavior and fitness in an **observational study** may reflect a third variable; for example, birds that nest in dense colonies may also be older or occupy better habitat. Experiments, or careful statistical control of confounders, are needed before causal conclusions.

## Summary

- Description. An ethogram (Definition 2.1.1) catalogs a species' behavior patterns with operational definitions. Behavior can be described by structure or by consequence; events are counted, states are timed. Standard measures are latency, frequency, duration, intensity and sequence; bouts are defined from the distribution of intervals.
- Sampling and recording rules (Definition 2.2.1):

  | Question | Suitable method |
  |---|---|
  | Activity budget of a group | Scan sampling with instantaneous recording |
  | Rates, durations and sequences for individuals | Focal sampling with continuous recording |
  | Rare, conspicuous events | Behavior sampling |
  | Preliminary observations | Ad libitum sampling |

  Instantaneous sampling estimates the proportion of time without bias; one–zero sampling overestimates it.
- Measurements must be reliable (Cohen's $\kappa$ between observers) and valid, and scored blind. Automated tracking, biologging and deep-learning pose estimation now record behavior at scale, and unsupervised methods decompose it into recurring motifs.
- Comparison. Cullen's kittiwakes, Crook's weaverbirds, Jarman's antelopes and primate testis size show how behavior covaries with ecology. Early studies suffered from subjective categories, confounding and above all the non-independence of species; **phylogenetically independent contrasts** and related methods solve the last problem.
- Experiment. Manipulation with sham controls, randomization, replication and blind scoring establishes causation, as in Hill's plumage manipulation in house finches and Tinbergen's eggshell experiment, which also revealed a trade-off with chick cannibalism.
- An optimality model (Definition 2.4.1) makes quantitative predictions from an explicit currency and constraints; Zach's crows drop whelks from about the height that minimizes total upward flight.
- Observers and marking alter behavior; research follows the three Rs (replacement, reduction, refinement). Common statistical pitfalls are **pseudoreplication**, ignoring effect sizes and power, multiple testing, and causal interpretation of correlations.

## Questions

1. You want to estimate the proportion of daylight time that a troop of 30 baboons spends feeding, resting, moving and grooming. Which sampling and recording rules would you use, and why? What if you instead wanted the rate at which each adult female is groomed by others?

   **Answer** For the activity budget of the troop, scan sampling with instantaneous recording: at regular intervals (for example every 10 minutes) the observer scans the troop and records the state of each visible individual, which gives an unbiased estimate of the proportion of time spent in each state, pooled over many animals. The scans must be quick and systematic to avoid bias toward conspicuous animals. For the rate of being groomed, focal sampling with continuous recording of each adult female in turn, recording every grooming bout received, its start and end, and the groomer; the time the focal female is out of sight must be recorded and subtracted. Focal females should be sampled in a predetermined order balanced across times of day.
2. Explain why one–zero sampling overestimates the proportion of time spent in a state. Is there any situation in which one–zero sampling is the preferable method?

   **Answer** An interval is scored positive if the state occurs at any time within it, so an interval in which the state occupies only a short part is counted as wholly positive; the estimate therefore exceeds the true proportion unless bouts are much longer than the interval, and the bias increases with the interval length. One–zero scores also do not measure frequency, because several short bouts in one interval count once. It can still be useful when the behavior consists of brief, intermittent acts that are hard to time (for instance play or bouts of short calls), when the aim is only to compare an index of occurrence between treatments sampled with the same interval, or when the observer must monitor several animals or behaviors simultaneously; the index should then not be interpreted as a proportion of time.
3. Two observers classified 200 video clips of a lizard as "display" or "no display". They agreed on 180 clips. Observer 1 scored 20 clips as display and observer 2 scored 30, with 15 clips scored as display by both. Compute the proportion of agreement and Cohen's $\kappa$, and comment.

   **Answer** The proportion of agreement is $p_{\mathrm{o}} = 180/200 = 0.90$. (Agreements are the 15 clips scored as display by both and 165 scored as no display by both: $200 - 15 - 5 - 15 = 165$, total 180.) The chance agreement is $p_{\mathrm{e}} = (20/200)(30/200) + (180/200)(170/200) = 0.015 + 0.765 = 0.78$. So $\kappa = (0.90 - 0.78)/(1 - 0.78) = 0.12/0.22 \approx 0.55$. The high raw agreement mostly reflects the fact that "no display" is common; agreement on displays themselves is only moderate ($\kappa \approx 0.55$), so the definition of a display should be sharpened and the observers retrained before data collection.
4. Crook found that savanna weaverbirds are colonial and often polygynous, and forest weaverbirds are solitary and monogamous. List the reasons why this correlation alone does not show that the habitat caused the mating system. How would a modern study test the hypothesis?

   **Answer** (1) Species are not independent: colonial polygynous species may descend from one ancestor, so the number of independent evolutionary origins of the association may be small. (2) Habitat covaries with diet, nest-site availability, predation and body size, so any of these could be the cause. (3) Categories such as "savanna" and "polygynous" are coarse. (4) The direction of causation is unclear (could coloniality have allowed polygyny, independently of habitat?). A modern study would measure the variables quantitatively for many species, build a phylogeny from DNA sequences, test for correlated evolution with phylogenetic methods (independent contrasts or phylogenetic regression for continuous variables, Pagel's method for discrete ones), use multiple regression to separate the effects of correlated ecological variables, and test the proposed mechanisms (for example, whether females can rear young alone in savanna) by experiments such as removing males in the field.
5. In Hill's experiment, why was the sham control necessary, and why does the first row of the table matter? What would you conclude if lightened males had paired as often as controls but brightened males more often?

   **Answer** The sham control experienced capture, handling and application of a dye solution without the color change, so a difference between brightened or lightened males and sham controls can be attributed to color rather than to handling or the smell of dye. The first row shows that the groups did not differ in plumage before treatment, as expected from random assignment, so differences afterward are due to the manipulation. If lightened males had paired as often as controls but brightened males more often, the conclusion would be that unusually red plumage increases attractiveness but that reducing redness within the natural range has no detectable effect; this might mean that females prefer the reddest males available but do not reject pale ones, or that the experiment lacked power to detect a smaller effect of lightening.
6. Using the whelk-dropping model of §2.4.4, derive the optimal drop height and explain how it would change if the whelk were smaller (harder to break, so $k$ larger) or if the rocks were harder (so $h_0$ smaller).

   **Answer** The total height is $H(h) = hN(h) = h + kh/(h - h_0)$, with $H'(h) = 1 - kh_0/(h - h_0)^2$. Setting $H'(h) = 0$ gives $h^* = h_0 + \sqrt{kh_0}$. A larger $k$ increases $h^*$ and also the minimum total height, so smaller whelks should be dropped from higher, and their cost per unit of food is larger, which can make them unprofitable, as Zach observed. A smaller $h_0$ (harder rocks, so that even low drops have some chance of breaking the shell) decreases $h^*$.
7. A researcher plays back a recording of a "dominant" call and a "subordinate" call to 30 territorial males each, using one recording of each call type, and finds a significant difference in response. What is wrong with the design, and how should it be improved?

   **Answer** The two treatments are represented by only one recording each, so the experiment has one replicate per treatment at the level of the stimulus. Any difference between the recordings (in loudness, background noise, the individual caller) is confounded with the call type; the 30 males are pseudoreplicates with respect to the question about call types. The design should use many different recordings of each type, ideally from different callers, each played to one or a few males, assigned at random, with stimulus identity included as a random effect in the analysis, and with the response scored blind to the treatment.
8. (Open question) Choose a behavior you can observe near you (for example, pigeons feeding in a square or ants at a food source). Write a short ethogram, state a hypothesis about the function of one behavior, and design an observational and an experimental test.

   **Answer** Example: feral pigeons feeding in a square. Ethogram: pecking (head moves down, bill contacts ground), walking, vigilance (head up, stationary, for at least 1 s), displacement (one bird approaches and another moves away within 1 s), courtship (male bows and coos, circling a female), flight. Hypothesis: vigilance is antipredator behavior, and individuals in larger flocks can be less vigilant because more eyes detect danger. Observational test: focal sampling of individuals with continuous recording of head-up time, for flocks of different sizes, controlling for distance to cover and time of day; prediction: the proportion of time vigilant declines with flock size. Experimental test: scatter food to create flocks of controlled size (for instance by varying the area of food), or present a model predator, and measure detection latency and vigilance; with a predetermined analysis, random order of treatments and blind scoring of video.
