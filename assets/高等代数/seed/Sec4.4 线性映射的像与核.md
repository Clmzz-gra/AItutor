---
type: 节
formal: true
subject: 高等代数
created: 2026-09-21
updated: 2026-09-21
tags: [math, 高等代数]
chapter: 4
section: 4.4
---
# Sec4.4 线性映射的像与核

> 定位：定义**像** $\mathrm{Im}\,\varphi$ 与**核** $\mathrm{Ker}\,\varphi$，用表示矩阵的秩算出它们的维数，得到**线性映射维数公式** $\dim\mathrm{Ker}\,\varphi+\dim\mathrm{Im}\,\varphi=\dim V$。
> 教材：谢启鸿、姚慕生、吴泉水《高等代数学》第四版 §4.4（p.200–204）

> [!info] 关联笔记
> - 父级：[[Ch4 线性映射]]
> - 前置：[[Sec4.3 线性映射与矩阵]] ｜ 后续：[[Sec4.5 不变子空间]]

---

## 来龙（为什么需要它）

- **类比已知**：§4.1 复习映射时已经定义了"像"$\varphi(A)$ 或 $\mathrm{Im}\,\varphi$——$A$ 中元素在 $\varphi$ 下的像全体构成的子集。但那里的像只是**集合**，还没有结构。
- **解决新问题**：对线性映射而言，像与"被映为零的向量全体"这两块恰好是线性空间意义上的子空间。于是产生三个问题：像与核是不是子空间？它们的维数怎么算？单映射、满映射能不能用维数或矩阵的秩来判断？
- **理论/应用需要**：本节把 §3.9 的子空间理论与 §3.6 的矩阵秩理论接在一起，得到**线性映射维数公式**。这条公式是后续所有"秩—零度"讨论的母公式：Ch4 §4.5 用它推"单 ⟺ 满"（有限维），Ch9 的秩—零度定理、Ch9 §9.10 的最小二乘解都要用它。

## 主体（核心内容）

**知识点清单**（来自教材 §4.4 正文，逐条列，标 `重点`/`难点`/`考点` 标签）

- 定义 4.4.1：像 $\mathrm{Im}\,\varphi$ 与核 $\mathrm{Ker}\,\varphi$ `重点` `考点`
- 命题 4.4.1：$\mathrm{Im}\,\varphi$ 是 $U$ 的子空间，$\mathrm{Ker}\,\varphi$ 是 $V$ 的子空间
- 推论 4.4.1：满 $\Leftrightarrow$ $\dim\mathrm{Im}\,\varphi=\dim U$；单 $\Leftrightarrow$ $\mathrm{Ker}\,\varphi=0$ `重点` `考点`
- 定义 4.4.2：线性映射的秩 $\mathrm{r}(\varphi)$ 与零度 `重点`
- 引理 4.4.1：定义域的限制（限制映射）`难点`
- 例 4.4.1：旋转在 $x$-轴上的限制
- 定理 4.4.1：$\dim\mathrm{Im}\,\varphi=\operatorname{rank}(A)$，$\dim\mathrm{Ker}\,\varphi=n-\operatorname{rank}(A)$ `重点` `考点`
- 推论 4.4.2（线性映射维数公式）：$\dim\mathrm{Ker}\,\varphi+\dim\mathrm{Im}\,\varphi=\dim V$ `重点` `考点`
- 推论 4.4.3：满 $\Leftrightarrow$ $\mathrm{r}(A)=m$（行满秩）；单 $\Leftrightarrow$ $\mathrm{r}(A)=n$（列满秩）`考点`
- 推论 4.4.4：$n$ 维空间上线性变换可逆 $\Leftrightarrow$ 单 $\Leftrightarrow$ 满 `重点` `考点`
- 推论 4.4.5：单（或满）$\Leftrightarrow$ 任意一组基下的表示矩阵可逆
- 例 4.4.2：计算像空间与核空间 `考点`

**关键定义与结论**（教材原述，逐条列）

- **定义 4.4.1（像与核）**：设 $\varphi$ 是数域 $\mathbb{K}$ 上线性空间 $V$ 到 $U$ 的线性映射，$\varphi$ 的**全体像元素**组成 $U$ 的子集称为 $\varphi$ 的**像**，记为 $\mathrm{Im}\,\varphi$。又，$V$ 中在 $\varphi$ 下映射为**零向量**的全体向量构成 $V$ 的子集，称为 $\varphi$ 的**核**，记为 $\mathrm{Ker}\,\varphi$。
  - 读法：$\mathrm{Im}\,\varphi$ 读作"$\varphi$ 的像"；$\mathrm{Ker}\,\varphi$ 读作"$\varphi$ 的核"。
- **命题 4.4.1**：设 $\varphi$ 是线性空间 $V\to U$ 的线性映射，则 $\mathrm{Im}\,\varphi$ 是 $U$ 的子空间，$\mathrm{Ker}\,\varphi$ 是 $V$ 的子空间。
  - 证明：设 $\alpha,\beta\in\mathrm{Im}\,\varphi$，则有 $V$ 中向量 $u,v$ 使 $\alpha=\varphi(u)$、$\beta=\varphi(v)$；由于 $\varphi(u+v)=\varphi(u)+\varphi(v)=\alpha+\beta$，故 $\alpha+\beta\in\mathrm{Im}\,\varphi$；若 $k\in\mathbb{K}$，则 $\varphi(ku)=k\varphi(u)=k\alpha$，故 $k\alpha\in\mathrm{Im}\,\varphi$。又设 $u,v\in\mathrm{Ker}\,\varphi$，则 $\varphi(u+v)=\varphi(u)+\varphi(v)=\mathbf{0}$，故 $u+v\in\mathrm{Ker}\,\varphi$；类似地可证 $ku\in\mathrm{Ker}\,\varphi$。
- **推论 4.4.1**：线性映射 $\varphi$ 是**满映射**的充分必要条件是 $\dim\mathrm{Im}\,\varphi=\dim U$；线性映射 $\varphi$ 是**单映射**的充分必要条件是 $\mathrm{Ker}\,\varphi=0$。
  - 证明要点（第二句）：若 $\varphi$ 单且 $v\in\mathrm{Ker}\,\varphi$，则 $\varphi(v)=\mathbf{0}=\varphi(\mathbf{0})$，于是 $v=\mathbf{0}$；反之若 $\mathrm{Ker}\,\varphi=0$ 且 $\varphi(u)=\varphi(v)$，则 $\varphi(u-v)=\mathbf{0}$，故 $u-v=\mathbf{0}$。
- **定义 4.4.2（秩与零度）**：设 $\varphi$ 是 $V\to U$ 的线性映射。像空间 $\mathrm{Im}\,\varphi$ 的维数称为 $\varphi$ 的**秩**，记作 $\mathrm{r}(\varphi)$；核空间 $\mathrm{Ker}\,\varphi$ 的维数称为 $\varphi$ 的**零度**。
  - 读法：$\mathrm{r}(\varphi)$ 读作"$\varphi$ 的秩"；"零度"读作"$\varphi$ 的零度"（即 $\dim\mathrm{Ker}\,\varphi$）。
- **引理 4.4.1（定义域的限制）**：设 $\varphi:V\to U$ 为线性映射，$V'\subseteq V$、$U'\subseteq U$ 为子空间且满足 $\varphi(V')\subseteq U'$，则通过定义域的限制可得线性映射 $\varphi':V'\to U'$，使得 $\varphi'$ 与 $\varphi$ 具有相同的映射法则。进一步，若 $\varphi$ 是单映射，则 $\varphi'$ 也是单映射。
  - 证明：定义 $\varphi'(v')=\varphi(v')\in U'$；它其实是将 $\varphi$ 的定义域限制在 $V'$ 上得到的映射。注意到 $\mathrm{Ker}\,\varphi'=\mathrm{Ker}\,\varphi\cap V'$，因此第二个结论由推论 4.4.1 即得。
- **例 4.4.1**：设 $V$ 是 Descartes 平面，$\varphi$ 是绕原点逆时针旋转 $\theta$ 角的线性变换。设 $V'$ 是 $x$-轴所在的一维子空间，$U'$ 是 $\theta$ 角直线所在的一维子空间，则限制映射 $\varphi':V'\to U'$ 不仅是单线性映射，也是满线性映射。
- **定理 4.4.1**：设 $V,U$ 分别是数域 $\mathbb{K}$ 上的 $n$ 维和 $m$ 维线性空间，又设 $\{e_1,\cdots,e_n\}$ 是 $V$ 的基，$\{f_1,\cdots,f_m\}$ 是 $U$ 的基。设 $\varphi$ 是 $V\to U$ 的线性映射，它在给定基下的表示矩阵为 $A$，则
  $$\dim\mathrm{Im}\,\varphi=\operatorname{rank}(A),\qquad \dim\mathrm{Ker}\,\varphi=n-\operatorname{rank}(A).$$
  - 证明思路：沿用定理 4.3.1 的记号与交换图 4.1。先证 $\eta_1(\mathrm{Ker}\,\varphi)\subseteq\mathrm{Ker}\,\varphi_A$、$\eta_2(\mathrm{Im}\,\varphi)\subseteq\mathrm{Im}\,\varphi_A$，再由引理 4.4.1 得两个单线性映射 $\eta_1':\mathrm{Ker}\,\varphi\to\mathrm{Ker}\,\varphi_A$ 与 $\eta_2':\mathrm{Im}\,\varphi\to\mathrm{Im}\,\varphi_A$，并证明它们都是满射，从而是**线性同构**。再把 $A$ 列分块 $A=(\alpha_1,\cdots,\alpha_n)$，对任意 $x=(x_1,\cdots,x_n)'$ 有 $\varphi_A(x)=x_1\alpha_1+\cdots+x_n\alpha_n$，故 $\mathrm{Im}\,\varphi_A=L(\alpha_1,\cdots,\alpha_n)$，由定理 3.9.1 知 $\dim\mathrm{Im}\,\varphi_A=\operatorname{rank}(A)$；又 $\mathrm{Ker}\,\varphi_A$ 是齐次线性方程组 $Ax=0$ 的解空间，由定理 3.10.2 知 $\dim\mathrm{Ker}\,\varphi_A=n-\operatorname{rank}(A)$。
- **推论 4.4.2（线性映射维数公式）**：设 $\varphi$ 是 $\mathbb{K}$ 上 $n$ 维线性空间 $V$ 到 $\mathbb{K}$ 上 $m$ 维线性空间 $U$ 的线性映射，则
  $$\dim\mathrm{Ker}\,\varphi+\dim\mathrm{Im}\,\varphi=\dim V.$$
- **推论 4.4.3**：记号同上，$\varphi$ 是**满映射**的充分必要条件是 $\mathrm{r}(A)=m$，即表示矩阵 $A$ 是一个**行满秩阵**；$\varphi$ 是**单映射**的充分必要条件是 $\mathrm{r}(A)=n$，即 $A$ 是一个**列满秩阵**。
- **推论 4.4.4**：$n$ 维线性空间 $V$ 上的线性变换 $\varphi$ 是**可逆变换**的充分必要条件为它是单映射或它是满映射。
  - 证明：若 $\varphi$ 单，则 $\mathrm{Ker}\,\varphi=0$，由维数公式得 $\dim\mathrm{Im}\,\varphi=n$，即 $\varphi$ 满，从而 $\varphi$ 是可逆变换（即自同构）；若 $\varphi$ 满，则 $\dim\mathrm{Im}\,\varphi=n$，由维数公式得 $\mathrm{Ker}\,\varphi=0$，即 $\varphi$ 单。
  - **注意**：这条推论**只对有限维空间成立**。
- **推论 4.4.5**：$n$ 维线性空间 $V$ 上的线性变换 $\varphi$ 是单映射（或满映射）的充分必要条件为它在 $V$ 的**任意一组基**下的表示矩阵是**可逆阵**。
  - 证明：由推论 4.3.1 和推论 4.4.4 即得；也可用代数方法——一个 $n$ 阶方阵 $A$ 可逆的充分必要条件是 $A$ 为行满秩阵或列满秩阵，故由推论 4.4.3 即得结论。
- **例 4.4.2（计算像空间与核空间）**：设 $V$ 是 $\mathbb{K}$ 上五维空间，$\{e_1,\cdots,e_5\}$ 是基，$U$ 是 $\mathbb{K}$ 上四维空间，$\{f_1,\cdots,f_4\}$ 是基，线性映射 $\varphi:V\to U$ 在上述基下的表示矩阵为
  $$A=\begin{pmatrix}1&2&1&-3&2\\2&1&1&1&-4\\1&1&2&2&-2\\2&3&-5&-17&8\end{pmatrix},$$
  求 $\mathrm{Im}\,\varphi$ 和 $\mathrm{Ker}\,\varphi$。
  - 解：对 $A$ 进行初等行变换得阶梯形，$\mathrm{r}(A)=3$，即 $\dim\mathrm{Im}\,\varphi=3$；$A$ 的前 3 个列向量线性无关，因此它们可以组成 $\mathrm{Im}\,\varphi$ 的一组基，故
    $$\mathrm{Im}\,\varphi=k_1(f_1+2f_2+f_3+2f_4)+k_2(2f_1+f_2+f_3+3f_4)+k_3(f_1+f_2+2f_3-5f_4);$$
    方程 $Ax=0$ 的基础解系为 $\alpha_1=(-1,3,-2,1,0)'$、$\alpha_2=(3,-3,1,0,1)'$，因此
    $$\mathrm{Ker}\,\varphi=k_1(-e_1+3e_2-2e_3+e_4)+k_2(3e_1-3e_2+e_3+e_5).$$
  - **方法要点**：求 $\mathrm{Im}\,\varphi$ 要用表示矩阵 $A$ 的**列向量**的极大无关组（因为 $\mathrm{Im}\,\varphi_A=L(\alpha_1,\cdots,\alpha_n)$）；求 $\mathrm{Ker}\,\varphi$ 要解齐次方程组 $Ax=0$ 并取其基础解系。
- **反例 / 边界**：
  - **推论 4.4.4 对无限维线性空间不成立**（教材 §4.4 习题 9 明确要求举例说明）：存在无限维线性空间 $V$ 上的线性变换 $\varphi$，使得 $\varphi$ 是单映射或满映射，但**不是**自同构。这正是"有限维"这一条件不可少的地方。
  - **求像空间时容易取错**：必须用 $A$ 的**列**向量的极大无关组，而不是行向量——因为 $\mathrm{Im}\,\varphi_A=L(\alpha_1,\cdots,\alpha_n)$ 中的 $\alpha_j$ 是 $A$ 的第 $j$ **列**。
  - **$\mathrm{Ker}\,\varphi=0$ 与"没有非零解"是同一件事**：推论 4.4.1 把"单映射"翻译成"核为零子空间"，这是把几何语言换成代数语言的关键一步。

**核心洞察**：这一节真正要说的是——**一个线性映射被两个子空间完全刻画**：核（"被压扁的部分"）与像（"留下来的部分"），而两者的维数之和恰好等于出发空间的维数。这条**维数公式**是线性代数的"守恒律"：线性映射不会凭空创造或消灭维度，它只是把维度在核与像之间分配。而分配的比例完全由表示矩阵的秩决定。

## 去脉（学完去哪）

- **本章内**：§4.5 中 $\mathrm{Im}\,\varphi$ 与 $\mathrm{Ker}\,\varphi$ 都是 $\varphi$ 的不变子空间（例 4.5.1）；推论 4.4.4 为"$n$ 维空间上单 ⟺ 满 ⟺ 可逆"提供了判据，§4.5 讨论表示矩阵形状时反复用到。
- **后续章节**：Ch6 中"$\lambda_0$ 是特征值 $\Leftrightarrow$ $\mathrm{Ker}(\lambda_0I-\varphi)\neq0$"，直接使用本节的定义，见 Ch6 §6.1；Ch7 §7.7 的根子空间是核空间 $\mathrm{Ker}(\lambda_0I-\varphi)^k$ 的推广；Ch9 §9.10 的最小二乘解用像空间与正交补的关系表述。
- **应用**：线性方程组的可解性判据（$\beta\in\mathrm{Im}\,\varphi$）；信号处理中的"零空间"与"值域"；控制论中能控子空间与不能观子空间。

## 防跳跃

- [ ] 命题 4.4.1 的证明只验证了"对加法与数乘封闭"，还需要补上"非空"（核至少含零向量、像至少含零向量）才能套用定义 3.9.1。
- [ ] 引理 4.4.1 是定理 4.4.1 证明的关键工具：它把 $\eta_1$、$\eta_2$ 限制到 $\mathrm{Ker}\,\varphi$、$\mathrm{Im}\,\varphi$ 上，再用推论 4.4.1 判断单射。
- [ ] 定理 4.4.1 的证明要说明 $\eta_1'$、$\eta_2'$ 都是**满射**（教材逐点构造原像），从而才是同构——只证单射不够。
- [ ] 定理 4.4.1 用到了定理 3.9.1（$\dim L(S)$ 等于极大无关组向量个数）与定理 3.10.2（解空间维数 $n-r$）——需要回看 §3.9 与 §3.10。
- [ ] 推论 4.4.4 的"有限维"条件不可少，教材 §4.4 习题 9 要求举例——这是一个必须能自己构造的反例。

## 待填充

- [ ] 完整证明展开
- [ ] 例题（原始信息 → 代入 → 结果 → 结论）
- [ ] 自测题（按 `tutor` skill 的检验回路生成）

## 来源与映射

| 本节点内容 | 来源 | 处理 |
|---|---|---|
| 知识点清单 | 教材 §4.4 正文标题与定义、定理名（定义 4.4.1–4.4.2、命题 4.4.1、引理 4.4.1、定理 4.4.1、推论 4.4.1–4.4.5、例 4.4.1–4.4.2） | 提取 |
| 定位/来龙 | 教材 §4.4 正文（像与核的定义及其后的问题："如果已知一个线性映射的表示矩阵，那么它的像空间和核空间的维数如何确定？"） | 提炼 |
| 反例/边界 | 教材 §4.4 正文（例 4.4.2 的解法要点）+ 习题 4.4 第 9 题（无限维反例） | 摘录并标注为习题来源 |
| 页码 | 教材目录 §4.4（p.200）与 §4.5 起始页（p.205） | 推断节末页 p.204 |