---
type: 节
formal: true
subject: 实变函数与泛函分析
created: 2026-09-21
updated: 2026-09-21
tags: [math, 实变函数与泛函分析]
chapter: 1
section: 1.1
---

# Sec1.1 集合及其运算

> 定位：本节给全书配一台"翻译机"——把"任意 / 存在 / 趋于极限"逐字翻译成集合的并、交、补，并把"一列集合逼近某个极限集合"写成上极限与下极限。
> 教材：郭懋正《实变函数与泛函分析》§1.1（p.1–13）
> 来源：旧讲解包《Ch1 集合》§二–§三（集合的表示与包含、集合的运算）；郭版教材 §1.1.1–§1.1.2

> [!info] 关联笔记
> - 父级：[[Ch1 集合与运算]]
> - 后续：[[Sec1.2 映射]]
> - 概念：本节是纯工具性内容，本组的概念节点挂在 [[Sec1.3 n 维欧氏空间]]

---

## 来龙（为什么需要它）

- **类比已知**：高等数学里说"数列 $x_n$ 收敛到 $a$"，用的是 $\varepsilon$-$N$ 语言——"对任意 $\varepsilon>0$（$\varepsilon$ 读作"艾普西龙"，代表任意小的正数），存在自然数 $N$，使 $n\geqslant N$ 时 $|x_n-a|<\varepsilon$"。这句话只用到两个词：**任意**与**存在**。本节要做的事，就是给这两个词各配一个集合运算，从此"极限"可以被写成算式。
- **解决新问题**：实变函数要研究的对象不是数列而是**点集**。它一开始就要问："使 $f_n(x)\to f(x)$ 的那些 $x$ 全体，是一个什么样的集合？""使 $f(x)>0$ 的那些 $x$ 全体，能不能写成可数个简单集合的并？"这些问题不引入集合运算就无法开口，更谈不上给它们量"大小"。
- **理论/应用需要**：后面每一章的第一个动作几乎都是"把某个性质写成集合式"：Ch2 用**可数个开矩体覆盖**定义外测度；Ch3 的 Levi 单调收敛定理、Fatou 引理、控制收敛定理，第一步都是把 $\{x:\ f_n(x)\to f(x)\}$ 写成可数交并。**本节是这套语法的语法书**——它本身不产生定理，但全书每一个定义都建在它上面。

## 主体（核心内容）

### 1.1.1 集合及其运算

**定义（集合与元素，朴素说法）**：集合是数学中的原始概念，不能用更基本的概念定义。本书采用的说法是：**具有一定性质的对象的全体**称为集合，其中每个对象称为该集合的**元素**。若 $x$ 是集合 $A$ 的元素，称 $x$ **属于** $A$，记为 $x\in A$（读作"$x$ 属于 $A$"）；否则记为 $x\notin A$（读作"$x$ 不属于 $A$"）。不含任何元素的集合称为**空集**，记作 $\varnothing$（读作"空集"）；只含一个元素 $a$ 的集合记作 $\{a\}$，称为**单元素集**。

一个集合的元素必须彼此互异，且"哪些对象属于它"必须明确。所以"全体高个子"不构成集合（"高"没有明确界限），而 $\{x:\ \sin x>1\}$ 构成集合（它是空集，因为正弦值不可能大于 $1$）。

**记号约定**（首次出现即定义，全书通用）：$\mathbb{N}$ 自然数集、$\mathbb{Z}$ 整数集、$\mathbb{Q}$ 有理数集、$\mathbb{R}$ 实数集、$\mathbb{C}$ 复数集。

**集合的两种表示法**：
- **列举法**：把元素一一写进花括号，如 10 以内的偶数构成的集合是 $\{2,4,6,8,10\}$；
- **描述法**：用元素满足的条件来描述，如 $A=\{a\mid a\text{ 具有性质 }\wp\}$（读作"满足性质 $\wp$ 的 $a$ 的全体"），其中 $\wp$ 可以是一段文字，也可以是一个数学式子。例如
$$
\mathbb{N}=\{k\in\mathbb{Z}\mid k>0\},\qquad
(x_0-\delta,\ x_0+\delta)=\{x\in\mathbb{R}\mid |x-x_0|<\delta\}.
$$

**定义（子集、真子集、相等）**：若 $A$ 中的元素都是 $B$ 中的元素，则称 $A$ 是 $B$ 的**子集合**，记作 $A\subset B$ 或 $B\supset A$（分别读作"$A$ 包含于 $B$ 中""$B$ 包含 $A$"）。空集 $\varnothing$ 是任何集合的子集，任何集合都是其自身的子集。若 $A\subset B$ 且存在 $b\in B$ 使 $b\notin A$，则称 $A$ 是 $B$ 的**真子集**，记作 $A\subsetneqq B$。若同时有 $A\supset B$ 与 $B\supset A$，则称 $A$ 与 $B$ **相等**，记作 $A=B$。

> **这个定义为什么重要**：$A=B$ 当且仅当互相包含——这是证明两个集合相等的**唯一标准方法**（"两边互相包含"）。在实变函数里，"函数具有某性质"常常被翻译成"某个集合包含于另一个集合"，例如 $f$ 在 $[a,b]$ 上有上界 $M$ $\iff$ $[a,b]\subset\{x:\ f(x)\leqslant M\}$。翻译成包含关系之后，才能对它做测度、做运算。

**定义（全集与补集）**：讨论问题时涉及的集合总是某个最大集合 $X$ 的子集，称 $X$ 为**全集**。当 $A\subset X$ 时，由 $X$ 中不属于 $A$ 的元素全体组成的集合称为 $A$ 的**补集**（或余集），记为 $A^{\mathrm{c}}$（读作"$A$ 的补集"）。显然 $X^{\mathrm{c}}=\varnothing$、$\varnothing^{\mathrm{c}}=X$。当全集已知时不必明显标出，简记为 $A^{\mathrm{c}}=\{x\in X\mid x\notin A\}$。例如在 $\mathbb{R}$ 中，
$$
[a,\infty)^{\mathrm{c}}=\{x\in\mathbb{R}\mid x<a\}=(-\infty,a).
$$

**定义 1.1.1（并、交、差）**：设 $A,B$ 是两个集合。称集合 $\{x\mid x\in A\text{ 或 }x\in B\}$ 为 $A$ 与 $B$ 的**并集**，记为 $A\cup B$（读作"$A$ 并 $B$"）；称集合 $\{x\mid x\in A\text{ 且 }x\in B\}$ 为 $A$ 与 $B$ 的**交集**，记为 $A\cap B$（读作"$A$ 交 $B$"）；若 $A\cap B=\varnothing$，称 $A$ 与 $B$ **互不相交**；称集合 $\{x\mid x\in A,\ x\notin B\}$ 为 $A$ 与 $B$ 的**差**，记为 $A\setminus B$（读作"$A$ 减 $B$"）。

例如
$$
[n,n+1)\cup[n+1,n+2)=[n,n+2),\quad
[n,n+2)\cap[n+1,n+3)=[n+1,n+2),\quad
[n,n+2)\setminus[n+1,n+3)=[n,n+1).
$$

> 【原书插图：图 1.1 用阴影标出 $A\cup B$、$A\cap B$、$A\setminus B$ 三个新集合】

**定理 1.1.2（运算律）**：设有集合 $A,B$ 与 $C$，则有

(1) **交换律**：$A\cup B=B\cup A$，$A\cap B=B\cap A$；
(2) **结合律**：$A\cup(B\cup C)=(A\cup B)\cup C$，$A\cap(B\cap C)=(A\cap B)\cap C$；
(3) **分配律**：$A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$，$A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$；
(4) **对偶律（德摩根 De Morgan 法则）**：$(A\cup B)^{\mathrm{c}}=A^{\mathrm{c}}\cap B^{\mathrm{c}}$，$(A\cap B)^{\mathrm{c}}=A^{\mathrm{c}}\cup B^{\mathrm{c}}$；
(5) $A\setminus B=A\cap B^{\mathrm{c}}$；
(6) 若 $A\supset B$，则 $A^{\mathrm{c}}\subset B^{\mathrm{c}}$。

*证明（以 (4) 的第一式为例，其余类似）*：若 $x\in(A\cup B)^{\mathrm{c}}$，则 $x\notin A\cup B$，于是 $x\notin A$ 且 $x\notin B$，即 $x\in A^{\mathrm{c}}$ 且 $x\in B^{\mathrm{c}}$，所以 $x\in A^{\mathrm{c}}\cap B^{\mathrm{c}}$，得 $(A\cup B)^{\mathrm{c}}\subset A^{\mathrm{c}}\cap B^{\mathrm{c}}$。反之，若 $x\in A^{\mathrm{c}}\cap B^{\mathrm{c}}$，则 $x\notin A$ 且 $x\notin B$，显然 $x\notin A\cup B$，即 $x\in(A\cup B)^{\mathrm{c}}$，得 $A^{\mathrm{c}}\cap B^{\mathrm{c}}\subset(A\cup B)^{\mathrm{c}}$。两边互相包含，故
$$
(A\cup B)^{\mathrm{c}}=A^{\mathrm{c}}\cap B^{\mathrm{c}}. \qquad\square
$$

**推广到任意多（无限并交）**：设有集合族 $\{A_\lambda\}_{\lambda\in I}$，其中 $I$ 称为**指标集**，$\lambda$ 是跑遍 $I$ 的**指标**（一个"编号"）。规定
$$
\bigcup_{\lambda\in I}A_\lambda=\{x\mid \exists\lambda\in I,\ x\in A_\lambda\},\tag{1.1.1}
$$
$$
\bigcap_{\lambda\in I}A_\lambda=\{x\mid \forall\lambda\in I,\ x\in A_\lambda\}.\tag{1.1.2}
$$

**★ 量词 ↔ 并交的翻译规则**（本节的核心，必须背下来）：
> **"存在"对应并，$\bigcup$；"任意"对应交，$\bigcap$。**

交换律与结合律仍适用于多个集合的并交；分配律与对偶律写成
$$
A\cap\Big(\bigcup_{\lambda\in I}B_\lambda\Big)=\bigcup_{\lambda\in I}(A\cap B_\lambda),\qquad
A\cup\Big(\bigcap_{\lambda\in I}B_\lambda\Big)=\bigcap_{\lambda\in I}(A\cup B_\lambda);
$$
$$
\Big(\bigcap_{\lambda\in I}A_\lambda\Big)^{\mathrm{c}}=\bigcup_{\lambda\in I}A_\lambda^{\mathrm{c}},\qquad
\Big(\bigcup_{\lambda\in I}A_\lambda\Big)^{\mathrm{c}}=\bigcap_{\lambda\in I}A_\lambda^{\mathrm{c}}.\tag{德摩根}
$$

**德摩根的读法**："并的补 = 补的交，交的补 = 补的并"。它精确地体现了逻辑否定规则：$\neg(\exists)$ 是 $\forall\neg$，$\neg(\forall)$ 是 $\exists\neg$（$\neg$ 读作"非"）。数学分析中"任意 $\varepsilon$ 存在 $N$"的否定句，就是靠它**机械化地**写出来的。

**定义（幂集）**：任给集合 $X$，它的子集之全体构成的集合称为 $X$ 的**幂集**，记作 $2^{X}$（读作"$X$ 的幂集"）。若 $A$ 是含 $n$ 个元素的有限集，则 $A$ 恰有 $2^{n}$ 个子集——这正是记号 $2^{X}$ 的来源。幂集 $2^{X}$ 关于并、交、补、差运算都是封闭的，这四种运算应看成 $2^{X}$ 中的代数结构。

**定义 1.1.4（直积）**：设有集合 $X_1,X_2,\cdots,X_n$。由所有**有序元素** $x=(x_1,x_2,\cdots,x_n)$（其中 $x_i\in X_i$）构成的集合，称为 $X_1,X_2,\cdots,X_n$ 的**直积**（也叫笛卡尔乘积），记作 $\prod_{i=1}^{n}X_i$ 或 $X_1\times X_2\times\cdots\times X_n$。若 $X_i=X$ 对一切 $i$ 成立，则把 $\prod_{i=1}^{n}X$ 记成 $X^{n}$，称为 $X$ 的 **$n$ 次幂**。

直积被广泛使用：$n$ 维欧氏空间 $\mathbb{R}^{n}=\{(x_1,\cdots,x_n)\mid x_i\in\mathbb{R}\}$ 就是 $\mathbb{R}$ 的 $n$ 次幂；$\mathbb{Z}^{n}$ 是 $\mathbb{R}^{n}$ 中整数格点的全体。通常把 $A\times B$ 形象地看成以 $A,B$ 为边的矩形。

**定义（集合族、集合列、单调列）**：设 $I$ 是一非空集，若对每个 $\lambda\in I$ 指定了一个集合 $A_\lambda$，则称 $\{A_\lambda\mid\lambda\in I\}$ 为一个**集合族**。称集合族 $\{A_n\mid n\in\mathbb{N}\}$ 为**集合列**，简记作 $\{A_n\}$。若 $A_1\subset A_2\subset\cdots\subset A_n\subset\cdots$（或反向包含），则称集合列 $\{A_n\}$ 是**升列**（或**降列**）；升列与降列合称**单调列**。

**★ 核心例题（把极限过程翻译成集合运算）**：

设 $f(x),f_n(x)$（$n\in\mathbb{N}$）是 $\mathbb{R}$ 上的实值函数，令
$$
A=\{x\in\mathbb{R}\mid \lim_{n\to\infty}f_n(x)=f(x)\},\qquad
A_{mn}=\Big\{x\in\mathbb{R}\ \Big|\ |f_n(x)-f(x)|<\frac{1}{m}\Big\}.
$$
**原始信息**：$f_n(x)\to f(x)$ 的含义是"对任意 $m\in\mathbb{N}$，存在 $n\in\mathbb{N}$，对一切 $k\geqslant n$ 有 $|f_k(x)-f(x)|<1/m$"。
**代入翻译规则**（$\forall$ 换成 $\bigcap$，$\exists$ 换成 $\bigcup$）：
$$
f_n(x)\to f(x)\iff \forall m\in\mathbb{N},\ \exists n\in\mathbb{N},\ \forall k\geqslant n:\ x\in A_{mk}
\iff x\in\bigcap_{m=1}^{\infty}\bigcup_{n=1}^{\infty}\bigcap_{k=n}^{\infty}A_{mk}.
$$
**结果**：
$$
A=\bigcap_{m=1}^{\infty}\bigcup_{n=1}^{\infty}\bigcap_{k=n}^{\infty}A_{mk}.\tag{1.1.3}
$$
**结论**：一个"逐点收敛"的定性描述，被完整地翻译成**可数**交并式。注意这里把"任意 $\varepsilon>0$"换成了"任意 $1/m$"——因为对任意 $\varepsilon>0$ 都可取 $m$ 使 $1/m<\varepsilon$，两种说法等价。**这个"可数化"替换把不可数个交变成可数个交，是全书最常用的技术动作之一**（Ch2、Ch3 会反复使用）。

**例（用对偶律写"函数值 $\leqslant 0$"的点集）**：若 $f$ 是 $\mathbb{R}$ 上的实值函数，$A=\{x\mid f(x)>0\}$，$A_n=\{x\mid f(x)>1/n\}$。因为 $f(x)>0\iff\exists n\in\mathbb{N}:f(x)>1/n$，故
$$
A=\bigcup_{n=1}^{\infty}A_n .
$$
再由德摩根公式，
$$
\{x\in\mathbb{R}\mid f(x)\leqslant 0\}=A^{\mathrm{c}}=\Big(\bigcup_{n=1}^{\infty}A_n\Big)^{\mathrm{c}}=\bigcap_{n=1}^{\infty}A_n^{\mathrm{c}}=\bigcap_{n=1}^{\infty}\Big\{x\in\mathbb{R}\ \Big|\ f(x)\leqslant\frac{1}{n}\Big\}.
$$
这一步示范了标准动作：**先写"好写的那个方向"（开集式的 $>$），再用对偶律取补得到"难写的那个方向"（闭集式的 $\leqslant$）**。

**反例 1（差运算不满足"看起来该有"的结合律）**：一般地
$$
A\setminus(B\setminus C)\neq(A\setminus B)\setminus C .
$$
*取 $A=B=C=\{1\}$*：左边 $B\setminus C=\varnothing$，故左边 $=\{1\}$；右边 $A\setminus B=\varnothing$，故右边 $=\varnothing$。两者不等。
**教训**：差运算是"不听话"的运算，凡是遇到差，先用 (5) 式把它改写成 $A\cap B^{\mathrm{c}}$，再进入并交的代数运算。

**反例 2（量词的顺序不可交换——$\bigcap\bigcup$ 与 $\bigcup\bigcap$ 不同）**：一般地
$$
\bigcap_{m=1}^{\infty}\bigcup_{n=1}^{\infty}A_{mn}\ \neq\ \bigcup_{n=1}^{\infty}\bigcap_{m=1}^{\infty}A_{mn}.
$$
*取 $A_{mn}=\{x\in\mathbb{R}:\ |x|<m/n\}$*（$m,n\in\mathbb{N}$，即 $A_{mn}=(-m/n,\ m/n)$）：
- **固定 $m$ 时**：$m/n$ 在 $n=1$ 时最大（等于 $m$），故 $\bigcup_{n=1}^{\infty}A_{mn}=(-m,m)$；再对 $m$ 取交得左边 $=\bigcap_{m=1}^{\infty}(-m,m)=\mathbb{R}$（任何实数 $x$ 都落在某个 $(-m,m)$ 内，故落在所有充分大的 $(-m,m)$ 内）；
- **固定 $n$ 时**：$m/n$ 在 $m=1$ 时最小（等于 $1/n$），故 $\bigcap_{m=1}^{\infty}A_{mn}=(-1/n,\ 1/n)$；再对 $n$ 取并得右边 $=\bigcup_{n=1}^{\infty}(-1/n,1/n)=\{0\}$（$0$ 属于每个 $(-1/n,1/n)$；而任何 $x\neq0$ 当 $n$ 充分大时 $|x|\geqslant1/n$，被排除）。

于是左边 $=\mathbb{R}\neq\{0\}=$ 右边。

**这个反例不是玩具**：数学分析中"$f$ 连续"是 $\forall x_0\,\forall\varepsilon\,\exists\delta$，"$f$ 一致连续"是 $\forall\varepsilon\,\exists\delta\,\forall x_0$——把 $\forall\varepsilon$ 与 $\exists\delta$ 交换了位置，强度就变了（$f(x)=x^{2}$ 在 $\mathbb{R}$ 上连续但不一致连续）。翻译成集合语言，就是 $\bigcap\bigcup\neq\bigcup\bigcap$。**写集合式时每换一层量词，都要停下来想一次顺序对不对。**

> **停顿自问**：为什么 $\bigcup$ 对应"存在"而 $\bigcap$ 对应"任意"？
> 因为 $\bigcup_{\lambda}A_\lambda$ 的定义是"**存在**某个 $\lambda$ 使 $x\in A_\lambda$"，$\bigcap_{\lambda}A_\lambda$ 的定义是"对**任意** $\lambda$ 都有 $x\in A_\lambda$"。这不是约定俗成，而是定义本身直接给出的——回头读 (1.1.1)、(1.1.2) 两式就能确认。

### 1.1.2 上极限与下极限

**定义 1.1.5（上确界）**：考虑 $\mathbb{R}$ 中的集合 $E$。若存在 $h\in\mathbb{R}$，使得对 $\forall x\in E$ 都有 $x\leqslant h$，则称 $h$ 是 $E$ 的一个**上界**。若数 $h$ 满足：(1) $h$ 是 $E$ 的一个上界；(2) 若 $h'$ 也是 $E$ 的上界，则必有 $h\leqslant h'$——就称 $h$ 是集合 $E$ 的**上确界**，记作 $h=\sup E$ 或 $h=\sup_{x\in E}x$（$\sup$ 读作"上确界"，即**最小上界**）。

**定义 1.1.6（下确界）**：设 $E\subset\mathbb{R}$，$m\in\mathbb{R}$。若 $\forall x\in E$ 均有 $x\geqslant m$，则称 $m$ 是 $E$ 的一个**下界**。若 $m$ 满足：(1) $m$ 是 $E$ 的下界；(2) 若 $m'$ 也是 $E$ 的下界，则必有 $m'\leqslant m$——就称 $m$ 是 $E$ 的**下确界**（**最大下界**），记作 $m=\inf E$ 或 $m=\inf_{x\in E}x$（$\inf$ 读作"下确界"）。

**定理 1.1.7（确界存在定理）**：$\mathbb{R}$ 中一个非空的、有上（下）界的集合，必有上（下）确界。

这是实数连续性理论中最重要的结果之一，它把 $\mathbb{R}$ 与 $\mathbb{Q}$ 区分开（$\mathbb{Q}$ 中 $\{x\in\mathbb{Q}:x^{2}<2\}$ 就没有上确界）。若序列 $x_n$ 单调上升有上界，则 $\lim_{n\to\infty}x_n=\sup_n x_n$；单调下降有下界时 $\lim_{n\to\infty}x_n=\inf_n x_n$。注意**集合 $E$ 的上确界与下确界可能属于 $E$，也可能不属于 $E$**。此外若记 $-E=\{-x\mid x\in E\}$，则 $\sup(-E)=-\inf E$，$\inf(-E)=-\sup E$。

**定理 1.1.8（确界的 $\varepsilon$ 刻画）**：设 $E\subset\mathbb{R}$，则

(1) $h=\sup E$ 的充要条件是：(i) $h$ 是 $E$ 的一个上界；(ii) $\forall\varepsilon>0$，$\exists x'\in E$ 使得 $x'>h-\varepsilon$；
(2) $m=\inf E$ 的充要条件是：(i) $m$ 是 $E$ 的一个下界；(ii) $\forall\varepsilon>0$，$\exists x'\in E$ 使得 $x'<m+\varepsilon$。

*证明（只证上确界部分）*：
**必要性**（反证）：设 (ii) 不成立，则 $\exists\varepsilon_0>0$，使得 $\forall x\in E$ 均有 $x\leqslant h-\varepsilon_0$。于是 $h-\varepsilon_0$ 是比 $h$ 还小的上界——**因为** $h$ 是上确界即最小上界，这与 $h$ 是上确界矛盾。
**充分性**（反证）：设 $h$ 不是 $E$ 的上确界，即 $\exists h'$ 是上界但 $h>h'$。令 $\varepsilon=h-h'>0$。由条件 (ii)，$\exists x'\in E$ 使 $x'>h-\varepsilon=h'$——**因为** $h'$ 是 $E$ 的上界，这与 $x'>h'$ 矛盾。$\square$

**注 1**：为方便起见，若 $E$ 无上界，则记 $\sup E=+\infty$；若 $E$ 无下界，则记 $\inf E=-\infty$。

**定义 1.1.9（点列的上极限与下极限）**：给定 $\{x_n\}\subset\mathbb{R}$，令
$$
h_n=\sup_{k\geqslant n}x_k,\qquad m_n=\inf_{k\geqslant n}x_k .
$$
显然 $m_n\leqslant x_n\leqslant h_n$，且 $\{h_n\}$ 是**非升列**、$\{m_n\}$ 是**非降列**。定义点列 $\{x_n\}$ 的**上极限**为
$$
\varlimsup_{n\to\infty}x_n=\lim_{n\to\infty}h_n;\tag{1.1.8}
$$
**下极限**为
$$
\varliminf_{n\to\infty}x_n=\lim_{n\to\infty}m_n.\tag{1.1.9}
$$
（$\varlimsup$ 读作"上极限"，$\varliminf$ 读作"下极限"。）

**注 2**：对任何点列，$\varlimsup_{n\to\infty}x_n$ 与 $\varliminf_{n\to\infty}x_n$ 可以是有限值，也可以是 $\pm\infty$，且显然有
$$
\varlimsup_{n\to\infty}x_n=\inf_{n\geqslant1}\sup_{k\geqslant n}x_k,\qquad
\varliminf_{n\to\infty}x_n=\sup_{n\geqslant1}\inf_{k\geqslant n}x_k,\qquad
\varliminf_{n\to\infty}x_n\leqslant\varlimsup_{n\to\infty}x_n .
$$

**注 3（上下极限的性质）**：
(1) 点列 $\{x_n\}$ 存在极限的充要条件是 $\varliminf_{n\to\infty}x_n=\varlimsup_{n\to\infty}x_n$；
(2) $\varliminf_{n\to\infty}(-x_n)=-\varlimsup_{n\to\infty}x_n$，$\varlimsup_{n\to\infty}(-x_n)=-\varliminf_{n\to\infty}x_n$；
(3) 若 $x_n\leqslant y_n$，则 $\varlimsup x_n\leqslant\varlimsup y_n$，$\varliminf x_n\leqslant\varliminf y_n$；
(4) 设 $x_n>0$，则 $\varlimsup\frac{1}{x_n}=\frac{1}{\varliminf x_n}$；
(5) 设 $\{x_{n_k}\}$ 是收敛子序列，因为 $m_{n_k}\leqslant x_{n_k}\leqslant h_{n_k}$，所以
$$
\varliminf_{n\to\infty}x_n\leqslant\lim_{k\to\infty}x_{n_k}\leqslant\varlimsup_{n\to\infty}x_n .
$$

**定理 1.1.10（上极限的子列刻画）**：设 $\{x_n\}\subset\mathbb{R}$，则 $a=\varlimsup_{n\to\infty}x_n$（$-\infty\leqslant a\leqslant\infty$）的充要条件是：
(1) $\exists$ 子列 $\{x_{n_k}\}$ 使得 $\lim_{k\to\infty}x_{n_k}=a$；
(2) 对于任意有广义极限的子列 $\{x_{l_j}\}$，有 $\lim_{j\to\infty}x_{l_j}=a'\leqslant a$。

*证明概要*：
**必要性**：由注 3(5) 得 (2)。只证 (1)。由 $a=\lim h_n$，分三种情况：
(i) $a$ 有限。因为 $h_n\to a$，$\exists l_1$ 使 $a-1<h_{l_1}=\sup_{n\geqslant l_1}x_n<a+1$，于是 $\exists n_1\geqslant l_1$ 使 $a-1<x_{n_1}<a+1$；再由 $h_n\to a$，$\exists l_2\geqslant n_1$ 使 $a-\frac12<h_{l_2}<a+\frac12$，于是 $\exists n_2\geqslant l_2$ 使 $a-\frac12<x_{n_2}<a+\frac12$；依次下去得到子列 $\{x_{n_k}\}$ 满足 $a-1/k<x_{n_k}<a+1/k$——**因为**左右两端都趋于 $a$，故 $\lim_k x_{n_k}=a$。
(ii) $a=+\infty$：因为 $h_n\to+\infty$，可依次取 $n_k$ 使 $x_{n_k}>k$——**因为** $k\to\infty$，故 $\lim_k x_{n_k}=+\infty=a$。
(iii) $a=-\infty$：显然成立。
**充分性**：设 $a$ 满足 (1)(2)。由注 3(5)，$a\leqslant\varlimsup x_n$。若等号不成立，记 $\varlimsup x_n=a'>a$；由必要性证明可知存在子列 $x_{n_k}\to a'>a$——**因为** 这与条件 (2) 矛盾，故 $\varlimsup x_n=a$。$\square$

**集列的上极限与下极限**：

**定义 1.1.3**：设 $\{A_n\}$ 是一集合列，记
$$
\varlimsup_{n\to\infty}A_n=\bigcap_{n=1}^{\infty}\bigcup_{k=n}^{\infty}A_k;\tag{1.1.4}
$$
$$
\varliminf_{n\to\infty}A_n=\bigcup_{n=1}^{\infty}\bigcap_{k=n}^{\infty}A_k.\tag{1.1.5}
$$
它们分别称为集合列 $\{A_n\}$ 的**上极限**与**下极限**；若二者相等，则称之为集合列 $\{A_n\}$ 的**极限**，记作 $\lim_{n\to\infty}A_n$，此时称集合列 $\{A_n\}$ **收敛**。

**由定义直接读出的含义**（这是最实用的部分）：
- $x$ 属于**上极限** $\iff$ **有任意大的 $n$** 使 $x\in A_n$ $\iff$ $x$ 属于**无穷多个** $A_n$；
- $x$ 属于**下极限** $\iff$ **当 $n$ 充分大时** $x\in A_n$ $\iff$ 除**有限个**下标外 $x$ 属于每个 $A_n$。

**直觉**：把 $A_n$ 想成"第 $n$ 天发生的事件"——上极限是"**无穷多天**都发生的事"（允许偶尔缺席），下极限是"**从某天起天天**发生的事"（要求最终稳定）。显然 $\varliminf_{n\to\infty}A_n\subset\varlimsup_{n\to\infty}A_n$。

**单调集列必收敛**：若 $\{A_n\}$ 是升列，则 $\lim_{n\to\infty}A_n=\bigcup_{n=1}^{\infty}A_n$；若 $\{A_n\}$ 是降列，则 $\lim_{n\to\infty}A_n=\bigcap_{n=1}^{\infty}A_n$。由于 $\bigcup_{k=n}^{\infty}A_k$ 是降列、$\bigcap_{k=n}^{\infty}A_k$ 是升列，上下极限还可以改写成
$$
\varlimsup_{n\to\infty}A_n=\lim_{n\to\infty}\bigcup_{k=n}^{\infty}A_k,\qquad
\varliminf_{n\to\infty}A_n=\lim_{n\to\infty}\bigcap_{k=n}^{\infty}A_k.\tag{1.1.6–1.1.7}
$$
用集列极限的语言，前面的 $A=\bigcup_n A_n$ 可写成 $A=\lim_{n\to\infty}A_n$，$A^{\mathrm{c}}=\lim_{n\to\infty}A_n^{\mathrm{c}}$，而 (1.1.3) 式可写成
$$
A=\bigcap_{m=1}^{\infty}\varliminf_{n\to\infty}A_{mn}.
$$

**定义（特征函数）**：对每个集合 $A$，定义函数
$$
\chi_A(x)=\begin{cases}1,&x\in A,\\ 0,&x\notin A.\end{cases}\tag{1.1.10}
$$
（$\chi_A$ 读作"$A$ 的特征函数"。）它是取值于 $\{0,1\}$ 的函数，**把集合问题翻译成函数问题**。给定集合列 $\{A_n\}$，容易证明
$$
\varliminf_{n\to\infty}\chi_{A_n}(x)=\chi_{\varliminf_{n\to\infty}A_n}(x),\qquad
\varlimsup_{n\to\infty}\chi_{A_n}(x)=\chi_{\varlimsup_{n\to\infty}A_n}(x).\tag{1.1.11–1.1.12}
$$
（教材 (1.1.12) 式右端下标的印刷为 $\varliminf$，按 (1.1.11) 的对偶与习题 13 的要求，应为 $\varlimsup$。）这条恒等式的意义：**集列收敛 $\iff$ 其特征函数列逐点收敛**。

**函数的上极限与下极限**：设 $\lambda>0$，$f(x)$ 在 $(a-\lambda,a+\lambda)\setminus\{a\}$ 上有定义。

**定义 1.1.11**：
$$
\varlimsup_{x\to a}f(x)=\lim_{\delta\to0}\sup_{0<|x-a|<\delta}f(x)=\inf_{\delta>0}\sup_{0<|x-a|<\delta}f(x);\tag{1.1.13}
$$
$$
\varliminf_{x\to a}f(x)=\lim_{\delta\to0}\inf_{0<|x-a|<\delta}f(x)=\sup_{\delta>0}\inf_{0<|x-a|<\delta}f(x).\tag{1.1.14}
$$

**定理 1.1.12**：$\varlimsup_{x\to a}f(x)=L$（有限或无限）的充要条件是：
(1) $\exists\{x_n\}\subset(a-\lambda,a+\lambda)\setminus\{a\}$，$x_n\to a$ 且 $f(x_n)\to L$；
(2) 对于任意 $(a-\lambda,a+\lambda)\setminus\{a\}$ 中趋于 $a$ 的点列 $\{x_n'\}$，若 $f(x_n')\to L'$，则 $L'\leqslant L$。

（对函数列 $f_n$ 也可逐点定义上极限函数 $\varlimsup_n f_n$ 与下极限函数 $\varliminf_n f_n$，定义域为 $D$：对 $\forall x_0\in D$，规定 $\varlimsup_n f_n(x_0)=\varlimsup_n(f_n(x_0))$，下极限同理。）

**反例（上下极限不相等的振荡集列）**：设
$$
A_{2m+1}=\Big[0,\ 2-\frac{1}{2m+1}\Big]\ (m=0,1,2,\dots),\qquad
A_{2m}=\Big[0,\ 1+\frac{1}{2m}\Big]\ (m=1,2,\dots).
$$
则
$$
\varlimsup_{n\to\infty}A_n=[0,2),\qquad \varliminf_{n\to\infty}A_n=[0,1].
$$
*为什么*：区间 $(1,2)$ 中的点被**无穷多个**奇指标集合包含（奇指标集合越来越长，右端 $2-\frac{1}{2m+1}\to2$），但只被**有限个**偶指标集合包含（偶指标集合右端 $1+\frac{1}{2m}\to1$）——所以它们属于上极限而不属于下极限；而 $[0,1]$ 中的点被**每一个** $A_n$ 包含，故属于下极限。端点 $2$ 不属于上极限，因为没有一个 $A_n$ 含 $2$。

**反例（点列的上下极限）**：$x_n=(-1)^{n}$ 时 $h_n\equiv1$、$m_n\equiv-1$，故 $\varlimsup x_n=1$，$\varliminf x_n=-1$。两者不等，正是"极限不存在"的精确表达（注 3(1)）。

**例题（求集列的极限）**：设 $A_n=\big(-1-\frac1n,\ 1+\frac1n\big)$，求 $\lim_{n\to\infty}A_n$。

**原始信息**：$\{A_n\}$ 是一个**降列**——因为 $-1-\frac1n$ 随 $n$ 增大而增大、$1+\frac1n$ 随 $n$ 增大而减小，所以 $A_1\supset A_2\supset\cdots$（区间越缩越窄）。
**代入**：对降列有 $\lim_{n\to\infty}A_n=\bigcap_{n=1}^{\infty}A_n$。
**结果**：$x\in\bigcap_n A_n$ $\iff$ 对一切 $n$ 有 $-1-\frac1n<x<1+\frac1n$ $\iff$ $-1\leqslant x\leqslant 1$。故
$$
\lim_{n\to\infty}A_n=\bigcap_{n=1}^{\infty}\Big(-1-\frac1n,\ 1+\frac1n\Big)=[-1,1].
$$
**结论**：可数个**开**集的交**可以不是**开集——每一层 $A_n$ 都把端点 $-1$ 与 $1$ 排除在外，但交的过程把两端的"缺口"压到了零，端点被"补"了回来。这正是"**有限**多个开集的交是开集，任意多个开集的交未必是开集"的反例（详见 [[Sec1.3 n 维欧氏空间]] §1.3.2 的运算规律）。

**例题（一个"看穿定义"的集列极限）**：设 $A_n=\{m/n\mid m\in\mathbb{Z}\}$，$n=1,2,\dots$，证明
$$
\varliminf_{n\to\infty}A_n=\mathbb{Z},\qquad \varlimsup_{n\to\infty}A_n=\mathbb{Q}.
$$
**原始信息**：$A_n$ 是分母恰为 $n$ 的全部有理数（含整数）。
**代入**：$x\in\varliminf A_n$ 意味着"当 $n$ 充分大后，$x$ 是分母为 $n$ 的有理数"——而 $x$ 的分母固定，只可能对有限多个 $n$ 写成 $m/n$，除非 $x$ 是整数（整数 $k$ 可写成 $kn/n$，对**一切** $n$ 成立）。
**结果**：$\varliminf A_n=\mathbb{Z}$。又 $x\in\varlimsup A_n$ 意味着"$x$ 有无穷多个分母"——有理数 $p/q$ 可写成 $\frac{kp}{kq}$，分母 $kq$ 无穷多；无理数则没有任何分母。故 $\varlimsup A_n=\mathbb{Q}$。
**结论**：$\varliminf A_n\subset\varlimsup A_n$ 严格成立（$\mathbb{Z}\subsetneqq\mathbb{Q}$），这个集列不收敛。它是"上下极限差距有多大"的直观标本。

> **问-答（旧讲解包检验回路，保留）**
>
> **Q2（翻译练习）** 用集合运算写出"函数列 $f_n$ 在点 $x$ 处**不**收敛到 $0$"（允许极限不存在）的点集，并说明每一步用了什么规则。
>
> > [!note]- 答案
> > $\{x:\ \lim f_n(x)\neq0\text{ 或不存在}\}=\bigcup_{\varepsilon\in\mathbb{R}^{+}}\bigcap_{N=1}^{\infty}\bigcup_{n=N}^{\infty}\{x:\ |f_n(x)|\geqslant\varepsilon\}$。理由：先写收敛点集（任意 $\varepsilon$ → 交，存在 $N$ → 并，任意 $n\geqslant N$ → 交），再用德摩根公式逐层取补：补集把"任意"变"存在"、把"$<$"变"$\geqslant$"。最后用"任意 $\varepsilon$ 等价于任意 $\frac1k$"可把 $\mathbb{R}^{+}$ 换成可数指标集。
>
> **停顿自问（动机复述）** 第一章要解决什么问题？"可数"为什么是测度论的必备词汇？
>
> > [!note]- 答案
> > ① 问题：把数学分析中的极限、连续、积分翻译成集合语言，并回答"无限集合是否一样多"。② 可数性给出最小无穷等级 $\aleph_0$：可数集的并、交、直积仍可数，是可数可加测度能安全操作的集合类。③ Ch2 说"可数个零测集的并仍是零测集"、Ch3 说"可数个可测集的可数并仍可测"，这些语句没有"可数"概念根本无法书写；而实数不可数（基数 $\mathfrak{c}>\aleph_0$）保证了测度论没有变成"全体集合都测度为零"的平凡理论。
>
> **讲给别人听清单（旧讲解包 §八.2 保留，本节部分）**：① 引言的两个需求：极限的集合翻译、康托尔的无穷分级；② "存在 ↔ 并，任意 ↔ 交"的翻译规则 $+$ 收敛点集的完整式子；③ 德摩根公式与它对"任意/存在否定"的解释；④ 上极限（无穷多个）与下极限（最终全在）的定义与并交表示。
>
> **回填提示（旧讲解包 §八.3 保留，本节部分）**：卡在**上下极限** → 用手画 $A_{2m+1}=[0,2-\frac{1}{2m+1}]$、$A_{2m}=[0,1+\frac{1}{2m}]$ 的图，标出 $[0,1]$ 与 $(1,2)$ 两类点的归属；卡在**集合运算式写不出来** → 先默写德摩根公式，再把量词逐层翻译（$\forall\to\bigcap$，$\exists\to\bigcup$）；**下一步**：集合本身没有"关系"，元素之间不能谈远近，下一节要给它装上"距离"。

## 去脉（学完去哪）

- **当代应用**：集合运算式是**测度论与概率论的书写语言**。概率里"事件 $A_n$ 无穷多次发生"记作 $\varlimsup A_n$（Borel–Cantelli 引理的两个方向都直接用它），"最终必然发生"记作 $\varliminf A_n$——本节的定义原样搬过去就是概率论的第一章。
- **跨领域解读**：量词 ↔ 并交的翻译规则，本质上是**逻辑与集合代数的同构**：$\exists$ 对应 $\bigcup$、$\forall$ 对应 $\bigcap$、$\neg$ 对应取补。所以德摩根公式不只是集合恒等式，它是"否定一个量化命题"的机械算法。程序语言里的"任意/存在"量词、数据库的 SELECT/WHERE 语义，都建在同一套规则上。
- **高层视角**：本章提供的是一套**语法**：集合运算是"把性质写成式子"，势（[[Sec1.2 映射]]）是"给式子里的集合量大小"。Ch2 的外测度定义 $m^{*}(E)=\inf\{\sum|I_k|:\ E\subset\bigcup I_k\}$——那个 $\bigcup$ 和 $\inf$ 就是本节的符号；Ch3 的 Levi 定理把 $f=\lim f_n$ 写成 $\bigcup$ 的升列，用的就是"升列极限 $=$ 并"这一条。
- **下一步**：集合本身没有"关系"，元素之间不能谈远近。要谈极限、连续，必须先给集合装上"距离"——这正是 [[Sec1.3 n 维欧氏空间]] 的工作。

## 防跳跃

- [ ] $\mathbb{R}$ 的完备性（确界存在定理 1.1.7）为什么是"连续性的公理级"事实？它和 Dedekind 分割、Cauchy 序列完备性三种表述的等价关系，需要时可以展开
- [ ] 幂集 $2^{X}$ 与势记号 $2^{\alpha}$ 的关系（$|2^{A}|=2^{|A|}$）——见 [[Sec1.2 映射]]
- [ ] 特征函数为什么是积分论中"最简单的可测函数"：$\chi_A$ 可测 $\iff$ $A$ 可测（Ch3 会用到）
- [ ] 集合列上下极限与测度可交换的条件：为什么单调升列总有 $m(\lim A_n)=\lim m(A_n)$（Ch2 §2.1）
- [ ] 不可数个交并的"可数化"替换：什么情况下换得掉、什么情况下换不掉，需要系统整理

## 来源与映射

| 本节点内容 | 来源 | 处理 |
|---|---|---|
| 集合的朴素定义、属于、空集、单元素集、记法约定、列举法与描述法 | 旧《Ch1 集合》§2.1；郭版教材 §1.1.1 | 原文迁移 + 合并去重 |
| 子集、真子集、相等、全集与补集 | 旧《Ch1 集合》§2.2；郭版教材 §1.1.1 | 原文迁移 |
| 并、交、差的定义与算例 | 郭版教材 §1.1.1 定义 1.1.1 | 新写补缺（旧包只有并交补） |
| 定理 1.1.2 六条运算律 + 德摩根证明 | 郭版教材 §1.1.1 定理 1.1.2 | 新写补缺（旧包只给结论） |
| 无限并交 (1.1.1)(1.1.2)、分配律与对偶律的推广 | 旧《Ch1 集合》§3.1；郭版教材 §1.1.1 | 原文迁移 + 合并去重 |
| **量词 ↔ 并交翻译规则** | 旧《Ch1 集合》§3.1、§3.2 | 原文迁移（原文保留，加"★"标记） |
| 幂集 $2^{X}$ 与"$n$ 元集恰有 $2^{n}$ 个子集" | 郭版教材 §1.1.1 | 新写补缺 |
| 直积（笛卡尔乘积）、$X^{n}$、$\mathbb{R}^{n}$ 作为 $\mathbb{R}$ 的 $n$ 次幂 | 旧《Ch1 集合》§3.4；郭版教材 §1.1.1 定义 1.1.4 | 原文迁移 |
| 集合族、集合列、升列/降列/单调列 | 郭版教材 §1.1.1 | 新写补缺 |
| 收敛点集的三重交并式 (1.1.3)（旧包 §3.2 的"关键应用"） | 旧《Ch1 集合》§3.2；郭版教材 §1.1.1 例 4 | 原文迁移 + 合并（两处是同一件事，旧包用 $\varepsilon$、教材用 $1/m$） |
| "$\mathbb{R}^{+}$ 换成 $\{1/k\}$"的可数化技巧 | 旧《Ch1 集合》§3.2 | 原文迁移 |
| 用对偶律写 $\{x:f(x)\leqslant0\}$ | 郭版教材 §1.1.1 例 2、例 3 | 新写补缺（作为例题） |
| 反例 1（差运算不满足结合律） | 郭版教材 §1.1.1 定理 1.1.2(5) 的边界 | 新写补缺 |
| 反例 2（$\bigcap\bigcup\neq\bigcup\bigcap$，量词顺序） | 郭版教材 §1.1.1 例 4 的边界 | 新写补缺 |
| 上确界、下确界、确界存在定理 1.1.7 | 旧《Ch1 集合》§3.3（仅一句）；郭版教材 §1.1.2 定义 1.1.5–1.1.6 | 新写补缺（旧包只提及 $\sup/\inf$ 读法） |
| 定理 1.1.8 确界的 $\varepsilon$ 刻画及其证明 | 郭版教材 §1.1.2 | 新写补缺 |
| 点列上下极限定义 1.1.9、注 2、注 3 五条性质 | 郭版教材 §1.1.2 | 新写补缺（旧包未讲点列上下极限） |
| 定理 1.1.10 上极限的子列刻画及证明 | 郭版教材 §1.1.2 | 新写补缺 |
| 集列上下极限定义 1.1.3、并交表示、单调列收敛 | 旧《Ch1 集合》§3.3；郭版教材 §1.1.1 定义 1.1.3 | 原文迁移 + 合并去重 |
| 特征函数 $\chi_A$ 与 (1.1.11)(1.1.12) | 郭版教材 §1.1.1、§1.1.2 | 新写补缺 |
| 函数的上极限与下极限（定义 1.1.11、定理 1.1.12） | 郭版教材 §1.1.2 | 新写补缺 |
| 反例（振荡集列 $\varlimsup=[0,2)$、$\varliminf=[0,1]$） | 旧《Ch1 集合》§3.3 | 原文迁移（原文保留） |
| 反例（点列 $x_n=(-1)^n$） | 郭版教材 §1.1.2 注 3(1) | 新写补缺 |
| 例题（$A_n=(-1-\frac1n,1+\frac1n)$ 求极限） | 郭版教材 §1.1 习题 9 | 新写补缺 |
| 例题（$A_n=\{m/n\}$ 的上下极限） | 郭版教材 §1.1 习题 11 | 新写补缺 |
| 问-答：翻译练习、动机复述 | 旧《Ch1 集合》§八.1 Q1、Q2 | 原文迁移（保留自测题形态） |
| 去脉：概率论 $\varlimsup/\varliminf$、逻辑与集合代数的同构 | —— | 新写补缺（跨领域解读） |

> **核心洞察**：这一节真正要说的是——**"任意"就是交，"存在"就是并，极限就是上下极限的相撞。** 学会把一句带量词的话逐字翻成 $\bigcup/\bigcap$ 之后，实变函数里所有"由性质定义集合"的动作都变成了机械操作；而"能换成可数个交并"这件事，正是测度论能走下去的前提。