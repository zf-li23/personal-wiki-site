---
title: 趋化性与聚集：盘基网柄菌
description: 社会性变形虫盘基网柄菌通过聚集而成为多细胞生物。生活史；前孢子细胞与前柄细胞的比例调节、其异速关系及其反应扩散解释；cAMP 信号与中继、Cohen–Robertson 脉冲模型、临界密度与波速、连续极限、靶波与螺旋波；Keller–Segel 模型、其推导、无限波长处的线性不稳定性与领地大小问题；趋化性增强的 Turing 系统；非线性理论（振幅方程、椭圆函数稳态、亚临界分岔、孤立聚集体与 sech² 团簇）；与维数有关的塌缩及二维中的临界质量；以及动物胚胎中的趋化性。
source_hash: 0a1b5f1b2e91
---

前面几章的胚胎都由一个细胞分裂而来。盘基网柄菌（*Dictyostelium discoideum*）走的是相反的道路：多达约 $10^5$ 个自由生活的变形虫在饥饿时聚集成一个生物体，它能运动，按固定比例分化成两种细胞类型，并构建出子实体。它属于变形虫门（Amoebozoa），是一种社会性变形虫，而不是真菌；尽管它传统上被称为"细胞黏菌"，并且产孢子的子实体曾使它被归入真菌，但它的分类与生态属于 [7.11](/7.11)。对发育生物学而言，它提供了很少有胚胎能提供的东西：细胞可以计数的图式、很早就被鉴定出来的信号（**环腺苷酸**），以及由**趋化性**（[7.3.15](/7.3.15)）驱动的聚集；Keller–Segel 模型使这种聚集成为数学生物学中研究得最多的方程之一。本章按生活史展开：比例调节（第 13.2 节）应用 [7.5.12](/7.5.12) 的反应扩散思想；中继波（13.3）是一种可兴奋介质；Keller–Segel 模型（13.4–13.7）把聚集描述为一种不稳定性；第 13.8 节转向动物胚胎中的趋化性。

## 13.1. 生活史

孢子在潮湿的土壤中萌发成变形虫，以吞噬方式取食细菌并分裂。食物耗尽时，细胞在数小时内改变其程序：开始发出并中继**环腺苷酸**（cAMP）的脉冲，朝它的源移动，并沿着邻近细胞走过的路径成流汇入聚集中心。聚集体形成土墩，长出尖端，并伸长为几毫米长的蛞蝓体，它在自己分泌的黏液鞘上朝向光与热迁移。蛞蝓体前部约五分之一由前柄细胞组成，其余是前孢子细胞。在成熟（culmination）阶段，前柄细胞像倒转的喷泉那样向下穿过细胞团，分泌纤维素管，成为柄，即由死亡的、有液泡的细胞构成的柱，把前孢子细胞举到顶端的孢子堆中，后者在那里变成孢子。它也有通过巨大细胞（大囊）实现的有性循环。

![盘基网柄菌（*Dictyostelium discoideum*）的无性生活史。孢子萌发成变形虫，取食并分裂；饥饿触发 cAMP 信号并成流地聚集；土墩长出尖端，形成迁移的蛞蝓体，前柄细胞（红）在前、前孢子细胞（蓝）在后，最后成熟为子实体，其中前柄细胞形成柄，前孢子细胞形成孢子](./plots/life-cycle.py)

聚集使柄成为一种合作行为：柄细胞死亡，以便其他细胞作为孢子散布。这引出了社会进化的问题（偏向于变成孢子的作弊突变体、亲缘识别），它们属于 [7.10](/7.10)。这也使该生物成为细胞类型比例调节的一个干净的例子，因为不同谱系的细胞在起初是混合的：图式不可能是在卵中预先安排好的。

## 13.2. 比例调节

前孢子组织与前柄组织之比是受调节的：在蛞蝓体开始迁移时与成熟时大致相同，把蛞蝓体切开，每一片段都会重新调整自己的比例。这种调节并不精确，而是异速的，

$$
\frac{\text{prespore volume}}{\text{prestalk volume}}=KV^\lambda,\qquad\lambda\approx0.2,
$$
所以较小的蛞蝓体有相对更多的前柄组织。前孢子细胞转变成前柄细胞很快，反过来较慢；迁移时间越长，后部的前孢子分数越高；光、葡萄糖与温度使比例偏向孢子，锂离子使之偏向柄。蛞蝓体还逐个细胞地极化：每个细胞的收缩**液泡**位于细胞核之后。

与最初为这些观察建立模型的时候相比，现在对细胞如何选择类型的理解要好得多。选择受到每个细胞历史的影响：饥饿开始时处于**细胞周期**特定时相的细胞，或曾在葡萄糖上生长的细胞，倾向于成为前柄或前孢子细胞。前柄细胞与前孢子细胞起初以椒盐式分散在土墩中，随后分选，前柄细胞凭借对 cAMP 更强的趋化性和不同的黏附（**差异黏附假说**，[7.5.7](/7.5.7)）移向尖端。比例由可扩散的信号调节：氯化的聚酮化合物 DIF-1 主要由前孢子细胞产生，诱导前柄细胞的一个亚型并抑制前孢子分化，前柄细胞则降解它，这是一种负反馈，在任一部分被切除之后恢复原来的比例。所以，对随机分化的细胞进行分选是主要机制；而下面的模型所假设的蛞蝓体中的反应扩散**预图式**则不是。

尽管如此，反应扩散模型仍然抓住了定量的规律，并且用的是 [7.5.12](/7.5.12) 的开关点数学。假设 (i) 激活物有一个从蛞蝓体前端递减的弱源密度，(ii) 被激活的组织成为前柄，未被激活的成为前孢子，(iii) 二者之间厚度为常数 $d$ 的过渡层在表型上是前柄。设被激活的区域是蛞蝓体中除过渡层之外的固定分数 $\alpha$（开关点处的相对调节，命题 12.5.1），并设过渡层的体积是蛞蝓体体积 $V$ 的分数 $1/(\beta V^{1/3})$（其截面按 $V^{2/3}$ 变化）。则

$$
\frac{\text{stalk}}{\text{spore}}=\frac{\alpha(1-v_t)+v_t}{(1-\alpha)(1-v_t)}=\frac\alpha{1-\alpha}\Big(1+\frac1\alpha\,\frac1{\beta V^{1/3}-1}\Big),\qquad v_t=\frac1{\beta V^{1/3}},
$$
这个比值在小蛞蝓体中较大，在大蛞蝓体中趋近 $\alpha/(1-\alpha)$。在一定的体积范围内，曲线接近指数约为 $0.2$ 的幂律。

在这个模型中，再生由抑制物的扩散控制。在 $x=\ell$ 处切去长度为 $L$ 的蛞蝓体的前端。旧的抑制物分布 $h_0$ 在新的末端不再满足无通量条件；缺失的通量相当于从 $t=0$ 起开启的汇 $\nu h_0'(\ell)\delta(x-\ell)$，变化量 $\Delta h$ 服从扩散方程，$\Delta h'(\ell)=-h_0'(\ell)$。在 Laplace 域中（[2.5.6](/2.5.6)），$\nu\Delta\tilde h''=\Omega\Delta\tilde h$，$\Delta\tilde h'(\ell)=-h_0'(\ell)/\Omega$，所以

$$
\Delta\tilde h(x,\Omega)=-\sqrt\nu\,h_0'(\ell)\,\frac{\mathrm{e}^{-(\Omega/\nu)^{1/2}(\ell-x)}}{\Omega^{3/2}},\qquad
\Delta h(x,t)=-\sqrt\nu\,h_0'(\ell)\Big[2\sqrt{\frac t\pi}\,\mathrm{e}^{-z^2}-\frac{\ell-x}{\sqrt\nu}\operatorname{erfc}z\Big],
$$
其中 $z=(\ell-x)/(2\sqrt{\nu t})$。当 $(\ell-x)^2\gg\nu t$ 时，erfc 的渐近展开给出

$$
\Delta h(x,t)\approx-\frac4{\sqrt\pi}\,h_0'(\ell)\,\frac{(\nu t)^{3/2}}{(\ell-x)^2}\,\mathrm{e}^{-(\ell-x)^2/4\nu t}:
$$
扰动经过 $(\ell-x_s)^2/\nu$ 量级的时间到达旧的开关点 $x_s$，这就是典型的扩散依赖关系。在较大的片段中，调节按距离的平方变慢，这可以通过测定不同大小的片段中前柄标记重新表达的时间来检验。

![A：蛞蝓体反应扩散模型（alpha = 0.15）中前孢子与前柄之比对体积的关系，与指数为 0.2 的幂律（虚线）比较；在大蛞蝓体中该比值饱和于 (1 - alpha) / alpha。B：截断之后，距切口 1、2、3 处的抑制物变化（nu = 1 的单位，已归一化）；达到后期值的 1 % 所需的时间（圆点）随距离的平方增长](./plots/proportion.py)

## 13.3. cAMP 信号与中继

趋化物最初称为 acrasin，1967 年被鉴定为 3′,5′-环腺苷酸。饥饿的细胞表达 **G 蛋白偶联受体** cAR1 与**腺苷酸环化酶** ACA；cAMP 的结合通过 G 蛋白激活环化酶，细胞合成并分泌 cAMP，数分钟后它适应并进入不应期。胞外的**环核苷酸磷酸二酯酶**（PdsA）由一种分泌的抑制剂调节，破坏该信号。聚集早期，靠近中心的细胞大约每 6 min 发放一次；周期后来缩短到 2–3 min。

**定义 13.3.1（cAMP 中继）** **cAMP 中继**是*盘基网柄菌*细胞对胞外 cAMP 升高超过阈值的响应：合成并分泌一个 cAMP 脉冲，随后是适应与不应期，使信号被放大并以波的形式在细胞之间传播。

每个细胞在每个波的上升相向源移动，每个脉冲约 $20\,\mathrm{\mu m}$，在下降相即使梯度此时指向外侧，也不会沿着趋化物退回去：这就是"波后问题"，由极性机制的适应所解决（[7.3.15](/7.3.15)）。

**公式 13.3.1（Cohen–Robertson 中继）** 设细胞的密度为 $a$（单位面积），平均间距为 $R$，$a^{-1}=\pi R^2/4$，发放的细胞释放强度为 $s$ 的瞬时脉冲，脉冲在平面内以系数 $\nu$ 扩散。距离为 $R$ 的邻居看到

$$
\rho(R,t)=\frac s{4\pi\nu t}\,\mathrm{e}^{-R^2/4\nu t}=\frac{sa}4\,g(\tau),\qquad g(\tau)=\frac{\mathrm{e}^{-1/\tau}}\tau,\quad\tau=\frac{4\nu t}{R^2}.
$$
由于 $g\le g(1)=1/\mathrm{e}$，发放阈值为 $\rho_c$ 的邻居只有在

$$
a>a_c=\frac{4\mathrm{e}\rho_c}s
$$
时才能被触发；高于此密度时，它在 $T_p=\frac{R^2}{4\nu}\tau_p$ 加上中继延迟 $T_d$ 之后发放，其中 $\tau_p$ 是 $g(\tau_p)=4\rho_c/(sa)$ 的较小根，波的传播速度为

$$
v(a)=\frac R{T_p+T_d}=\frac{(4/\pi a)^{1/2}}{\tau_p/(\pi\nu a)+T_d}.
$$

**证明** 二维热核为 $(4\pi\nu t)^{-1}\mathrm{e}^{-r^2/4\nu t}$（[2.5.7](/2.5.7)）；代入 $4\pi\nu t=4\tau/a$ 即得 $\rho$。$g'(\tau)=\mathrm{e}^{-1/\tau}(1-\tau)/\tau^3$ 在 $\tau=1$ 处为零。$\square$

存在一个临界密度，低于它时中继失败，并且速度依赖于密度。取估计值 $T=300\,\mathrm{s}$（周期）、$T_d=15\,\mathrm{s}$、每个脉冲的运动持续时间 $T_c=100\,\mathrm{s}$，cAMP 的 $\nu\approx400\,\mathrm{\mu m^2\,s^{-1}}$，则在间距 $R\approx30$–$60\,\mathrm{\mu m}$ 上的扩散只需不到一秒：速度由中继延迟决定，$v\approx R/T_d$，量级为 $100$–$200\,\mathrm{\mu m\,min^{-1}}$，与实测的每分钟几百微米同一量级。

![Cohen–Robertson 中继。A：最近的邻居所见的 cAMP 信号对无量纲时间 tau 的关系；曲线越过阈值处邻居发放，这只有在高于临界密度时才可能（曲线的最大值为 1/e），密度越高发放越早（a / a_c = 1.2、2 与 5）。B：中继延迟为 15 s 时波速对密度的关系：延迟起主导作用，速度遵循 R / T_d](./plots/relay-waves.py)

该模型还给出一维聚集的连续描述。设第 $n$ 个波在位置 $x_n(t)$ 处经过，速度 $\mathrm{d}x_n/\mathrm{d}t=v(a_n)$，每个波使每个细胞向中心 $x=0$ 移动距离 $\Delta(a)$，早期它是常数，在密堆积时为零。若运动时间比周期短（$T_c\ll T$），则一个波把密度 $a_{n-1}$ 映为 $a_n$，细胞数守恒（波过之后 $[x,x+\mathrm{d}x]$ 中的细胞，在波过之前位于 $[x+\Delta,\,x+\mathrm{d}x+\Delta(a)+\Delta'a_x\mathrm{d}x]$）给出，对小的 $\Delta$ 及 $a(x,nT)=a_n(x)$，

$$
a_t+\frac{\partial Q(a)}{\partial x}=0,\qquad Q(a)=-\frac{a\,\Delta(a)}T .
$$
这是运动学波方程：密度扰动沿特征线以速度 $Q'(a)$ 运动，向中心压缩，并形成激波；由于没有随机运动，细胞在 $x=0$ 处聚集成权重不断增长的 delta 函数。脉冲波本身沿 $\dot x=v(a)\propto a^{-1/2}$（对 $T_p\ll T_d$）穿过这个变化的密度：组织波产生趋化图式，图式又改变波。

聚集细胞的场显示出围绕周期性发放中心的同心靶波，更常见的是旋转的螺旋波。二者对于可兴奋介质都是普遍的：超阈值的刺激触发一个脉冲，随后是不应期。中继现在用受体脱敏模型（Martiel 与 Goldbeter，1987）和粗粒化的可兴奋动力学建模；当密度越过阈值时出现集体振荡，这是一种动力学群体感应（Gregor 等，2010）。螺旋波不需要特殊的起搏细胞：任何断裂的波前都会卷曲成螺旋。

![一般可兴奋介质（Barkley 模型）中的可兴奋波。左：周期性受刺激的中心发出同心的靶波；每个波前之后的不应区阻止反向传播。右：断裂的波前卷曲成自维持的螺旋波](./plots/spiral-waves.py)

## 13.4. Keller–Segel 模型

Keller 与 Segel（1970）把聚集的开始描述为均匀细胞场的不稳定性，把脉冲平滑掉。设 $a(\boldsymbol{r},t)$ 为变形虫的密度，$\rho$ 为引诱物，$\eta$ 为降解酶，$c$ 为酶–引诱物复合物，$\rho+\eta\rightleftharpoons c\to\eta+\text{product}$（速率常数 $k_1$、$k_{-1}$、$k_2$）。若产生与细胞密度成正比，

$$
\rho_t=-k_1\rho\eta+k_{-1}c+af(\rho)+\nu_0\Delta\rho,\quad \eta_t=-k_1\rho\eta+(k_{-1}+k_2)c+aF(\rho,\eta)+\delta\Delta\eta,\quad c_t=k_1\rho\eta-(k_{-1}+k_2)c+\lambda_c\Delta c .
$$
若酶促步骤很快，总酶量 $\eta+c=\eta_0$ 固定，则 Michaelis–Menten 消去（[7.5.12](/7.5.12#sec-12.2.4)）给出 $\eta=\eta_0/(1+K\rho)$，$K=k_1/(k_{-1}+k_2)$，引诱物满足

$$
\rho_t=af(\rho)-g(\rho)+\nu_0\Delta\rho,\qquad g(\rho)=\frac{\eta_0k_2K\rho}{1+K\rho}.
$$
细胞数守恒，$a_t+\nabla\cdot\boldsymbol{J}=0$，其通量包括沿 $\rho$ 梯度上升的趋化部分，以及沿 $a$ 梯度下降的随机运动部分。

**定义 13.4.1（Keller–Segel 模型）** **Keller–Segel 模型**是系统

$$
a_t=\nabla\cdot\big(\mu(a,\rho)\nabla a-\kappa(a,\rho)\nabla\rho\big),\qquad \rho_t=af(\rho)-g(\rho)+\nu\Delta\rho,
\tag{13.1}
$$
其中 $a$ 为细胞密度，随机运动系数为 $\mu$，趋化敏感度为 $\kappa$，引诱物 $\rho$ 由细胞按每个细胞速率 $f$ 产生，并以速率 $g$ 被清除。

在满足 $a_0f(\rho_0)=g(\rho_0)$ 的均匀态 $(a_0,\rho_0)$ 附近线性化。设 $\alpha_0=a_0f'(\rho_0)-g'(\rho_0)$，$f_0=f(\rho_0)$，$\mu_0$、$\kappa_0$ 为均匀态处的值，

$$
\rho'_t=\alpha_0\rho'+f_0a'+\nu_0\Delta\rho',\qquad a'_t=-\kappa_0\Delta\rho'+\mu_0\Delta a' .
$$
对扰动 $\mathrm{e}^{\sigma t+\mathrm{i}\boldsymbol{k}\cdot\boldsymbol{r}}$，$\sigma^2+A\sigma+B=0$，其中

$$
A=(\mu_0+\nu_0)k^2-\alpha_0,\qquad B=\mu_0\nu_0k^4-(\mu_0\alpha_0+\kappa_0f_0)k^2 .
$$

**定理 13.4.1** (a) 增长率是实数：$A^2-4B=\big((\mu_0-\nu_0)k^2+\alpha_0\big)^2+4\kappa_0f_0k^2\ge0$，所以在该模型中趋化聚集不发生振荡。(b) 在 $k=0$ 处，$\sigma\in\{0,\alpha_0\}$，要使细胞不动时引诱物是稳定的，需要 $\alpha_0<0$。(c) 模式 $k$ 增长，当且仅当 $B<0$，即 $\mu_0\alpha_0+\kappa_0f_0>\mu_0\nu_0k^2$；某个模式增长，当且仅当

$$
\Delta\equiv\mu_0\alpha_0+\kappa_0f_0>0\iff\mu_0a_0f'(\rho_0)+\kappa_0f_0>\mu_0g'(\rho_0).
$$
(d) 在起始点附近（$0<\Delta\ll1$），$\sigma\approx(\Delta k^2-\mu_0\nu_0k^4)/\lvert\alpha_0\rvert$，在 $k^2_{\max}=\Delta/(2\mu_0\nu_0)$ 处最大，$\sigma_{\max}=\Delta^2/(4\lvert\alpha_0\rvert\mu_0\nu_0)$。

**证明** (a) 展开：$A^2-4B=(\mu_0+\nu_0)^2k^4-2\alpha_0(\mu_0+\nu_0)k^2+\alpha_0^2-4\mu_0\nu_0k^4+4(\mu_0\alpha_0+\kappa_0f_0)k^2$，重新组合即得所述形式。(b)、(c) 由于 $\alpha_0<0$，$A>0$，两根之积为 $B$；恰当 $B<0$ 时有一个根为正。(d) 对小的 $\sigma$，$\sigma\approx-B/A\approx-B/\lvert\alpha_0\rvert$，其中 $k^2=O(\Delta)$，所以 $\sigma=O(\Delta^2)$；对 $k^2$ 取最大。$\square$

该条件说明，当引诱物的产生或趋化响应相对于引诱物的破坏很强时，均匀态不稳定：小团簇产生更多引诱物，吸引更多细胞。引人注目的是 (d)：边缘模式是 $k=0$，即无限波长。当 $\Delta$ 越过零点时，最长的波首先被激发，偏好的波长 $2\pi/k_{\max}\propto\Delta^{-1/2}$ 取决于系统超过阈值多远。然而，真实的聚集场会分裂成大小确定的领地。Segel 与 Stoeckley 讨论了一些修正：把领地大小等同于最快的波长，使它依赖于初始的 $\Delta$；信号传导的阈值使问题成为非线性的，并预测一个最大间距；扩大化学系统可以给出有限的波长，但此时长度尺度是化学的（一种扩散不稳定性），细胞只是跟随它。"真正的"趋化不稳定性往往具有零临界波数。真实生物体中的解决办法是，领地由第 13.3 节的中继波所决定，而平滑的模型把它平均掉了。

![A：Delta = -0.2、0.1、0.4 与 1 时 Keller–Segel 模型的增长率：不稳定带总是从 k = 0 开始。B：仅凭化学在每个波数上都稳定（虚线，在标度之下）的趋化性增强 Turing 系统，当同时产生两种化学物质的细胞沿第一种的梯度向上运动时，在有限波数带内变得不稳定；第 13.5 节的例子（kappa1 = 1）刚越过阈值，kappa1 = 1.5 则远远越过](./plots/ks-dispersion.py)

## 13.5. 趋化性增强的 Turing 系统

无限的临界波长是由定向运动形成图式的典型特征吗？考虑由细胞产生并相互反应的 $n$ 种化学物质，线性化后

$$
\rho_{i,t}=f_ia+\sum_j\alpha_{ij}\rho_j+\nu_i\Delta\rho_i,\qquad a_t=-\sum_i\kappa_i\Delta\rho_i+\mu\Delta a,
$$
其中某些 $\kappa_i$ 可能为零。对模式 $\mathrm{e}^{\mathrm{i}\boldsymbol{k}\cdot\boldsymbol{r}+\sigma t}$，第二个方程给出 $a=k^2\kappa^{\mathsf T}\rho/(\sigma+\mu k^2)$，消去 $a$ 得

$$
\big[\sigma^2I+\sigma(P+k^2Q)+\mu k^2(k^2S-R)\big]\hat\rho=0,\qquad P=-\alpha,\ Q=\operatorname{diag}(\mu+\nu_i),\ S=\operatorname{diag}(\nu_i),\ R=\alpha+\frac{f\kappa^{\mathsf T}}\mu .
$$
在非振荡不稳定性的起始点（$\sigma\to0$），问题化为 $\det(k^2S-R)=0$：这是以增广矩阵 $R$ 代替 $\alpha$ 的 Turing 问题（[7.5.12](/7.5.12)，定理 12.3.1）。若 $R$ 能够产生具有有限化学波长的扩散不稳定性，而 $\alpha$ 不能，则尽管机制涉及趋化性，临界波长是有限的。只有一种化学物质时这不可能（$1\times1$ 的"Turing"问题的临界模式在 $k=0$），但有两种化学物质时就可能发生。

**例 13.5.1** 取 $\nu_1=1$，$\nu_2=4$，$f_1/\mu=f_2/\mu=1$，$\kappa_1=1$，$\kappa_2=0$，$\alpha=\begin{bmatrix}2&-3\\5&-5\end{bmatrix}$。则 $\operatorname{tr}\alpha=-3$，$\det\alpha=5$，但 $\nu_1\alpha_{22}+\nu_2\alpha_{11}=3<2\sqrt{\nu_1\nu_2\det\alpha}=2\sqrt{20}=8.94$：仅凭化学物质没有 Turing 不稳定性。有趋化性时，$R=\begin{bmatrix}3&-3\\6&-5\end{bmatrix}$，$\det R=3$，$\nu_1R_{22}+\nu_2R_{11}=7>2\sqrt{12}=6.93$：有限的波数带是不稳定的，尽管只是刚刚如此。

所以，趋化性可以实现化学本身已经具有（在长波处的失稳倾向）却无法单独表现出来的扩散不稳定性的能力。在另一个极端，若 $\alpha$ 是对称负定的（"绝对稳定"），具有非简并的主特征向量 $\boldsymbol{v}$，且 $f$、$\kappa$ 都平行于 $\boldsymbol{v}$，其长度之积的选取使 $R$ 的最大特征值为零，则对所有 $k\ne0$ 有 $\rho^{\mathsf T}B\rho>0$，不稳定性在无限波长处开始。在真实的组织中，区域的大小与形状决定适用哪一种极限。

## 13.6. 非线性理论

### 13.6.1. 振幅方程

在起始点附近，$\sigma\sim k^4\sim\Delta^2$。写 $\Delta=\mu_0\alpha_0+\kappa_0f_0=\varepsilon r$，在慢变量 $\tilde{\boldsymbol{x}}=\varepsilon^{1/2}\boldsymbol{x}$、$\tilde t=\varepsilon^2t$ 中展开 $a=a_0+\varepsilon a_1+\varepsilon^2a_2+\cdots$，$\rho=\rho_0+\varepsilon\rho_1+\cdots$。在 $\varepsilon$ 阶，引诱物方程给出 $f_0a_1+\alpha_0\rho_1=0$，且由于 $f_0/\lvert\alpha_0\rvert=\mu_0/\kappa_0+O(\varepsilon)$，$\rho_1=\mu_0a_1/\kappa_0$：引诱物跟随细胞。把 $\kappa_0\tilde\nabla^2$ 乘以引诱物方程，加到 $\alpha_0$ 乘以细胞方程上，可消去首项，在下一阶得

$$
-\alpha_0\frac{\partial a_1}{\partial\tilde t}+r\tilde\nabla^2a_1+\nu\mu_0\tilde\nabla^4a_1+q\tilde\nabla^2a_1^2=0,
$$
其中 $q$ 汇集二次项（来自 $f'(\rho_0)$、$g''(\rho_0)$ 以及 $\mu$ 与 $\kappa$ 的导数）。由于 $\alpha_0<0$，$\nu\mu_0>0$，作重标度 $\tilde\nabla^2=\nabla^{*2}/(\nu\mu_0)$，$\partial_{\tilde t}=\partial_{t^*}/(-\alpha_0\nu\mu_0)$，$a_1=a^*/q$，得（略去星号）

$$
a_t+r\Delta a+\Delta^2a+\Delta(a^2)=0 .
\tag{13.2}
$$
其线性部分给出 $\sigma=rk^2-k^4$：当 $r>0$ 时为长波不稳定性，如定理 13.4.1。同样的方程也局部地出现在一般的趋化性增强 Turing 系统中。

### 13.6.2. 周期稳态与亚临界分岔

在一维中，寻求 (13.2) 周期为 1 的稳态解，且在 $x=0,1$ 处 $a_x=a_{xxx}=0$。积分两次得 $a_{xx}+ra+a^2=C$，乘以 $a_x$ 再积分，

$$
a_x^2=-\tfrac23a^3-ra^2+2Ca+D .
$$
作平移 $a=A+h$，把三次多项式的中间根放在原点，得 $A_x^2=\frac23(A+A_1)A(A_0-A)$，其中 $A_0,A_1>0$，$0\le A\le A_0$。细胞数守恒要求 $a$ 的平均值为零，所以 $h=-\bar A$，比较根之和得 $r=2\bar A+\frac23(A_1-A_0)$。

**命题 13.6.1** 周期稳态为

$$
A=A_0\frac{(1-m)\,\operatorname{sn}^2(\xi,m)}{1-m\operatorname{sn}^2(\xi,m)},\qquad m=\frac{A_0}{A_0+A_1},\qquad\xi=x\sqrt{\frac{A_0}{6m}},
$$
其中 $\operatorname{sn}$ 是参数为 $m=k^2$ 的 Jacobi 椭圆函数，积分 $\pm\sqrt{3/2}\,x=\int_0^A[s(A_0-s)(s+A_1)]^{-1/2}\mathrm{d}s$ 已被反演。周期为 1 要求 $A_0=24K^2m$，此时

$$
r=48K\Big(E+\frac m3K-\frac23K\Big),
$$
其中 $K(m)$、$E(m)$ 是第一类与第二类完全椭圆积分。

当 $m\to0$ 时，$K,E\to\pi/2$，$r\to48\cdot\frac\pi2\cdot\frac\pi6=4\pi^2$，这是周期为 1 的模式的线性阈值（$k=2\pi$ 处 $rk^2=k^4$）。随着 $m$ 增大，振幅 $A_0$ 增大而 $r$ 减小：稳定图式在 $r<4\pi^2$ 时存在，此时均匀态在线性意义下是稳定的。这个**分岔**是亚临界的，部分原因是它从无限波长处分出。这些图式预期是不稳定的，它们标出了一个阈值：当均匀态刚刚稳定时，有限振幅的扰动仍然可以触发聚集。该理论没有说系统此后会去往何处，只说它最终远离均匀状态。

### 13.6.3. 孤立聚集体与塌缩

为了沿该分支继续追踪，取最简单的非线性系统（常系数，$\alpha$ 归一化为 $-1$）：

$$
fa-\rho+\nu\rho_{xx}=0,\qquad\mu a_{xx}-\kappa(a\rho_x)_x=0 .
$$
对边界无细胞通量的定态图式，通量处处为零：$a_x=\lambda a\rho_x$，$\lambda=\kappa/\mu$，所以 $a=\frac{A\lambda}{2f}\mathrm{e}^{\lambda\rho}$。代入并积分一次，

$$
\nu\rho_x^2+V(\rho)=E,\qquad V(\rho)=A\mathrm{e}^{\lambda\rho}-\rho^2 .
$$
在亚临界分岔附近，图式在 $V$ 的浅势阱中振荡。高度非线性的情形是孤立的凸起，即离开背景 $\rho_1$ 又回到背景的同宿轨道：$E-V$ 在 $\rho_1$ 处有二重根，要求 $E=-\rho_1^2+A\mathrm{e}^{\lambda\rho_1}$ 与 $2\rho_1=\lambda A\mathrm{e}^{\lambda\rho_1}$，因此 $A=\frac{2\rho_1}\lambda\mathrm{e}^{-\lambda\rho_1}$，$E=-\rho_1^2+\frac{2\rho_1}\lambda$，远处 $a=a_1=\rho_1/f$。取 $\rho_1=1$，峰值 $\rho_2$ 满足

$$
\rho_2^2-\frac2\lambda\mathrm{e}^{\lambda(\rho_2-1)}=1-\frac2\lambda .
$$
在 $\lambda=1$ 时唯一的解是 $\rho_2=1$（没有凸起）；$\lambda$ 减小时 $\rho_2$ 增大，当 $\lambda\to0$ 时，$\mathrm{e}^{\lambda\rho_2}\approx\lambda\rho_2^2/2$ 给出 $\rho_2\sim\lvert\ln\lambda\rvert/\lambda$ 以及峰值密度

$$
a_2=\frac1f\mathrm{e}^{\lambda(\rho_2-1)}\sim\frac{(\ln\lambda)^2}{2\lambda f}
$$
（首项）。若这些解是不稳定的（看来很可能如此），则由周围细胞供给的孤立团簇会无限制地增长和收缩：这就是 Nanjundiah（1973）设想的随时间变化的奇异解。对于径向对称的团簇，进一步的不稳定性使细胞的角分布变得不均匀，这可能与聚集晚期汇聚到中心的细流有关。

对于完全周期的解，每个中心可用的细胞数是有限的。取 $\rho_0=1$，当 $-V''(1)=2(1-\lambda)<0$ 时出现无穷小振幅的周期解，所以它们在 $\lambda>1$ 时从均匀态分出，波长为

$$
L_0=\int\frac{\mathrm{d}\rho}{\sqrt{(E-(\lambda-1)(\rho-1)^2)/\nu}}\Big|_{\text{one period}}=\frac{\pi}{\sqrt{\lambda-1}}\quad(\nu=1),
$$
一个分支由该波长与每个领地的细胞数 $L_0a_0=L_0/f$ 确定。可能还存在第二个稳定的稳态解分支，这将使具有有限领地大小的聚集成为一个经由不稳定分支到达稳定团簇的有限振幅转变；对该模型尚未证明这一点。大 $\lambda$ 的渐近解提供了一些证据。写 $\frac{A\lambda}{2f}=\lambda B\mathrm{e}^{-\lambda\rho_m}$，其中 $\rho_m$ 是 $\rho$ 的最大值，位于 $x=\pm L_0/2$。远离极大值处可以忽略趋化性，$\rho^*(x)=\dfrac{\cosh(x/\sqrt\nu)}{2f\sqrt\nu\sinh(L_0/2\sqrt\nu)}$，其周期延拓在极大值处有一个尖角。在边界层 $\xi=(x-L_0/2)\lambda/\sqrt\nu$，$w=(\rho-\rho_m)\lambda$ 中，当 $\lambda\to\infty$ 时方程变为 $B\mathrm{e}^w+w_{\xi\xi}=0$，$\xi=0$ 处 $w_\xi=0$，所以 $B\mathrm{e}^w+\frac12w_\xi^2=B$，

$$
w=\ln\operatorname{sech}^2\Big(\sqrt{\tfrac B2}\,\xi\Big),\qquad B=\frac1{8f^2\nu},\qquad a=\lambda B\operatorname{sech}^2\Big(\sqrt{\tfrac B2}\,\xi\Big)
$$
（检验：$w_{\xi\xi}=-B\operatorname{sech}^2$，$B\mathrm{e}^w=B\operatorname{sech}^2$）。复合近似为 $\rho=\frac1\lambda\big[w\big(\frac\lambda{\sqrt\nu}(x-\frac{L_0}2)\big)+w\big(\frac\lambda{\sqrt\nu}(x+\frac{L_0}2)\big)\big]+\rho^*(x)$。除聚集点附近外，细胞密度是指数小的。

![非线性稳态。A：振幅方程的周期解在 r = 4 pi^2 处离开均匀态，并随振幅增大而向较小的 r 弯回，这是亚临界分岔；插图：椭圆参数为 0.5 与 0.99 的分布。B：孤立聚集体的峰值细胞密度对 lambda = kappa / mu 的关系，随 lambda 减小而无限增长（虚线：首项渐近线）。C：大 lambda 时的边界层聚集体是 sech^2 团簇，其高度随 lambda 增长](./plots/ks-nonlinear.py)

## 13.7. 塌缩取决于维数

继 Nanjundiah 提出聚集体塌缩成 delta 函数的猜想之后，Childress 与 Percus（1981）证明答案取决于空间的维数。在一维中，常系数 Keller–Segel 模型不能形成奇点。在二维中，必须聚集到临界数目的细胞，才会在有限时间内形成 delta 函数。在三维或更高维中，存在任意大小的自相似塌缩聚集体。

**定义 13.7.1（趋化塌缩）** **趋化塌缩**是趋化模型的细胞密度在有限时间内形成奇点，即有限数量的细胞集中到一点。

二维阈值可以对抛物–椭圆简化给出精确形式：$a_t=\mu\Delta a-\kappa\nabla\cdot(a\nabla\rho)$，$-\Delta\rho=a$，在 $\mathbb{R}^2$ 中，其中引诱物扩散很快且不被降解。

**定理 13.7.1（临界质量）** 设 $M=\int a\,\mathrm{d}\boldsymbol{x}$ 为细胞总数。对具有有限二阶矩的光滑解，

$$
\frac{\mathrm{d}}{\mathrm{d}t}\int\lvert\boldsymbol{x}\rvert^2a\,\mathrm{d}\boldsymbol{x}=4\mu M\Big(1-\frac{\kappa M}{8\pi\mu}\Big).
$$
因此，若 $M>8\pi\mu/\kappa$，则解不能对所有时间都存在：细胞在有限时间内塌缩。

**证明** 分部积分得 $\frac{\mathrm{d}}{\mathrm{d}t}\int\lvert\boldsymbol{x}\rvert^2a=\mu\int a\,\Delta\lvert\boldsymbol{x}\rvert^2+\kappa\int a\,\nabla\lvert\boldsymbol{x}\rvert^2\cdot\nabla\rho=4\mu M+2\kappa\int a\,\boldsymbol{x}\cdot\nabla\rho$。由 $\rho=-\frac1{2\pi}\ln\lvert\cdot\rvert*a$，$\nabla\rho(\boldsymbol{x})=-\frac1{2\pi}\int\frac{\boldsymbol{x}-\boldsymbol{y}}{\lvert\boldsymbol{x}-\boldsymbol{y}\rvert^2}a(\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}$，并对 $\boldsymbol{x}$ 与 $\boldsymbol{y}$ 对称化，

$$
\int a\,\boldsymbol{x}\cdot\nabla\rho=-\frac1{4\pi}\iint a(\boldsymbol{x})a(\boldsymbol{y})\frac{(\boldsymbol{x}-\boldsymbol{y})\cdot(\boldsymbol{x}-\boldsymbol{y})}{\lvert\boldsymbol{x}-\boldsymbol{y}\rvert^2}=-\frac{M^2}{4\pi}.
$$
所以二阶矩以常速率 $4\mu M-\kappa M^2/2\pi$ 变化。若它为负，则非负的二阶矩将在有限时间内变成负的，这对光滑解是不可能的。$\square$

低于临界质量时，解整体存在（Jäger 与 Luckhaus，1992；Blanchet、Dolbeault 与 Perthame，2006），所以 $8\pi\mu/\kappa$ 是尖锐的。真实的细胞不能被无限压缩：若趋化通量随空间被填满而减小，$\kappa\to\kappa(1-a/a_{\max})$，则塌缩被阻止，聚集体成为密度有界的平台，并缓慢粗化（Painter 与 Hillen，2002），其精神与黏附驱动运动模型中的体积排斥项相同（[7.5.7](/7.5.7)）。

![带体积填充的 Keller–Segel 模型中的二维聚集，由近乎均匀的细胞场出发：出现小团簇（t = 6），从周围吸引细胞而长大（t = 15），最后成为少数几个聚集体，其密度在堆积极限处饱和（t = 40）](./plots/ks-aggregation-2d.py)

## 13.8. 动物胚胎中的趋化性

曾有人类比黏菌，提出趋化性是脊椎动物**原肠作用**的机制。现在知道它指导许多胚胎迁移，尽管很少单独起作用。

| 迁移 | 引诱物与受体 | 说明 | 章 |
|---|---|---|---|
| 原始生殖细胞（斑马鱼、小鼠、果蝇） | SDF-1（CXCL12）与 CXCR4 | 细胞沿着移动的 SDF-1 条带走向性腺；果蝇中是来自性腺的脂质信号 | [7.5.27](/7.5.27) |
| 鸡原条中的中胚层 | FGF8（排斥）与 FGF4（吸引） | 离开原条的细胞被推也被拉 | [7.5.9](/7.5.9) |
| 神经嵴 | SDF-1、补体 C3a（共吸引） | 与运动接触抑制相结合 | [7.5.20](/7.5.20) |
| 侧线原基（斑马鱼） | SDF-1 与 CXCR4，后部有清道夫受体 CXCR7 | 细胞通过清除引诱物自己产生梯度 | [7.5.20](/7.5.20) |
| 轴突 | netrin、Slit、信号素（生长锥导向） | 对细胞一部分的吸引与排斥 | [7.5.21](/7.5.21) |

侧线原基让人想起 Keller–Segel 模型的降解项 $g(\rho)$：既响应又破坏均匀分布在组织中的引诱物的一群细胞，会在自身内部形成梯度并沿它向上迁移，这是一种不需要局部源的自生成梯度。盘基网柄菌细胞在密集的群体中对叶酸与 cAMP 也是这样做的。

## 小结

| 主题 | 主要结果 |
|---|---|
| 生物体 | 社会性变形虫（变形虫门，不是真菌）；饥饿 → cAMP 信号 → 约 $10^5$ 个细胞聚集 → 蛞蝓体（前柄在前，前孢子在后）→ 子实体 |
| 比例 | 前孢子/前柄 $=KV^\lambda$，$\lambda\approx0.2$；当前的机制：有偏的随机选择、分选与 DIF-1 反馈；具有恒定过渡层的反应扩散模型再现该异速关系；截断后的调节需要 $\sim(\ell-x_s)^2/\nu$ 的时间 |
| 中继 | 定义 13.3.1；邻居所见的脉冲 $(sa/4)\mathrm{e}^{-1/\tau}/\tau$；临界密度 $a_c=4\mathrm{e}\rho_c/s$；速度 $R/(T_p+T_d)\approx R/T_d$（公式 13.3.1）；连续极限 $a_t+Q(a)_x=0$，$Q=-a\Delta(a)/T$；可兴奋介质的靶波与螺旋波 |
| Keller–Segel | 定义 13.4.1；增长率为实数；不稳定当且仅当 $\mu_0\alpha_0+\kappa_0f_0>0$；边缘模式 $k=0$，$k^2_{\max}=\Delta/2\mu_0\nu_0$，$\sigma_{\max}=\Delta^2/4\lvert\alpha_0\rvert\mu_0\nu_0$（定理 13.4.1）；领地大小问题 |
| 增强的 Turing | 用 $R=\alpha+f\kappa^{\mathsf T}/\mu$ 代替 $\alpha$；有两种化学物质时趋化性可以产生有限波长（例 13.5.1） |
| 非线性 | 振幅方程 (13.2)；椭圆函数稳态，$r=48K(E+mK/3-2K/3)$，$A_0=24K^2m$，亚临界（命题 13.6.1）；孤立聚集体 $a_2\sim(\ln\lambda)^2/2\lambda f$；大 $\lambda$ 时的 sech² 团簇 |
| 塌缩 | 定义 13.7.1；一维中无塌缩，二维中临界质量为 $8\pi\mu/\kappa$（定理 13.7.1），三维中任意质量；体积填充阻止塌缩 |
| 胚胎 | 生殖细胞与神经嵴的 SDF-1/CXCR4，原条中的 FGF，自生成梯度 |

## 思考题

1. 为什么*盘基网柄菌*虽然不是动物，却被用于发育生物学研究？为什么它不是真菌？

   **答** 它以简单的形式解决发育问题：多细胞性、细胞类型的比例调节与切割之后的调节、分选、形态发生运动与信号中继，有已知的信号（cAMP）和可计数的细胞；并且由于它的细胞来自不同的谱系而聚集在一起，图式不可能继承自卵。分子系统发育把它放在变形虫门，与阿米巴样的原生生物在一起，而不与真菌在一起（真菌与动物同属后鞭毛生物）；它有壁的孢子与子实体与真菌的相似是趋同的。

2. 在 Cohen–Robertson 模型中，证明当密度从上方趋近 $a_c$ 时触发时间 $\tau_p$ 趋于 $1$，当 $a\to\infty$ 时趋于 $0$。波速会怎样变化？这符合实际吗？

   **答** 触发条件为 $g(\tau_p)=a_c/(\mathrm{e}a)$。当 $a\to a_c^+$ 时，右端趋近 $g$ 的最大值 $1/\mathrm{e}$，它在 $\tau=1$ 处取得，所以 $\tau_p\to1$。当 $a\to\infty$ 时右端趋于零，$\mathrm{e}^{-1/\tau}/\tau=\varepsilon$ 的较小根趋于零（大约 $\tau_p\approx1/\ln(1/\varepsilon)$）。速度 $R/(R^2\tau_p/4\nu+T_d)$ 趋近 $R/T_d$，它按 $a^{-1/2}$ 减小。在真实的细胞中，中继延迟与兴奋性随密度和发育而变化，所以速度并不遵循这一简单规律；模型的启示是，中继波受延迟限制，而不是受扩散限制。

3. 估计 cAMP 脉冲在相邻变形虫之间（$R=40\,\mathrm{\mu m}$，$\nu=400\,\mathrm{\mu m^2\,s^{-1}}$）和越过 $5\,\mathrm{mm}$ 的领地所需的扩散时间。这对远程信号传导意味着什么？

   **答** 相邻细胞之间 $R^2/4\nu=1600/1600=1\,\mathrm{s}$；越过领地为 $(5000)^2/(4\times400)\approx1.6\times10^4\,\mathrm{s}\approx4.3\,\mathrm{h}$，脉冲会被稀释到消失。仅靠扩散不能在 5 min 的一个周期内组织起一个领地；而中继，即每个细胞再生信号，使波在几分钟内传遍领地，代价是每个细胞有固定的延迟。

4. 验证恒等式 $A^2-4B=((\mu_0-\nu_0)k^2+\alpha_0)^2+4\kappa_0f_0k^2$，并从生物学上解释为什么 Keller–Segel 不稳定性不是振荡的，而真实细胞的 cAMP 信号传导是振荡的。

   **答** 按定理 13.4.1 证明中那样展开。由于 $\kappa_0f_0>0$（细胞沿自己所产生的引诱物的梯度向上运动），判别式为正，所以根是实数。模型中没有延迟的负反馈：引诱物吸引细胞，细胞产生更多引诱物，这是一个纯粹的正反馈环。真实细胞会适应（受体**脱敏**与环化酶的适应）并进入不应期，这是延迟的负反馈，使信号系统成为可兴奋的或振荡的，而平均化的模型把这一点略去了。

5. 取 $\mu_0=\nu_0=1$，$\alpha_0=-1$，$\Delta=0.1$，计算增长最快的波长及其增长率。若 $\Delta$ 加倍，波长如何变化？为什么这对解释领地大小是个问题？

   **答** $k^2_{\max}=\Delta/(2\mu_0\nu_0)=0.05$，$k_{\max}=0.224$，波长 $2\pi/k_{\max}=28$；$\sigma_{\max}=\Delta^2/(4\lvert\alpha_0\rvert\mu_0\nu_0)=0.0025$。$\Delta$ 加倍给出 $k^2_{\max}=0.1$，波长 $19.9$，缩小到 $1/\sqrt2$。波长取决于聚集开始时系统恰好超过阈值多远，所以领地大小会随初始条件而变化；而观察到的领地有特征大小，这指向中继动力学，而不是平滑的不稳定性。

6. 检验例 13.5.1：计算有与没有趋化性时的 $R$ 与 Turing 量。该例子超过阈值多少倍？

   **答** $f\kappa^{\mathsf T}/\mu=\begin{bmatrix}1&0\\1&0\end{bmatrix}$，所以 $R=\begin{bmatrix}3&-3\\6&-5\end{bmatrix}$，$\det R=-15+18=3$。没有趋化性：$\nu_1\alpha_{22}+\nu_2\alpha_{11}=-5+8=3$，而 $2\sqrt{4\cdot5}=8.94$（稳定）。有趋化性：$-5+12=7$，而 $2\sqrt{4\cdot3}=6.93$：不稳定，裕度约 1 %。（若按 $2\sqrt5$ 与 $2\sqrt3$ 来写，阈值会低一个因子 $\sqrt{\nu_1\nu_2}=2$；结论成立，但只是勉强。）更强的响应 $\kappa_1=1.5$ 给出 $R_{11}=3.5$，$R_{21}=6.5$，$\det R=2$，$-5+14=9>2\sqrt8=5.66$，明显不稳定。

7. 证明命题 13.6.1 的周期稳态在振幅趋于零时 $r\to4\pi^2$，并解释为什么分支向较小的 $r$ 弯曲意味着聚集中的**滞后**。

   **答** 当 $m\to0$ 时，$K=E=\pi/2$，$r=48\cdot\frac\pi2\big(\frac\pi2-\frac\pi3\big)=4\pi^2$，这正是模式 $k=2\pi$ 的线性增长率 $rk^2-k^4$ 变号的点。当 $r$ 略小于 $4\pi^2$ 时，均匀态是稳定的，但其附近存在一个不稳定的图式态；比这个态更大的扰动可以把系统推入大振幅的聚集态。一旦聚集，把 $r$ 降到阈值以下并不能恢复均匀性（聚集态持续存在），而把 $r$ 升到 $4\pi^2$ 以上则使均匀态失稳：转变取决于变化的方向，这是亚临界分岔典型的滞后。

8. 证明在一维中孤立聚集体只在 $\lambda<1$ 时存在，并分别用首项公式和精确方程估计 $\lambda=0.1$ 时的峰值细胞密度。

   **答** 在 $\lambda=1$ 时，背景 $\rho_1=1$ 是退化的（三重）根，凸起的振幅为零；对 $\lambda>1$，背景是 $V$ 的极小点（$V''(1)=2(\lambda-1)>0$），围绕它只存在周期轨道，没有同宿轨道。在 $\lambda=0.1$ 时，首项公式给出 $a_2\approx(\ln0.1)^2/(2\times0.1)=26.5$。精确方程 $\rho_2^2-20\mathrm{e}^{0.1(\rho_2-1)}=-19$ 的根为 $\rho_2\approx48.9$，所以 $a_2=\mathrm{e}^{0.1\times47.9}\approx121$：渐近公式的趋势正确，但收敛很慢，因为修正是 $\ln\lvert\ln\lambda\rvert$ 量级的。

9. （实验设计）在蛞蝓体中，如何区分根据位置转变细胞的反应扩散预图式与随机选择命运的细胞的分选？

   **答** 在聚集之前标记一个细胞亚群（例如用荧光标记），并追踪它们。在分选的情形，表达前柄标记的细胞起初散布在整个土墩中，随后移向尖端；被标记的细胞改变位置多于改变命运。在位置预图式的情形，细胞根据所处的位置采取命运，被移植的细胞（或切开再重新拼合的蛞蝓体中被移动的细胞）会不经移动而改变命运以适应新的位置。两种情况都发生：最初的分化是椒盐式的，随后分选；而切割之后，新边界处的细胞确实发生转变，这是由 DIF-1 等可扩散信号介导的调整性响应。

10. 利用定理 13.7.1，当 $\mu=10\,\mathrm{\mu m^2\,min^{-1}}$，$\kappa$ 使 $\kappa/\mu=10^{-3}\,\mathrm{\mu m^2}$ 每个细胞（取 $-\Delta\rho=a$ 的归一化）时，计算塌缩的临界细胞数。为什么真实的聚集体不会塌缩成一个点？

    **答** $M_c=8\pi\mu/\kappa=8\pi\times10^3\approx2.5\times10^4$ 个细胞。$10^5$ 个细胞的真实聚集体超过了它，却没有塌缩，因为细胞有有限的体积：堆积极限、细胞间黏附与土墩的力学（以体积填充 $\kappa(1-a/a_{\max})$ 建模）用密度有界的致密土墩取代了奇点，随后土墩长出尖端并成为蛞蝓体。
