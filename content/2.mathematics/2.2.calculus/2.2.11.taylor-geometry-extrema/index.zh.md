---
title: Taylor 公式、几何应用与极值
---

上一章的全微分是多元函数的一阶近似。本章沿两个方向使用它：一是几何——一阶近似给出空间曲线的切线与曲面的切平面；二是分析——二阶近似（Taylor 公式）给出极值的判别法，二阶项是一个二次型，极值的类型由 Hesse 矩阵的正定性决定。最后讨论带约束的极值问题，Lagrange 乘子法的理论依据是 [2.2.10](/2.2.10) 的隐函数定理，几何意义是目标函数的等值线与约束曲线相切。

本章与线性代数联系紧密：Hesse 矩阵、**二次型**与**正定矩阵**见 [2.1.7](/2.1.7)（那里的例 7.2.1、例 7.3.1 从矩阵角度讨论了同一问题），最小二乘拟合与**正规方程**见 [2.1.4](/2.1.4)。一元函数的 **Taylor 公式**与极值见 [2.2.5](/2.2.5)。

## 11.1. 预备：向量积、平面与直线

讨论空间曲线与曲面之前，先简要回顾空间解析几何。$\mathbb{R}^3$ 中的向量记作 $\boldsymbol{a}=(a_1,a_2,a_3)$，坐标单位向量为 $\boldsymbol{i},\boldsymbol{j},\boldsymbol{k}$，数量积 $\boldsymbol{a}\cdot\boldsymbol{b}$ 就是标准**内积**。

**定义 11.1.1（向量积）** 向量 $\boldsymbol{a},\boldsymbol{b}\in\mathbb{R}^3$ 的**向量积**（叉积）为

$$
\boldsymbol{a}\times\boldsymbol{b}=\begin{vmatrix}\boldsymbol{i}&\boldsymbol{j}&\boldsymbol{k}\\ a_1&a_2&a_3\\ b_1&b_2&b_3\end{vmatrix}=(a_2b_3-a_3b_2,\ a_3b_1-a_1b_3,\ a_1b_2-a_2b_1).
$$

行列式只是形式记号（按第一行展开）。向量积有以下性质：$\boldsymbol{a}\times\boldsymbol{b}$ 与 $\boldsymbol{a},\boldsymbol{b}$ 都垂直，$\boldsymbol{a},\boldsymbol{b},\boldsymbol{a}\times\boldsymbol{b}$ 构成右手系；$\|\boldsymbol{a}\times\boldsymbol{b}\|=\|\boldsymbol{a}\|\|\boldsymbol{b}\|\sin\theta$ 是以 $\boldsymbol{a},\boldsymbol{b}$ 为邻边的平行四边形的面积；$\boldsymbol{b}\times\boldsymbol{a}=-\boldsymbol{a}\times\boldsymbol{b}$，$\boldsymbol{a}\times\boldsymbol{b}=\boldsymbol{0}$ 当且仅当两者共线；固定 $\boldsymbol{a}$ 时 $\boldsymbol{b}\mapsto\boldsymbol{a}\times\boldsymbol{b}$ 是**线性变换**（[2.1.1](/2.1.1) 中给出了它的表示矩阵）。混合积 $(\boldsymbol{a}\times\boldsymbol{b})\cdot\boldsymbol{c}=\det[\boldsymbol{a}\ \boldsymbol{b}\ \boldsymbol{c}]$（以三向量为行或列），其绝对值是平行六面体的体积，这是**行列式**的几何意义（[2.1.5](/2.1.5)）。

- 平面：过点 $M_0(x_0,y_0,z_0)$、以 $\boldsymbol{n}=(A,B,C)\ne\boldsymbol{0}$ 为法向量的平面（点法式）为 $A(x-x_0)+B(y-y_0)+C(z-z_0)=0$，一般式为 $Ax+By+Cz+D=0$。点 $(x_1,y_1,z_1)$ 到它的距离为 $\dfrac{|Ax_1+By_1+Cz_1+D|}{\sqrt{A^2+B^2+C^2}}$（例 11.6.6 用 Lagrange 乘子法推出）。
- 直线：过 $M_0$、方向向量为 $\boldsymbol{s}=(l,m,n)$ 的直线，参数式为 $(x,y,z)=(x_0,y_0,z_0)+t(l,m,n)$，对称式（标准式）为 $\dfrac{x-x_0}{l}=\dfrac{y-y_0}{m}=\dfrac{z-z_0}{n}$（分母为零时理解为分子为零）。两个平面的交线是一条直线，其方向向量是两个法向量的向量积。
- 两直线（两平面）的夹角由方向向量（法向量）的夹角 $\cos\theta=\dfrac{|\boldsymbol{s}_1\cdot\boldsymbol{s}_2|}{\|\boldsymbol{s}_1\|\|\boldsymbol{s}_2\|}$ 给出。

## 11.2. 多元函数的 Taylor 公式

### 11.2.1. Lagrange 余项的 Taylor 公式

为了简洁地写出高阶项，引入记号

$$
\Big(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y}\Big)f(x_0,y_0)=hf_x(x_0,y_0)+kf_y(x_0,y_0),
$$

$$
\Big(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y}\Big)^lf(x_0,y_0)=\sum_{i=0}^{l}\binom{l}{i}\frac{\partial^lf}{\partial x^i\,\partial y^{l-i}}(x_0,y_0)\,h^ik^{l-i}.
$$

它就是 [2.2.10](/2.2.10) 中的 $l$ 阶全微分 $\mathrm{d}^lf$（取 $\mathrm{d}x=h$，$\mathrm{d}y=k$）。

**定理 11.2.1（二元函数的 Taylor 公式）** 设 $f(x,y)$ 在 $M_0(x_0,y_0)$ 的某邻域内有 $q+1$ 阶连续偏导数，$(x_0+h,y_0+k)$ 属于该邻域，则存在 $\theta\in(0,1)$，使

$$
f(x_0+h,y_0+k)=f(x_0,y_0)+\sum_{l=1}^{q}\frac1{l!}\Big(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y}\Big)^lf(x_0,y_0)+\frac{1}{(q+1)!}\Big(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y}\Big)^{q+1}f(x_0+\theta h,y_0+\theta k).
$$

**证明** 把二元函数限制在连接两点的线段上，化为一元函数。令 $g(t)=f(x_0+th,y_0+tk)$，$t\in[0,1]$。由链式法则 $g'(t)=hf_x+kf_y=\big(h\partial_x+k\partial_y\big)f(x_0+th,y_0+tk)$，归纳可得

$$
g^{(l)}(t)=\Big(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y}\Big)^lf(x_0+th,y_0+tk)\qquad(l\le q+1)
$$

（这里用到混合偏导数与次序无关）。对 $g$ 在 $t=0$ 用一元的带 **Lagrange 余项**的 Taylor 公式并取 $t=1$：$g(1)=\sum_{l=0}^q\frac{g^{(l)}(0)}{l!}+\frac{g^{(q+1)}(\theta)}{(q+1)!}$，即得结论。$\square$

$q=0$ 时得到二元函数的中值定理：$f(x_0+h,y_0+k)-f(x_0,y_0)=hf_x(x_0+\theta h,y_0+\theta k)+kf_y(x_0+\theta h,y_0+\theta k)$。由它可知：若在区域 $D$ 上 $\nabla f\equiv\boldsymbol{0}$，则 $f$ 在 $D$ 上为常数（$D$ 中任两点可以用折线连接，在每段线段上用中值定理）。

### 11.2.2. Peano 余项与唯一性

**定理 11.2.2（Peano 余项）** 设 $f$ 在 $M_0(x_0,y_0)$ 的某邻域内有 $q$ 阶连续偏导数，$\rho=\sqrt{h^2+k^2}$，则

$$
f(x_0+h,y_0+k)=f(x_0,y_0)+\sum_{l=1}^{q}\frac1{l!}\Big(h\frac{\partial}{\partial x}+k\frac{\partial}{\partial y}\Big)^lf(x_0,y_0)+o(\rho^q)\qquad(\rho\to0).
$$

**证明** 由定理 11.2.1（取 $q-1$ 阶，余项为 $q$ 阶导数在中间点的值），余项与 $\frac1{q!}\big(h\partial_x+k\partial_y\big)^qf(x_0,y_0)$ 之差是 $\sum_i\binom{q}{i}h^ik^{q-i}$ 乘以 $q$ 阶偏导数在中间点与在 $M_0$ 之差；后者由连续性趋于 $0$，而 $|h^ik^{q-i}|\le\rho^q$。$\square$

**定理 11.2.3（Taylor 展开的唯一性）** 若

$$
f(x_0+h,y_0+k)=P(h,k)+o(\rho^q),
$$

其中 $P$ 是 $h,k$ 的次数不超过 $q$ 的多项式，则 $P$ 就是 $f$ 在 $M_0$ 的 $q$ 阶 Taylor 多项式。

**证明** 两个展开相减，得到一个次数不超过 $q$ 的多项式 $Q(h,k)=o(\rho^q)$。把 $Q$ 按次数分成齐次部分 $Q=Q_0+Q_1+\cdots+Q_q$。令 $(h,k)\to0$ 得 $Q_0=0$。设 $Q_0=\cdots=Q_{j-1}=0$，对固定的 $(h,k)\ne(0,0)$，$Q_j(th,tk)=t^jQ_j(h,k)$，而 $Q(th,tk)=o(t^j)$（$t\to0^+$），除以 $t^j$ 并令 $t\to0^+$ 得 $Q_j(h,k)=0$。归纳得 $Q\equiv0$。$\square$

唯一性的意义在于：可以用一元函数的已知展开间接求多元函数的 Taylor 展开，而不必逐个计算偏导数。

**例 11.2.1** 求 $f(x,y)=\mathrm{e}^x\ln(1+y)$ 在原点的三阶 Taylor 展开。由 $\mathrm{e}^x=1+x+\frac{x^2}2+O(x^3)$，$\ln(1+y)=y-\frac{y^2}2+\frac{y^3}3+O(y^4)$，相乘并保留三次以下的项：

$$
\mathrm{e}^x\ln(1+y)=y+xy-\frac{y^2}{2}+\frac{x^2y}{2}-\frac{xy^2}{2}+\frac{y^3}{3}+o(\rho^3).
$$

由唯一性，这就是三阶 Taylor 公式，并可读出 $f_{xy}(0,0)=1$，$\frac{1}{3!}\cdot3f_{xxy}(0,0)=\frac12$ 即 $f_{xxy}(0,0)=1$ 等。多项式的 Taylor 展开就是把它按 $x-x_0$、$y-y_0$ 的幂重新整理。

### 11.2.3. $n$ 元函数的二阶 Taylor 公式与 Hesse 矩阵

$n$ 元函数的情形完全类似。记增量 $\boldsymbol{h}=(h_1,\dots,h_n)^{\mathsf T}$，对 $g(t)=f(x_0+t\boldsymbol{h})$ 求两次导数，$g''(t)=\sum_{i,j}f_{x_ix_j}(x_0+t\boldsymbol{h})h_ih_j$。

**定理 11.2.4** 设 $f$ 在 $x_0$ 的某邻域内有二阶连续偏导数，则

$$
f(x_0+\boldsymbol{h})=f(x_0)+\nabla f(x_0)\cdot\boldsymbol{h}+\frac12\boldsymbol{h}^{\mathsf T}H_f(x_0+\theta\boldsymbol{h})\boldsymbol{h},\qquad\theta\in(0,1),
$$

$$
f(x_0+\boldsymbol{h})=f(x_0)+\nabla f(x_0)\cdot\boldsymbol{h}+\frac12\boldsymbol{h}^{\mathsf T}H_f(x_0)\boldsymbol{h}+o(\|\boldsymbol{h}\|^2),
$$

其中 $H_f=\Big[\dfrac{\partial^2f}{\partial x_i\,\partial x_j}\Big]_{n\times n}$ 是 $f$ 的 **Hesse 矩阵**。

由于二阶偏导数连续，$H_f$ 是实对称矩阵，二阶项是 $\boldsymbol{h}$ 的一个**二次型**。对比一元的 $f(x_0+h)=f(x_0)+f'(x_0)h+\frac12f''(x_0)h^2+o(h^2)$：梯度相当于一阶导数，Hesse 矩阵相当于二阶导数（它也是梯度映射 $x\mapsto\nabla f(x)$ 的 Jacobi 矩阵）。线性代数的 [例 7.2.1](/2.1.7#ex-7.2.1) 写出了同一公式。

**例 11.2.2** 设 $f$ 有三阶连续偏导数。用 Taylor 公式估计数值计算中常用的五点差分

$$
\Delta_hf(x,y)=\frac{f(x+h,y)+f(x-h,y)+f(x,y+h)+f(x,y-h)-4f(x,y)}{h^2}
$$

近似 $f_{xx}+f_{yy}$ 的误差。对 $f(x\pm h,y)$ 分别展开到二阶并带三阶 Lagrange 余项，相加时一阶项抵消：$f(x+h,y)+f(x-h,y)=2f+h^2f_{xx}+\frac{h^3}{6}\big[f_{xxx}(x+\theta_1h,y)-f_{xxx}(x-\theta_2h,y)\big]$，$y$ 方向同理。所以

$$
\Delta_hf-(f_{xx}+f_{yy})=\frac{h}{6}\big[f_{xxx}(x+\theta_1h,y)-f_{xxx}(x-\theta_2h,y)+f_{yyy}(x,y+\theta_3h)-f_{yyy}(x,y-\theta_4h)\big],
$$

误差不超过 $\frac{2h}{3}M$，$M$ 是三阶偏导数绝对值的上界（四阶偏导数连续时还可以证明误差是 $O(h^2)$）。

## 11.3. 向量值函数

**定义 11.3.1（向量值函数）** 从区间 $I\subset\mathbb{R}$ 到 $\mathbb{R}^3$（或 $\mathbb{R}^n$）的映射 $\boldsymbol{r}(t)=(x(t),y(t),z(t))$ 称为一元**向量值函数**。若 $\lim\limits_{\Delta t\to0}\dfrac{\boldsymbol{r}(t+\Delta t)-\boldsymbol{r}(t)}{\Delta t}$ 存在，则称它为 $\boldsymbol{r}$ 在 $t$ 的导数，记作 $\boldsymbol{r}'(t)$。

按 [2.2.10](/2.2.10) 定理 10.3.4 的思路，向量值函数的极限、连续、可导都可以逐个分量地判断：$\boldsymbol{r}$ 连续当且仅当 $x,y,z$ 都连续，且 $\boldsymbol{r}'(t)=(x'(t),y'(t),z'(t))$。若 $\boldsymbol{r}(t)$ 是质点的位置，则 $\boldsymbol{r}'(t)$ 是速度，$\boldsymbol{r}''(t)$ 是加速度。

**定理 11.3.1（求导法则）** 设 $\boldsymbol{u}(t),\boldsymbol{v}(t)$ 是可导的向量值函数，$\varphi(t)$ 是可导的数量函数，$c$ 是常数，则

1. $(c\boldsymbol{u})'=c\boldsymbol{u}'$，$(\boldsymbol{u}\pm\boldsymbol{v})'=\boldsymbol{u}'\pm\boldsymbol{v}'$；
2. $(\varphi\boldsymbol{u})'=\varphi'\boldsymbol{u}+\varphi\boldsymbol{u}'$；
3. $(\boldsymbol{u}\cdot\boldsymbol{v})'=\boldsymbol{u}'\cdot\boldsymbol{v}+\boldsymbol{u}\cdot\boldsymbol{v}'$；
4. $(\boldsymbol{u}\times\boldsymbol{v})'=\boldsymbol{u}'\times\boldsymbol{v}+\boldsymbol{u}\times\boldsymbol{v}'$（因子的顺序不能交换）。

**证明** 逐个分量用一元函数的乘积求导法则。例如 3：$(\sum_ku_kv_k)'=\sum_ku_k'v_k+\sum_ku_kv_k'$。4 的第一个分量为 $(u_2v_3-u_3v_2)'=(u_2'v_3-u_3'v_2)+(u_2v_3'-u_3v_2')$，其余同理。$\square$

**定理 11.3.2** 可导的向量值函数 $\boldsymbol{r}(t)$ 的长度为常数，当且仅当 $\boldsymbol{r}(t)\cdot\boldsymbol{r}'(t)\equiv0$。

**证明** $\|\boldsymbol{r}\|^2=\boldsymbol{r}\cdot\boldsymbol{r}$ 为常数，当且仅当 $(\boldsymbol{r}\cdot\boldsymbol{r})'=2\boldsymbol{r}\cdot\boldsymbol{r}'\equiv0$。$\square$

例如做匀速圆周运动的质点，位置向量（从圆心出发）与速度垂直；速率不变的运动中，加速度与速度垂直。

向量值函数的积分也逐个分量地定义：$\displaystyle\int_a^b\boldsymbol{r}(t)\,\mathrm{d}t=\Big(\int_a^bx(t)\,\mathrm{d}t,\int_a^by(t)\,\mathrm{d}t,\int_a^bz(t)\,\mathrm{d}t\Big)$，**微积分基本定理**同样成立。

**例 11.3.1** 质点在时刻 $t$ 的速度为 $\boldsymbol{v}(t)=(\cos t,\sin t,1)$，$t=0$ 时位于 $\boldsymbol{s}(0)=(1,0,2)$，求 $t=\pi$ 时的位置。

$$
\boldsymbol{s}(\pi)=\boldsymbol{s}(0)+\int_0^\pi\boldsymbol{v}(t)\,\mathrm{d}t=(1,0,2)+\big(\sin t,-\cos t,t\big)\Big|_0^\pi=(1,2,2+\pi).
$$

质点的轨迹是一条螺旋线。

## 11.4. 曲线的切线与曲面的切平面

### 11.4.1. 参数曲线的切线与法平面

设空间曲线 $L$ 的参数方程为 $\boldsymbol{r}(t)=(x(t),y(t),z(t))$，$t\in[\alpha,\beta]$，点 $M_0$ 对应 $t_0$。割线方向 $\dfrac{\boldsymbol{r}(t_0+\Delta t)-\boldsymbol{r}(t_0)}{\Delta t}$ 在 $\Delta t\to0$ 时的极限就是 $\boldsymbol{r}'(t_0)$。

**定义 11.4.1（切向量、切线与法平面）** 设 $x,y,z$ 在 $t_0$ 可导且 $\boldsymbol{r}'(t_0)\ne\boldsymbol{0}$。称 $\boldsymbol{r}'(t_0)=(x'(t_0),y'(t_0),z'(t_0))$ 为曲线在 $M_0$ 处的**切向量**，过 $M_0$ 以它为方向向量的直线为切线，过 $M_0$ 以它为法向量的平面为**法平面**：

$$
\frac{x-x_0}{x'(t_0)}=\frac{y-y_0}{y'(t_0)}=\frac{z-z_0}{z'(t_0)},\qquad x'(t_0)(x-x_0)+y'(t_0)(y-y_0)+z'(t_0)(z-z_0)=0.
$$

切向量 $\boldsymbol{r}'(t_0)$ 指向参数增大的方向。若 $\boldsymbol{r}\in C^1$ 且处处 $\boldsymbol{r}'\ne\boldsymbol{0}$，则称曲线为**光滑曲线**，其**弧长**为 $\displaystyle\int_\alpha^\beta\|\boldsymbol{r}'(t)\|\,\mathrm{d}t$。曲线写成 $y=y(x)$、$z=z(x)$ 时，以 $x$ 为参数，切向量为 $(1,y'(x),z'(x))$。

**例 11.4.1** 求螺旋线 $x=a\cos t$，$y=a\sin t$，$z=bt$ 在 $t=\frac\pi4$ 处的切线。切点为 $\Big(\dfrac{a}{\sqrt2},\dfrac{a}{\sqrt2},\dfrac{b\pi}4\Big)$，切向量 $(-a\sin t,a\cos t,b)=\Big(-\dfrac{a}{\sqrt2},\dfrac{a}{\sqrt2},b\Big)$，切线为

$$
\frac{x-a/\sqrt2}{-a/\sqrt2}=\frac{y-a/\sqrt2}{a/\sqrt2}=\frac{z-b\pi/4}{b}.
$$

螺旋线的切向量与 $z$ 轴的夹角 $\gamma$ 满足 $\cos\gamma=\dfrac{b}{\sqrt{a^2+b^2}}$，是常数。

### 11.4.2. 曲面的切平面与法向量

**定义 11.4.2（切平面与法向量）** 设 $M_0$ 是曲面 $S$ 上的点。若曲面上过 $M_0$ 的所有光滑曲线在 $M_0$ 处的切线都位于同一个平面内，则称该平面为 $S$ 在 $M_0$ 处的**切平面**，切平面的法向量称为曲面在 $M_0$ 处的**法向量**，过 $M_0$ 以法向量为方向的直线称为曲面的法线。

对隐式曲面 $F(x,y,z)=0$，设 $F$ 有连续偏导数，$F(M_0)=0$，$\nabla F(M_0)\ne\boldsymbol{0}$。对曲面上过 $M_0$ 的任一光滑曲线 $\boldsymbol{r}(t)$，由 $F(\boldsymbol{r}(t))\equiv0$ 和链式法则得 $\nabla F(M_0)\cdot\boldsymbol{r}'(t_0)=0$。所以所有切线都垂直于 $\nabla F(M_0)$，切平面存在，法向量为 $\boldsymbol{n}=\nabla F(M_0)$：

$$
F_x(M_0)(x-x_0)+F_y(M_0)(y-y_0)+F_z(M_0)(z-z_0)=0.
$$

这也正是"梯度垂直于等值面"：曲面 $F=0$ 是 $F$ 的一个等值面。

对显式曲面 $z=f(x,y)$，令 $F=f(x,y)-z$，法向量为 $\boldsymbol{n}=(f_x,f_y,-1)$，切平面为 $z-z_0=f_x(x_0,y_0)(x-x_0)+f_y(x_0,y_0)(y-y_0)$，这就是 [2.2.10](/2.2.10) 中"微分的几何意义"给出的平面。法线为 $\dfrac{x-x_0}{f_x}=\dfrac{y-y_0}{f_y}=\dfrac{z-z_0}{-1}$。

**例 11.4.2** 求曲面 $z=1-x^2-y^2$ 在点 $(1,2,-4)$ 处的切平面与法线。$z_x=-2x=-2$，$z_y=-2y=-4$，切平面为 $z+4=-2(x-1)-4(y-2)$，即 $2x+4y+z=6$；法线为 $\dfrac{x-1}{2}=\dfrac{y-2}{4}=\dfrac{z+4}{1}$。

![旋转抛物面在一点的切平面（半透明）与法线：曲面在切点附近与切平面的高度差是距离的高阶无穷小](./plots/tangent-plane.py)

**例 11.4.3** 证明球面 $x^2+y^2+z^2=R^2$ 与锥面 $x^2+y^2=a^2z^2$ 正交（在交点处法向量垂直）。两者的法向量分别为 $(2x,2y,2z)$ 与 $(2x,2y,-2a^2z)$，内积为 $4(x^2+y^2-a^2z^2)$，在交点处为零。

### 11.4.3. 两曲面的交线

设曲线 $L$ 由 $F(x,y,z)=0$、$G(x,y,z)=0$ 给出。它同时在两个曲面上，所以它在 $M_0$ 处的切向量同时垂直于 $\nabla F(M_0)$ 与 $\nabla G(M_0)$。当两者不共线时，切向量为

$$
\boldsymbol{\tau}=\nabla F(M_0)\times\nabla G(M_0)=\Big(\det\frac{\partial(F,G)}{\partial(y,z)},\ \det\frac{\partial(F,G)}{\partial(z,x)},\ \det\frac{\partial(F,G)}{\partial(x,y)}\Big)\Big|_{M_0},
$$

切线是两个切平面的交线。$\nabla F\times\nabla G\ne\boldsymbol{0}$ 正是 [2.2.10](/2.2.10) 定理 10.8.3 中某个二阶 Jacobi 行列式不为零的条件，此时曲线在 $M_0$ 附近可以表示为参数曲线。

**例 11.4.4** 求曲线 $x^2+y^2+z^2=6$，$z=x^2+y^2$ 在 $M_0(1,1,2)$ 处的切线。两个法向量为 $(2,2,4)\parallel(1,1,2)$ 与 $(2x,2y,-1)=(2,2,-1)$，

$$
\boldsymbol{\tau}=(1,1,2)\times(2,2,-1)=(-5,5,0)\parallel(1,-1,0),
$$

切线为 $\dfrac{x-1}{1}=\dfrac{y-1}{-1}$，$z=2$。

### 11.4.4. 参数曲面

设曲面由 $\boldsymbol{r}(u,v)=(x(u,v),y(u,v),z(u,v))$ 给出，$M_0$ 对应 $(u_0,v_0)$。固定 $v=v_0$ 得到曲面上的一条 $u$ 曲线，切向量为 $\boldsymbol{r}_u=(x_u,y_u,z_u)$；同理 $v$ 曲线的切向量为 $\boldsymbol{r}_v$。若两者不共线，切平面由它们张成，法向量为

$$
\boldsymbol{n}=\boldsymbol{r}_u\times\boldsymbol{r}_v=\begin{vmatrix}\boldsymbol{i}&\boldsymbol{j}&\boldsymbol{k}\\ x_u&y_u&z_u\\ x_v&y_v&z_v\end{vmatrix}=\Big(\det\frac{\partial(y,z)}{\partial(u,v)},\ \det\frac{\partial(z,x)}{\partial(u,v)},\ \det\frac{\partial(x,y)}{\partial(u,v)}\Big).
$$

$\boldsymbol{r}_u\times\boldsymbol{r}_v\ne\boldsymbol{0}$ 等价于映射 $(u,v)\mapsto\boldsymbol{r}(u,v)$ 的 $3\times2$ Jacobi 矩阵的秩为 $2$。[2.2.13](/2.2.13) 中曲面的面积元就是 $\|\boldsymbol{r}_u\times\boldsymbol{r}_v\|\,\mathrm{d}u\,\mathrm{d}v$。

**例 11.4.5** 求螺旋面 $x=u\cos v$，$y=u\sin v$，$z=v$ 在 $(u_0,v_0)$ 对应点处的切平面。$\boldsymbol{r}_u=(\cos v,\sin v,0)$，$\boldsymbol{r}_v=(-u\sin v,u\cos v,1)$，

$$
\boldsymbol{n}=\boldsymbol{r}_u\times\boldsymbol{r}_v=(\sin v,-\cos v,u),
$$

切平面为 $(x-x_0)\sin v_0-(y-y_0)\cos v_0+u_0(z-z_0)=0$，其中 $(x_0,y_0,z_0)=(u_0\cos v_0,u_0\sin v_0,v_0)$。

四种情形汇总如下：

| 给出方式 | 切向量或法向量 |
|---|---|
| 曲线 $\boldsymbol{r}(t)$ | 切向量 $\boldsymbol{r}'(t_0)$ |
| 曲线 $F=G=0$ | 切向量 $\nabla F\times\nabla G$ |
| 曲面 $z=f(x,y)$ | 法向量 $(f_x,f_y,-1)$ |
| 曲面 $F(x,y,z)=0$ | 法向量 $\nabla F$ |
| 曲面 $\boldsymbol{r}(u,v)$ | 法向量 $\boldsymbol{r}_u\times\boldsymbol{r}_v$ |

## 11.5. 极值

### 11.5.1. 极值的定义与必要条件

**定义 11.5.1（极值）** 设 $f$ 在 $x_0$ 的某邻域 $N(x_0,\delta)$ 内有定义。若对一切 $x\in N(x_0,\delta)$ 有 $f(x)\le f(x_0)$（$f(x)\ge f(x_0)$），则称 $f(x_0)$ 为 $f$ 的**极大值**（**极小值**），$x_0$ 称为**极大值点**（**极小值点**），统称**极值**与**极值点**。

极值是局部性质，极值点必须是定义域的内点。

**定理 11.5.1（极值的必要条件）** 若 $f$ 在 $x_0$ 取得极值，且 $f$ 在 $x_0$ 的偏导数都存在，则 $\nabla f(x_0)=\boldsymbol{0}$，即 $f_{x_1}(x_0)=\cdots=f_{x_n}(x_0)=0$。

**证明** 固定其余变量，一元函数 $x_i\mapsto f(x_1^0,\dots,x_i,\dots,x_n^0)$ 在 $x_i^0$ 取得极值，由一元的 **Fermat 定理**，其导数 $f_{x_i}(x_0)=0$。$\square$

梯度为零的点称为 $f$ 的**驻点**。与一元情形一样，可微的极值点必是驻点，但驻点不一定是极值点，偏导数不存在的点也可能是极值点：$f=\sqrt{x^2+y^2}$ 在原点取极小值，但偏导数不存在。

**定义 11.5.2（鞍点）** 若 $x_0$ 是 $f$ 的驻点，但不是极值点，则称 $x_0$ 为 $f$ 的**鞍点**。

$z=x^2-y^2$ 与 $z=xy$ 的原点都是鞍点：沿某些方向函数增大，沿另一些方向减小，曲面形如马鞍。

### 11.5.2. 极值的充分条件

在驻点处一阶项为零，由定理 11.2.4，$f(x_0+\boldsymbol{h})-f(x_0)\approx\frac12\boldsymbol{h}^{\mathsf T}H_f(x_0)\boldsymbol{h}$，极值的类型由这个二次型的符号决定。

**定理 11.5.2（极值的充分条件）** 设 $f$ 在 $x_0$ 的某邻域内有二阶连续偏导数，$\nabla f(x_0)=\boldsymbol{0}$。

1. 若 $H_f(x_0)$ 是**正定矩阵**，则 $x_0$ 是严格极小值点；
2. 若 $H_f(x_0)$ 是**负定矩阵**，则 $x_0$ 是严格极大值点；
3. 若 $H_f(x_0)$ 是**不定矩阵**，则 $x_0$ 是鞍点。

**证明** 1：由 $H_f(x_0)$ 正定，单位球面上连续函数 $\boldsymbol{e}\mapsto\boldsymbol{e}^{\mathsf T}H_f(x_0)\boldsymbol{e}$ 的最小值 $m>0$（它等于 $H_f(x_0)$ 的最小特征值）。由定理 11.2.4 的 Peano 形式，

$$
f(x_0+\boldsymbol{h})-f(x_0)=\frac12\boldsymbol{h}^{\mathsf T}H_f(x_0)\boldsymbol{h}+o(\|\boldsymbol{h}\|^2)\ge\Big(\frac m2+o(1)\Big)\|\boldsymbol{h}\|^2,
$$

$\|\boldsymbol{h}\|$ 充分小且 $\boldsymbol{h}\ne\boldsymbol{0}$ 时右端为正。2 同理。3：取 $\boldsymbol{e}_1,\boldsymbol{e}_2$ 使 $\boldsymbol{e}_1^{\mathsf T}H\boldsymbol{e}_1>0>\boldsymbol{e}_2^{\mathsf T}H\boldsymbol{e}_2$，则 $f(x_0+t\boldsymbol{e}_1)-f(x_0)=\frac{t^2}2\boldsymbol{e}_1^{\mathsf T}H\boldsymbol{e}_1+o(t^2)>0$，$f(x_0+t\boldsymbol{e}_2)-f(x_0)<0$（$t$ 充分小），所以 $x_0$ 不是极值点。$\square$

正定、负定可以用顺序主子式或特征值判断（[2.1.7](/2.1.7)）。二元情形记 $A=f_{xx}(x_0,y_0)$，$B=f_{xy}(x_0,y_0)$，$C=f_{yy}(x_0,y_0)$，$H=\begin{bmatrix}A&B\\ B&C\end{bmatrix}$，$\det H=AC-B^2$，得到：

**推论 11.5.1** 设二元函数 $f$ 在驻点 $(x_0,y_0)$ 的某邻域内有二阶连续偏导数。

1. $AC-B^2>0$ 且 $A>0$：极小值点；$AC-B^2>0$ 且 $A<0$：极大值点；
2. $AC-B^2<0$：鞍点；
3. $AC-B^2=0$：不能判断。

定理 11.5.2 不包括 $H_f(x_0)$ 半正定或半负定且奇异（$\det H_f(x_0)=0$）的情形。这时二阶项在某些方向上为零，极值性由更高阶的项决定，结论什么都可能发生：

**例 11.5.1** 下列函数以原点为驻点，在原点的 Hesse 矩阵都是奇异的半定矩阵（$\operatorname{diag}(2,0)$、$\operatorname{diag}(0,2)$ 或 $O$）：

1. $f=x^2+y^4$：原点是极小值点；$f=x^2-y^4$：原点是鞍点；$f=-(x^4+y^4)$：原点是极大值点。
2. $f=2x^4-3x^2y+y^2=(y-x^2)(y-2x^2)$。限制在任一过原点的直线上，原点都是极小值点：在坐标轴上 $f=2x^4$ 或 $y^2$；在 $y=kx$（$k\ne0$）上 $g(x)=f(x,kx)=2x^4-3kx^3+k^2x^2$，$g''(0)=2k^2>0$。但在两条抛物线 $y=x^2$ 与 $y=2x^2$ 之间 $f<0$，在其外 $f>0$，原点不是极值点。

第 2 个例子说明，沿每条直线都取极小值的点也可能不是极小值点，这是多元函数与一元函数的又一个差别。

**算法 11.5.1（求二元函数的极值）** 设 $f$ 有二阶连续偏导数。

1. 解方程组 $f_x=0$、$f_y=0$，求出全部驻点；另外列出偏导数不存在的点；
2. 对每个驻点计算 $A,B,C$，按推论 11.5.1 判断；
3. $AC-B^2=0$ 的驻点与偏导数不存在的点，用定义（考察 $f(x)-f(x_0)$ 的符号）判断。

**例 11.5.2** 求 $f(x,y)=x^3+y^3-3xy$ 的极值。由 $f_x=3x^2-3y=0$、$f_y=3y^2-3x=0$ 得驻点 $(0,0)$ 与 $(1,1)$。$f_{xx}=6x$，$f_{xy}=-3$，$f_{yy}=6y$。在 $(0,0)$ 处 $AC-B^2=-9<0$，是鞍点（沿 $y=x$，$f=2x^3-3x^2<0$；沿 $y=-x$，$f=3x^2>0$）；在 $(1,1)$ 处 $AC-B^2=27>0$，$A=6>0$，极小值 $f(1,1)=-1$。

![z = x³ + y³ − 3xy 的曲面与等值线：(1, 1) 是极小值点，原点是鞍点，鞍点附近的等值线交叉成"×"形](./plots/stationary-points.py)

**例 11.5.3** 求 $f(x,y)=2x^4+y^4-2x^2-2y^2$ 的极值。$f_x=8x^3-4x$，$f_y=4y^3-4y$，驻点为 $x\in\{0,\pm\frac1{\sqrt2}\}$ 与 $y\in\{0,\pm1\}$ 的 $9$ 种组合。$f_{xx}=24x^2-4$，$f_{xy}=0$，$f_{yy}=12y^2-4$，$AC-B^2=16(6x^2-1)(3y^2-1)$。

| 驻点 | $AC-B^2$ | $A$ | 结论 |
|---|---|---|---|
| $(0,0)$ | $16$ | $-4$ | 极大值 $0$ |
| $\big(\pm\frac1{\sqrt2},\pm1\big)$（4 个） | $64$ | $8$ | 极小值 $-\frac32$ |
| $(0,\pm1)$、$\big(\pm\frac1{\sqrt2},0\big)$（4 个） | $-32$ | | 鞍点 |

**例 11.5.4** 求由 $x^2-6xy+10y^2-2yz-z^2+18=0$ 确定的隐函数 $z=z(x,y)$ 的极值。对 $x$、$y$ 分别求导：

$$
2x-6y-2yz_x-2zz_x=0,\qquad-6x+20y-2z-2yz_y-2zz_y=0.
$$

令 $z_x=z_y=0$，得 $x=3y$，$z=y$，代入原方程得 $y^2=9$，驻点为 $(9,3)$（$z=3$）与 $(-9,-3)$（$z=-3$）。再求导一次，并代入 $z_x=z_y=0$：

$$
2-2(y+z)z_{xx}=0,\qquad-6-2(y+z)z_{xy}=0,\qquad20-2(y+z)z_{yy}=0
$$

（含 $z_x$、$z_y$ 的项都已消去）。在 $(9,3,3)$ 处 $A=\frac16$，$B=-\frac12$，$C=\frac53$，$AC-B^2=\frac1{36}>0$，$A>0$，故 $z(9,3)=3$ 是极小值；在 $(-9,-3,-3)$ 处 $A=-\frac16$，$B=\frac12$，$C=-\frac53$，故 $z(-9,-3)=-3$ 是极大值。

### 11.5.3. 最小二乘拟合

**例 11.5.5（最小二乘直线）** 给定观测数据 $(x_1,y_1),\dots,(x_n,y_n)$（$x_i$ 不全相等），求 $a,b$ 使 $Q(a,b)=\sum\limits_{i=1}^n\big(y_i-(ax_i+b)\big)^2$ 最小。这是**最小二乘法**的最简单情形。由

$$
Q_a=-2\sum_i\big(y_i-ax_i-b\big)x_i=0,\qquad Q_b=-2\sum_i\big(y_i-ax_i-b\big)=0
$$

得**正规方程**

$$
\begin{bmatrix}\sum x_i^2&\sum x_i\\ \sum x_i&n\end{bmatrix}\begin{bmatrix}a\\ b\end{bmatrix}=\begin{bmatrix}\sum x_iy_i\\ \sum y_i\end{bmatrix},\qquad
a=\frac{n\sum x_iy_i-\sum x_i\sum y_i}{n\sum x_i^2-(\sum x_i)^2},\quad b=\frac{\sum x_i^2\sum y_i-\sum x_i\sum x_iy_i}{n\sum x_i^2-(\sum x_i)^2}.
$$

$Q$ 的 Hesse 矩阵是上面系数矩阵的 $2$ 倍，由 **Cauchy–Schwarz 不等式**，$n\sum x_i^2-(\sum x_i)^2>0$（$x_i$ 不全相等），它是正定的常数矩阵。由 Taylor 公式，$Q(a+h,b+k)-Q(a,b)=\frac12(h,k)H(h,k)^{\mathsf T}>0$ 对一切 $(h,k)\ne\boldsymbol{0}$ 成立，所以唯一的驻点就是最小值点。这与 [2.1.4](/2.1.4) 从正交投影得到的结论一致。指数曲线 $y=a\mathrm{e}^{bx}$ 的拟合可以取对数 $\ln y=\ln a+bx$ 化为直线拟合。

## 11.6. 条件极值与 Lagrange 乘子法

### 11.6.1. 问题与几何意义

许多问题要求在一定条件下求函数的极值，例如求 $f(x,y,z)$ 在曲面 $g(x,y,z)=0$ 上、或在曲线 $g=h=0$ 上的极值。

**定义 11.6.1（条件极值）** 设 $M_0$ 满足约束条件 $g(M_0)=0$。若存在 $M_0$ 的邻域，使对邻域中满足 $g(M)=0$ 的一切点 $M$，有 $f(M)\le f(M_0)$（或 $\ge$），则称 $f(M_0)$ 为 $f$ 在约束 $g=0$ 下的**条件极值**，$f$ 称为目标函数。多个约束同理。

若能从约束中解出一部分变量，代入目标函数，就化为无条件极值（直接法）。例如求 $f=y^2-x^2$ 在椭圆 $\frac{x^2}4+y^2=1$ 上的最值：代入 $y^2=1-\frac{x^2}4$，$g(x)=1-\frac54x^2$，$x\in[-2,2]$，最大值 $g(0)=1$，最小值 $g(\pm2)=-4$。但约束一般不能显式解出，这时用下面的方法。

**引理 11.6.1** 设 $f$ 在 $M_0$ 可微。

1. 若 $M_0$ 在光滑曲线 $L$ 上，$f$ 限制在 $L$ 上时在 $M_0$ 取得极值，则 $\nabla f(M_0)$ 与 $L$ 在 $M_0$ 的切线垂直；
2. 若 $M_0$ 在曲面 $S$ 上，$S$ 在 $M_0$ 有切平面，$f$ 限制在 $S$ 上时在 $M_0$ 取得极值，则 $\nabla f(M_0)$ 与切平面垂直。

**证明** 1：设 $L$ 为 $\boldsymbol{r}(t)$，$\boldsymbol{r}(t_0)=M_0$，则一元函数 $f(\boldsymbol{r}(t))$ 在 $t_0$ 取极值，导数 $\nabla f(M_0)\cdot\boldsymbol{r}'(t_0)=0$。2：对 $S$ 上过 $M_0$ 的每条光滑曲线用 1，而这些曲线的切线张成切平面。$\square$

### 11.6.2. 一个约束条件

**定理 11.6.1（Lagrange 乘子法）** 设 $f,g$ 在 $M_0$ 的某邻域内有连续偏导数，$f$ 在约束 $g=0$ 下在 $M_0$ 取得条件极值，且 $\nabla g(M_0)\ne\boldsymbol{0}$，则存在实数 $\lambda$，使

$$
\nabla f(M_0)=\lambda\nabla g(M_0).
$$

**证明** 以三元函数为例。不妨设 $g_z(M_0)\ne0$，由隐函数定理，约束在 $M_0$ 附近确定 $z=z(x,y)$，曲面 $g=0$ 在 $M_0$ 有切平面，法向量为 $\nabla g(M_0)$。由引理 11.6.1，$\nabla f(M_0)$ 也垂直于该切平面，所以与 $\nabla g(M_0)$ 平行。$\square$

几何上，条件极值点处目标函数的等值面（线）与约束曲面（曲线）相切。若两者在 $M_0$ 处横截相交，沿约束移动就能穿过 $f$ 的等值面，$f$ 的值可增可减，$M_0$ 不是极值点。$\lambda$ 称为 Lagrange 乘子。引入 Lagrange 函数

$$
L(x,y,z,\lambda)=f(x,y,z)-\lambda g(x,y,z),
$$

则定理的结论连同约束本身，恰好是 $L$ 关于全部 $4$ 个变量的驻点方程 $L_x=L_y=L_z=0$、$L_\lambda=-g=0$：条件极值问题化为无条件的驻点问题。

**算法 11.6.1（Lagrange 乘子法）** 求 $f$ 在约束 $g=0$ 下的极值（最值）：

1. 写出 $L=f-\lambda g$，解方程组 $L_x=L_y=L_z=0$，$g=0$，得到可能的条件极值点（同时检查 $\nabla g=\boldsymbol{0}$ 的点）；
2. 判断哪些点是所求的极值点。实际问题中，若由问题的性质知道最值存在（例如约束集是有界闭集，或最值显然在内部取得），而可能的点只有有限个，比较函数值即可。

**例 11.6.1** 求 $f(x,y)=xy$ 在圆 $(x-1)^2+y^2=1$ 上的最值。由 $\nabla f=(y,x)$，$\nabla g=(2(x-1),2y)$，得

$$
y=2\lambda(x-1),\qquad x=2\lambda y,\qquad(x-1)^2+y^2=1.
$$

前两式消去 $\lambda$ 得 $y^2=x(x-1)$，代入约束得 $2x^2-3x=0$。$x=0$ 时 $y=0$，$f=0$；$x=\frac32$ 时 $y=\pm\frac{\sqrt3}2$，$f=\pm\frac{3\sqrt3}{4}$。圆周是有界闭集，最值存在，所以最大值为 $\frac{3\sqrt3}4$，最小值为 $-\frac{3\sqrt3}4$。点 $(0,0)$ 也满足方程组，但不是条件极值点：在它附近圆周可写成 $x=1+\cos t$，$y=\sin t$（$t$ 接近 $\pi$），$f\approx-\frac12(t-\pi)^3$ 变号。

![f = xy 的等值线与约束圆 (x − 1)² + y² = 1：在最大值点与最小值点处等值线与圆相切，∇f 与 ∇g 平行](./plots/lagrange-tangency.py)

**例 11.6.2** 用料最省的长方体盒子：容积为 $a$ 的长方体，表面积 $S=2(xy+yz+zx)$ 何时最小？由 $\nabla S=\lambda\nabla(xyz)$ 得 $2(y+z)=\lambda yz$，$2(x+z)=\lambda xz$，$2(x+y)=\lambda xy$。前两式相减得 $2(y-x)=\lambda z(y-x)$，若 $x\ne y$ 则 $\lambda z=2$，代回第一式得 $2y=0$，矛盾；所以 $x=y$，同理 $y=z$，即 $x=y=z=\sqrt[3]{a}$，正方体用料最省（表面积在 $x,y,z\to0^+$ 或 $\to+\infty$ 时趋于无穷，最小值存在）。

**例 11.6.3** 设 $a>0$，求正数 $x_1,\dots,x_n$ 满足 $\sum x_i=a$ 时乘积 $\prod x_i$ 的最大值。令 $L=\prod x_i-\lambda(\sum x_i-a)$，$L_{x_i}=\prod_{j\ne i}x_j-\lambda=0$，各式乘以 $x_i$ 得 $\prod_jx_j=\lambda x_i$，所以 $x_1=\cdots=x_n=\frac an$，最大值为 $\big(\frac an\big)^n$（乘积在边界 $x_i\to0$ 处趋于 $0$）。于是对任意正数 $x_i$，$\sqrt[n]{x_1\cdots x_n}\le\frac{x_1+\cdots+x_n}{n}$，这就是**算术–几何平均不等式**。

**例 11.6.4（光的折射定律）** 光在空气与水中的速度分别为 $v_1$、$v_2$。光从空气中的点 $A$ 经水面上的点 $C$ 到达水中的点 $B$，设 $A$、$B$ 到水面的距离分别为 $a$、$b$，两点的水平距离为 $c$，入射角为 $\alpha$，折射角为 $\beta$。设光走用时最短的路径，即在约束 $a\tan\alpha+b\tan\beta=c$ 下求 $T=\dfrac{a}{v_1\cos\alpha}+\dfrac{b}{v_2\cos\beta}$ 的最小值。由

$$
\frac{a\sin\alpha}{v_1\cos^2\alpha}=\lambda\frac{a}{\cos^2\alpha},\qquad\frac{b\sin\beta}{v_2\cos^2\beta}=\lambda\frac{b}{\cos^2\beta}
$$

得 $\dfrac{\sin\alpha}{v_1}=\dfrac{\sin\beta}{v_2}$，这就是 Snell 折射定律。

### 11.6.3. 多个约束条件

**定理 11.6.2** 设 $f,g,h$ 在 $M_0$ 附近有连续偏导数，$f$ 在约束 $g=0$、$h=0$ 下在 $M_0$ 取得条件极值，且 $\nabla g(M_0)$ 与 $\nabla h(M_0)$ 不共线，则存在 $\lambda,\mu$，使

$$
\nabla f(M_0)=\lambda\nabla g(M_0)+\mu\nabla h(M_0).
$$

**证明** 约束曲线 $g=h=0$ 在 $M_0$ 处的切向量为 $\boldsymbol{\tau}=\nabla g\times\nabla h\ne\boldsymbol{0}$。由引理 11.6.1，$\nabla f\cdot\boldsymbol{\tau}=0$，即 $\nabla f$ 位于与 $\boldsymbol{\tau}$ 垂直的平面内，而该平面由 $\nabla g,\nabla h$ 张成。$\square$

一般地，$n$ 元函数在 $m$ 个约束 $g_1=\cdots=g_m=0$（$m<n$）下的条件极值点 $M_0$ 处，若约束的 $m\times n$ Jacobi 矩阵 $\dfrac{\partial(g_1,\dots,g_m)}{\partial(x_1,\dots,x_n)}$ **满秩**（各 $\nabla g_i$ 线性无关），则存在 $\lambda_1,\dots,\lambda_m$ 使 $\nabla f=\sum\lambda_i\nabla g_i$。证明的思路是：由隐函数定理用 $n-m$ 个变量表示其余 $m$ 个变量，对复合后的无约束函数用必要条件，再把乘子解出来。Lagrange 函数为 $L=f-\sum_i\lambda_ig_i$。

**例 11.6.5** 求 $f=xyz$ 在直线 $x+y+z=30$，$x+y-z=0$ 上的最大值。由 $\nabla f=\lambda(1,1,1)+\mu(1,1,-1)$ 得 $yz=xz=\lambda+\mu$，所以 $z(x-y)=0$。若 $z=0$，由约束得 $x+y=30$ 且 $x+y=0$，矛盾；故 $x=y$，解得 $z=15$，$x=y=\frac{15}2$，$f_{\max}=\frac{3375}4$。（也可直接把直线参数化验证：$f=15x(15-x)$。）

**例 11.6.6（点到平面的距离）** 求 $P_0(x_0,y_0,z_0)$ 到平面 $Ax+By+Cz+D=0$ 的距离。在约束下最小化 $d^2=(x-x_0)^2+(y-y_0)^2+(z-z_0)^2$：

$$
2(x-x_0)=\lambda A,\qquad 2(y-y_0)=\lambda B,\qquad 2(z-z_0)=\lambda C.
$$

三式分别乘以 $A,B,C$ 相加，利用 $Ax+By+Cz=-D$，得 $\lambda=-\dfrac{2(Ax_0+By_0+Cz_0+D)}{A^2+B^2+C^2}$，于是

$$
d=\frac{|\lambda|}{2}\sqrt{A^2+B^2+C^2}=\frac{|Ax_0+By_0+Cz_0+D|}{\sqrt{A^2+B^2+C^2}}.
$$

**例 11.6.7** 抛物面 $z=x^2+y^2$ 被平面 $x+y+z=1$ 截成一个椭圆，求椭圆上的点到原点的最长与最短距离。令

$$
L=x^2+y^2+z^2-\lambda_1(z-x^2-y^2)-\lambda_2(x+y+z-1),
$$

$L_x=2x+2\lambda_1x-\lambda_2=0$，$L_y=2y+2\lambda_1y-\lambda_2=0$，相减得 $(1+\lambda_1)(x-y)=0$。若 $\lambda_1=-1$，则 $\lambda_2=0$，由 $L_z=2z+1=0$ 得 $z=-\frac12<0$，与 $z=x^2+y^2$ 矛盾。所以 $x=y$，代入两约束得 $2x^2+2x-1=0$，$x=y=\frac{-1\pm\sqrt3}2$，$z=2\mp\sqrt3$。距离平方 $d^2=x^2+y^2+z^2=z+z^2=9\mp5\sqrt3$，所以最长距离为 $\sqrt{9+5\sqrt3}$，最短距离为 $\sqrt{9-5\sqrt3}$。

## 11.7. 有界闭区域上的最值

由最大最小值定理，有界闭区域 $D$ 上的连续函数一定有最大值与最小值。最值若在内部取得，则必是极值点；若在边界上取得，则是 $f$ 限制在边界上的条件极值点。

**算法 11.7.1（有界闭区域上的最值）** 设 $f$ 在有界闭区域 $D$ 上连续。

1. 求 $D$ 内部的驻点与偏导数不存在的点；
2. 求 $f$ 在边界 $\partial D$ 上的可能最值点：边界由方程给出时用 Lagrange 乘子法或参数化，边界由几段组成时还要加上各段的端点（角点）；
3. 比较以上各点的函数值，最大者为最大值，最小者为最小值。不必判断这些点是否为极值点。

**例 11.7.1** 求 $z=x^2+y^2-12x+16y$ 在 $x^2+y^2\le25$ 上的最值。驻点 $(6,-8)$ 在区域外。边界上令 $L=z-\lambda(x^2+y^2-25)$，$2x-12=2\lambda x$，$2y+16=2\lambda y$，得 $y=-\frac43x$，代入约束得 $(3,-4)$ 与 $(-3,4)$。$z(3,-4)=-75$，$z(-3,4)=125$，所以最大值 $125$，最小值 $-75$。也可以把 $z=25-12x+16y$ 看作边界上的线性函数，由 Cauchy–Schwarz 不等式直接得到。

**例 11.7.2** 在以 $P_1(0,0)$、$P_2(1,0)$、$P_3(0,1)$ 为顶点的闭三角形上，求到三个顶点距离平方和最大、最小的点。目标函数 $z=3x^2+3y^2-2x-2y+2$。内部驻点为重心 $M_0\big(\frac13,\frac13\big)$；边 $P_1P_2$（$y=0$）上 $z=3x^2-2x+2$，驻点 $\big(\frac13,0\big)$；边 $P_1P_3$ 上驻点 $\big(0,\frac13\big)$；边 $P_2P_3$（$y=1-x$）上 $z=6x^2-6x+3$，驻点 $\big(\frac12,\frac12\big)$。连同三个顶点比较：

| 点 | $P_1$ | $P_2$、$P_3$ | $M_0$ | $\big(\frac13,0\big)$、$\big(0,\frac13\big)$ | $\big(\frac12,\frac12\big)$ |
|---|---|---|---|---|---|
| $z$ | $2$ | $3$ | $\frac43$ | $\frac53$ | $\frac32$ |

最大值 $3$ 在 $P_2$、$P_3$ 取得，最小值 $\frac43$ 在重心取得。

一元函数在区间上若只有一个极值点，它必是最值点（否则函数在别处更小，中间必有另一个极值点）。多元函数没有这一结论：

**例 11.7.3** $f(x,y)=3(x^2+y^2)-x^3$ 的驻点为 $(0,0)$ 与 $(2,0)$。在 $(0,0)$ 处 $A=C=6$，$B=0$，是极小值点；在 $(2,0)$ 处 $A=-6$，$C=6$，是鞍点。所以 $(0,0)$ 是 $f$ 唯一的极值点，而且是极小值点。但在 $D=\{x^2+y^2\le16\}$ 的边界上 $f=48-x^3$，$f(4,0)=-16<f(0,0)=0$。比较 $f(0,0)=0$、$f(2,0)=4$、边界上的 $f(4,0)=-16$ 与 $f(-4,0)=112$，最大值为 $112$，最小值为 $-16$，都在边界上取得。直观地说，函数可以从极小值点出发"绕过"鞍点下降到别处，平面上的路径比直线上多。

## 小结

| 问题 | 方法 | 要点 |
|---|---|---|
| 曲线的切线 | $\boldsymbol{r}'(t_0)$，或 $\nabla F\times\nabla G$ | 切向量非零 |
| 曲面的切平面 | $\nabla F$，$(f_x,f_y,-1)$，$\boldsymbol{r}_u\times\boldsymbol{r}_v$ | 梯度垂直于等值面 |
| Taylor 公式 | $g(t)=f(x_0+t\boldsymbol{h})$ 化为一元 | 二阶项 $\frac12\boldsymbol{h}^{\mathsf T}H_f\boldsymbol{h}$；展开唯一 |
| 无条件极值 | $\nabla f=\boldsymbol{0}$，再看 $H_f$ | 正定极小、负定极大、不定鞍点，半定且奇异时不定 |
| 条件极值 | $\nabla f=\sum\lambda_i\nabla g_i$，$g_i=0$ | 约束的 Jacobi 矩阵满秩；等值面与约束相切 |
| 闭区域上的最值 | 内部驻点、不可微点、边界上的条件驻点、角点 | 比较函数值；唯一极值点未必是最值点 |

| 二元极值判别（驻点处） | $AC-B^2>0$ | $AC-B^2<0$ | $AC-B^2=0$ |
|---|---|---|---|
| 结论 | $A>0$ 极小，$A<0$ 极大 | 鞍点 | 需进一步判断 |
