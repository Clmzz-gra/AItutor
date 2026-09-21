---
type: 节
formal: true
subject: 高等代数
created: 2026-09-21
updated: 2026-09-21
tags: [math, 高等代数]
chapter: 4
section: 4.2
---
# Sec4.2 线性映射的运算

> 定位：在 $\mathcal{L}(V,U)$ 上定义加法、数乘与复合，证明它是线性空间；在 $\mathcal{L}(V)$ 上进一步证明它是**代数**——乘法就是映射的复合。
> 教材：谢启鸿、姚慕生、吴泉水《高等代数学》第四版 §4.2（p.187–190）

> [!info] 关联笔记
> - 父级：[[Ch4 线性映射]]
> - 前置：[[Sec4.1 线性映射的概念]] ｜ 后续：[[Sec4.3 线性映射与矩阵]]

---

## 来龙（为什么需要它）

- **类比已知**：在例 4.1.3 中，任意一个 $m\times n$ 矩阵 $A$ 都可以定义一个从 $n$ 维列向量空间到 $m$ 维列向量空间的线性映射 $\varphi(\alpha)=A\alpha$。如果另有一个 $m\times n$ 矩阵 $B$，它定义的线性映射是 $\psi(\alpha)=B\alpha$，注意到矩阵之间存在的运算，我们可以定义这两个映射的加法 $(\varphi+\psi)(\alpha)=(A+B)\alpha$，也可以定义数乘 $(k\varphi)(\alpha)=kA\alpha$。
- **解决新问题**：教材由此提出——"**对一般的线性映射，我们是否也可以定义它们的加法和数乘呢？**" 答案是肯定的：只要**逐点**定义即可。
- **理论/应用需要**：定义了加法和数乘之后，从 $V$ 到 $U$ 的线性映射全体 $\mathcal{L}(V,U)$ 就有了线性空间结构；而在 $V=U$ 的情形，还能再定义一个乘法（映射的复合），从而得到**代数**。这个结构在 §4.3 被证明与矩阵代数完全同构——这正是本章"几何 ↔ 代数"翻译的核心。

## 主体（核心内容）

**知识点清单**（来自教材 §4.2 正文，逐条列，标 `重点`/`难点`/`考点` 标签）

- 定义 4.2.1：线性映射的加法与数乘 `重点`
- $\varphi+\psi$ 与 $k\varphi$ 仍是线性映射
- 命题 4.2.1：$\mathcal{L}(V,U)$ 是 $\mathbb{K}$ 上的线性空间 `重点` `考点`
- 共轭空间 $V^*$ 与对偶空间
- $\mathcal{L}(V)$ 的记号与其中的乘法（映射的复合）
- 定义 4.2.2：代数（含恒等元）`重点` `难点`
- 定理 4.2.1：$\mathcal{L}(V)$ 是 $\mathbb{K}$ 上的代数 `重点` `考点`
- 线性变换的幂：$\varphi^n\circ\varphi^m=\varphi^{n+m}$，$(\varphi^n)^m=\varphi^{nm}$
- 逆变换与负数次幂：$\varphi^{-n}=(\varphi^{-1})^n$，$\varphi^{-n}=(\varphi^n)^{-1}$，$\varphi^0=I_V$
- 复合不满足交换律：一般 $\varphi\circ\psi\neq\psi\circ\varphi$ `重点` `难点`
- 可逆变换的运算：$(\varphi\circ\psi)^{-1}=\psi^{-1}\circ\varphi^{-1}$，$(k\varphi)^{-1}=k^{-1}\varphi^{-1}$

**关键定义与结论**（教材原述，逐条列）

- **定义 4.2.1（线性映射的加法与数乘）**：设 $\varphi,\psi$ 是 $\mathbb{K}$ 上线性空间 $V\to U$ 的线性映射，定义 $\varphi+\psi$ 为 $V\to U$ 的映射：
  $$(\varphi+\psi)(\alpha)=\varphi(\alpha)+\psi(\alpha),\qquad\alpha\in V.$$
  若 $k\in\mathbb{K}$，定义 $k\varphi$ 为 $V\to U$ 的映射：
  $$(k\varphi)(\alpha)=k\varphi(\alpha),\qquad\alpha\in V.$$
  - 读法：$\varphi+\psi$ 读作"$\varphi$ 与 $\psi$ 的和"；$k\varphi$ 读作"$k$ 与 $\varphi$ 的数乘"。
  - **容易验证 $\varphi+\psi$ 是线性映射**。证明：
    $$(\varphi+\psi)(k\alpha+l\beta)=\varphi(k\alpha+l\beta)+\psi(k\alpha+l\beta)=k\varphi(\alpha)+l\varphi(\beta)+k\psi(\alpha)+l\psi(\beta)=k(\varphi+\psi)(\alpha)+l(\varphi+\psi)(\beta).$$
    同理可证明 $k\varphi$ 也是线性映射。
- **命题 4.2.1**：设 $\mathcal{L}(V,U)$ 是 $V\to U$ 的线性映射全体，则在上述线性映射的加法及数乘定义下，$\mathcal{L}(V,U)$ 是 $\mathbb{K}$ 上的线性空间。特别，$V\to\mathbb{K}$ 的所有线性函数全体构成一个线性空间。
  - 教材说明：这个命题的证明很容易，只需按照线性空间的定义逐条验证即可，**证明留给读者**。
- **共轭空间与对偶空间**：若 $U=\mathbb{K}$，即把 $\mathbb{K}$ 看成是 $\mathbb{K}$ 上的一维空间，则 $V\to\mathbb{K}$ 的线性映射通常称为 $V$ 上的**线性函数**。$V$ 上所有的线性函数构成的线性空间通常称为 $V$ 的**共轭空间**，记为 $V^*$。当 $V$ 是有限维空间时，$V^*$ 也称为 $V$ 的**对偶空间**。
- **$\mathcal{L}(V)$ 与其中的乘法**：若 $V=U$，我们用 $\mathcal{L}(V)$ 来记 $\mathcal{L}(V,V)$，即 $V$ 上线性变换全体构成的线性空间。这时在 $\mathcal{L}(V)$ 上，除了加法和数乘运算外，还有乘法运算，**这个乘法就是映射的复合**。
- **定义 4.2.2（代数）**：设 $A$ 是数域 $\mathbb{K}$ 上的线性空间，如果在 $A$ 上定义了一个乘法"$\cdot$"（通常可以省略），使对任意的 $A$ 中元素 $a,b,c$ 及 $\mathbb{K}$ 中元素 $k$，适合下列条件：
  (1) 乘法结合律：$a\cdot(b\cdot c)=(a\cdot b)\cdot c$；
  (2) 存在 $A$ 中元 $e$，使对一切 $a\in A$ 均有 $e\cdot a=a\cdot e=a$；
  (3) 分配律：$a\cdot(b+c)=a\cdot b+a\cdot c$，$(b+c)\cdot a=b\cdot a+c\cdot a$；
  (4) 乘法与数乘的相容性：$(ka)\cdot b=k(a\cdot b)=a\cdot(kb)$，
  则称 $A$ 是数域 $\mathbb{K}$ 上的**代数**，元素 $e$ 称为 $A$ 的**恒等元**。
  - 注（教材）：$A$ 的恒等元常常用 $1$ 表示，注意不要与数 $1$ 混淆。
- **定理 4.2.1**：设 $V$ 是数域 $\mathbb{K}$ 上的线性空间，则 $\mathcal{L}(V)$ 是 $\mathbb{K}$ 上的代数。
  - 证明要点：由命题 4.2.1，$\mathcal{L}(V)$ 是 $\mathbb{K}$ 上的线性空间。逐条验证定义 4.2.2：
    (1) 乘法结合律就是映射复合的结合律；
    (2) 恒等元是 $\mathbf{1}_V$，因为 $\mathbf{1}_V\circ\varphi=\varphi\circ\mathbf{1}_V=\varphi$；
    (3) 分配律：$(\varphi_1\circ(\varphi_2+\varphi_3))(\alpha)=\varphi_1(\varphi_2(\alpha)+\varphi_3(\alpha))=\varphi_1(\varphi_2(\alpha))+\varphi_1(\varphi_3(\alpha))=(\varphi_1\circ\varphi_2+\varphi_1\circ\varphi_3)(\alpha)$，同理可证另一个；
    (4) 相容性：$((k\varphi)\circ\psi)(\alpha)=(k\varphi)(\psi(\alpha))=k(\varphi(\psi(\alpha)))=k((\varphi\circ\psi)(\alpha))$，从而 $(k\varphi)\circ\psi=k(\varphi\circ\psi)$，同理 $\varphi\circ(k\psi)=k(\varphi\circ\psi)$。
- **线性变换的幂**：在 $\mathcal{L}(V)$ 中，定义线性变换 $\varphi$ 的 $n$ 次幂为 $n$ 个 $\varphi$ 的复合，则不难验证
  $$\varphi^n\circ\varphi^m=\varphi^{n+m},\qquad(\varphi^n)^m=\varphi^{nm}.$$
- **逆变换与负数次幂**：若 $\varphi$ 是双射，即为 $V$ 上的自同构，则 $\varphi^{-1}$ 也是 $V$ 上的线性变换（也是自同构），称 $\varphi^{-1}$ 为 $\varphi$ 的**逆变换**。如定义 $\varphi^{-n}=(\varphi^{-1})^n$，则不难验证 $\varphi^{-n}=(\varphi^n)^{-1}$。这时定义 $\varphi^0=I_V$，则 $\varphi^n\circ\varphi^m=\varphi^{n+m}$ 对一切整数均成立。
  - **但需注意 $\varphi$ 的负数次幂仅对自同构（又称可逆变换或非异变换）有意义。**
- **复合不满足交换律**：读者需要特别注意的是，**线性变换的复合通常不满足交换律**，即一般来说
  $$\varphi\circ\psi\neq\psi\circ\varphi.$$
  因此一般来说，$(\varphi\circ\psi)^n\neq\varphi^n\circ\psi^n$。
- **可逆变换的运算**：如果 $\varphi$ 与 $\psi$ 都是可逆线性变换，则 $\varphi\circ\psi$ 也是可逆线性变换，且
  $$(\varphi\circ\psi)^{-1}=\psi^{-1}\circ\varphi^{-1}.$$
  对任一非零数 $k$，若 $\varphi$ 可逆，则 $k\varphi$ 也可逆，且
  $$(k\varphi)^{-1}=k^{-1}\varphi^{-1}.$$
  （读者不难自己验证上述结论。）
- **反例 / 边界**：
  - **复合不可交换是最重要的边界**：由它直接推出 $(\varphi\circ\psi)^n\neq\varphi^n\circ\psi^n$ 一般成立。教材 §4.2 习题 3 给出一个经典例子：设 $V$ 是实系数多项式全体构成的实线性空间，$D(f(x))=\dfrac{\mathrm{d}}{\mathrm{d}x}f(x)$，$S(f(x))=\displaystyle\int_0^xf(t)\,\mathrm{d}t$，则 $D,S$ 均为线性变换且 $DS=I_V$，但 $SD\neq I_V$——**这说明"单侧逆"不足以成为可逆变换**（与命题 4.1.1 要求的双侧逆对照）。
  - **负数次幂只对自同构有意义**：对不可逆的线性变换，$\varphi^{-1}$ 不存在，$\varphi^{-n}$ 无从定义。
  - **$\mathcal{L}(V,U)$ 与 $\mathcal{L}(V)$ 的差别**：前者只有加法与数乘（线性空间），后者才有乘法（代数）——因为只有 $V\to V$ 的映射才能与自身复合。

**核心洞察**：这一节真正要说的是——**线性映射本身也可以当成"向量"**。它们之间可以相加、可以数乘，全体构成一个线性空间 $\mathcal{L}(V,U)$；而在 $V=U$ 时，复合又给出一乘法，使它成为**代数**。这一步的意义在 §4.3 兑现：$\mathcal{L}(V,U)$ 与矩阵空间 $M_{m\times n}(\mathbb{K})$ 同构，$\mathcal{L}(V)$ 与 $M_n(\mathbb{K})$ 作为代数同构——**矩阵乘法就是映射复合的代数影子**。

## 去脉（学完去哪）

- **本章内**：§4.3 的定理 4.3.2 证明 $T(\psi\varphi)=T(\psi)T(\varphi)$——本节的"复合是乘法"在那里被翻译成"矩阵乘法"；§4.4 的像与核是线性变换的子空间，与本节的结构无关但同属一个框架。
- **后续章节**：Ch6 中 $\varphi$ 的极小多项式（见 Ch6 §6.3）就是把 $\mathcal{L}(V)$ 的乘法（复合）用到 $\varphi$ 的幂上；Ch7 §7.8 的矩阵函数是同一思想在矩阵代数中的展开；Ch10 §10.1 的对偶空间 $V^*$ 直接引用本节的定义。
- **应用**：算子代数（泛函分析）；微分算子与积分算子的复合次序（$DS\neq SD$）在微分方程中反复出现。

## 防跳跃

- [ ] 命题 4.2.1 的证明教材留给了读者——需要逐条验证线性空间八条公理，注意零元是**零映射**，负元是 $-\varphi$。
- [ ] 定义 4.2.2 的恒等元 $e$ 在 $\mathcal{L}(V)$ 中就是恒等变换 $\mathbf{1}_V$；教材提醒"不要与数 $1$ 混淆"。
- [ ] 为什么 $\mathcal{L}(V)$ 的乘法（复合）不满足交换律，而加法满足？需要举出具体的 $\varphi,\psi$ 使 $\varphi\circ\psi\neq\psi\circ\varphi$。
- [ ] 习题 4.2 第 3 题的 $DS=I_V$ 但 $SD\neq I_V$：需要说明 $SD$ 把 $f(x)$ 映成什么，从而看出它不是恒等变换。
- [ ] 习题 4.2 第 5 题（$\varphi^{m-1}(\alpha)\neq\mathbf{0}$、$\varphi^m(\alpha)=\mathbf{0}$ 则 $\alpha,\varphi(\alpha),\cdots,\varphi^{m-1}(\alpha)$ 线性无关）是幂与线性无关结合的标准题型。

## 待填充

- [ ] 完整证明展开
- [ ] 例题（原始信息 → 代入 → 结果 → 结论）
- [ ] 自测题（按 `tutor` skill 的检验回路生成）

## 来源与映射

| 本节点内容 | 来源 | 处理 |
|---|---|---|
| 知识点清单 | 教材 §4.2 正文标题与定义、定理名（定义 4.2.1–4.2.2、命题 4.2.1、定理 4.2.1、公式 (4.2.1)–(4.2.2)） | 提取 |
| 定位/来龙 | 教材 §4.2 开头段（由矩阵定义的线性映射能否定义加法与数乘） | 提炼 |
| 反例/边界 | 教材 §4.2 正文（复合不满足交换律、负数次幂仅对自同构有意义）+ 习题 4.2 第 3 题（$DS=I_V$ 但 $SD\neq I_V$） | 摘录并标注为习题来源 |
| 页码 | 教材目录 §4.2（p.187）与 §4.3 起始页（p.191） | 推断节末页 p.190 |