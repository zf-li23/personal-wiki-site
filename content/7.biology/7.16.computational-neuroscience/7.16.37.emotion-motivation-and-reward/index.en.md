---
title: Emotion, Motivation and Reward
description: "Emotions as internal states with scalability, persistence, generalization and valence; fear conditioning in the amygdala, from CS–US convergence in the lateral amygdala to central amygdala output, and extinction as new learning; the mesolimbic dopamine system, intracranial self-stimulation and the distinction between wanting and liking; the reward prediction error response of dopamine neurons; addiction as a disorder of reward learning, with opponent-process and prediction-error models; the coding of valence."
---

Why does an animal approach some things and avoid others, and why do some events change behavior long after they are over? The answers lie in a set of brain systems that assign value to stimuli and actions and that generate internal states, emotions and motivations, which organize behavior around these values. This chapter treats two of them in detail: the amygdala, the best-understood circuit for learned fear, and the midbrain dopamine system, which signals the difference between the reward received and the reward expected. The latter observation connects neuroscience to the theory of **reinforcement learning**, developed in [7.16.39](/7.16.39), [7.16.40](/7.16.40) and [7.16.41](/7.16.41); here we describe the circuits and the data that the theory must explain. Hunger and thirst as drives were treated in [7.16.34](/7.16.34), the **limbic system** and its classical lesion and stimulation experiments in [7.14.46](/7.14.46#sec-46.6), and the dopamine system as a **neuromodulator** system in [7.16.11](/7.16.11#sec-11.4).

## 37.1. Emotions as Internal States

The word emotion covers three things that are easy to confuse: the bodily and behavioral responses (heart rate, hormones, freezing, facial expression), the conscious feeling, and the central state that produces both. William James and Carl Lange proposed that feelings are the perception of bodily changes; Walter Cannon and Philip Bard objected that visceral responses are too slow and too undifferentiated to account for different emotions, and that animals deprived of visceral feedback still display emotional behavior. Modern neuroscience retains elements of both: interoceptive signals from the body ([7.16.34](/7.16.34)) contribute to feelings, and central circuits generate states that coordinate responses.

**Definition 37.1.1 (Emotion State)** An **emotion state** is a central internal state of the brain, elicited by stimuli of biological significance, that causes coordinated changes in behavior, physiology and cognition and is characterized by scalability (graded intensity), persistence (it outlasts the stimulus), generalization (it affects responses to other stimuli) and valence (it is positive or negative, so that animals approach or avoid what elicits it) (Anderson and Adolphs, 2014).

The definition is operational: it can be applied to flies and mice as well as to humans, without asking what an animal feels. A fly startled by repeated passing shadows runs faster, keeps running after the shadows stop and becomes less responsive to food, a defensive state with all four properties. Persistence and scalability, as seen in the aggressive state of [7.16.36](/7.16.36#sec-36.3.2), can be implemented by slow modes of recurrent networks or by slow neuromodulatory and peptidergic signals; valence is the subject of Section 37.6.

## 37.2. Fear Conditioning and the Amygdala

### 37.2.1. The Paradigm

**Definition 37.2.1 (Fear Conditioning)** **Fear conditioning** is a form of **Pavlovian conditioning** in which a neutral conditioned stimulus (CS), such as a tone, is paired with an aversive unconditioned stimulus (US), such as a mild foot shock, so that the CS alone comes to evoke defensive responses: freezing, a rise of heart rate and blood pressure, release of stress hormones and potentiated startle.

Fear conditioning is fast (one pairing can suffice), lasting (months) and conserved from flies to humans; in humans it can be measured by the skin conductance response. Its acquisition is described by the same error-correcting rule as other forms of Pavlovian learning, the **Rescorla–Wagner rule** ([7.16.39](/7.16.39)): the associative strength $V$ of the CS changes on each trial by $\Delta V = \alpha\beta(\lambda - V)$, where $\lambda$ is the strength the US supports (0 when the US is absent) and $\alpha\beta$ a learning rate. Learning is fast when the US is surprising and slows as it becomes predicted.

![Acquisition and extinction of conditioned fear with the Rescorla–Wagner rule ($\alpha\beta = 0.3$ during acquisition with tone–shock pairings, shaded; $\alpha\beta = 0.15$ during extinction with the tone alone; freezing $= 80\,V$ percent). The rule predicts exponential approach to the asymptote and exponential extinction. The red square marks the partial return of freezing when the animal is tested the next day (spontaneous recovery), which the rule, with a single associative strength, cannot produce.](./plots/fear-learning.py)

### 37.2.2. The Circuit

**Definition 37.2.2 (Amygdala)** The **amygdala** is a group of nuclei in the medial temporal lobe comprising the basolateral complex (lateral, basal and accessory basal nuclei), a cortex-like structure of glutamatergic projection neurons and GABAergic interneurons, and the central and medial nuclei, striatum-like structures composed mainly of GABAergic neurons; it assigns emotional significance to stimuli and controls defensive and other emotional responses.

The circuit of fear conditioning (LeDoux, Davis, Fanselow and others) has a clear input–output organization:

| Stage | Structure | Role |
|---|---|---|
| CS input | Auditory thalamus (medial geniculate) and auditory cortex to the lateral amygdala (LA) | The fast thalamic route carries a coarse signal, the cortical route a detailed one |
| US input | Nociceptive pathways via the parabrachial nucleus, thalamus and insular cortex to LA | Shock activates LA neurons strongly |
| Association | LA principal neurons | CS–US convergence; Hebbian potentiation of CS synapses |
| Context | Hippocampus to basal amygdala | Contextual fear (fear of the place of conditioning) |
| Output | Central amygdala (CeA): lateral (CeL) inhibits medial (CeM) | CeM projects to the periaqueductal gray (freezing), the lateral hypothalamus (sympathetic responses) and the PVH (stress hormones, the **hypothalamic–pituitary–adrenal axis**) |

The cellular mechanism of the CS–US association is synaptic plasticity at CS synapses on LA neurons. Conditioning increases the response of LA neurons to the CS (Quirk, Repa and LeDoux, 1995) and potentiates thalamo-amygdala synapses ex vivo and in vivo (Rogan, Stäubli and LeDoux, 1997; McKernan and Shinnick-Gallagher, 1997). Blocking **NMDA receptors** in LA during training prevents acquisition. The most direct test used **optogenetics**: rats were conditioned by pairing optogenetic stimulation of auditory inputs to LA with a shock; inducing **LTD** at these inputs afterward abolished the conditioned response, and inducing **LTP** again restored it (Nabavi and colleagues, 2014). The memory therefore resides, at least in part, in the strength of these synapses, a test of the synaptic hypothesis of memory ([7.16.14](/7.16.14#sec-14.1)).

Within LA, not all neurons store a given memory. Neurons with higher excitability (more active CREB) at the time of training are preferentially allocated to the memory trace, and their later ablation erases the memory (Han and colleagues, 2009). The output is gated by inhibition: in CeL, neurons expressing protein kinase C δ (PKCδ⁺) are inhibited by the CS after conditioning, which disinhibits CeM output neurons and produces freezing (Haubensak and colleagues, 2010; Ciocchi and colleagues, 2010). The output is thus a **disinhibition** circuit, like many motor selection circuits ([7.16.40](/7.16.40)).

### 37.2.3. Extinction

If the CS is presented repeatedly without the US, the conditioned response declines, a process called extinction. Extinction is not forgetting. The response returns spontaneously with time (spontaneous recovery), when the CS is presented outside the context of extinction (renewal), and after an unsignaled US (reinstatement). Extinction is therefore new learning, a second, context-dependent memory that the CS no longer predicts the US and that competes with the original memory. It requires the infralimbic part of the medial prefrontal cortex, whose activity during the recall of extinction inhibits CeA output through intercalated GABAergic cells and inhibitory interneurons of the basolateral amygdala, and the hippocampus, which supplies the context. A single associative strength, as in the Rescorla–Wagner rule, cannot account for spontaneous recovery; models that represent extinction as a separate inhibitory association, or as the inference of a new latent cause (a new "state of the world"; Gershman, Blei and Niv, 2010), can. Exposure therapy for anxiety disorders is a clinical application of extinction, and the return of fear after therapy corresponds to renewal and spontaneous recovery.

## 37.3. The Mesolimbic Dopamine System and Reward

### 37.3.1. Self-Stimulation

Olds and Milner (1954) discovered that rats press a lever thousands of times an hour to deliver electrical stimulation through electrodes in the septal area and medial forebrain bundle ([7.14.46](/7.14.46#sec-46.6)). The most effective sites lie along the axons of **dopamine** neurons of the ventral tegmental area (VTA) that project to the nucleus accumbens (ventral striatum) and prefrontal cortex, the mesolimbic and mesocortical pathways, and dopamine receptor antagonists reduce self-stimulation. Optogenetic stimulation of VTA dopamine neurons alone supports self-stimulation and conditioned place preference (Tsai and colleagues, 2009; Witten and colleagues, 2011).

**Definition 37.3.1 (Reward)** In behavioral neuroscience, a **reward** is an object, event or stimulus that an animal will work to obtain and that increases the frequency of behaviors that precede it (positive reinforcement); primary rewards (food, water, social contact) are rewarding without learning, and conditioned rewards acquire their value by association with primary rewards.

### 37.3.2. Wanting and Liking

The early "anhedonia" hypothesis held that dopamine produces the pleasure of reward. Berridge and Robinson tested it with the facial reactions that rats (like human infants) show to sweet tastes. Rats whose dopamine neurons were destroyed by 6-hydroxydopamine stop eating and do not work for food, yet show normal positive facial reactions to sucrose placed in the mouth; increasing dopamine raises the effort rats expend for a reward without increasing these reactions. Berridge therefore distinguished two components of reward:

| Component | Meaning | Main substrates |
|---|---|---|
| Wanting (incentive salience) | Motivation to obtain a reward; cues become attractive and energize approach | Mesolimbic dopamine |
| Liking (hedonic impact) | The pleasure of consuming it | Opioid, **endocannabinoid** and orexin signaling in small hotspots of the nucleus accumbens shell and ventral pallidum |
| Learning | Predictions and associations about rewards | Dopamine prediction errors (Section 37.4) |

Dopamine also scales vigor and effort: dopamine-depleted rats choose a freely available, less preferred food over a preferred food that requires effort (Salamone), and tonic dopamine levels in the striatum correlate with the rate at which animals act, which **reinforcement learning** interprets as the average reward rate that sets the cost of time (Niv and colleagues, 2007).

## 37.4. The Dopamine Prediction Error

Schultz and colleagues recorded single dopamine neurons in the VTA and substantia nigra of monkeys learning that a visual or auditory cue predicted a drop of juice (reviewed by Schultz, Dayan and Montague, 1997). The neurons fire tonically at a few spikes per second and respond to rewards with a brief burst of about $100$–$200\,\mathrm{ms}$ at a latency of about $100\,\mathrm{ms}$. Their responses follow three rules:

1. A reward that is not predicted evokes a burst.
2. After learning, the cue that predicts the reward evokes a burst and the fully predicted reward evokes none.
3. If a predicted reward is omitted, the neurons pause, briefly falling silent, at the time the reward should have occurred.

![Responses of a dopamine neuron in the three conditions of the experiments of Schultz and colleagues (simulated peri-stimulus time histograms reproducing the published data shapes; 20 trials, baseline $4\,\mathrm{Hz}$). Top: an unpredicted reward evokes a burst. Middle: after training, the conditioned stimulus (CS) evokes the burst and the predicted reward has no effect. Bottom: when the predicted reward is omitted, the neuron pauses at the expected time of reward.](./plots/schultz-rpe.py)

**Definition 37.4.1 (Reward Prediction Error)** A **reward prediction error** is the difference between the reward received (including the value of the situation it leads to) and the reward predicted; it is positive when outcomes are better than expected, zero when they are as expected and negative when they are worse.

The three rules are exactly those of a reward prediction error, and further experiments confirmed the quantitative correspondence. When a cue predicts reward with probability $p$, the cue response grows with $p$ and the reward response with $1 - p$ (Fiorillo, Tobler and Schultz, 2003); when cues predict different reward magnitudes, the reward response is proportional to the difference between received and expected magnitude; and in the blocking paradigm, in which a new cue added to an already predictive cue is not learned because the reward is already predicted, dopamine neurons do not respond to the blocked cue (Waelti, Dickinson and Schultz, 2001). In mice, optogenetic identification of VTA dopamine neurons showed that their reward responses are reduced by expectation in a subtractive manner, and that neighboring VTA GABA neurons carry an expectation signal that could supply the subtracted term (Cohen and colleagues, 2012; Eshel and colleagues, 2015).

The causal test asks whether a dopamine burst can substitute for a prediction error. In a blocking design, rats normally fail to learn about a cue added to a fully predictive one; optogenetic stimulation of dopamine neurons at the time of the (predicted) reward made them learn about the added cue (Steinberg and colleagues, 2013), and optogenetic inhibition at the time of an expected reward produced learning as if the reward had been omitted (Chang and colleagues, 2016). The prediction error interpretation leads directly to the temporal-difference model of [7.16.39](/7.16.39), which explains why the burst moves from the reward to the earliest predictive cue.

Not all dopamine neurons conform. Neurons projecting to the tail of the striatum respond to novel and threatening stimuli and support avoidance; some respond to salient events of either valence; and the population carries a distribution of prediction errors rather than a single value ([7.16.39](/7.16.39)). The broad picture, a prediction error that drives learning in its targets through **three-factor learning rules** ([7.16.14](/7.16.14#sec-14.9)), applies best to the VTA and ventral SNc neurons projecting to the ventral and dorsomedial striatum.

## 37.5. Addiction

**Definition 37.5.1 (Addiction)** **Addiction** (substance use disorder in clinical terms) is a chronic, relapsing disorder in which the use of a drug, or a behavior such as gambling, continues compulsively despite adverse consequences, accompanied by loss of control over intake, craving, and negative emotional states when the drug is unavailable.

### 37.5.1. A Common Target

Addictive drugs differ in their molecular targets but share one action: all of them increase dopamine in the nucleus accumbens (Di Chiara and Imperato, 1988). Psychostimulants act on the dopamine transporter, either blocking reuptake or reversing transport; opioids inhibit GABAergic interneurons of the VTA through μ-opioid receptors and so disinhibit dopamine neurons; nicotine activates nicotinic receptors on dopamine neurons; alcohol and cannabinoids act indirectly through several of these routes. Natural rewards also release dopamine, but their prediction error disappears once they are predicted. Drug-evoked dopamine does not depend on a prediction and so cannot be predicted away, which suggested a computational account (Redish, 2004).

**Formula 37.5.1 (Prediction Error with a Pharmacological Component)** If a drug adds a dopamine signal $d > 0$ that cannot be cancelled by learning, the prediction error is
$$
\delta_t = \max\bigl(r_t + \gamma\,\hat v(S_{t+1}) - \hat v(S_t) + d,\; d\bigr),
$$
where $\hat v$ is the learned value of states (**temporal-difference learning**, [7.16.39](/7.16.39)). Because $\delta_t \ge d > 0$ on every drug-associated transition, the learned value of the states and actions that lead to the drug grows without bound, whereas for natural rewards $\delta_t \to 0$ as the value converges.

The model explains why drug-associated cues and actions come to dominate choice and why, unlike natural rewards, drugs do not show blocking; it does not explain why only a minority of users become addicted, which depends on genetic factors, stress, age at first use and the transition from goal-directed to habitual control mediated by the dorsal striatum ([7.16.40](/7.16.40)).

### 37.5.2. Adaptation: Tolerance and Withdrawal

Repeated drug exposure triggers adaptations that oppose the drug's effects. At the cellular level, chronic opioids up-regulate the cAMP pathway in neurons of the locus coeruleus and nucleus accumbens, so that withdrawal leaves an overshoot of cAMP signaling; psychostimulants induce the stable transcription factor ΔFosB in striatal neurons, which accumulates over repeated exposure and changes gene expression for weeks; and synapses on accumbens neurons change their **AMPA receptor** composition during abstinence, a candidate mechanism for the "incubation" of cue-induced craving, which grows over weeks of abstinence. These adaptations reduce the response to the drug (tolerance) and produce a negative state when it is absent (withdrawal), so that use is driven increasingly by relief of the negative state, negative reinforcement, rather than by the positive effect.

**Definition 37.5.2 (Opponent Process)** An **opponent process** is a slow, opposing response that a stimulus with a strong affective effect elicits in addition to its primary effect; the primary (a-) process follows the stimulus closely, whereas the opponent (b-) process builds up and decays slowly and grows with repeated exposure (Solomon and Corbit, 1974).

![The opponent-process model of tolerance and withdrawal (Definition 37.5.2; 1-h exposure, shaded; a-process time constant $0.1\,\mathrm{h}$; b-process $\tau_b\,\dot b = -b + k\,a$ with $\tau_b = 1.5\,\mathrm{h}$; the gain grows with the exposure number $n$ as $k_n = 2.7(1 - 0.8^n)$). A: at the first exposure the net effect (black) is nearly the primary effect, with a small after-reaction. B: after ten exposures the opponent process cancels much of the effect during exposure (tolerance) and produces a large, long negative after-reaction (withdrawal).](./plots/opponent-process.py)

The model shows how the same neuroadaptation produces both tolerance and withdrawal and why the motivational balance shifts with repetition. It is a phenomenological description; at the circuit level, the b-process corresponds to recruitment of stress systems (corticotropin-releasing factor and dynorphin in the extended amygdala) and to the reduced dopamine function measured in people with addiction.

## 37.6. Valence

Approach and avoidance require that stimuli be assigned a sign, and the brain contains several systems that carry valence explicitly. In the basolateral amygdala, neurons that project to the nucleus accumbens are preferentially potentiated by reward conditioning and promote approach, whereas neurons projecting to the CeA are potentiated by fear conditioning and promote avoidance (Namburi and colleagues, 2015); genetically distinct populations in anterior and posterior BLA show a similar division. The lateral habenula, an epithalamic nucleus, is excited by punishments and by the omission of expected rewards and inhibits dopamine neurons through the GABAergic rostromedial tegmental nucleus (Matsumoto and Hikosaka, 2007): it is a source of the negative prediction errors seen as pauses of dopamine neurons, and its hyperactivity is implicated in depression. In the **hypothalamus**, AgRP and thirst neurons carry the negative valence of need ([7.16.34](/7.16.34#sec-34.3.3)).

Valence is not fixed by the stimulus. The same taste is attractive or aversive depending on internal state (alliesthesia, [7.16.34](/7.16.34#sec-34.5.3)) and on learning: a single pairing of a novel taste with nausea produces a strong, long-lasting aversion even with hours between taste and illness (conditioned taste aversion, Garcia), an exception to the usual requirement of close temporal contiguity that reflects a specialized circuit through the parabrachial nucleus and amygdala. Representations of valence therefore combine stimulus identity, internal state and learned predictions, the same three ingredients that **reinforcement learning** combines in a **value function**.

## Summary

- Emotion states (Definition 37.1.1) are central states with scalability, persistence, generalization and valence; they can be studied in any animal by these operational criteria.
- In fear conditioning (Definition 37.2.1), CS and US converge on lateral amygdala neurons, whose CS synapses are potentiated (LTD and LTP of these inputs remove and restore the memory); the central amygdala (Definition 37.2.2) produces freezing, autonomic and endocrine responses by disinhibition. Extinction is new, context-dependent learning involving the infralimbic cortex; acquisition and extinction follow the Rescorla–Wagner rule, spontaneous recovery does not.
- Mesolimbic dopamine supports self-stimulation, wanting (incentive salience) and vigor, while liking depends on opioid and other hotspots (Definition 37.3.1 for reward).
- Dopamine neurons signal a reward prediction error (Definition 37.4.1): a burst for unexpected reward, transfer to the predictive cue, a pause for omission; optogenetic bursts and pauses are sufficient to drive and reverse learning.
- Addictive drugs (Definition 37.5.1) all raise accumbens dopamine; a drug-evoked component that cannot be predicted away makes drug-associated values grow without bound (Formula 37.5.1). Opponent processes (Definition 37.5.2) account for tolerance and withdrawal and the shift to negative reinforcement.
- Valence is carried by projection-defined BLA neurons, the lateral habenula and hypothalamic need neurons, and depends on state and learning.

| Signal | Positive outcome | Negative outcome | Source |
|---|---|---|---|
| Dopamine (VTA) | Burst for better than expected | Pause for worse than expected | VTA, SNc |
| Lateral habenula | Inhibited | Excited by punishment and omitted reward | Epithalamus |
| BLA projections | BLA→NAc potentiated | BLA→CeA potentiated | Amygdala |
| Need neurons | Inhibited by predicted relief | AgRP, thirst neurons active and aversive | Hypothalamus |

## Questions

1. With the Rescorla–Wagner rule and $\alpha\beta = 0.3$, how many tone–shock pairings bring $V$ to 90% of its asymptote? If after acquisition the tone is compounded with a light and the compound is paired with the shock, what does the rule predict for the light, and what would the dopamine prediction error look like?

   **Answer** $V_n = 1 - 0.7^n$, which exceeds 0.9 when $0.7^n < 0.1$, i.e. $n \ge 7$. In the compound phase the prediction is $V_{\mathrm{tone}} + V_{\mathrm{light}} \approx 1$ already, so $\lambda - V_{\mathrm{total}} \approx 0$ and the light gains almost no strength: blocking. In the appetitive version of the same design (Waelti, Dickinson and Schultz, 2001), dopamine neurons show no burst at the fully predicted reward of the compound trials and acquire no response to the blocked cue: the absent prediction error is what fails to drive learning about it.

2. Why is extinction considered new learning rather than erasure of the original memory? Name three behavioral phenomena and one neural observation that support this.

   **Answer** Erasure predicts that the response, once extinguished, should behave like that of a naive animal. Instead it returns with time (spontaneous recovery), in a context different from that of extinction (renewal), and after an unsignaled US (reinstatement); relearning after extinction is also faster than original learning (savings). Neurally, extinction recall requires activity in the infralimbic cortex and inhibitory circuits that suppress CeA output, while the potentiated LA synapses and the neurons allocated to the original memory remain; inhibiting infralimbic cortex at test restores fear.

3. In Formula 37.5.1, consider a single state $S$ with a drug reward that ends the episode, so that the update is $\hat v \leftarrow \hat v + \alpha\delta$ with $\delta = \max(r - \hat v + d, d)$. Find the fixed point for a natural reward ($d = 0$) and show that there is none for $d > 0$.

   **Answer** For $d = 0$, $\delta = \max(r - \hat v, 0)$; if $\hat v < r$, $\hat v$ increases toward $r$ and stops there ($\delta = 0$), so the fixed point is $\hat v = r$. (The max makes the learned value never decrease, which is a simplification.) For $d > 0$, $\delta \ge d$ for every $\hat v$, so $\hat v$ increases by at least $\alpha d$ on every trial and grows linearly without bound; when the drug state competes with natural rewards in a choice, its value eventually exceeds all of them, which models the narrowing of behavior onto the drug. The model predicts no blocking for drug rewards, a prediction tested with mixed results.

4. (Open question) Dopamine neurons respond to rewards with prediction errors, yet their activity is also related to movement and to salient, non-rewarding events. Propose experiments that distinguish a pure reward prediction error from a salience signal.

   **Answer** A salience signal predicts responses of the same sign to unexpected events of either valence, whereas a prediction error predicts opposite signs for better-than-expected and worse-than-expected outcomes. Test: in the same identified neurons (optogenetic tagging), present unexpected rewards, unexpected punishments (air puffs) and omissions of expected rewards and punishments; compare responses to cues predicting reward or punishment with different probabilities. A prediction error neuron bursts to unexpected reward and to omission of expected punishment and pauses to punishment and reward omission; a salience neuron bursts to all surprising events. Experiments of this kind found both types, segregated by projection target: reward prediction error neurons project mainly to the ventral striatum, and salience- or threat-responsive neurons to the tail of the striatum and other targets. Causal tests then manipulate each population at the time of the outcome and ask whether it drives approach learning, avoidance learning or neither.
