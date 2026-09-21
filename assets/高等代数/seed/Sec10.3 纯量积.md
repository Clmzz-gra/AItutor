---
type: 节
formal: true
subject: 高等代数
created: 2026-09-21
updated: 2026-09-21
tags: [math, 高等代数]
chapter: 10
section: 10.3
---

# Sec10.3 纯量积

> 定位：把双线性型的两个变元收回**同一个空间** $V$（即 $g:V\times V\to\mathbb{K}$），考察"对称"与"交错"两种特殊情形；证明"正交关系可交换"当且仅当 $g$ 是对称型或交错型，并给出正交补的直和分解。
> 教材：谢启鸿、姚慕生、吴泉水《高等代数学》第四版 §10.3（p.453–457）★ 选学

> [!info] 关联笔记
> - 父级：[[Ch10 双线性型]]
> - 前置：[[Sec10.2 双线性型]] ｜ 后续：[[Sec10.4 交错型与辛几何]]

---

## 来龙（为什么需要它）

- **类比已知**：Ch9 的内积就是"两个变元在同一个空间、并且带对称性"的双线性函数；§10.2 已把双线性型的最一般形态讲清（$U\times V\to\mathbb{K}$，表示矩阵 $A=(g(e_i,v_j))$，标准形 $\begin{pmatrix}I_r&O\\O&O\end{pmatrix}$）。
- **解决新问题**：§10.2 的两个变元分属 $U$ 与 $V$，地位**不对称**，所以"左根子空间"与"右根子空间"必须分别定义。一旦把两个变元收回同一个空间 $V$，"$x$ 与 $y$ 配对得零"就可以自然地读作"$x$ 与 $y$ 正交"，于是产生新问题：**这种正交关系可交换吗？** 教材 §10.3 原文："设 $g$ 是 $V$ 上的纯量积，$\boldsymbol{x},\boldsymbol{y}$ 是 $V$ 中两个向量。若 $g(\boldsymbol{x},\boldsymbol{y})=0$，则称 $\boldsymbol{x}$ 左垂直于 $\boldsymbol{y}$ 或 $\boldsymbol{y}$ 右垂直于 $\boldsymbol{x}$……反过来，如果 $g$ 有下列性质：由 $\boldsymbol{x}\perp\boldsymbol{y}$ 总可推出 $\boldsymbol{y}\perp\boldsymbol{x}$，那么 $g$ 是否必为对称型或交错型呢？下面的定理将给予肯定的回答。"
- **理论/应用需要**：正交补的直和分解 $V=U\oplus U^{\perp}$（定理 10.3.2）是 §10.4 交错型标准形证明的**核心工具**（§10.4 证明原文："注意到 $g$ 限制在 $V_0$ 上是非退化的，故由定理 10.3.2 得到 $V=V_0\oplus V_0^{\perp}$"），也是 §10.5 正交几何的地基；定理 10.3.3 则说明**非退化纯量积在同构意义下唯一**，为交错型与对称型两个分支的平行讨论铺路。

## 主体（核心内容）

**知识点清单**（来自教材 §10.3 正文，逐条列，标 `重点`/`难点`/`考点` 标签）

- **纯量积（数量积）** —— $V\times V\to\mathbb{K}$ 的双线性函数 `重点`
- **对称型** —— $g(\boldsymbol{x},\boldsymbol{y})=g(\boldsymbol{y},\boldsymbol{x})$ 对一切 $\boldsymbol{x},\boldsymbol{y}\in V$ 成立 `重点`
- **交错型（反对称型）** —— $g(\boldsymbol{x},\boldsymbol{y})=-g(\boldsymbol{y},\boldsymbol{x})$ 对一切 $\boldsymbol{x},\boldsymbol{y}$ 成立 `重点` `考点`
- 交错型的**等价刻画** —— "对 $V$ 中任一元素 $\boldsymbol{x}$，$g(\boldsymbol{x},\boldsymbol{x})=0$" `重点`
- 纯量积的**矩阵表示** —— 只取一组基，$\boldsymbol{A}=(g(\boldsymbol{e}_i,\boldsymbol{e}_j))$，(10.3.1) 式 `重点`
- **换基公式** —— 过渡矩阵 $\boldsymbol{C}$ 给出 $\boldsymbol{B}=\boldsymbol{C}'\boldsymbol{A}\boldsymbol{C}$，即纯量积在不同基下的表示矩阵**合同** `考点`
- **表示矩阵与型的对应** —— 对称型 $\leftrightarrow$ 对称阵，反对称型 $\leftrightarrow$ 反对称阵（取定基后一一对应）`考点`
- **左垂直 / 右垂直 / 正交** —— $\boldsymbol{x}\perp\boldsymbol{y}$ 的定义与可交换性 `重点`
- 定理 10.3.1 —— 正交关系可交换 $\iff$ $g$ 为对称型或交错型 `重点` `难点`
- 推论 10.3.1 —— 对称型/交错型下子空间的正交补 $U^{\perp}$ `难点`
- 定理 10.3.2 —— $V=U\oplus U^{\perp}$ $\iff$ $g$ 限制在 $U$ 上非退化 `重点` `难点`
- 注 —— $g$ 非退化时，$g$ 在 $U$ 上非退化 $\iff$ $g$ 在 $U^{\perp}$ 上非退化
- 定理 10.3.3 —— 两个非退化纯量积之间存在**唯一**的非异线性变换相联系 `难点`
- 习题（见教材 §10.3 末，本节范围 p.453–457）

**关键定义与结论**（教材原述，逐条列）

- **定义**（定义 10.3.1，纯量积 / 对称型 / 交错型）：设 $g$ 是 $V\times V\to\mathbb{K}$ 的双线性函数，则称 $g$ 是 $V$ 上的**纯量积**或**数量积**。若
  $$g(\boldsymbol{x},\boldsymbol{y})=g(\boldsymbol{y},\boldsymbol{x})$$
  对一切 $\boldsymbol{x},\boldsymbol{y}\in V$ 成立，则称 $g$ 是 $V$ 上的**对称型**。若
  $$g(\boldsymbol{x},\boldsymbol{y})=-g(\boldsymbol{y},\boldsymbol{x})$$
  对一切 $\boldsymbol{x},\boldsymbol{y}\in V$ 成立，则称 $g$ 是 $V$ 上的**交错型**。
  读法：$g(\boldsymbol{x},\boldsymbol{y})$ 读作"$\boldsymbol{x}$ 与 $\boldsymbol{y}$ 的纯量积"；$V\times V$ 读作"$V$ 与自身的积集合"。
  教材补充：交错型又称为**反对称型**。交错型的另一等价说法是，对 $V$ 中任一元素 $\boldsymbol{x}$，$g(\boldsymbol{x},\boldsymbol{x})=0$。事实上，由 $g(\boldsymbol{x},\boldsymbol{x})=-g(\boldsymbol{x},\boldsymbol{x})$ 可推出 $g(\boldsymbol{x},\boldsymbol{x})=0$；另一方面，若 $g(\boldsymbol{x},\boldsymbol{x})=0$ 对一切 $\boldsymbol{x}$ 成立，则 $g(\boldsymbol{x}+\boldsymbol{y},\boldsymbol{x}+\boldsymbol{y})=0$，由此即可推出 $g(\boldsymbol{x},\boldsymbol{y})=-g(\boldsymbol{y},\boldsymbol{x})$。
  边界：上述两个方向的推导都要用到"由 $2\,g(\boldsymbol{x},\boldsymbol{y})=0$ 可得 $g(\boldsymbol{x},\boldsymbol{y})=0$"，即隐含 $\mathrm{char}\,\mathbb{K}\neq2$（教材全书按通常数域讨论）。
- **矩阵表示**：$V$ 上的纯量积也可用矩阵表示，但与一般双线性型有一点区别——**只取 $V$ 的一组基，而不是取两组基**。若 $\{\boldsymbol{e}_1,\boldsymbol{e}_2,\dots,\boldsymbol{e}_n\}$ 是 $V$ 的一组基，则 $g$ 的表示矩阵为 $\boldsymbol{A}=(g(\boldsymbol{e}_i,\boldsymbol{e}_j))$；对 $\boldsymbol{x}=\sum_i a_i\boldsymbol{e}_i$、$\boldsymbol{y}=\sum_i b_i\boldsymbol{e}_i$ 有
  $$g(\boldsymbol{x},\boldsymbol{y})=(a_1,a_2,\dots,a_n)\,\boldsymbol{A}\,(b_1,b_2,\dots,b_n)'.\tag{10.3.1}$$
- **换基公式**：设 $\{\boldsymbol{v}_i\}$ 是 $V$ 的另一组基，$\boldsymbol{B}$ 是 $g$ 在 $\{\boldsymbol{v}_i\}$ 下的表示矩阵，若从 $\{\boldsymbol{e}_i\}$ 到 $\{\boldsymbol{v}_i\}$ 的过渡矩阵为 $\boldsymbol{C}$，则 $\boldsymbol{B}=\boldsymbol{C}'\boldsymbol{A}\boldsymbol{C}$——**纯量积 $g$ 在不同基下的表示矩阵是合同的**。
- **表示矩阵与型的对应**：显然，对称型的表示矩阵是对称阵，反对称型的表示矩阵是反对称阵。反过来，在取定 $V$ 的一组基后，若给定一个对称阵（反对称阵），则 (10.3.1) 式定义了 $V$ 上的一个对称型（反对称型）。
- **定义**（正交）：设 $g$ 是 $V$ 上的纯量积，$\boldsymbol{x},\boldsymbol{y}$ 是 $V$ 中两个向量。若 $g(\boldsymbol{x},\boldsymbol{y})=0$，则称 $\boldsymbol{x}$ **左垂直于** $\boldsymbol{y}$，或 $\boldsymbol{y}$ **右垂直于** $\boldsymbol{x}$，记为 $\boldsymbol{x}\perp\boldsymbol{y}$。当 $g$ 是对称型或交错型时，$\boldsymbol{x}\perp\boldsymbol{y}$ 等价于 $\boldsymbol{y}\perp\boldsymbol{x}$，这时称 $\boldsymbol{x}$ 与 $\boldsymbol{y}$ **正交**。
  读法：$\boldsymbol{x}\perp\boldsymbol{y}$ 读作"$\boldsymbol{x}$ 与 $\boldsymbol{y}$ 正交"。
- **定理**（定理 10.3.1）：设 $g$ 是 $V$ 上的纯量积，则在 $V$ 中 $\boldsymbol{x}\perp\boldsymbol{y}$ 等价于 $\boldsymbol{y}\perp\boldsymbol{x}$ 的充分必要条件是 $g$ 为**对称型或交错型**。
  证明思路（教材只证必要性）：设 $\boldsymbol{x},\boldsymbol{y},\boldsymbol{z}\in V$，令
  $$\boldsymbol{w}=g(\boldsymbol{x},\boldsymbol{y})\boldsymbol{z}-g(\boldsymbol{x},\boldsymbol{z})\boldsymbol{y},$$
  则
  $$g(\boldsymbol{x},\boldsymbol{w})=g(\boldsymbol{x},\boldsymbol{y})g(\boldsymbol{x},\boldsymbol{z})-g(\boldsymbol{x},\boldsymbol{z})g(\boldsymbol{x},\boldsymbol{y})=0,$$
  即 $\boldsymbol{x}\perp\boldsymbol{w}$；由假设（正交关系可交换）得 $\boldsymbol{w}\perp\boldsymbol{x}$，即
  $$g(\boldsymbol{w},\boldsymbol{x})=g(\boldsymbol{x},\boldsymbol{y})\,g(\boldsymbol{z},\boldsymbol{x})-g(\boldsymbol{x},\boldsymbol{z})\,g(\boldsymbol{y},\boldsymbol{x})=0,$$
  再由 $\boldsymbol{x},\boldsymbol{y},\boldsymbol{z}$ 的任意性推出 $g$ 为对称型或交错型（最后一步的细节见「防跳跃」）。
- **推论**（推论 10.3.1）：若 $g$ 是 $V$ 上的对称型或交错型，$U$ 是 $V$ 的子空间，记 $U^{\perp}=\{\boldsymbol{v}\in V\mid g(\boldsymbol{v},U)=0\}$（骨架在"记"处截断，记号按教材 §10.4 证明中的用法补全），则……（结论待核，见「防跳跃」）。
- **定理**（定理 10.3.2）：设 $g$ 是 $n$ 维线性空间 $V$ 上的对称型（交错型），$U$ 是 $V$ 的子空间，则
  $$V=U\oplus U^{\perp}$$
  的充分必要条件是 $g$ 限制在 $U$ 上是 $U$ 上的一个**非退化**的纯量积。这时有直和分解（教材原文此处截断，具体形式待核）。
  意义：这是内积空间"正交补直和分解"在**去掉正定性**后的版本——它仍然成立，但**多了一个条件**：$g$ 在 $U$ 上的限制必须非退化。
- **注**：当 $g$ 非退化时，有（教材原文截断的等式），故由定理 10.3.2 知，此时 $g$ 限制在 $U$ 上非退化**当且仅当** $g$ 限制在 $U^{\perp}$ 上也非退化。
- **定理**（定理 10.3.3）：设 $g$ 与 $h$ 是 $V$ 上的两个**非退化**纯量积，则存在 $V$ 上**唯一**的非异线性变换 $\sigma$，使（骨架截断；按 §10.2 定理 10.2.3 的形式应为 $h(\boldsymbol{x},\boldsymbol{y})=g(\sigma(\boldsymbol{x}),\sigma(\boldsymbol{y}))$，待核）。
  对照 §10.2 定理 10.2.3：那里左右各需一个非异变换，且**不唯一**；这里两个变元同属 $V$ 且 $g,h$ 都非退化，于是出现了**唯一性**。
- **反例 / 边界**：
  - **"左垂直"不等于"正交"**：在 $V=\mathbb{K}^2$ 上取 $g(\boldsymbol{x},\boldsymbol{y})=x_1y_2$（表示矩阵 $\boldsymbol{A}=\begin{pmatrix}0&1\\0&0\end{pmatrix}$）。它既不是对称型也不是交错型。取 $\boldsymbol{x}=(0,1)$、$\boldsymbol{y}=(1,0)$：$g(\boldsymbol{x},\boldsymbol{y})=0$ 而 $g(\boldsymbol{y},\boldsymbol{x})=1\neq0$——**$\boldsymbol{x}\perp\boldsymbol{y}$ 成立但 $\boldsymbol{y}\perp\boldsymbol{x}$ 不成立**，正是定理 10.3.1 条件不满足时的表现。
  - **既对称又交错者只有零型**：若 $g$ 同时是对称型与交错型，则 $g(\boldsymbol{x},\boldsymbol{y})=g(\boldsymbol{y},\boldsymbol{x})=-g(\boldsymbol{x},\boldsymbol{y})$，在 $\mathrm{char}\,\mathbb{K}\neq2$ 时得 $g\equiv0$。所以定理 10.3.1 中的"或"不能改成"且"。
  - **非退化也不能保证 $V=U\oplus U^{\perp}$**：在 $\mathbb{R}^2$ 上取 $g(\boldsymbol{x},\boldsymbol{y})=x_1y_1-x_2y_2$（非退化对称型），令 $U=\mathrm{span}\{(1,1)\}$。此时 $g|_U\equiv0$ 退化，且 $U^{\perp}=\{\boldsymbol{v}\mid v_1-v_2=0\}=U$，故 $U\cap U^{\perp}=U\neq0$，$V\neq U\oplus U^{\perp}$——**定理 10.3.2 的条件不可少**。
  - **零纯量积**：$g\equiv0$ 既是对称型也是交错型，但 $U^{\perp}=V$，任何非零子空间 $U$ 都有 $U\cap U^{\perp}=U\neq0$，$V=U\oplus U^{\perp}$ 永不成立。
  - **表示矩阵是"合同"而不是"相似"**：换基给的是 $\boldsymbol{B}=\boldsymbol{C}'\boldsymbol{A}\boldsymbol{C}$（合同），不是 Ch7 相似标准型中的 $\boldsymbol{C}^{-1}\boldsymbol{A}\boldsymbol{C}$；两者只在 $\boldsymbol{C}$ 满足 $\boldsymbol{C}'=\boldsymbol{C}^{-1}$（正交阵）时才重合。

> **这一节真正要说的是**：把双线性型的两个变元收回同一个空间后，"正交"这个概念才有意义；而**正交关系可交换**不是自动的，它恰好刻画了对称型与交错型这两类（定理 10.3.1）。从此纯量积分成两条互不重叠的支流——**交错型（§10.4，辛几何）**与**对称型（§10.5，正交几何）**；两支共用的地基则是定理 10.3.2 的正交补直和分解：**它把"非退化"这个抽象条件翻译成"$V$ 能沿 $U$ 与 $U^{\perp}$ 拆开"这个几何事实**。

## 去脉（学完去哪）

- **本章内**：§10.4 取**交错型**一支，用定理 10.3.2 归纳证明交错型的标准形 $\mathrm{diag}\{S,\dots,S;0,\dots,0\}$，得到**辛空间**；§10.5 取**对称型**一支，讨论**正交几何**（正交变换、迷向向量、双曲平面、Minkowski 空间）。
- **后续章节**：本章为末章。回看 Ch9 §9.2（内积的矩阵表示与 (10.3.1) 式形式相同，差别只在 $\boldsymbol{A}$ 是正定对称阵）；见 Ch8 §8.1（$B=C'AC$ 的合同变换与二次型化简用的是同一套变换）；见 Ch8 §8.3（实对称阵的惯性定理给出对称型在实数域上的分类）。
- **应用**：
  - **辛几何与力学**：非退化交错型（§10.4）就是 Hamilton 力学中"广义坐标—广义动量"的配对。
  - **相对论时空**：非退化对称型（§10.5）给出 Minkowski 度量的代数模型。
  - **二次型理论**：对称型与二次型一一对应（Ch8），纯量积的语言让"合同"有了几何解释。

## 防跳跃

- [ ] 定理 10.3.1 必要性证明的**最后一跳**：如何由 $g(\boldsymbol{x},\boldsymbol{y})g(\boldsymbol{z},\boldsymbol{x})=g(\boldsymbol{x},\boldsymbol{z})g(\boldsymbol{y},\boldsymbol{x})$ 对一切 $\boldsymbol{x},\boldsymbol{y},\boldsymbol{z}$ 成立推出 $g$ 为对称型或交错型（教材后续步骤未读，待核）
- [ ] 推论 10.3.1 的**完整陈述**（骨架在"记"处截断：$U^{\perp}$ 的确切记号与结论）
- [ ] 定理 10.3.2 中"这时有直和分解"之后的**具体形式**
- [ ] 注中"当 $g$ 非退化时，有……"被截断的等式（疑为 $\dim U+\dim U^{\perp}=\dim V$ 或 $(U^{\perp})^{\perp}=U$，待核）
- [ ] 定理 10.3.3 中唯一非异线性变换 $\sigma$ 所满足的等式
- [ ] $\mathrm{char}\,\mathbb{K}=2$ 时"交错 $\iff$ 对一切 $\boldsymbol{x}$ 有 $g(\boldsymbol{x},\boldsymbol{x})=0$"是否仍成立（教材未讨论）
- [ ] 定理 10.3.2 的完整证明（如何由 $g|_U$ 非退化构造出直和分解）

## 待填充

- [ ] 完整证明展开
- [ ] 例题（原始信息 → 代入 → 结果 → 结论）
- [ ] 自测题（按 `tutor` skill 的检验回路生成）

## 来源与映射

| 本节点内容 | 来源 | 处理 |
|---|---|---|
| 知识点清单 | 教材 §10.3 正文条目（定义 10.3.1、定理 10.3.1–10.3.3、推论 10.3.1、注、(10.3.1) 式、换基公式） | 提取 |
| 定位 / 来龙 | 教材 §10.3 开头段与"左垂直 / 右垂直 / 正交"段（已回读 OCR 行 18665–18724 逐字核对） | 提炼 |
| 关键定义与结论 | 教材 §10.3 定义 10.3.1、定理 10.3.1 及证明首步、(10.3.1) 式、换基公式、正交定义的**逐字原文**（OCR 行 18665–18724）；其余条目取自骨架文件 `_scratch/seed-init/gaodai-outline/Ch10.md` | 摘录 |
| 反例 / 边界 | $g=x_1y_2$ 破坏正交可交换性；$x_1y_1-x_2y_2$ 上 $U=\mathrm{span}\{(1,1)\}$ 破坏直和分解；零纯量积；合同 vs 相似 | 推导 |