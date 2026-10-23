---
title: 质点运动学
description: 参考系与质点模型；位矢、位移、速度与加速度；匀加速运动与抛体；自然坐标系中的切向与法向加速度，圆周运动的角量；平面极坐标系；相对运动与 Galilei 速度变换。
---

力学研究物体的机械运动，即物体位置随时间的变化。本章是力学的第一步：运动学（kinematics）只描述运动本身——物体在什么时刻处于什么位置、运动得多快、速度怎样变化——而不追问运动变化的原因；原因（力）是下一章 [5.1.2](/5.1.2) 的主题。描述运动的语言是矢量和**向量值函数**的微积分：位置是时间的矢量函数，速度和加速度是它的一阶、二阶导数（[2.2.11](/2.2.11)）；矢量代数中的**内积**与**向量积**（[2.2.11](/2.2.11#def-11.1.1)）在本章和后面各章中随处可见。本章依次讨论参考系与质点模型、直角坐标系中的描述、匀加速运动、自然坐标系与圆周运动、平面极坐标系，最后讨论不同参考系之间的速度变换，它在 [5.1.8](/5.1.8) 中将被相对论修正。

## 1.1. 参考系

### 1.1.1. 运动的相对性

同一个物体的运动，在不同的观察者看来可能完全不同：车厢里静止的乘客，在地面上看来在高速运动。描述运动必须先说明"相对于什么"。

**定义 1.1.1（参考系）** 为描述物体的运动而选作参照的物体或物体系称为**参考系**。

运动学中参考系可以任意选取，物体的运动形式随参考系而不同，这就是运动的相对性。常用的参考系有：

- 太阳参考系（以太阳中心为原点、坐标轴指向遥远恒星）；
- 地心参考系（以地心为原点、坐标轴指向遥远恒星，不随地球自转）；
- 地面参考系（实验室参考系），固结在地面上；
- 质心参考系，见 [5.1.3](/5.1.3)。

为了定量描述运动，要在参考系上固结一个坐标系。参考系选定之后坐标系仍可任选，不同坐标系中运动的数学表述不同，但描述的是同一个运动。本章用到三种坐标系：

| 坐标系 | 坐标 | 单位矢量 | 适用情形 |
|---|---|---|---|
| 直角坐标系 | $x, y, z$ | $\boldsymbol{e}_x, \boldsymbol{e}_y, \boldsymbol{e}_z$，不随时间变化 | 加速度为常矢量，如抛体 |
| 平面极坐标系 | $r, \theta$ | $\boldsymbol{e}_r, \boldsymbol{e}_\theta$，随质点位置变化 | 加速度指向定点，如行星绕太阳运动 |
| 自然坐标系 | 路程 $s$ | $\boldsymbol{e}_{\mathrm{t}}, \boldsymbol{e}_{\mathrm{n}}$，随质点位置变化 | 轨迹已知，如圆周运动 |

### 1.1.2. 平动、转动与质点模型

物体运动时，若其中任意两点的连线始终保持平行，就称物体做平动（translation）。平动物体内各点的轨迹形状完全相同，只是彼此平移，因此可以用其中一个点的运动代表整个物体。物体绕某个固定轴或瞬时轴旋转时，各点的运动状态不同，不能用一个点代表；转动描述的是一个质点集合的运动，留到刚体一章 [5.1.5](/5.1.5) 讨论。

**定义 1.1.2（质点）** 只考虑物体的质量和位置、忽略其大小和形状时，把物体看作一个有质量的几何点，称为**质点**。

质点是理想模型。物体能否看作质点取决于所研究的问题：物体的尺寸远小于它的运动范围时（研究地球绕太阳公转），或者物体只做平动时，都可以把它看作质点；研究地球自转时就不能。形状规则、运动缓慢都不是判据。

### 1.1.3. 平动参考系与转动参考系

参考系本身也可以运动。固结在参考系上的坐标框架方位始终不变的，称为平动参考系；坐标框架随时间转动的，称为转动参考系。平动参考系的原点可以沿曲线运动：只考虑公转、忽略自转的飞船就是一个平动参考系，它的坐标轴始终指向固定的方向。在转动的圆盘上固结的坐标系则是转动参考系。两类参考系之间的变换见 1.7 节与 [5.1.2](/5.1.2)。

## 1.2. 质点的运动函数

在参考系中选定原点 $O$，并配备一套同步的时钟，就可以给出质点位置与时间的函数关系。

**定义 1.2.1（位置矢量）** 从原点 $O$ 指向质点所在位置 $P$ 的矢量 $\boldsymbol{r} = \overrightarrow{OP}$ 称为质点的**位置矢量**，简称**位矢**。位矢随时间变化的函数

$$
\boldsymbol{r} = \boldsymbol{r}(t) = x(t)\,\boldsymbol{e}_x + y(t)\,\boldsymbol{e}_y + z(t)\,\boldsymbol{e}_z
$$
称为质点的运动函数（运动方程）。

运动函数是一个**向量值函数**。从三个分量式中消去 $t$，得到质点轨迹满足的方程，称为轨道方程。运动函数比轨道方程包含更多的信息：它不仅给出质点走过的路径，还给出质点何时到达路径上的每一点，由它可以求出速度和加速度。

## 1.3. 位移、速度、加速度

### 1.3.1. 位移与路程

**定义 1.3.1（位移）** 质点在 $t$ 到 $t + \Delta t$ 时间内位矢的改变量

$$
\Delta\boldsymbol{r} = \boldsymbol{r}(t + \Delta t) - \boldsymbol{r}(t)
$$
称为这段时间内的**位移**。它的大小 $\lvert\Delta\boldsymbol{r}\rvert$ 等于起点 $P_1$ 到终点 $P_2$ 的直线距离，方向由 $P_1$ 指向 $P_2$。

质点沿轨迹实际经过的长度称为路程，记作 $\Delta s$。要分清三个量：

- $\Delta\boldsymbol{r}$ 是矢量；$\lvert\Delta\boldsymbol{r}\rvert$ 是位移的大小；$\Delta r = \lvert\boldsymbol{r}(t+\Delta t)\rvert - \lvert\boldsymbol{r}(t)\rvert$ 是位矢大小的改变量，即质点到原点距离的变化。一般 $\lvert\Delta\boldsymbol{r}\rvert \ne \Delta r$：质点绕原点做圆周运动时 $\Delta r = 0$，而位移不为零。
- 一般 $\Delta s \ge \lvert\Delta\boldsymbol{r}\rvert$，弦不长于弧；但对无限小的过程 $\mathrm{d}s = \lvert\mathrm{d}\boldsymbol{r}\rvert$（**弧长**的微分），而 $\lvert\mathrm{d}\boldsymbol{r}\rvert \ne \mathrm{d}r$ 仍然成立。

### 1.3.2. 速度与速率

**定义 1.3.2（速度）** 位移与所用时间之比 $\bar{\boldsymbol{v}} = \Delta\boldsymbol{r}/\Delta t$ 称为平均速度；$\Delta t \to 0$ 时的极限

$$
\boldsymbol{v} = \lim_{\Delta t\to0}\frac{\Delta\boldsymbol{r}}{\Delta t} = \frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t} = \dot{\boldsymbol{r}}
$$
称为质点在时刻 $t$ 的（瞬时）**速度**。

速度是位矢的导数，方向沿轨迹在该点的切线、指向运动的前方（**切向量**，[2.2.11](/2.2.11#def-11.4.1)）。

**定义 1.3.3（速率）** 速度的大小称为**速率**：

$$
v = \lvert\boldsymbol{v}\rvert = \frac{\lvert\mathrm{d}\boldsymbol{r}\rvert}{\mathrm{d}t} = \frac{\mathrm{d}s}{\mathrm{d}t}.
$$

注意 $v \ne \dfrac{\mathrm{d}r}{\mathrm{d}t}$：后者只是质点到原点的距离的变化率（1.6 节中的径向速度）。

### 1.3.3. 加速度

**定义 1.3.4（加速度）** 速度对时间的变化率

$$
\boldsymbol{a} = \lim_{\Delta t\to0}\frac{\Delta\boldsymbol{v}}{\Delta t} = \frac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t} = \frac{\mathrm{d}^2\boldsymbol{r}}{\mathrm{d}t^2} = \ddot{\boldsymbol{r}}
$$
称为质点的**加速度**。

加速度的方向是速度变化 $\mathrm{d}\boldsymbol{v}$ 的方向，一般不沿轨迹的切线，而是指向轨迹弯曲的内侧（1.5 节）。同样要注意 $a = \lvert\boldsymbol{a}\rvert = \Big\lvert\dfrac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t}\Big\rvert \ne \dfrac{\mathrm{d}v}{\mathrm{d}t}$：匀速率圆周运动中速率不变，加速度却不为零。

速度、加速度的单位分别是 $\mathrm{m\,s^{-1}}$ 与 $\mathrm{m\,s^{-2}}$。

### 1.3.4. 直角坐标系中的描述

直角坐标系的单位矢量 $\boldsymbol{e}_x, \boldsymbol{e}_y, \boldsymbol{e}_z$ 不随时间变化，所以求导只作用在分量上：

$$
\boldsymbol{v} = \dot{x}\,\boldsymbol{e}_x + \dot{y}\,\boldsymbol{e}_y + \dot{z}\,\boldsymbol{e}_z, \qquad
\boldsymbol{a} = \ddot{x}\,\boldsymbol{e}_x + \ddot{y}\,\boldsymbol{e}_y + \ddot{z}\,\boldsymbol{e}_z,
$$

$$
v = \sqrt{v_x^2 + v_y^2 + v_z^2}, \qquad \mathrm{d}s = \lvert\mathrm{d}\boldsymbol{r}\rvert = \sqrt{(\mathrm{d}x)^2 + (\mathrm{d}y)^2 + (\mathrm{d}z)^2}.
$$

各分量的运动彼此独立：$x$ 方向的运动只由 $a_x$ 和 $x$ 方向的初始条件决定。因此，复杂的运动可以分解为三个方向上的直线运动分别求解，再合成。这一独立性是直角坐标系独有的；在单位矢量随位置变化的坐标系中，分量之间互相牵连（1.6 节）。

### 1.3.5. 运动学的两类问题

运动学的问题分为两类：

1. 已知运动函数 $\boldsymbol{r}(t)$，逐次求导得到 $\boldsymbol{v}(t)$ 与 $\boldsymbol{a}(t)$；
2. 已知加速度 $\boldsymbol{a}(t)$ 以及初始条件 $\boldsymbol{r}(t_0) = \boldsymbol{r}_0$、$\boldsymbol{v}(t_0) = \boldsymbol{v}_0$，积分求出 $\boldsymbol{v}(t)$ 与 $\boldsymbol{r}(t)$：

$$
\boldsymbol{v}(t) = \boldsymbol{v}_0 + \int_{t_0}^{t}\boldsymbol{a}(t')\,\mathrm{d}t', \qquad
\boldsymbol{r}(t) = \boldsymbol{r}_0 + \int_{t_0}^{t}\boldsymbol{v}(t')\,\mathrm{d}t'.
$$

动力学（[5.1.2](/5.1.2)）由受力给出加速度，所以第二类问题是力学的主要问题；加速度依赖于位置和速度时，它就成为一个**常微分方程**的初值问题。矢量形式便于作一般性的陈述，定量计算则要选定坐标系（1.1.1 节的表）。

**注 1.3.1（矢量函数的求导）** 矢量函数的和、数乘、内积与向量积的求导法则见 [2.2.11](/2.2.11#thm-11.3.1)，其中向量积的因子顺序不能交换。把矢量写成大小与方向的乘积 $\boldsymbol{A} = A\,\boldsymbol{e}_A$（$\boldsymbol{e}_A$ 是 $\boldsymbol{A}$ 方向的单位矢量），则

$$
\frac{\mathrm{d}\boldsymbol{A}}{\mathrm{d}t} = \frac{\mathrm{d}A}{\mathrm{d}t}\,\boldsymbol{e}_A + A\,\frac{\mathrm{d}\boldsymbol{e}_A}{\mathrm{d}t}.
$$
由于 $\boldsymbol{e}_A$ 的长度恒为 1，$\dfrac{\mathrm{d}\boldsymbol{e}_A}{\mathrm{d}t} \perp \boldsymbol{e}_A$（[2.2.11](/2.2.11#thm-11.3.2)）。所以矢量的变化总是由两部分组成：沿自身方向的部分来自大小的变化，垂直于自身的部分来自方向的变化。1.5 节的切向加速度与法向加速度正是这一分解。后面还常用到两个恒等式（展开分量即可验证）：

$$
\boldsymbol{A}\cdot(\boldsymbol{B}\times\boldsymbol{C}) = \boldsymbol{B}\cdot(\boldsymbol{C}\times\boldsymbol{A}) = \boldsymbol{C}\cdot(\boldsymbol{A}\times\boldsymbol{B}), \qquad
\boldsymbol{A}\times(\boldsymbol{B}\times\boldsymbol{C}) = \boldsymbol{B}(\boldsymbol{A}\cdot\boldsymbol{C}) - \boldsymbol{C}(\boldsymbol{A}\cdot\boldsymbol{B}).
$$
前者是混合积，等于以 $\boldsymbol{A}, \boldsymbol{B}, \boldsymbol{C}$ 为棱的平行六面体的有向体积，即三者分量构成的**行列式**；后者是二重向量积的展开式。

## 1.4. 匀加速运动

### 1.4.1. 一般公式

加速度为常矢量 $\boldsymbol{a}$ 时，取 $t_0 = 0$，对 $\mathrm{d}\boldsymbol{v} = \boldsymbol{a}\,\mathrm{d}t$ 与 $\mathrm{d}\boldsymbol{r} = \boldsymbol{v}\,\mathrm{d}t$ 依次积分：

$$
\boldsymbol{v} = \boldsymbol{v}_0 + \boldsymbol{a}t, \qquad \boldsymbol{r} = \boldsymbol{r}_0 + \boldsymbol{v}_0 t + \frac12\boldsymbol{a}t^2.
$$

运动发生在过 $\boldsymbol{r}_0$、由 $\boldsymbol{v}_0$ 与 $\boldsymbol{a}$ 张成的平面内。按 $\boldsymbol{v}_0$ 与 $\boldsymbol{a}$ 是否共线，分为直线运动与抛体运动两种情形。

### 1.4.2. 匀加速直线运动

$\boldsymbol{v}_0$ 与 $\boldsymbol{a}$ 共线（或 $\boldsymbol{v}_0 = \boldsymbol{0}$）时，运动是一维的：

$$
v = v_0 + at, \qquad x = x_0 + v_0 t + \frac12 at^2, \qquad v^2 - v_0^2 = 2a(x - x_0).
$$

**例 1.4.1** 蹦极跳台高 $55\,\mathrm{m}$。若把人看作初速度为零的自由落体，下落 $55\,\mathrm{m}$ 时的速率为 $v = \sqrt{2gh} = \sqrt{2 \times 9.8 \times 55}\,\mathrm{m\,s^{-1}} \approx 33\,\mathrm{m\,s^{-1}}$。这是速率的上限：实际的绳索在下落到底之前就开始拉伸减速，空气阻力也使速率更小。

实际的落体还受空气阻力。阻力随速率增大，下落足够久后与重力平衡，物体最终匀速下落，这个速率称为收尾速率；雨滴的收尾速率在每秒数米的量级（大雨滴约 $9\,\mathrm{m\,s^{-1}}$）。收尾速率的计算属于动力学，见 [5.1.2](/5.1.2) 的例 2.5.3。

### 1.4.3. 抛体运动

忽略空气阻力时，抛体的加速度为重力加速度 $\boldsymbol{g}$，与初速度不共线。取 $x$ 轴水平、$y$ 轴竖直向上，初速度 $v_0$ 与水平面成仰角 $\theta$，抛出点为原点。由分量的独立性，水平方向是匀速运动，竖直方向是匀加速运动：

$$
x = v_0\cos\theta\,t, \qquad y = v_0\sin\theta\,t - \frac12 gt^2.
$$

- 到达最高点时 $v_y = v_0\sin\theta - gt = 0$，所以 $t = \dfrac{v_0\sin\theta}{g}$，最大高度 $y_{\max} = \dfrac{v_0^2\sin^2\theta}{2g}$。
- 落回原高度时的水平射程为 $\dfrac{v_0^2\sin2\theta}{g}$，$\theta = 45^\circ$ 时最大。
- 消去 $t$ 得轨道方程

$$
y = x\tan\theta - \frac{g x^2}{2v_0^2\cos^2\theta},
$$
这是一条抛物线。

![初速率相同、仰角不同的抛体轨迹（忽略空气阻力），圆点是最高点；虚线是所有轨迹的包络 $y = \frac{v_0^2}{2g} - \frac{g x^2}{2 v_0^2}$，以此初速率能到达的点都在它下方](./plots/projectile-trajectories.py)

对给定的 $x$，让轨道方程中的 $y$ 对 $\tan\theta$ 取最大值，得 $\tan\theta = \dfrac{v_0^2}{gx}$，代回即得图中的包络线（安全抛物线）。实际的子弹和炮弹受空气阻力很大，轨迹明显偏离抛物线（见 [5.1.2](/5.1.2) 的数值解）；远程弹道导弹则在重力加速度的大小和方向都显著变化的范围内运动。但这些问题的出发点都是上面的运动学。

**例 1.4.2** 瞄准树上的苹果开枪，子弹出膛的瞬间苹果恰好开始自由下落。忽略空气阻力，只要苹果落地之前子弹能飞到它的水平位置，子弹就能击中苹果。以自由下落的苹果为参考系最容易看出：在这个参考系中子弹和苹果的加速度都是 $\boldsymbol{g} - \boldsymbol{g} = \boldsymbol{0}$，子弹沿瞄准线做匀速直线运动，苹果静止在瞄准线上。

## 1.5. 自然坐标系与圆周运动

### 1.5.1. 自然坐标系

轨迹已知时，用质点沿轨迹走过的路程描述它的位置最为直接。

**定义 1.5.1（自然坐标系）** 在已知轨迹上取一点为起点，用质点沿轨迹到起点的路程 $s(t)$ 作为坐标；在质点所在位置取两个单位矢量：切向单位矢量 $\boldsymbol{e}_{\mathrm{t}}$ 沿轨迹切线指向 $s$ 增加的方向，法向单位矢量 $\boldsymbol{e}_{\mathrm{n}}$ 垂直于切线、指向轨迹的曲率中心。这样的坐标系称为**自然坐标系**。

$\boldsymbol{e}_{\mathrm{t}}$、$\boldsymbol{e}_{\mathrm{n}}$ 固结在质点所在位置上，随质点的位置（因而随时间）改变方向，这是它与直角坐标系的根本区别。速度沿切线，

$$
\boldsymbol{v} = v\,\boldsymbol{e}_{\mathrm{t}}, \qquad v = \frac{\mathrm{d}s}{\mathrm{d}t}.
$$

求加速度时，$\boldsymbol{e}_{\mathrm{t}}$ 也要求导（注 1.3.1）：

$$
\boldsymbol{a} = \frac{\mathrm{d}v}{\mathrm{d}t}\,\boldsymbol{e}_{\mathrm{t}} + v\,\frac{\mathrm{d}\boldsymbol{e}_{\mathrm{t}}}{\mathrm{d}t}.
$$

设质点走过 $\mathrm{d}s$ 时切线转过角度 $\mathrm{d}\varphi$。$\mathrm{d}\boldsymbol{e}_{\mathrm{t}}$ 的大小为 $\lvert\boldsymbol{e}_{\mathrm{t}}\rvert\,\mathrm{d}\varphi = \mathrm{d}\varphi$，方向垂直于 $\boldsymbol{e}_{\mathrm{t}}$ 并指向轨迹弯曲的一侧，即 $\boldsymbol{e}_{\mathrm{n}}$。按**曲率**的定义 $\dfrac{\mathrm{d}\varphi}{\mathrm{d}s} = \dfrac1\rho$（$\rho$ 是**曲率半径**，[2.2.7](/2.2.7#def-7.5.3)），

$$
\frac{\mathrm{d}\boldsymbol{e}_{\mathrm{t}}}{\mathrm{d}t} = \frac{\mathrm{d}\varphi}{\mathrm{d}s}\frac{\mathrm{d}s}{\mathrm{d}t}\,\boldsymbol{e}_{\mathrm{n}} = \frac{v}{\rho}\,\boldsymbol{e}_{\mathrm{n}},
\qquad\text{所以}\qquad
\boldsymbol{a} = \frac{\mathrm{d}v}{\mathrm{d}t}\,\boldsymbol{e}_{\mathrm{t}} + \frac{v^2}{\rho}\,\boldsymbol{e}_{\mathrm{n}}.
$$

**定义 1.5.2（切向加速度与法向加速度）** 加速度沿切向的分量 $\boldsymbol{a}_{\mathrm{t}} = \dfrac{\mathrm{d}v}{\mathrm{d}t}\,\boldsymbol{e}_{\mathrm{t}}$ 称为**切向加速度**，沿法向的分量 $\boldsymbol{a}_{\mathrm{n}} = \dfrac{v^2}{\rho}\,\boldsymbol{e}_{\mathrm{n}}$ 称为**法向加速度**。

切向加速度描述速率的变化：$\boldsymbol{a}_{\mathrm{t}}$ 与 $\boldsymbol{v}$ 同向时质点加快，反向时减慢。法向加速度描述速度方向的变化，总是指向轨迹弯曲的内侧，所以加速度不可能指向轨迹的外侧。自然坐标系最直接地反映运动的特征，物理图像清晰，适用于轨迹已知的情形。

**例 1.5.1** 求抛体轨迹最高点处的曲率半径。最高点处速度水平、大小为 $v_0\cos\theta$，重力加速度竖直向下，正好沿法向，切向加速度为零。由 $a_{\mathrm{n}} = g = \dfrac{v^2}{\rho}$ 得

$$
\rho = \frac{v_0^2\cos^2\theta}{g}.
$$
同理，在抛出点 $a_{\mathrm{n}} = g\cos\theta$，$\rho = \dfrac{v_0^2}{g\cos\theta}$。这种由运动学求曲率半径的方法，比直接对轨道方程用曲率公式简便得多。

**例 1.5.2（电子能量分析器）** 半球形电子能量分析器由两个同心的半球形电极组成，两极之间的电场给进入其中的电子提供指向球心的加速度。设在中心半径 $R_0$ 处这一加速度为 $a_0$。电子以速率 $v_0$ 沿切向射入时，只有满足 $\dfrac{v_0^2}{R_0} = a_0$ 的电子才能沿半径为 $R_0$ 的圆周运动、从出口狭缝射出；速率更大的电子所需的向心加速度更大，偏向外侧电极，速率更小的偏向内侧。于是分析器只让一定能量的电子通过，调节两极的电压就可以扫描电子的能谱。电场的具体分布见电磁学部分 [5.3.1](/5.3.1)。

### 1.5.2. 圆周运动的角量

质点做半径为 $R$ 的圆周运动时，用位矢与参考方向的夹角 $\theta(t)$ 描述它的位置，路程 $s = R\theta$。

有限大小的角位移不是矢量：两次有限转动的结果与先后顺序有关（把一本书先绕 $x$ 轴、再绕 $y$ 轴各转 $90^\circ$，与先绕 $y$ 轴、再绕 $x$ 轴的结果不同），不满足矢量加法的交换律。用矩阵的语言说，三维空间的旋转由**正交矩阵**表示（[2.1.4](/2.1.4)），矩阵乘法一般不可交换。但无限小转动的合成与顺序无关（差别是二阶小量），所以角速度可以定义为矢量。

**定义 1.5.3（角速度）** 设质点在 $\mathrm{d}t$ 时间内绕轴转过角度 $\mathrm{d}\theta$。矢量 $\boldsymbol{\omega}$ 称为**角速度**：其大小为 $\omega = \dfrac{\mathrm{d}\theta}{\mathrm{d}t}$，方向沿转轴，与转动方向成右手螺旋关系（右手四指顺着转动方向弯曲，拇指的指向）。

**定义 1.5.4（角加速度）** 角速度对时间的变化率 $\boldsymbol{\alpha} = \dfrac{\mathrm{d}\boldsymbol{\omega}}{\mathrm{d}t}$ 称为**角加速度**。

绕固定轴转动时 $\boldsymbol{\omega}$ 的方向不变，$\alpha = \dfrac{\mathrm{d}\omega}{\mathrm{d}t} = \dfrac{\mathrm{d}^2\theta}{\mathrm{d}t^2}$。角速度的单位是 $\mathrm{rad\,s^{-1}}$（弧度是量纲一的单位，常写作 $\mathrm{s^{-1}}$）。

取原点在转轴上，质点的速度为

$$
\boldsymbol{v} = \boldsymbol{\omega}\times\boldsymbol{r}, \qquad v = \frac{\mathrm{d}s}{\mathrm{d}t} = R\frac{\mathrm{d}\theta}{\mathrm{d}t} = R\omega.
$$
更一般地，任何长度不变、以角速度 $\boldsymbol{\omega}$ 转动的矢量 $\boldsymbol{A}$ 都满足 $\dfrac{\mathrm{d}\boldsymbol{A}}{\mathrm{d}t} = \boldsymbol{\omega}\times\boldsymbol{A}$；这一关系在 [5.1.2](/5.1.2) 的转动参考系与 [5.1.5](/5.1.5) 的刚体中反复使用。

对圆周运动，$\boldsymbol{e}_{\mathrm{t}}$、$\boldsymbol{e}_{\mathrm{n}}$ 只是角 $\theta$ 的函数。$\theta$ 增加 $\Delta\theta$ 时，$\boldsymbol{e}_{\mathrm{t}}$ 转过同一角度，$\lvert\Delta\boldsymbol{e}_{\mathrm{t}}\rvert \approx \Delta\theta$，方向趋于 $\boldsymbol{e}_{\mathrm{n}}$，于是

$$
\frac{\mathrm{d}\boldsymbol{e}_{\mathrm{t}}}{\mathrm{d}\theta} = \boldsymbol{e}_{\mathrm{n}}, \qquad \frac{\mathrm{d}\boldsymbol{e}_{\mathrm{n}}}{\mathrm{d}\theta} = -\boldsymbol{e}_{\mathrm{t}}, \qquad
\frac{\mathrm{d}\boldsymbol{e}_{\mathrm{t}}}{\mathrm{d}t} = \frac{\mathrm{d}\boldsymbol{e}_{\mathrm{t}}}{\mathrm{d}\theta}\frac{\mathrm{d}\theta}{\mathrm{d}t} = \omega\,\boldsymbol{e}_{\mathrm{n}} = \frac{v}{R}\,\boldsymbol{e}_{\mathrm{n}},
$$
从而 $\boldsymbol{a} = \dfrac{\mathrm{d}v}{\mathrm{d}t}\,\boldsymbol{e}_{\mathrm{t}} + \dfrac{v^2}{R}\,\boldsymbol{e}_{\mathrm{n}}$，这是 1.5.1 节一般公式在 $\rho = R$ 时的特例。圆周运动的法向加速度指向圆心，又称向心加速度。

**公式 1.5.1（角量与线量的关系）** 半径为 $R$ 的圆周运动中，

$$
v = R\omega, \qquad a_{\mathrm{t}} = R\alpha, \qquad a_{\mathrm{n}} = \frac{v^2}{R} = R\omega^2.
$$
用矢量表示（原点在转轴上）：$\boldsymbol{a} = \boldsymbol{\alpha}\times\boldsymbol{r} + \boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r})$，其中 $\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\boldsymbol{r}) = -\omega^2\boldsymbol{r}_\perp$，$\boldsymbol{r}_\perp$ 是从转轴垂直指向质点的矢量。

这组关系在刚体的定轴转动（[5.1.5](/5.1.5)）中要反复使用：刚体上各点的角量相同，线量与到转轴的距离成正比。

## 1.6. 平面极坐标系

**定义 1.6.1（平面极坐标系）** 在平面内取极点 $O$ 与极轴，质点的位置用到极点的距离 $r$ 与极角 $\theta$（从极轴逆时针为正）描述。在质点所在位置取径向单位矢量 $\boldsymbol{e}_r$（指向 $r$ 增加的方向）与横向单位矢量 $\boldsymbol{e}_\theta$（指向 $\theta$ 增加的方向）。

这就是**极坐标**（[2.2.7](/2.2.7)）配上随位置变化的单位矢量。$\boldsymbol{e}_r = \cos\theta\,\boldsymbol{e}_x + \sin\theta\,\boldsymbol{e}_y$，$\boldsymbol{e}_\theta = -\sin\theta\,\boldsymbol{e}_x + \cos\theta\,\boldsymbol{e}_y$ 只依赖于 $\theta$，与 $r$ 无关，直接求导得

$$
\frac{\mathrm{d}\boldsymbol{e}_r}{\mathrm{d}\theta} = \boldsymbol{e}_\theta, \qquad \frac{\mathrm{d}\boldsymbol{e}_\theta}{\mathrm{d}\theta} = -\boldsymbol{e}_r.
$$

位矢 $\boldsymbol{r} = r\,\boldsymbol{e}_r$。对时间求导，用链式法则 $\dfrac{\mathrm{d}\boldsymbol{e}_r}{\mathrm{d}t} = \dot\theta\,\boldsymbol{e}_\theta$、$\dfrac{\mathrm{d}\boldsymbol{e}_\theta}{\mathrm{d}t} = -\dot\theta\,\boldsymbol{e}_r$：

$$
\boldsymbol{v} = \dot r\,\boldsymbol{e}_r + r\dot\theta\,\boldsymbol{e}_\theta, \qquad
\boldsymbol{a} = (\ddot r - r\dot\theta^2)\,\boldsymbol{e}_r + (r\ddot\theta + 2\dot r\dot\theta)\,\boldsymbol{e}_\theta.
$$

速度的两个分量 $v_r = \dot r$、$v_\theta = r\dot\theta$ 分别称为径向速度与横向速度。与直角坐标不同，这两个正交的分运动在描述上并不独立：横向速度中含有 $r$，加速度的每个分量都同时含有 $r$ 与 $\theta$ 的导数。加速度的横向分量可以写成 $a_\theta = \dfrac1r\dfrac{\mathrm{d}}{\mathrm{d}t}(r^2\dot\theta)$，所以加速度始终指向极点的运动（有心力作用下的运动）中 $r^2\dot\theta$ 守恒，这就是 [5.1.3](/5.1.3) 的 Kepler 第二定律。$r$ 为常数时，上式退化为圆周运动的结果 $\boldsymbol{a} = -r\dot\theta^2\boldsymbol{e}_r + r\ddot\theta\,\boldsymbol{e}_\theta$。

**例 1.6.1** 岸上的绞车以恒定速率 $v_0$ 收绳，拉动水面上的船。滑轮 $O$ 高出水面 $h$，求绳与竖直方向成 $\theta$ 角时船的速率。

以滑轮 $O$ 为极点建立极坐标，$r$ 为滑轮到船的绳长。收绳使 $\dot r = -v_0$，即 $v_r = -v_0$。由几何关系 $\cos\theta = h/r$，两边对时间求导：

$$
-\sin\theta\,\dot\theta = -\frac{h}{r^2}\dot r \quad\Longrightarrow\quad v_\theta = r\dot\theta = \frac{h\dot r}{r\sin\theta} = -\frac{\cos\theta}{\sin\theta}\,v_0,
$$

$$
v = \sqrt{v_r^2 + v_\theta^2} = \frac{v_0}{\sin\theta}.
$$
船的速度水平，它沿绳方向的分量等于收绳速率 $v_0$，所以 $v\sin\theta = v_0$，船比绳走得快，靠岸时越来越快。常见的错误是把收绳速度当作船速的一个分量，得到 $v = v_0\sin\theta$。

## 1.7. 相对运动

### 1.7.1. 绝对运动、相对运动与牵连运动

在不同参考系中观察同一质点的运动，结果之间有什么关系？

**定义 1.7.1（绝对运动、相对运动与牵连运动）** 取两个参考系，称其中一个为静止参考系 $S$，另一个为运动参考系 $S'$。质点相对 $S$ 的运动称为绝对运动，速度 $\boldsymbol{v}$ 称为**绝对速度**；质点相对 $S'$ 的运动称为相对运动，速度 $\boldsymbol{v}'$ 称为**相对速度**；$S'$ 相对 $S$ 的运动称为牵连运动，$S'$ 中与质点重合的那一点相对 $S$ 的速度 $\boldsymbol{u}$ 称为**牵连速度**。

"静止"与"运动"只是相对的称呼，两个参考系的地位是平等的。下面先讨论 $S'$ 相对 $S$ 平动的情形，此时 $S'$ 上各点的速度相同，牵连速度就是 $S'$ 的原点 $O'$ 的速度。

### 1.7.2. Galilei 速度变换

设 $O'$ 相对 $O$ 的位矢为 $\boldsymbol{r}_0$，质点相对 $O$、$O'$ 的位矢分别为 $\boldsymbol{r}$、$\boldsymbol{r}'$，则 $\boldsymbol{r} = \boldsymbol{r}' + \boldsymbol{r}_0$。对时间求导得到：

**定理 1.7.1（Galilei 速度变换）** 运动参考系 $S'$ 相对 $S$ 平动，牵连速度为 $\boldsymbol{u} = \dot{\boldsymbol{r}}_0$、牵连加速度为 $\boldsymbol{a}_0 = \dot{\boldsymbol{u}}$ 时，

$$
\boldsymbol{v} = \boldsymbol{v}' + \boldsymbol{u}, \qquad \boldsymbol{a} = \boldsymbol{a}' + \boldsymbol{a}_0.
$$
特别地，$S'$ 相对 $S$ 做匀速直线运动时 $\boldsymbol{a} = \boldsymbol{a}'$：两个参考系中测得的加速度相同。

几点说明：

1. 这些关系以经典的绝对时空观为前提。位矢的关系 $\boldsymbol{r} = \boldsymbol{r}' + \boldsymbol{r}_0$ 假定了长度的测量与参考系无关（空间的绝对性）；再对 $t$ 求导得到速度与加速度的关系，假定了两个参考系用同一个时间 $t = t'$（时间的绝对性）。在 $u \ll c$（$c$ 为真空中的光速）时它们是极好的近似，$u$ 接近 $c$ 时要换成 [5.1.8](/5.1.8) 的相对论速度变换。
2. 不要把速度的合成与分解和 Galilei 速度变换混为一谈。前者是在同一个参考系中把一个矢量写成几个矢量之和，总是成立的；后者联系两个参考系中的测量结果，只在低速时近似成立。
3. $S'$ 相对 $S$ 平动时，牵连速度 $\boldsymbol{u}$ 与牵连加速度 $\boldsymbol{a}_0$ 与质点在 $S'$ 中的位置无关。若 $S'$ 相对 $S$ 匀速转动，则 $\boldsymbol{u} = \boldsymbol{\omega}\times\boldsymbol{r}$ 与质点的位置有关；速度变换 $\boldsymbol{v} = \boldsymbol{v}' + \boldsymbol{u}$ 仍然成立，但加速度变换中除牵连加速度外，还要增加一项 Coriolis 加速度 $2\boldsymbol{\omega}\times\boldsymbol{v}'$。它的来历和物理效应见 [5.1.2](/5.1.2) 的 2.6 节。

**例 1.7.1** 雨滴竖直下落，骑车人只在胸前铺一块塑料布就能遮雨。设雨滴相对地面的速度为 $\boldsymbol{v}_{\mathrm{R}}$（竖直向下），人相对地面的速度为 $\boldsymbol{v}_{\mathrm{B}}$（水平向前）。以人为运动参考系，牵连速度就是 $\boldsymbol{v}_{\mathrm{B}}$，雨滴相对人的速度为

$$
\boldsymbol{v}' = \boldsymbol{v}_{\mathrm{R}} - \boldsymbol{v}_{\mathrm{B}},
$$
它斜向后下方、与竖直方向成 $\arctan(v_{\mathrm{B}}/v_{\mathrm{R}})$ 角。在人看来雨是迎面斜着打来的，所以挡住胸前即可。

**例 1.7.2** 半径为 $R$ 的轮子在水平面上做无滑滚动：任意时刻轮与地面的接触点 $P$ 相对地面的速度为零。轮心 $C$ 相对地面的速度为 $\boldsymbol{v}_C$。（1）证明 $P$ 点相对轮心的速度为 $-\boldsymbol{v}_C$；（2）求轮缘上任一点 $A$ 相对地面的速度，$A$ 的位置用 $\theta = \angle ACP$ 表示。

（1）以随轮心平动的参考系为 $S'$，牵连速度为 $\boldsymbol{v}_C$。由 Galilei 速度变换，$P$ 相对地面的速度 $\boldsymbol{v}_P = \boldsymbol{v}'_P + \boldsymbol{v}_C$；无滑条件 $\boldsymbol{v}_P = \boldsymbol{0}$，所以 $\boldsymbol{v}'_P = -\boldsymbol{v}_C$。

（2）在 $S'$ 中轮子绕 $C$ 做圆周运动，由（1），轮缘上各点相对 $C$ 的速率都是 $v_C$，即角速度 $\omega = v_C/R$。$A$ 相对 $C$ 的速度 $\boldsymbol{v}'_A$ 大小为 $v_C$、垂直于 $CA$，于是 $\boldsymbol{v}_A = \boldsymbol{v}'_A + \boldsymbol{v}_C$ 是两个大小都为 $v_C$、夹角为 $\pi - \theta$ 的矢量之和，

$$
v_A = 2v_C\sin\frac{\theta}{2}.
$$
另一种解法以 $P$ 为参考点：$P$ 瞬时静止，轮子在这一瞬间相当于绕 $P$ 转动（$P$ 是瞬时转动中心，见 [5.1.5](/5.1.5)），角速度仍为 $\omega = v_C/R$，所以 $v_A = \omega\cdot\overline{PA} = \dfrac{v_C}{R}\cdot 2R\sin\dfrac\theta2$，方向垂直于 $PA$。最高点（$\theta = \pi$）的速率为 $2v_C$，接触点为零。

![无滑滚动的轮缘上一点的轨迹是摆线。图中画出某一时刻轮缘上各点的速度（箭头，按比例缩短），它们都垂直于该点与接触点 P 的连线，大小与到 P 的距离成正比](./plots/cycloid-velocities.py)

## 小结

| 内容 | 要点 |
|---|---|
| 两类问题 | $\boldsymbol{r}(t) \xrightarrow{\text{求导}} \boldsymbol{v}(t) \xrightarrow{\text{求导}} \boldsymbol{a}(t)$；由 $\boldsymbol{a}$ 与初始条件 $\boldsymbol{r}_0$、$\boldsymbol{v}_0$ 积分求运动 |
| 直角坐标系 | 单位矢量不变，各分量独立；匀加速运动 $\boldsymbol{r} = \boldsymbol{r}_0 + \boldsymbol{v}_0t + \frac12\boldsymbol{a}t^2$ |
| 自然坐标系 | $\boldsymbol{a} = \dfrac{\mathrm{d}v}{\mathrm{d}t}\boldsymbol{e}_{\mathrm{t}} + \dfrac{v^2}{\rho}\boldsymbol{e}_{\mathrm{n}}$：切向改变速率，法向改变方向 |
| 圆周运动 | $\omega = \dot\theta$，$\alpha = \dot\omega$；$v = R\omega$，$a_{\mathrm{t}} = R\alpha$，$a_{\mathrm{n}} = R\omega^2$ |
| 平面极坐标系 | $\boldsymbol{v} = \dot r\boldsymbol{e}_r + r\dot\theta\boldsymbol{e}_\theta$；$\boldsymbol{a} = (\ddot r - r\dot\theta^2)\boldsymbol{e}_r + (r\ddot\theta + 2\dot r\dot\theta)\boldsymbol{e}_\theta$ |
| 相对运动 | 平动参考系之间 $\boldsymbol{v} = \boldsymbol{v}' + \boldsymbol{u}$，$\boldsymbol{a} = \boldsymbol{a}' + \boldsymbol{a}_0$；以绝对时空观为前提，只在低速时成立 |

## 思考题

1. 质点在平面内运动，$x = x(t)$，$y = y(t)$。有人先求 $r = \sqrt{x^2 + y^2}$，再用 $v = \dot r$、$a = \ddot r$ 求速率与加速度的大小；也有人用 $v = \sqrt{\dot x^2 + \dot y^2}$、$a = \sqrt{\ddot x^2 + \ddot y^2}$。哪种方法正确？

   **答** 第二种正确。$\dot r$ 只是径向速度，漏掉了横向速度 $r\dot\theta$；$\ddot r$ 也不是加速度的大小（1.6 节）。

2. 质点某一时刻的速度为 $\boldsymbol{v}$，它的加速度可以指向哪些方向？

   **答** 只给定一个时刻的速度，加速度可以指向任何方向。加速度在 $\boldsymbol{v}$ 方向上的分量决定速率的增减，垂直于 $\boldsymbol{v}$ 的分量决定轨迹向哪一侧弯曲、弯曲得多厉害（$\rho = v^2/a_{\mathrm{n}}$）。反过来，若已知这一点附近的轨迹，加速度就不能指向轨迹弯曲的外侧。

3. 行星沿椭圆轨道运动，加速度始终指向太阳所在的焦点。行星从远日点向近日点运动时速率增大还是减小？

   **答** 加速度在速度方向上的投影就是切向加速度。从远日点到近日点，行星与太阳的距离减小，速度与指向太阳的加速度成锐角，速率增大；反之减小。

4. 圆周运动中质点的加速度是否一定垂直于速度？

   **答** 不一定。只有匀速率圆周运动的切向加速度为零，加速度才指向圆心。
