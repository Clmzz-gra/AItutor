---
type: 节
formal: true
subject: 实变函数与泛函分析
created: 2026-09-21
updated: 2026-09-21
tags: [math, 实变函数与泛函分析]
chapter: 3
section: 3.2
---

# Sec3.2 Lebesgue 积分的极限定理

> 定位：回答「什么时候能把极限搬进积分号」——用 Levi 单调收敛定理、Fatou 引理、Lebesgue 控制收敛定理串成一条「谁推谁」的逻辑链，并用它刻画黎曼可积性。
> 教材：郭懋正《实变函数与泛函分析》§3.2（p.111–129）
> 来源：旧讲解包《Ch5 积分论》§四–§六；郭版教材 §3.2.3（新写补缺）

> [!info] 关联笔记
> - 父级：[[Ch3 Lebesgue 积分]]
> - 前置：[[Sec3.1 Lebesgue 可测函数的积分]] ｜ 后续：[[Sec3.3 重积分与累次积分]]
> - 概念：[[概念-测度与黎曼积分的类比]]

---

## 来龙（为什么需要它）

- **类比已知**：黎曼框架下想交换极限与积分，通常要求 $\{f_n\}$ **一致收敛**——这个条件既苛刻又难验证：它要求所有 $x$ 的收敛速度一致，而实际问题里函数往往在某些点附近收敛得极慢。
- **解决新问题**：本节要把「一致收敛」换成「**逐点收敛 + 一个可积的控制函数**」。这是勒贝格积分最大的战果：控制函数 $F$ 只要求 $\int F<\infty$，不要求任何一致性的量。同时还要回答一个反向问题——**黎曼积分到底能积哪些函数**？答案是「不连续点集零测」（Lebesgue 判据），而这个判据的证明恰恰要用本节的极限定理。
- **理论/应用需要**：Ch4 的 $L^p$ 完备性、傅里叶级数的收敛、概率论里「期望与极限交换」、PDE 中「积分号下求导」，全都建立在本节的三个定理上。**可以说：§3.1 造出了积分，§3.2 才让它变得好用。**

## 主体（核心内容）

### 3.2.1 Lebesgue 积分与极限运算的交换定理

#### 逻辑链总览（先看清「谁推谁」）

三个定理不是并列的三件事，而是一条**单链**——每个定理都由前一个推出：

```
【地基】§3.1 的积分定义（上确界）+ 简单函数积分对递增区域列的连续性
   ↓ 直接证明
【定理 1】Levi 单调收敛定理：0 ≤ f₁ ≤ f₂ ≤ ⋯，fₙ ↑ f  ⟹  ∫fₙ → ∫f
   ↓ 对 gₙ = inf{fₖ : k ≥ n} 用 Levi（gₙ 递增且 gₙ ≤ fₙ）
【定理 2】Fatou 引理：∫ liminf fₙ ≤ liminf ∫fₙ        （只有"≤"，方向不可反）
   ↓ 对非负函数列 (2F − |fₙ − f|) 用 Fatou，控制函数 F 保证非负性
【定理 3】Lebesgue 控制收敛定理：|fₙ| ≤ F ∈ L，fₙ → f a.e.  ⟹  ∫fₙ → ∫f
   ↓ 取常数控制函数 F ≡ M（需 mE < ∞）
【推论 4】有界收敛定理
   ↓ 用 Riesz 定理把"依测度收敛"换成"a.e. 收敛的子列"
【推论 5】依测度收敛版本
```

**另外两条支线**（都由主链推出）：
- 非负函数列的**逐项积分**（$\int\sum f_n=\sum\int f_n$）是 **Levi** 的直接推论（部分和递增）；
- **积分号下求导**是 **LDCT** 的直接推论（差商被 $F$ 控制）。

> **反向也成立（这一点常被忽略）**：**Fatou 引理可以反过来推出 Levi 定理**。若 $0\leqslant f_n\uparrow f$，Fatou 给出 $\int f\leqslant\varliminf\int f_n$；而单调性给出 $\int f_n\leqslant\int f$，故 $\varlimsup\int f_n\leqslant\int f$；两个方向夹逼得 $\lim\int f_n=\int f$。**所以 Levi 与 Fatou 是等价的**——它们是同一件事的「严格版」与「宽松版」。但 LDCT **不能**由 Levi 直接推出，它必须借道 Fatou，这是控制函数登场的地方。

#### 定理 1：Levi 单调收敛定理（本章第一定理，推导全程）

**定理 1（Levi）** 设 $0\leqslant f_1\leqslant f_2\leqslant\cdots$ 是 $E$ 上的非负可测函数列，$f=\lim_n f_n$（逐点），则
$$\lim_{n\to\infty}\int_E f_n(x)\,dx=\int_E f(x)\,dx .$$

**证明（一正一反两个方向）**

- **方向 $\leqslant$（容易）**：*因为* $f_n\leqslant f_{n+1}\leqslant f$，由单调性（Sec3.1 定理 4）得 $\int_E f_n\leqslant\int_E f_{n+1}\leqslant\int_E f$，故 $\lim_n\int_E f_n\leqslant\int_E f$。
- **方向 $\geqslant$（用简单函数「卡」）**：任取简单函数 $\varphi$，$0\leqslant\varphi\leqslant f$，任取常数 $0<c<1$。令
  $$E_n=E[f_n\geqslant c\varphi].$$
  *因为* $f_n\uparrow f$ 且 $c<1$，有 $E_n\uparrow E$：对 $x\in E$，只要 $f_n(x)\to f(x)$，终有 $f_n(x)\geqslant c\varphi(x)$（因为 $\varphi(x)\leqslant f(x)$，而 $c<1$ 留出了缝隙）。
  于是
  $$\int_E f_n\,dx\geqslant\int_{E_n}f_n\,dx\geqslant\int_{E_n}c\varphi\,dx=c\int_{E_n}\varphi\,dx .$$
  由简单函数积分对递增区域列的连续性（Sec3.1 定理 1(3)），$\int_{E_n}\varphi\,dx\to\int_E\varphi\,dx$。故
  $$\lim_n\int_E f_n\,dx\geqslant c\int_E\varphi\,dx .$$
  *因为* $c$ 是任意小于 $1$ 的数，令 $c\to1$；再由 $\varphi$ 任意，对一切 $\varphi\leqslant f$ 取上确界得 $\lim_n\int_E f_n\geqslant\int_E f$。双向夹逼即得结论。$\square$

> **为什么引入 $c<1$？** 这是「留一点余量」的标准技术：$f_n$ 未必逐点 $\geqslant\varphi$（$\varphi$ 可能在某个单点上恰好等于 $f$，而 $f_n$ 永远差一点），但乘上 $c<1$ 后终将超过。$c$ 的角色就是给「严格超过」留出缝隙。
>
> **停顿自问**：如果把 $c$ 取成 $1$，$E_n=E[f_n\geqslant\varphi]$ 还会递增到 $E$ 吗？——不会。取 $E=[0,1]$、$f\equiv1$、$\varphi\equiv1$、$f_n=1-\frac1n$，则 $f_n<1=\varphi$ 处处成立，$E_n=\varnothing$ 对所有 $n$ 成立，永远长不到 $E$。**$c<1$ 不是技术细节，而是证明成立的必要条件。**

#### 推论：线性与逐项积分

**定理 2（线性）** $\int_E(\alpha f+\beta g)\,dx=\alpha\int_E f\,dx+\beta\int_E g\,dx$（$\alpha,\beta\geqslant0$，$f,g$ 非负可测）。

**证明**：用可测函数的逼近定理（Ch2 §2.2）取递增简单函数列 $\varphi_n\uparrow f$、$\psi_n\uparrow g$，则 $\alpha\varphi_n+\beta\psi_n\uparrow\alpha f+\beta g$；*因为* 简单函数积分线性，对两边用 Levi 定理即得。$\square$

**定理 3（逐项积分）** 对非负可测函数列 $\{f_n\}$，
$$\int_E\sum_{n=1}^{\infty}f_n(x)\,dx=\sum_{n=1}^{\infty}\int_E f_n(x)\,dx .$$

**证明**：令部分和 $g_n=\sum_{k=1}^{n}f_k$，*因为* $g_n\uparrow\sum_k f_k$ 且积分具有有限线性，用 Levi 定理把极限穿过积分号即得。$\square$

**注意**：定理 3 对**非负**函数列无条件成立；一旦允许变号，就必须附加 $\sum_n\int_E|f_n|<\infty$ 的条件（见下面的定理 8）。

#### 定理 4：Fatou 引理（极限进去只亏不赚）

**定理 4（Fatou）** 设 $\{f_n\}$ 是 $E$ 上的非负可测函数列，则
$$\int_E\varliminf_{n\to\infty}f_n(x)\,dx\leqslant\varliminf_{n\to\infty}\int_E f_n(x)\,dx .$$
（$\varliminf_n f_n$ 读作「$f_n$ 的**下极限**」，逐点取：$\varliminf_n f_n(x)=\lim_n\inf_{k\geqslant n}f_k(x)$。）

**证明（由 Levi 推出）**：令 $g_n(x)=\inf\{f_k(x):k\geqslant n\}$。*因为* $g_n$ 随 $n$ 递增、$g_n\leqslant f_{n+1}$（特别地 $g_n\leqslant f_n$ 的某一后继），且 $g_n\uparrow\varliminf f_n$，由 Levi 定理与单调性：
$$\int_E\varliminf_{n\to\infty}f_n\,dx=\int_E\lim_{n\to\infty}g_n\,dx=\lim_{n\to\infty}\int_E g_n\,dx\leqslant\varliminf_{n\to\infty}\int_E f_n\,dx .\qquad\square$$

**反例（$\leqslant$ 不能改成 $=$，必须会默写）** 在 $(0,\infty)$ 上取 $f_n=n\chi_{(0,1/n)}$。

- *因为* 每个固定的 $x>0$ 终有 $1/n<x$（只要 $n>1/x$），故 $f_n(x)=0$ 对足够大的 $n$ 成立，于是 $f_n\to0$，$\int_{(0,\infty)}\varliminf f_n\,dx=0$；
- 但 $\int_{(0,\infty)}f_n\,dx=n\cdot m(0,1/n)=n\cdot\frac1n=1$，故 $\varliminf_n\int f_n=1>0$。

**直观**：积分是「总量」，逐点极限看不住「质量逃到无穷远处或摊薄到无穷」的过程。**每点的函数值都趋于 $0$，但总质量 $1$ 一路向右逃逸。**

> **核心洞察**：Levi 与 Fatou 是一对——**单调递增时极限与积分完全可交换（Levi）；一般情形只保证「积分的下极限不小于下极限的积分」（Fatou）**。Fatou 的不等号方向永远指向「可能亏」，这个方向感在全章都要用到。

#### 定理 5：Lebesgue 控制收敛定理（本章核心定理，推导全程）

**定理 5（LDCT，Lebesgue Dominated Convergence Theorem）** 设 $\{f_n\}$ 在 $E$ 上可测，$F$ 是 $E$ 上非负 $L$ 可积函数，满足
$$|f_n(x)|\leqslant F(x)\ \text{a.e.},\qquad f_n(x)\to f(x)\ \text{a.e.},$$
则 $f_n,f\in L(E)$，且
$$\lim_{n\to\infty}\int_E|f_n-f|\,dx=0,\qquad \lim_{n\to\infty}\int_E f_n\,dx=\int_E f\,dx .$$

**证明（全部力气花在第一个等式上）**：令 $g_n=|f_n-f|$。*因为* $|f_n|\leqslant F$ 且 $f_n\to f$，极限函数也满足 $|f|\leqslant F$ a.e.，故 $g_n$ 非负可积、$g_n\leqslant2F$、$g_n\to0$ a.e.。

对非负函数列 $\{2F-g_n\}$ 用 **Fatou 引理**：
$$2\int_E F\,dx=\int_E\lim_n(2F-g_n)\,dx\leqslant\varliminf_n\int_E(2F-g_n)\,dx=2\int_E F\,dx-\varlimsup_n\int_E g_n\,dx .$$
*因为* $2\int_E F<\infty$（$F$ 可积），两边消去它得 $\varlimsup_n\int_E g_n\leqslant0$；又 $\int_E g_n\geqslant0$，故 $\lim_n\int_E g_n=0$。第二个等式由 $\left|\int_E f_n-\int_E f\right|\leqslant\int_E|f_n-f|$ 立即得到。$\square$

**为什么这个证明漂亮**：它把「差收敛到 $0$」包装成 Fatou 引理里「不会亏」的对象——**控制函数 $F$ 的作用不是摆设，它让 $2F-g_n\geqslant0$，Fatou 才敢出手**。若没有 $F$，$2F-g_n$ 可能变负，Fatou 的前提就不成立。

**反例（控制条件不可少——本章最高频的错误直觉）** 论断「$f_n\to f$ a.e. 且每个 $f_n$ 都 $L$ 可积，则 $\int f_n\to\int f$」是**错的**。用 Fatou 的反例检验：$f_n=n\chi_{(0,1/n)}$ 满足 $f_n\to0$ a.e.、$\int f_n=1<\infty$，但 $\int f_n=1\not\to0=\int f$。**缺的条件正是「可积控制函数」**：这里不存在 $F\in L(0,\infty)$ 使 $|f_n|\leqslant F$ a.e.（否则由 LDCT 必有 $\int f_n\to0$）。「逐点收敛 + 各元可积」不足以换序。

> **问**：既然 Fatou 引理能反过来推出 Levi 定理，为什么不干脆只用 Fatou，把 Levi 当成推论？
> **答**：*因为* 逻辑上 Levi 才是「从积分定义直接得到」的那一个——它的证明只用到上确界定义与简单函数积分对区域列的连续性，不需要任何别的极限定理。而 Fatou 与 LDCT 的证明都要绕回 Levi。把 Levi 当起点，整条链的依赖关系没有环、最清晰；反过来用 Fatou 证 Levi 虽然可行，却会让 Fatou 的证明无处落脚（它本身要靠 Levi）。**教科书选择 Levi 打头，是为了让证明的依赖图是一棵从定义长出来的树，而不是一个环。**

#### 推论 6：有界收敛定理

**推论 6（有界收敛）** 设 $mE<\infty$，$|f_n|\leqslant M$ a.e. 且 $f_n\to f$ a.e.，则 $\lim_n\int_E f_n\,dx=\int_E f\,dx$。

**证明**：*因为* 常值函数 $F\equiv M$ 在有限测度集 $E$ 上可积（$\int_E M=M\cdot mE<\infty$），直接套 LDCT。$\square$

**反例（$mE<\infty$ 不可少）** 在 $\mathbb{R}$ 上取 $f_n=\chi_{[n,n+1]}$。*因为* $|f_n|\leqslant1$ 一致有界、$f_n(x)\to0$ 对每点 $x$ 成立，故 $\int\lim f_n=0$；但 $\int_{\mathbb{R}}f_n\,dx=1$ 对一切 $n$ 成立。**原因**：控制函数 $F\equiv1$ 在 $\mathbb{R}$ 上**不**可积（$m\mathbb{R}=\infty$），LDCT 的前提被破坏。**有界本身从来不够，必须「有界 + 有限测度」或「可积控制函数」二者居其一。**

#### 推论 7：依测度收敛版本

**推论 7** 把 LDCT 中的「$f_n\to f$ a.e.」换成「$f_n\Rightarrow f$（依测度收敛）」，其余条件不变，结论不变。

**证明（子列论证）**：若 $\int_E|f_n-f|\,dx\not\to0$，则存在子列（仍记作 $n$）使 $\int_E|f_n-f|\,dx\geqslant\varepsilon_0>0$。*因为* 依测度收敛，由 Riesz 定理（Ch2 §2.3）可再取子列 a.e. 收敛到 $f$；对这个子列用定理 5 得 $\int_E|f_n-f|\to0$，与 $\geqslant\varepsilon_0$ 矛盾。$\square$

#### 定理 8：逐项积分与积分号下求导（支撑档）

**定理 8（变号情形的逐项积分）** 若 $\sum_n\int_E|f_n|\,dx<\infty$，则 $\sum_n f_n$ a.e. 收敛，和函数可积，且
$$\int_E\sum_{n=1}^{\infty}f_n\,dx=\sum_{n=1}^{\infty}\int_E f_n\,dx .$$

**证明**：令 $F=\sum_n|f_n|$。*因为* 各项非负，由逐项积分（定理 3）得 $\int_E F=\sum_n\int_E|f_n|<\infty$，故 $F$ 可积，从而 $F<\infty$ a.e.（Sec3.1 定理 5(2)），即级数 a.e. 绝对收敛；对部分和用 LDCT（控制函数 $F$）即得。$\square$

**定理 9（积分号下求导）** 设 $f(x,t)$ 对 a.e. 的 $x$ 关于 $t$ 可导，且 $\left|\frac{\partial}{\partial t}f(x,t)\right|\leqslant F(x)$（$F$ 可积），则
$$\frac{d}{dt}\int_E f(x,t)\,dx=\int_E\frac{\partial}{\partial t}f(x,t)\,dx .$$

**证明**：取 $h_n\to0$，令差商 $g_n(x)=\frac{1}{h_n}\bigl[f(x,t+h_n)-f(x,t)\bigr]$。*因为* 由微分中值定理 $|g_n|\leqslant F$，且 $g_n\to\frac{\partial f}{\partial t}$，直接套 LDCT。$\square$

#### 例题

**例题 1（LDCT 的标准用法）** 求 $\displaystyle\lim_{n\to\infty}\int_0^1\frac{nx}{1+n^2x^2}\,dx$。

- **原始信息**：$f_n(x)=\dfrac{nx}{1+n^2x^2}$ 在 $[0,1]$ 上连续，故可测。
- **找控制函数**：*因为* $1+n^2x^2\geqslant 2nx$（均值不等式），故 $0\leqslant f_n(x)\leqslant\frac12$。取 $F\equiv\frac12$，在有限测度集 $[0,1]$ 上可积。
- **求逐点极限**：$x=0$ 时 $f_n(0)=0$；$x>0$ 时 $f_n(x)=\dfrac{nx}{1+n^2x^2}\to0$。故 $f_n\to0$ a.e.。
- **结果**：由 LDCT，$\lim_{n\to\infty}\int_0^1 f_n\,dx=\int_0^1 0\,dx=0$。（直接计算 $(1/(2n))\ln(1+n^2)\to0$ 也得同一结果。）
- **结论**：**先找控制函数、再看逐点极限**，是这类题目的固定套路；控制函数可以很粗糙（这里 $F\equiv\frac12$），只要可积就行。

**例题 2（极限函数在零测集上被改写）** 求 $\displaystyle\lim_{n\to\infty}\int_0^1\frac{dx}{1+x^n}$。

- **原始信息**：$0<\dfrac{1}{1+x^n}\leqslant1$，故 $F\equiv1$ 在 $[0,1]$ 上可积。
- **求逐点极限**：$x\in[0,1)$ 时 $x^n\to0$，故 $\dfrac{1}{1+x^n}\to1$；$x=1$ 时恒为 $\frac12$。
- **结果**：极限函数 $f(x)=1$ 于 $[0,1)$、$f(1)=\frac12$——它与常函数 $1$ 只在一个零测集（单点 $\{1\}$）上不同，故 $\int_{[0,1]}f\,dx=1$。由 LDCT，$\lim_n\int_0^1\frac{dx}{1+x^n}=1$。
- **结论**：**积分看不见零测集上的差异**——这正是 LDCT 只要求「a.e. 收敛」而不是「处处收敛」的原因。

> **检验回路：讲给别人听（明天验收）**
> 1. **动机复述（必答）**：黎曼积分的两个缺陷 + §3.1 三步定义各解决什么；
> 2. 非负简单函数积分的定义、良定性（公共加细）与三条性质；
> 3. 非负可测函数积分的定义（上确界），为什么这样定义；
> 4. Sec3.1 定理 3(2)：$\int f=0\Rightarrow f=0$ a.e. 的 $\frac1n\chi_{A_n}$ 证明；
> 5. Levi 定理的完整证明，特别是 $c<1$ 的余量技巧；
> 6. Fatou 引理与 $n\chi_{(0,1/n)}$ 反例；
> 7. 「积分确定」与「$L$ 可积」的区别；
> 8. LDCT 的完整证明（Fatou 作用于 $2F-g_n$）与「控制函数不可少」的反例；
> 9. 黎曼可积 $\iff$ a.e. 连续；$\sin x/x$ 的边界。
>
> **卡壳对照表**
> - 卡在 **Levi 的 $c<1$** → 把 $E_n=E[f_n\geqslant c\varphi]$ 画出来，验证 $E_n\uparrow E$ 需要「$c<1$」与「逐点收敛」两件事同时成立；
> - 卡在 **LDCT 的证明** → 先复述 Fatou，再写下目标 $\int(2F-g_n)\to\int2F$ 与前提 $2F-g_n\geqslant0$，证明只是这两句的展开；
> - 卡在 **$\sin x/x$** → 只记结论链：$L$ 可积 $\iff|f|$ 可积；条件收敛的正负面积都无穷；
> - **主动建议**：把 Ch2 的叶戈罗夫定理与本节的 LDCT 连起来看——它们是同一句话「有限测度 / 可积控制把『几乎』换成『真正』」的两种实现。

### 3.2.2 黎曼可积性的刻画

> 本小节回答 Sec3.1 留下的问题：**黎曼积分到底能积哪些函数**？答案是「不连续点集零测」。证明必须放在这里，*因为* 它要用到 3.2.1 的有界收敛定理。

**先定义振幅**：设 $f$ 在 $[a,b]$ 上有界，对 $x\in[a,b]$ 令
$$\omega(x)=\lim_{\delta\to0^{+}}\ \sup\bigl\{|f(x')-f(x'')|:\ x',x''\in(x-\delta,x+\delta)\cap[a,b]\bigr\}$$
（读作「$f$ 在点 $x$ 处的**振幅**」）。**关键事实**：$\omega(x)=0\iff f$ 在 $x$ 连续；$\omega(x)$ 越大，$f$ 在 $x$ 附近摆动越剧烈。

**定理 10（Lebesgue 判据）** 有界函数 $f$ 在 $[a,b]$ 上黎曼可积 $\iff f$ 在 $[a,b]$ 上 a.e. 连续（即不连续点集是零测集）。

**完整论证**：

1. **取一列越来越细的分法**：对每个 $n$ 取 $[a,b]$ 的分法 $T^{(n)}:a=x_0^{(n)}<x_1^{(n)}<\cdots<x_{k_n}^{(n)}=b$，使最大区间长 $\delta(T^{(n)})\to0$。在第 $i$ 个小区间 $I_i^{(n)}=[x_{i-1}^{(n)},x_i^{(n)})$ 上记 $M_i^{(n)}=\sup_{I_i^{(n)}}f$、$m_i^{(n)}=\inf_{I_i^{(n)}}f$（*因为* $f$ 有界，这些都是有限实数）。
2. **造逼近振幅的函数**：令
   $$h_n(x)=M_i^{(n)}-m_i^{(n)}\quad\text{当 }x\in I_i^{(n)} .$$
   *因为* $h_n$ 在每块上取常值，$h_n$ 是非负简单函数，于是它的积分就是达布大和与下和之差：
   $$(L)\int_{[a,b]}h_n\,dx=\sum_{i=1}^{k_n}\bigl(M_i^{(n)}-m_i^{(n)}\bigr)\,\Delta x_i^{(n)}=\overline{S}(T^{(n)})-\underline{S}(T^{(n)}).$$
   *因为* 分法越来越细，$\overline{S}(T^{(n)})\to\overline{\int_a^b}f$、$\underline{S}(T^{(n)})\to\underline{\int_a^b}f$（达布上、下积分）。
3. **取极限**：*因为* $f$ 有界，$0\leqslant h_n\leqslant 2M$（$M=\sup_{[a,b]}|f|<\infty$），即 $\{h_n\}$ 被**可积控制函数** $F\equiv2M$ 控制（$m[a,b]<\infty$）；又当分法无限变细时 $h_n(x)\to\omega(x)$ a.e.（在 $f$ 的连续点处，落得足够深的那个小区间上 $M_i-m_i\to0$）。用**有界收敛定理（推论 6）**：
   $$(L)\int_{[a,b]}\omega\,dx=\lim_{n\to\infty}(L)\int_{[a,b]}h_n\,dx=\overline{\int_a^b}f\,dx-\underline{\int_a^b}f\,dx .$$
4. **收口**：$\omega\geqslant0$ 且可测。于是
   $$f\ \text{黎曼可积}\iff\overline{\int_a^b}f=\underline{\int_a^b}f\iff(L)\int_{[a,b]}\omega\,dx=0\iff\omega=0\ \text{a.e.}\iff f\ \text{a.e. 连续}.$$
   最后一步用的是 Sec3.1 定理 3(2)：非负函数积分为 $0$ 蕴含它 a.e. 为 $0$。$\square$

**读法**：黎曼可积的障碍只有一个——**不连续点太多**；而「太多」的精确含义是「测度不为零」。狄利克雷函数处处不连续 $\Rightarrow$ 不可积；单调函数的不连续点至多可数 $\Rightarrow$ 必可积。

**例题（用判据判断一个「怪函数」是否可积）** 判断黎曼函数
$$R(x)=\begin{cases}\dfrac1q,& x=\dfrac pq\ \text{（}p,q\ \text{为互素正整数，}q>0\text{）},\\[4pt] 0,& x\ \text{为无理数}\end{cases}$$
在 $[0,1]$ 上是否黎曼可积，并求积分值。

- **原始信息**：$R$ 在有理点取 $1/q$，在无理点取 $0$；$0\leqslant R\leqslant1$，有界。
- **找不连续点**：任取无理点 $x_0$ 与 $\varepsilon>0$。*因为* 满足 $1/q\geqslant\varepsilon$ 的有理数只有有限多个（要求 $q\leqslant1/\varepsilon$，$p$ 又被 $[0,1]$ 限制），可取 $x_0$ 的一个邻域把这些点全部避开；于是在该邻域内 $|R(x)-R(x_0)|=|R(x)|<\varepsilon$，故 $R$ 在 $x_0$ 连续。反之在有理点 $x_0=p/q$ 处 $R(x_0)=1/q>0$，而任意邻域内都有无理点使 $R=0$，故 $R$ 在 $x_0$ 不连续。
- **代入判据**：不连续点集 $=\mathbb{Q}\cap[0,1]$，它是可数集，故测度为 $0$，由定理 10 知 $R$ 黎曼可积。
- **结果与结论**：$R=0$ a.e.，故 $(R)\int_0^1 R\,dx=(L)\int_{[0,1]}R\,dx=0$。**函数可以不连续于无穷多个点，只要这些点「不多」（零测）就仍可积。**

**反例（判据中「零测」不能放宽为「可数」或「有限」以外的东西——也不能收紧）** 狄利克雷函数 $D=\chi_{\mathbb{Q}\cap[0,1]}$ 处处不连续，不连续点集 $[0,1]$ 的测度为 $1\neq0$，故 $D$ **不**黎曼可积；但它 a.e. 等于 $0$，故勒贝格可积且积分为 $0$。**这条反例说明判据的两侧都被用到了**：测度为零 ⟹ 可积（黎曼函数），测度不为零 ⟹ 不可积（狄利克雷函数）。

### 3.2.3 $L(X,\mathcal{F},\mu)$ 中积分的极限定理

> 本小节是**新写补缺**（郭版 §3.2.3）：旧讲解包只讲 $\mathbb{R}^n$ 上的极限定理，抽象测度空间上的版本是郭版新增内容。郭版的处理方式是「只叙述结果」——*因为* 证明与 $\mathbb{R}^n$ 情形**逐字雷同**，只是把 $m$、$dx$ 换成 $\mu$、$\mu(\mathrm{d}x)$。这恰恰体现了 §3.1.4 抽象化的价值：**证明一次，处处可用。**

**定理 11（Lebesgue 基本定理，郭版定理 3.2.11）** 设 $\{f_n\}$ 是测度空间 $(X,\mathcal{F},\mu)$ 上的非负可测函数列，$f(x)=\sum_{n=1}^{\infty}f_n(x)$，则
$$\int_X f(x)\,\mu(\mathrm{d}x)=\sum_{n=1}^{\infty}\int_X f_n(x)\,\mu(\mathrm{d}x).$$

**推论 12（可数可加性，郭版推论 3.2.12）** 若 $\{A_n\}$ 是 $X$ 的互不相交可测子集，$X=\bigcup_{n=1}^{\infty}A_n$，且 $f$ 在 $X$ 上有积分，则 $f$ 在每个 $A_n$ 上都有积分；特别地当 $f\in L(X)$ 时 $f\in L(A_n)$，且
$$\int_X f(x)\,\mu(\mathrm{d}x)=\sum_{n=1}^{\infty}\int_{A_n}f(x)\,\mu(\mathrm{d}x).$$

**定理 13（Fatou 引理，郭版定理 3.2.13）** 若 $\{f_n\}$ 是 $(X,\mathcal{F},\mu)$ 上非负可测函数列，则
$$\int_X\varliminf_{n\to\infty}f_n(x)\,\mu(\mathrm{d}x)\leqslant\varliminf_{n\to\infty}\int_X f_n(x)\,\mu(\mathrm{d}x).$$

**定理 14（控制收敛定理，郭版定理 3.2.14）** 设 $\{f_n\}\subset\mathfrak{M}(X,\mathcal{F},\mu)$ 且 $f_n\to f$，$\mu$-a.e.。若存在 $F\in L(X)$ 使 $|f_n(x)|\leqslant F(x)$ 对一切 $n$ 成立（$\mu$-a.e.），则 $f_n\in L(X)$、$f\in L(X)$，且
$$\lim_{n\to\infty}\int_X f_n(x)\,\mu(\mathrm{d}x)=\int_X f(x)\,\mu(\mathrm{d}x).$$
$F$ 称为函数列 $\{f_n\}$ 的**控制函数**。

**推论 15（依测度收敛版本，郭版推论 3.2.15）** 把定理 14 中的「$\mu$-a.e. 收敛」换成「依测度 $\mu$ 收敛」，结论不变。

**推论 16（有界收敛定理，郭版推论 3.2.16）** 设 $\mu(X)<\infty$，$\{f_n\}\subset L(X)$ 且**一致有界**：存在常数 $M>0$ 使 $|f_n(x)|\leqslant M$ 对一切 $n$、一切 $x\in X$ 成立。则当 $f_n\to f$（$\mu$-a.e.）或 $f_n$ 依测度 $\mu$ 收敛到 $f$ 时，均有
$$\lim_{n\to\infty}\int_X f_n(x)\,\mu(\mathrm{d}x)=\int_X f(x)\,\mu(\mathrm{d}x).$$

**例题（抽象定理的「化身」：计数测度上的极限定理）** 在 $(\mathbb{N},2^{\mathbb{N}},\mu)$（$\mu$ 为计数测度）上，设对每个 $n$ 有数列 $a^{(n)}=\{a^{(n)}_k\}_{k\geqslant1}$，满足 $|a^{(n)}_k|\leqslant b_k$ 且 $\sum_k b_k<\infty$，并对每个固定的 $k$ 有 $a^{(n)}_k\to a_k$。求 $\lim_n\sum_k a^{(n)}_k$。

- **原始信息**：把 $a^{(n)}$ 看成 $\mathbb{N}$ 上的函数 $f_n(k)=a^{(n)}_k$（每点可测，故 $f_n$ 可测）。
- **翻译条件**：由 §3.1.4 的例题，$\int_{\mathbb{N}}f_n\,\mu(\mathrm{d}x)=\sum_k a^{(n)}_k$；控制条件 $|f_n|\leqslant F$ 翻译成 $|a^{(n)}_k|\leqslant b_k$，$F\in L(\mathbb{N})$ 翻译成 $\sum_k b_k<\infty$；逐点收敛翻译成「对每个 $k$ 有 $a^{(n)}_k\to a_k$」。
- **代入定理 14**：$\lim_n\sum_k a^{(n)}_k=\sum_k a_k$。
- **结论**：**「积分与极限交换」在计数测度下就是「级数与逐项极限交换」**——这就是分析教材里「一致控制 $\sum|b_k|<\infty$ 下可逐项取极限」那条定理的真正来源。**抽象测度空间的极限定理不是新的数学，而是把所有旧定理收进了一个框子。**

**反例（抽象情形下 Fatou 的 $\leqslant$ 同样不能改 $=$）** 仍在计数测度空间上取 $f_n(k)=\delta_{n,k}$（即 $f_n(n)=1$，其余为 $0$）。

- *因为* 对每个固定的 $k$，当 $n>k$ 时 $f_n(k)=0$，故 $f_n\to0$ 逐点，$\int_{\mathbb{N}}\varliminf f_n\,\mu(\mathrm{d}x)=0$；
- 但 $\int_{\mathbb{N}}f_n\,\mu(\mathrm{d}x)=\sum_k\delta_{n,k}=1$ 对一切 $n$ 成立，故 $\varliminf_n\int f_n=1>0$。

**这正是 $n\chi_{(0,1/n)}$ 的抽象翻版**：质量「逃到第 $n$ 个坐标上」而不是「逃到无穷远处」，但逐点极限同样看不见它。**结论：Fatou 的方向性在任何测度空间上都不可改进。**

> **这一节真正要说的是什么**：勒贝格积分的力量浓缩在 LDCT 里——**用一个可积控制函数，换掉黎曼时代苛刻的一致收敛**。三个定理不是三个并列的工具，而是一条从定义出发的单链：**Levi 是根，Fatou 是它的一般化，控制收敛是 Fatou 加上控制函数**。把 $m$ 换成任意测度 $\mu$，整条链一字不改地成立。

## 去脉（学完去哪）

- **回填 Sec3.1**：Sec3.1 的定理 9（黎曼可积 $\Rightarrow$ 勒贝格可积）用到的正是本节的有界收敛定理——两节是咬合的。
- **$L^p$ 空间**（见 Ch4）：Riesz–Fischer 完备性定理的证明要用 LDCT 从收敛子列中抽出 a.e. 收敛的子列；Hölder 与 Minkowski 不等式也要用 Fatou 取极限。
- **概率论**：控制收敛定理就是「期望与极限交换」的标准工具；有界收敛定理是「$P(\Omega)=1<\infty$ 时一致有界 ⟹ 期望收敛」。**概率空间是 $\mu(X)=1$ 的特例，本节的推论 16 在那里永远可用。**
- **傅里叶分析**（见 Ch4 §4.3）：傅里叶变换的连续性与可微性、$L^2$ 中的收敛，都靠「积分号下取极限 / 求导」。
- **PDE 与变分法**：定理 9（积分号下求导）是研究解关于参数光滑性的日常工具。
- **一句话**：本节把「积分」从一个静态的定义变成了一个**能通过极限的算子**——这才是它能支撑起整个泛函分析的原因。

## 防跳跃

- [ ] Riesz 定理（依测度收敛 ⟹ 存在 a.e. 收敛子列）的证明——推论 7 只引用未展开，详见 Ch2 §2.3
- [ ] 定理 8 中级数 $\sum_n f_n$ a.e. 收敛的完整论证（本节只给「$F<\infty$ a.e.」这一句）
- [ ] 反向 Fatou（$\varlimsup$ 版本）：$f_n\leqslant g$、$g\in L(E)$ 时 $\int\varlimsup f_n\geqslant\varlimsup\int f_n$（郭版 §3.2 习题 1）
- [ ] 「$\int_E|f_n|\leqslant M$ 且 $f_n\to f$ a.e. 则 $f\in L(E)$」（郭版 §3.2 习题 2）——与 LDCT 的区别在于结论只要求可积，不要求积分收敛
- [ ] Vitali 收敛定理（用「一致可积」代替「控制函数」）——本节未涉及，属测度论进阶
- [ ] 定理 10 证明中「$h_n\to\omega$ a.e.」的完整论证（需要讨论分法嵌套与连续点处的局部估计）
- [ ] Volterra 例（有界导函数但不可黎曼可积）的构造——Sec3.1 只引用结论，未给构造

## 来源与映射

| 本节点内容 | 来源 | 处理 |
|---|---|---|
| 三大定理的「谁推谁」逻辑链总览（Levi → Fatou → LDCT → 有界收敛 → 依测度版本） | 旧《Ch5 积分论》§四–§五 | 新写（旧包分散陈述，本次收束为单链） |
| Levi 单调收敛定理完整证明（含 $c<1$ 余量技巧）、线性、逐项积分 | 旧《Ch5 积分论》§四 4.3、4.4 | 原文迁移 |
| Fatou 引理证明、$n\chi_{(0,1/n)}$ 反例 | 旧《Ch5 积分论》§四 4.5、§九 Q3 | 原文迁移（Q3 转为正文反例） |
| LDCT 完整证明（Fatou 作用于 $2F-g_n$）、依测度收敛版本 | 旧《Ch5 积分论》§五 5.6 | 原文迁移 |
| 有界收敛推论 + 「$mE<\infty$ 不可少」反例 | 旧《Ch5 积分论》§五 5.6 推论；反例为本次新写 | 迁移 + 新写（反例） |
| LDCT 控制条件不可少的反例（Q4 陷阱） | 旧《Ch5 积分论》§九 Q4 | 原文迁移（转为正文反例） |
| 逐项积分（变号情形）与积分号下求导 | 旧《Ch5 积分论》§五 5.7 | 原文迁移 |
| 黎曼可积 $\iff$ a.e. 连续（Lebesgue 判据）完整论证 | 旧《Ch5 积分论》§六 6.1 | 原文迁移（自 Sec3.1 移入本节，因证明依赖有界收敛） |
| 黎曼函数算例、狄利克雷函数反例 | 旧《Ch5 积分论》§六 6.1；算例为本次新写 | 迁移 + 新写（例题） |
| LDCT 两个算例（$\frac{nx}{1+n^2x^2}$、$\frac{1}{1+x^n}$） | 郭版教材 §3.2（极限定理的应用） | 新写补缺（例题） |
| 抽象测度空间上的 Lebesgue 基本定理、可数可加、Fatou、控制收敛、依测度版本、有界收敛 | 郭版教材 §3.2.3（定理 3.2.11–推论 3.2.16） | 新写补缺 |
| 计数测度上的极限定理算例与 $\delta_{n,k}$ 反例 | 郭版教材 §2.1 例 7 + §3.2.3 | 新写补缺 |
| 「讲给别人听」清单与卡壳对照表 | 旧《Ch5 积分论》§九 9.2、9.3 | 原文迁移（转为正文段落） |
| 「这一节真正要说的是什么」核心洞察 | 旧《Ch5 积分论》§八核心洞察 | 改写迁移 |