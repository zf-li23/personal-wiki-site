---
title: Introduction and the Potential Outcomes Framework
description: Causation versus association, the three parts of a causal analysis and a brief history; units, actions and potential outcomes; unit-level causal effects and which "because" statements are well defined; the fundamental problem of causal inference; SUTVA and exclusion restrictions; finite-sample causal estimands and covariates; and Lord's paradox analyzed with potential outcomes.
---

Questions of cause and effect guide decisions. Is a new drug effective for a given group of patients? Did a driving restriction improve the air quality of a city? Does a flipped classroom raise the grades of students who would otherwise sit in a traditional lecture? Each question asks what would happen if we did one thing rather than another. Association answers a different question: it lets us predict one variable from another, but a prediction is not a guide to action, because changing a variable need not change the variables it predicts. Causal inference is the part of statistics that makes the step from data to statements about the consequences of actions precise.

This course presents two frameworks. The first, the potential outcomes framework of Neyman and Rubin, starts from a given cause, a treatment that can be applied to units, and asks for its effects; it occupies [3.9.1](/3.9.1)–[3.9.10](/3.9.10) and [3.9.14](/3.9.14). The second, the causal graphical models of Pearl, describes the causal structure among many variables at once and asks which effects can be computed from it; it is the subject of [3.9.11](/3.9.11)–[3.9.13](/3.9.13). This chapter introduces the vocabulary of the first framework: units, treatments, potential outcomes, causal effects and the assumptions that link them to data. Its ideas grew out of the design of experiments ([3.8](/3.8)), where **randomization** was first used as the basis of inference, and they explain when a regression coefficient ([3.3](/3.3)) has a causal meaning and when it does not.

## 1.1. Causality and Statistics

### 1.1.1. Causation and Association

The question of causes is as old as philosophy. Aristotle used the word "cause" for an explanation, an answer to a question beginning with "why"; Democritus is reported to have said that he would rather discover one causal law than be king of Persia. In modern terms, causality is the relation between a process (the cause) and another process or state (the effect) such that the first is partly responsible for the second and the second depends on the first. Two kinds of questions can be asked about it: what is the cause of a given effect, and what is the effect of a given cause. Statistical methods are far better at the second, and the potential outcomes framework is built for it.

Association and causation can come apart in both directions.

- Association without causation. The cock crows every morning just before sunrise, yet silencing the cock will not delay the dawn. Two accurate watches always show the same time, but neither drives the other: both are driven by a common cause, the passage of time.
- Causation without (visible) association. Workers in physically demanding jobs often turn out to be healthier than the general population, even when the job itself harms their health, because only people healthy enough to do the work are hired and remain employed (the healthy worker effect). The harmful effect of the job is masked by the selection of who is exposed. Similarly, a comparison of the lifetimes of people who practice taiji with those who do not mixes the effect of taiji with the reasons people take it up.

For a long time statistics textbooks avoided causal language outside randomized experiments; some warned their readers against it, and many mentioned causation only to stress that correlation is not causation. The reason is not that causal questions are unimportant but that answering them requires assumptions beyond the data. The purpose of a framework is to state those assumptions explicitly.

### 1.1.2. The Three Parts of a Causal Analysis

The same data can support very different causal conclusions depending on how they were collected. If patients who received a drug did better than those who did not, it matters whether a coin decided who got the drug or the patients' doctors did, choosing the drug for those they expected to benefit. A causal analysis therefore has three parts:

1. a causal model, which defines the causal effects of interest (in this framework, through potential outcomes);
2. assumptions about how the data were collected, in particular how the units came to receive their treatments (the assignment mechanism of [3.9.2](/3.9.2));
3. statistical inference from the collected data about the parameters of the causal model.

The second part has no counterpart in a purely predictive analysis, and it is where most of the difficulty lies.

### 1.1.3. A Brief History

Statistical frameworks for causality that apply to many kinds of data are only about a century old. The two most important early developments were the introduction of potential outcomes for randomized experiments by Jerzy Neyman (1923), in a paper on agricultural field trials, and the introduction of randomization as the "reasoned basis" for inference by R. A. Fisher (1935). Both were confined to randomized experiments. Donald Rubin (1974, 1975, 1978) put potential outcomes at the center of the analysis of causal effects in both randomized experiments and observational studies, explained the benefits of randomization in terms of eliminating systematic differences between treated and control units, and formulated the assignment mechanism in general mathematical terms; for this reason the framework is often called the Rubin causal model. James Robins extended it to treatments that vary over time, and Judea Pearl developed the graphical approach of [3.9.11](/3.9.11).

## 1.2. Potential Outcomes

### 1.2.1. Units and Actions

The basic idea of the framework is that causality is tied to an action applied to a unit.

**Definition 1.2.1 (Unit and Action)** A unit is the object to which an action can be applied: a physical object, a firm, an individual person, or a collection of objects or persons such as a classroom or a market, at a particular point in time. An action is a manipulation, treatment or intervention that can potentially be applied to a unit.

A unit is the counterpart of the **experimental unit** of [3.8.1](/3.8.1), and an action is the counterpart of a **treatment**. In the example of a headache, possible actions are to take an aspirin, not to take the aspirin, or to take another medicine. We mostly consider settings with two actions; extensions to multi-valued treatments are conceptually straightforward. The more active of the two (taking the aspirin) is called the active treatment, or simply the treatment, and the more passive one (not taking it) the control treatment, or control. The two labels are merely names: formally the two actions are treated symmetrically, and nothing in the theory depends on which one is called the treatment.

### 1.2.2. Potential Outcomes and Unit-Level Causal Effects

**Definition 1.2.2 (Potential Outcome)** For a given unit and a given set of actions, each action–unit pair is associated with a **potential outcome**: the value that an outcome variable of the unit would take if the action were applied to it. With two actions we write $Y_i(1)$ for the potential outcome of unit $i$ under the active treatment and $Y_i(0)$ for its potential outcome under control.

**Definition 1.2.3 (Unit-Level Causal Effect)** The **unit-level causal effect** of the active treatment relative to control for unit $i$ is a comparison of its two potential outcomes, usually the difference

$$
\tau_i = Y_i(1) - Y_i(0),
$$
or, for positive outcomes, the ratio $Y_i(1)/Y_i(0)$.

The potential outcomes are attributes of the unit that exist before any treatment is applied; the action only decides which of them we get to see. A causal effect is defined by the pair of potential outcomes of one and the same unit, not by a comparison of different units, and its definition does not depend on which action is actually taken. Any treatment must occur before the outcome is observed: an action taken today can only affect outcomes measured later. An outcome measured before the treatment is not an outcome but a covariate (Section 1.5.3).

In the headache example, with outcome "headache one hour later", there are four possibilities.

| Case | $Y(\text{aspirin})$ | $Y(\text{no aspirin})$ | Unit-level causal effect |
|---|---|---|---|
| 1 | no headache | headache | improvement due to aspirin |
| 2 | headache | headache | none (headache in both cases) |
| 3 | no headache | no headache | none (headache gone in both cases) |
| 4 | headache | no headache | deterioration due to aspirin |

Only the first case justifies the statement "my headache went away because I took an aspirin", and in cases 2 and 3 the aspirin made no difference even though the observed outcome differs between them.

### 1.2.3. Which Causal Statements Are Well Defined

The framework gives a test for informal causal statements of the form "$A$ because $B$": identify the unit, the treatment and the control, and check that both potential outcomes are well defined.

| Statement | Unit | Treatment | Control | Verdict |
|---|---|---|---|---|
| "My headache went away because I took an aspirin." | I (at that time) | taking an aspirin | not taking it, at the same moment | well defined: the effect is $Y(1) - Y(0)$ |
| "She got a good job last year because she went to college." | she | going to college | not going, but instead what? Enlisting in the military, joining an artists' colony, working at once… | ambiguous: each alternative gives a different $Y_i(0)$ and a different effect |
| "She has long hair because she is a girl." | she | being a girl | being a boy | ill defined: no action is articulated that would have made her a boy |

In the second statement the effect becomes well defined once the control action is specified; the statement is incomplete rather than wrong. In the third, different conceivable interventions (hormone treatment at some age, a surgical procedure, a different genetic make-up at conception) would lead to different potential outcomes, and none of them is implied by the statement. In this framework such a "because" statement is not a causal statement at all. The point is often summarized in the motto "no causation without manipulation" (Holland 1986): causal questions are about the effects of actions that could, at least in principle, be taken. Attributes of a unit such as sex or race can still enter an analysis as covariates, and their association with outcomes can be described, but their "effects" have to be translated into the effects of specific manipulations before the framework applies.

## 1.3. The Fundamental Problem of Causal Inference

### 1.3.1. At Most One Potential Outcome Is Observed

A film can show both worlds, the one in which the hero took the train and the one in which he missed it; reality cannot. For each unit, at most one of the two potential outcomes is realized and observed: the one corresponding to the action actually taken. The other is counterfactual and remains unobserved. Consequently the unit-level causal effect $Y_i(1) - Y_i(0)$ can never be computed from data on unit $i$ alone. Holland (1986) called this the *fundamental problem of causal inference*. Causal inference is therefore a missing data problem: at least half of all potential outcomes are missing, and every method in this course is, in one way or another, a method for predicting the missing ones.

### 1.3.2. Learning from Multiple Units

The only way out is to observe several units, some exposed to the treatment and some to the control, and to use the outcomes of some units to predict the missing outcomes of others. There are two basic options:

- observe the same physical object under different treatments at different points in time;
- observe different physical objects at approximately the same time.

It is important to recognize that both options involve different units. Different objects at the same time are obviously different units: your headache after an aspirin may differ from what mine would have been, because I may be more or less sensitive to aspirin or may have started with a more severe headache. But the same object at different times is also a different unit. My confidence that an aspirin relieves my headache rests on earlier episodes in which I took it and the headache went away, and episodes in which I did not and it stayed; yet I may have become more or less sensitive to aspirin, evenings may differ from mornings, and the initial intensity of the headache may differ. For inanimate objects it is often reasonable to assume that time makes little difference, which is why physical experiments can repeat measurements on the same apparatus; for human subjects this is much less reasonable. In either case "the same unit at another time behaves the same way" is an assumption, and it should never be confused with a definition.

### 1.3.3. Multiple Units Do Not Solve the Problem by Themselves

Having several units creates a new difficulty. Suppose you and I both have headaches and there are two equally effective aspirin tablets. The treatment is now a pair $\boldsymbol{t} = (t_1, t_2)$ with four possible values: both of us take an aspirin, only you do, only I do, or neither of us does. Each of us has four potential outcomes $Y_i(\boldsymbol{t})$, and for each of us there are $\binom{4}{2} = 6$ different comparisons that could be called a causal effect: the status of my headache if we both take aspirin versus if neither does, if only you take one versus if both do, and so on. With $N$ units and two treatments there are $2^N$ potential outcomes per unit. Without further assumptions, observing more units only multiplies the number of unknowns.

## 1.4. SUTVA and Other Assumptions

### 1.4.1. The Stable Unit Treatment Value Assumption

A typical assumption in the two-person example is that whether you take an aspirin does not affect my headache. It is important to understand the force of such an assumption and never to forget that it is an assumption, not a fact; it may be false. If we are in the same room and your incessant complaining keeps my headache going unless you take an aspirin, then your treatment affects my outcome.

**Definition 1.4.1 (Stable Unit Treatment Value Assumption)** The **stable unit treatment value assumption** (SUTVA) consists of two conditions.

1. No interference: the potential outcomes of any unit do not vary with the treatments assigned to other units, $Y_i(\boldsymbol{t}) = Y_i(t_i)$.
2. No hidden variations of treatments: for each unit there are no different forms or versions of each treatment level that lead to different potential outcomes, so that $Y_i(t_i) \in \{Y_i(0), Y_i(1)\}$ is well defined.

Under SUTVA each unit has exactly two potential outcomes, $Y_i(0)$ and $Y_i(1)$, whatever the number of units, and the unit-level causal effect $Y_i(1) - Y_i(0)$ is a single number. The first condition fails when units interact: vaccination protects the unvaccinated through herd immunity, students in a class learn from each other, and a job training program may help its participants at the expense of non-participants competing for the same jobs. A common remedy is to redefine the unit at a level where interference is negligible, for example to randomize whole classes rather than students ([3.9.7](/3.9.7)). The second condition fails when "the treatment" covers several things: if some aspirin tablets are fresh and others have expired, $Y_i(1)$ depends on which tablet unit $i$ would receive. The remedy is to define the treatment more finely, or to argue that the versions have the same effect.

### 1.4.2. Exclusion Restrictions

SUTVA is one example of a wider class of assumptions that use substantive knowledge to restrict the potential outcomes.

**Definition 1.4.2 (Exclusion Restriction)** An **exclusion restriction** is an assumption that relies on external, substantive information to rule out the existence of a causal effect of a particular treatment relative to an alternative.

For example, if patients are randomly encouraged to take a drug, one may assume that the encouragement itself has no effect on health except through the drug actually taken; this exclusion restriction is the basis of the instrumental variables methods of [3.9.14](/3.9.14). Exclusion restrictions are not part of SUTVA: SUTVA consists of the two conditions above, while an exclusion restriction is a separate assumption that sets certain causal effects equal to zero. Causal inference is generally impossible without assumptions of these kinds. What matters is to be explicit about their content and their justification.

### 1.4.3. SUTVA Is Not Enough

SUTVA simplifies the model but does not by itself make causal effects estimable. Suppose you and I both have headaches, I take an aspirin and you do not, and an hour later neither of us has a headache. Under SUTVA the observed data are $Y_{\mathrm{me}}(1) = \text{no headache}$ and $Y_{\mathrm{you}}(0) = \text{no headache}$. They are consistent with the following potential outcomes:

| Unit | $Y(\text{aspirin})$ | $Y(\text{no aspirin})$ | Causal effect |
|---|---|---|---|
| You | no headache | no headache (observed) | none |
| I | no headache (observed) | headache | improvement due to aspirin |

Here the aspirin helped me, although the observed outcomes are the same; perhaps my headache was more severe to begin with. The data are equally consistent with no effect for either of us. To learn anything we need assumptions about how the units came to receive their treatments and about how similar the units are, which are the subjects of the next sections and of [3.9.2](/3.9.2).

## 1.5. Causal Estimands

### 1.5.1. Population-Level Causal Estimands

From now on we assume SUTVA and consider a finite population of $N$ units, $i = 1, \dots, N$, each with potential outcomes $Y_i(0)$ and $Y_i(1)$. Since unit-level effects cannot be observed, we usually summarize them over the population or over subpopulations.

**Definition 1.5.1 (Finite-Sample Causal Estimands)** The finite-sample **average treatment effect** is

$$
\tau_{\mathrm{fs}} = \frac{1}{N}\sum_{i=1}^{N}\bigl(Y_i(1) - Y_i(0)\bigr) = \bar Y(1) - \bar Y(0).
$$
Averages over subpopulations are defined in the same way, for example over the $N(f)$ units with covariate value $X_i = f$ (say, the females), over the $N_{\mathrm{t}}$ units that actually received the treatment, or over the units whose potential outcomes are both positive:

$$
\tau_{\mathrm{fs}}(f) = \frac{1}{N(f)}\sum_{i:X_i = f}\bigl(Y_i(1) - Y_i(0)\bigr), \qquad
\tau_{\mathrm{fs,t}} = \frac{1}{N_{\mathrm{t}}}\sum_{i:W_i = 1}\bigl(Y_i(1) - Y_i(0)\bigr), \qquad
\tau_{\mathrm{fs,pos}} = \frac{1}{N_{\mathrm{pos}}}\sum_{i:Y_i(0)>0,\,Y_i(1)>0}\bigl(Y_i(1) - Y_i(0)\bigr).
$$
The estimand $\tau_{\mathrm{fs,t}}$ is the **average treatment effect on the treated** (ATT). The average treatment effect is also called the average causal effect (ACE).

More generally, a causal estimand is any function of the potential outcomes, the covariates and the treatments of all units,

$$
\tau = \tau\bigl(\boldsymbol{Y}(0), \boldsymbol{Y}(1), \boldsymbol{X}, \boldsymbol{W}\bigr),
$$
where $\boldsymbol{Y}(0)$ and $\boldsymbol{Y}(1)$ are the $N$-vectors of potential outcomes, $\boldsymbol{X}$ is the $N \times K$ array of covariates and $\boldsymbol{W}$ the $N$-vector of treatment indicators introduced below. Examples beyond averages are the median of the unit-level effects, the difference of medians $\operatorname{med}\{Y_i(1)\} - \operatorname{med}\{Y_i(0)\}$ (which is not the same thing), or the fraction of units for which the treatment is beneficial. The estimands $\tau_{\mathrm{fs,t}}$ and $\tau_{\mathrm{fs,pos}}$ show that the set of units over which we average may itself depend on $\boldsymbol{W}$ or on the potential outcomes. In [3.9.2](/3.9.2) we will regard the $N$ units as a sample from a larger super-population and define the corresponding super-population estimands.

### 1.5.2. Observed and Missing Outcomes

Let $W_i \in \{0, 1\}$ be the treatment indicator of unit $i$, equal to $1$ if the unit receives the active treatment and $0$ if it receives the control. The observed and the missing potential outcomes are

$$
Y_i^{\mathrm{obs}} = Y_i(W_i) = W_i Y_i(1) + (1 - W_i) Y_i(0), \qquad
Y_i^{\mathrm{mis}} = Y_i(1 - W_i) = (1 - W_i) Y_i(1) + W_i Y_i(0).
$$
The data consist of $\boldsymbol{W}$, $\boldsymbol{Y}^{\mathrm{obs}}$ and $\boldsymbol{X}$; the estimand depends in general also on $\boldsymbol{Y}^{\mathrm{mis}}$. We write $N_{\mathrm{t}} = \sum_i W_i$ and $N_{\mathrm{c}} = N - N_{\mathrm{t}}$ for the numbers of treated and control units, and $\bar Y_{\mathrm{t}}^{\mathrm{obs}}$, $\bar Y_{\mathrm{c}}^{\mathrm{obs}}$ for the averages of the observed outcomes in the two groups. Bold letters denote the arrays for all $N$ units.

A note on notation used throughout the course. The potential outcomes $Y_i(0)$, $Y_i(1)$ and the covariates $X_i$ of the $N$ units can be regarded either as fixed numbers or as draws from a super-population, and the treatments $\boldsymbol{W}$ are random. We indicate the source of the randomness by a subscript: $\mathbb{E}_W$ and $\operatorname{Var}_W$ average over the distribution of the assignment $\boldsymbol{W}$ only, with the potential outcomes held fixed, while $\mathbb{E}_{\mathrm{sp}}$ and $\operatorname{Var}_{\mathrm{sp}}$ also average over the sampling of the units from the super-population. The distinction between these two layers of randomness is central to [3.9.3](/3.9.3)–[3.9.7](/3.9.7).

**Example 1.5.1** Four patients can receive either a drug ($W_i = 0$) or surgery ($W_i = 1$); the outcome is the number of years of survival. Suppose that a doctor knew all potential outcomes and gave each patient the treatment that is better for that patient.

| Patient | $Y_i(0)$ | $Y_i(1)$ | $Y_i(1) - Y_i(0)$ | $W_i$ | $Y_i^{\mathrm{obs}}$ |
|---|---|---|---|---|---|
| 1 | 1 | 7 | 6 | 1 | 7 |
| 2 | 6 | 5 | $-1$ | 0 | 6 |
| 3 | 1 | 5 | 4 | 1 | 5 |
| 4 | 8 | 7 | $-1$ | 0 | 8 |
| Average | 4 | 6 | 2 | | |

The average treatment effect is $\tau_{\mathrm{fs}} = 2$: on average surgery adds two years. But the observed data show the surgery patients living $(7 + 5)/2 = 6$ years and the drug patients $(6 + 8)/2 = 7$ years, so the naive comparison $\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}} = -1$ suggests that surgery is harmful. The ideal medical practice makes the observed comparison misleading precisely because the assignment depends on the potential outcomes. Ignoring how the treatments were assigned can lead to wrong conclusions; [3.9.2](/3.9.2) makes the assignment a mathematical object.

:::

### 1.5.3. Covariates

With many units and SUTVA, at least half of all potential outcomes are missing, and to estimate a causal effect we must predict or impute them. Background attributes of the units help with these predictions.

**Definition 1.5.2 (Covariate)** A covariate, or pre-treatment variable, of unit $i$ is a characteristic $X_i$ of the unit that is known a priori to be unaffected by the treatment, typically because it is measured before the treatment is assigned.

The defining property of a covariate is that it does not depend on the treatment, so that it has the same value under both actions. Age, sex, a pre-test score and the severity of the disease at baseline are covariates; a variable measured after the treatment, such as whether the patient actually took the pills, is not, even if it is recorded at the same time as other baseline information. Covariates serve three purposes:

- defining subgroups and the corresponding estimands, such as $\tau_{\mathrm{fs}}(f)$;
- estimating causal effects more precisely, because they help to predict the potential outcomes ([3.9.5](/3.9.5));
- describing the assignment mechanism, which may depend on them, as when doctors choose a treatment based on the severity of the illness ([3.9.2](/3.9.2), [3.9.8](/3.9.8)).

## 1.6. Example: Lord's Paradox

### 1.6.1. The Problem

**Example 1.6.1** A large university is interested in the effects on its students of the diet provided in the university dining halls, and in any sex differences in these effects. The weight of each student is recorded at the time of arrival in September and again the following June (Lord 1967). For the males, the whole distribution of weights is the same in June as in September; the same is true for the females. The only difference between the sexes is that the females started and ended the year lighter on average than the males. On average, neither males nor females gained or lost weight.

Two statisticians analyze these data.

- Statistician 1 observes that for neither sex is there any difference between the September and June weight distributions, and concludes that there is no evidence of any effect of the diet, or of anything else, on weight, and in particular no evidence of a differential effect on the two sexes.
- Statistician 2 fits a regression of June weight on September weight and sex with a common slope (a "parallel regression adjustment", that is, an analysis of covariance). Because the within-sex regression slope is less than one, the two fitted lines are parallel but separated: at any given September weight, males weigh more in June than females. Statistician 2 concludes that after controlling for initial weight, the diet has a larger positive effect on males than on females.

Both analyses are arithmetically correct, yet the conclusions contradict each other. This is *Lord's paradox*.

![Simulated September and June weights of males and females: each sex lies along the 45-degree line on average with no change in mean weight, while parallel within-sex regression lines with slope below one are separated by about 4.5 kg](./plots/lords_paradox.py)

:::

The figure shows simulated data with the features described by Lord: the means of both sexes lie on the $45^\circ$ line, so the distribution of weights does not change, but within each sex the regression of June on September weight has slope about $0.7$, which is the familiar regression toward the mean of two imperfectly correlated measurements. The vertical distance between the two parallel lines is what Statistician 2 reports as a differential effect.

### 1.6.2. Analysis with Potential Outcomes

If the two statisticians confined themselves to describing the data, both would be right: the distributions do not change, and at a given September weight males do weigh more in June. As causal statements both are unsupported, because these data cannot support any conclusion about the causal effect of the diet without very strong, and arguably implausible, assumptions. Writing down the elements of the framework shows why.

| Element | In Lord's example |
|---|---|
| Units | the students |
| Treatment | the university diet from September to June |
| Control | not defined at all (another diet? no university at all?) |
| Potential outcomes | $Y_i(1)$ = June weight under the university diet, observed for everyone; $Y_i(0)$ = June weight under the undefined control, never observed |
| Covariates | sex, September weight |
| Assignment | every student received the treatment; nobody received the control |

The causal effect for a student is $Y_i(1) - Y_i(0)$, and its average difference between the sexes involves $\mathbb{E}[Y(0) \mid \text{male}] - \mathbb{E}[Y(0) \mid \text{female}]$, a quantity about which the data contain no information at all, since no student was ever exposed to the control. Each statistician has implicitly filled in the missing $Y_i(0)$ in a different way: Statistician 1 by assuming that without the diet the June weight would equal the September weight, Statistician 2 by assuming that it would follow a common linear function of September weight for both sexes. Each conclusion is correct under its own assumption, and neither assumption can be checked against the data. Lord's paradox illustrates the value of stating the potential outcomes and the assignment explicitly: once they are written down the paradox disappears, and what remains is a disagreement about untestable assumptions. The two assumptions are worked out in [3.9.2](/3.9.2).

## Summary

- Framework: Causality is tied to an action applied to a unit. With two actions each unit has two potential outcomes, $Y_i(0)$ and $Y_i(1)$, and the unit-level causal effect is their comparison, $Y_i(1) - Y_i(0)$ (Definitions 1.2.2 and 1.2.3). A "because" statement is a causal statement only if the treatment and the alternative action are well defined (Section 1.2.3).
- Fundamental problem: At most one potential outcome per unit is observed: $Y_i^{\mathrm{obs}} = W_iY_i(1) + (1 - W_i)Y_i(0)$. Causal inference is a missing data problem, and it requires several units, which are different units even when they are the same object at different times.
- Assumptions: SUTVA (Definition 1.4.1: no interference, no hidden versions of treatments) reduces the potential outcomes to two per unit; exclusion restrictions (Definition 1.4.2) rule out specific effects by substantive knowledge. Neither makes effects estimable by itself; that requires assumptions about the assignment.
- Estimands: The finite-sample average treatment effect $\tau_{\mathrm{fs}} = \bar Y(1) - \bar Y(0)$, its subpopulation versions such as the ATT, and in general any function $\tau(\boldsymbol{Y}(0), \boldsymbol{Y}(1), \boldsymbol{X}, \boldsymbol{W})$ (Definition 1.5.1). Covariates are known not to be affected by the treatment; they define subgroups, improve precision and enter the assignment mechanism.
- Lord's paradox: With no unit under control, conclusions about the effect of the diet depend entirely on untestable assumptions about $Y_i(0)$ (Example 1.6.1).

| Symbol | Meaning |
|---|---|
| $W_i \in \{0, 1\}$ | treatment indicator (1 = active treatment) |
| $Y_i(0), Y_i(1)$ | potential outcomes under control and treatment |
| $Y_i^{\mathrm{obs}}, Y_i^{\mathrm{mis}}$ | observed and missing potential outcomes |
| $X_i$ | covariates (a $1 \times K$ row) |
| $N_{\mathrm{t}}, N_{\mathrm{c}}$ | numbers of treated and control units |
| $\tau_{\mathrm{fs}}, \tau_{\mathrm{fs,t}}$ | finite-sample average treatment effect, ATT |
| $\mathbb{E}_W, \operatorname{Var}_W$ | moments over the random assignment only |
| $\mathbb{E}_{\mathrm{sp}}, \operatorname{Var}_{\mathrm{sp}}$ | moments over sampling from the super-population and assignment |

## Questions

1. For each statement, identify the unit, the treatment, the control and the potential outcomes, and decide whether the statement is a well-defined causal statement. (a) "The city's air improved because of the odd–even driving restriction." (b) "He earns more because he is tall." (c) "The patient recovered because she received the vaccine."

   **Answer** (a) Unit: the city during a given period; treatment: the restriction; control: no restriction during the same period; outcome: an air quality index. Well defined, although only one unit is observed, so the effect can only be estimated with strong assumptions (for example by comparison with other cities or other periods, which are different units). (b) Unit: the man; treatment: being tall; control: being short. No action is specified that would change his height (growth hormone in childhood would have other effects as well), so as stated this is not a causal statement; it describes an association. (c) Unit: the patient; treatment: receiving the vaccine at a given time; control: not receiving it; outcome: recovery. Well defined, provided the alternative (no vaccine, or a placebo) is specified.
2. In the two-person aspirin example without SUTVA, list the four treatment vectors and the six comparisons that define a causal effect for one person. Which of these comparisons remain distinct under the no-interference condition?

   **Answer** The vectors are $(1,1)$, $(1,0)$, $(0,1)$, $(0,0)$, where the first entry is my treatment. My potential outcomes are $Y_{\mathrm{me}}(1,1)$, $Y_{\mathrm{me}}(1,0)$, $Y_{\mathrm{me}}(0,1)$, $Y_{\mathrm{me}}(0,0)$, and any two of them give a comparison, $\binom{4}{2} = 6$ in all. Under no interference $Y_{\mathrm{me}}(t_1, t_2) = Y_{\mathrm{me}}(t_1)$, so $Y_{\mathrm{me}}(1,1) = Y_{\mathrm{me}}(1,0)$ and $Y_{\mathrm{me}}(0,1) = Y_{\mathrm{me}}(0,0)$; four of the six comparisons become $Y_{\mathrm{me}}(1) - Y_{\mathrm{me}}(0)$ and the remaining two are identically zero.
3. Give an example from education or public health in which the no-interference part of SUTVA is violated, and describe how the definition of the unit could be changed to make it more plausible.

   **Answer** Vaccinating some children in a school lowers the infection risk of their unvaccinated classmates, so a child's outcome depends on the vaccination status of others. Taking the school (or a community) as the unit and comparing schools in which a vaccination program is or is not introduced makes no interference between units more plausible, at the cost of fewer units and a different estimand (the effect of a program at the school level, which includes the indirect effects).
4. A trial compares "physical therapy" with no therapy, but the therapy is delivered by therapists of very different skill. Which part of SUTVA is in question, and what are two ways to deal with it?

   **Answer** The condition of no hidden variations of treatments: "therapy by therapist A" and "therapy by therapist B" may be different treatments with different potential outcomes. One can define the treatment more finely (therapy by a specific therapist, a multi-valued treatment), or redefine the treatment as "being assigned to the therapy program", whose potential outcome averages over the therapists a patient would get; the effect is then the effect of the program as delivered.
5. Using Example 1.5.1, compute $\tau_{\mathrm{fs,t}}$ and the average effect on the control units under the ideal assignment, and compare them with $\tau_{\mathrm{fs}}$ and with the naive difference $\bar Y_{\mathrm{t}}^{\mathrm{obs}} - \bar Y_{\mathrm{c}}^{\mathrm{obs}}$.

   **Answer** The treated units are patients 1 and 3, so $\tau_{\mathrm{fs,t}} = (6 + 4)/2 = 5$; the control units are patients 2 and 4, with average effect $(-1 - 1)/2 = -1$. The overall effect is $\tau_{\mathrm{fs}} = 2$, the average of $5$ and $-1$. The naive difference $-1$ coincides with none of them: it equals $\bar Y_{\mathrm{t}}(1) - \bar Y_{\mathrm{c}}(0) = 6 - 7$, a comparison of different units.
6. Explain why the difference of the medians of $Y_i(1)$ and $Y_i(0)$ is in general different from the median of the unit-level effects. Give a three-unit example.

   **Answer** The median is not linear, so the median of differences need not equal the difference of medians. Take $(Y_i(0), Y_i(1)) = (1, 3), (2, 1), (3, 2)$. The medians of $Y(1)$ and $Y(0)$ are both $2$, so their difference is $0$, while the unit-level effects are $2, -1, -1$ with median $-1$. (For means the two coincide, which is one reason the average effect is the default estimand.)
7. In Lord's paradox, suppose that a second university with an otherwise similar student body served a different diet, and the same measurements were made there. Which estimand could then be estimated, and what assumption would be needed?

   **Answer** With the second university as the control, $Y_i(0)$ is the June weight under its diet, and the effect of the first diet relative to the second for males and for females could be estimated by comparing the two universities, possibly adjusting for September weight. The key assumption is that the students of the two universities are comparable, that is, that attending one or the other is unrelated to the potential outcomes given sex and September weight (the unconfoundedness of [3.9.2](/3.9.2)); in addition there is only one "unit" of each kind at the level of universities, so differences between the universities other than the diet are confounded with the diet.
