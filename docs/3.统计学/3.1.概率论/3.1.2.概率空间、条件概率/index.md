## 2.1 概率空间

### 2.1.1 事件域（$\sigma$-代数）

**定义**：设$\Omega$是样本空间，$\mathcal{F}$表示$\Omega$的某些子集构成的集合，如果$\mathcal{F}$满足：
1. $\Omega \in \mathcal{F}$
2. 如果 $A \in \mathcal{F}$，则 $A^c \in \mathcal{F}$
3. 如果 $A_n \in \mathcal{F}$，$n=1,2,\ldots$，则 $\bigcup_{n=1}^\infty A_n \in \mathcal{F}$

称$\mathcal{F}$是$\Omega$上的**事件域**或**$\sigma$-代数**，称$(\Omega,\mathcal{F})$是**可测空间**。

**注**：
- $\mathcal{F}$中每一个事件都是可以分配概率的
- $\Omega$的任意子集未必是事件，只有$\mathcal{F}$中的元素才能称之为事件
- $\mathcal{F}$对集合的各类可列交并补运算都是封闭的

### 2.1.2 事件域的构造示例
- 平凡$\sigma$-代数：$\mathcal{F} = \{\Omega, \emptyset\}$
- 最大$\sigma$-代数：$\mathcal{F} = \{\Omega\}$的所有子集
- 由$A$生成的最小$\sigma$-代数：$\mathcal{F} = \{\Omega, \emptyset, A, A^c\}$

### 2.1.3 概率测度

**定义**：设$(\Omega, \mathcal{F})$是可测空间，$\mathbb{P}$是定义在$\mathcal{F}$上的函数，如果满足：
1. **非负性**：对任意的$A \in \mathcal{F}, \mathbb{P}(A) \geq 0$
2. **归一化**：$\mathbb{P}(\Omega) = 1$
3. **可列可加性**：对于互不相交的事件$A_1, A_2, ...,$，有
   $$
   \mathbb{P} \left( \bigcup_{n=1}^{\infty} A_n \right) = \sum_{n=1}^{\infty} \mathbb{P}(A_n)
   $$

称$\mathbb{P}$为概率测度，称$(\Omega, \mathcal{F}, \mathbb{P})$为**概率空间**。

### 2.1.4 概率空间示例
1. **掷硬币**：$\Omega = \{H, T\}, \mathcal{F} = \{\Omega, \emptyset, \{H\}, \{T\}\}$
2. **掷骰子**：$\Omega = \{1, 2, ..., 6\}, \mathcal{F} = 2^\Omega$（幂集）
3. **反复掷硬币**：$\Omega = \{T^n H: n \geq 0\} \cup \{T^\infty\}$

## 2.2 概率的连续性

### 2.2.1 单调序列
- **单调增序列**：$A_1 \subset A_2 \subset \cdots$，则$\lim_{n \to \infty} A_n = \bigcup_{i=1}^{\infty} A_i$
- **单调减序列**：$A_1 \supset A_2 \supset \cdots$，则$\lim_{n \to \infty} A_n = \bigcap_{i=1}^{\infty} A_i$

### 2.2.2 连续性定理
如果$\{A_i\}$是单调增序列，则
$$
\mathbb{P} (\lim_{n \to \infty} A_n) = \lim_{n \to \infty} \mathbb{P} (A_n)
$$
如果$\{B_j\}$是单调减序列，则
$$
\mathbb{P} (\lim_{n \to \infty} B_n) = \lim_{n \to \infty} \mathbb{P} (B_n)
$$

### 2.2.3 上下极限
- **上极限**：
  $$
  \limsup_{n \to \infty} A_n = \bigcap_{n=1}^{\infty} \bigcup_{k=n}^{\infty} A_k = \{\omega \in \Omega: \omega\text{属于无穷多个}A_i\}
  $$
- **下极限**：
  $$
  \liminf_{n \to \infty} A_n = \bigcup_{n=1}^{\infty} \bigcap_{k=n}^{\infty} A_k = \{\omega \in \Omega: \omega\text{属于所有的}A_i\text{除了有限个之外}\}
  $$

### 2.2.4 Borel-Cantelli引理
设$\{A_n\}$是事件列：
1. 如果$\sum_{n=1}^{\infty} \mathbb{P}(A_n) < \infty$，则$\mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = 0$
2. 如果$\{A_n\}$相互独立且$\sum_{n=1}^{\infty} \mathbb{P}(A_n) = \infty$，则$\mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = 1$

**应用**：抛掷硬币无穷多次，以概率1会有无穷多次正面出现。

## 2.3 条件概率

### 2.3.1 定义
设$(\Omega, \mathcal{F}, \mathbb{P})$是概率空间，$A, B \in \mathcal{F}$，且$\mathbb{P}(A) > 0$，则
$$
\mathbb{P}(B|A) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(A)}
$$

### 2.3.2 条件概率的性质
- $\mathbb{P}(B|A) \geq 0$
- $\mathbb{P}(\Omega|A) = 1$
- 对互不相容的事件列$\{B_i\}$，有$\mathbb{P}(\cup_{i=1}^{\infty} B_i | A) = \sum_{i=1}^{\infty} \mathbb{P}(B_i | A)$

**结论**：$(\Omega, \mathcal{F}, \mathbb{P}_A)$也是一个概率空间，其中$\mathbb{P}_A(\cdot) = \mathbb{P}(\cdot | A)$

### 2.3.3 条件概率vs无条件概率
- 当$B \subset A$时，$\mathbb{P}(B|A) = \frac{\mathbb{P}(B)}{\mathbb{P}(A)} \geq \mathbb{P}(B)$
- 当$A \cap B = \emptyset$时，$\mathbb{P}(B|A) = 0 \leq \mathbb{P}(B)$
- 一般情况下大小关系不确定

## 2.4 乘法公式

### 2.4.1 定理
设$A_i \in \mathcal{F}$，$i = 1, ..., n$，且$\mathbb{P}(A_1 \cap A_2 \cap ... \cap A_{n-1}) > 0$，则
$$
\mathbb{P} \left( \bigcap_{i=1}^n A_i \right) = \mathbb{P}(A_1) \prod_{i=2}^n \mathbb{P}(A_i | A_1 \cap A_2 \cap ... \cap A_{i-1})
$$

### 2.4.2 序贯树形图计算法
1. 设立序贯树形图，关心的事件处于末端
2. 在路径的每个分枝上写相应的条件概率
3. 叶子事件的概率是相应分枝条件概率的乘积

### 2.4.3 应用：配对问题
$n$封信装入$n$个信封，每个信封任意写地址：
- 至少一个信封地址正确的概率：
  $$
  \mathbb{P} \left( \bigcup_{i=1}^n A_i \right) = 1 - \frac{1}{2!} + \frac{1}{3!} - \cdots + (-1)^{n-1} \frac{1}{n!}
  $$
- 当$n \to \infty$时，$q_0 \approx e^{-1}$

## 2.5 全概率公式

### 2.5.1 定理
设$\{A_i\}$是$\Omega$的一个分割，且$\mathbb{P}(A_i) > 0$，则
$$
\mathbb{P}(B) = \sum_{i=1}^n \mathbb{P}(A_i)\mathbb{P}(B|A_i)
$$

特别地，当$0 < \mathbb{P}(A) < 1$时：
$$
\mathbb{P}(B) = \mathbb{P}(A)\mathbb{P}(B|A) + \mathbb{P}(A^c)\mathbb{P}(B|A^c)
$$

### 2.5.2 应用：无放回抽样
袋中有$n$个白球与$m$个黑球，无放回连续抽取$k$个球，第$k$次取得黑球的概率：
$$
\mathbb{P}(A_k) = \frac{m}{n+m}
$$
**结论**：无论抽取顺序如何，每次抽到黑球的概率都等于初始黑球比例。

### 2.5.3 应用：敏感问题调查
为估计敏感问题比例$p$，使用随机化回答技术：
$$
p_1 = q_0 + (p_0 - q_0)p \quad \Rightarrow \quad p = \frac{p_1 - q_0}{p_0 - q_0}
$$
其中$p_0$为红球比例，$q_0 = 1-p_0$为白球比例。

## 2.6 贝叶斯法则

### 2.6.1 定理
设$\{A_i\}$是$\Omega$的一个分割，且$\mathbb{P}(B) > 0$，$\mathbb{P}(A_i) > 0$，则
$$
\mathbb{P}(A_i|B) = \frac{\mathbb{P}(A_i)\mathbb{P}(B|A_i)}{\sum_{j=1}^n \mathbb{P}(A_j)\mathbb{P}(B|A_j)}, \quad i = 1, ..., n
$$

特别地：
$$
\mathbb{P}(A|B) = \frac{\mathbb{P}(A)\mathbb{P}(B|A)}{\mathbb{P}(A)\mathbb{P}(B|A) + \mathbb{P}(A^c)\mathbb{P}(B|A^c)}
$$

### 2.6.2 应用：假阳性之谜
某种疾病发病率为0.001，检验准确率为0.95：
- 如果检验为阳性，实际患病的概率：
  $$
  \mathbb{P}(A|B) = \frac{0.001 \times 0.95}{0.001 \times 0.95 + 0.999 \times 0.05} \approx 1.87\%
  $$
  **结论**：由于发病率低和诊断准确性不够高，即使检验为阳性，实际患病概率也很低。

### 2.6.3 贝叶斯统计应用
- 贝叶斯网络
- 传染病传播预测模型
- 图灵奖得主Judea Pearl的工作

## 小结

### 核心知识点
- **概率空间**：事件域、概率测度的严格定义
- **概率连续性**：单调序列的极限、上下极限、Borel-Cantelli引理
- **条件概率**：定义、性质、条件概率空间
- **三大法则**：乘法公式、全概率公式、贝叶斯法则

### 重要技巧
- 类比熟悉概念理解新概念（数列极限→集合极限）
- 复杂问题拆分为简单问题
- 选择合适的条件概率顺序和样本空间分割以简化计算
- 利用序贯树形图进行概率计算

### 关键公式总结
- 条件概率：$\mathbb{P}(B|A) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(A)}$
- 乘法公式：$\mathbb{P}(A_1 \cap \cdots \cap A_n) = \mathbb{P}(A_1) \prod_{i=2}^n \mathbb{P}(A_i | A_1 \cap \cdots \cap A_{i-1})$
- 全概率公式：$\mathbb{P}(B) = \sum_{i=1}^n \mathbb{P}(A_i)\mathbb{P}(B|A_i)$
- 贝叶斯法则：$\mathbb{P}(A_i|B) = \frac{\mathbb{P}(A_i)\mathbb{P}(B|A_i)}{\sum_j \mathbb{P}(A_j)\mathbb{P}(B|A_j)}$
