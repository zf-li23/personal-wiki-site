## 1.1 概率模型

### 1.1.1 样本空间
- **定义**：样本空间$\Omega$是一个集合，包含试验的所有可能结果
- **基本要求**：
  - 试验结果必须互斥且完整
  - 可能是有限或无限个结果
  - 连续抛三次硬币视为一次试验，而非三次独立试验

### 1.1.2 样本空间的选择艺术
- 同一试验可根据不同兴趣确定不同模型
- 选择原则：既要有足够细节，又要避免不必要繁琐
- **示例**：连续抛掷10次硬币的两种不同游戏规则

### 1.1.3 样本空间类型
- **离散样本空间**：序贯树形图描述
- **连续样本空间**：如约会延迟问题
  $$
  \Omega = \{(x, y) | 0 \leq x, y \leq 1\}
  $$

## 1.2 概率公理

### 1.2.1 概率公理系统
1. **非负性**：对一切事件 $A$，$\mathbb{P}(A) \geq 0$
2. **归一化**：$\mathbb{P}(\Omega) = 1$
3. **可列可加性**：若 $A_1, A_2, \ldots$ 互不相交，则
   $$
   \mathbb{P}\left( \bigcup_{i=1}^{\infty} A_i \right) = \sum_{i=1}^{\infty} \mathbb{P}(A_i)
   $$

### 1.2.2 概率模型构成
- 样本空间$\Omega$：所有可能结果的集合
- 概率$\mathbb{P}(A)$：为事件$A$确定的非负数，表示信念程度

## 1.3 概率模型类型

### 1.3.1 离散模型
- **古典概型（离散均匀概率）**：
  $$
  \mathbb{P}(A) = \frac{\text{合于事件$A$的试验结果数}}{n}
  $$
- 假设骰子均匀时各种概率计算

### 1.3.2 连续模型
- **几何概率模型（连续均匀概率）**：
  $$
  \mathbb{P}(A) = \frac{m(A)}{m(\Omega)}
  $$
  其中 $ m(A) $ 表示$ A $的体积

## 1.4 模型与现实：Bertrand悖论

在半径为1的圆内任取一条弦，求弦长 $\geq \sqrt{3}$的概率：
- **方法1**：弦端点等可能落在圆周上 $\rightarrow$ $\mathbb{P} = 1/3$
- **方法2**：弦中点等可能落在直径上 $\rightarrow$ $\mathbb{P} = 1/2$
- **方法3**：弦中点等可能落在圆内 $\rightarrow$ $\mathbb{P} = 1/4$

**结论**：不同的"等可能"假设导致不同计算结果

## 1.5 概率的性质

### 1.5.1 基本性质
1. $\mathbb{P}(\emptyset) = 0$
2. **有限可加性**：若 $A_i \cap A_j = \emptyset (i \neq j)$，则
   $$
   \mathbb{P}\left( \bigcup_{i=1}^n A_i \right) = \sum_{i=1}^n \mathbb{P}(A_i)
   $$
3. $\mathbb{P}(A^c) = 1 - \mathbb{P}(A)$
4. 若 $A \subset B$，则 $\mathbb{P}(B \setminus A) = \mathbb{P}(B) - \mathbb{P}(A)$

### 1.5.2 重要不等式与公式
- **单调性**：若 $A \subset B$，则 $\mathbb{P}(A) \leq \mathbb{P}(B)$
- **加法公式**：
  $$
  \mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)
  $$
- **容斥恒等式**：
  $$
  \mathbb{P}\left( \bigcup_{i=1}^n A_i \right) = \sum_{i} \mathbb{P}(A_i) - \sum_{i<j} \mathbb{P}(A_i \cap A_j) + \sum_{i<j<k} \mathbb{P}(A_i \cap A_j \cap A_k) - \cdots
  $$
- **Bonferroni不等式**：
  $$
  \mathbb{P}\left( \bigcup_{i=1}^n A_i \right) \geq \sum_{i} \mathbb{P}(A_i) - \sum_{i<j} \mathbb{P}(A_i \cap A_j)
  $$
- **可列次可加性** / **Boole不等式**：
  $$
  \mathbb{P}\left( \bigcup_{i=1}^{\infty} A_i \right) \leq \sum_{i=1}^{\infty} \mathbb{P}(A_i)
  $$

## 1.6 随机抽样与随机分配

### 1.6.1 排列与组合公式
- 排列数：
	$$
	P_n^k = \frac{n!}{(n-k)!}
	$$
- 组合数：
	$$
	\binom{n}{k} = \frac{n!}{k!(n-k)!}
	$$

### 1.6.2 抽样方式分类
| 抽样方式   | 有序抽样 | 无序抽样           |
| ---------- | -------- | ------------------ |
| **有放回** | $M^n$    | $\binom{M+n-1}{n}$ |
| **无放回** | $P_M^n$  | $\binom{M}{n}$     |

### 1.6.3 随机分配对应关系
- 有序抽样 $\Leftrightarrow$ 质点可辨别
- 无序抽样 $\Leftrightarrow$ 质点不可辨别  
- 放回抽样 $\Leftrightarrow$ 箱中可容纳任意多质点
- 不放回抽样 $\Leftrightarrow$ 箱中最多容纳一个质点

## 1.7 古典概型补充说明

### 1.7.1 解题技巧
- 不要失去常识，也不要过分依赖
- 用最简单情形验证
- 将物体编号
- 情景证明(story proof)

### 1.7.2 情景证明示例
- 组合恒等式：
  $$
  \binom{m}{n} = \binom{m-1}{n-1} + \binom{m-1}{n}
  $$
- 多项式系数：把$m$个球放入$r$个盒子，使得$m_j$个球进入第$j$个盒子

## 小结

### 核心知识点
- **概念**：试验、事件、样本空间、概率（公理化定义）
- **经典模型**：古典概型、几何概型
- **概率性质**：有限/可列可加性、各种等式与不等式
- **随机抽样**：有无放回、有无序四种组合方式

### 重要技巧
- 定义的明确性（样本空间、等可能性）
- 直观化、简单化（情景证明、Taylor展开近似）
- 证明工具：互斥集合分解、归纳法、求补法

### 关键公式总结
- 古典概型：$\mathbb{P}(A) = \frac{\text{有利结果数}}{\text{总结果数}}$
- 几何概型：$\mathbb{P}(A) = \frac{m(A)}{m(\Omega)}$
- 容斥原理：多事件并集的概率计算
- 抽样计数：四种抽样方式的样本空间大小公式
