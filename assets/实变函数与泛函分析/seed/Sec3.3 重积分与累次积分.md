---
type: 节
formal: true
subject: 实变函数与泛函分析
created: 2026-09-21
updated: 2026-09-21
tags: [math, 实变函数与泛函分析]
chapter: 3
section: 3.3
---

# Sec3.3 重积分与累次积分

> 定位：回答「高维积分能不能拆成先对一个变量积、再对另一个变量积」——用截面定理把高维测度化归为一维，用 Tonelli / Fubini 定理给出可交换次序的两种条件。
> 教材：郭懋正《实变函数与泛函分析》§3.3（p.133–150）
> 来源：旧讲解包《Ch5 积分论》§七；郭版教材 §3.3.2（新写补缺）

> [!info] 关联笔记
> - 父级：[[Ch3 Lebesgue 积分]]
> - 前置：[[Sec3.2 Lebesgue 积分的极限定理]] ｜ 后续：Ch4 §4.3 卷积与 Fourier 变换（见 Ch4）
> - 概念：[[概念-测度与黎曼积分的类比]]

---

## 来龙（为什么需要它）

- **类比已知**：数学分析里算二重积分，标准动作是「化累次积分」：$\iint_{[a,b]\times[c,d]}f\,dA=\int_a^b dx\int_c^d f(x,y)\,dy$。但数学分析没有回答两个问题——**凭什么可以这么化？换成什么次序都行吗？**
- **解决新问题**：本节的路线是「**先几何、再分析**」：把 $f$ 的积分翻译成它下方图形的**测度**（几何对象），再用**截面定理**把这个高维集合沿 $x$ 方向切片（每片是一维的），最后把切片测度积回去——三重奏首尾相接，累次积分公式就自然浮出来了。至于「次序能不能换」，答案分成两半：**非负函数无条件可换（Tonelli）；变号函数必须先证明可积（Fubini）**。
- **理论/应用需要**：Ch4 中卷积与 Fourier 变换的定义就是重积分，Hölder 与 Minkowski 不等式的证明要用 Fubini 交换次序；概率论里「联合分布 → 边缘分布」就是截面定理；数理方程中的 Green 函数、多重积分换序全都靠这一节。

## 主体（核心内容）

### 3.3.1 Fubini 定理

#### 直积与截面（先把新符号定义好）

- **直积** $A\times B=\{(x,y):x\in A,\ y\in B\}$（读作「$A$ 叉乘 $B$」），其中 $A\subset\mathbb{R}^p$、$B\subset\mathbb{R}^q$，它是 $\mathbb{R}^{p+q}$ 中的集合；
- **截面** 对 $E\subset\mathbb{R}^{p+q}$ 与固定 $x_0\in\mathbb{R}^p$，令
  $$E_{x_0}=\{y\in\mathbb{R}^q:(x_0,y)\in E\}$$
  （读作「$E$ 在 $x_0$ 处的**截面**」）——把高维集合沿 $x$ 方向「切片」。对称地可定义 $E^{y_0}=\{x\in\mathbb{R}^p:(x,y_0)\in E\}$。
- 记 $dP=dx\,dy$ 为 $\mathbb{R}^{p+q}$ 上的 Lebesgue 测度对应的体积元。

**直觉**：切片的面积 $mE_x$ 随 $x$ 变化，把所有切片「摞起来」就是原集合的体积——这就是卡瓦列里原理的严格化。

#### 截面定理：高维测度 = 截面测度的积分

**定理 1（截面定理）** 设 $E\subset\mathbb{R}^{p+q}$ 可测，则

1. 对 a.e. 的 $x\in\mathbb{R}^p$，截面 $E_x$ 是 $\mathbb{R}^q$ 中的可测集；
2. $mE_x$ 作为 $x$ 的函数在 $\mathbb{R}^p$ 上 a.e. 有定义且可测；
3. $mE=\displaystyle\int_{\mathbb{R}^p}mE_x\,dx$。

**证明按「特殊到一般」分五步推进**（与卢津定理的三步证明是同一套方法）：

| 步骤 | 集合类型 | 用什么 |
|---|---|---|
| ① | 区间（矩体） | 直接算：$m(I\times J)=mI\cdot mJ$ |
| ② | 开集 | 可数不交矩体之并 + 逐项积分（Sec3.2 定理 3） |
| ③ | $G_\delta$ 集 | 递减交 + 测度的递减连续性 / 控制收敛（Sec3.2 定理 5） |
| ④ | 零测集 | 用 $G_\delta$ 集把它包住，夹逼 |
| ⑤ | 一般可测集 | 测度结构定理 $E=G\setminus M$（$G$ 为 $G_\delta$ 集、$M$ 为零测集） |

**每一步都只调用上一步 + 一个已证定理**——这是测度论里最典型的「爬梯子」证法。

#### 积分的几何意义：积分 = 下方图形的测度

**定义（下方图形）** 设 $f\geqslant0$ 在 $E\subset\mathbb{R}^n$ 上，$\mathbb{R}^{n+1}$ 中的集合
$$G(E,f)=\{(x,z):x\in E,\ 0\leqslant z<f(x)\}$$
称为「$f$ 在 $E$ 上的**下方图形**」。

**定理 2** $f\geqslant0$ 在 $E$ 上可测 $\iff G(E,f)$ 可测；且此时
$$\int_E f(x)\,dx=mG(E,f).$$

**直觉**：积分终于回到了最原始的意义——**曲边梯形的面积就是它下方图形的测度**。勒贝格绕了一大圈（测度 → 可测函数 → 简单函数 → 积分），最后证明这条圆闭合上了：**积分与测度互为表里**。推论：$f$ 可积 $\iff mG(E,f^+)$ 与 $mG(E,f^-)$ 都有限。

> 【原书插图：下方图形 $G(E,f)$ 与积分的关系示意】

#### Tonelli 定理（非负情形）

**定理 3（Tonelli 定理）** 设 $A\subset\mathbb{R}^p$、$B\subset\mathbb{R}^q$ 可测，$f$ 是 $A\times B$ 上的**非负**可测函数，则对 a.e. 的 $x\in A$，$f(x,y)$ 作为 $y$ 的函数在 $B$ 上可测，且
$$\int_{A\times B}f\,dP=\int_A dx\int_B f(x,y)\,dy=\int_B dy\int_A f(x,y)\,dx .$$
**条件只有一条：$f\geqslant0$ 且可测。** 无需验证任何可积性，允许两端同为 $+\infty$。

#### Fubini 定理（可积情形）

**定理 4（Fubini 定理）** 设 $f$ 在 $A\times B$ 上勒贝格可积（$f\in L(A\times B)$），则

1. 对 a.e. 的 $x\in A$，$f(x,y)$ 作为 $y$ 的函数在 $B$ 上可积；
2. 内层积分 $x\mapsto\int_B f(x,y)\,dy$ 作为 $x$ 的函数在 $A$ 上可积；
3. $$\int_{A\times B}f\,dP=\int_A dx\int_B f(x,y)\,dy=\int_B dy\int_A f(x,y)\,dx .$$

**证明路线（三定理首尾相接）**：把 $A\times B$ 上的积分写成下方图形测度 $mG(A\times B,f)$（定理 2）→ 对下方图形用**截面定理**沿 $x$ 切片，截面恰好是 $G(B,f_{(x\,\text{固定})})$（定理 1）→ 该截面的测度再由几何意义等于 $\int_B f(x,y)\,dy$（定理 2 再用一次）——**Fubini 是它们的直接推论**。变号情形则由 $f=f^+-f^-$ 对两个非负部分分别用 Tonelli 再相减（*因为* 可积性保证两个积分都有限，相减合法）。

#### Tonelli 与 Fubini 的区别与各自条件（本节最该记住的对照）

| | **Tonelli 定理** | **Fubini 定理** |
|---|---|---|
| 对 $f$ 的要求 | $f\geqslant0$ 且可测 | $f\in L(A\times B)$（即 $\int|f|<\infty$） |
| 要验证什么 | **什么都不用验证** | 必须先证明**可积性** |
| 结论强度 | 两个累次积分存在且都等于重积分（可为 $+\infty$） | 两个累次积分存在且都等于重积分（有限实数） |
| 能不能换序 | 能，无条件 | 能，但前提是可积 |
| 典型用法 | 算非负积分、证明不等式（先换序再算） | 算含变号的积分、证等式 |

**记忆钩子**：**Tonelli 管「非负」，Fubini 管「可积」；先 Tonelli 验可积，再用 Fubini 换序。** 实际做题的固定套路是：遇到变号函数，先用 Tonelli 对 $|f|$ 算一遍——如果 $\int|f|<\infty$，就拿到了 Fubini 的通行证。

> **问**：为什么变号时必须先验证可积性？难道不是「能算出来就行」吗？
> **答**：不行，下面这个反例会告诉你为什么。

**反例（Fubini 的可积性条件不可少——两个累次积分竟然不等）** 在 $[0,1]\times[0,1]$ 上取
$$f(x,y)=\frac{x^2-y^2}{(x^2+y^2)^2}\quad\bigl((x,y)\neq(0,0)\bigr),\qquad f(0,0)=0 .$$

- **先算一种次序**：*因为* $\dfrac{\partial}{\partial y}\left(\dfrac{y}{x^2+y^2}\right)=\dfrac{x^2-y^2}{(x^2+y^2)^2}$，故
  $$\int_0^1 f(x,y)\,dy=\left[\frac{y}{x^2+y^2}\right]_{y=0}^{y=1}=\frac{1}{1+x^2},$$
  于是
  $$\int_0^1 dx\int_0^1 f(x,y)\,dy=\int_0^1\frac{dx}{1+x^2}=\frac{\pi}{4}.$$
- **再算另一种次序**：*因为* $f(y,x)=-f(x,y)$（分子分母对 $x,y$ 交换后分子变号），同样的计算给出 $\int_0^1 f(x,y)\,dx=\dfrac{-1}{1+y^2}$，于是
  $$\int_0^1 dy\int_0^1 f(x,y)\,dx=-\frac{\pi}{4}.$$
- **结果**：两个累次积分都存在，却互为相反数，**$\frac{\pi}{4}\neq-\frac{\pi}{4}$**。
- **原因**：*因为* 两个累次积分不相等，由 Fubini 定理（逆否）知 $f$ **不**在 $[0,1]^2$ 上勒贝格可积——事实上 $|f|$ 在原点附近的积分发散。**可积性一旦缺失，「换序」这件事就彻底失去保障。** 这也是 Tonelli 定理只能对非负函数生效的原因：非负函数的两个累次积分不会「互相抵消」，所以不会出现这种矛盾。

**例题 1（Tonelli 的最小实例）** 计算 $\displaystyle\int_{[0,1]^2}x\,dP$。

- **原始信息**：$f(x,y)=x$ 在 $[0,1]^2$ 上非负可测。
- **代入 Tonelli**：$\displaystyle\int_{[0,1]^2}x\,dP=\int_0^1 dx\int_0^1 x\,dy=\int_0^1 x\,dx=\frac12$。
- **换序验证**：另一顺序 $\displaystyle\int_0^1 dy\int_0^1 x\,dx=\int_0^1\frac12\,dy=\frac12$，结果相同。
- **结论**：两个顺序都合法（非负可测，Tonelli 无条件），结果一致——**这是「横竖切法随便挑」的严格保证**。

**例题 2（Tonelli 的实战用法：交换次序算一个算不动的积分）** 设 $0<a<b$，求
$$I=\int_0^\infty\frac{e^{-ax^2}-e^{-bx^2}}{x}\,dx .$$

- **原始信息**：直接对 $x$ 积分算不出来（原函数不是初等函数）。*因为* $0<a<b$ 时 $e^{-ax^2}>e^{-bx^2}$，故被积函数在 $(0,\infty)$ 上**非负**——可以放心用 Tonelli。
- **把一元积分写成二重积分**：*因为* $\displaystyle\int_a^b x e^{-tx^2}\,dt=x\cdot\frac{e^{-ax^2}-e^{-bx^2}}{x^2}=\frac{e^{-ax^2}-e^{-bx^2}}{x}$，故
  $$I=\int_0^\infty\!\!\int_a^b x e^{-tx^2}\,dt\,dx .$$
- **交换次序（Tonelli）**：被积函数 $xe^{-tx^2}\geqslant0$ 在 $(0,\infty)\times(a,b)$ 上可测，无条件换序：
  $$I=\int_a^b\!\!\int_0^\infty x e^{-tx^2}\,dx\,dt=\int_a^b\left[-\frac{1}{2t}e^{-tx^2}\right]_{x=0}^{x=\infty}dt=\int_a^b\frac{dt}{2t}=\frac12\ln\frac ba .$$
- **结果与结论**：$I=\dfrac12(\ln b-\ln a)$。**这就是「升维再换序」的威力**：一个算不动的一元积分，把它看成二重积分、换序后变成初等积分。**Tonelli 定理在这里的作用不是「算积分」，而是「允许你把积分当积木重新拼装」。**

### 3.3.2 测度空间上的重积分与累次积分

> 本小节是**新写补缺**（郭版 §3.3.2）：旧讲解包只讲 $\mathbb{R}^{p+q}$ 上的 Fubini，抽象乘积测度空间的构造是郭版新增内容。它把「截面 + 乘积测度 + Tonelli/Fubini」整条链搬到一般测度空间，为概率论（联合分布）提供统一语言。

#### 乘积空间与截口

设 $(X,\mathcal{F},\mu)$、$(Y,\mathcal{G},\nu)$ 是两个给定的测度空间。令 $Z=X\times Y$，称形如 $A\times B$（$A\in\mathcal{F}$、$B\in\mathcal{G}$）的集合为 $Z$ 中的**可测矩体**，全体记作 $\mathcal{R}$；由 $\mathcal{R}$ 生成的 $\sigma$ 代数记作 $\mathcal{H}$。于是 $(Z,\mathcal{H})$ 是可测空间，称为 $(X,\mathcal{F})$ 与 $(Y,\mathcal{G})$ 的**乘积空间**，记作 $(Z,\mathcal{H})=(X,\mathcal{F})\times(Y,\mathcal{G})$。

对 $E\in\mathcal{H}$ 与 $x\in X$、$y\in Y$，定义
$$E_x=\{y\in Y\mid(x,y)\in E\},\qquad E^y=\{x\in X\mid(x,y)\in E\},$$
称为集合 $E$ 的**截口**（与 §3.3.1 的「截面」是同一件事，只是换了记号）。

#### 乘积测度的存在唯一性

**定理 5（郭版定理 3.3.9）** 设 $(X,\mathcal{F})$ 与 $(Y,\mathcal{G})$ 是两个 **$\sigma$ 有限**测度空间，$(Z,\mathcal{H})$ 是 $X$ 与 $Y$ 的乘积空间，则存在**唯一**定义在 $\mathcal{H}$ 上的 $\sigma$ 有限测度 $\lambda$，满足

1. $\lambda(A\times B)=\mu(A)\cdot\nu(B)$ 对一切可测矩体 $A\times B\in\mathcal{R}$ 成立；
2. 对任给 $E\in\mathcal{H}$，
   $$\lambda(E)=\int_X\nu(E_x)\,\mu(\mathrm{d}x)=\int_Y\mu(E^y)\,\nu(\mathrm{d}y).$$

$\lambda$ 称为 $\mu$ 与 $\nu$ 的**乘积测度**，记作 $\lambda=\mu\times\nu$；$(Z,\mathcal{H},\lambda)$ 称为乘积测度空间。

**证明骨架（郭版分 4 步）**：

1. **截口可测**：令 $\mathcal{E}=\{E\subset Z\mid E$ 的截口都可测$\}$。*因为* 可测矩体的截口只可能是 $A$、$B$ 或 $\varnothing$，故 $\mathcal{R}\subset\mathcal{E}$；又 *因为* $\mathcal{E}$ 对可数并与补运算封闭（$(\bigcup_n E_n)_x=\bigcup_n(E_n)_x$、$(E^{\mathrm{c}})_x=(E_x)^{\mathrm{c}}$），$\mathcal{E}$ 是 $\sigma$ 代数，故 $\mathcal{H}\subset\mathcal{E}$。
2. **单调族**：称满足「单调列的极限仍在其中」的集合族为**单调族**。*因为* $\sigma$ 代数是单调族，且「既是单调族又是代数」的集合族必是 $\sigma$ 代数，于是可用**单调类定理**把「代数上成立」升级为「$\sigma$ 代数上成立」。
3. **验证 (3.3.21) 式**：先设 $\mu(X)<\infty$、$\nu(Y)<\infty$。令 $\mathcal{L}=\{E\in\mathcal{E}\mid(3.3.21)$ 成立$\}$。*因为* 矩体上两边都等于 $\mu(A)\nu(B)$，故 $\mathcal{R}\subset\mathcal{L}$；由 $\mathcal{R}$ 生成的代数 $\mathcal{B}$ 中每个集合是有限个互不相交矩体之并，而 $\mathcal{L}$ 对有限不交并封闭，故 $\mathcal{B}\subset\mathcal{L}$；再 *因为* 对升列 $\{E_n\}\subset\mathcal{L}$ 用 **Levi 定理**（Sec3.2 定理 1）可把极限搬进积分号，对降列同理，故 $\mathcal{L}$ 是单调类，从而 $\mathcal{H}\subset\mathcal{L}$。
4. **去掉有限性假设**：用 $\sigma$ 有限性把 $X$、$Y$ 分解成可数多个有限测度块，逐块验证再求和。$\square$

**为什么必须 $\sigma$ 有限**：见下面的反例——去掉这个条件，乘积测度**不唯一**，「先对 $x$ 积」与「先对 $y$ 积」会给出不同答案。

#### 抽象 Tonelli 定理与 Fubini 定理

与欧氏空间上的理论**相仿**（郭版原话：「与欧氏空间上 Lebesgue 重积分与累次积分可交换理论相仿」），有：

**定理 6（Tonelli 定理，郭版定理 3.3.10）** 设 $(X,\mathcal{F},\mu)$、$(Y,\mathcal{G},\nu)$ 是 $\sigma$ 有限测度空间，$(Z,\mathcal{H},\lambda)$ 是乘积测度空间。若 $f$ 是 $Z$ 上的**非负 $\mathcal{H}$ 可测函数**，则
$$\int_Z f\,\mathrm{d}\lambda=\int_X\left(\int_Y f(x,y)\,\nu(\mathrm{d}y)\right)\mu(\mathrm{d}x)=\int_Y\left(\int_X f(x,y)\,\mu(\mathrm{d}x)\right)\nu(\mathrm{d}y).$$
**条件：$f\geqslant0$ 且 $\mathcal{H}$ 可测，此外无需验证任何可积性。**

**定理 7（Fubini 定理，郭版定理 3.3.11）** 设 $f\in L(Z,\mathcal{H},\lambda)$，则
$$\int_Z f\,\mathrm{d}\lambda=\int_X\left(\int_Y f(x,y)\,\nu(\mathrm{d}y)\right)\mu(\mathrm{d}x)=\int_Y\left(\int_X f(x,y)\,\mu(\mathrm{d}x)\right)\nu(\mathrm{d}y).$$
**条件：$f$ 关于乘积测度 $\lambda$ 可积（$\int_Z|f|\,\mathrm{d}\lambda<\infty$）。**

> **与 §3.3.1 的对照**：把 $\mathbb{R}^p$ 换成 $X$、$\mathbb{R}^q$ 换成 $Y$、$m$ 换成 $\mu$、$n$ 换成 $\nu$，定理 1 变成定理 5 的第 2 条，定理 3 与定理 4 变成定理 6 与定理 7。**「Tonelli 管非负、Fubini 管可积」这条分工，在任何测度空间上都原样成立。**

**例题（非负二重级数可交换求和次序）** 在 $(\mathbb{N},2^{\mathbb{N}},\mu)$（$\mu$ 为计数测度）上，设 $a_{mn}\geqslant0$（$m,n\geqslant1$）。证明
$$\sum_{m=1}^{\infty}\sum_{n=1}^{\infty}a_{mn}=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}a_{mn}.$$

- **原始信息**：取 $X=Y=\mathbb{N}$、$\mathcal{F}=\mathcal{G}=2^{\mathbb{N}}$、$\mu=\nu=$ 计数测度，它们都是 $\sigma$ 有限的（$X=\bigcup_m\{m\}$ 且 $\mu(\{m\})=1<\infty$）。
- **识别乘积测度**：*因为* 单点集上 $\lambda(\{m\}\times\{n\})=\mu(\{m\})\nu(\{n\})=1$，且 $\mathbb{N}\times\mathbb{N}$ 可数，故 $\lambda$ 就是 $\mathbb{N}\times\mathbb{N}$ 上的计数测度。
- **代入定理 6（Tonelli）**：令 $f(m,n)=a_{mn}\geqslant0$，则
  $$\int_Z f\,\mathrm{d}\lambda=\int_{\mathbb{N}}\left(\int_{\mathbb{N}}a_{mn}\,\nu(\mathrm{d}n)\right)\mu(\mathrm{d}m)=\sum_{m=1}^{\infty}\sum_{n=1}^{\infty}a_{mn},$$
  另一种次序同理得 $\sum_n\sum_m a_{mn}$，两者相等。
- **结论**：**「非负二重级数可以任意交换求和次序」这条分析里的老结论，就是 Tonelli 定理在计数测度下的化身**。注意条件「$a_{mn}\geqslant0$」与 Tonelli 的「$f\geqslant0$」精确对应——去掉非负性（例如 $a_{mn}$ 变号）结论立刻可能失效，正如 §3.3.1 的反例。

**反例（定理 5 中「$\sigma$ 有限」不可少：乘积测度不唯一，两个次序给出不同答案）** 取 $X=Y=[0,1]$、$\mathcal{F}=\mathcal{G}=$ Borel $\sigma$ 代数，$\mu=$ Lebesgue 测度（$\sigma$ 有限），$\nu=$ **计数测度**（*因为* 不可数集上 $\nu$ 取 $+\infty$，而 $[0,1]$ 不能写成可数多个有限 $\nu$ 测度集之并，故 $\nu$ **不是** $\sigma$ 有限的）。取 $E=\{(x,x):x\in[0,1]\}$ 为对角线。

- **先对 $y$ 积**：*因为* 固定 $x$ 时 $E_x=\{x\}$，$\nu(E_x)=1$，故 $\displaystyle\int_X\nu(E_x)\,\mu(\mathrm{d}x)=\int_{[0,1]}1\,d\mu=1$。
- **先对 $x$ 积**：*因为* 固定 $y$ 时 $E^y=\{y\}$，$\mu(E^y)=m\{y\}=0$，故 $\displaystyle\int_Y\mu(E^y)\,\nu(\mathrm{d}y)=\int_{[0,1]}0\,d\nu=0$。
- **结果**：$1\neq0$——**同一个集合 $E$ 的两个累次积分不相等**。
- **结论**：*因为* $\nu$ 不 $\sigma$ 有限，定理 5 的前提被破坏，乘积测度既不唯一，(3.3.20) 式也不再成立。**$\sigma$ 有限不是技术性装饰，而是定理成立的必要条件。**（对照 §3.3.1：Lebesgue 测度是 $\sigma$ 有限的，所以那个反例的病根在「$f$ 不可积」，而不在测度。）

> **这一节真正要说的是什么**：累次积分公式不是「积分技巧」，而是**测度的可数可加性在高维的必然表现**——高维测度 = 截面测度的积分（截面定理），积分 = 下方图形的测度（几何意义），两件事一叠加，Fubini 定理就是推论。而「什么时候能换序」的答案只有一句话：**非负时无条件（Tonelli），变号时必须先可积（Fubini）**。把 Lebesgue 测度换成任意 $\sigma$ 有限测度，整条链原样成立——概率论里「联合分布对边缘分布」用的正是同一套东西。

> **检验回路（续 Sec3.2 的「讲给别人听」清单）**
> 10. **几何意义与 Fubini 定理的证明路线**：下方图形 → 截面定理 → 累次积分，三个定理如何首尾相接；
> 11. **Tonelli 与 Fubini 的区别**：各自条件、为什么变号时必须先验证可积、$(x^2-y^2)/(x^2+y^2)^2$ 反例的两个累次积分；
> 12. **抽象乘积测度空间**：可测矩体 → 乘积空间 → 截口 → 乘积测度 $\lambda=\mu\times\nu$ → 定理 5 为什么必须 $\sigma$ 有限。

## 去脉（学完去哪）

- **直接服务于 Ch4 §4.3**：卷积 $(f*g)(x)=\int_{\mathbb{R}^n}f(x-t)g(t)\,dt$ 的定义就是重积分，其结合律与 $L^1$ 范数不等式 $\|f*g\|_1\leqslant\|f\|_1\|g\|_1$ 的证明要用 Tonelli 换序；Fourier 变换的许多性质同样依赖本节的工具。
- **$L^p$ 空间**（见 Ch4）：Hölder 不等式与 Minkowski 不等式的证明都要把 $\int|f|^p$ 写成重积分再换序。
- **概率论**：$(\Omega,\mathcal{F},P)$ 上两个随机变量的**联合分布**就是乘积空间上的乘积测度；**边缘分布 = 对另一个变量积分（截面定理）**；「$E[X+Y]=E[X]+E[Y]$」与「独立时 $E[XY]=E[X]E[Y]$」都靠 Fubini。**本节是概率论的计算引擎。**
- **数理方程**：Green 函数、多重积分换序、能量估计中反复出现的 $\int\!\!\int$ 交换，都建立在这里。
- **一句话**：本节把「积分」从一维推到高维，并给出唯一的操作许可——**先证非负（Tonelli），再证可积（Fubini），然后放心换序**。

## 防跳跃

- [ ] 单调类定理的完整陈述与证明（定理 5 的证明第 2 步只给了骨架）
- [ ] 定理 5 证明第 3 步中「$\mathcal{D}$ 是代数 ⟹ 是 $\sigma$ 代数」的细节
- [ ] 定理 5 中「$\sigma$ 有限 ⟹ 可分解为可数有限测度块」的具体分解方法（证明第 4 步只给了一句）
- [ ] 定理 1（截面定理）第 ③ 步「$G_\delta$ 集」用到的测度递减连续性条件（需要某一项测度有限）
- [ ] 反例中 $|f|$ 在原点附近积分发散的具体估计（本节只给了结论与逆否推理）
- [ ] 抽象 Tonelli / Fubini（定理 6、7）的证明——郭版与欧氏情形「证明雷同」，本节按郭版只叙述结果
- [ ] 卷积的完整定义与性质——属 Ch4 §4.3，本节只作指向
- [ ] 概率论中「独立 ⟹ 乘积测度」的严格表述——需先有概率空间的定义，本节只作类比

## 来源与映射

| 本节点内容 | 来源 | 处理 |
|---|---|---|
| 直积与截面的定义、截面定理（高维测度 = 截面测度积分）与五步证明 | 旧《Ch5 积分论》§七 7.1、7.2 | 原文迁移 |
| 下方图形定义、积分 = 下方图形测度（几何意义） | 旧《Ch5 积分论》§七 7.3 | 原文迁移 |
| Tonelli（非负版本）与 Fubini（可积版本）的陈述、证明路线（三定理首尾相接） | 旧《Ch5 积分论》§七 7.4 | 原文迁移 |
| Tonelli 与 Fubini 的对照表、「先 Tonelli 验可积再用 Fubini」套路 | 旧《Ch5 积分论》§七 7.4 | 改写（旧包以「非负版本 / 可积版本」并列，本次显式对照） |
| $(x^2-y^2)/(x^2+y^2)^2$ 两个累次积分不等的反例 | 郭版教材 §3.3 习题（两累次积分不等 ⟹ 不可积） | 新写补缺（本次补全计算） |
| 例题 1：$\int_{[0,1]^2}x\,dP=\frac12$ | 旧《Ch5 积分论》§七 7.4 最小实例 | 原文迁移 |
| 例题 2：$\int_0^\infty\frac{e^{-ax^2}-e^{-bx^2}}{x}dx=\frac12\ln\frac ba$ | 郭版教材 §3.3 习题（提示「用 Tonelli 定理」） | 新写补缺（本次补全计算） |
| 可测矩体、乘积空间、截口 $E_x$/$E^y$、乘积测度 $\lambda=\mu\times\nu$ | 郭版教材 §3.3.2（定理 3.3.9） | 新写补缺 |
| 定理 5 的四步证明骨架 | 郭版教材 §3.3.2 | 新写补缺 |
| 抽象 Tonelli 定理（定理 3.3.10）、抽象 Fubini 定理（定理 3.3.11） | 郭版教材 §3.3.2 | 新写补缺 |
| 计数测度上非负二重级数可换序的例题 | 郭版教材 §2.1 例 7 + §3.3.2 | 新写补缺 |
| 「$\sigma$ 有限不可少」的对角线反例 | 郭版教材 §3.3.2 定理 3.3.9 条件 | 新写补缺（条件必要性说明） |
| 「检验回路」第 10–12 项 | 旧《Ch5 积分论》§九 9.2 | 原文迁移（转为正文段落） |
| 「这一节真正要说的是什么」核心洞察 | 旧《Ch5 积分论》§七、§八 | 改写迁移 |