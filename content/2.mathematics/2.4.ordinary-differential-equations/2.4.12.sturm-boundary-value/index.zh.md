---
title: Sturm 理论与边值问题
---

二阶变系数线性方程 $y''+a_1(x)y'+a_2(x)y=0$ 一般解不出来，但它的解的许多性质仍然可以直接从方程读出。本章的主角是解的零点：零点在哪里、有多密、两个解的零点怎样排列。Sturm 的思想是把待研究的方程与一个已知解的方程（常常是常系数方程）比较，系数大的方程振动得快、零点密。这套"不求解的定性理论"有两个用途：一是判断解是否振动、估计零点间距；二是研究边值问题——在区间两端给定条件、同时求未知参数 $\lambda$ 的特征值问题。后者引出 Sturm–Liouville 理论：特征值是实的、可数的、趋于无穷，特征函数两两正交并可以用来展开函数，三角级数（[2.2.9](/2.2.9#sec-9.3)）只是它的一个特例。偏微分方程（[2.5](/2.5)）的分离变量法正是建立在这一理论之上。

本章用到二阶线性方程的一般理论（[2.4.9](/2.4.9)、[2.2.16](/2.2.16#sec-16.1)）：**存在唯一性定理**、**Wronski 行列式**与 **Liouville 公式**。以下总设系数在所论区间上连续，"非零解"指不恒为零的解。

## 12.1. 二阶线性方程的标准形式

### 12.1.1. 零点的孤立性

**引理 12.1.1** 设 $a_1,a_2\in C(I)$，$y(x)$ 是方程

$$
y''+a_1(x)y'+a_2(x)y=0\tag{12.1}
$$
在区间 $I$ 上的非零解，则 $y$ 的零点是孤立的：$y$ 的零点在 $I$ 内没有聚点。特别地，$y$ 在任何有界闭子区间上只有有限个零点。

**证明** 反证。设零点 $x_k\to x^*\in I$，$x_k\ne x^*$。由连续性 $y(x^*)=\lim y(x_k)=0$；由 Lagrange 中值定理，存在 $\xi_k$ 介于 $x_k$ 与 $x^*$ 之间，使

$$
y'(\xi_k)=\frac{y(x_k)-y(x^*)}{x_k-x^*}=0,
$$
令 $k\to\infty$ 得 $y'(x^*)=0$。于是 $y$ 与零解满足同一初值条件 $y(x^*)=y'(x^*)=0$，由解的唯一性 $y\equiv0$，矛盾。$\square$

同样的论证说明：非零解的零点都是单零点，即 $y(x_0)=0$ 时必有 $y'(x_0)\ne0$，所以解在零点处一定变号。

### 12.1.2. 标准形与自伴形式

方程 (12.1) 有两种常用的等价写法，各自消去了一个系数。

**引理 12.1.2** 设 $a_1\in C^1(I)$，$a_2\in C(I)$，$x_0\in I$。作变换

$$
y=z\exp\Big(-\frac12\int_{x_0}^x a_1(t)\,\mathrm{d}t\Big),
$$
则方程 (12.1) 化为不含一阶导数的标准形

$$
z''+Q(x)z=0,\qquad Q(x)=a_2(x)-\frac12a_1'(x)-\frac14a_1^2(x).\tag{12.2}
$$

直接代入即可验证。由于变换因子恒正，$y$ 与 $z$ 的零点完全相同，因此研究零点时只需讨论标准形 (12.2)。

**定义 12.1.1（自伴形式）** 设 $p\in C^1(I)$，$p>0$，$q\in C(I)$。形如

$$
\big(p(x)y'\big)'+q(x)y=0\tag{12.3}
$$
的方程称为二阶线性方程的**自伴形式**（Sturm–Liouville 形式）。

把 (12.1) 乘以 $p(x)=\exp\big(\int_{x_0}^x a_1(t)\,\mathrm{d}t\big)$，因为 $p'=a_1p$，左边就是 $(py')'+a_2py$。所以任何方程 (12.1)（只需 $a_1$ 连续）都可以化为自伴形式，取 $q=a_2p$。"自伴"的意义见 §12.5：在适当的边界条件下，算子 $y\mapsto-(py')'+qy$ 是**自伴随算子**。

对自伴形式，Liouville 公式化为一个简洁的守恒律：若 $u,v$ 都是 (12.3) 的解，则

$$
\frac{\mathrm{d}}{\mathrm{d}x}\Big[p(uv'-u'v)\Big]=u(pv')'-v(pu')'=u(-qv)-v(-qu)=0,
$$
即 $p(x)W(x)$ 是常数，其中 $W=uv'-u'v$。

## 12.2. Sturm 比较定理

### 12.2.1. 分离定理

**定理 12.2.1（Sturm 分离定理）** 设 $u,v$ 是方程 (12.1) 的两个线性无关的解，则 $u,v$ 没有公共零点，且它们的零点相互交错：$u$ 的任意两个相邻零点之间恰有 $v$ 的一个零点，反之亦然。

**证明** 由 Liouville 公式，$W(x)=u v'-u'v=W(x_0)\exp\big(-\int_{x_0}^x a_1\big)$ 处处不为零，不妨设 $W>0$。若 $u,v$ 有公共零点 $x_1$，则 $W(x_1)=0$，矛盾。

设 $x_1<x_2$ 是 $u$ 的相邻零点，不妨设 $u>0$ 于 $(x_1,x_2)$。零点是单零点，故 $u'(x_1)>0$，$u'(x_2)<0$。在 $x_1,x_2$ 处 $W=-u'v$，于是

$$
W(x_1)=-u'(x_1)v(x_1)>0,\qquad W(x_2)=-u'(x_2)v(x_2)>0,
$$
得 $v(x_1)<0<v(x_2)$，由介值定理 $v$ 在 $(x_1,x_2)$ 内至少有一个零点。若 $v$ 在 $(x_1,x_2)$ 内有两个零点 $\zeta<\eta$，交换 $u,v$ 的角色，$u$ 在 $(\zeta,\eta)$ 内有零点，与 $x_1,x_2$ 相邻矛盾。$\square$

例如 $y''+y=0$ 的解 $\sin x$ 与 $\cos x$ 的零点交错。分离定理说明：同一方程的所有非零解"振动得一样快"，零点个数在任何区间上至多相差 1。

### 12.2.2. 比较定理

考虑两个标准形方程

$$
z''+Q(x)z=0,\tag{12.4}
$$

$$
y''+P(x)y=0,\tag{12.5}
$$
其中 $P,Q\in C[x_0,+\infty)$。

**定理 12.2.2（Sturm 比较定理）** 设 $Q(x)\le P(x)$，$x\ge x_0$。若 $a<b$ 是方程 (12.4) 的某个非零解 $z$ 的两个相邻零点，则方程 (12.5) 的任一非零解 $y$ 在闭区间 $[a,b]$ 上至少有一个零点。

**证明** 用 $y$ 乘 (12.4)、$z$ 乘 (12.5) 后相减，得 $yz''-y''z=(P-Q)yz$，即

$$
\frac{\mathrm{d}}{\mathrm{d}x}(yz'-y'z)=(P-Q)yz.
$$
从 $a$ 到 $b$ 积分，利用 $z(a)=z(b)=0$：

$$
y(b)z'(b)-y(a)z'(a)=\int_a^b\big[P(x)-Q(x)\big]y(x)z(x)\,\mathrm{d}x.\tag{12.6}
$$
不妨设 $z>0$ 于 $(a,b)$，则 $z'(a)>0$，$z'(b)<0$。若 $y>0$ 于 $[a,b]$，则 (12.6) 左边小于零而右边大于等于零，矛盾；$y<0$ 于 $[a,b]$ 时同理。故 $y$ 在 $[a,b]$ 上有零点。$\square$

**推论 12.2.1** 若在定理 12.2.2 中还有：在 $[a,b]$ 的任何子区间上 $P\not\equiv Q$，则 $y$ 在开区间 $(a,b)$ 内至少有一个零点。

**证明** 若 $y$ 在 $(a,b)$ 内无零点，不妨设 $y>0$ 于 $(a,b)$，$y(a),y(b)\ge0$。此时 (12.6) 左边 $\le0$；右边被积函数 $\ge0$ 且在某处为正（$P-Q\ge0$ 连续且不恒为零），积分 $>0$，矛盾。$\square$

**推论 12.2.2** 若 $0<m^2\le Q(x)\le M^2$，$x\in(a,b)$，其中 $m,M$ 是常数，则方程 (12.4) 的任一非零解在 $(a,b)$ 内的两个相邻零点之间的距离 $d$ 满足

$$
\frac{\pi}{M}\le d\le\frac{\pi}{m}.
$$

**证明** 与常系数方程 $u''+m^2u=0$、$v''+M^2v=0$ 比较，它们的解 $\sin(mx+\theta_1)$、$\sin(Mx+\theta_2)$ 的相邻零点间距是 $\pi/m$、$\pi/M$，适当选取 $\theta_1,\theta_2$ 可以让零点落在任意指定的位置。若 $z$ 有相邻零点 $\alpha<\beta$ 且 $\beta-\alpha>\pi/m$，可取 $u$ 使它的两个相邻零点都落在 $(\alpha,\beta)$ 内，由定理 12.2.2（$m^2\le Q$），$z$ 在 $u$ 的这两个零点所夹的闭区间上有零点，与 $\alpha,\beta$ 相邻矛盾。另一侧同理（用 $Q\le M^2$ 与 $v$ 比较）。$\square$

比较定理的意义是："$Q$ 越大，解振动得越快。"下图左侧是 $y''+xy=0$ 的两个线性无关解，零点交错，且随着系数 $x$ 增大越来越密（间距约为 $\pi/\sqrt x$）；右侧比较 $z''+z=0$ 与 $y''+(1+x/5)y=0$：后者系数更大，$\sin x$ 的每两个相邻零点之间都有它的零点。

![左：y'' + x y = 0 的两个线性无关解的零点交错且渐密；右：y'' + (1 + x/5) y = 0 的解比 sin x 振动得快](./plots/sturm-zeros.py)

**例 12.2.1** Bessel 方程 $x^2y''+xy'+(x^2-\nu^2)y=0$（$x>0$，见 [2.4.10](/2.4.10)）的标准形为（引理 12.1.2，$a_1=1/x$，$y=z/\sqrt x$）

$$
z''+\Big(1+\frac{1-4\nu^2}{4x^2}\Big)z=0.
$$
由推论 12.2.2：$|\nu|<\frac12$ 时 $Q>1$，**Bessel 函数**的相邻零点间距小于 $\pi$；$|\nu|>\frac12$ 时 $Q<1$，间距大于 $\pi$；$\nu=\frac12$ 时 $z=\sin x$，间距恰为 $\pi$。又 $Q\to1$（$x\to+\infty$），对任意 $\varepsilon>0$，$x$ 充分大时 $(1-\varepsilon)^2\le Q\le(1+\varepsilon)^2$，所以无论 $\nu$ 为何值，相邻零点间距都趋于 $\pi$。

### 12.2.3. 自伴形式的比较定理

比较定理对自伴形式同样成立，此时 $p$ 小、$q$ 大的方程振动得快。

**定理 12.2.3（Sturm–Picone 比较定理）** 设 $p_1\ge p_2>0$，$q_2\ge q_1$ 于 $[a,b]$，$p_i\in C^1$，$q_i\in C$。若 $a,b$ 是方程 $(p_1y')'+q_1y=0$ 的某个非零解 $y$ 的相邻零点，则方程 $(p_2z')'+q_2z=0$ 的任一非零解 $z$ 在 $[a,b]$ 上至少有一个零点。

证明的思路与定理 12.2.2 相同，只是把积分恒等式 (12.6) 换成 Picone 恒等式：在 $z\ne0$ 处

$$
\frac{\mathrm{d}}{\mathrm{d}x}\Big[\frac{y}{z}\big(p_1y'z-p_2yz'\big)\Big]=(q_2-q_1)y^2+(p_1-p_2)y'^2+p_2\Big(y'-\frac{y}{z}z'\Big)^2.
$$
若 $z$ 在 $[a,b]$ 上无零点，从 $a$ 到 $b$ 积分，左边为零，右边为非负函数的积分，只能各项恒为零，由此推出 $z$ 是 $y$ 的常数倍，与 $z(a)\ne0$ 矛盾。

## 12.3. 振动与非振动

### 12.3.1. 振动方程

**定义 12.3.1（振动解）** 设 $y$ 是方程 (12.3)（或 (12.4)）在 $[x_0,+\infty)$ 上的非零解。若 $y$ 在 $[x_0,+\infty)$ 上只有有限个零点，则称 $y$ 是**非振动的**；否则称 $y$ 是**振动的**，即存在无穷多个 $x_k\in[x_0,+\infty)$ 使 $y(x_k)=0$。由零点的孤立性（引理 12.1.1），此时必有 $x_k\to+\infty$。

由分离定理，同一方程的两个非零解零点个数在任何区间上至多差 1，因此一个解振动当且仅当所有非零解都振动。

**定义 12.3.2（振动方程）** 若方程 (12.3) 有一个（从而所有）非零解是振动的，则称方程是**振动的**；否则称它是**非振动的**。

**定理 12.3.1** 考虑方程 $(p_1y')'+q_1y=0$ 与 $(p_2y')'+q_2y=0$，$x\ge x_0$，其中 $p_1\le p_2$，$q_1\ge q_2$。

1. 若第二个方程是振动的，则第一个方程也是振动的；
2. 若第一个方程是非振动的，则第二个方程也是非振动的。

这是定理 12.2.3 的直接推论：第二个方程的非零解在 $[x_0,+\infty)$ 上有无穷多个相邻零点对，每一对之间都有第一个方程的解的零点。两条结论互为逆否命题。

### 12.3.2. Riccati 不等式判别法

方程 (12.3) 的非零解 $y$ 在无零点的区间上满足：$r=py'/y$ 满足一阶方程

$$
r'+q(x)+\frac{r^2}{p(x)}=0,
$$
这是一个 **Riccati 方程**（直接求导可验证）。于是"解没有零点"可以翻译成"Riccati 方程有整体解"，而有不等式的解就够了：

**定理 12.3.2** 方程 (12.3)（$x\ge x_0$）是非振动的，当且仅当存在 $x_1\ge x_0$ 与 $r\in C^1[x_1,+\infty)$，使当 $x\ge x_1$ 时

$$
r'+q(x)+\frac{r^2}{p(x)}\le0.\tag{12.7}
$$

**证明** 必要性：若方程非振动，则存在 $x_1$，使某个非零解 $y$ 在 $[x_1,+\infty)$ 上无零点，取 $r=py'/y$，(12.7) 以等号成立。

充分性：记 $s(x)=r'+q+r^2/p\le0$，则 $r$ 满足 $r'+(q-s)+r^2/p=0$。令 $z(x)=\exp\big(\int_{x_1}^x\frac{r(t)}{p(t)}\,\mathrm{d}t\big)>0$，则 $pz'=rz$，

$$
(pz')'=r'z+rz'=\Big(r'+\frac{r^2}{p}\Big)z=(s-q)z,
$$
即 $z$ 是方程 $(pz')'+(q-s)z=0$ 的无零点的解，该方程非振动。因为 $q-s\ge q$，由定理 12.3.1 的第 2 条，方程 (12.3) 非振动。$\square$

**例 12.3.1** 若 $q(x)\le0$（$x\ge x_0$），则 (12.3) 非振动：取 $r\equiv0$，$r'+q+r^2/p=q\le0$。也可以与 $(py')'=0$ 比较，后者有无零点的解 $y\equiv1$。

**例 12.3.2** 若 $0<p(x)\le p_0$，$q(x)\ge q_0>0$，则 (12.3) 是振动的，且任一非零解的相邻零点间距不超过 $\pi\sqrt{p_0/q_0}$。事实上，与 $(p_0y')'+q_0y=0$ 即 $y''+\frac{q_0}{p_0}y=0$ 比较，后者的解 $\sin\big(\sqrt{q_0/p_0}\,(x-x_0)\big)$ 的零点为 $x_0+n\pi\sqrt{p_0/q_0}$，由定理 12.2.3，(12.3) 的解在每两个相邻零点之间都有零点。特别地，$p\equiv1$，$q\ge M>0$ 时，相邻零点间距不超过 $\pi/\sqrt M$；若 $q(x)\to+\infty$，则相邻零点间距趋于 $0$。

**例 12.3.3（临界常数 $\frac14$）** **Euler 方程** $y''+\dfrac{c}{x^2}y=0$（$x\ge1$）的解为 $x^m$，$m(m-1)+c=0$。当 $c\le\frac14$ 时 $m$ 是实数，解 $x^{m_1}$、$x^{m_2}$（$c=\frac14$ 时为 $\sqrt x$、$\sqrt x\ln x$）的线性组合在 $x\ge1$ 上至多有一个零点，方程非振动；当 $c>\frac14$ 时 $m=\frac12\pm\mathrm{i}\beta$，实解 $\sqrt x\cos(\beta\ln x)$ 有无穷多个零点，方程振动。结合比较定理得 Kneser 判别法：若 $x$ 充分大时 $q(x)\le\frac{1}{4x^2}$，则 $y''+q(x)y=0$ 非振动（也可直接取 $r=\frac{1}{2x}$ 验证 (12.7)）；若 $q(x)\ge\frac{c}{x^2}$，$c>\frac14$，则方程振动。可见 $q\to0$ 的方程是否振动取决于 $q$ 趋于零的速度。

### 12.3.3. Prüfer 变换

比较定理的另一种证明方式是用极坐标描述相平面 $(y,y')$ 上的运动。对方程 $y''=f(x,y,y')$ 令

$$
y=r\sin\theta,\qquad y'=r\cos\theta\qquad(r>0).
$$
由 $y'=r'\sin\theta+r\theta'\cos\theta=r\cos\theta$ 与 $y''=r'\cos\theta-r\theta'\sin\theta=f$，第一式乘 $\sin\theta$ 加第二式乘 $\cos\theta$、第一式乘 $\cos\theta$ 减第二式乘 $\sin\theta$，得等价方程组

$$
r'=\cos\theta\big[r\sin\theta+f(x,y,y')\big],\qquad\theta'=\cos^2\theta-\frac{\sin\theta\,f(x,y,y')}{r}.
$$
对标准形 $y''+Q(x)y=0$，$f=-Qy=-Qr\sin\theta$，角度方程与 $r$ 无关：

$$
\theta'=\cos^2\theta+Q(x)\sin^2\theta.\tag{12.8}
$$
这就是 Prüfer 变换（Prüfer transformation）：把二阶线性方程化为一个关于角度 $\theta$ 的一阶方程和一个可由 $\theta$ 求出的 $r$。$y$ 的零点恰是 $\theta$ 取 $\pi$ 的整数倍的点，在这些点上 $\theta'=1>0$，所以 $\theta$ 只能递增地穿过 $k\pi$。零点问题由此变成"$\theta$ 转得多快"的问题，而由 (12.8)，$Q$ 越大，$\theta$ 转得越快——这就是比较定理的几何解释。对自伴形式 (12.3)，相应地令 $y=r\sin\theta$，$py'=r\cos\theta$，得 $\theta'=\frac{1}{p}\cos^2\theta+q\sin^2\theta$。

**例 12.3.4** 设 $0<m^2\le Q(x)\le M^2$。由 (12.8)，$\cos^2\theta+m^2\sin^2\theta\le\theta'\le\cos^2\theta+M^2\sin^2\theta$，于是 $\theta$ 增加 $2\pi$ 所需的"时间" $T=\int_{\theta_0}^{\theta_0+2\pi}\frac{\mathrm{d}x}{\mathrm{d}\theta}\,\mathrm{d}\theta$ 满足

$$
\frac{2\pi}{M}=\int_{\theta_0}^{\theta_0+2\pi}\frac{\mathrm{d}\theta}{\cos^2\theta+M^2\sin^2\theta}\le T\le\int_{\theta_0}^{\theta_0+2\pi}\frac{\mathrm{d}\theta}{\cos^2\theta+m^2\sin^2\theta}=\frac{2\pi}{m},
$$
这里用到 $\int_{\theta_0}^{\theta_0+2\pi}\frac{\mathrm{d}\theta}{A^2\cos^2\theta+B^2\sin^2\theta}=\frac{2\pi}{AB}$（$A,B>0$）。若存在正整数 $n$ 使 $n<m\le M<n+1$，则 $\frac{2\pi}{n+1}<T<\frac{2\pi}{n}$，于是在长为 $2\pi$ 的区间上 $\theta$ 的增量严格介于 $2n\pi$ 与 $2(n+1)\pi$ 之间。而若 $y$ 是以 $2\pi$ 为周期的非零解，$(y,y')$ 回到原处，$\theta$ 的增量必须是 $2\pi$ 的整数倍。所以此时方程 $y''+Q(x)y=0$ 没有以 $2\pi$ 为周期的非零解。这推广了常系数方程 $y''+M^2y=0$（$M\notin\mathbb{Z}$）没有 $2\pi$ 周期解的事实（对比 [2.4.9](/2.4.9) 中 $y''+M^2y=f$ 的周期解）。

## 12.4. 两点边值问题

初值问题在一点给定 $y$ 与 $y'$，解总是存在唯一。物理中更常见的是在区间两端各给一个条件，例如两端固定的弦、两端温度给定的杆，这就是两点边值问题（boundary value problem）。边值问题的解可能不存在，也可能不唯一，答案取决于方程中的参数——这正是特征值问题的来源。

### 12.4.1. $y''+\lambda y=0$ 的特征值问题

**定义 12.4.1（特征值问题）** 设 $\lambda$ 是参数。若边值问题

$$
y''+\lambda y=0,\quad x\in[0,l],\qquad\text{加上齐次边界条件}
$$
在 $\lambda=\lambda_0$ 时有非零解，则称 $\lambda_0$ 为该问题的**特征值**，相应的非零解称为属于 $\lambda_0$ 的**特征函数**。

常见的齐次边界条件有：Dirichlet 边界条件（Dirichlet boundary condition）$y(0)=y(l)=0$（端点值给定），Neumann 边界条件（Neumann boundary condition）$y'(0)=y'(l)=0$（端点导数给定），以及两者的混合。

**例 12.4.1（Dirichlet 问题）** 求 $y''+\lambda y=0$，$y(0)=y(\pi)=0$ 的特征值与特征函数。

**解** 若 $\lambda=-k^2<0$，通解 $y=c_1\mathrm{e}^{kx}+c_2\mathrm{e}^{-kx}$，代入边界条件得 $c_1=c_2=0$。若 $\lambda=0$，$y=c_1x+c_2$，同样只有零解。若 $\lambda=k^2>0$（$k>0$），$y=c_1\cos kx+c_2\sin kx$，由 $y(0)=0$ 得 $c_1=0$，由 $y(\pi)=c_2\sin k\pi=0$ 且 $c_2\ne0$ 得 $k\in\mathbb{N}_+$。所以特征值为 $\lambda_n=n^2$，特征函数为 $\sin nx$，$n=1,2,\dots$（$k$ 取负整数给出同一特征函数的负倍数，不是新的特征值）。

用同样的方法可以得到下表（区间 $[0,l]$；一般区间 $[a,b]$ 把 $x$ 换成 $x-a$、$l$ 换成 $b-a$）。

| 边界条件 | 特征值 $\lambda_n$ | 特征函数 | $n$ 的范围 |
|---|---|---|---|
| $y(0)=y(l)=0$ | $\big(\frac{n\pi}{l}\big)^2$ | $\sin\frac{n\pi x}{l}$ | $1,2,\dots$ |
| $y'(0)=y'(l)=0$ | $\big(\frac{n\pi}{l}\big)^2$ | $\cos\frac{n\pi x}{l}$ | $0,1,2,\dots$ |
| $y(0)=0$，$y'(l)=0$ | $\big(\frac{(2n-1)\pi}{2l}\big)^2$ | $\sin\frac{(2n-1)\pi x}{2l}$ | $1,2,\dots$ |
| $y'(0)=0$，$y(l)=0$ | $\big(\frac{(2n-1)\pi}{2l}\big)^2$ | $\cos\frac{(2n-1)\pi x}{2l}$ | $1,2,\dots$ |
| $y(-l)=y(l)$，$y'(-l)=y'(l)$ | $\big(\frac{n\pi}{l}\big)^2$ | $1$；$\cos\frac{n\pi x}{l}$，$\sin\frac{n\pi x}{l}$ | $0$；$1,2,\dots$ |

Neumann 问题多了特征值 $0$（特征函数为常数）；最后一行是周期边界条件，每个正特征值对应两个线性无关的特征函数。这五个问题的特征函数系分别给出**正弦级数**、**余弦级数**、半整数频率的三角级数和完整的 **Fourier 级数**：三角级数展开正是这些特征值问题的特征函数展开。表中的规律（特征值实、可数、递增趋于 $+\infty$，第 $n$ 个特征函数在区间内恰有 $n-1$ 个零点，特征函数两两正交）在 §12.5 中对一般方程成立。

### 12.4.2. 非齐次边值问题

**定理 12.4.1** 设 $a_1,a_2,f\in C[a,b]$，且齐次边值问题

$$
y''+a_1(x)y'+a_2(x)y=0,\qquad y(a)=y(b)=0\tag{12.9}
$$
只有零解。则非齐次边值问题

$$
y''+a_1(x)y'+a_2(x)y=f(x),\qquad y(a)=y(b)=0\tag{12.10}
$$
有唯一解。

**证明** 设 $\varphi,\psi$ 是齐次方程的基本解组，由常数变易法（[2.4.9](/2.4.9)），非齐次方程的通解为 $y=C_1\varphi+C_2\psi+y^*$，其中

$$
y^*(x)=\int_a^xK(x,t)f(t)\,\mathrm{d}t,\qquad K(x,t)=\frac{\varphi(t)\psi(x)-\varphi(x)\psi(t)}{\varphi(t)\psi'(t)-\varphi'(t)\psi(t)}.
$$
边界条件给出线性方程组

$$
C_1\varphi(a)+C_2\psi(a)=-y^*(a),\qquad C_1\varphi(b)+C_2\psi(b)=-y^*(b),
$$
其系数行列式 $\Delta=\varphi(a)\psi(b)-\varphi(b)\psi(a)$。若 $\Delta=0$，则存在不全为零的 $c_1,c_2$ 使 $y_0=c_1\varphi+c_2\psi$ 满足 $y_0(a)=y_0(b)=0$；由于 $\varphi,\psi$ 线性无关，$y_0$ 是 (12.9) 的非零解，与假设矛盾。故 $\Delta\ne0$，$C_1,C_2$ 唯一确定：

$$
C_1=\frac{y^*(b)\psi(a)-y^*(a)\psi(b)}{\Delta},\qquad C_2=\frac{y^*(a)\varphi(b)-y^*(b)\varphi(a)}{\Delta}.
$$
唯一性：两个解之差是 (12.9) 的解，只能是零。$\square$

反过来，若齐次问题有非零解，非齐次问题要么无解、要么有无穷多解（见 §12.4.3 末尾）。这与线性代数中 $A\boldsymbol{x}=\boldsymbol{b}$ 的情形完全类似。

**例 12.4.2** 设 $M>0$，$2M\notin\mathbb{Z}$。求 $y''+M^2y=f(x)$，$y(0)=y(2\pi)=0$ 的解。

**解** 取 $\varphi=\cos Mx$，$\psi=\sin Mx$，则 $K(x,t)=\frac1M\sin M(x-t)$，$y^*(x)=\frac1M\int_0^x\sin M(x-t)f(t)\,\mathrm{d}t$，$y^*(0)=0$。$\Delta=\sin2M\pi\ne0$：条件 $2M\notin\mathbb{Z}$ 恰好说明 $M^2$ 不是 $[0,2\pi]$ 上 Dirichlet 问题的特征值 $k^2/4$（见 §12.4.1 的表），齐次问题只有零解。于是 $C_1=0$，

$$
C_2=-\frac{y^*(2\pi)}{\sin2M\pi}=\frac{1}{M\sin2M\pi}\int_0^{2\pi}\sin M(t-2\pi)f(t)\,\mathrm{d}t,
$$
唯一解为

$$
y(x)=\frac1M\Big[\frac{\sin Mx}{\sin2M\pi}\int_0^{2\pi}\sin M(t-2\pi)f(t)\,\mathrm{d}t+\int_0^x\sin M(x-t)f(t)\,\mathrm{d}t\Big].
$$

### 12.4.3. Green 函数

定理 12.4.1 的解可以写成一个积分算子作用于 $f$。对自伴形式，结果最为对称。记

$$
Ly=-\big(p(x)y'\big)'+q(x)y,\qquad p\in C^1[a,b],\ p>0,\ q\in C[a,b].
$$

**定理 12.4.2** 设齐次问题 $Ly=0$，$y(a)=y(b)=0$ 只有零解。取 $Lu=0$ 的非零解 $u_1,u_2$，使 $u_1(a)=0$，$u_2(b)=0$，记常数 $c=p\,(u_1u_2'-u_1'u_2)$（§12.1.2），则 $c\ne0$，且对任意 $f\in C[a,b]$，问题 $Ly=f$，$y(a)=y(b)=0$ 的唯一解为

$$
y(x)=\int_a^bG(x,t)f(t)\,\mathrm{d}t,\qquad G(x,t)=-\frac1c\begin{cases}u_1(t)u_2(x),&a\le t\le x,\\u_1(x)u_2(t),&x\le t\le b.\end{cases}\tag{12.11}
$$

**证明** 若 $c=0$，则 $u_1,u_2$ 线性相关，$u_1$ 同时满足两端的条件，是齐次问题的非零解，矛盾。记 $y=-\frac1c\big[u_2(x)\int_a^xu_1f\,\mathrm{d}t+u_1(x)\int_x^bu_2f\,\mathrm{d}t\big]$。求导时变上下限产生的两项 $\pm u_1(x)u_2(x)f(x)$ 抵消，得 $y'=-\frac1c\big[u_2'\int_a^xu_1f+u_1'\int_x^bu_2f\big]$，再求导：

$$
(py')'=-\frac1c\Big[(pu_2')'\int_a^xu_1f+(pu_1')'\int_x^bu_2f\Big]-\frac1c\,p\,(u_2'u_1-u_1'u_2)f=qy-f,
$$
即 $Ly=f$。又 $y(a)=-\frac1cu_1(a)\int_a^bu_2f=0$，$y(b)=0$ 同理。$\square$

**定义 12.4.2（Green 函数）** 式 (12.11) 中的 $G(x,t)$ 称为边值问题 $Ly=f$，$y(a)=y(b)=0$ 的 **Green 函数**。

Green 函数有以下特征性质，它们也可以用来直接求 $G$：

1. 对固定的 $t$，$G(\cdot,t)$ 在 $x\ne t$ 处满足 $LG=0$，并满足两端的边界条件；
2. $G$ 在 $[a,b]^2$ 上连续，且对称：$G(x,t)=G(t,x)$；
3. $\partial G/\partial x$ 在 $x=t$ 处有跳跃：$\dfrac{\partial G}{\partial x}(t^+,t)-\dfrac{\partial G}{\partial x}(t^-,t)=-\dfrac{1}{p(t)}$。

物理上，$G(x,t)$ 是在 $t$ 处施加单位点力（或点热源）时系统在 $x$ 处的响应，解 $y=\int G f$ 是把分布的外力看成无数点力的叠加；对称性 $G(x,t)=G(t,x)$ 是互易原理。

**例 12.4.3** 求 $-y''=f(x)$，$y(0)=y(1)=0$ 的 Green 函数。

**解** $p=1$，$q=0$，取 $u_1=x$，$u_2=1-x$，$c=x\cdot(-1)-1\cdot(1-x)=-1$，于是

$$
G(x,t)=\begin{cases}t(1-x),&0\le t\le x,\\x(1-t),&x\le t\le1.\end{cases}
$$
例如 $f\equiv1$ 时 $y=\int_0^xt(1-x)\,\mathrm{d}t+\int_x^1x(1-t)\,\mathrm{d}t=\frac{x(1-x)}{2}$，直接验证 $-y''=1$。这里 $G\ge0$：向上的力处处使弦向上弯曲。

![-y'' = f, y(0) = y(1) = 0 的 Green 函数 G(x, t)：几个固定 t 处的折线](./plots/green-function.py)

若齐次问题有非零解 $\varphi$（即 $0$ 是特征值），Green 函数不存在。此时对自伴算子有 Fredholm 二择一（Fredholm alternative）：$Ly=f$ 在边界条件下可解当且仅当 $\int_a^bf\varphi\,\mathrm{d}x=0$，且有解时解相差 $\varphi$ 的任意倍数。例如 $-y''=f$，$y'(0)=y'(1)=0$（$\varphi=1$）可解当且仅当 $\int_0^1f\,\mathrm{d}x=0$：两端绝热的杆，热源的总和必须为零才可能有稳态温度。

## 12.5. Sturm–Liouville 问题

### 12.5.1. 正则 Sturm–Liouville 问题

**定义 12.5.1（Sturm–Liouville 问题）** 设 $p\in C^1[a,b]$，$p>0$，$q,w\in C[a,b]$，$w>0$，实数 $\alpha_1,\alpha_2$ 不全为零，$\beta_1,\beta_2$ 不全为零。含参数 $\lambda$ 的边值问题

$$
-\big(p(x)y'\big)'+q(x)y=\lambda w(x)y,\quad a<x<b,\tag{12.12}
$$

$$
\alpha_1y(a)-\alpha_2y'(a)=0,\qquad\beta_1y(b)+\beta_2y'(b)=0\tag{12.13}
$$
称为**正则 Sturm–Liouville 问题**；使它有非零解的 $\lambda$ 称为特征值，相应的非零解称为特征函数，$w$ 称为权函数。

(12.13) 称为分离型边界条件：每个条件只涉及一个端点。$\alpha_2=0$ 是 Dirichlet 条件，$\alpha_1=0$ 是 Neumann 条件，两者都不为零时称为 Robin 条件（第三类边界条件）。例 12.4.1 是 $p=w=1$，$q=0$ 的特例。区间无界，或 $p$、$w$ 在端点为零时，问题称为奇异的，Legendre 方程、Bessel 方程（[2.4.10](/2.4.10)）都属于此类。

记 $Ly=-(py')'+qy$。对 $u,v\in C^2[a,b]$ 有 Lagrange 恒等式 $vLu-uLv=\frac{\mathrm{d}}{\mathrm{d}x}\big[p(uv'-u'v)\big]$，积分得 Green 公式

$$
\int_a^b(vLu-uLv)\,\mathrm{d}x=\Big[p\,(uv'-u'v)\Big]_a^b.\tag{12.14}
$$
若 $u,v$ 都满足 (12.13)，则在 $x=a$ 处，非零向量 $(\alpha_1,-\alpha_2)$ 是以 $\begin{bmatrix}u(a)&u'(a)\\v(a)&v'(a)\end{bmatrix}$ 为系数矩阵的齐次方程组的解，行列式 $uv'-u'v$ 在 $a$ 处为零；$b$ 处同理。于是 (12.14) 右端为零：

$$
\int_a^b vLu\,\mathrm{d}x=\int_a^b uLv\,\mathrm{d}x.
$$
用内积 $\langle u,v\rangle=\int_a^b uv\,\mathrm{d}x$ 来说，$\langle Lu,v\rangle=\langle u,Lv\rangle$：$L$ 在满足 (12.13) 的函数空间上是对称的。这正是有限维中实对称矩阵（**自伴随算子**）的类比，下面的定理也与"实对称矩阵的特征值是实数、不同特征值的特征向量正交"一一对应。

### 12.5.2. 特征值与特征函数的性质

**定理 12.5.1** 正则 Sturm–Liouville 问题 (12.12)–(12.13) 有以下性质：

1. 特征值都是实数，特征函数可以取为实函数；
2. 每个特征值都是单的：属于同一特征值的特征函数彼此只差常数倍；
3. 属于不同特征值的特征函数关于权 $w$ 正交：$\lambda\ne\mu$ 时 $\int_a^b\varphi_\lambda\varphi_\mu w\,\mathrm{d}x=0$。

**证明** (1) 设 $L\varphi=\lambda w\varphi$，$\varphi$ 可以是复值函数。因为 $p,q,w$ 与边界条件的系数都是实的，$\bar\varphi$ 满足 $L\bar\varphi=\bar\lambda w\bar\varphi$ 和 (12.13)。在 (12.14) 中取 $u=\varphi$，$v=\bar\varphi$：

$$
0=\int_a^b(\bar\varphi L\varphi-\varphi L\bar\varphi)\,\mathrm{d}x=(\lambda-\bar\lambda)\int_a^bw|\varphi|^2\,\mathrm{d}x,
$$
而 $\int w|\varphi|^2>0$，故 $\lambda=\bar\lambda$。此时 $\varphi$ 的实部与虚部都满足方程与边界条件，其中至少一个不恒为零，是实特征函数。

(2) 若 $\varphi,\psi$ 属于同一特征值，由上面的讨论它们的 Wronski 行列式在 $a$ 处为零，而它们是同一个二阶线性方程的解，故线性相关。

(3) 在 (12.14) 中取 $u=\varphi_\lambda$，$v=\varphi_\mu$，得 $(\lambda-\mu)\int_a^b\varphi_\lambda\varphi_\mu w\,\mathrm{d}x=0$。$\square$

**定理 12.5.2** 正则 Sturm–Liouville 问题的特征值构成一个严格递增、趋于 $+\infty$ 的实数列

$$
\lambda_1<\lambda_2<\cdots<\lambda_n<\cdots\to+\infty,
$$
且属于 $\lambda_n$ 的特征函数 $\varphi_n$ 在开区间 $(a,b)$ 内恰有 $n-1$ 个零点。

证明的思路是 Prüfer 变换（§12.3.3）。令 $y=r\sin\theta$，$py'=r\cos\theta$，方程 (12.12) 的角度满足

$$
\theta'=\frac{1}{p}\cos^2\theta+(\lambda w-q)\sin^2\theta,
$$
左端条件确定 $\theta(a)=\alpha\in[0,\pi)$（$\alpha_1\sin\alpha=\frac{\alpha_2}{p(a)}\cos\alpha$），右端条件要求 $\theta(b)$ 等于某个固定角 $\beta\in(0,\pi]$ 加上 $\pi$ 的整数倍。记 $\theta(b;\lambda)$ 为满足 $\theta(a)=\alpha$ 的解在 $b$ 处的值，由比较论证，它关于 $\lambda$ 连续、严格递增，$\lambda\to-\infty$ 时趋于 $0$，$\lambda\to+\infty$ 时趋于 $+\infty$。于是方程 $\theta(b;\lambda)=\beta+(n-1)\pi$ 对每个 $n=1,2,\dots$ 恰有一个解 $\lambda_n$；$\theta$ 在 $(a,b)$ 内穿过 $\pi,2\pi,\dots,(n-1)\pi$ 各一次，正是 $\varphi_n$ 的 $n-1$ 个零点。

第 $n$ 个特征函数恰有 $n-1$ 个零点，这推广了 $\sin nx$ 在 $(0,\pi)$ 内有 $n-1$ 个零点的事实：特征值越大，特征函数振动得越快。下图右侧是变系数问题的数值结果，可以看到同样的规律。

![左：y'' + λ y = 0, y(0) = y(π) = 0 的前四个特征函数 sin nx；右：-((1 + x) y')' = λ y, y(0) = y(1) = 0 的前四个特征函数（数值解），第 n 个有 n - 1 个内部零点](./plots/sl-eigenfunctions.py)

特征值的符号常可由 Rayleigh 商判断。用 $\varphi$ 乘 $L\varphi=\lambda w\varphi$ 并分部积分：

$$
\lambda\int_a^bw\varphi^2\,\mathrm{d}x=\int_a^b\big(p\varphi'^2+q\varphi^2\big)\,\mathrm{d}x-\Big[p\varphi\varphi'\Big]_a^b.
$$
若 $q\ge0$，且 $\alpha_1\alpha_2\ge0$、$\beta_1\beta_2\ge0$，则边界项 $-[p\varphi\varphi']_a^b\ge0$（例如 $\alpha_2\ne0$ 时 $p(a)\varphi(a)\varphi'(a)=p(a)\frac{\alpha_1}{\alpha_2}\varphi(a)^2\ge0$），从而所有特征值 $\lambda\ge0$。Dirichlet 与 Neumann 条件都满足这一要求。

### 12.5.3. 特征函数展开

把特征函数规范化，$\int_a^b\varphi_n^2w\,\mathrm{d}x=1$，则 $\{\varphi_n\}$ 是关于权 $w$ 的规范**正交函数系**。仿照 Fourier 级数，对函数 $f$ 定义

$$
c_n=\int_a^bf(x)\varphi_n(x)w(x)\,\mathrm{d}x,\qquad f\sim\sum_{n=1}^\infty c_n\varphi_n(x).\tag{12.15}
$$
这称为 $f$ 的特征函数展开（eigenfunction expansion），$c_n$ 是 $f$ 在 $\varphi_n$ 上的"坐标"。

**定理 12.5.3（展开定理）** 设 $\{\varphi_n\}$ 是正则 Sturm–Liouville 问题 (12.12)–(12.13) 的规范正交特征函数系。

1. 若 $f\in C^2[a,b]$ 且满足边界条件 (12.13)，则级数 (12.15) 在 $[a,b]$ 上绝对一致收敛于 $f$；
2. 若 $f$ 在 $[a,b]$ 上分段光滑，则级数在 $(a,b)$ 内每一点收敛于 $\frac12\big[f(x^+)+f(x^-)\big]$，与 Fourier 级数的 Dirichlet 定理（[2.2.9](/2.2.9#thm-9.3.1)）相同；
3. 若 $\int_a^bf^2w\,\mathrm{d}x<+\infty$，则级数平方平均收敛于 $f$，并有 Parseval 等式 $\int_a^bf^2w\,\mathrm{d}x=\sum_{n=1}^\infty c_n^2$。

第 3 条说的是特征函数系的完备性：它在平方可积函数空间中是一组"正交基"。证明需要把 $L$ 的逆（以 Green 函数为核的积分算子，§12.4.3）看成紧的对称算子，用其谱定理，这里不展开。取 $[0,\pi]$ 上的 Dirichlet 与 Neumann 问题，定理就是正弦级数与余弦级数的收敛定理。

**例 12.5.1（Legendre 方程）** $\big((1-x^2)y'\big)'+\lambda y=0$，$-1<x<1$，是 $p=1-x^2$ 在两端为零的奇异 Sturm–Liouville 问题，"边界条件"换成在 $x=\pm1$ 处有界。可以证明它恰在 $\lambda=n(n+1)$（$n=0,1,2,\dots$）时有有界解，特征函数为 **Legendre 多项式** $P_n(x)$，于是 $\int_{-1}^1P_mP_n\,\mathrm{d}x=0$（$m\ne n$），区间 $[-1,1]$ 上的函数可以按 Legendre 多项式展开。

**例 12.5.2（Bessel 方程）** 在半径为 $R$ 的圆盘上用极坐标分离变量会得到 $(xy')'+\big(\lambda x-\frac{\nu^2}{x}\big)y=0$，$0<x<R$，$y(R)=0$，$y$ 在 $0$ 处有界。这里 $p=w=x$ 在 $x=0$ 处为零，问题是奇异的。其特征函数为 $J_\nu(\sqrt{\lambda_k}\,x)$，其中 $\sqrt{\lambda_k}R$ 是 $J_\nu$ 的第 $k$ 个正零点；它们关于权 $x$ 正交，由此得到 Fourier–Bessel 展开。

### 12.5.4. 与分离变量法的联系

以两端温度为零、长为 $l$ 的杆的热传导为例：$u_t=u_{xx}$，$u(0,t)=u(l,t)=0$，$u(x,0)=f(x)$。设 $u=X(x)T(t)$，代入得 $\frac{T'}{T}=\frac{X''}{X}=-\lambda$，于是 $X$ 满足 Dirichlet 特征值问题 $X''+\lambda X=0$，$X(0)=X(l)=0$，$\lambda_n=(n\pi/l)^2$，$X_n=\sin\frac{n\pi x}{l}$；而 $T_n=\mathrm{e}^{-\lambda_nt}$。叠加得

$$
u(x,t)=\sum_{n=1}^\infty c_n\mathrm{e}^{-(n\pi/l)^2t}\sin\frac{n\pi x}{l},
$$
初始条件要求 $f=\sum c_n\sin\frac{n\pi x}{l}$，$c_n$ 由特征函数展开 (12.15) 确定。一般的区域、变系数的介质或不同的边界条件，只是把 $\sin\frac{n\pi x}{l}$ 换成相应 Sturm–Liouville 问题的特征函数；定理 12.5.1–12.5.3 保证了这一方法的合理性。详见 [2.5](/2.5)。

## 小结

| 结论 | 内容 | 方法 |
|---|---|---|
| 零点孤立、单零点 | 非零解的零点没有聚点，且 $y'\ne0$ | 唯一性 |
| 分离定理 | 同一方程两个线性无关解的零点交错 | Wronski 行列式不变号 |
| 比较定理 | $Q\le P$ 时，$z''+Qz=0$ 的相邻零点之间有 $y''+Py=0$ 的零点 | 积分恒等式 (12.6) / Picone 恒等式 |
| 零点间距 | $m^2\le Q\le M^2$ ⟹ $\pi/M\le d\le\pi/m$ | 与常系数方程比较 |
| 非振动判别 | 非振动 ⟺ Riccati 不等式 (12.7) 有整体解 | $r=py'/y$ |
| 边值问题 | 齐次问题只有零解 ⟹ 非齐次问题唯一可解，解 $=\int Gf$ | 常数变易法、Green 函数 |
| Sturm–Liouville | 特征值实、单、$\lambda_n\uparrow+\infty$；$\varphi_n$ 有 $n-1$ 个零点；关于权 $w$ 正交且完备 | Green 公式 (12.14)、Prüfer 变换 |
