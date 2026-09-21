---
type: 节
formal: true
subject: 实变函数与泛函分析
created: 2026-09-21
updated: 2026-09-21
tags: [math, 实变函数与泛函分析]
chapter: 4
section: 4.3
---

# Sec4.3 卷积与 Fourier 变换

> 定位：在 $L^p$ 上引入两个最基本的线性算子——卷积（把函数"抹平"）与 Fourier 变换（把函数"换一组坐标"），并证明后者在 $L^2$ 上是保持长度不变的对称变换。
> 教材：郭懋正《实变函数与泛函分析》§4.3（p.185–208）
> 来源：**旧讲解包完全无对应内容**（本次最大补缺项）；全部据郭版教材 §4.3.1–§4.3.2 新写

> [!info] 关联笔记
> - 父级：[[Ch4 L^p 空间]]
> - 前置：[[Sec4.1 L^p 空间]] ｜ [[Sec4.2 L^2 空间]]
> - 概念：[[概念-Lp空间]] ｜ [[概念-完备性]]

---

## 来龙（为什么需要它）

- **类比已知**：$L^p$ 已经给了函数"长度"和"距离"，但那只是度量，还没有**运算**。本节要装两个运算：
  - **卷积** $f*g$ 是"加权滑动平均"——把 $g$ 当作一个"权重窗口"，让它在 $f$ 上滑动并逐点求加权平均。**它的作用是把粗糙的函数抹平**：$f$ 只有可积，$f*\varphi$ 却可以无限次可微。
  - **Fourier 变换** $\hat f$ 是"换坐标"——把函数按 $e^{it\cdot x}$ 这组"基"重新拆解，得到的 $\hat f(t)$ 是 $f$ 在频率 $t$ 上的分量。**它的作用是把微分变成乘法**：$\widehat{D^\alpha f}(t)=(it)^\alpha\hat f(t)$，于是常系数微分方程在变换后变成代数方程。

- **解决新问题**：前三章解决的是"函数能不能积分""极限能不能交换"。但真正的应用问题是**微分方程**：$P(D)u=f$ 有没有解？怎么表示？**因为** Fourier 变换把 $D$ 变成乘以 $it$、把卷积变成乘法，方程 $P(D)u=f$ 变换后成为 $\hat u=\hat f/P(it)$——形式解立刻写出。所以需要一套完整的变换理论：变换的定义域、值域、可逆性、与卷积的关系。

- **理论/应用需要**：$L^1$ 上的 Fourier 变换有严重缺陷——**它不把 $L^1$ 映到 $L^1$**（见反例 4），于是逆变换公式在 $L^1$ 上没有普适形式，且 $L^1$ 不是"自对偶的舞台"。Plancherel 定理解决了这个问题：**把 Fourier 变换延拓到 $L^2$ 上，它就成为一个一一在上的等距同构**——$L^2$ 上变换与逆变换地位完全对等，Parseval 等式保证"能量守恒"。这就是为什么信号处理、量子力学都选 $L^2$ 作舞台。

## 主体（核心内容）

### 4.3.1 卷积

#### 预备：复值函数的扩充

Fourier 变换理论在**复值**函数上讨论，因此前三章的实值结论必须扩充。若 $u,v$ 是 $E$ 上几乎处处有限的实值可测函数，则 $f=u+\mathrm{i}v$ 称为 $E$ 上的**复可测函数**，全体记作 $\mathfrak{M}(E)$（需要强调取值于复数域时记 $\mathfrak{M}_{\mathbb{C}}(E)$，一般不写下标）。当 $\int_E|f(x)|\,\mathrm{d}x<\infty$ 时称 $f$ **可积**，并定义
$$\int_E f(x)\,\mathrm{d}x=\int_E u(x)\,\mathrm{d}x+\mathrm{i}\int_E v(x)\,\mathrm{d}x.$$
复可积函数全体仍记作 $L(E)$。此时积分仍是线性的：$\int_E(\alpha f+\beta g)=\alpha\int_E f+\beta\int_E g$ 对复数 $\alpha,\beta$ 成立。

**复值积分的三角不等式**：
$$\left|\int_E f(x)\,\mathrm{d}x\right|\le\int_E|f(x)|\,\mathrm{d}x.$$
**证明**：记 $z=\int_E f$，作极分解 $z=\alpha|z|$（$|\alpha|=1$），**因为** $\operatorname{Re}[\bar\alpha f(x)]\le|\bar\alpha f(x)|=|f(x)|$，于是
$$\left|\int_E f\right|=\bar\alpha\int_E f=\int_E\bar\alpha f=\int_E\operatorname{Re}[\bar\alpha f]\le\int_E|f|. \qquad\square$$

$C(E)$、$L^p(E)$（$1\le p\le\infty$）相应扩充为复值版本，范数仍定义为
$$\|f\|_p=\left(\int_E|f(x)|^p\,\mathrm{d}x\right)^{1/p},\qquad \|f\|_\infty=\inf_{\substack{\triangle\subset E\\ m(\triangle)=0}}\sup_{x\in E\setminus\triangle}|f(x)|,$$
其中 $|f(x)|=\sqrt{u^2(x)+v^2(x)}$。**因为** 上述定义只用到 $|f|$，而 $|f|$ 仍是实值可测函数，所以 §4.1 的全部结论（Hölder 不等式、范数公理、可分性、完备性）在复值情形**逐条成立**，齐次性中的常数 $\alpha$ 可以是复数。

**复 $L^2$ 的内积必须改**：
$$(f,g)=\int_E f(x)\overline{g(x)}\,\mathrm{d}x,$$
它满足**共轭双线性**（对第一变元线性、对第二变元共轭线性）、**共轭对称** $(f,g)=\overline{(g,f)}$、**正定性** $(f,f)\ge 0$ 且 $(f,f)=0\iff f=0$，$\mathrm{a.e.}[E]$。§4.2.2 的弱收敛、正交性、Fourier 展开、标准正交基全部可移植，只是带复系数的结论要做相应调整：Bessel 不等式改为 $\sum_{k=1}^\infty|c_k|^2\le\|f\|^2$；Riesz–Fischer 定理中的实数列 $\{c_k\}$ 改为复数列且满足 $\sum|c_k|^2<\infty$；内积等式改为
$$(f,g)=\sum_{k=1}^\infty c_k\overline{d_k},\qquad c_k=(f,\varphi_k),\ d_k=(g,\varphi_k).$$

#### 卷积的定义

**定义**（郭版 (4.3.10)）：设 $f,g$ 是 $\mathbb{R}^n$ 上（实值或复值）的可测函数。若积分
$$\int_{\mathbb{R}^n}f(x-y)g(y)\,\mathrm{d}y$$
存在，就称此积分为 $f$ 与 $g$ 的**卷积**，记为 $f*g(x)$。读作"$f$ 卷 $g$"。

**注**：$f(x-y)$ 作为 $(x,y)$ 的二元函数仍是可测的，**因为** 它是可测函数 $f$ 与连续映射 $(x,y)\mapsto x-y$ 的复合。

**基本性质**：
- **对称性**：$f*g=g*f$。**因为** 在积分中作代换 $y\mapsto x-y$ 即得。
- **双线性性**：$f*g$ 关于 $f$ 与 $g$ 分别是线性的。**因为** 积分是线性的。

**定理**（Young 不等式，郭版定理 4.3.1）：若 $f\in L^p(\mathbb{R}^n)$（$1\le p\le\infty$），$g\in L^1(\mathbb{R}^n)$，则 $f*g\in L^p(\mathbb{R}^n)$，且
$$\|f*g\|_p\le\|f\|_p\|g\|_1.$$

**证明**（分两种情形，每步有"因为"）：
- **$p=\infty$**：**因为** $|f(x-y)|\le\|f\|_\infty$ 对几乎一切 $y$ 成立，
$$|f*g(x)|\le\int|f(x-y)||g(y)|\,\mathrm{d}y\le\|f\|_\infty\int|g(y)|\,\mathrm{d}y=\|f\|_\infty\|g\|_1.$$
- **$1\le p<\infty$**：把 $|g(y)|$ 拆成 $|g(y)|^{1/p}\cdot|g(y)|^{1-1/p}$，**因为** $1/p+(p-1)/p=1$，对两个因子用 Hölder 不等式：
$$|f*g(x)|\le\left(\int|f(x-y)|^p|g(y)|\,\mathrm{d}y\right)^{1/p}\left(\int|g(y)|\,\mathrm{d}y\right)^{(p-1)/p}.$$
两端作 $p$ 次乘方再对 $x$ 积分，**因为** 被积函数非负、可用 Fubini 定理交换积分次序：
$$\int|f*g(x)|^p\,\mathrm{d}x\le\|g\|_1^{p-1}\int\left(\int|f(x-y)|^p\,\mathrm{d}x\right)|g(y)|\,\mathrm{d}y=\|f\|_p^p\|g\|_1^p,$$
其中内层积分经平移代换后等于 $\|f\|_p^p$。开 $p$ 次方即得。$\square$

**特别地，$p=1$ 时卷积关于 $L^1(\mathbb{R}^n)$ 是封闭的**——两个可积函数卷起来仍可积。但 **$L^1(\mathbb{R}^n)$ 中的卷积运算没有单位元**（郭版本节习题第 19 题），见反例 1。

**引理**（平均连续性，郭版引理 4.3.2）：若 $f\in L^p(\mathbb{R}^n)$（$1\le p<\infty$），则
$$\lim_{t\to 0}\int_{\mathbb{R}^n}|f(x+t)-f(x)|^p\,\mathrm{d}x=0.$$

**证明**：任给 $\varepsilon>0$，由 §4.1.4 定理 4.1.16，**因为** $C_c(\mathbb{R}^n)$ 在 $L^p$ 中稠密，可作分解 $f=f_1+f_2$，其中 $f_1\in C_c(\mathbb{R}^n)$、$\|f_2\|_p<\varepsilon/4$。**因为** $f_1$ 具紧支集且一致连续，存在 $\delta>0$ 使 $|t|<\delta$ 时 $\int|f_1(x+t)-f_1(x)|^p\,\mathrm{d}x<(\varepsilon/2)^{1/p}$。再由 Minkowski 不等式，
$$\left(\int|f(x+t)-f(x)|^p\right)^{1/p}\le\left(\int|f_1(x+t)-f_1(x)|^p\right)^{1/p}+\left(\int|f_2(x+t)-f_2(x)|^p\right)^{1/p}<\frac\varepsilon2+2\|f_2\|_p<\varepsilon. \qquad\square$$

**读法**：$L^p$ 函数"平移一点点，整体变化就很小"。这条引理是卷积逼近定理（定理 4.3.6）的技术核心——**它说明 $L^p$ 中的元素在平移下是连续的**。

**定理**（$L^2*L^2$，郭版定理 4.3.3）：若 $f,g\in L^2(\mathbb{R}^n)$，则 $f*g(x)$ 是 $\mathbb{R}^n$ 上的**有界连续函数**，且
$$\|f*g\|_\infty\le\|f\|_2\|g\|_2.$$

**证明**：由 Schwarz 不等式，
$$\int|f(x-y)g(y)|\,\mathrm{d}y\le\left(\int|f(x-y)|^2\,\mathrm{d}y\right)^{1/2}\|g\|_2=\|f\|_2\|g\|_2,$$
**因为** 右端与 $x$ 无关，故 $f*g\in L^\infty$ 且 (4.3.14) 成立。再对连续性：**因为** 仍用 Schwarz，
$$|f*g(x+t)-f*g(x)|^2\le\|g\|_2^2\int|f(x+t-y)-f(x-y)|^2\,\mathrm{d}y=\|g\|_2^2\int|f(y-t)-f(y)|^2\,\mathrm{d}y,$$
由引理 4.3.2 右端当 $t\to 0$ 时趋于 $0$，故 $f*g\in C(\mathbb{R}^n)$。$\square$

> **对照记法**：$L^1*L^p\subseteq L^p$（Young），而 $L^2*L^2\subseteq L^\infty\cap C$。**因为** $L^2$ 的"自共轭"（$q=p=2$）使 Hölder 直接给出与 $x$ 无关的界，卷积就被"磨"成了有界连续函数——**卷积是平滑算子**，这条定理是最干净的证据。

#### 卷积的平滑作用与逼近恒等元

**多重指数与高阶可微**：由 $n$ 个非负整数构成的有序数组 $\alpha=(\alpha_1,\dots,\alpha_n)$ 称为**多重指数**；引入**多重微分算子**
$$\mathrm{D}^\alpha=\left(\frac{\partial}{\partial x_1}\right)^{\alpha_1}\cdots\left(\frac{\partial}{\partial x_n}\right)^{\alpha_n},\qquad |\alpha|=\alpha_1+\cdots+\alpha_n\ \text{（称为}\ \alpha\ \text{的次数）}.$$
$|\alpha|=0$ 时规定 $\mathrm{D}^\alpha f=f$。对开集 $\Omega$ 记
$$C^\infty(\Omega)=\{f\in C(\Omega)\mid \mathrm{D}^\alpha f\in C(\Omega),\ \forall\alpha\},\qquad C^s(\Omega)=\{f\in C(\Omega)\mid \mathrm{D}^\alpha f\in C(\Omega),\ \forall|\alpha|\le s\}.$$

**定理**（微分可穿过卷积号，郭版定理 4.3.4）：记 $B_r=\{x\in\mathbb{R}^n\mid\|x\|<r\}$。设 $g$ 满足对一切 $r>0$ 有 $g\in L(B_r)$，又 $f\in C_c^s(\mathbb{R}^n)$，则 $f*g\in C^s(\mathbb{R}^n)$，且
$$\mathrm{D}^\alpha(f*g)=\mathrm{D}^\alpha f*g,\qquad|\alpha|\le s.$$

**证明**：卷积 $f*g$ 显然存在。**因为** $f$ 具紧支集，积分实际上在紧集上进行，而 $f$ 有直到 $s$ 阶的连续偏导，可应用第三章"积分号下取微商"定理（定理 3.2.7）相继 $s$ 次。$\square$

**这条定理是"卷积 = 平滑"的全部秘密**：**因为** 微商落在 $f$ 上而不落在 $g$ 上，只要把 $f$ 换成光滑的 $\varphi$，$f$ 再粗糙（哪怕只是 $L^p$），$\varphi*f$ 也自动是光滑的。

**定义**（逼近恒等元，郭版定义 4.3.5）：设 $\varphi$ 定义在 $\mathbb{R}^n$ 上，对任意 $\varepsilon>0$ 记
$$\varphi_\varepsilon(x)=\varepsilon^{-n}\varphi\left(\frac{x}{\varepsilon}\right).$$
（**读法**：$\varphi_\varepsilon$ 是把 $\varphi$ 沿各方向压缩 $\varepsilon$ 倍、再把高度放大 $\varepsilon^{-n}$ 倍——**总积分保持不变**，所以 $\|\varphi_\varepsilon\|_1=\|\varphi\|_1$。当 $\varepsilon\to 0$ 时它越来越"尖"。）

**定理**（逼近恒等元定理，郭版定理 4.3.6）：设 $\varphi\in L^1(\mathbb{R}^n)$ 且 $\|\varphi\|_1=1$。若 $f\in L^p(\mathbb{R}^n)$（$1\le p<\infty$），则
$$\lim_{\varepsilon\to 0}\|\varphi_\varepsilon*f-f\|_p=0.$$

**证明**（骨架，每步有"因为"）：
1. **因为** 作变量代换 $y\mapsto\varepsilon y$ 并用 $\|\varphi\|_1=1$，
$$\varphi_\varepsilon*f(x)=\int f(x-y)\varphi_\varepsilon(y)\,\mathrm{d}y=\int f(x-\varepsilon y)\varphi(y)\,\mathrm{d}y,$$
故 $\varphi_\varepsilon*f(x)-f(x)=\int[f(x-\varepsilon y)-f(x)]\varphi(y)\,\mathrm{d}y$。
2. 把 $|\varphi(y)|$ 拆成 $|\varphi(y)|^{1/p}\cdot|\varphi(y)|^{1/q}$（$q$ 为 $p$ 的共轭指数），**因为** Hölder 不等式，
$$|\varphi_\varepsilon*f(x)-f(x)|\le\left[\int|f(x-\varepsilon y)-f(x)|^p|\varphi(y)|\,\mathrm{d}y\right]^{1/p}.$$
3. 两端作 $p$ 次乘方再对 $x$ 积分，**因为** 被积函数非负、可用 Fubini 定理交换次序，
$$\int|\varphi_\varepsilon*f(x)-f(x)|^p\,\mathrm{d}x\le\int|\varphi(y)|\left\{\int|f(x-\varepsilon y)-f(x)|^p\,\mathrm{d}x\right\}\mathrm{d}y.$$
4. 令 $\varepsilon\to 0$。**因为** 内层积分被 $2^p\|f\|_p^p$ 一致控制、且 $\varphi\in L^1$，由控制收敛定理可在积分号下取极限；再**因为** 平均连续性（引理 4.3.2）内层极限为 $0$，故整个右端趋于 $0$。$\square$

**读法**：$L^1(\mathbb{R}^n)$ 中的卷积虽无单位元，但 $\varphi_\varepsilon*f\xrightarrow{L^p}f$——所以 $\varphi_\varepsilon$ 称为卷积运算的**渐近单位元**（或"逼近恒等元"）。

**例 1（滑动平均）**：取 $\varphi=\chi_{[-1,1]}$，则 $\varphi_\varepsilon(x)=\dfrac1\varepsilon\chi_{[-\varepsilon,\varepsilon]}(x)$。对任给 $f\in L^p(\mathbb{R})$，
$$\varphi_\varepsilon*f(x)=\frac1\varepsilon\int_{x-\varepsilon}^{x+\varepsilon}f(y)\,\mathrm{d}y\ \stackrel{\text{def}}{=}\ f_\varepsilon(x).$$
由 Young 不等式 $\|f_\varepsilon\|_p\le\|f\|_p$（**因为** $\|\varphi_\varepsilon\|_1=1$）；由定理 4.3.6，$f_\varepsilon\xrightarrow{L^p}f$。**几何意义**：$f_\varepsilon(x)$ 就是 $f$ 在以 $x$ 为中心、长 $2\varepsilon$ 的区间上的平均值——**卷积就是滑动平均**。

**例 2（$C_c^\infty$ 稠密，郭版定理 4.3.10）**：在 $(0,1)$ 上定义 $\varphi(x)=\left[1+\exp\left(\frac1{1-x}-\frac1x\right)\right]^{-1}$，再令 $\varphi(0)=0$、$\varphi(x)=0$（$x\ge 1$）、$\varphi(x)=\varphi(-x)$（$x<0$）。可证明 $\varphi\in C_c^\infty(\mathbb{R})$。记 $\varphi_n(x)=n\varphi(nx)/\|\varphi\|_1$，对 $f\in L^p(\mathbb{R})$（$1\le p<\infty$）令 $f_n=\varphi_n*f$，则由定理 4.3.4 得 $f_n\in C^\infty(\mathbb{R})$、由定理 4.3.6 得 $f_n\xrightarrow{L^p}f$。**结论**：每个 $f\in L^p(\mathbb{R})$ 可用**无限次可微**函数 $L^p$ 逼近，即 $C_c^\infty(\mathbb{R})$ 在 $L^p(\mathbb{R})$ 中稠密。

> 【原书插图】图 4.1：光滑截断函数 $\varphi$ 的图像（在 $(-1,1)$ 内为正、外侧恒为零，$C^\infty$ 光滑）

**例 3（Gauss 核 ⇒ 多项式稠密）**：取
$$W(x)=\frac{1}{\sqrt{2\pi}}\mathrm{e}^{-\frac12x^2},\qquad W_n(x)=nW(nx).$$
则 $\|W_n\|_1=1$ 对一切 $n$ 成立，且对任意 $\delta>0$，$\lim_{n\to\infty}\int_{-\delta}^{\delta}W_n(x)\,\mathrm{d}x=1$（**因为** 代换 $t=nx$ 后积分化为标准正态的分布函数值）。取 $-\infty<a<\alpha<\beta<b<\infty$，记 $\Delta=(\alpha,\beta)$、$f=\chi_\Delta$、$f_n=W_n*f$，则
$$f_n(x)=\frac{n}{\sqrt{2\pi}}\int_\alpha^\beta \mathrm{e}^{-\frac12 n^2(x-y)^2}\,\mathrm{d}y=\frac{1}{\sqrt{2\pi}}\sum_{k=0}^\infty\frac{(-1)^k n^{2k+1}}{2^kk!(2k+1)}P_{2k}(x),$$
其中 $P_{2k}(x)=(x-\alpha)^{2k+1}-(x-\beta)^{2k+1}$ 是 $2k$ 次多项式（**因为** 把指数函数展成幂级数后逐项积分）。**因为** $f_n\xrightarrow{L^p}f$，而在 $[a,b]$ 上 $f_n$ 可用该级数的部分和一致逼近，故 $\chi_\Delta$ 在 $[a,b]$ 上可用**多项式** $L^p$ 逼近。结合简单函数逼近（定理 4.1.15）得：**区间 $[a,b]$ 上的全体多项式是 $L^p[a,b]$ 的稠密线性子空间**。

**反例 1（$L^1$ 中卷积无单位元）**：不存在 $e\in L^1(\mathbb{R}^n)$ 使 $e*f=f$ 对一切 $f\in L^1(\mathbb{R}^n)$ 成立。

**证明**：反设存在这样的 $e$。取 $f\in L^1\cap L^2$ 且 $\hat f\not\equiv 0$（例如 $f=\chi_{[-1,1]}$）。由引理 4.3.8(3)，卷积的变换等于变换的乘积：$\hat e\cdot\hat f=\hat f$，**因为** 存在 $t$ 使 $\hat f(t)\ne 0$，在该点得 $\hat e(t)=1$。**因为** 上式对一切 $f$ 成立，可以选取一族 $f$ 迫使 $\hat e\equiv 1$；但由定理 4.3.12（Riemann–Lebesgue 引理），**因为** $e\in L^1$，$\hat e\in C_0(\mathbb{R}^n)$，即 $|t|\to\infty$ 时 $\hat e(t)\to 0$，与 $\hat e\equiv 1$ 矛盾。$\square$

**这条反例说明**：逼近恒等元 $\varphi_\varepsilon$ 只能做到"$\varphi_\varepsilon*f\to f$"，**做不到"$\varphi_\varepsilon*f=f$"**。$\varphi_\varepsilon$ 在 $L^1$ 中不收敛（$\|\varphi_\varepsilon\|_1=1$ 而它越来越尖，弱收敛到 Dirac 测度），所以极限对象根本不在 $L^1$ 里——**这正是必须引入广义函数（分布）理论的原因**。

**反例 2（$\varphi$ 只是 $L^1$ 时只能保证连续，不能保证可微）**：取 $f=\chi_{[0,1]}$、$\varphi=\chi_{[-1,1]}$，由例 1，
$$f_\varepsilon(x)=\frac1\varepsilon\int_{x-\varepsilon}^{x+\varepsilon}\chi_{[0,1]}(y)\,\mathrm{d}y.$$
当 $0<\varepsilon<1/2$ 时，在 $x\in(-\varepsilon,\varepsilon)$ 上 $f_\varepsilon(x)=\dfrac{x+\varepsilon}{\varepsilon}$，在 $x\in(1-\varepsilon,1+\varepsilon)$ 上 $f_\varepsilon(x)=\dfrac{1+\varepsilon-x}{\varepsilon}$，其余处为常数 $0$ 或 $1$。于是 $f_\varepsilon$ 在 $x=\pm\varepsilon$ 与 $x=1\pm\varepsilon$ 处有**角点**，**不可微**。**结论**：定理 4.3.4 要求 $\varphi\in C_c^s$，条件不可少——**因为** 微商要能"穿过"卷积号落到 $\varphi$ 上，$\varphi$ 本身必须足够光滑；$\varphi$ 只有 $L^1$ 时定理 4.3.4 不适用，$f_\varepsilon$ 只连续而不光滑。

**例题**：计算 $f*g$，其中 $f=g=\chi_{[0,1]}$，并用 Young 不等式核对。

- **原始信息**：$f,g\in L^1(\mathbb{R})\cap L^\infty(\mathbb{R})$，$\|f\|_1=\|g\|_1=1$，$\|f\|_2=\|g\|_2=1$。
- **代入**：按定义
$$f*g(x)=\int_{\mathbb{R}}\chi_{[0,1]}(x-y)\chi_{[0,1]}(y)\,\mathrm{d}y.$$
被积函数非零当且仅当 $y\in[0,1]$ **且** $x-y\in[0,1]$，即 $y\in[x-1,x]\cap[0,1]$，这是一个长度随 $x$ 变化的区间。
- **计算**：分三段讨论交集长度：
  - $x\le 0$ 或 $x\ge 2$：交集为空，$f*g(x)=0$；
  - $0<x<1$：交集为 $[0,x]$，长度 $x$，故 $f*g(x)=x$；
  - $1\le x<2$：交集为 $[x-1,1]$，长度 $2-x$，故 $f*g(x)=2-x$。
  即 $f*g$ 是以 $(1,1)$ 为顶点的**三角形函数**（常记作 $\Lambda$）。
- **核对 Young 不等式**：$\|f*g\|_1=\int_0^1 x\,\mathrm{d}x+\int_1^2(2-x)\,\mathrm{d}x=\frac12+\frac12=1$，而 $\|f\|_1\|g\|_1=1$，故 $\|f*g\|_1=\|f\|_1\|g\|_1=1$，不等式取等号。又 $\|f*g\|_\infty=1=\|f\|_2\|g\|_2$，定理 4.3.3 的估计也取等号。
- **结论**：两个**不连续**的指示函数卷起来得到一个**连续**的三角形函数——这是"卷积 = 平滑"最直观的例子。再卷一次 $\chi_{[0,1]}$ 会得到 $C^1$ 的分段二次函数，光滑度逐次递增。**注意**：$f*g$ 在 $x=0,1,2$ 处仍不可微（角点），与反例 2 的机制一致——**因为** $\chi_{[0,1]}$ 本身不光滑，定理 4.3.4 不适用。

### 4.3.2 $L^2(\mathbb{R}^n)$ 上的 Fourier 变换

**定义**（Fourier 变换，郭版定义 4.3.7）：对任意 $f\in L(\mathbb{R}^n)$（即 $L^1$），令
$$\hat f(t)=\frac{1}{(2\pi)^{n/2}}\int_{\mathbb{R}^n}f(x)\mathrm{e}^{-\mathrm{i}t\cdot x}\,\mathrm{d}x,\qquad t\cdot x=\sum_{i=1}^n t_ix_i,$$
称 $\hat f$ 是 $f$ 的 **Fourier 变换**（$\hat f$ 读作"$f$ 的帽"）。有时记 $\mathcal{F}:f\mapsto\hat f$，于是 $\mathcal{F}f=\hat f$。$\mathcal{F}$ 是**线性映射**：$\mathcal{F}(\alpha f_1+\beta f_2)=\alpha\mathcal{F}f_1+\beta\mathcal{F}f_2$。

**读法**：变量 $t$ 称为变量 $x$ 的**对偶变量**（物理上 $x$ 是位置/时间，$t$ 是频率）。当 $f$ 是实值函数时 $\hat f$ 是复值函数。引入记号 $e_t(x)\stackrel{\text{def}}{=}\mathrm{e}^{\mathrm{i}t\cdot x}$，则
$$\hat f(t)=f*e_{-t}(0)=\int_{\mathbb{R}^n}f(x)e_{-t}(x)\,\mathrm{d}x,$$
**这说明 Fourier 变换与卷积是同一件事的两个侧面**——$\hat f(t)$ 就是 $f$ 与"频率 $t$ 的纯波"的卷积在原点处的值。

**基本估计**：**因为** $|e_t(x)|=1$ 且 $|f(x)e_{-t}(x)|\le|f(x)|$，
$$|\hat f(t)|\le\frac{1}{(2\pi)^{n/2}}\|f\|_1,$$
且在积分号下取极限可知 $\hat f$ 是 $t$ 的**连续**函数。于是 **$f\in L^1$ 时 $\hat f$ 是有界连续函数**。

**微分记号**：对多重指数 $\alpha$ 记
$$\mathrm{D}_\alpha=\mathrm{i}^{-|\alpha|}\mathrm{D}^\alpha=\left(\frac1{\mathrm{i}}\frac{\partial}{\partial x_1}\right)^{\alpha_1}\cdots\left(\frac1{\mathrm{i}}\frac{\partial}{\partial x_n}\right)^{\alpha_n},$$
则 $\mathrm{D}_\alpha e_t=t^\alpha e_t$（$t^\alpha=t_1^{\alpha_1}\cdots t_n^{\alpha_n}$）。对复多项式 $P(\xi)=\sum c_\alpha\xi^\alpha$，记 $P(\mathrm{D})=\sum c_\alpha\mathrm{D}_\alpha$、$P(-\mathrm{D})=\sum(-1)^{|\alpha|}c_\alpha\mathrm{D}_\alpha$，则
$$P(\mathrm{D})e_t=P(t)e_t.$$
**这条式子就是"Fourier 变换把微分变成乘法"的代数根源**：$e_t$ 是 $P(\mathrm{D})$ 的特征函数，特征值是 $P(t)$。

**平移算子**：对 $x,y\in\mathbb{R}^n$ 记 $\tau_xf(y)=f(y-x)$。

**引理**（Fourier 变换的四条基本性质，郭版引理 4.3.8）：设 $f,g\in L^1(\mathbb{R}^n)$，$x\in\mathbb{R}^n$，则
1. $(\tau_xf)^\wedge=e_{-x}\hat f$（**平移变调制**）；
2. $(e_xf)^\wedge=\tau_x\hat f$（**调制变平移**）；
3. $(f*g)^\wedge=\hat f\hat g$（**卷积变乘法**）；
4. 若 $\lambda>0$、$h(x)=f(x/\lambda)$，则 $\hat h(t)=\lambda^n\hat f(\lambda t)$（**伸缩变反伸缩**）。

**证明**：(1) 作代换 $u=y-x$，
$$(\tau_xf)^\wedge(t)=\frac{1}{(2\pi)^{n/2}}\int f(y-x)\mathrm{e}^{-\mathrm{i}t\cdot y}\,\mathrm{d}y=\frac{1}{(2\pi)^{n/2}}\int f(u)\mathrm{e}^{-\mathrm{i}t\cdot(u+x)}\,\mathrm{d}u=\mathrm{e}^{-\mathrm{i}t\cdot x}\hat f(t).$$
(2) 直接计算：
$$(e_xf)^\wedge(t)=\frac{1}{(2\pi)^{n/2}}\int f(y)\mathrm{e}^{-\mathrm{i}(t-x)\cdot y}\,\mathrm{d}y=\hat f(t-x)=(\tau_x\hat f)(t).$$
(3) **因为** 被积函数绝对可积，由 Fubini 定理交换积分次序即得。(4) 由变量线性变换得出。$\square$

> **性质 (3) 是全节最有用的公式**：它把"卷积这个难算的运算"变成"逐点相乘这个易算的运算"。定理 4.3.14 会把它反过来用：乘积的变换是变换的卷积。

**定义**（速降函数，郭版定义 4.3.9）：若 $f\in C^\infty(\mathbb{R}^n)$ 且对一切 $N=0,1,2,\dots$，
$$\sup_{|\alpha|\le N}\ \sup_{x\in\mathbb{R}^n}(1+|x|^2)^N|\mathrm{D}^\alpha f(x)|<\infty,$$
称 $f$ 为**速降函数**，$\mathbb{R}^n$ 上速降函数全体记作 $S(\mathbb{R}^n)$（也称 Schwartz 空间）。

**读法**：速降函数是"任意次可微、且任意阶导数都比任意多项式的倒数衰减得更快"的函数。**等价刻画**：$f\in S(\mathbb{R}^n)\iff$ 对任意多重指数 $\alpha$ 与任意多项式 $P$，$P\cdot\mathrm{D}^\alpha f$ 在 $\mathbb{R}^n$ 上有界；**因为** 可用 $(1+|x|^2)^NP$ 代替 $P$，这也等价于 $P\cdot\mathrm{D}^\alpha f\in L^1(\mathbb{R}^n)$。

**命题**（郭版命题 4.3.11）：速降函数空间具有以下性质：
1. 若 $f\in S(\mathbb{R}^n)$，则对任意多项式 $P$、多重指数 $\alpha$ 与任意 $g\in S(\mathbb{R}^n)$，仍有 $P\cdot f$、$g\cdot f$、$\mathrm{D}_\alpha f\in S(\mathbb{R}^n)$；
2. $(P(\mathrm{D})f)^\wedge=P\cdot\hat f$，$(P\cdot f)^\wedge=P(-\mathrm{D})\hat f$；
3. $\hat f\in S(\mathbb{R}^n)$。

**证明要点**：(1) **因为** 求导不改变速降性、且莱布尼兹法则下多项式乘法保持速降性。(2) 第一式由 $P(\mathrm{D})e_t=P(t)e_t$ 出发，**因为** $P(\mathrm{D})$ 是线性算子且可与卷积交换，
$$(P(\mathrm{D})f)*e_t=f*(P(\mathrm{D})e_t)=f*(P(t)e_t)=P(t)(f*e_t),$$
两边在原点取值即得。第二式对一维情形用差商与中值估计：**因为** $x_1f\in L^1$，由控制收敛定理
$$-\frac1{\mathrm{i}}\frac{\partial}{\partial t_1}\hat f(t)=\frac{1}{(2\pi)^{n/2}}\int x_1f(x)\mathrm{e}^{-\mathrm{i}x\cdot t}\,\mathrm{d}x,$$
一般情形重复运用即可。(3) 取 $g(x)=(-1)^{|\alpha|}x^\alpha f(x)\in S$，由 (2) 得 $\hat g=\mathrm{D}_\alpha\hat f$；**因为** $P(\mathrm{D})g\in L^1$ 蕴含 $(P(\mathrm{D})g)^\wedge$ 有界，故 $P\cdot\mathrm{D}_\alpha\hat f$ 对一切 $P,\alpha$ 有界，即 $\hat f\in S$。$\square$

**命题 (3) 的意义**：**Fourier 变换把 $S(\mathbb{R}^n)$ 映到自身**——$S$ 是变换的"天然定义域"，在其中变换的所有运算（求导、乘多项式、反演）都自由可用。这就是为什么逆定理（定理 4.3.13）必须先在 $S$ 上证明。

**定理**（Riemann–Lebesgue 引理，郭版定理 4.3.12）：若 $f\in L^1(\mathbb{R}^n)$，则 $\hat f\in C_0(\mathbb{R}^n)$（**读法**：$C_0$ 表示"在无穷远处趋于零的连续函数"），并且
$$\|\hat f\|_\infty\le\frac{1}{(2\pi)^{n/2}}\|f\|_1.$$

**证明**：**因为** $S(\mathbb{R}^n)$ 在 $L^1(\mathbb{R}^n)$ 中稠密，存在 $f_j\in S$ 使 $\|f-f_j\|_1\to 0$。**因为** $\hat f_j\in S\subseteq C_0$，且由 (4.3.26) 式 $|\hat f(t)-\hat f_j(t)|\le(2\pi)^{-n/2}\|f-f_j\|_1$，故 $\hat f_j$ 在 $\mathbb{R}^n$ 上**一致**收敛到 $\hat f$。一致收敛保持连续性与"无穷远处趋于零"，故 $\hat f\in C_0$。$\square$

**Gauss 函数与自对偶**：考虑 Gauss 密度
$$G(x)=\exp\left(-\frac12|x|^2\right),$$
则 $G\in S(\mathbb{R}^n)$，**$\hat G=G$**（称 $G$ 是 Fourier 变换的**自对偶**函数），且
$$G(0)=\frac{1}{(2\pi)^{n/2}}\int_{\mathbb{R}^n}\hat G(t)\,\mathrm{d}t.$$
**证明思路**：**因为** $G$ 可分离变量，$G(x)=\prod_{j=1}^nG_j(x_j)$（$G_j(x_j)=\mathrm{e}^{-x_j^2/2}$），只需处理一元情形。**因为** $G_1$ 是一阶常微分方程 $y'+x_1y=0$ 的解，而由命题 4.3.11(2) 知 $\hat G_1$ 也满足同一方程，故 $\hat G_1/G_1$ 为常数；由 $\hat G_1(0)=\frac{1}{\sqrt{2\pi}}\int_{\mathbb{R}}\mathrm{e}^{-x_1^2/2}\,\mathrm{d}x_1=1$ 得 $\hat G_1=G_1$。逐分量相乘得 $\hat G=G$。再把 $\hat G=G$ 代入 $\hat G(0)$ 的定义即得 (4.3.35)。$\square$

**定理**（Fourier 逆定理，郭版定理 4.3.13）：
1. 若 $g\in S(\mathbb{R}^n)$，则
$$g(x)=\frac{1}{(2\pi)^{n/2}}\int_{\mathbb{R}^n}\hat g(t)\mathrm{e}^{\mathrm{i}x\cdot t}\,\mathrm{d}t;$$
2. Fourier 变换 $\mathcal{F}:S(\mathbb{R}^n)\to S(\mathbb{R}^n)$ 是**一一在上**的线性映射，而且 $\mathcal{F}^4=I$（$I$ 是恒等映射）；
3. 若 $f\in L^1(\mathbb{R}^n)$ **且** $\hat f\in L^1(\mathbb{R}^n)$，令 $f_0(x)=\frac{1}{(2\pi)^{n/2}}\int\hat f(t)\mathrm{e}^{\mathrm{i}x\cdot t}\,\mathrm{d}t$，则 $f(x)=f_0(x)$，$\mathrm{a.e.}[\mathbb{R}^n]$。

**证明脉络**：
- **先证对偶关系 (4.3.37)**：若 $f,g\in L^1(\mathbb{R}^n)$，**因为** 二重积分绝对可积，由 Fubini 定理
$$\int_{\mathbb{R}^n}\hat f(y)g(y)\,\mathrm{d}y=\int_{\mathbb{R}^n}f(t)\hat g(t)\,\mathrm{d}t.$$
- **(1)**：在 (4.3.37) 中取 $f(t)=G(t/\lambda)$（$\lambda>0$），利用引理 4.3.8(4) 得 $\int g(y/\lambda)\hat G(y)\,\mathrm{d}y=\int G(t/\lambda)\hat g(t)\,\mathrm{d}t$。令 $\lambda\to\infty$，**因为** $g(y/\lambda)\to g(0)$、$G(t/\lambda)\to G(0)=1$，由控制收敛定理得 $g(0)\int\hat G=\int\hat g$，再由 (4.3.35) 得 $g(0)=\frac{1}{(2\pi)^{n/2}}\int\hat g(t)\,\mathrm{d}t$。最后**因为** 可用引理 4.3.8(1)，$g(x)=(\tau_{-x}g)(0)=\frac{1}{(2\pi)^{n/2}}\int(\tau_{-x}g)^\wedge(t)\,\mathrm{d}t=\frac{1}{(2\pi)^{n/2}}\int\hat g(t)\mathrm{e}^{\mathrm{i}x\cdot t}\,\mathrm{d}t$。
- **(2)**：由 (1)，**因为** $\hat g=0$ 蕴含 $g=0$，$\mathcal{F}$ 在 $S$ 上单射。又 (4.3.36) 可写成 $\mathcal{F}\hat g(x)=g(-x)$；记 $\check g(x)=g(-x)$ 则 $\mathcal{F}^2g=\check g$，于是 $\mathcal{F}^4g=g$，**因为** 逆映射 $\mathcal{F}^3$ 存在，$\mathcal{F}$ 是满射。
- **(3)**：对任意 $g\in S$ 计算 $\int f_0(x)\hat g(x)\,\mathrm{d}x$，交换积分次序并两次用 (4.3.37) 得它等于 $\int f(x)\hat g(x)\,\mathrm{d}x$。**因为** 由 (2) 知 $\hat g$ 可取遍 $S(\mathbb{R}^n)$，故对一切 $\phi\in C_c^\infty$ 有 $\int(f_0-f)\phi=0$，于是 $f_0=f$，$\mathrm{a.e.}$。$\square$

**定理**（郭版定理 4.3.14）：设 $f,g\in S(\mathbb{R}^n)$，则
1. $f*g\in S(\mathbb{R}^n)$；
2. $(fg)^\wedge=\hat f*\hat g$（**乘积变卷积**——与引理 4.3.8(3) 对偶）。

**证明**：由引理 4.3.8(3)，$\mathcal{F}(f*g)=\mathcal{F}(f)\mathcal{F}(g)$。把 $f,g$ 换成 $\hat f,\hat g$ 并用 $\mathcal{F}^2h=\check h$，
$$\mathcal{F}(\hat f*\hat g)=\mathcal{F}^2(f)\cdot\mathcal{F}^2(g)=\check f\check g=(fg)^\vee=\mathcal{F}^2(fg).$$
两边作用 $\mathcal{F}^3$ 即得 (2)。再由 (2)：**因为** $fg\in S$，故 $\hat f*\hat g\in S$；又**因为** $\mathcal{F}$ 是 $S$ 上的满射，用 $f,g$ 代替 $\hat f,\hat g$ 即得 $f*g\in S$。$\square$

**定理**（Plancherel 定理，郭版定理 4.3.15）：存在 $L^2(\mathbb{R}^n)$ 到自身的一个**一一在上**线性映射 $\Psi$，它满足
$$\Psi f=\hat f,\quad\forall f\in S(\mathbb{R}^n);\qquad \|\Psi f\|_2=\|f\|_2,\quad\forall f\in L^2(\mathbb{R}^n).$$
即：**Fourier 变换可以延拓成 $L^2(\mathbb{R}^n)$ 上的等距同构**。

**证明**（四步，每步有"因为"）：
1. **先在 $S$ 上建立 Parseval 等式**。若 $f,g\in S(\mathbb{R}^n)$，由逆定理 (4.3.36) 把 $f$ 用 $\hat f$ 表示后代入 $\int f\bar g$，**因为** 被积函数绝对可积、可交换积分次序，
$$\int_{\mathbb{R}^n}f(x)\overline{g(x)}\,\mathrm{d}x=\int_{\mathbb{R}^n}\hat f(t)\overline{\hat g(t)}\,\mathrm{d}t.$$
2. **取 $g=f$ 得等距性**：$\|\hat f\|_2=\|f\|_2$ 对一切 $f\in S(\mathbb{R}^n)$ 成立。于是 $\mathcal{F}$ 是 $S(\mathbb{R}^n)$ 到自身的 **$L^2$ 模等距映射**。
3. **用稠密性延拓**。设 $f\in L^2(\mathbb{R}^n)$。**因为** $S(\mathbb{R}^n)$ 在 $L^2$ 中稠密，存在 $g_j\in S$ 使 $g_j\xrightarrow{L^2}f$。**因为** 等距性，$\{\hat g_j\}$ 是 $L^2$ 中的**基本列**（$\|\hat g_j-\hat g_k\|_2=\|g_j-g_k\|_2\to 0$）；**因为** $L^2$ 完备（§4.1.3），它收敛。记极限为 $\Psi f$。
4. **验证良定义与等距**。若另有 $h_j\in S$ 使 $h_j\xrightarrow{L^2}f$，**因为** $g_j-h_j\xrightarrow{L^2}0$ 且等距，$\hat g_j-\hat h_j\xrightarrow{L^2}0$，故 $\Psi f$ 不依赖逼近列的选取，$\Psi$ 是良定义的线性映射。再由 $\|\Psi f\|_2=\lim_j\|\hat g_j\|_2=\lim_j\|g_j\|_2=\|f\|_2$ 得等距性。最后**因为** $S$ 在 $L^2$ 中稠密、且 $\Psi$ 在 $S$ 上就是 $\mathcal{F}$，等距线性映射必是单射，稠密性把单射升级为满射。$\square$

**Plancherel 变换 $\Psi$ 的代数性质**（对一切 $f\in L^2(\mathbb{R}^n)$）：
$$\Psi^2f=\check f\ (\text{即}\ \check f(x)=f(-x)),\qquad \Psi^4f=f,\qquad \Psi^3=\Psi^{-1},$$
$$(\Psi f,\Psi g)=(f,g)=(\Psi^{-1}f,\Psi^{-1}g),\qquad (f,\Psi g)=(\Psi^{-1}f,g),$$
$$\int(\Psi f)(x)g(x)\,\mathrm{d}x=\int f(x)(\Psi g)(x)\,\mathrm{d}x.$$
**读法**：$\Psi$ 是**周期为 4 的等距同构**——做两次变换得到"镜像"，做四次回到原处。在量子力学中，$\Psi$ 对应"位置表象 ↔ 动量表象"的切换，$\Psi^2$ 对应宇称算子。

**Parseval 等式**（$L^2$ 形式，郭版 (4.3.40)）：
$$\int_{\mathbb{R}^n}f(x)\overline{g(x)}\,\mathrm{d}x=\int_{\mathbb{R}^n}\hat f(t)\overline{\hat g(t)}\,\mathrm{d}t.$$
取 $g=f$ 即"**能量守恒**"：$\|\hat f\|_2=\|f\|_2$。

**反例 3（$L^2$ 上的变换与 $L^1$ 上的变换是两回事）**：取 $f=\chi_{[-1,1]}\in L^1(\mathbb{R})\cap L^2(\mathbb{R})$，则
$$\hat f(t)=\frac{1}{\sqrt{2\pi}}\int_{-1}^1\mathrm{e}^{-\mathrm{i}tx}\,\mathrm{d}x=\frac{1}{\sqrt{2\pi}}\cdot\frac{2\sin t}{t}.$$
**因为** $\int_{\mathbb{R}}|\sin t/t|\,\mathrm{d}t=+\infty$（这是经典反常积分结论），$\hat f\notin L^1(\mathbb{R})$。于是：
- 逆定理 (4.3.36) **不能**直接用于 $f$——**因为** 定理 4.3.13(1) 要求 $g\in S$、(3) 要求 $\hat f\in L^1$，两条都不满足；
- 但 Plancherel 定理**照样**成立：$\Psi f=\hat f$ 是 $L^2$ 元素，$\|\Psi f\|_2=\|f\|_2=\sqrt2$，且 $\Psi^{-1}\hat f=f$ 在 $L^2$ 意义下成立。

**结论**：$L^2$ 上的 Fourier 变换（$\Psi$）不是 $L^1$ 上的 Fourier 变换（$\mathcal{F}$）的简单限制——它是**用稠密性 + 等距性延拓出来的新算子**。这正是 Plancherel 定理的价值所在：**在 $L^2$ 上，变换与逆变换地位对等，而在 $L^1$ 上不是**。

**反例 4（$L^1$ 上的 Fourier 变换不是满射）**：由定理 4.3.12，$f\in L^1$ 时 $\hat f\in C_0$。但**反向不成立**：$C_0$ 中并非每个函数都是某个 $L^1$ 函数的 Fourier 变换（**因为** 若 $\hat f=\hat g$ 则 $f=g$，值域远小于 $C_0$；这一事实的完整证明属于 Fourier 分析的进一步内容，郭版未展开）。**结论**：$\mathcal{F}:L^1\to C_0$ 是单射但**不是满射**，因此 $L^1$ 上不存在"逆变换算子"（这也是反例 3 的深层原因）。完整刻画 $\mathcal{F}(L^1)$ 的问题见本节「防跳跃」。

**例题**：用 Plancherel 定理计算 $\displaystyle\int_{-\infty}^{\infty}\frac{\sin^2 u}{u^2}\,\mathrm{d}u$。

- **原始信息**：直接求这个反常积分需要复变函数或繁琐的实变技巧；改用 $L^2$ 的 Fourier 变换可以一步得到。
- **代入**：取 $f=\chi_{[-a,a]}$（$a>0$）。**因为** $f\in L^1\cap L^2$，先算 $\hat f$：
$$\hat f(t)=\frac{1}{\sqrt{2\pi}}\int_{-a}^{a}\mathrm{e}^{-\mathrm{i}tx}\,\mathrm{d}x=\frac{1}{\sqrt{2\pi}}\cdot\frac{2\sin(at)}{t}.$$
- **计算**：由 Plancherel 定理 $\|\hat f\|_2^2=\|f\|_2^2$，而
$$\|f\|_2^2=\int_{-a}^{a}1\,\mathrm{d}x=2a,\qquad \|\hat f\|_2^2=\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{4\sin^2(at)}{t^2}\,\mathrm{d}t=\frac{2}{\pi}\int_{-\infty}^{\infty}\frac{\sin^2(at)}{t^2}\,\mathrm{d}t.$$
令二者相等：$\dfrac{2}{\pi}\displaystyle\int_{-\infty}^{\infty}\frac{\sin^2(at)}{t^2}\,\mathrm{d}t=2a$，即 $\displaystyle\int_{-\infty}^{\infty}\frac{\sin^2(at)}{t^2}\,\mathrm{d}t=\pi a$。
- **结果**：作代换 $u=at$（$a>0$）得 $\displaystyle\int_{-\infty}^{\infty}\frac{\sin^2u}{u^2}\,\mathrm{d}u=\pi$。特别地取 $a=1$ 直接得到 $\displaystyle\int_{-\infty}^{\infty}\frac{\sin^2u}{u^2}\,\mathrm{d}u=\pi$。
- **结论**：**Plancherel 定理把"算积分"变成了"算函数本身的 $L^2$ 范数"**。这不是技巧，而是结构性事实——$\hat f$ 的能量就是 $f$ 的能量，所以只要 $f$ 的范数好算，$\hat f$ 的积分就自动得到。这与 §4.2 中"用 Parseval 等式求 $\sum 1/n^2=\pi^2/6$"是**同一原理**的连续版本：那里是离散正交基上的能量守恒，这里是连续群上的能量守恒。

**本节收束**：卷积与 Fourier 变换是 $L^p$ 上两个互补的算子——**卷积在"空间侧"把函数抹平（$L^2*L^2\to C\cap L^\infty$，$L^1*L^p\to L^p$），Fourier 变换在"频率侧"把卷积变成乘法**（引理 4.3.8(3)）。二者的对偶关系由 Plancherel 定理收束：在 $L^2$ 上 Fourier 变换是等距同构，Parseval 等式保证能量守恒，$\Psi^4=I$ 保证变换可逆。**这一节真正要说的是：$L^2$ 上的 Fourier 变换不是"算积分的技术"，而是一个几何对象——它是 $L^2$ 到自身的保长对称变换。**

## 去脉（学完去哪）

- **当代应用**：
  - **微分方程**：常系数方程 $P(D)u=f$ 经 Fourier 变换化为代数方程 $\hat u=\hat f/P(it)$，形式解立刻得到；椭圆正则性理论中"$u$ 的光滑性由 $\hat u$ 的衰减速度决定"。
  - **信号处理**：卷积是滤波器（低通/高通就是选择保留哪些频率），引理 4.3.8(3)"卷积变乘法"就是"时域滤波 = 频域相乘"；Parseval 等式保证滤波器不凭空产生能量。
  - **概率论**：独立随机变量之和的密度函数是各自密度的**卷积**，而卷积的 Fourier 变换是乘积——这正是特征函数方法（用乘积处理和的分布）的全部依据。
  - **量子力学**：$\Psi$ 是位置表象与动量表象之间的等距同构，$\Psi^4=I$ 对应测不准原理的代数结构。
- **跨领域解读**：**逼近恒等元（磨光）是"用光滑对象逼近粗糙对象"的标准手段**。本节用它证明了 $C_c^\infty$ 在 $L^p$ 中稠密（例 2）、多项式在 $L^p[a,b]$ 中稠密（例 3），并在 §4.1.4 的可分性证明中已埋下伏笔。同样的手法在偏微分方程（弱解的正则化）、数值分析（有限元的磨光）、机器学习（核平滑）中反复出现。**"先在有良好性质的子空间上证明，再用稠密性 + 等距性/连续性延拓"** 是本节的第二条方法论主线——Plancherel 定理就是它的完美范例。
- **高层视角**：本节把 [[Sec4.1 L^p 空间]] 的"范数/距离"与 [[Sec4.2 L^2 空间]] 的"内积/正交"升级为**算子**的语言：卷积是 $L^p$ 上的有界线性算子（Young 不等式正是算子范数估计 $\|T_g\|\le\|g\|_1$），Fourier 变换是 $L^2$ 上的酉算子（等距同构）。**从这里开始，"函数空间"变成了"算子作用的舞台"**——这正是 Ch5（Hilbert 空间上的算子）与 Ch6（Banach 空间上的有界线性算子）的出发点。特别地，$L^2$ 上的 Fourier 变换是 Ch5 §5.3 中"酉算子"最重要的具体例子。

## 防跳跃

- [ ] **广义 Young 不等式**：郭版只给出 $g\in L^1$ 的情形（定理 4.3.1）。一般形式 $\|f*g\|_r\le\|f\|_p\|g\|_q$（$\frac1r=\frac1p+\frac1q-1$）在本节**没有依据**，需要时另找材料。
- [ ] **$L^1$ 中卷积无单位元的完整证明**：反例 1 只给骨架（借定理 4.3.12 的 $C_0$ 性质），郭版把完整证明列为本节习题第 19 题，本节未展开。
- [ ] **$\mathcal{F}(L^1)$ 的完整刻画**：反例 4 指出 $\mathcal{F}:L^1\to C_0$ 非满射，但"哪些 $C_0$ 函数是某个 $L^1$ 函数的变换"这一问题郭版未讨论。
- [ ] **Fourier 变换在 $L^p$（$p\ne 1,2$）上的形态**：本节只讨论 $L^1$ 与 $L^2$。$1<p<2$ 时由 Hausdorff–Young 不等式有 $\mathcal{F}:L^p\to L^q$，$p>2$ 时只能作为广义函数意义下的变换——郭版未涉及。
- [ ] **Sobolev 空间**：由 $(P(\mathrm{D})f)^\wedge=P\hat f$ 与 $\hat f$ 的衰减估计可以定义 $W^{k,p}$ 并证明嵌入定理，这是本节结论最重要的下游，郭版未展开。
- [ ] **定理 4.3.13(3) 中 $C_c^\infty$ 的完备性论证**：证明末尾用"对一切 $\phi\in C_c^\infty$ 有 $\int(f_0-f)\phi=0$ 推出 $f_0=f$ a.e."，这一步依据的是 $C_c^\infty$ 在 $L^1_{\text{loc}}$ 中的稠密性（变分法基本引理），郭版未单独证明。
- [ ] **Plancherel 变换与 §4.2 标准正交基展开的关系**：$\Psi$ 在 $L^2(\mathbb{R})$ 上的特征函数是 Hermite 函数（特征值为 $(\pm\mathrm{i})^n$），这与 §4.2.2 的 Fourier 级数展开是"离散基"与"连续基"的对应，郭版未涉及。

## 来源与映射

| 本节点内容 | 来源 | 处理 |
|---|---|---|
| 复值可测/可积函数、复积分的三角不等式 | 郭版教材 §4.3 开头 | 新写（旧讲解包无对应） |
| 复值 $L^p$、复 $L^2$ 内积 $(f,g)=\int f\bar g$、复系数下 Bessel/Riesz–Fischer 的调整 | 郭版教材 §4.3 (4.3.3)–(4.3.9) | 新写；与 [[Sec4.2 L^2 空间]] 的实值版本呼应并标注差异 |
| 卷积定义、对称性、双线性性 | 郭版教材 §4.3.1 (4.3.10)(4.3.11) | 新写 |
| Young 不等式 + 完整证明（$p=\infty$ 与 $1\le p<\infty$ 两种情形） | 郭版教材 §4.3.1 定理 4.3.1 | 新写（保留 Fubini 交换积分次序的关键步） |
| $L^1$ 中卷积无单位元 | 郭版教材 §4.3.1 正文（指向习题 19） | 新写骨架证明（借定理 4.3.12） |
| 平均连续性引理 | 郭版教材 §4.3.1 引理 4.3.2 | 新写 |
| $L^2*L^2$ 有界连续、$\|f*g\|_\infty\le\|f\|_2\|g\|_2$ | 郭版教材 §4.3.1 定理 4.3.3 | 新写 |
| 多重指数、$\mathrm{D}^\alpha$、$C^s$、$C^\infty$ | 郭版教材 §4.3.1 (4.3.15)–(4.3.19) | 新写 |
| 微分可穿过卷积号 | 郭版教材 §4.3.1 定理 4.3.4 | 新写 |
| 逼近恒等元 $\varphi_\varepsilon$ 与定理 $\varphi_\varepsilon*f\xrightarrow{L^p}f$ | 郭版教材 §4.3.1 定义 4.3.5、定理 4.3.6 | 新写（完整证明骨架） |
| 例 1：滑动平均 $f_\varepsilon$ | 郭版教材 §4.3.1 例 1 | 新写 |
| 例 2：$C_c^\infty$ 在 $L^p$ 中稠密 | 郭版教材 §4.3.1 例 2、定理 4.3.10 | 新写（合并两处） |
| 例 3：Gauss 核 ⇒ 多项式在 $L^p[a,b]$ 中稠密 | 郭版教材 §4.3.1 例 3 | 新写（幂级数展开逐项积分的关键式保留） |
| 反例：$\varphi$ 仅 $L^1$ 时卷积只连续不可微 | 本节推演（由例 1 直接得出） | 新写 |
| 例题：$\chi_{[0,1]}*\chi_{[0,1]}$ 为三角形函数 | 本节推演 | 新写（并核对 Young 与定理 4.3.3 的等号） |
| Fourier 变换定义、$\hat f=f*e_{-t}(0)$、有界连续性 | 郭版教材 §4.3.2 定义 4.3.7、(4.3.25)(4.3.26) | 新写 |
| $\mathrm{D}_\alpha$、$P(\mathrm{D})e_t=P(t)e_t$ | 郭版教材 §4.3.2 (4.3.27)–(4.3.31) | 新写 |
| 引理 4.3.8：平移/调制/卷积/伸缩四条性质 | 郭版教材 §4.3.2 引理 4.3.8 | 新写（(1)(2) 保留完整计算） |
| 速降函数 $S(\mathbb{R}^n)$ 定义与等价刻画 | 郭版教材 §4.3.2 定义 4.3.9 | 新写 |
| $S(\mathbb{R}^n)$ 的三条性质（含 $\hat f\in S$） | 郭版教材 §4.3.2 命题 4.3.11 | 新写 |
| Riemann–Lebesgue 引理（$f\in L^1\Rightarrow\hat f\in C_0$） | 郭版教材 §4.3.2 定理 4.3.12 | 新写 |
| Gauss 函数的自对偶 $\hat G=G$ | 郭版教材 §4.3.2 (4.3.34)(4.3.35) | 新写（ODE 证明思路保留） |
| Fourier 逆定理（反演公式、$\mathcal{F}^4=I$、$L^1\cap\hat L^1$ 情形） | 郭版教材 §4.3.2 定理 4.3.13 | 新写（三步证明脉络完整） |
| 乘积变卷积 $(fg)^\wedge=\hat f*\hat g$ | 郭版教材 §4.3.2 定理 4.3.14 | 新写 |
| **Plancherel 定理**、Parseval 等式、$\Psi^2=\check f$、$\Psi^4=I$、等距同构 | 郭版教材 §4.3.2 定理 4.3.15、(4.3.40)–(4.3.46) | 新写（四步证明：$S$ 上 Parseval → 等距 → 稠密延拓 → 良定义与满射） |
| 反例：$\chi_{[-1,1]}$ 的变换不属于 $L^1$ | 本节推演 | 新写（由 $\int|\sin t/t|=\infty$ 得出） |
| 反例：$\mathcal{F}(L^1)\subsetneq C_0$ | 本节推演 | 新写（标注完整证明不在郭版范围，入「防跳跃」） |
| 例题：用 Plancherel 求 $\int\sin^2u/u^2\,\mathrm{d}u=\pi$ | 本节推演 | 新写 |
| 旧讲解包对应内容 | —— | **无**。旧《Ch7》《Ch9》《Ch10》均不涉及卷积与 Fourier 变换，本节为 100% 新写补缺 |