---
title: Game Theory and Competition for Resources
description: "Evolutionary game theory as a tool for behavior: frequency dependence, Nash equilibria and evolutionarily stable strategies, replicator dynamics and their stability, mixed strategies and polymorphisms; asymmetric contests, the bourgeois strategy and the war of attrition; competition by exploitation and the ideal free distribution (sticklebacks, ducks, dung flies, unequal competitors), resource defense and the despotic distribution; producer–scrounger games; alternative strategies; and animal personalities and behavioral syndromes."
---

When a bird decides where to feed, the best choice depends on where the other birds are feeding; when a male decides whether to fight for a female, the best choice depends on how his rivals fight. Most of the decisions treated in the preceding chapters on foraging ([7.18.22](/7.18.22), [7.18.23](/7.18.23)) could be analyzed with an **optimality model** ([7.18.2](/7.18.2#def-2.4.1)): the payoff of each option was fixed by the environment, and we asked which option maximizes it. As soon as individuals compete for the same resources, the payoff of an option depends on how many others choose it, and the question "what is the best behavior?" has no answer independent of the population. Its place is taken by the question "which behavior, once common, cannot be bettered by an alternative?", the question of evolutionary game theory.

The concepts were introduced in [7.10.16](/7.10.16#sec-16.2.3), where the **evolutionarily stable strategy** and the **hawk–dove game** were defined. This chapter develops the tools a behavioral ecologist needs in addition: the relation between Nash equilibria, ESSs and the stability of the replicator dynamics, which uses the stability theory of ordinary differential equations ([2.4.11](/2.4.11)); asymmetric contests and the war of attrition; and three applications that recur in the rest of the course: how competitors distribute themselves between resources (the ideal free distribution), how a population comes to contain producers and scroungers, and why individuals of the same population differ consistently in behavior (animal personality). Contests over territories are continued in the next chapter ([7.18.26](/7.18.26)), alternative mating strategies in [7.18.28](/7.18.28), and the evolution of signals in conflict in [7.18.39](/7.18.39). Throughout, we deal with the decisions of individuals; the population and community consequences of competition (competition coefficients, coexistence, niche theory) belong to ecology (7.19).

## 25.1. Frequency Dependence and Evolutionary Games

### 25.1.1. When Optimality Is Not Enough

A familiar human example shows the logic. A crowd sits on the floor to watch a concert; someone stands up to see better; the people behind must now stand to see at all, and a wave of standing spreads until everyone stands and nobody sees better than before. Sitting is not stable, because in a crowd of sitters a stander does better; standing is stable, because in a crowd of standers nobody gains by sitting down. The stable outcome is not the best one for the crowd: if everyone had agreed to sit, all would have been more comfortable. The same two features, a payoff that depends on what others do and a stable outcome that need not maximize the welfare of the group, characterize most competitive behavior.

Selection in such situations is **frequency-dependent selection**: the fitness of a behavior is a function of its frequency in the population. Under **negative frequency-dependent selection** a behavior does best when rare, and the population tends to a stable mixture of behaviors; under positive frequency dependence the common behavior does best and the population tends to fix whichever behavior gets ahead. Evolutionary game theory, developed by John Maynard Smith and George Price (1973) to explain why animal fights are so often "limited wars", is the mathematics of frequency-dependent selection on behavior.

In this theory a *strategy* is an inherited rule that specifies what an individual does in each situation it may meet (fight or display, stay or leave, produce or scrounge). The word implies no deliberation: a strategy is a phenotype, and the theory assumes that the strategy with the higher payoff increases in frequency, by genetic inheritance, by learning or by cultural transmission. Most models also ignore the details of genetics (diploidy, dominance, recombination) and assume that offspring resemble their parents in strategy, an assumption known as the *phenotypic gambit*. Its justification is that genetic details usually affect how fast and how closely a population approaches an equilibrium but rarely which equilibria are possible; the exceptions, such as an ESS that can be produced only by a heterozygote, are discussed in [7.10.16](/7.10.16#sec-16.2.3).

### 25.1.2. Payoffs, Nash Equilibria and ESSs

Consider a population in which individuals meet at random in pairs and play one of $n$ pure strategies $1, \dots, n$. Let $a_{ij}$ be the payoff, measured as a change in fitness, to an individual playing $i$ against one playing $j$, and collect these in the payoff matrix $A = (a_{ij})$. A *mixed strategy* plays pure strategy $i$ with probability $p_i$; it is a vector $\boldsymbol{p}$ in the simplex $\Delta_n = \{\boldsymbol{p} \in \mathbb{R}^n\colon p_i \geq 0,\ \sum_i p_i = 1\}$, and its payoff against a mixed strategy $\boldsymbol{q}$ is $E(\boldsymbol{p}, \boldsymbol{q}) = \boldsymbol{p}^{\mathsf T}A\boldsymbol{q}$.

**Definition 25.1.1 (Nash Equilibrium)** A strategy $\boldsymbol{p}^*$ of a symmetric two-player game is a (symmetric) **Nash equilibrium** if it is a best reply to itself,

$$
E(\boldsymbol{p}^*, \boldsymbol{p}^*) \geq E(\boldsymbol{q}, \boldsymbol{p}^*) \quad \text{for every strategy } \boldsymbol{q},
$$
and a *strict* Nash equilibrium if the inequality is strict for every $\boldsymbol{q} \neq \boldsymbol{p}^*$.

The concept comes from economics (John Nash, 1950), where the players are rational and each chooses the best reply to the others. In a population, a Nash equilibrium is a state in which no individual can gain by unilaterally changing strategy. The ESS of Maynard Smith and Price ([Definition 16.2.2](/7.10.16#def-16.2.2)) adds a condition for the case of equality: a strategy $I$ is an ESS if for every $J \neq I$ either $E(I, I) > E(J, I)$, or $E(I, I) = E(J, I)$ and $E(I, J) > E(J, J)$.

**Proposition 25.1.1** Every strict Nash equilibrium is an ESS, and every ESS is a Nash equilibrium. Equivalently, $\boldsymbol{p}^*$ is an ESS if and only if for every $\boldsymbol{q} \neq \boldsymbol{p}^*$ there is an $\bar\varepsilon > 0$ such that for all $0 < \varepsilon < \bar\varepsilon$

$$
E\bigl(\boldsymbol{p}^*, (1 - \varepsilon)\boldsymbol{p}^* + \varepsilon\boldsymbol{q}\bigr) > E\bigl(\boldsymbol{q}, (1 - \varepsilon)\boldsymbol{p}^* + \varepsilon\boldsymbol{q}\bigr).
$$

**Proof** The first two statements follow from the definitions: a strict Nash equilibrium satisfies the first ESS condition for every $J$, and either ESS condition implies $E(I, I) \geq E(J, I)$. For the equivalence, write the difference of the two sides as $(1 - \varepsilon)[E(\boldsymbol{p}^*, \boldsymbol{p}^*) - E(\boldsymbol{q}, \boldsymbol{p}^*)] + \varepsilon[E(\boldsymbol{p}^*, \boldsymbol{q}) - E(\boldsymbol{q}, \boldsymbol{q})]$, which is linear in $\varepsilon$. It is positive for all small $\varepsilon > 0$ exactly when the first bracket is positive, or the first bracket is zero and the second positive, which are the two ESS conditions. $\square$

The second form states the biological meaning: when a small fraction $\varepsilon$ of mutants playing $\boldsymbol{q}$ enters a population playing $\boldsymbol{p}^*$, the residents do better than the mutants in the resulting mixed population, so the mutants cannot spread. A Nash equilibrium that is not an ESS can be invaded by a mutant that does as well against the residents and better against itself; such a mutant spreads by drift and is then favored.

### 25.1.3. Replicator Dynamics

The ESS is a static concept: it tells us which populations resist invasion, not whether and how a population gets there. The simplest dynamic model follows the frequencies of pure strategies in a population in which each individual plays one pure strategy and its rate of increase is proportional to its payoff.

**Definition 25.1.2 (Replicator Dynamics)** Let $x_i$ be the frequency of pure strategy $i$ in a large, randomly mixing population, $\boldsymbol{x} = (x_1, \dots, x_n) \in \Delta_n$. The **replicator dynamics** of the game with payoff matrix $A$ is the system

$$
\dot{x}_i = x_i\left[(A\boldsymbol{x})_i - \boldsymbol{x}^{\mathsf T}A\boldsymbol{x}\right], \qquad i = 1, \dots, n, \tag{25.1}
$$
where $(A\boldsymbol{x})_i$ is the mean payoff of strategy $i$ and $\boldsymbol{x}^{\mathsf T}A\boldsymbol{x}$ the mean payoff in the population.

A strategy increases in frequency when it does better than the average and decreases when it does worse. Eq. (25.1) was introduced by Peter Taylor and Leo Jonker (1978) as the continuous-time limit of selection with frequency-dependent fitness, in which fitness is a baseline plus the payoff. The simplex $\Delta_n$ and each of its faces are invariant (a strategy absent at the start stays absent), and the rest points are the states in which all strategies present earn the same payoff. For two strategies with $x_1 = p$ the system reduces to one equation, $\dot p = p(1 - p)[W_1(p) - W_2(p)]$, the form used for the hawk–dove game in [Theorem 16.2.2](/7.10.16#thm-16.2.2).

**Example 25.1.1 (Stability in the Hawk–Dove Game)** With $V < C$, the right-hand side is $f(p) = p(1 - p)(V - Cp)/2$, with **equilibrium points** $p = 0$, $p = 1$ and $p^* = V/C$. By the linearization criterion for a one-dimensional autonomous system ([2.4.11](/2.4.11#sec-11.3)), an equilibrium is asymptotically stable if $f'(p) < 0$ and unstable if $f'(p) > 0$. Here $f'(0) = V/2 > 0$ and $f'(1) = (C - V)/2 > 0$, so both pure states are unstable, and $f'(p^*) = -\tfrac{C}{2}p^*(1 - p^*) < 0$, so the mixed state is asymptotically stable; since $f$ has no other zeros in $(0, 1)$, every population containing both hawks and doves converges to it. The eigenvalue $-\tfrac{C}{2}p^*(1 - p^*)$ also gives the speed of return after a perturbation: a population returns faster when fights are costly.

:::

The ESS and the stable rest points of Eq. (25.1) are closely related but not identical.

**Theorem 25.1.1 (ESS and Replicator Dynamics)** For a matrix game with payoff matrix $A$:

1. every Nash equilibrium is a rest point of the replicator dynamics, and every Lyapunov stable rest point is a Nash equilibrium;
2. every ESS $\boldsymbol{p}^*$ is an asymptotically stable rest point of the replicator dynamics; if $\boldsymbol{p}^*$ lies in the interior of $\Delta_n$, every trajectory starting in the interior converges to it.

The converse of 2 is false: there are asymptotically stable rest points that are not ESSs (Zeeman 1980).

**Proof** We prove part 2 for an interior ESS $\boldsymbol{p}^*$ with a Lyapunov function ([2.4.11](/2.4.11#sec-11.4)); the boundary case and part 1 are in Hofbauer and Sigmund (1998). Let $L(\boldsymbol{x}) = \sum_i p^*_i \ln x_i$ on the interior of $\Delta_n$. By Jensen's inequality, $L(\boldsymbol{x}) - L(\boldsymbol{p}^*) = \sum_i p^*_i \ln(x_i/p^*_i) \leq \ln \sum_i x_i = 0$, with equality only at $\boldsymbol{x} = \boldsymbol{p}^*$, so $L$ has a strict maximum at $\boldsymbol{p}^*$. Along solutions of Eq. (25.1),

$$
\dot L = \sum_i p^*_i \frac{\dot x_i}{x_i} = \boldsymbol{p}^{*\mathsf T}A\boldsymbol{x} - \boldsymbol{x}^{\mathsf T}A\boldsymbol{x} = E(\boldsymbol{p}^*, \boldsymbol{x}) - E(\boldsymbol{x}, \boldsymbol{x}).
$$
For an interior ESS, all pure strategies earn the same payoff against $\boldsymbol{p}^*$ (Theorem 25.1.2 below), so $E(\boldsymbol{x}, \boldsymbol{p}^*) = E(\boldsymbol{p}^*, \boldsymbol{p}^*)$ for every $\boldsymbol{x}$, and the second ESS condition gives $E(\boldsymbol{p}^*, \boldsymbol{x}) > E(\boldsymbol{x}, \boldsymbol{x})$ for every $\boldsymbol{x} \neq \boldsymbol{p}^*$. Hence $\dot L > 0$ away from $\boldsymbol{p}^*$: $-L$ is a strict Lyapunov function, and every interior trajectory converges to $\boldsymbol{p}^*$. $\square$

The proof uses the population state $\boldsymbol{x}$ as if it were a mixed strategy. The replicator dynamics thus does not distinguish between a population of pure strategists in the proportions $\boldsymbol{p}^*$ and a population of individuals each playing the mixed strategy $\boldsymbol{p}^*$; the distinction matters in the next section.

### 25.1.4. Mixed Strategies and Polymorphisms

The mixed ESS of the hawk–dove game can be realized in two ways: as a polymorphism, with a fraction $V/C$ of individuals always playing Hawk and the rest always playing Dove, or as a mixed strategy, with every individual playing Hawk in a random fraction $V/C$ of its contests. In both cases the average payoff per contest, $(1 - V/C)V/2$, is lower than the $V/2$ that a population of doves would obtain: the ESS is stable because it is "immune to treachery from within", not because it is good for the population. A general property of mixed ESSs explains why a population of pure strategists can mimic a mixed strategy.

**Theorem 25.1.2 (Bishop–Cannings)** Let $\boldsymbol{p}^*$ be a mixed ESS, and let $S$ be its support, the set of pure strategies played with positive probability. Then every pure strategy in $S$ earns the same payoff against $\boldsymbol{p}^*$, equal to $E(\boldsymbol{p}^*, \boldsymbol{p}^*)$.

**Proof** $E(\boldsymbol{p}^*, \boldsymbol{p}^*) = \sum_{i \in S} p^*_i E(i, \boldsymbol{p}^*)$ is a weighted average of the payoffs of the pure strategies in the support. If one of them earned more than the average, it would earn more than $\boldsymbol{p}^*$ against $\boldsymbol{p}^*$, contradicting the Nash property. So none earns more, and since the average equals $E(\boldsymbol{p}^*, \boldsymbol{p}^*)$, none earns less. $\square$

The theorem (Bishop and Cannings 1978) gives a practical test: in a population at a mixed equilibrium, the alternatives should have equal average success. It also explains why mixed ESSs are only weakly protected: a mutant that plays the pure strategies of the support in any proportion does exactly as well as the residents against the residents, and it is kept out only by the second ESS condition. With two strategies, the polymorphism and the mixed strategy have the same dynamics. With more strategies, or when the polymorphism is genetic and the ESS proportions cannot be produced by the genotypes available, the two realizations can behave differently; in particular, a genetic polymorphism may be unable to reach the ESS proportions at all.

When the payoff of each option varies with the state of the individual (its size, hunger or experience), the stable outcome is usually neither a polymorphism nor a randomizing mixed strategy but a **conditional strategy** ([7.18.5](/7.18.5#def-5.6.1)): "fight if larger than the opponent, otherwise retreat". Section 25.4.3 returns to this distinction.

### 25.1.5. When the Prize Is Worth More Than the Risk

If $V \geq C$, Hawk is the ESS ([Theorem 16.2.2](/7.10.16#thm-16.2.2)), and contests should escalate. The value $V$ must be understood as the increase in lifetime reproductive success that winning brings, and $C$ as the loss of future reproduction that an injury causes. For most animals, an item of food or a shelter is worth little compared with the risk of serious injury, so $V < C$ and contests are limited. But when the future holds little, as for a short-lived animal with a single chance to mate, the cost of injury is small relative to the prize, and models predict escalation to the death (Enquist and Leimar 1990). Fatal fighting is indeed found in such animals: wingless males of many fig wasps, which live their whole adult life inside a fig and fight with powerful mandibles for access to the few females emerging there (Hamilton 1979), and males of the bowl and doily spider *Frontinella pyramitela*, which fight to the death over females late in the season, when the chance of finding another female is low (Austad 1983).

## 25.2. Asymmetric Contests

### 25.2.1. The Bourgeois Strategy

Real contests are almost never symmetric. One contestant usually owns the contested resource, one is larger, one is hungrier. An asymmetry that both contestants perceive can be used to settle contests without fighting, even if it has no effect on the payoffs.

**Definition 25.2.1 (Bourgeois Strategy)** In a contest between an owner and an intruder, the **bourgeois strategy** plays Hawk when it is the owner and Dove when it is the intruder.

**Example 25.2.1 (The Hawk–Dove–Bourgeois Game)** Add Bourgeois (B) to the hawk–dove game and suppose that each contestant is owner or intruder with probability $\tfrac12$, independently of its strategy, and that ownership does not change $V$ or $C$. Averaging over the two roles gives the payoffs to the row player

| | against H | against D | against B |
|---|---|---|---|
| H | $(V - C)/2$ | $V$ | $(3V - C)/4$ |
| D | $0$ | $V/2$ | $V/4$ |
| B | $(V - C)/4$ | $3V/4$ | $V/2$ |

For example, a hawk meeting a bourgeois player faces a hawk (payoff $(V - C)/2$) when B is owner and a dove (payoff $V$) when B is intruder. Two bourgeois players never fight: the owner wins, so each gets $V$ or $0$ with equal probability. Then $E(B, B) = V/2$, $E(H, B) = (3V - C)/4$ and $E(D, B) = V/4$, so for $V < C$ Bourgeois is a strict Nash equilibrium and hence an ESS (Proposition 25.1.1). The replicator dynamics carries every population containing bourgeois players to pure Bourgeois. The hawk–dove mixture $p^* = V/C$ remains a rest point, but there Bourgeois earns exactly the average payoff (it plays Hawk half the time and Dove half the time, and both earn the same at $p^*$), and populations near it drift toward Bourgeois.

![The hawk–dove–bourgeois game with V = 2 and C = 3. A: payoffs to the focal (row) player, averaged over the owner and intruder roles; the highlighted cell, E(B, B) = V/2, exceeds the payoffs of Hawk and Dove against Bourgeois, so Bourgeois is a strict ESS. B: replicator dynamics on the strategy simplex (corners: pure Hawk, Dove and Bourgeois populations). On the hawk–dove edge (red) the population converges to the mixed equilibrium p* = V/C (open circle); populations containing bourgeois players are carried to the Bourgeois corner, those starting near the edge first approaching the hawk–dove mixture and then drifting away from it](./plots/hawk-dove-bourgeois.py)

:::

The result is surprising: an asymmetry that is "payoff-irrelevant" (it changes neither the value of the resource nor fighting ability) can settle contests, simply because it is a cue both contestants can use to coordinate who retreats. The same argument shows that the paradoxical rule "play Hawk as intruder, Dove as owner" is also an ESS when it is common, although it would cause continual changes of ownership; the bourgeois convention is more likely to evolve because owners usually do have more to lose, so that even a slight payoff asymmetry favors respecting ownership (Maynard Smith and Parker 1976; Grafen 1987). Grafen also pointed out that respect for ownership can collapse when ownership is everything: if nonowners have no prospect of breeding, they should fight as "desperadoes".

Owners do win most contests in nature. The classic case was the speckled wood butterfly *Pararge aegeria*, in which males defend patches of sunlight on the forest floor where they meet females. Nick Davies (1978) found that resident males always won, after a brief spiral flight, against intruders; when he removed a resident and let a new male take the sunspot, the new resident in turn always defeated the original owner on its release. This looked like the bourgeois convention. The experiment was repeated by Darrell Kemp and Christer Wiklund (2003), who kept the removed males cool and calm instead of holding them in a net; on release, the original residents won 50 of 52 contests against the replacements, after spiral flights that lasted much longer than those Davies had seen. The original result had probably been caused by the stress of capture, and the speckled wood does not follow an arbitrary rule. In most species studied since, owners win because ownership is correlated with fighting ability or with the value of the resource to the owner, the subject of the next chapter ([7.18.26](/7.18.26)).

### 25.2.2. Correlated Asymmetries

When contestants differ in fighting ability or in the value they place on the resource, the asymmetry is payoff-relevant, and the ESS uses it: the contestant more likely to win, or with more to gain, should escalate, and the other should retreat (Hammerstein 1981). A difference in fighting ability, often called resource-holding potential (defined in [7.18.26](/7.18.26)), can be assessed through displays that reveal size or strength, and a difference in value through the behavior of a motivated owner. Because owners have usually won a contest to obtain the resource and have invested in it (learning its features, settling boundaries with neighbors), ownership, ability and value tend to coincide, and observations alone rarely show which of them settles a contest. Experiments that separate them, such as the replacement experiments of [7.18.26](/7.18.26), suggest that animals assess both ability and value and do not rely on an arbitrary convention.

### 25.2.3. The War of Attrition

In many contests, nobody is injured: two males display at each other, or chase each other in circles, until one gives up. Maynard Smith (1974) modeled such contests as a *war of attrition*.

**Definition 25.2.2 (War of Attrition)** In a **war of attrition**, two contestants for a resource of value $V$ display until one of them gives up; each pays a cost $kt$ for a contest of duration $t$, the cost of the time and energy spent, whether it wins or loses. A strategy is the time an individual is prepared to persist, chosen before the contest and not revealed to the opponent; the contestant prepared to persist longer wins $V$.

No pure strategy is stable: in a population in which everyone persists for time $T$, a mutant persisting slightly longer wins every contest at a slightly higher cost, and a mutant that gives up at once avoids the cost $kT$ that residents pay in the half of their contests they lose.

**Theorem 25.2.1 (ESS of the War of Attrition)** The war of attrition has a unique ESS, a mixed strategy in which the persistence time is drawn from the exponential distribution with mean $V/k$, with density

$$
p(x) = \frac{k}{V}\,\mathrm{e}^{-kx/V}, \qquad x \geq 0. \tag{25.2}
$$
At the ESS the expected payoff of a contestant is zero: the value of the resource is, on average, entirely dissipated in display costs.

**Proof** Let the opponent's persistence time have density $p$ and distribution function $F$. A contestant prepared to persist for time $x$ wins, at cost $kt$, if the opponent gives up at $t < x$, and loses, at cost $kx$, if the opponent persists longer:

$$
E(x) = \int_0^x (V - kt)\,p(t)\,\mathrm{d}t - kx\,[1 - F(x)].
$$
By the Bishop–Cannings theorem (Theorem 25.1.2), $E(x)$ must be constant for all $x$ in the support of the ESS. Differentiating, $E'(x) = (V - kx)p(x) - k[1 - F(x)] + kx\,p(x) = V p(x) - k[1 - F(x)]$, so the condition $E'(x) = 0$ requires $p(x)/[1 - F(x)] = k/V$: the probability of giving up per unit time, given that the opponent has not yet given up, is the constant $k/V$. This is the exponential distribution (25.2). Its payoff is $E(0) = 0$. That it is an ESS, and the only one, is shown by Bishop and Cannings (1978). $\square$

The theorem makes testable predictions: the durations of contests between equally matched opponents should follow an exponential distribution (a constant probability of giving up per unit time), with a mean that increases with the value of the resource and decreases with the cost of displaying. The strategy must also be concealed: a contestant that revealed in advance how long it was prepared to persist could be beaten by an opponent persisting slightly longer, so displays in a war of attrition should not betray the contestant's intentions. Real contests rarely satisfy the model's assumptions (contestants differ in ability, assess each other and adjust their persistence during the contest), and the assessment models of [7.18.26](/7.18.26) extend it in these directions.

## 25.3. Competition by Exploitation: The Ideal Free Distribution

Competitors may simply use up resources (*exploitation* or scramble competition) or may keep others away from them by dominance or territoriality (interference, or resource defense). The first question for an animal facing exploitation competition is where to forage.

### 25.3.1. The Ideal Free Model

Suppose there are two habitats, one rich and one poor, and no fighting or territoriality. The first arrivals will go to the rich habitat. As more competitors join them, the resources there are shared among more individuals, and the payoff per individual falls; eventually a newcomer does as well in the poor habitat, where it has fewer competitors. From then on, newcomers should fill the two habitats so that the payoff per individual remains equal in both. Stephen Fretwell and Henry Lucas (1969) called this outcome the ideal free distribution: "ideal" because the animals are assumed to know the profitability of every habitat, "free" because they are assumed to be free to settle wherever they do best, without exclusion by stronger competitors.

**Definition 25.3.1 (Ideal Free Distribution)** Let habitats $i = 1, \dots, m$ offer a payoff $W_i(n_i)$ to each of the $n_i$ individuals that settle there, decreasing with $n_i$. A distribution $(n_1, \dots, n_m)$ of $N = \sum_i n_i$ competitors is an **ideal free distribution** if no individual can increase its payoff by moving to another habitat:

$$
W_i(n_i) \geq W_j(n_j + 1) \quad \text{for all occupied habitats } i \text{ and all habitats } j \neq i.
$$
For large populations treated as continuous, the condition becomes: all occupied habitats give the same payoff, and no unoccupied habitat gives more.

The ideal free distribution is a Nash equilibrium of a population game, in which the "strategy" of an individual is its choice of habitat; because the payoffs decrease with crowding, it is also stable. The same condition defines an equilibrium of traffic in a road network, where it is known as Wardrop's principle: every route used has the same travel time.

The simplest case is a *continuous-input* system, in which food arrives in habitat $i$ at a constant rate $Q_i$ and is shared equally among the $n_i$ competitors present, as with insects drifting downstream past waiting fish. Then $W_i = Q_i/n_i$, and equal payoffs require

$$
\frac{n_i}{N} = \frac{Q_i}{\sum_j Q_j}, \tag{25.3}
$$
the *input matching rule* (Parker 1978): the proportion of competitors in each habitat equals the proportion of the resource input it receives.

### 25.3.2. Tests: Sticklebacks, Ducks and Dung Flies

Manfred Milinski (1979) tested the rule with six three-spined sticklebacks in a tank, into which he dropped water fleas (*Daphnia*) from pipettes at the two ends, at one end twice as fast as at the other. Within a few minutes the fish settled four at the rich end and two at the poor end, the only distribution at which no fish could gain by moving; when the rates were reversed, they redistributed to four and two again. David Harper (1982) did the same experiment with a flock of 33 mallards (*Anas platyrhynchos*): two people threw bread at different rates, and the flock divided between them in the ratio of the rates. Remarkably, the ducks reached the predicted distribution within about a minute, before most of them had taken a single piece of bread from both sites, so they must have assessed the input rates directly, by watching the bread arrive, rather than by sampling their own intake.

![The ideal free distribution in a continuous-input system. A: intake per individual Q/n in a rich patch (input Q = 2) and a poor patch (Q = 1); with six competitors the only distribution at which no individual gains by moving is four in the rich patch and two in the poor one, where both receive 0.5. B: an individual-based simulation of Milinski's stickleback experiment: each of six fish occasionally compares its intake with what it would obtain at the other end and moves if that is better, with small errors; end A first receives one third of the input, then (at t = 60) two thirds. The mean of 400 simulated groups (red) tracks the input-matching prediction (dashed). C: unequal competitors: if six of twelve fish eat twice as fast as the other six, four different distributions equalize the intake per competitive unit between a patch receiving two thirds of the input and one receiving one third; the most likely one, counted by the number of ways of assigning individual fish, has 8 fish in the rich patch, the same as predicted for equal competitors (after Milinski and Parker 1991)](./plots/ideal-free.py)

The ideal free model makes three predictions, of which these experiments tested only the first: the numbers of competitors should match the input rates; the intake rates should be equal in all patches; and the risk to prey should be the same everywhere (Kacelnik and colleagues 1992). A large comparative survey of tests found that the numerical prediction usually holds approximately, with a consistent deviation called *undermatching*: fewer competitors than predicted in the rich patches and more in the poor ones (Kennedy and Gray 1993). Undermatching is expected if animals cannot perfectly distinguish patches that differ in quality, if moving between patches has a cost, or if competitors are unequal.

The same logic applies in time. Female yellow dung flies (*Scathophaga stercoraria*) arrive at a fresh cowpat to lay eggs, most of them in the first minutes, fewer as the pat ages and forms a crust. Males wait on and around the pat and mate with arriving females, and each male must decide how long to wait before flying to a fresher pat. If most males left early, a male that stayed would have the late females to himself; if most stayed long, a male would do better to leave. Geoffrey Parker (1970) counted the males on pats of different ages and found that their numbers declined exponentially with time; given this distribution, the expected mating rate was about the same for males staying for any length of time. The males had reached an ideal free distribution over stay times, as sticklebacks and ducks do over space; how they do it (by fixed individual differences or by flexible responses to female arrivals and competitor numbers) is not known.

In the field, the ideal free model has been applied to habitat choice (the next chapter) and to the distribution of shorebirds over feeding areas. Red knots (*Calidris canutus*) wintering on seven large tidal flats in Britain, the Netherlands and France were distributed not in proportion to the area of each flat but so as to equalize the intake of mollusks per bird, given the density of prey and of other knots (Quaintenne and colleagues 2011).

### 25.3.3. Unequal Competitors

The ideal free model assumes that all competitors are equal, but they rarely are: in Harper's flock, a few dominant ducks took most of the bread. Geoffrey Parker and William Sutherland (1986) extended the model by counting *competitive units*: if one individual eats twice as fast as another, it counts as two units, and the stable distribution equalizes the intake per competitive unit across patches. Many distributions of individuals do so, and the observed numbers need not match the input. But the different distributions are not equally likely. Manfred Milinski and Parker (1991) pointed out that, if individuals settle at random among the stable distributions, the most likely numerical pattern often coincides with the prediction for equal competitors (panel C of the figure above): by chance alone, a population of unequal competitors will often look ideal free. The numerical test is therefore a weak test of the model, and a strong test requires measuring the intake of individuals.

Thomas Whitham (1978, 1980) studied a natural system with features of both ideal free and despotic competition. In spring, stem mothers of the gall aphid *Pemphigus betae* settle on the leaves of narrowleaf cottonwood (*Populus angustifolia*), each forming a gall in which she reproduces parthenogenetically; large leaves give up to seven times as many offspring as small ones. Females settling later must choose between sharing a large leaf with others and occupying a small leaf alone. Whitham's measurements showed that the average reproductive success was the same on leaves shared by one, two or three stem mothers, as the ideal free model predicts. Within a leaf, however, success was unequal: the best position is at the base of the leaf blade, where all the sap flowing into and out of the leaf passes, and stem mothers fight for it by kicking and shoving, sometimes for two days; if a basal female is removed, a distal one moves into her place.

### 25.3.4. Resource Defense and the Despotic Distribution

When the first settlers defend the resources they occupy, later arrivals are forced into poorer habitat even though they do worse there.

**Definition 25.3.2 (Despotic Distribution)** A **despotic distribution** is a distribution of competitors over habitats in which individuals that settle first, or are dominant, exclude others from the better habitats by territorial defense or aggression, so that individuals in better habitats obtain higher payoffs than those in poorer habitats and some may be excluded from breeding altogether (Fretwell and Lucas 1969; Brown 1969).

In Wytham Woods near Oxford, the oak woodland, the best breeding habitat for great tits (*Parus major*), is filled with territories every spring, and the surplus birds breed in hedgerows, where they raise fewer young; when territory owners in the wood are removed, birds from the hedgerows quickly move in (Krebs 1971). In red grouse (*Lagopus lagopus scoticus*), territorial birds hold the richest areas of heather moor, and the excluded birds live in flocks in poor habitat where their chances of survival are low; again, a removed owner is replaced by a bird from the flock (Watson 1967). Removal experiments of this kind, in which "floaters" fill vacancies at once, are the standard evidence that territorial behavior limits the number of breeders in good habitat. The economics of defending resources, which decides whether competition takes the ideal free or the despotic form, is analyzed in [7.18.26](/7.18.26).

The ideal free model can also be extended to other costs. Mark Abrahams and Lawrence Dill (1989) offered guppies a choice between two feeders, one of them in the presence of a predatory fish; the fish undermatched the food at the risky feeder, and by adding food there until the distribution was equal, the researchers measured how much extra food a guppy required to accept the risk, a direct measure of the **trade-off** between food and safety treated in [7.18.23](/7.18.23).

## 25.4. Producers and Scroungers

### 25.4.1. Two Ways to Maintain Variation

In many foraging groups, some individuals find food and others exploit what they find. *Producers* search for food or make it available (by digging, turning stones or opening seeds), and *scroungers* steal from producers or join them at their discoveries. Why should a population contain both?

One hypothesis is that scroungers are poorer competitors that "make the best of a bad job": the fitness of both decreases as scroungers become common, but producers always do better, and individuals scrounge only because they cannot produce effectively. Ruddy turnstones (*Arenaria interpres*) wintering on rocky shores in Scotland used six foraging techniques; dominant birds tended to rout seaweed for prey and displaced subordinates from the best patches, and subordinates often probed in sand or stole food exposed by dominants. When dominants were temporarily removed, some subordinates increased their routing (Whitfield 1990), a sign that their technique was a conditional response to their social status.

The other hypothesis is that producing and scrounging are equally good at a stable frequency, because each does best when rare: when most birds produce, there is plenty to steal; when most scrounge, competition for each discovery is intense and producing pays. This is negative frequency dependence, and the ESS is a stable mixture of the two behaviors in which they have equal payoffs (Barnard and Sibly 1981, from experiments with flocks of house sparrows, *Passer domesticus*). Treated in this way, the interaction is the *producer–scrounger game*, the most widely studied game of social foraging (Giraldeau and Caraco 2000).

### 25.4.2. The Rate-Maximizing Model

A simple model makes the second hypothesis quantitative (after Vickery and colleagues 1991). A group of $G$ foragers contains $G - S$ producers and $S$ scroungers. Each producer finds food patches at rate $\lambda$, each containing $F$ items. The finder eats $a$ items (the *finder's share*) before the scroungers arrive; then the remaining $F - a$ items are divided equally among the finder and all $S$ scroungers. The intake rates are

$$
W_{\mathrm{P}} = \lambda\left[a + \frac{F - a}{S + 1}\right], \qquad W_{\mathrm{S}} = \lambda\,(G - S)\,\frac{F - a}{S + 1}, \tag{25.4}
$$
since a scrounger joins every patch found by any of the $G - S$ producers.

**Proposition 25.4.1 (Stable Proportion of Scroungers)** In the model (25.4), producers and scroungers have equal intake rates when the proportion of scroungers is

$$
\hat{q} = \frac{S^*}{G} = 1 - \frac{a}{F} - \frac{1}{G}, \tag{25.5}
$$
provided this is positive; otherwise producing is always better. The equilibrium is stable: with fewer scroungers than $S^*$ scrounging pays more, with more scroungers producing pays more.

**Proof** Setting $W_{\mathrm{P}} = W_{\mathrm{S}}$ and multiplying by $(S + 1)/\lambda$ gives $a(S + 1) + F - a = (G - S)(F - a)$, that is $aS + F = G(F - a) - S(F - a)$, so $SF = G(F - a) - F$ and $S^* = G(1 - a/F) - 1$. $W_{\mathrm{S}} - W_{\mathrm{P}}$ is proportional to $(G - S - 1)(F - a) - a(S + 1)$, which decreases in $S$, so it is positive below $S^*$ and negative above. $\square$

The model predicts that scrounging should be more common when the finder's share is small (the patch is quickly reached by joiners, or the food is easily divided), and in larger groups. The rate at which patches are found does not matter, since it multiplies both payoffs; nor does the payoff to the population, which is maximized by having no scroungers at all, but this is not stable.

![The producer–scrounger game (Eq. 25.4) in a group of six foragers finding patches of ten items. A: when the finder eats only two items before the scroungers arrive, the scroungers' intake (red) falls steeply as they become common and equals the producers' intake (blue) at S* = 3.8 scroungers. B: when the finder's share is five items, the equilibrium falls to two scroungers. Points mark whole numbers of scroungers; the scrounger curve starts at one scrounger. C: the equilibrium proportion of scroungers, 1 − a/F − 1/G, falls with the finder's share and rises with group size G](./plots/producer-scrounger.py)

Kieron Mottley and Luc-Alain Giraldeau (2000) tested the model with captive flocks of six spice finches (*Lonchura punctulata*). The aviary was divided by a barrier: birds on the producer side could pull a string to release seeds into a dish on the other side, which they reached through a hole; birds on the scrounger side had no strings and could only eat from dishes filled by producers. Covering the dishes partially reduced the scroungers' access without affecting the producers, the equivalent of increasing the finder's share. When the number of birds on each side was fixed by the experimenters, scroungers did better when there were more producers, and the number of scroungers at which both did equally well was two to three with uncovered dishes and zero to one with covered dishes. When the birds were then free to move between the two sides, the numbers on the scrounger side converged over a few days on these predicted values in both treatments. The equilibrium was reached by behavioral decisions within the lifetime of the birds, presumably by learning which side paid more (the learning rules are discussed in [7.18.41](/7.18.41)), not by selection between genetic types.

### 25.4.3. Strategies, Tactics and Alternative Phenotypes

The two hypotheses for producers and scroungers apply equally to the alternative ways in which males compete for mates, and the distinction they draw is basic to the analysis of such alternatives (Davies, Krebs and West 2012). A *strategy*, in the evolutionary sense, is a genetically based decision rule; a *tactic* is a behavior pattern played as part of a strategy. A conditional strategy such as "call if large, act as a satellite beside a calling male if small" produces two tactics, and there is no reason for them to have equal payoffs: the satellite tactic is the best that a small male can do, but large callers do better. This is the case in natterjack toads (*Epidalea calamita*), whose small males sit silently beside loud callers and intercept females, and in many other species, often with a switch that depends on body size (the horned and hornless males of dung beetles, [7.18.5](/7.18.5#sec-5.6.3)). Where alternatives are genetically distinct strategies, as in the three male morphs of the ruff (*Calidris pugnax*), the marine isopod *Paracerceis sculpta* and the side-blotched lizard (*Uta stansburiana*), they can persist only if they have equal average success at a stable frequency, as in the producer–scrounger equilibrium, or if their frequencies cycle, as in the rock–paper–scissors game of the lizards. These cases are treated with the rest of sexual selection in [7.18.28](/7.18.28).

## 25.5. Animal Personality and Behavioral Syndromes

### 25.5.1. Consistent Individual Differences

The ESS analyses of this chapter predict variation between individuals: some play Hawk and some Dove, some produce and some scrounge. Studies of many animals have shown that individuals of the same population also differ in continuous behavioral traits, such as boldness toward predators, exploration of a new environment, activity and aggression toward conspecifics, and that these differences are consistent over time and across situations. Such differences were long treated as noise around an adaptive mean; since about 2000 they have become a field of research in themselves.

**Definition 25.5.1 (Animal Personality)** **Animal personality** is the set of consistent differences in behavior between individuals of a population that persist over time, so that an individual's behavior in one test predicts its behavior in later tests of the same kind.

**Definition 25.5.2 (Behavioral Syndrome)** A **behavioral syndrome** is a correlation, across individuals of a population, between behaviors expressed in different contexts or situations, such as between boldness toward predators and aggressiveness toward conspecifics (Sih and colleagues 2004).

The consistency of a behavior is measured by its repeatability, the fraction of the total variance in repeated measurements that is due to differences between individuals,

$$
R = \frac{\sigma^2_{\mathrm{ind}}}{\sigma^2_{\mathrm{ind}} + \sigma^2_{\mathrm{w}}}, \tag{25.6}
$$
where $\sigma^2_{\mathrm{ind}}$ is the variance among individual means and $\sigma^2_{\mathrm{w}}$ the variance among measurements of the same individual. $R$ is estimated as an intraclass correlation from a one-way analysis of variance or, now usually, from a mixed model with individual as a random effect; a meta-analysis of 759 estimates found an average repeatability of behavior of about 0.37 (Bell, Hankison and Laskowski 2009). Repeatability sets an upper limit to the **heritability** of the behavior, since the variance among individuals includes the additive genetic variance as one component ([7.4.24](/7.4.24)).

![Measuring personality (simulated data). A: the boldness of 12 individuals measured in five trials each; individuals differ in their means (bars), and the measurements of the same individual scatter around its mean, giving a repeatability of about 0.5. B: individual means of boldness and of aggression in a population in which the two traits are correlated across individuals, a behavioral syndrome. C: a population with no such correlation: each trait is consistent, but they vary independently](./plots/personality.py)

The best-studied case is the great tit. Each bird caught in a nest-box population near Arnhem in the Netherlands was kept overnight in an aviary and released the next morning into a small room with five artificial trees, and the number of flights and hops in the first two minutes was used as a score of exploration. The score was repeatable and heritable: offspring resembled their parents, and four generations of artificial selection for fast and for slow exploration produced strongly diverged lines (Dingemanse and colleagues 2002; Drent and colleagues 2003). Fast explorers were also more aggressive toward conspecifics, bolder toward novel objects, more likely to scrounge food from others, and showed lower physiological stress responses when handled. Correlated traits of this kind, along an axis from "proactive" (fast, bold, aggressive, routine-forming) to "reactive" (slow, cautious, flexible) individuals, have been found in many vertebrates, and personalities have been described in insects, spiders and cephalopods as well.

### 25.5.2. Why Are Individuals Consistent?

Two questions arise. First, what maintains variation in a personality trait? Second, why are traits correlated, and why is behavior consistent at all, when a perfectly flexible individual could adjust each behavior to each situation?

Variation can be maintained by negative frequency dependence, as for hawks and doves or producers and scroungers: fast explorers may do best in a population of slow explorers and vice versa. It can also be maintained by fluctuating selection, if different personalities do best in different environments that vary in space or time. In the Dutch great tits, survival depended on personality in opposite ways in different years: after winters with abundant beech mast, when competition for food was relaxed, slow-exploring females survived better, and fast-exploring males did better in the resulting intense competition for breeding territories; after poor mast years, fast-exploring females and slow-exploring males survived better (Dingemanse and colleagues 2004). The pattern is complex, and only long-term studies can reveal it.

Correlations between traits may reflect constraints: if boldness toward predators and aggressiveness share hormonal or genetic mechanisms, they cannot be optimized independently, and the behavior in one context may be maladaptive. In three-spined sticklebacks, however, the correlation between aggressiveness and boldness was present in populations exposed to predators and absent in populations without them (Bell 2005), which suggests that the correlation is itself shaped by selection. An influential adaptive explanation links personality to **life history** (Wolf and colleagues 2007). An individual with large expected future reproduction (because it has accumulated resources, a territory or social status) has more to lose by taking risks than an individual with little to lose, and should therefore be cautious in every risky context, in foraging, toward predators and in fights. If differences in future prospects arise and are self-reinforcing (cautious individuals survive to accumulate more), consistent differences in risk-taking across contexts follow. Consistent with this view, a meta-analysis found that bolder individuals tend to have higher reproductive success but lower survival than shyer ones (Smith and Blumstein 2008).

Personality has consequences for social behavior: in cooperatively breeding meerkats (*Suricata suricatta*) and Seychelles warblers (*Acrocephalus sechellensis*), contributions to helping and exploratory behavior are repeatable, but they did not predict which individuals became dominant breeders or gained extra-pair matings (Carter and colleagues 2014; Edwards and colleagues 2017). Some researchers have argued that the personality framework adds mainly new terms to the old study of individual variation (Beekman and Jordan 2017); others reply that it has shown that the variance around the mean is itself a trait with ecological and evolutionary consequences, for example for dispersal, which bold individuals often undertake more readily ([7.18.26](/7.18.26)), and for the spread of innovations and diseases through social networks ([7.18.27](/7.18.27)).

## Summary

- When payoffs depend on what others do, behavior is analyzed with evolutionary game theory. A strategy is an inherited decision rule; the phenotypic gambit ignores genetic details.
- A Nash equilibrium (Definition 25.1.1) is a best reply to itself; an ESS is a Nash equilibrium that also resists invasion by mutants that do equally well against residents (Proposition 25.1.1).
- The replicator dynamics (Definition 25.1.2, Eq. (25.1)) increases strategies that do better than average. Every ESS is an asymptotically stable rest point, and an interior ESS attracts all interior trajectories (Theorem 25.1.1); in the hawk–dove game the mixed state $p^* = V/C$ is the only stable equilibrium (Example 25.1.1).
- At a mixed ESS all strategies in the support earn equal payoffs (Theorem 25.1.2); the mixture can be a polymorphism or a randomizing strategy. If $V \geq C$, fights escalate, as in fig wasps and bowl and doily spiders.
- Asymmetric contests:

  | Model | Key result |
  |---|---|
  | Hawk–dove–bourgeois (Example 25.2.1) | Bourgeois (Definition 25.2.1) is an ESS if $V < C$, even for a payoff-irrelevant asymmetry |
  | Correlated asymmetries | The contestant with greater fighting ability or resource value should escalate |
  | War of attrition (Definition 25.2.2) | Exponential persistence times with mean $V/k$, zero expected payoff (Theorem 25.2.1) |

  The speckled wood butterfly, once the example of the bourgeois rule, does not follow it.
- The ideal free distribution (Definition 25.3.1) equalizes payoffs across habitats; in continuous-input systems it gives input matching (Eq. (25.3)), confirmed in sticklebacks, ducks and, over time, dung flies, with frequent undermatching. With unequal competitors the numerical prediction is a weak test. Resource defense produces a despotic distribution (Definition 25.3.2), shown by removal experiments.
- Producers and scroungers coexist either because scroungers make the best of a bad job (turnstones) or at a frequency-dependent equilibrium $1 - a/F - 1/G$ (Proposition 25.4.1), confirmed in spice finches. Tactics of a conditional strategy need not have equal payoffs; genetic strategies must.
- Animal personality (Definition 25.5.1) and behavioral syndromes (Definition 25.5.2) are measured by repeatability (Eq. (25.6)); they are maintained by frequency dependence, fluctuating selection (great tits) and differences in future prospects.

## Questions

1. Show that in the hawk–dove game with $V < C$ the mixed strategy $p^* = V/C$ satisfies the second ESS condition against every mutant mixed strategy $q \neq p^*$, by computing $E(p^*, q) - E(q, q)$.

   **Answer** Write $E(p, q)$ for the payoff of a player who plays Hawk with probability $p$ against one who plays Hawk with probability $q$: $E(p, q) = pq\frac{V - C}{2} + p(1 - q)V + (1 - p)(1 - q)\frac{V}{2}$. Then $E(p^*, q) - E(q, q) = (p^* - q)\left[q\frac{V - C}{2} + (1 - q)V - (1 - q)\frac{V}{2}\right] = (p^* - q)\left[\frac{V}{2} - \frac{C}{2}q\right] = \frac{C}{2}(p^* - q)(p^* - q) = \frac{C}{2}(p^* - q)^2 > 0$, using $V = Cp^*$. Since every $q$ does equally well as $p^*$ against $p^*$ (Theorem 25.1.2), this inequality is exactly the second ESS condition.
2. In the hawk–dove–bourgeois game (Example 25.2.1), suppose that owners place a value $V_{\mathrm{o}}$ on the resource and intruders a value $V_{\mathrm{i}} < V_{\mathrm{o}}$, both less than $C$. Without full calculation, explain why this asymmetry makes Bourgeois more likely to evolve than the paradoxical strategy that plays Hawk as intruder and Dove as owner.

   **Answer** Both conventions avoid fights between their users, so their payoffs against themselves are the expected value of winning in the role in which they win: Bourgeois wins as owner and collects $V_{\mathrm{o}}/2$ on average, the paradoxical strategy wins as intruder and collects only $V_{\mathrm{i}}/2$. Against mutant hawks, a Bourgeois player escalates as owner, where it has more at stake, whereas the paradoxical player escalates as intruder. Bourgeois therefore has a higher payoff when common and is harder to invade, and from a mixed starting population selection is more likely to carry the population to Bourgeois. More generally, any asymmetry in value or ability that is correlated with ownership tips the balance toward respecting ownership, which may explain why owners usually win.
3. In Milinski's experiment, the sticklebacks reached the 4 : 2 distribution within minutes. List the assumptions of the ideal free model, and for each, describe how its violation would change the observed distribution.

   **Answer** (1) Animals are equal competitors: if some are better, the numbers need not match the inputs, though by chance they often appear to (Section 25.3.3). (2) Animals know the profitability of each patch ("ideal"): with imperfect information they spread more evenly than predicted, producing undermatching, and take longer to respond to a change. (3) Animals are free to move, without cost or exclusion ("free"): travel costs make them stay where they are unless the gain is large, again causing undermatching and lag; exclusion by dominants produces a despotic distribution with unequal intakes. (4) Payoffs depend only on food and competitors: if one patch is more dangerous, fewer animals use it than its food predicts (Abrahams and Dill 1989). (5) Input is continuous: if prey are depleted, the profitability of a patch changes with time and the prediction becomes one of equal intake rather than input matching.
4. Using Eq. (25.5), predict how the proportion of scroungers should change (a) when a flock of house sparrows feeds on a large carcass of seeds rather than scattered single seeds; (b) when the group size increases from 4 to 20; (c) when producers are given food in covered dishes that only they can open quickly. Compare with the spice finch experiment.

   **Answer** (a) A large patch relative to what the finder can eat before others arrive means $a/F$ is small, so the predicted proportion of scroungers is large. (b) The term $1/G$ falls from 0.25 to 0.05, so the proportion of scroungers rises by 0.2. (c) Covering the dishes increases the finder's share $a$ relative to $F$, so scrounging should decline. In the spice finch experiment, covered dishes lowered the equilibrium number of scroungers in a flock of six from two or three to zero or one, and the birds converged on these numbers when free to choose.
5. Derive the war of attrition prediction that the probability that a contest between matched opponents lasts longer than $t$ is $\mathrm{e}^{-2kt/V}$. Suggest how you would test whether a population of territorial damselflies settles its aerial contests by a war of attrition.

   **Answer** A contest lasts longer than $t$ only if both contestants are prepared to persist beyond $t$. At the ESS each persistence time is exponential with rate $k/V$, independently, so the probability is $(\mathrm{e}^{-kt/V})^2 = \mathrm{e}^{-2kt/V}$: contest durations are exponential with mean $V/(2k)$. A test: record many contest durations between males of similar size and condition and check whether the log of the proportion of contests still in progress declines linearly with time (a constant hazard of ending); manipulate the value of the resource (for example, territories with more or fewer females or oviposition sites) and check that the mean duration increases with value; and test whether the eventual loser can be predicted from his behavior early in the contest, which the model forbids. In damselflies, the fat reserves of the loser predict contest duration, suggesting an energetic war of attrition based on self-assessment ([7.18.26](/7.18.26)).
6. (Open question) Great tits that explore quickly are also more aggressive and more likely to scrounge. Propose a hypothesis linking these traits through the life-history argument of Wolf and colleagues, and design a study that could test it in the wild.

   **Answer** Hypothesis: individuals with low expected future reproduction (for example, young birds without a territory, or birds in poor condition) gain more by taking risks now, so they should be bold, explore quickly, fight readily and exploit others' discoveries, whereas birds with good prospects should be cautious. Predictions: within a population, exploration speed should be negatively related to survival and positively to current reproductive investment; experimentally improving an individual's prospects (for example, giving it a high-quality territory or supplementary food in winter) should make it more cautious, if personality is plastic in this way; and the correlation between traits should be stronger where differences in prospects are large. A study could combine the standard novel-room test of exploration, repeated over years, with field measures of aggression (responses to a model intruder) and scrounging at RFID feeders, long-term survival and breeding records, and a food supplementation experiment in a subset of territories.
