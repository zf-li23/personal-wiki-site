---
title: Harvesting and Pest Management
description: "Population ecology applied to management: surplus production and the maximum sustainable yield; fixed-quota and fixed-effort harvesting, the saddle-node collapse and the slow decline under an overestimated quota; the Schaefer model and catch–effort data; escapement, compensation, hyperstability and depensation; the Peruvian anchoveta and other collapses; the Gordon–Schaefer model, maximum economic yield, open access and the tragedy of the commons; discounting and the modified golden rule; harvesting under uncertainty; pest status and the economically optimal level of control; pest resurgence and secondary pests in a pest–enemy model; pesticide resistance, transgenic crops and decision support; bioaccumulation and biomagnification."
---

Two of the oldest practical uses of population ecology pull in opposite directions. In harvesting, people want a population of fish, game or timber to stay productive while they remove part of it every year; in pest management, they want a population to stay small while doing as little damage as possible to everything else. Both are questions about the same object, the net recruitment of a population as a function of its density, and both are answered with the models of the earlier chapters: the logistic equation and its generalizations (7.19.10, 7.19.11), stochastic growth (7.19.15), compensatory mortality (7.19.24) and predator–prey dynamics (7.19.25, 7.19.27). This chapter first develops harvesting theory: the maximum sustainable yield, why the way a harvest is regulated matters more than its size, and how economics and uncertainty change the answer. It then turns to pests, building on the entomological account of [7.17.40](/7.17.40), where the economic injury level, insecticides and their resistance, biological control and integrated pest management are described; here the emphasis is on the population dynamics that make pesticides backfire and on the accumulation of persistent chemicals in food chains. The pollution of whole ecosystems and agriculture as an ecological system follow in 7.19.54.

## 53.1. Surplus Production and the Maximum Sustainable Yield

### 53.1.1. Renewable Resources and Surplus Production

Natural resources are the materials and energy that people draw from nature. They are *renewable* when natural processes regenerate them after use on a human time scale (forests, grasslands, fish, wildlife, fresh water), and nonrenewable when they are depleted by use (metal ores, fossil fuels). Biological resources are renewable only conditionally: a population regenerates because its members reproduce, and if too many are removed it cannot. Harvesting theory asks how much can be taken without destroying this capacity.

**Definition 53.1.1 (Surplus Production and Sustainable Yield)** Let a population without harvesting follow $\mathrm{d}N/\mathrm{d}t = F(N)$, where $F(N)$ is its net recruitment (births and individual growth minus natural deaths) at density $N$. $F(N)$ is the **surplus production** of the population: the amount by which it would increase in a unit of time. A harvest rate $Y$ is a **sustainable yield** if there is a density $N^*$ with $F(N^*) = Y$, so that removing $Y$ per unit time keeps the population at $N^*$ indefinitely.

The surplus is zero at $N = 0$ and at the carrying capacity, where recruitment and natural mortality balance, and positive in between: a population at **carrying capacity** produces nothing that can be harvested without reducing it, and an unharvested population "wastes" its surplus on growth until it reaches $K$. High yields therefore come from populations held below, often well below, their carrying capacity.

**Definition 53.1.2 (Maximum Sustainable Yield)** The **maximum sustainable yield** (MSY) of a population is the largest sustainable yield, $\mathrm{MSY} = \max_N F(N)$; it is taken by holding the population at the density $N_{\mathrm{MSY}}$ at which $F$ is maximal.

**Proposition 53.1.1 (MSY of Logistic and θ-Logistic Populations)** (a) For **logistic growth**, $F(N) = rN(1 - N/K)$, the MSY is $rK/4$, taken at $N_{\mathrm{MSY}} = K/2$. (b) For the θ-logistic model of Definition 10.3.1, $F(N) = rN[1 - (N/K)^\theta]$,

$$
N_{\mathrm{MSY}} = K(1 + \theta)^{-1/\theta}, \qquad \mathrm{MSY} = \frac{\theta}{1 + \theta}\,rN_{\mathrm{MSY}}. \tag{53.1}
$$

**Proof** (a) $F'(N) = r(1 - 2N/K) = 0$ at $N = K/2$, where $F = rK/4$; $F'' = -2r/K < 0$. (b) $F'(N) = r[1 - (1 + \theta)(N/K)^\theta] = 0$ gives $(N/K)^\theta = 1/(1 + \theta)$; substituting, $F = rN_{\mathrm{MSY}}[1 - 1/(1 + \theta)]$. For $\theta = 1$ this reduces to (a). $\square$

As $\theta$ increases from 0 to infinity, $N_{\mathrm{MSY}}/K$ increases from $1/\mathrm{e}$ to 1. Large mammals, whose density dependence acts mainly near carrying capacity ($\theta > 1$, Section 10.3.1), are most productive only slightly below $K$; fish with strong density dependence of juvenile survival may be most productive at a third of $K$ or less. The logistic value $K/2$ is a special case, not a law; it also hides the time scale: the surplus is proportional to $r$, so that a slowly reproducing population (whales, sharks, long-lived trees) can sustain only a small fraction of its standing stock.

### 53.1.2. Fixed-Quota Harvesting

How the harvest is regulated determines whether an equilibrium can be maintained. The two simplest rules fix either the amount taken or the effort spent taking it.

**Definition 53.1.3 (Fixed-Quota and Fixed-Effort Harvesting)** In **fixed-quota harvesting** a constant amount $H$ is removed per unit time, independently of the density of the population (a total allowable catch, a number of hunting tags, a timber quota). In **fixed-effort harvesting** a constant effort $E$ is applied (boat-days of fishing, hunter-days, area cut per year), and the catch is $qEN$, proportional to density, where the catchability $q$ is the fraction of the population taken per unit of effort.

With a logistic population and a quota,

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = rN\left(1 - \frac{N}{K}\right) - H. \tag{53.2}
$$

In the dimensionless variables $x = N/K$, $\tau = rt$ and $h = H/(rK)$, the quota measured in units of $rK$ (so that the MSY quota is $h = 1/4$),

$$
\frac{\mathrm{d}x}{\mathrm{d}\tau} = x(1 - x) - h. \tag{53.3}
$$

**Proposition 53.1.2 (Equilibria under a Fixed Quota)** (a) If $0 < h < 1/4$, Eq. (53.3) has two equilibria

$$
x_\pm = \frac{1 \pm \sqrt{1 - 4h}}{2};
$$
$x_+ > 1/2$ is stable, $x_- < 1/2$ is unstable, and populations below $x_-$ decline to extinction in finite time. (b) At $h = 1/4$ the two equilibria merge at $x = 1/2$, which is semistable: populations above it decline to it, populations below it decline to extinction. (c) If $h > 1/4$, there is no equilibrium, and every population is harvested to extinction in finite time. The transition at $h = 1/4$ is a **saddle-node bifurcation** ([7.6.33](/7.6.33#def-33.2.2)).

**Proof** Equilibria solve $x^2 - x + h = 0$. Let $f(x) = x(1 - x) - h$; $f'(x) = 1 - 2x$ is negative at $x_+$ and positive at $x_-$, so (a) follows by linearization ([2.4.11](/2.4.11)); between the roots $f > 0$, outside them $f < 0$, so a population below $x_-$ keeps declining; near $x = 0$ its rate of decline approaches $h > 0$, so it reaches zero in finite time. (b) At $h = 1/4$, $f(x) = -(x - 1/2)^2 \le 0$. (c) For $h > 1/4$, $f(x) = -[(x - 1/2)^2 + h - 1/4] < 0$ for all $x$. $\square$

The MSY quota is therefore the most dangerous quota possible: it is harvested at a semistable point, and any shortfall of recruitment, from a bad year or from an overestimate of $r$ or $K$, sends the population below $N_{\mathrm{MSY}}$, where the same quota now exceeds the surplus and drives it further down (Figure 1A). A quota slightly below the MSY is little safer, because its unstable threshold $x_-$ lies close to $x_+$. Near the bifurcation the stable equilibrium also loses resilience: the return rate after a small perturbation is $-f'(x_+) = \sqrt{1 - 4h}$, in units of $r$, which tends to zero as $h \to 1/4$, the **critical slowing down** of Definition 39.4.2.

The time scale of collapse is deceptive. If the quota exceeds the MSY, the decline begins slowly.

**Proposition 53.1.3 (Time to Extinction under an Excessive Quota)** Let $h = 1/4 + \varepsilon$ with $\varepsilon > 0$. A population starting at carrying capacity is harvested to extinction after the dimensionless time

$$
T = \frac{2}{\sqrt{\varepsilon}}\arctan\frac{1}{2\sqrt{\varepsilon}} \;\approx\; \frac{\pi}{\sqrt{\varepsilon}} \quad (\varepsilon \to 0). \tag{53.4}
$$

**Proof** Here $\mathrm{d}x/\mathrm{d}\tau = -[(x - 1/2)^2 + \varepsilon]$, so $T = \int_0^1 \mathrm{d}x/[(x - 1/2)^2 + \varepsilon] = \varepsilon^{-1/2}[\arctan((x - 1/2)/\sqrt{\varepsilon})]_0^1$, which is Eq. (53.4); for small $\varepsilon$ the arctangent tends to $\pi/2$. $\square$

A quota 1% above the MSY ($\varepsilon = 0.0025$) takes $T \approx 59$ units of $1/r$ to exhaust the stock, about 120 years for a fish with $r = 0.5$ per year; a quota 10% above it takes 16 units, about 30 years (Figure 1D). Most of this time is spent passing slowly through the neighborhood of $x = 1/2$, the "ghost" of the vanished equilibrium, where the population declines by a fraction of a percent per year, well within the noise of stock assessments. When the decline finally accelerates, it is fast. Managers who judge a quota by the absence of visible decline in its first decades are therefore misled.

### 53.1.3. Fixed-Effort Harvesting and the Schaefer Model

With a fixed effort, the logistic model with harvest proportional to stock is the *Schaefer model* (Schaefer 1954):

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = rN\left(1 - \frac{N}{K}\right) - qEN, \qquad \frac{\mathrm{d}x}{\mathrm{d}\tau} = x(1 - x) - ex, \quad e = \frac{qE}{r}. \tag{53.5}
$$

The harvest is now a line through the origin with slope $e$ (Figure 1B). Fishing adds a per capita mortality $qE$, like the extra mortality in the bifurcation diagram of Section 10.3.2.

**Proposition 53.1.4 (Fixed Effort)** (a) For $0 \le e < 1$, Eq. (53.5) has the globally stable equilibrium $x^* = 1 - e$ (for $x_0 > 0$), with return rate $1 - e$; for $e \ge 1$ the population declines to zero, the transition at $e = 1$ being a transcritical bifurcation. (b) The sustainable yield, in units of $rK$, is $Y(e) = e(1 - e)$, maximal at $e_{\mathrm{MSY}} = 1/2$, where $Y = 1/4$ and $x^* = 1/2$. (c) If the effort exceeds $e_{\mathrm{MSY}}$ by a fraction $\delta$, $e = (1 + \delta)/2$ with $0 \le \delta < 1$, the yield falls only by the factor $1 - \delta^2$ and the population stays at $x^* = (1 - \delta)/2$.

**Proof** (a) Eq. (53.5) is the logistic equation with growth rate $1 - e$ and carrying capacity $1 - e$, whose positive equilibrium is globally stable for $1 - e > 0$ (Proposition 10.2.3); for $e \ge 1$, $\mathrm{d}x/\mathrm{d}\tau < 0$ for $x > 0$. (b) $Y = ex^* = e(1 - e)$. (c) Substitute $e = (1 + \delta)/2$: $Y = (1 + \delta)(1 - \delta)/4$. $\square$

The contrast with Proposition 53.1.2 is the central lesson of harvesting theory (Figure 1C). An overestimated MSY quota leads to certain extinction; an effort 20% above the MSY effort costs only 4% of the yield. The reason is the feedback built into effort regulation: when the stock falls, a fixed effort catches less, and the harvest rate drops below recruitment, so that the stock recovers. The price is a variable catch, which falls whenever the stock does, and a political temptation: when catches fall, fishers want more effort, and gradually increasing effort chasing a shrinking yield can drive a stock to $e \ge 1$. Regulating effort also requires monitoring it, which is harder than it sounds: fleets become more efficient each year ("effort creep", a rise of $q$ by a few percent per year from better engines, sonar and navigation), and vessel monitoring systems usually cover only large boats.

![Fixed-quota and fixed-effort harvesting of a logistic population (dimensionless: stock x = N/K, rates in units of rK). A: the surplus production curve x(1 − x) and three quotas. A quota below the MSY (h = 0.15) crosses the curve twice: the upper equilibrium (filled) is stable, the lower (open) is an extinction threshold, and arrows show the direction of change; the MSY quota h = 0.25 just touches the peak (semistable); a larger quota leaves no equilibrium. B: fixed efforts are lines ex through the origin; each crosses the curve once at a stable equilibrium x* = 1 − e, and the MSY effort e = 0.5 passes through the peak. C: equilibria against the harvest relative to its MSY level: under a quota the stable and unstable equilibria meet in a saddle-node bifurcation at the MSY and the population collapses beyond it; under a fixed effort the equilibrium declines linearly and reaches zero only at twice the MSY effort (transcritical bifurcation). D: time for a population starting at K to be harvested to extinction when the quota exceeds the MSY (Proposition 53.1.3; dots: numerical integration).](./plots/quota-effort.py)

Effort regulation also gives a method of estimation. At equilibrium the catch per unit effort (CPUE), $Y/E = qN^*$, is an index of abundance.

**Proposition 53.1.5 (Catch–Effort Relationship of the Schaefer Model)** At equilibrium the CPUE of the Schaefer model decreases linearly with effort,

$$
\frac{Y}{E} = qK - \frac{q^2K}{r}E \equiv \alpha - \beta E, \tag{53.6}
$$
and the yield $Y = \alpha E - \beta E^2$ is maximal at $E_{\mathrm{MSY}} = \alpha/(2\beta)$, with $\mathrm{MSY} = \alpha^2/(4\beta) = rK/4$.

**Proof** $N^* = K(1 - qE/r)$ from Proposition 53.1.4, so $Y/E = qN^*$ is Eq. (53.6); maximizing the parabola gives the rest. $\square$

Regressing CPUE on effort across years of a fishery therefore estimates the MSY and the MSY effort without separate estimates of $r$, $K$ and $q$, which is how surplus-production models were first fitted. The method assumes that each year's catch is in equilibrium with that year's effort, which is rarely true when effort is changing: a fishery that expands quickly sees high catch rates from the accumulated stock and overestimates the MSY. Modern fits treat Eq. (53.5) as a dynamic model of the time series of catches and abundance indices (observation-error or state-space fitting, [3.3](/3.3)), and they still face the problem that CPUE may not be proportional to abundance (Section 53.1.5).

### 53.1.4. Escapement, Proportional Harvesting and Compensation

Two further rules are used in practice. In *proportional harvesting* a fixed fraction of the population is taken each season, which is equivalent to a fixed harvest mortality and has the stability of fixed effort; most hunting of upland game birds is regulated this way. In *fixed-escapement harvesting* a fixed number of breeders is allowed to escape each season and everything above it is taken. In a discrete-time model $N_{t+1} = R(S_t)$ with $S_t$ the escapement, the sustainable yield of escapement $S$ is $R(S) - S$, maximal where $R'(S) = 1$; Reed (1979) showed that a constant escapement remains optimal when recruitment fluctuates randomly from year to year. Escapement requires counting the population before each harvest, and it is used where this is possible, for example for the sockeye salmon (*Oncorhynchus nerka*) of Bristol Bay, Alaska, whose fisheries open only when the counted spawning run exceeds the escapement target of each river.

All these rules assume that harvest mortality replaces part of the natural surplus. Whether it does is the question of compensation (Definition 24.4.1): if natural mortality falls when the harvest removes individuals that would have died anyway (the "doomed surplus" of Errington), the harvest is compensatory and costs the population little; if it does not, it is additive. In willow ptarmigan (*Lagopus lagopus*) in Norway, experimental harvests of 15% of the autumn population were partly compensated by lower natural mortality, but harvests of 30% were almost fully additive (Sandercock et al. 2011), because the hunting season coincided with the period of juvenile dispersal and territory establishment, when most natural mortality occurs, and the immigrants that would have compensated at low density were hunted too. Compensation is strongest when harvests precede the period of density-dependent mortality and when the population is near carrying capacity.

Harvests that remove one sex or one size class can change the dynamics qualitatively. Selective removal of male saiga antelope (*Saiga tatarica*) for their horns turned the demographic advantage of polygyny into an **Allee effect** (7.19.21): fertility collapsed when males became too rare to hold harems. Fishing that removes the largest fish selects for maturation at smaller size and younger age (fisheries-induced evolution, documented in Atlantic cod and other stocks), and it removes the large, old females whose eggs and larvae are often more numerous and more viable, so that the stock's recruitment declines faster than its biomass.

### 53.1.5. Hyperstability, Depensation and Multiple Equilibria

Fixed effort is safe in the Schaefer model because the catch per unit effort falls in proportion to the stock. For schooling fish this assumption fails. Sardines, anchovies and herring form a few large schools that follow predictable routes; a fleet with sonar finds and empties them almost as easily when there are few schools as when there are many. Catchability then increases as the stock declines.

**Proposition 53.1.6 (Harvest with Density-Dependent Catchability)** Let the catchability be $q(N) = q_0(K/N)^\beta$ with $0 < \beta < 1$, so that the dimensionless dynamics are

$$
\frac{\mathrm{d}x}{\mathrm{d}\tau} = x(1 - x) - e x^{1 - \beta}, \qquad e = \frac{q_0E}{r}. \tag{53.7}
$$
Then (a) $x = 0$ is locally attracting for every $e > 0$; (b) the positive equilibria solve $g(x) \equiv (1 - x)x^\beta = e$; $g$ has its maximum $e_{\mathrm c} = \frac{1}{1 + \beta}\left(\frac{\beta}{1 + \beta}\right)^\beta$ at $x_{\mathrm m} = \beta/(1 + \beta)$, so that for $e < e_{\mathrm c}$ there is a stable equilibrium above $x_{\mathrm m}$ and an unstable threshold below it, which merge in a saddle-node bifurcation at $e = e_{\mathrm c}$.

**Proof** Write $\mathrm{d}x/\mathrm{d}\tau = x^{1 - \beta}[g(x) - e]$. Since $g(0) = 0$, the bracket is negative near $x = 0$, so small populations decline (a). $g'(x) = x^{\beta - 1}[\beta - (1 + \beta)x]$ vanishes at $x_{\mathrm m}$, where $g$ is maximal; for $e < e_{\mathrm c}$ the equation $g = e$ has one root on each side of $x_{\mathrm m}$, and $g - e$ is positive between them and negative outside, which gives the stability. $\square$

In the limit $\beta \to 1$ the catch $e x^{1 - \beta}$ is independent of the stock: effort regulation of a perfectly schooling fish is quota regulation in disguise. And because the CPUE, $q(N)N \propto N^{1 - \beta}$, stays high while the stock declines (*hyperstability*), catch rates give no warning (Figure 2). The same multiple equilibria arise from *depensation*, a decline of per capita recruitment at low stock size (an Allee effect in recruitment): with harvest added to a strong Allee effect, the stock collapses at a saddle-node (Proposition 10.3.3), and reducing harvest afterwards does not restore it, because the unharvested population has its own extinction threshold. North Sea herring (*Clupea harengus*) collapsed in the 1970s and recovered only after a four-year closure; a statistical analysis of its stock–recruitment data indicates depensation (Perälä and Kuparinen 2017). The northern cod (*Gadus morhua*) of Newfoundland and Labrador, which had sustained fisheries for five centuries, collapsed in the late 1980s; the moratorium declared in 1992 cost some 30 000 jobs, and the stock remained far below its former level for more than two decades, possibly because the reduced stock allowed its former prey, which eat cod eggs and larvae, to increase (a predator-pit, a form of **regime shift**, Definition 39.4.1).

![Catchability that rises as the stock falls (Proposition 53.1.6; dimensionless stock x = N/K, effort e = q0 E/r). A: for β = 0.6 and e = 0.25 the per capita harvest e x^(−β) rises steeply at low stock and crosses the per capita growth 1 − x twice: a stable equilibrium (filled) and an extinction threshold (open). B: equilibria against effort: for ordinary catchability (β = 0) the stock declines linearly, as in Figure 1C; for schooling fish (β = 0.5, 0.8) a saddle-node fold appears at moderate effort (solid stable, dashed unstable). C: catch per unit effort relative to its value at K: with β > 0 it remains high while the stock is depleted (hyperstability).](./plots/hyperstability.py)

### 53.1.6. The Peruvian Anchoveta and the Lessons of Collapse

The Peruvian anchoveta (*Engraulis ringens*) lives in the cold, nutrient-rich upwelling of the Humboldt Current and formed the largest single-species fishery in the world from the early 1960s, its catch reduced to fish meal. Experts estimated the MSY at about 10 million tonnes a year, but the fleet and processing capacity grew beyond it, and landings reached about 12 million tonnes in 1970. In 1972–1973 an El Niño, by suppressing upwelling and productivity, coincided with intense fishing on a reduced stock, and landings fell to below 2 million tonnes in 1973. A moratorium was politically difficult, because tens of thousands of people depended on the industry, and the stock took two decades to recover; it suffered further setbacks in the El Niño years of 1983 and 1998. The case combines every theme of this section: a quota-like regime (high catchability of schools), an overestimated MSY, environmental fluctuations, and a fleet whose capacity made reduction costly.

Not every collapse is caused by fishing alone; the environment often provides the final blow, and populations crushed by a bad year recover more readily than those depleted by years of overfishing. But fishing pressure determines how far a bad year can push a stock. In China's seas, the wild large yellow croaker (*Larimichthys crocea*), once one of the four main commercial species, was depleted by intensive fishing of its spawning aggregations in the 1950s–1970s, including "knock fishing" that stunned whole schools with sound, and its wild stocks have not recovered despite massive aquaculture; China introduced a summer fishing moratorium in the East and Yellow Seas in 1995, since extended to all its waters. In 2021, about 62% of the world's assessed marine fish stocks were fished within biologically sustainable levels, the rest overfished (FAO 2024).

Surplus-production models treat the population as an undifferentiated biomass. *Dynamic pool* models, developed by Beverton and Holt (1957), separate recruitment, individual growth, natural mortality and fishing mortality by age or size, and they show that the yield depends also on the size at first capture, set by mesh size: catching fish too young forgoes their growth and their reproduction. An analysis of ten fish species in the seas around China found that for almost all of them the mesh sizes in use were smaller than those that would maximize the yield per recruit (Liang and Pauly 2017).

## 53.2. The Economics of Harvesting

### 53.2.1. The Gordon–Schaefer Model

Harvesting is a business, and the yield must be weighed against the cost of obtaining it. Gordon (1954) combined the Schaefer model with the simplest economics: a constant price $p$ per unit of catch and a constant cost $c$ per unit of effort (fuel, crew, wear of gear), so that the sustainable rent, revenue minus cost at equilibrium, is

$$
\pi(E) = pY(E) - cE = pqEK\left(1 - \frac{qE}{r}\right) - cE. \tag{53.8}
$$

It is convenient to define the stock $N_\infty = c/(pq)$ at which the catch of one unit of effort, $pqN$, just pays its cost.

**Definition 53.2.1 (Maximum Economic Yield)** The **maximum economic yield** (MEY, also called the economically optimum yield) is the sustainable yield obtained at the effort $E_{\mathrm{MEY}}$ that maximizes the sustainable rent $\pi(E)$.

**Proposition 53.2.1 (MEY of the Gordon–Schaefer Model)** If $N_\infty < K$,

$$
E_{\mathrm{MEY}} = \frac{r}{2q}\left(1 - \frac{N_\infty}{K}\right) < E_{\mathrm{MSY}} = \frac{r}{2q}, \qquad N_{\mathrm{MEY}} = \frac{K + N_\infty}{2} > \frac{K}{2}. \tag{53.9}
$$
If $N_\infty \ge K$, no effort is profitable.

**Proof** $\pi'(E) = pqK - 2pq^2KE/r - c = 0$ gives $E_{\mathrm{MEY}} = (r/2q)(1 - c/(pqK))$, and $N^* = K(1 - qE/r)$ gives $N_{\mathrm{MEY}}$; $\pi'' < 0$. $\square$

The economic optimum thus takes less effort and leaves a larger stock than the MSY (Figure 3A): the last units of effort before the MSY add little catch but full cost. The difference vanishes as the cost per unit effort tends to zero; for enterprises whose costs are mostly fixed (capital-intensive distant-water fleets), the variable cost $c$ is small, the economic optimum lies close to the MSY, and the incentive to overfish is strongest. Fixed costs do not change $E_{\mathrm{MEY}}$ at all, since they do not depend on effort; but they determine whether the fishery is profitable, and subsidies that lower $c$ push the stock down.

### 53.2.2. Open Access and the Tragedy of the Commons

The MEY is what a sole owner of the stock would choose. If access is open, every fisher who can cover the cost of effort will fish, regardless of the effect on others.

**Definition 53.2.2 (Open-Access Equilibrium)** The **open-access equilibrium** (bionomic equilibrium, Gordon 1954) of a fishery is the state in which effort has expanded until the sustainable rent is zero: revenue equals cost, $pqN = c$, so that the stock is $N_\infty = c/(pq)$.

**Proposition 53.2.2 (Open Access)** (a) In the Gordon–Schaefer model the open-access effort is $E_\infty = (r/q)(1 - N_\infty/K) = 2E_{\mathrm{MEY}}$. (b) Open access exceeds the MSY effort, and depletes the stock below $K/2$, if and only if $N_\infty < K/2$, that is, if $c/p < qK/2$. (c) If effort adjusts in proportion to profit (Smith 1968),

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = rN\left(1 - \frac{N}{K}\right) - qEN, \qquad \frac{\mathrm{d}E}{\mathrm{d}t} = kE(pqN - c), \tag{53.10}
$$
the open-access equilibrium $(N_\infty, E_\infty)$ with $0 < N_\infty < K$ is locally asymptotically stable, and the approach is oscillatory when $(rN_\infty/K)^2 < 4kpq^2N_\infty E_\infty$.

**Proof** (a) Zero rent at equilibrium means $N^* = N_\infty$, and $N^* = K(1 - qE/r)$ gives $E_\infty$; compare with Eq. (53.9). (b) $E_\infty > r/(2q)$ iff $1 - N_\infty/K > 1/2$. (c) The **Jacobian matrix** of Eq. (53.10) at $(N_\infty, E_\infty)$, using $r(1 - N_\infty/K) = qE_\infty$ and $pqN_\infty = c$, is

$$
J = \begin{bmatrix} -rN_\infty/K & -qN_\infty \\ kpqE_\infty & 0 \end{bmatrix},
$$
with $\operatorname{tr} J = -rN_\infty/K < 0$ and $\det J = kpq^2N_\infty E_\infty > 0$, so both eigenvalues have negative real parts ([2.4.11](/2.4.11)); they are complex when $(\operatorname{tr} J)^2 < 4\det J$. $\square$

System (53.10) is a **Lotka–Volterra model** with logistic prey (7.19.25, Section 25.3), in which the fishing fleet is the predator and profit is its numerical response. Starting from an unexploited stock, effort grows while catches are profitable, overshoots, depletes the stock below $N_\infty$, contracts as boats lose money, and settles after damped boom-and-bust oscillations (Figure 3B, C). Since capital (boats) cannot be withdrawn quickly, real fleets contract more slowly than they expand, which makes the overshoot worse.

Open access dissipates the whole rent of the resource and, when fishing is cheap relative to the price, overexploits it biologically: each fisher bears the full cost of his effort but only a share of the loss of stock it causes. This is a case of what Hardin (1968) called the *tragedy of the commons*: a resource open to all is overused because the benefit of use goes to the user and the cost is shared by everyone. Hardin's conclusion that common resources must be either privatized or regulated by the state is too pessimistic. Ostrom (1990) documented many communities that have managed common-pool resources (fisheries, pastures, forests, irrigation systems) sustainably for centuries by their own rules, and identified their conditions: clear boundaries of the resource and its users, rules adapted to local conditions, participation of users in making them, monitoring, graduated sanctions and conflict resolution. The real tragedy is that of open access, not of common property. Modern fisheries management uses both routes: limited entry, individual transferable quotas (shares of the total catch owned by fishers) and territorial use rights give fishers an interest in the future of the stock.

### 53.2.3. Discounting and Optimal Harvesting

A sole owner who maximizes profit over time must compare a fish caught now with a fish left to grow. Economics discounts future income at a rate $\delta$: money banked today grows by $\mathrm{e}^{\delta t}$, so income $\pi(t)$ in the future is worth $\mathrm{e}^{-\delta t}\pi(t)$ today. Let the unit cost of catching fish depend on their density, $c(N) = c/(qN)$ (the cost of effort divided by the catch per unit effort). The owner chooses the harvest $H(t) \ge 0$ to maximize the present value

$$
J = \int_0^\infty \mathrm{e}^{-\delta t}\,\bigl[p - c(N)\bigr]H\,\mathrm{d}t, \qquad \frac{\mathrm{d}N}{\mathrm{d}t} = F(N) - H. \tag{53.11}
$$

**Theorem 53.2.1 (Modified Golden Rule; Clark and Munro 1975)** Suppose the harvest rate can be varied freely (between zero and a large maximum). Then the optimal policy drives the stock as fast as possible to the level $N^*$ that solves

$$
F'(N^*) - \frac{c'(N^*)F(N^*)}{p - c(N^*)} = \delta \tag{53.12}
$$
and then holds it there by harvesting $H = F(N^*)$, provided $N^*$ is the unique maximizer of the function $W$ below.

**Proof** (Key steps.) Substitute $H = F(N) - \dot N$ in Eq. (53.11). Let $\Phi(N) = \int^N [p - c(s)]\,\mathrm{d}s$, so that $[p - c(N)]\dot N = \mathrm{d}\Phi(N)/\mathrm{d}t$. Integrating this term by parts,

$$
J = \int_0^\infty \mathrm{e}^{-\delta t}\,W\bigl(N(t)\bigr)\,\mathrm{d}t + \Phi(N_0), \qquad W(N) = \bigl[p - c(N)\bigr]F(N) - \delta\,\Phi(N),
$$
when $\mathrm{e}^{-\delta t}\Phi(N(t)) \to 0$. The present value is maximal when $N(t)$ stays at the maximizer of $W$ at all times, which is approached as quickly as the constraints on $H$ allow (the "most rapid approach path"). The condition $W'(N^*) = 0$ reads $-c'F + (p - c)F' - \delta(p - c) = 0$, which is Eq. (53.12). $\square$

The left side of Eq. (53.12) is the return on leaving a fish in the sea: its contribution to growth, $F'(N)$, plus the saving in harvesting cost from a denser stock (the second term is positive since $c' < 0$). The right side is the return on money in the bank. Two limits make the meaning clear:

- With $\delta = 0$, $W = [p - c(N)]F(N)$ is the sustainable rent, and Eq. (53.12) gives the MEY stock $N_{\mathrm{MEY}}$.
- As $\delta \to \infty$, the solution tends to $N_\infty$: an owner who values only the present behaves like the open-access fleet (Clark 1973).

For the logistic model without stock-dependent costs ($c = 0$), Eq. (53.12) becomes $r(1 - 2N^*/K) = \delta$, so $N^* = (K/2)(1 - \delta/r)$, and if the discount rate exceeds the intrinsic growth rate, $\delta \ge r$, the optimal stock is zero: it pays to catch every fish and invest the money elsewhere (Figure 3D). This "economically optimal extinction" is not a curiosity. Antarctic blue whales (*Balaenoptera musculus*) and many long-lived deep-sea fish such as orange roughy (*Hoplostethus atlanticus*, which can live for more than a century) grow at a few percent per year, below commercial discount rates of 5–10%, and Clark (1973) used the blue whale to show that profit maximization alone does not protect such species; only costs that rise steeply as the stock declines, regulation, or values not captured by the market (existence values, 7.19.50) do. The analysis exposes the assumptions of discounting rather than justifying extinction: discount rates that treat future generations' consumption as worth little, and markets that price fish but not whales.

![Bioeconomics of a logistic fishery (dimensionless: stock x = N/K, effort e = qE/r, money in units of prK; x∞ = c/(pqK)). A: sustainable revenue e(1 − e) and cost x∞e for x∞ = 0.3; the rent (shaded) is largest at the MEY effort (1 − x∞)/2 = 0.35, below the MSY effort 0.5, and vanishes at the open-access effort 1 − x∞ = 0.7, twice the MEY effort (Propositions 53.2.1, 53.2.2). B: open-access dynamics (Eq. 53.10, k = 1.5 in these units) from an unexploited stock with little effort (square), with the nullclines: the trajectory spirals into the bionomic equilibrium (dot). C: the same run in time: effort overshoots, the stock is depleted below its equilibrium and catches boom and bust before settling. D: the optimal steady stock under discounting (Theorem 53.2.1) against the discount rate relative to the intrinsic growth rate, for several cost levels: it falls from the MEY stock (δ = 0) toward x∞ (dotted) as δ increases; without stock-dependent costs (x∞ = 0) it reaches zero at δ = r.](./plots/gordon-schaefer.py)

### 53.2.4. Uncertainty, Precaution and Multiple Objectives

Real stocks fluctuate, and their parameters are known only roughly. Figure 4 compares three strategies in a model whose carrying capacity varies randomly from year to year. A quota of 90% of the deterministic MSY collapses the stock within a century in most runs: a run of bad years pushes the stock below the unstable threshold of Proposition 53.1.2, from which the quota drives it to extinction. A constant effort at the MSY level gives almost the MSY on average, with a variable catch, and never collapses the stock. A harvest control rule that reduces the fishing mortality when the stock falls below a trigger level gives a similar yield and protects the stock against the overestimation of its productivity, which the constant-effort rule does not.

![Harvest strategies in a fluctuating environment (annual surplus-production model, x' = x + 0.5x(1 − x/k_t) − H, with a carrying capacity k_t fluctuating with a coefficient of variation of 0.3 and positive autocorrelation; 400 runs of 100 years). A: one run, the same environment for all strategies: a fixed quota of 90% of the deterministic MSY (red), a constant harvest rate at the MSY level F_MSY = r/2 (blue), and a control rule (green) that harvests at 0.8 F_MSY above x = 0.4 and reduces the rate linearly to zero at x = 0.1. A series of poor years drives the quota-harvested stock below its threshold and to extinction. B: mean annual yield relative to the MSY (solid) and the coefficient of variation of the yield among years (hatched). C: probability that the stock falls below 5% of K within 100 years.](./plots/stochastic-harvest.py)

These results underlie the *precautionary approach* to fisheries, adopted in the FAO Code of Conduct for Responsible Fisheries and the UN Fish Stocks Agreement (both 1995): where knowledge is uncertain, management should be more cautious, and the absence of scientific certainty should not be used to postpone measures to protect a stock. In practice, the MSY has changed from a target into a limit. Fishing mortality is set below $F_{\mathrm{MSY}}$; a limit biomass $B_{\mathrm{lim}}$ below which recruitment is impaired, and a trigger biomass above it, define a harvest control rule like the green line of Figure 4; and the rule is tested by simulation against the uncertainties of the stock (management strategy evaluation). Simple rules of thumb express the same caution where data are poor: keep fishing mortality below natural mortality, keep the stock above the level that produces the MSY, and let fish spawn at least once before they are caught (Froese et al. 2016).

Fisheries also have more than one objective. Yield, profit, employment, the stability of catches, the protection of bycatch species (sea turtles, seabirds, small cetaceans caught incidentally) and the structure of the ecosystem conflict, and management chooses among the trade-offs rather than maximizing a single quantity. Harvest affects other species: the mean trophic level of world fisheries landings declined by about 0.1 per decade from the 1950s to the 1990s as large predatory fish were depleted and fisheries turned to smaller species lower in the **food chain** ("fishing down marine food webs", Pauly et al. 1998), and harvesting a predator or its prey changes the dynamics of both (Proposition 25.2.1). Ecosystem-based fisheries management sets harvests with these interactions in view. Social arrangements matter as much as biology: in Javanese teak (*Tectona grandis*) plantations, sharing timber profits with local people who guard the plantations against illegal logging increases the overall profit up to an intermediate share, which a model of the people's incentives can optimize (Lee et al. 2018).

## 53.3. Pest Management

### 53.3.1. Pest Status and the Optimal Level of Control

A pest is a species that people consider undesirable, at a density that causes them economic loss; the concept is economic, not biological ([7.17.40](/7.17.40#sec-40.5.1)). Whether a species is a pest depends on where its density fluctuates relative to the **economic injury level** (EIL, [Definition 40.5.1](/7.17.40#def-40.5.1) of 7.17.40), the lowest density at which the loss caused by the pest equals the cost of controlling it.

**Definition 53.3.1 (Pest Status)** A species whose density, without control, fluctuates mostly above its economic injury level is a *pest*; one whose density remains below it is not a pest, whatever damage individuals do. A **potential pest** is a species whose carrying capacity exceeds its EIL but whose density is held below it by natural enemies or other factors; it becomes an actual pest when these are removed.

The EIL of [Formula 40.5.1](/7.17.40#sec-40.5.2) of 7.17.40, $\mathrm{EIL} = C/(VIDK)$, answers a yes-or-no question: is a control measure with a fixed cost $C$ worth applying? When control can be applied at different intensities, the question becomes how far to reduce the pest.

**Proposition 53.3.1 (Economically Optimal Pest Density)** Let a control of intensity $u \ge 0$ cost $cu$ and reduce the pest from $N_0$ to $N = N_0\mathrm{e}^{-ku}$, and let the crop loss be $VDN$ ($V$ the value of the crop per unit yield, $D$ the yield lost per pest). If $N_0 > N^* = c/(kVD)$, the total cost $cu + VDN$ is minimized by reducing the pest to

$$
N^* = \frac{c}{kVD}; \tag{53.13}
$$
otherwise no control is optimal.

**Proof** In terms of $N$, the total cost is $T(N) = (c/k)\ln(N_0/N) + VDN$ for $N \le N_0$, with $T'(N) = -c/(kN) + VD$, which is negative below $N^*$ and positive above it; $T$ is therefore minimal at $N^*$ if $N^* < N_0$ and at $N_0$ (no control) otherwise. $\square$

At $N^*$ the marginal cost of further control, $c/(kN)$ per unit reduction of density, equals the marginal loss $VD$ that it prevents: reducing the pest further "does not pay" (Figure 5B). This is the sense of the definition, common in textbooks, of the economic injury level as the density at which the net benefit of control is greatest. It differs from the threshold of Pedigo's formula, which compares the total cost of one discrete application with the total loss it prevents; the two answer different questions, but they have the same structure, with $c/k$, the cost of reducing the pest by a factor $\mathrm{e}$, in place of $C/K$. Both show that eradication is rarely economic, that a more valuable crop justifies control at lower densities, and that cheaper or more effective control lowers the optimal density. The **economic threshold**, at which control is started so that the pest does not reach the EIL, is set lower to allow for the time control takes; for the potato leafhopper (*Empoasca fabae*) on alfalfa in the United States it is taken as 75% of the EIL, and the EIL was revised downward when the crop became more valuable (Chasen et al. 2015).

![Pest status and the optimal level of control. A: three species fluctuating around equilibria set by their resources and enemies (stochastic Ricker model), relative to an economic injury level (EIL, dashed): a pest whose density exceeds the EIL most of the time, a non-pest always below it, and a potential pest held below the EIL by natural enemies until these are removed (dotted line), after which its equilibrium rises above the EIL. B: costs against the pest density left after control (Proposition 53.3.1): the cost of control rises steeply as the target density approaches zero, the crop loss rises linearly with density, and the total is minimal at N* = c/(kVD), where further control costs as much as it saves.](./plots/pest-status.py)

### 53.3.2. Pest Resurgence and Secondary Pests

Broad-spectrum insecticides kill the natural enemies of pests as well as the pests themselves. **Pest resurgence** (7.19.25, Section 25.2.2) is the rapid increase of a target pest after treatment, to densities above those before it, because surviving or immigrating pests find abundant food and few enemies. Its relative is the secondary pest outbreak: a potential pest held down by enemies becomes an actual pest when a treatment aimed at another species kills those enemies. A pest–enemy model shows how both arise.

**Proposition 53.3.2 (Continuous Spraying of a Pest and Its Enemy)** Let a pest $N$ with logistic growth be attacked by an enemy $P$ with a linear **functional response**, and let an insecticide add per capita mortalities $h_N$ to the pest and $h_E$ to the enemy:

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = rN\left(1 - \frac{N}{K}\right) - aNP - h_NN, \qquad \frac{\mathrm{d}P}{\mathrm{d}t} = caNP - (m + h_E)P. \tag{53.14}
$$
If $N^\dagger = (m + h_E)/(ca) < K(1 - h_N/r)$, the system has the stable equilibrium

$$
N^* = \frac{m + h_E}{ca}, \qquad P^* = \frac{1}{a}\left[r\left(1 - \frac{N^*}{K}\right) - h_N\right] > 0;
$$
otherwise the enemy is eliminated and the pest settles at $K(1 - h_N/r)$ (or at zero if $h_N \ge r$).

**Proof** At an equilibrium with $P^* > 0$, $\mathrm{d}P/\mathrm{d}t = 0$ requires $caN^* = m + h_E$, and $\mathrm{d}N/\mathrm{d}t = 0$ then gives $P^*$, positive under the stated condition. The Jacobian matrix at this point has trace $-rN^*/K < 0$ and determinant $ca^2N^*P^* > 0$, so the equilibrium is stable, as for the prey-limited Lotka–Volterra model of Section 25.3. If the condition fails, the enemy's per capita growth $caN - m - h_E$ is negative at the pest's enemy-free equilibrium $K(1 - h_N/r)$, which is then stable. $\square$

As long as the enemy persists, the pest's equilibrium density is set by the enemy's requirements and does not depend on the mortality $h_N$ inflicted on the pest at all; mortality inflicted on the enemy raises it (Figure 6B). This is the Volterra principle of Proposition 25.2.1 in a pest–enemy system: a selective insecticide, which spares the enemies, achieves a long-term reduction of an enemy-regulated pest only if it is strong enough to replace the enemies' control altogether; a broad-spectrum insecticide raises the pest's equilibrium until it does. The model also shows the transient (Figure 6A): after a single heavy application the enemies, deprived of food, decline, and the pest overshoots when it recovers; killing the enemies too makes the overshoot larger. Repeated applications aimed at a key pest can keep the enemies of a secondary pest permanently depressed and its density above the EIL (Figure 6C). The model assumes a specialist enemy with a linear functional response; generalist enemies, which persist on other prey, and enemies with saturating responses change the details, but field studies show the predicted pattern repeatedly.

- In cotton in Arizona, the broad-spectrum organophosphate acephate increased the density of the plant bug *Lygus hesperus*, its target, relative to untreated plots, and depressed a wide range of its predators, whereas the selective insecticide flonicamid had neither effect (Asiimwe et al. 2014).
- Spraying malathion against the boll weevil (*Anthonomus grandis grandis*) in Texas was followed by outbreaks of two secondary pests, the beet armyworm (*Spodoptera exigua*) and the cotton aphid (*Aphis gossypii*) (Knutson et al. 2011).
- The brown planthopper (*Nilaparvata lugens*), a minor pest of rice before the Green Revolution, became the most damaging pest of rice in tropical Asia in the 1970s, as frequent spraying killed its spider and mirid predators. In Indonesia, a presidential decree of 1986 banned 57 insecticide formulations on rice and introduced integrated pest management through farmer field schools; insecticide use fell sharply and the outbreaks subsided.
- Some insecticides stimulate pest reproduction at sublethal doses (*hormesis*), which can add to resurgence.

![Pest resurgence and secondary pest outbreaks in a pest–enemy model (Eq. 53.14 with r = 1, K = 10, a = 1, c = 0.5, m = 1; the unsprayed pest equilibrium is 2, and the economic injury level is set at 4, dashed). A: a single application at t = 20 kills 90% of the pests and either 95% of their enemies (broad-spectrum, red) or none (selective, blue). The enemies decline for lack of food in both cases and the pest overshoots, but the overshoot above the EIL is larger when the enemies are killed. B: equilibrium pest density under continuous spraying (Proposition 53.3.2) against the extra mortality on the pest, with the enemy suffering 1.5 times this mortality (broad-spectrum) or none (selective): while the enemy persists the pest equilibrium is unaffected by the selective spray and rises under the broad-spectrum spray; only when the enemy is eliminated does spraying reduce the pest, along the enemy-free line (dotted). C: a secondary pest with the same parameters and its own enemy, subjected to sprays aimed at a key pest every 8 time units (dotted), which kill 20% of the secondary pest and 95% of its enemy: the secondary pest is held in repeated outbreaks above the EIL.](./plots/pest-resurgence.py)

### 53.3.3. Resistance, Transgenic Crops and Decision Support

Pesticides that kill most of a large, genetically variable population select for resistance. The mechanisms, the history, the population-genetic model of resistance evolution with untreated refuges and the **refuge strategy** for transgenic Bt crops are described in [7.17.40](/7.17.40#sec-40.6.2); the ecological point is that resistance and resurgence interact. Each application that fails because of resistance invites more frequent or heavier applications, which kill more enemies, cause more resurgence and select for still more resistance, the "pesticide treadmill" that IPM was designed to escape.

Transgenic crops change pest management in two directions. Bt crops, which express insecticidal toxins of *Bacillus thuringiensis*, reduce spraying against their target pests and thereby conserve natural enemies, which in Bt cotton in northern China increased and spilled over into neighboring crops, while mirid bugs, previously controlled incidentally by sprays against the bollworm, rose to key-pest status ([7.17.40](/7.17.40#sec-40.6.2)). Herbicide-tolerant crops have the opposite effect on farmland biodiversity: they allow the non-selective herbicide glyphosate to be used throughout the season, removing weeds whose seeds and associated insects feed farmland birds. Watkinson et al. (2000) modeled the effect of herbicide-tolerant sugar beet on skylarks (*Alauda arvensis*), which feed in winter on the seeds of fat hen (*Chenopodium album*). Since weed seeds are aggregated in a few weedy fields and skylarks concentrate there, the outcome depended less on how strongly the technology reduced weeds than on which farmers adopted it: if those with the weediest fields adopted it first, the birds' food supply collapsed; if those with already clean fields did, the effect was small. A socioeconomic parameter thus mattered more than an ecological one, a reminder that sustainability has ecological, economic and social dimensions.

**Integrated pest management** ([Definition 40.6.3](/7.17.40#def-40.6.3) of 7.17.40) acts only when thresholds are exceeded, combines physical, cultural, biological, genetic and chemical methods, and prefers those least damaging to the rest of the community; **biological control** is its preferred tool, with the agents chosen by the criteria of parasitoid–host theory (7.19.27). Because no two pest problems are the same, IPM depends on monitoring and on decision support systems that combine local data with models. For barley yellow dwarf, a virus disease of cereals transmitted by aphids, such a system takes the farmer through a sequence of decisions, whether to treat the seed, when to sow, whether and when to monitor aphids and whether to spray, using weather data, aphid flight records and the local history, and it can be used through a website or a smartphone application into which farmers also feed their observations (Walls et al. 2016). Natural enemies are also an ecosystem service with a calculable value: in eight counties of south-central Texas, Brazilian free-tailed bats (*Tadarida brasiliensis*), which emerge in millions each night and eat corn earworm moths (*Helicoverpa zea*), were estimated to save cotton growers 121 000 to 1 725 000 US dollars a year in crop losses and avoided sprays (Cleveland et al. 2006), and insectivorous bats in the United States as a whole about 23 billion dollars a year (Boyle et al. 2011), estimates that illustrate the scale while depending on many assumptions.

### 53.3.4. Bioaccumulation and Biomagnification

Some of the most serious unintended effects of pesticides arise because organisms retain them. Persistent, fat-soluble compounds such as DDT and its metabolites, other organochlorines and polychlorinated biphenyls (PCBs) are absorbed readily, stored in lipids and metabolized and excreted slowly.

**Definition 53.3.2 (Bioaccumulation and Biomagnification)** *Bioconcentration* is the uptake of a chemical by an organism directly from the surrounding water or air, to a concentration exceeding that of the medium; **bioaccumulation** is the net accumulation of a chemical in an organism from all sources, the medium and food; **biomagnification** is the increase of the concentration of a chemical in organisms with increasing trophic level, because consumers take it up from their food faster than they eliminate it.

The classic data come from a salt marsh on Long Island, New York, sprayed with DDT for mosquito control for twenty years (Woodwell et al. 1967): DDT residues rose from 0.00005 ppm in the water to 0.04 ppm in plankton, 0.2–2 ppm in fish and more than 20 ppm in fish-eating birds, a concentration factor of about 500 000 (Figure 7A). A compartment model (Definition 45.2.1) of each trophic level explains such factors.

**Proposition 53.3.3 (Biomagnification Factor)** Let a consumer of trophic level $i$ ingest food at rate $I$ per unit body mass, assimilate a fraction $\alpha$ of the chemical in its food, eliminate the chemical at rate constant $k_{\mathrm e}$, and grow at rate $g$ per unit mass, so that the concentration $C_i$ in its tissue changes as

$$
\frac{\mathrm{d}C_i}{\mathrm{d}t} = \alpha I C_{i-1} - (k_{\mathrm e} + g)C_i. \tag{53.15}
$$
(a) At steady state, the biomagnification factor is

$$
\mathrm{BMF} = \frac{C_i}{C_{i-1}} = \frac{\alpha I}{k_{\mathrm e} + g}, \tag{53.16}
$$
and the concentration approaches it with time constant $1/(k_{\mathrm e} + g)$, the residence time (Definition 45.2.2) of the chemical in the consumer. (b) If growth is a fraction $\varepsilon$ of ingestion, $g = \varepsilon I$ (the gross growth efficiency, related to the production efficiencies of 7.19.43), then $\mathrm{BMF} = \alpha/(\varepsilon + k_{\mathrm e}/I)$, which for a chemical that is not eliminated tends to $\alpha/\varepsilon$. (c) In a food chain with equal factors at each step, $C_n = C_1\,\mathrm{BMF}^{\,n-1}$.

**Proof** (a) Setting the derivative to zero gives Eq. (53.16); the solution of the linear equation (53.15) with constant $C_{i-1}$ approaches it exponentially at rate $k_{\mathrm e} + g$. Growth dilutes the chemical as elimination does, since the concentration falls when tissue is added. (b) Substitute $g = \varepsilon I$. (c) Iterate. $\square$

The mechanism is mass balance. A consumer converts only a small fraction $\varepsilon$ of the food it eats into its own tissue, typically 10% or less, and burns or excretes the rest; if it retains most of a persistent chemical, the chemical in all that food ends up in a small mass of tissue. With $\alpha = 0.8$ and $\varepsilon = 0.1$, the factor is about 7 per trophic level and $7^3 \approx 350$ over three steps (Figure 7B). The same logic predicts where biomagnification fails: chemicals that are metabolized or excreted quickly (most modern pesticides, many metals in inorganic form) have $k_{\mathrm e}/I$ large and a factor below 1, and they become less concentrated up the food chain. Biomagnification is therefore expected for compounds that are persistent (resistant to degradation), lipophilic (octanol–water partition coefficients $\log K_{\mathrm{ow}}$ of about 5–7) and poorly metabolized, the defining properties of the persistent organic pollutants regulated by the Stockholm Convention (in force since 2004). It is strongest in long-lived top predators, which have slow elimination and slow growth, and in long food chains, such as those of the sea and of large lakes; air-breathing predators (seabirds, marine mammals, people) cannot eliminate such compounds across gills and accumulate them most. Methylmercury is the important inorganic-derived case (7.19.54).

The time constants have practical consequences (Figure 7C). Top predators reach their steady concentrations years after contamination begins and remain contaminated for years after it ends, especially when the chemical persists in sediments or soil. DDE, the main metabolite of DDT, thins the eggshells of birds of prey by impairing calcium deposition in the shell gland, so that eggs break during incubation; populations of the peregrine falcon (*Falco peregrinus*), the osprey (*Pandion haliaetus*), the bald eagle (*Haliaeetus leucocephalus*) and the brown pelican (*Pelecanus occidentalis*) collapsed in the 1950s–1960s with little mortality of adults. Rachel Carson's *Silent Spring* (1962) brought the problem to public attention; DDT was banned for agricultural use in the United States in 1972 and in China in 1983, and the raptor populations recovered over the following decades, aided by captive breeding and reintroduction. Persistent pollutants remain in polar food webs far from their sources, carried by air and ocean currents, and climate change alters their routes: polar bears in eastern Greenland accumulated more organochlorines when sea-ice loss shifted their diet toward more contaminated seals (McKinney et al. 2013). Newer pesticides are less persistent but not harmless: neonicotinoids, which are water-soluble rather than lipophilic and do not biomagnify, nevertheless occur in surface waters worldwide at concentrations harmful to aquatic invertebrates (Morrissey et al. 2015).

![Biomagnification of persistent chemicals. A: DDT residues (DDT + DDD + DDE, ppm wet weight, whole organisms) in a Long Island estuary that had been sprayed for mosquito control: water, plankton, fish (blue) and birds (orange), data of Woodwell, Wurster and Isaacson (1967) as tabulated by Odum and Barrett (2005); logarithmic scale. B: steady-state concentrations along a food chain in the compartment model (Proposition 53.3.3) with gross growth efficiency 0.1, for a persistent lipophilic chemical (assimilation 0.8, slow elimination), a partly metabolized chemical and a rapidly excreted one; the last is diluted up the chain. C: the persistent chemical in a four-level chain whose elimination and growth rates decrease with body size up the chain: uptake from water starts in year 0 and is banned in year 15, after which the concentration in water declines with a half-life of 3 years; the top predator approaches its steady concentration slowly and remains contaminated for decades. Panels B and C are model calculations.](./plots/biomagnification.py)

## Summary

| Topic | Model or result | Ecological meaning |
|---|---|---|
| Maximum sustainable yield | $\max F(N)$; logistic: $rK/4$ at $K/2$; θ-logistic: Eq. (53.1) (Proposition 53.1.1) | Harvest the surplus of a population held below $K$; the optimal density depends on the form of density dependence |
| Fixed quota | $\dot x = x(1 - x) - h$: stable and unstable equilibria merge at the MSY (saddle-node, Proposition 53.1.2); slow decline $T \approx \pi/\sqrt{\varepsilon}$ (Proposition 53.1.3) | An MSY quota is fragile; an overestimated one leads to certain, initially invisible, collapse |
| Fixed effort | $x^* = 1 - e$, $Y = e(1 - e)$, 20% excess effort costs 4% of yield (Proposition 53.1.4); CPUE linear in effort (Proposition 53.1.5) | Feedback from stock to catch stabilizes; catch varies |
| Hyperstability, depensation | Catchability rising at low stock creates a fold (Proposition 53.1.6); Allee effects (Proposition 10.3.3) | Schooling fish and depensating stocks collapse abruptly and recover slowly (anchoveta, herring, cod) |
| Gordon–Schaefer | MEY effort $< E_{\mathrm{MSY}}$, stock $(K + N_\infty)/2$ (Proposition 53.2.1); open access at $2E_{\mathrm{MEY}}$, stable with damped boom–bust (Proposition 53.2.2) | Open access dissipates rent and overfishes when fishing is cheap; common-property institutions can avoid it |
| Discounting | Modified golden rule, Eq. (53.12) (Theorem 53.2.1); $N^* = 0$ if $\delta \ge r$ without stock effects | Slow-growing species are liquidated by pure profit maximization |
| Uncertainty | Quotas collapse under environmental variation; harvest control rules (Figure 4) | Precautionary approach: MSY as a limit, not a target |
| Pest status | Equilibrium relative to the EIL (Definition 53.3.1); optimal density $c/(kVD)$ (Proposition 53.3.1) | Eradication is rarely economic; potential pests are held down by enemies |
| Resurgence | Pest equilibrium $(m + h_E)/(ca)$, independent of mortality on the pest (Proposition 53.3.2) | Broad-spectrum sprays raise enemy-regulated pests and release secondary pests |
| Biomagnification | $\mathrm{BMF} = \alpha I/(k_{\mathrm e} + g) \to \alpha/\varepsilon$ (Proposition 53.3.3) | Persistent lipophilic chemicals concentrate in top predators (DDT and raptors) |

## Questions

1. A deer population grows logistically with $r = 0.4$ per year and $K = 2000$. (a) What are the MSY and the density at which it is taken? (b) A manager sets a fixed quota of 180 deer per year. Find the equilibria and their stability. (c) What happens if a severe winter reduces the herd to 500?

   **Answer** (a) $\mathrm{MSY} = rK/4 = 200$ deer per year at $N = 1000$. (b) $h = H/(rK) = 180/800 = 0.225$; $x_\pm = (1 \pm \sqrt{1 - 0.9})/2 = (1 \pm 0.316)/2$, so $N_+ \approx 1316$ (stable) and $N_- \approx 684$ (unstable threshold). (c) At $N = 500 < N_-$ the surplus, $0.4 \cdot 500 \cdot 0.75 = 150$, is below the quota; the herd declines further and is exterminated unless the quota is reduced. Under a fixed harvest rate giving the same yield at equilibrium ($qE = 180/1316 \approx 0.137$), the herd at 500 would grow (surplus 150 > harvest 68) and recover.

2. Show that in the Schaefer model the sustainable yield as a function of the equilibrium stock is the surplus production curve itself, and explain why a manager who knows only the catch and effort records of a developing fishery tends to overestimate the MSY.

   **Answer** At equilibrium the catch equals the surplus, $Y = F(N^*)$, so plotting yield against equilibrium stock traces $F$. In a developing fishery effort increases each year, and the stock lags behind its equilibrium for the current effort: it is still above it, so the catch per unit effort and the catch exceed the sustainable values. Fitting Eq. (53.6) to such non-equilibrium data attributes high catches to high efforts and places the peak of the yield–effort parabola too far to the right and too high. Dynamic fitting of the time series, or contrast in effort (reductions as well as increases), avoids this.

3. In the Gordon–Schaefer model with $r = 0.5$ per year, $K = 10^6$ tonnes, $q = 10^{-4}$ per boat-day, $p = 1000$ yuan per tonne and $c = 30\,000$ yuan per boat-day, compute $N_\infty$, $E_{\mathrm{MEY}}$, $E_{\mathrm{MSY}}$ and $E_\infty$. Is the open-access fishery biologically overexploited? What price would make it so if it is not?

   **Answer** $N_\infty = c/(pq) = 30\,000/(1000 \times 10^{-4}) = 3 \times 10^5$ tonnes $= 0.3K$. $E_{\mathrm{MSY}} = r/(2q) = 2500$ boat-days; $E_{\mathrm{MEY}} = 2500(1 - 0.3) = 1750$; $E_\infty = 2E_{\mathrm{MEY}} = 3500$. Since $N_\infty = 0.3K < K/2$, open access overexploits the stock biologically, and its yield, $qE_\infty N_\infty = 0.0001 \times 3500 \times 3 \times 10^5 = 105\,000$ tonnes, is below the MSY of $125\,000$ tonnes. Overexploitation occurs whenever $c/(pq) < K/2$, i.e. for any price above $c/(qK/2) = 600$ yuan per tonne; at prices below 600 yuan, open access stops short of the MSY effort.

4. Use the modified golden rule to explain why a sole owner might still exterminate a stock, and why a rising cost of harvesting at low density can prevent it.

   **Answer** Without stock-dependent costs, the optimal stock solves $F'(N^*) = \delta$. For logistic growth $F'(N) \le r$, so if $\delta \ge r$ no positive stock earns the market rate of return, and the owner liquidates it: whales and long-lived fish with $r$ of a few percent per year face discount rates of 5–10%. If the unit cost $c(N) = c/(qN)$ rises as fish become scarce, the second term of Eq. (53.12) is positive and grows without bound as $N$ approaches $N_\infty$, so a positive solution $N^* > N_\infty$ always exists: the last fish are too expensive to catch. This protects the stock only if $N_\infty$ is not too small; with cheap, efficient technology or high prices (rare species fetch high prices, the "anthropogenic Allee effect"), it may not.

5. Using Proposition 53.3.2, explain why spraying a selective insecticide against a pest that is regulated by a specialist enemy may have no lasting effect on the pest, while a broad-spectrum insecticide makes it worse. Under what conditions does spraying help?

   **Answer** While the enemy persists, the pest equilibrium is $N^* = (m + h_E)/(ca)$: the density at which enemies just replace themselves. Extra mortality on the pest ($h_N$) reduces the enemy, not the pest, because fewer enemies are then supported; extra mortality on the enemy ($h_E$) raises the density of pests needed to sustain them. Spraying lowers the pest only if it is strong enough to eliminate the enemy ($N^\dagger \ge K(1 - h_N/r)$), after which the pest is controlled by the spray alone and must be sprayed indefinitely; or if the pest is not enemy-regulated in the first place. The lessons are to use selective products, to spray only above thresholds, and to conserve enemies.

6. A persistent chemical is assimilated from food with efficiency $\alpha = 0.9$ and hardly eliminated. Phytoplankton bioconcentrate it to $10^4$ times the concentration in water. Estimate the concentration factor in a fish-eating bird at trophic level 4, taking a gross growth efficiency of 0.1 for zooplankton and small fish and of 0.02 for the bird (an endotherm). Why do endotherms at the top of food chains suffer most?

   **Answer** By Proposition 53.3.3(b), $\mathrm{BMF} \approx \alpha/\varepsilon$: $0.9/0.1 = 9$ for zooplankton and for small fish, and $0.9/0.02 = 45$ for the bird. The concentration factor relative to water is $10^4 \times 9 \times 9 \times 45 \approx 3.6 \times 10^7$. Endotherms burn most of their food in respiration, so their growth efficiency is low and their BMF high; air-breathing animals also cannot lose lipophilic compounds across gills, and long-lived top predators accumulate them over decades. The estimate exceeds observed factors (about $10^5$–$10^6$ in Figure 7A) because real elimination, metabolism and growth are not zero and food webs mix trophic levels.

7. (Open question) Discuss whether the maximum sustainable yield should still be used as a target in fisheries management, considering the models of this chapter and the facts that stocks fluctuate, that species interact and that fisheries have social and economic objectives.

   **Answer** Points for discussion: the MSY is a useful benchmark because it summarizes productivity and because yield near the MSY is achievable with stable effort (Proposition 53.1.4); but as a fixed quota it is fragile (Propositions 53.1.2, 53.1.3), it is estimated with large error, it changes with environment, it ignores age structure and interactions (harvesting all species at their single-species MSYs is impossible when they eat one another), and economically the MEY is lower and safer. Current practice treats $F_{\mathrm{MSY}}$ as a limit and uses precautionary harvest control rules tested by simulation; ecosystem-based management adds bycatch, habitat and food-web objectives. A good answer distinguishes biological limits from social choices, which models can inform but not make.
