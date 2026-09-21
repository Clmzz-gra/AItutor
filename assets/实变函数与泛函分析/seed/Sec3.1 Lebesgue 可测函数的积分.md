---
type: 节
formal: true
subject: 实变函数与泛函分析
created: 2026-09-21
updated: 2026-09-21
tags: [math, 实变函数与泛函分析]
chapter: 3
section: 3.1
---

# Sec3.1 Lebesgue 可测函数的积分

> 定位：把前两章造好的「测度」与「可测函数」组装成积分——用三步定义（非负简单函数 → 非负可测函数 → 一般可测函数）绕开 $\infty-\infty$，并说清它与黎曼积分的关系。
> 教材：郭懋正《实变函数与泛函分析》§3.1（p.91–110）
> 来源：旧讲解包《Ch5 积分论》§一–§六；郭版教材 §3.1.4（新写补缺）

> [!info] 关联笔记
> - 父级：[[Ch3 Lebesgue 积分]]
> - 前置：Ch2 §2.3 可测函数列的收敛性（可测函数、a.e. 收敛）｜ 后续：[[Sec3.2 Lebesgue 积分的极限定理]]
> - 概念：[[概念-测度与黎曼积分的类比]]

---

## 来龙（为什么需要它）

- **类比已知**：黎曼积分把定义域 $[a,b]$ 竖着切成小区间，用「高 $\times$ 宽」求和。勒贝格积分把它转 90 度——**横着切值域**：先问「函数值落在 $[y_i,y_{i+1})$ 里的那些 $x$ 组成多大的集合」，再用测度给这个集合称重。切法变了，称重的尺子就得换，这正是 Ch2 造测度、Ch2 §2.2 造可测函数的原因。
- **解决新问题**：黎曼积分有两个治不好的病。其一，**极限与积分交换的条件太苛刻**——黎曼框架下要交换 $\int\lim f_n=\lim\int f_n$ 通常得要求 $\{f_n\}$ 一致收敛；其二，**微积分基本定理不完整**——可微函数 $F$ 的导函数 $f$ 即使有界也可能不是 $R$ 可积的（Volterra 的例子），于是 Newton–Leibniz 公式 $F(x)-F(a)=\int_a^x f$ 无从成立。勒贝格积分把第一个病治成「逐点收敛 + 一个可积控制函数」，把第二个病在 a.e. 意义下治回完整。
- **理论/应用需要**：测度已经具备可数可加性，可测函数已经具备「水平集可称重」「可被简单函数递增逼近」两条性质——**地基铺好了，只差组装**。组装路线就是
  $$\int f\ \approx\ \sum_i y_i\cdot m(A_i).$$
  但直接对这条式子取极限会立刻撞上两个麻烦：$f$ 可以无界、可以取 $\pm\infty$，于是积分值可能出现 $\infty-\infty$ 的不定式。**所以勒贝格的定义分三步走，一步只解决一个麻烦**：

```
第一步（§3.1.1）非负简单函数 φ = Σ cᵢ χ_{Eᵢ}：积分 = Σ cᵢ mEᵢ（纯加权和，唯一能直接算的）
        ↓ 第二步（§3.1.1）非负可测函数 f：积分 = sup{∫φ : 0 ≤ φ ≤ f}（用简单函数从下方逼近）
        ↓ 第三步（§3.1.2）一般可测函数 f = f⁺ − f⁻：积分 = ∫f⁺ − ∫f⁻（正负部分开，避开 ∞−∞）
        ↓ 对话（§3.1.3）与黎曼积分的关系：R 可积 ⟺ a.e. 连续；反常积分的陷阱
        ↓ 推广（§3.1.4）抽象测度空间 (X, F, μ) 上的同一套定义
```

**先记住两个记号**：$(R)\int$ 表示黎曼积分，$(L)\int$ 表示勒贝格积分（$L$ = Lebesgue）。

## 主体（核心内容）

### 3.1.1 非负可测函数的积分

#### 符号约定（首次出现即定义）

- $\chi_A$（读作「集合 $A$ 的特征函数」）：$x\in A$ 时取 $1$，否则取 $0$；
- $f^+(x)=\max\{f(x),0\}$（读作「$f$ 的**正部**」），$f^-(x)=\max\{-f(x),0\}$（读作「$f$ 的**负部**」）；恒有 $f=f^+-f^-$ 与 $|f|=f^++f^-$；
- $\int_E f(x)\,dx$（读作「$f$ 在可测集 $E$ 上的勒贝格积分」）；
- $L(E)$（读作「$E$ 上勒贝格可积函数全体」）：正部、负部积分都有限的函数组成的集合；
- a.e.（almost everywhere，几乎处处）：除一个零测集外处处成立。

#### 第一步：非负简单函数的积分

**定义（非负简单函数的勒贝格积分）** 设 $E\subset\mathbb{R}^n$ 可测，$\varphi=\sum_{i=1}^{k}c_i\chi_{E_i}$，其中 $c_i\geqslant0$，$\{E_i\}$ 是 $E$ 的有限可测划分，定义
$$\int_E\varphi(x)\,dx=\sum_{i=1}^{k}c_i\,mE_i .$$
对可测子集 $A\subset E$，令 $\int_A\varphi\,dx=\sum_i c_i\,m(A\cap E_i)$。

**为什么这个定义「良定」**：同一个 $\varphi$ 可以有完全不同的分块表示（把某一块再切细）。*因为* 测度具有有限可加性，$c_i\,m(E_i)=\sum_j c_i\,m(E_{ij})$，两种表示求和结果相同——加权和不依赖分法。教材证明中「取公共加细 $E_i\cap F_j$」正是这件事的标准写法。

**例题（全章第一算）** 求 $\mathbb{R}$ 上狄利克雷函数 $D=\chi_{\mathbb{Q}}$（$\mathbb{Q}$ 读作「有理数集」）的勒贝格积分。

- **原始信息**：$D$ 在有理点取 $1$、无理点取 $0$，故 $D$ 是取值为 $0,1$ 的非负简单函数；$\mathbb{R}=\mathbb{Q}\cup(\mathbb{R}\setminus\mathbb{Q})$ 是两块互不相交的可测划分。
- **代入定义**：$\int_{\mathbb{R}}D\,dx=1\cdot m\mathbb{Q}+0\cdot m(\mathbb{R}\setminus\mathbb{Q})$。
- **结果**：$m\mathbb{Q}=0$（可数集零测），$m(\mathbb{R}\setminus\mathbb{Q})=\infty$，配合约定 $0\cdot\infty=0$，得 $\int_{\mathbb{R}}D\,dx=0$。
- **结论**：$D$ 黎曼不可积（处处不连续），但勒贝格可积且积分为 $0$——**可积函数类被极大地扩充了**；同时「可数但稠密」的 $\mathbb{Q}$ 测度为零这一 Ch2 核心结论在这里第一次变现。

**定理 1（非负简单函数积分的三条基本性质）** 设 $\varphi$ 为非负简单函数，则

1. $\int_E c\varphi\,dx=c\int_E\varphi\,dx$（$c\geqslant0$）；
2. $A,B\subset E$ 可测且不相交 $\Rightarrow\int_{A\cup B}\varphi\,dx=\int_A\varphi\,dx+\int_B\varphi\,dx$；
3. 若 $A_1\subset A_2\subset\cdots$ 且 $\bigcup_n A_n=E$，则 $\lim_n\int_{A_n}\varphi\,dx=\int_E\varphi\,dx$。

**证明一句话**：三条都直接展开成有限和 $\sum_i c_i\,m(\cdot\cap E_i)$，然后分别用「数乘分配律」「测度的有限可加性」「测度的递增连续性」即可。

**定理 2（线性）** 非负简单函数 $\varphi,\psi$ 满足
$$\int_E(\alpha\varphi+\beta\psi)\,dx=\alpha\int_E\varphi\,dx+\beta\int_E\psi\,dx\quad(\alpha,\beta\geqslant0).$$

**证明关键**：把 $\varphi,\psi$ 的不同分法做**公共加细**——用 $\{E_i\cap F_j\}$ 同时表示两者，在每块 $E_i\cap F_j$ 上 $\varphi+\psi=c_i+d_j$，于是
$$\int_E(\varphi+\psi)\,dx=\sum_{i,j}(c_i+d_j)\,m(E_i\cap F_j)=\int_E\varphi\,dx+\int_E\psi\,dx .$$

> **停顿自问**：为什么简单函数积分不需要「取极限」？——因为它只有有限块、有限个值，加权和一步到位；所有困难都被推迟到「从简单到一般」的那一步。

#### 第二步：非负可测函数的积分（取上确界）

**定义（非负可测函数的勒贝格积分）** 设 $f\geqslant0$ 在可测集 $E$ 上可测，定义
$$\int_E f(x)\,dx=\sup\left\{\int_E\varphi(x)\,dx:\ \varphi\ \text{是简单函数},\ 0\leqslant\varphi\leqslant f\ \text{于}\ E\right\}.$$
积分值允许 $+\infty$。若 $\int_E f\,dx<\infty$，称 $f$ 在 $E$ 上**勒贝格可积**（$L$ 可积）。

**直觉**：把所有「不超过 $f$ 的阶梯块」的积分拿出来，取上确界——这就是「横柱求和」的严格化，$\int_E f$ 是「从下方逼近 $f$ 的最优代价」。

> **问**：为什么不直接定义 $\int f=\sum_i y_i\,m(A_i)$？
> **答**：*因为* $f$ 可以无界、可以取 $+\infty$，直接写会同时撞上「和式发散」与「$\infty-\infty$」两个麻烦。取上确界相当于「用有限的阶梯块从下方试探到底能逼近多少」，避开了一切发散与相减。

**定理 3（四条基础性质）** 设 $f\geqslant0$ 在 $E$ 上可测，则

1. $mE=0\Rightarrow\int_E f\,dx=0$；
2. $\int_E f\,dx=0\Rightarrow f=0$ a.e. 于 $E$；
3. $\int_E f\,dx<\infty\Rightarrow f<\infty$ a.e. 于 $E$；
4. $A,B$ 不相交可测 $\Rightarrow\int_{A\cup B}f\,dx=\int_A f\,dx+\int_B f\,dx$。

**证明 (2)（本章第一次「用测试函数压出零测」）**：令 $A_n=E[f\geqslant1/n]$，作简单函数 $\varphi_n=\frac1n\chi_{A_n}$。*因为* $\varphi_n\leqslant f$ 且 $\int_E f=0$，
$$0=\int_E f\,dx\geqslant\int_E\varphi_n\,dx=\frac1n\,mA_n\geqslant0\ \Longrightarrow\ mA_n=0 .$$
再 *因为* $E[f>0]=\bigcup_n A_n$ 是可数并，故 $mE[f>0]=0$，即 $f=0$ a.e.。$\square$

**证明 (3)**：令 $E_\infty=E[f=+\infty]$。*因为* $\varphi_n=n\chi_{E_\infty}\leqslant f$，故 $n\,mE_\infty\leqslant\int_E f\,dx<\infty$ 对一切 $n$ 成立，令 $n\to\infty$ 得 $mE_\infty=0$。$\square$

**证明 (4)**：对 $A\cup B$ 上任一满足 $0\leqslant\varphi\leqslant f$ 的简单函数，用定理 1(2) 拆开 $\int_{A\cup B}\varphi=\int_A\varphi+\int_B\varphi$，两侧取上确界夹逼即得。$\square$

**定理 4（单调性与 a.e. 相等）** $f\leqslant g$ a.e. $\Rightarrow\int_E f\leqslant\int_E g$；特别地 $f=g$ a.e. $\Rightarrow$ 两者积分相等。

**证明**：把例外集 $E[f>g]$ 挖掉（它是零测集），在剩下的 $E_1=E[f\leqslant g]$ 上，每个不超过 $f$ 的简单函数也不超过 $g$，取上确界即得。$\square$

> **核心事实**：**积分不看零测集**——在零测集上随便改函数值，积分不变。这是勒贝格积分区别于黎曼积分的第一个「宽容」。

**反例（定理 3(2) 不能加强为「积分 $=0$ 则函数恒为 $0$」）**：取 $D=\chi_{\mathbb{Q}\cap[0,1]}$，则 $\int_{[0,1]}D\,dx=0$，但 $D\not\equiv0$（$D$ 在有理点取 $1$）。**边界就在「a.e.」三个字上**：结论只能到「几乎处处为 $0$」，因为零测集上的取值对积分完全没有贡献。同理 $\int_E f=\int_E g$ 也只推出 $f=g$ a.e.。

**例题（用上确界定义实算一次）** 求 $\int_{[0,1]}x\,dx$。

- **原始信息**：$f(x)=x$ 在 $[0,1]$ 上非负可测（连续）。
- **构造逼近**：取 $\varphi_n=\sum_{k=1}^{n}\frac{k-1}{n}\chi_{[\frac{k-1}{n},\frac{k}{n}]}$，*因为* 在每个小区间上 $\frac{k-1}{n}\leqslant x$，故 $0\leqslant\varphi_n\leqslant f$。
- **代入定义**：$\int_{[0,1]}\varphi_n\,dx=\sum_{k=1}^{n}\frac{k-1}{n}\cdot\frac1n=\frac{n-1}{2n}\to\frac12$。
- **结果与结论**：所有 $\varphi\leqslant f$ 的简单函数积分都不超过 $\frac12$（可用分割的细度论证），而 $\frac12$ 又被 $\varphi_n$ 逼近到，故上确界 $\int_{[0,1]}x\,dx=\frac12$，与黎曼积分一致。

### 3.1.2 一般可测函数的积分

#### 第三步：正负部分开

**定义（一般可测函数的积分）** 设 $f$ 在可测集 $E$ 上可测。

- 若 $\int_E f^+\,dx$ 与 $\int_E f^-\,dx$ 中**至少一个有限**，称 $f$ 在 $E$ 上**积分确定**，并定义
  $$\int_E f(x)\,dx=\int_E f^+(x)\,dx-\int_E f^-(x)\,dx ;$$
- 若两者**都有限**，称 $f$ 在 $E$ 上**勒贝格可积**（$L$ 可积），全体记为 $L(E)$。

**读法**：积分确定 = 积分值存在（可为 $\pm\infty$ 或有限实数）；$L$ 可积 = 积分值是有限实数。例如「正负面积都无穷」的函数**连积分确定都不是**。

**定理 5（七条基本性质）** 设 $f$ 在 $E$ 上可测：

1. **零测集上一切函数可积且积分为零**：$mE=0\Rightarrow$ 任何 $f$ 在 $E$ 上 $L$ 可积且 $\int_E f=0$。*因为* $f^+,f^-$ 都是 $E$ 上非负可测函数，而定理 3(1) 说零测集上非负积分恒为 $0$。
2. **可积函数 a.e. 有限**：$f\in L(E)\Rightarrow|f|<\infty$ a.e.。*因为* 两个非负积分都有限，对 $f^+$、$f^-$ 分别用定理 3(3)。
3. **区域可加**：$E=A\cup B$ 不相交可测 $\Rightarrow\int_E f=\int_A f+\int_B f$。*因为* 对 $f^+,f^-$ 分别用定理 3(4) 再相减。
4. **a.e. 相等不改积分**：$f=g$ a.e. $\Rightarrow$ 两者积分同确定、同值。*因为* $f^\pm=g^\pm$ a.e.，用定理 4。
5. **单调性**：$f\leqslant g$ a.e. $\Rightarrow\int_E f\leqslant\int_E g$；特别地，若 $mE<\infty$ 且 $b\leqslant f\leqslant B$ a.e.，则 $b\,mE\leqslant\int_E f\leqslant B\,mE$（**有界函数在有限测度集上必可积**）。
6. **绝对值不等式**：$f\in L(E)\Rightarrow|f|\in L(E)$ 且 $\left|\int_E f\right|\leqslant\int_E|f|$。*因为* $\int_E|f|=\int_E f^++\int_E f^-<\infty$，而 $\left|\int_E f\right|=\left|\int_E f^+-\int_E f^-\right|\leqslant\int_E f^++\int_E f^-$。
7. **控制判据**：$|f|\leqslant g$ a.e. 且 $g$ 非负 $L$ 可积 $\Rightarrow f\in L(E)$ 且 $\left|\int_E f\right|\leqslant\int_E|f|\leqslant\int_E g$。

**定理 6（线性）** 设 $f,g\in L(E)$，$\lambda\in\mathbb{R}$，则 $\lambda f$、$f+g$、$\alpha f+\beta g$ 都可积，且
$$\int_E\lambda f=\lambda\int_E f,\qquad \int_E(f+g)=\int_E f+\int_E g .$$

**证明要领**：数乘按 $\lambda=0$、$\lambda>0$、$\lambda<0$ 分三种情形（$\lambda<0$ 时用 $(\lambda f)^+=|\lambda|f^-$ 换号）；加法先用不等式 $(f+g)^+\leqslant f^++g^+$ 与 $(f+g)^-\leqslant f^-+g^-$ 证明可积，再搬运恒等式
$$(f+g)^++f^-+g^-=(f+g)^-+f^++g^+$$
两边积分后整理即得。细节繁琐，但每一步都只是「正负部 + 定理 3」。

**反例（线性定理中「$f,g$ 可积」的条件不可少）**：在 $[0,\infty)$ 上取 $f\equiv1$、$g\equiv-1$。两者都**积分确定**（$\int f=+\infty$、$\int g=-\infty$），但 $\int f+\int g=+\infty+(-\infty)$ 无意义；而 $f+g\equiv0$ 的积分是 $0$。**所以**「积分确定」不足以保证线性公式成立，必须要求两者**都可积**（两个积分都是有限实数，相加才合法）。这条反例是第三步「要求正负部都有限」的直接理由。

**定理 7（积分的绝对连续性）** 设 $f\in L(E)$。则对任意 $\varepsilon>0$，存在 $\delta>0$，使得只要可测集 $A\subset E$ 满足 $mA<\delta$，就有
$$\left|\int_A f\,dx\right|\leqslant\int_A|f|\,dx<\varepsilon .$$

**证明**：*因为* $\int_E|f|<\infty$，由非负可测函数积分的定义可取简单函数 $\varphi$，$0\leqslant\varphi\leqslant|f|$，使 $\int_E(|f|-\varphi)\,dx<\varepsilon/2$。令 $M=1+\max\varphi$（$\varphi$ 只取有限个值，故 $M<\infty$）、$\delta=\varepsilon/(2M)$。任取满足 $mA<\delta$ 的可测集 $A$，
$$\int_A|f|\,dx=\int_A(|f|-\varphi)\,dx+\int_A\varphi\,dx\leqslant\frac{\varepsilon}{2}+M\cdot mA<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon .\qquad\square$$

**直觉**：把积分看成定义在可测集上的**集合函数** $A\mapsto\int_A f$，它关于测度是绝对连续的——集合越小，积分越小。这一条是后面「分布函数的连续性」与概率论中积分性质的源头。

**定理 8（积分的可数可加性）** 设 $E=\bigcup_n E_n$，$E_n$ 两两不相交可测，$f$ 在 $E$ 上积分确定，则
$$\int_E f(x)\,dx=\sum_{n=1}^{\infty}\int_{E_n}f(x)\,dx .$$

**证明**：对 $f^+$ 用非负情形的逐项积分（注意 $f^+=\sum_n f^+\chi_{E_n}$），对 $f^-$ 同理；*因为* 「积分确定」保证两个正项级数至少一个收敛，故可逐项相减。$\square$

**例题（a.e. 相等派上用场）** 求 $f(x)=x$（$x$ 为无理点）、$f(x)=1$（$x$ 为有理点）在 $[0,1]$ 上的积分。

- **原始信息**：$f$ 与连续函数 $g(x)=x$ 只在 $\mathbb{Q}\cap[0,1]$ 上不同。
- **代入**：$m(\mathbb{Q}\cap[0,1])=0$，故 $f=g$ a.e.。
- **结果**：由定理 5(4)（a.e. 相等不改积分）与 §3.1.1 的例题，$\int_{[0,1]}f\,dx=\int_{[0,1]}x\,dx=\frac12$。
- **结论**：**只要在一个零测集上动手脚，积分值纹丝不动**——黎曼框架下这个函数连可积性都要重新讨论，勒贝格框架下一句话解决。

### 3.1.3 黎曼积分与 Lebesgue 积分的关系

> **先记住结论**：有界函数 $f$ 黎曼可积的**充要条件**是「$f$ 的不连续点集是零测集」（Lebesgue 判据）。这条判据的证明要用到 §3.2 的有界收敛定理，因此放在 **Sec3.2 §3.2.2** 完整论证；本节先建立「黎曼可积 $\Rightarrow$ 勒贝格可积且值相等」这一半。

**定理 9（两者相等）** 若 $f$ 在 $[a,b]$ 上有界且黎曼可积，则 $f$ 是勒贝格可积的，且
$$(L)\int_{[a,b]}f\,dx=(R)\int_a^b f\,dx .$$

**证明思路**：用达布大和构造一列阶梯函数 $g_n\to f$ a.e.（*因为* 黎曼可积时达布大和与下和之差趋于 $0$，两者夹住 $f$），*因为* $g_n$ 被常数 $M=\sup|f|$ 控制、$m[a,b]<\infty$，由**有界收敛定理**（见 Sec3.2）即可把极限穿过积分号，两侧同时收敛到 $(R)\int_a^b f$。$\square$

**定理 10（非负反常积分）** 设 $f\geqslant0$ 在 $[a,\infty)$ 上每段 $[a,A]$ 都黎曼可积，且反常积分 $(R)\int_a^\infty f\,dx$ 收敛，则 $f$ 在 $[a,\infty)$ 上勒贝格可积，且两者相等；若反常积分发散，则勒贝格积分同为 $+\infty$。

**例题（定理 10 的直接用法）** 证明 $f(x)=\dfrac{1}{\sqrt{x}}$（$x\in(0,1]$，$f(0)=0$）在 $[0,1]$ 上勒贝格可积，并求积分值。

- **原始信息**：$f\geqslant0$，在每段 $[\eta,1]$（$\eta>0$）上连续因而黎曼可积；在 $0$ 附近无界。
- **代入定理 10**：$(R)\int_0^1\frac{dx}{\sqrt{x}}=\lim_{\eta\to0^+}\bigl[2\sqrt{x}\bigr]_\eta^1=2$，反常积分收敛。
- **结果**：$f\in L[0,1]$ 且 $(L)\int_{[0,1]}f\,dx=2$。
- **结论**：**无界函数照样可以勒贝格可积**——勒贝格框架不要求 $f$ 有界，只要求 $\int|f|<\infty$。这是它对黎曼积分的第一处「放宽」。

**例题（定理 10 的直接用法）** 证明 $f(x)=\dfrac{1}{\sqrt{x}}$（$x\in(0,1]$，$f(0)=0$）在 $[0,1]$ 上勒贝格可积，并求积分值。

- **原始信息**：$f\geqslant0$，在每段 $[\eta,1]$（$\eta>0$）上连续因而黎曼可积；在 $0$ 附近无界。
- **代入定理 10**：$(R)\int_0^1\frac{dx}{\sqrt{x}}=\lim_{\eta\to0^+}\bigl[2\sqrt{x}\bigr]_\eta^1=2$，反常积分收敛。
- **结果**：$f\in L[0,1]$ 且 $(L)\int_{[0,1]}f\,dx=2$。
- **结论**：**无界函数照样可以勒贝格可积**——勒贝格框架不要求 $f$ 有界，只要求 $\int|f|<\infty$。这是它对黎曼积分的第一处「放宽」。

#### 边界：$L$ 积分不是 $R$ **反常**积分的推广

**反例（必须记住的边界）** 取
$$f(x)=\frac{\sin x}{x}\quad(x>0),\qquad f(0)=1 .$$
$(R)\int_0^\infty\frac{\sin x}{x}\,dx=\frac{\pi}{2}$ 收敛（条件收敛）。但把正负部分开：*因为* $\sin x$ 在每个长度 $2\pi$ 的周期上有一段正、一段负，
$$\int_{[0,\infty)}f^+\,dx\geqslant\sum_{n=0}^{\infty}\frac{2}{(2n+1)\pi}=\infty,\qquad \int_{[0,\infty)}f^-\,dx=\infty .$$
正部、负部都无穷 $\Rightarrow$ $f$ **连积分确定都不是**，当然更不 $L$ 可积。

**原因一句话**：勒贝格积分是**绝对收敛型**积分（$f$ 可积 $\iff|f|$ 可积，见定理 5(6)），而条件收敛的 $R$ 反常积分靠「正负相消」存活，在 $L$ 框架里不被允许。

> **问**：那勒贝格积分是不是「不如」黎曼积分，因为它算不出 $\frac{\pi}{2}$？
> **答**：不是。两种积分回答的是不同的问题：$R$ 反常积分问「部分积分的极限是否存在」，勒贝格积分问「$f$ 是否属于 $L^1$」。$L^1$ 是完备的赋范空间（见 Ch4），而 $R$ 可积函数全体不完备——**放弃条件收敛，换来的是完备性与极限定理**，这是划算的交易。

#### 对比总表

| | 黎曼积分 | 勒贝格积分 |
|---|---|---|
| 切法 | 竖切定义域 | 横切值域 |
| 可积函数 | 有界 + 不连续点集零测 | 可测 + 正负部积分有限 |
| 极限定理 | 一致收敛（条件苛刻） | 控制收敛（一个可积控制函数） |
| 反常积分 | 可条件收敛（$\sin x/x$） | 只承认绝对收敛 |
| 零测集 | 无对应物 | 积分完全忽略零测集 |
| 完备性 | $R$ 可积空间不完备 | $L^1$ 完备（Ch4 的地基） |

### 3.1.4 测度空间上可测函数的积分

> 本小节是**新写补缺**：旧讲解包只讲 $\mathbb{R}^n$ 上的勒贝格积分，抽象测度空间 $(X,\mathcal{F},\mu)$ 上的积分是郭版 §3.1.4 的内容。它把上面三步定义**一字不改地搬到一般测度空间**，为后面的概率论与 $L^p$ 空间统一铺路。

**记号**：$(X,\mathcal{F},\mu)$（读作「测度空间」，$\mathcal{F}$ 是 $X$ 上的 $\sigma$ 代数，$\mu$ 是其上的测度）；$\mathfrak{M}(X,\mathcal{F},\mu)$ 表示 $X$ 上全体 $\mu$ 可测函数。

**定义（非负 $\mu$ 可测简单函数的积分，郭版定义 3.1.16）** 设
$$h(x)=\sum_{j=1}^{m}a_j\chi_{A_j}(x),\quad \forall x\in X,$$
其中 $a_j\geqslant0$，$A_1,\dots,A_m$ 是互不相交的可测集，定义
$$\int_X h(x)\,\mu(\mathrm{d}x)=\sum_{j=1}^{m}a_j\,\mu(A_j)$$
（约定 $0\cdot\infty=0$）。记 $S^+(X)$ 为非负 $\mu$ 可测简单函数全体，则积分 $I(h)\stackrel{\mathrm{def}}{=}\int_X h\,\mu(\mathrm{d}x)$ 是 $S^+(X)$ 上的**可加泛函**：$I(h_1+h_2)=I(h_1)+I(h_2)$，且 $I(ah)=aI(h)$（$a\geqslant0$）。

**定义（非负 $\mu$ 可测函数的积分，郭版定义 3.1.17）** 设 $f$ 是 $X$ 上非负 $\mu$ 可测函数，定义
$$I(f)=\int_X f(x)\,\mu(\mathrm{d}x)=\sup\left\{\int_X h(x)\,\mu(\mathrm{d}x)\ \Big|\ h\in S^+(X),\ h\leqslant f\right\},$$
积分值允许 $+\infty$；若 $\int_X f\,\mu(\mathrm{d}x)<\infty$，称 $f$ 在 $X$ 上 **$\mu$ 可积**。

**性质（郭版同节列出，与 $\mathbb{R}^n$ 情形逐条对应）**：(1) 若 $h\in S^+(X)$ 且 $\mu(X(h>0))=0$，则 $h$ 可积且 $\int_X h\,\mu(\mathrm{d}x)=0$；(2) $f\leqslant g\ \mu$-a.e. $\Rightarrow I(f)\leqslant I(g)$；(3) 对上升函数列 $f_k\uparrow f$（$\mu$-a.e.）有 $\lim_k I(f_k)=I(f)$——**这就是抽象测度空间上的 Levi 定理**；(4) $I(af+bg)=aI(f)+bI(g)$；(5) $I(f)<\infty\Rightarrow f<\infty$ $\mu$-a.e.；(6) $I(f)=0\Rightarrow f=0$ $\mu$-a.e.。

**定义（一般 $\mu$ 可测函数的积分，郭版定义 3.1.18）** 设 $f\in\mathfrak{M}(X,\mathcal{F},\mu)$。若 $f^+$ 与 $f^-$ 中至少一个 $\mu$ 可积，则称 $f$ 的积分存在，定义为
$$\int_X f(x)\,\mu(\mathrm{d}x)=\int_X f^+(x)\,\mu(\mathrm{d}x)-\int_X f^-(x)\,\mu(\mathrm{d}x) ;$$
当右端两个积分值**皆为有限**时，称 $f$ 关于 $\mu$ 可积。$X$ 上可积函数全体记为 $L(X,\mathcal{F},\mu)$，简记 $L(X)$。

**定理 11（郭版定理 3.1.19）** 设 $f$ 是 $(X,\mathcal{F},\mu)$ 上 $\mu$ 可测函数，则
$$f\in L(X)\iff |f|\in L(X,\mathcal{F},\mu),$$
且此时 $\left|\int_X f\,\mu(\mathrm{d}x)\right|\leqslant\int_X|f|\,\mu(\mathrm{d}x)$。

**证明**：*因为* $\int_X|f|\,\mu(\mathrm{d}x)=\int_X f^+\,\mu(\mathrm{d}x)+\int_X f^-\,\mu(\mathrm{d}x)$（注意这里没有减法，故不会出现 $\infty-\infty$），右端有限 $\iff$ 两个加项都有限 $\iff f\in L(X)$。不等式由 $f=f^+-f^-$ 与三角不等式即得。$\square$

**由此立得的基本性质**：(1) $f\in L(X)\Rightarrow|f|<\infty$ $\mu$-a.e.；(2) $f=g$ $\mu$-a.e. 且 $f\in L(X)\Rightarrow g\in L(X)$ 且积分相等；(3) $|f|\leqslant g$、$g\in L(X)$ $\Rightarrow f\in L(X)$ 且 $\left|\int_X f\,\mu(\mathrm{d}x)\right|\leqslant\int_X g\,\mu(\mathrm{d}x)$；(4) 单调性：$f\leqslant g$（$f,g\in L(X)$）$\Rightarrow\int_X f\,\mu(\mathrm{d}x)\leqslant\int_X g\,\mu(\mathrm{d}x)$；(5) **若 $\mu(X)<\infty$，则 $X$ 上任意有界 $\mu$ 可测函数可积**；(6) 线性：$af+bg\in L(X)$ 且 $I(af+bg)=aI(f)+bI(g)$。

**子集上的积分**：对 $A\in\mathcal{F}$，定义
$$\int_A f(x)\,\mu(\mathrm{d}x)=\int_X f(x)\chi_A(x)\,\mu(\mathrm{d}x).$$

**定理 12（积分的绝对连续性，郭版定理 3.1.20）** 设 $f\in L(X)$，则对任意 $\varepsilon>0$，存在 $\delta>0$，使得对任意 $A\in\mathcal{F}$，只要 $\mu(A)<\delta$，就有
$$\left|\int_A f(x)\,\mu(\mathrm{d}x)\right|\leqslant\int_A|f(x)|\,\mu(\mathrm{d}x)<\varepsilon .$$

**证明**：与定理 7 逐字相同，只把 $m$ 换成 $\mu$、$E$ 换成 $X$——*因为* 定理 7 的证明只用到「非负积分的定义」「简单函数取有限个值」「测度的可加性」这三件在抽象测度空间同样成立的事。**这正是「抽象化」的价值：证明一次，处处可用。** $\square$

**例题（计数测度：积分退化成求和）** 取 $X=\mathbb{N}$、$\mathcal{F}=2^{\mathbb{N}}$、$\mu$ 为计数测度（郭版 §2.1 例 7：有限集取元素个数，无限集取 $+\infty$）。求 $\int_X f\,\mu(\mathrm{d}x)$。

- **原始信息**：每个单点集 $\{n\}$ 满足 $\mu(\{n\})=1$，且 $X=\bigcup_{n}\{n\}$ 是互不相交的可测分解。
- **代入定义**：先看非负情形。取简单函数 $h_k=\sum_{n=1}^{k}f(n)\chi_{\{n\}}$，*因为* $h_k\leqslant f$ 且 $h_k\uparrow f$，由性质 (3)（抽象 Levi 定理）
  $$\int_X f\,\mu(\mathrm{d}x)=\lim_{k\to\infty}\sum_{n=1}^{k}f(n)\cdot1=\sum_{n=1}^{\infty}f(n).$$
- **结果**：$\int_{\mathbb{N}}f\,\mu(\mathrm{d}x)=\sum_{n=1}^{\infty}f(n)$；可积 $\iff$ 级数 $\sum_n|f(n)|$ 收敛（由定理 11）。
- **结论**：**测度选得好，积分就退化成你熟悉的运算**——计数测度下积分 = 级数，Lebesgue 测度下积分 = 面积。这也解释了为什么「级数收敛」与「积分收敛」的许多定理长得一模一样：它们本来就是同一个定理的两个化身。

**反例（性质 (5) 中 $\mu(X)<\infty$ 不可少）** 仍在计数测度空间 $(\mathbb{N},2^{\mathbb{N}},\mu)$ 上取 $f(n)=\frac1n$。*因为* $0\leqslant f\leqslant1$，$f$ 有界且可测；但
$$\int_{\mathbb{N}}f\,\mu(\mathrm{d}x)=\sum_{n=1}^{\infty}\frac1n=+\infty ,$$
故 $f\notin L(\mathbb{N})$。**边界**：「有界 $\Rightarrow$ 可积」只在 $\mu(X)<\infty$ 时成立；$\mu(X)=\infty$ 时有界函数完全可以不可积。对照 $\mathbb{R}^n$：常数函数 $1$ 在 $[0,1]$ 上可积，在 $\mathbb{R}$ 上不可积，是同一件事。

> **这一节真正要说的是什么**：勒贝格积分的定义是「**先简单、再单调、后分解**」的三级跳；把 $m$ 换成任意测度 $\mu$，这套三级跳一字不改地照搬——**积分的本质不是「面积」，而是「用测度给水平集称重后求和」**。一旦看清这一点，$\mathbb{R}^n$、概率空间、计数空间上的积分就是同一个东西。

## 去脉（学完去哪）

- **直接服务于** [[Sec3.2 Lebesgue 积分的极限定理]]：定义只是地基，真正让勒贝格积分「好用」的是三大极限定理（Levi / Fatou / 控制收敛），它们都在下一节。
- **$L^p$ 空间**（见 Ch4）：$L^p$ 的范数 $\|f\|_p=\left(\int|f|^p\right)^{1/p}$ 就是本节的积分；$L^1$ 的完备性、Hölder 与 Minkowski 不等式都以本节的性质为原料。
- **概率论**：概率空间 $(\Omega,\mathcal{F},P)$ 就是一个测度空间（$P(\Omega)=1<\infty$），随机变量就是可测函数，**期望 $E[X]=\int_\Omega X\,\mathrm{d}P$ 就是 §3.1.4 的积分**；本节的绝对连续性正是「$P(A)\to0$ 时 $\int_A X\,\mathrm{d}P\to0$」。
- **测度论统一视角**：级数、积分、求和都是「关于某个测度的积分」——§3.1.4 的例题给出了最干净的证据。
- **注意**：本节的积分**忽略了零测集**，所以「积分相等」永远只能推出「a.e. 相等」；这个「宽容」在后面构造 $L^p$ 空间时要靠「按 a.e. 相等分等价类」来收拾（见 Ch4）。

## 防跳跃

- [ ] 振幅 $\omega(x)$ 与「$f$ 在 $x$ 连续 $\iff\omega(x)=0$」的严格证明（数学分析的内容，本节只引用）
- [ ] 达布大和/下和逼近 $f$ 时「$g_n\to f$ a.e.」的完整论证（定理 9 只给证明思路）
- [ ] 无界函数的黎曼反常积分与勒贝格积分的完整对应（定理 10 只覆盖非负情形）
- [ ] Volterra 例（有界导函数但不可黎曼可积）的构造——本节只引用结论，未给构造
- [ ] 无界函数的 $R$ 反常积分与 $L$ 积分的关系（本节只给了非负情形的定理 11）
- [ ] 抽象测度空间上「$\mu$ 可积」与「$\mu$-a.e. 有限」的充要关系（定理 11 只给了必要条件）
- [ ] $L(X,\mathcal{F},\mu)$ 在 $\mu$ 完备化之后的表现（与 Ch2 §2.1 完备化呼应）

## 来源与映射

| 本节点内容 | 来源 | 处理 |
|---|---|---|
| 三步定义的设计动机、符号约定（$\chi_A$、$f^\pm$、$L(E)$、a.e.） | 旧《Ch5 积分论》§一、§二 | 原文迁移 + 改写为节结构 |
| 非负简单函数积分定义、良定性（公共加细）、三条性质、线性定理 | 旧《Ch5 积分论》§三 | 原文迁移 |
| 狄利克雷函数算例、$\int_{[0,1]}x\,dx$ 算例 | 旧《Ch5 积分论》§三、§九 Q2 | 原文迁移（Q2 转为正文例题） |
| 非负可测函数积分定义（取上确界）、四条基础性质及其证明、单调性 | 旧《Ch5 积分论》§四 | 原文迁移 |
| 一般可测函数积分定义（积分确定 vs $L$ 可积）、七条性质、线性、绝对连续性、可数可加性 | 旧《Ch5 积分论》§五 | 原文迁移 |
| 黎曼可积 $\Rightarrow$ 勒贝格可积且值相等（定理 9）、非负反常积分（定理 10） | 旧《Ch5 积分论》§六 | 原文迁移 |
| $\sin x/x$ 边界、对比总表、$R$ 反常积分问答 | 旧《Ch5 积分论》§六、§九 Q5 | 原文迁移 |
| $1/\sqrt{x}$ 无界可积算例 | 郭版教材 §3.1.3（反常积分与积分的关系） | 新写补缺（例题） |
| Lebesgue 判据「$R$ 可积 $\iff$ a.e. 连续」的完整论证 | 旧《Ch5 积分论》§六 | 移入 [[Sec3.2 Lebesgue 积分的极限定理]] §3.2.2（该证明依赖有界收敛定理） |
| 「为什么不能直接定义 $\int f=\sum y_imA_i$」问答 | 旧《Ch5 积分论》§一 | 原文迁移（转为问答段落） |
| 抽象测度空间上的简单函数积分、非负函数积分、一般函数积分、$L(X,\mathcal{F},\mu)$、定理 3.1.19 | 郭版教材 §3.1.4（定义 3.1.16–3.1.18） | 新写补缺 |
| 抽象测度空间上的绝对连续性（定理 3.1.20） | 郭版教材 §3.1.4 | 新写补缺 |
| 计数测度例题与「有界不蕴含可积」反例 | 郭版教材 §2.1 例 7（计数测度）+ §3.1.4 | 新写补缺 |
| 「这一节真正要说的是什么」核心洞察 | 旧《Ch5 积分论》§八核心洞察 | 改写迁移 |