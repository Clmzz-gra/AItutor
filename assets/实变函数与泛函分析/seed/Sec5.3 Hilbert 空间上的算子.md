---
type: 节
formal: true
subject: 实变函数与泛函分析
created: 2026-09-21
updated: 2026-09-21
tags: [math, 实变函数与泛函分析]
chapter: 5
section: 5.3
---

# Sec5.3 Hilbert 空间上的算子

> 定位：Hilbert 空间上的线性算子什么时候连续？它有多大？它有没有"转置"？本节回答这三问，并证明投影算子与闭子空间一一对应——把几何对象（子空间）翻译成代数对象（算子）。
> 教材：郭懋正《实变函数与泛函分析》§5.3（p.240–255）
> 来源：旧讲解包《Ch8 有界线性算子和连续线性泛函》§1；旧讲解包《Ch9 内积空间和希尔伯特空间》§5；郭版教材 §5.3.1–§5.3.3

> [!info] 关联笔记
> - 父级：[[Ch5 Hilbert 空间理论]]
> - 前置：[[Sec5.2 Hilbert 空间理论]] ｜ 后续：[[Sec5.4 Hilbert 空间上的紧算子]]
> - 概念：[[概念-正交投影]]

---

## 来龙（为什么需要它）

- **类比已知**：$\mathbb{R}^n$ 上的线性算子就是矩阵，矩阵的"大小"用算子范数衡量，矩阵有转置 $A^{\mathsf T}$，对称矩阵满足 $A=A^{\mathsf T}$。本节把这些概念逐一搬到无穷维。
- **解决新问题**：微分算子 $Tx=x'$ 在 $C[0,1]$ 上是线性的，但它**不连续**——线性不再自动蕴含连续。而微分方程、积分方程、量子力学里到处是算子，必须先说清"哪些算子可以放心地取极限"。**无穷维里"线性"不再自动推出"连续"**，这是本节存在的根本理由。
- **理论/应用需要**：
  - 上一节的 Riesz 表示定理用了"连续线性泛函"，本节给出判定连续性的实用判据（**有界 ⟺ 连续**）；
  - 下一节的紧算子定义（"把有界集映成列紧集"）必须先有"有界算子"概念；
  - **共轭算子 $T^*$** 让算子有了"转置"，从而"自伴/酉/正规"三类算子可以定义——量子力学的可观测量 = 自伴算子、时间演化 = 酉算子。

> **边界说明**：赋范空间/ Banach 空间上的一般算子理论（范数等价、开映射定理、逆算子定理、共鸣定理）见 Ch6 §6.2；本节只写 **Hilbert 空间侧**的形态。

---

## 主体（核心内容）

### 5.3.1 线性算子的连续性和有界性

**记号（先固定）**：$X,Y$ 是同数域（$\mathbb R$ 或 $\mathbb C$）上的线性空间，$T:\mathcal D(T)\to Y$ 满足
$$T(x+y)=Tx+Ty,\qquad T(\alpha x)=\alpha Tx,$$
称 $T$ 为**线性算子**；$\mathcal D(T)$ 读作"$T$ 的定义域"，$\mathcal R(T)$ 读作"$T$ 的值域"，$\mathcal N(T)=\{x\in\mathcal D(T):Tx=0\}$ 读作"$T$ 的零空间"（也叫核 $\ker T$）。当 $Y$ 是数域时，$T$ 称为**线性泛函**。

**五个标准例子**（后面反复用）：

1. **相似算子** $Tx=\alpha x$（$\alpha$ 是固定数）；$\alpha=1$ 记 $I$（恒等算子），$\alpha=0$ 记 $O$（零算子）；
2. **微分算子** $Tx=x'$（定义在 $\mathcal P[0,1]$，即 $[0,1]$ 上多项式全体上）；
3. **积分算子** $(Tx)(t)=\int_a^t x(\tau)\,\mathrm d\tau$（$C[a,b]\to C[a,b]$）；$f(x)=\int_a^b x(\tau)\,\mathrm d\tau$ 是线性泛函；
4. **乘法算子** $(Tx)(t)=t\,x(t)$；
5. **矩阵算子**：$\mathbb R^n$ 上 $T=(t_{\mu\nu})$，$y_\mu=\sum_\nu t_{\mu\nu}\xi_\nu$——**有限维里线性算子与矩阵一一对应**。

**定义（有界线性算子）**：$X,Y$ 是赋范空间，线性算子 $T:\mathcal D(T)\to Y$。若存在常数 $c$ 使
$$\|Tx\|\leqslant c\|x\|\quad(\forall x\in\mathcal D(T)),$$
称 $T$ **有界**，否则称**无界**。

> **读法**：有界**不是**"值域有界"，而是"**放大倍数有上界**"——$T$ 把任何向量拉长的比例不超过常数 $c$。零向量必须映到零向量（*因为* $T0=T(0\cdot0)=0\cdot T0=0$），所以"值域有界"只可能发生在 $T=O$ 时。

**定理（有界 $\iff$ 连续，本节第一定理）**：线性算子 $T:X\to Y$ 有界 $\iff$ $T$ 连续。

**证明**：

- $(\Rightarrow)$ 设 $\|Tx\|\leqslant c\|x\|$。若 $x_n\to x$，则 *因为* $T$ 线性，
  $$\|Tx_n-Tx\|=\|T(x_n-x)\|\leqslant c\|x_n-x\|\to0,$$
  故 $Tx_n\to Tx$，$T$ 连续。
- $(\Leftarrow)$ **反证**。设 $T$ 连续但无界。无界指：存在 $\{x_n\}$ 使 $\|x_n\|\neq0$ 且 $\|Tx_n\|\geqslant n\|x_n\|$。令
  $$y_n=\frac{x_n}{n\|x_n\|},$$
  则 $\|y_n\|=\dfrac1n\to0$，即 $y_n\to0$。*因为* $T$ 连续，$Ty_n\to T0=0$；但 *因为* $T$ 线性，
  $$\|Ty_n\|=\frac{\|Tx_n\|}{n\|x_n\|}\geqslant1,$$
  不可能趋于 $0$。矛盾。$\square$

> **核心事实**：线性算子只要在**一个点**连续（比如 $0$ 点），就在所有点连续，且自动有界——*因为* 线性能把任意点的问题平移到 $0$ 点：$Tx-Tx_0=T(x-x_0)$。这是线性结构给分析学的红利。

**定理（线性泛函的零空间判据）**：线性泛函 $f:X\to\mathbb R$（或 $\mathbb C$）连续 $\iff$ 零空间 $\mathcal N(f)$ 是闭集。

**证明**：

- $(\Rightarrow)$：若 $x_n\in\mathcal N(f)$ 且 $x_n\to x$，*因为* $f$ 连续，$f(x)=\lim_n f(x_n)=0$，故 $x\in\mathcal N(f)$。
- $(\Leftarrow)$：设 $\mathcal N(f)$ 闭但 $f$ 无界，则存在 $\|y_n\|=1$ 且 $|f(y_n)|\geqslant n$。作
  $$z_n=\frac{y_n}{f(y_n)}-\frac{y_1}{f(y_1)},$$
  *因为* $f$ 线性且 $f(y_1)\neq0$（*因为* $|f(y_1)|\geqslant1$），$f(z_n)=1-1=0$，即 $z_n\in\mathcal N(f)$。但 *因为* $\left\|\dfrac{y_n}{f(y_n)}\right\|=\dfrac1{|f(y_n)|}\to0$，有 $z_n\to-\dfrac{y_1}{f(y_1)}$，而 $f\!\left(-\dfrac{y_1}{f(y_1)}\right)=-1\neq0$，极限不在 $\mathcal N(f)$ 中——与闭性矛盾。$\square$

**用途**：判断一个具体泛函是否连续，只需看它的零空间是否闭。**但注意**：这个等价只对**泛函**成立。

**反例（"零空间闭"推不出一般算子有界）**：取 $X$ 上无界线性泛函 $g$（无穷维空间中存在，构造依赖 Ham–Banach 定理），固定 $y_0\in Y$、$y_0\neq0$，定义
$$T:X\to X\times Y,\qquad Tx=(x,\ g(x)y_0).$$
则 *因为* $Tx=0$ 要求 $x=0$，$\mathcal N(T)=\{0\}$ 是闭集；但 $T$ 无界（*因为* $g$ 无界）。所以"核闭 $\Rightarrow$ 有界"是**泛函**的特殊性质，不是一般算子的性质。

**定义（算子范数）**：
$$\|T\|=\sup_{\substack{x\in\mathcal D(T)\\ x\neq0}}\frac{\|Tx\|}{\|x\|}.$$

**引理（三种等价算法）**：
$$\|T\|=\sup_{\|x\|=1}\|Tx\|=\sup_{\|x\|\leqslant1}\|Tx\|.$$
**证明**：把 $x/\|x\|$ 记作 $y$，则 *因为* 范数是正齐次的，$\|y\|=1$ 且 $\dfrac{\|Tx\|}{\|x\|}=\|Ty\|$，故第一个与第二个上确界互相夹住；又 *因为* 对 $\|x\|\leqslant1$ 有 $\|Tx\|\leqslant\|T\|\|x\|\leqslant\|T\|$，第三个不超过前两个。$\square$

**两个方向的使用习惯**：

- 要证 $\|T\|\leqslant c$：对任意 $x$ 证 $\|Tx\|\leqslant c\|x\|$；
- 要证 $\|T\|\geqslant c$：找一列 $\|x_n\|\leqslant1$ 使 $\|Tx_n\|\to c$（或找一个单位向量使 $\|Tx\|=c$）。

**例（相似算子）**：$Tx=\alpha x$ 有界且 $\|T\|=|\alpha|$；特别地 $\|I\|=1$、$\|O\|=0$。

**定理（$\mathcal B(H)$ 是 Banach 代数）**：记 $\mathcal B(H)$ 为 $H$ 上**有界线性算子**全体（$\mathcal B(H,H)$ 简写为 $\mathcal B(H)$）。

1. **线性结构**：按 $(A+B)x=Ax+Bx$、$(\alpha A)x=\alpha(Ax)$ 定义，$\mathcal B(H)$ 是线性空间，$\|\cdot\|$ 是范数；
2. **完备性**：$\mathcal B(H)$ 按算子范数**完备**，即它是 Banach 空间；
3. **乘法（复合）封闭且次可乘**：$A,B\in\mathcal B(H)\Rightarrow AB\in\mathcal B(H)$，且
   $$\|AB\|\leqslant\|A\|\,\|B\|$$
   （*因为* $\|ABx\|\leqslant\|A\|\,\|Bx\|\leqslant\|A\|\,\|B\|\,\|x\|$，对 $\|x\|\leqslant1$ 取上确界即得）；
4. **含单位元**：$I\in\mathcal B(H)$，$\|I\|=1$。

同时具备 (1)(2)(3)(4) 的结构称为 **Banach 代数**。

> **完备性的用法**：$\mathcal B(H)$ 完备意味着**算子列可以取极限**——这正是下一节定义紧算子的基础（紧算子全体 = 有限秩算子全体在 $\mathcal B(H)$ 中的闭包）。一般赋范空间的 $\mathcal B(X,Y)$ 完备性证明见 Ch6 §6.2。

**反例（无界算子，必须记住）**：$\mathcal P[0,1]$ 上的**微分算子** $Tx=x'$ 无界。取 $x_n(t)=t^n$，*因为* $\|x_n\|=\max_{[0,1]}|t^n|=1$，而 $\|Tx_n\|=\max_{[0,1]}|nt^{n-1}|=n$，故 $\|T\|\geqslant n$ 对一切 $n$ 成立，即 $\|T\|=\infty$。**这就是"线性不蕴含连续"的具体见证。**

**两个计算范数的例子**：

- **积分算子（$C[0,1]$ 上）**：$K(t,\tau)$ 在 $[0,1]^2$ 上连续，$(Tx)(t)=\int_0^1K(t,\tau)x(\tau)\,\mathrm d\tau$，则
  $$\|T\|=\max_{0\leqslant t\leqslant1}\int_0^1|K(t,\tau)|\,\mathrm d\tau.$$
  **$\leqslant$ 方向**：$\|Tx\|=\max_t\left|\int Kx\right|\leqslant\max_t\int|K|\cdot\|x\|$。
  **$\geqslant$ 方向（重点手法）**：设 $t_0$ 使 $\int_0^1|K(t_0,\tau)|\,\mathrm d\tau=M$。取**符号函数** $x(\tau)=\operatorname{sign}K(t_0,\tau)$（$K>0$ 处取 $1$、$K<0$ 处取 $-1$）——它只是可测、**不连续**，不能直接当 $C[0,1]$ 的元素。由**卢津定理**（Ch2 §2.3），存在连续函数 $x_n$ 使 $\|x_n\|\leqslant1$，且除一个测度小于 $1/(2nL)$ 的集合外 $x_n=x$（$L=\max|K|$）。于是
  $$M=\int_0^1K(t_0,\tau)x(\tau)\,\mathrm d\tau\leqslant\frac1n+\|Tx_n\|\leqslant\frac1n+\|T\|,$$
  令 $n\to\infty$ 得 $M\leqslant\|T\|$。**这里的卢津定理不是装饰：它把"能取到范数的可测函数"改造成"合法的连续函数"。**
- **Volterra 算子（$L^1[a,b]$ 上）**：$(Tf)(t)=\int_a^tf(\tau)\,\mathrm d\tau$，则 $\|T\|=b-a$。
  $\leqslant$ 方向：$\|Tf\|_1\leqslant\int_a^b\int_a^t|f(\tau)|\,\mathrm d\tau\,\mathrm dt\leqslant(b-a)\|f\|_1$；
  $\geqslant$ 方向：取 $f_n=n$ 于 $[a,a+1/n]$、$0$ 于其余，则 $\|f_n\|_1=1$，而 $\|Tf_n\|_1=(b-a)-\dfrac1{2n}\to b-a$。

### 5.3.2 共轭算子

**定义（共轭双线性形式回顾）**：上一节已定义——$u:H\times K\to\mathbb K$ 对第一变元线性、对第二变元共轭线性，且 $|u(x,z)|\leqslant c\|x\|\,\|z\|$ 时称有界，$c$ 为上界。

**定理（共轭算子的存在唯一性）**：设 $H,K$ 是 Hilbert 空间，$A\in\mathcal B(H,K)$，则存在**唯一**的 $A^*\in\mathcal B(K,H)$（$A^*$ 读作"$A$ 的共轭算子"，也叫 $A$ 的**伴随**）使
$$\langle Ax,y\rangle=\langle x,A^*y\rangle\quad(\forall x\in H,\ y\in K),\qquad \|A^*\|=\|A\|.$$

**证明骨架**：固定 $y\in K$，定义 $f_y(x)=\langle Ax,y\rangle$。*因为* $A$ 有界、内积连续，
$$|f_y(x)|=|\langle Ax,y\rangle|\leqslant\|Ax\|\,\|y\|\leqslant\|A\|\,\|y\|\,\|x\|,$$
即 $f_y$ 是 $H$ 上的连续线性泛函，$\|f_y\|\leqslant\|A\|\,\|y\|$。*因为* $H$ 是 Hilbert 空间，由 **Riesz 表示定理**（§5.2.3）存在唯一的 $z\in H$ 使 $f_y(x)=\langle x,z\rangle$，令 $A^*y=z$。**线性性**由 Riesz 表示的唯一性推出：*因为* $f_{\alpha y_1+\beta y_2}=\alpha f_{y_1}+\beta f_{y_2}$ 而表示元唯一，$A^*(\alpha y_1+\beta y_2)=\alpha A^*y_1+\beta A^*y_2$。**有界性**由 $\|A^*y\|=\|f_y\|\leqslant\|A\|\,\|y\|$ 得 $\|A^*\|\leqslant\|A\|$；再由 $A^{**}=A$ 双向估计得 $\|A^*\|=\|A\|$。$\square$

**基本性质**：

- $(A+B)^*=A^*+B^*$；
- $(\alpha A)^*=\bar\alpha A^*$（**注意共轭**：数乘要取共轭）；
- $A^{**}=A$（对合性）；
- $\|A^*A\|=\|AA^*\|=\|A\|^2$（**$C^*$ 恒等式**）；
- $(AB)^*=B^*A^*$（**次序反转**，与矩阵转置一致）。

**定义（自伴、酉、正规算子）**：设 $T\in\mathcal B(H)$，

- **自伴算子**（自共轭算子）：$T=T^*$；
- **正规算子**：$TT^*=T^*T$；
- **酉算子**：$T$ 是到上的等距映射，等价地 $T^*T=TT^*=I$（此时 $T^*=T^{-1}$）。

**关系**：自伴 $\Rightarrow$ 正规（*因为* $TT^*=T^2=T^*T$）；酉 $\Rightarrow$ 正规（*因为* $TT^*=I=T^*T$）；**反之不成立**：$T=2\mathrm iI$ 是正规的（$TT^*=4I=T^*T$），但 $T^*=-2\mathrm iI\neq T$ 故不自伴，又 $\|Tx\|=2\|x\|\neq\|x\|$ 故不酉。

**定理（自伴算子的判定，复空间）**：

1. **引理**：$T=O\iff\langle Tx,x\rangle=0$ 对一切 $x$。
2. **定理**：复 Hilbert 空间上，$T$ 自伴 $\iff\langle Tx,x\rangle$ 恒为实数。

**证明 (1)**：$(\Rightarrow)$ 平凡。$(\Leftarrow)$ 对 $v=\alpha x+y$ 用条件，*因为* $\langle Tv,v\rangle=0$ 且内积对第二变元共轭线性，展开得
$$\alpha\langle Tx,y\rangle+\bar\alpha\langle Ty,x\rangle+|\alpha|^2\langle Tx,x\rangle+\langle Ty,y\rangle=0,$$
其中后两项由条件为 $0$，故 $\alpha\langle Tx,y\rangle+\bar\alpha\langle Ty,x\rangle=0$ 对一切 $\alpha$ 成立。取 $\alpha=1$ 与 $\alpha=\mathrm i$ 分别代入，*因为* $\langle Tx,y\rangle$ 与 $\langle Ty,x\rangle=\overline{\langle Tx,y\rangle}$ 的关系，两式相加得 $\langle Tx,y\rangle=0$ 对一切 $x,y$，故 $T=O$。
**证明 (2)**：*因为* $\overline{\langle Tx,x\rangle}=\langle x,Tx\rangle=\langle T^*x,x\rangle$，若 $\langle Tx,x\rangle$ 恒为实数则 $\langle Tx,x\rangle=\langle T^*x,x\rangle$，即 $\langle(T-T^*)x,x\rangle=0$ 对一切 $x$，由引理 (1) 得 $T=T^*$。$\square$

> **实空间的反例（引理 (1) 在实空间不成立）**：在 $\mathbb R^2$ 上取旋转 $90^\circ$ 的算子 $T(x_1,x_2)=(-x_2,x_1)$。*因为* $\langle Tx,x\rangle=-x_2x_1+x_1x_2=0$ 对一切 $x$ 成立，但 $T\neq O$。所以上面的引理**只对复空间**成立——这也是为什么自伴算子的谱理论（§5.4.3）要假定复 Hilbert 空间。

**定理（自伴算子的其他性质）**：

- 自伴算子乘积自伴 $\iff$ 两算子可交换：$(T_1T_2)^*=T_2^*T_1^*=T_2T_1$，故 $(T_1T_2)^*=T_1T_2\iff T_1T_2=T_2T_1$。
- 自伴算子列的极限仍自伴：*因为* $\|T_n-T\|\to0\Rightarrow\|T_n^*-T^*\|=\|(T_n-T)^*\|\to0$，故 $T^*=\lim T_n^*=\lim T_n=T$。
- **自伴算子的范数可由二次型算出**：$\|T\|=\sup_{\|x\|=1}|\langle Tx,x\rangle|$。

**定理（酉算子的性质）**：酉算子保范（$\|Ux\|=\|x\|$）、$\|U\|=1$、$U^{-1}$ 与 $UV$ 仍酉、酉算子列的极限仍酉。

**反例（保范不一定是酉，关键反例）**：$l^2$ 上的**单向移位**
$$T(\xi_1,\xi_2,\xi_3,\dots)=(0,\xi_1,\xi_2,\dots).$$
*因为* $\|Tx\|^2=\sum_{k\geqslant1}|\xi_k|^2=\|x\|^2$，$T$ **保范**；但 $\mathcal R(T)=\{y\in l^2:y_1=0\}$ **不是满射**（第一坐标为 $0$ 的全体），故 $T$ 不是酉算子。**区别在于：酉算子要求"保范 + 到上"，缺一不可。** 顺带一提，$T^*$ 是反向移位 $T^*(\eta_1,\eta_2,\dots)=(\eta_2,\eta_3,\dots)$，满足 $T^*T=I$ 但 $TT^*\neq I$——这正是"保范不到上"的代数表现。

**定理（正规算子）**：设 $A=\dfrac{T+T^*}{2}$（**实部**）、$B=\dfrac{T-T^*}{2\mathrm i}$（**虚部**），则 $A,B$ 自伴且 $T=A+\mathrm iB$（**笛卡儿分解**）。并且

1. $T$ 正规 $\iff AB=BA$；
2. $T$ 正规 $\iff\|T^*x\|=\|Tx\|$ 对一切 $x$。

**证明 (2)**：*因为*
$$\|T^*x\|^2-\|Tx\|^2=\langle T^*x,T^*x\rangle-\langle Tx,Tx\rangle=\langle(TT^*-T^*T)x,x\rangle,$$
由 5.3.2 的引理 (1)，右端恒为 $0$ $\iff$ $TT^*-T^*T=O$。$\square$

> **核心事实**：内积让算子有了"转置"（共轭算子），于是有限维矩阵理论的三类重要矩阵（Hermite 矩阵、酉矩阵、正规矩阵）在无穷维获得了对应物。**量子力学里可观测量 = 自伴算子，时间演化算子 = 酉算子**——这就是三类算子如此命名的原因。

### 5.3.3 投影算子

**定义（投影算子）**：设 $M$ 是 Hilbert 空间 $H$ 的**闭**子空间。由投影定理（§5.2.2），每个 $x\in H$ 有唯一分解 $x=y+z$，$y\in M$、$z\in M^\perp$。定义
$$P_Mx=y,$$
称 $P_M$ 为 $H$ 到 $M$ 上的**正交投影算子**（简称投影算子）。

**定理（投影算子的基本性质）**：设 $M$ 是闭子空间，$P=P_M$，则

1. $P$ 是**线性**算子；
2. $P$ 是**有界**的，且 $\|P\|=1$（当 $M\neq\{0\}$）；
3. **幂等**：$P^2=P$；
4. **自伴**：$P^*=P$；
5. $\mathcal R(P)=M$，$\mathcal N(P)=M^\perp$；
6. $I-P=P_{M^\perp}$。

**证明要点**：

- (1) *因为* 分解唯一，$\alpha x_1+\beta x_2$ 的 $M$ 分量必为 $\alpha y_1+\beta y_2$，故 $P$ 线性。
- (2) *因为* $y\perp z$，勾股公式给出 $\|x\|^2=\|y\|^2+\|z\|^2\geqslant\|y\|^2=\|Px\|^2$，故 $\|Px\|\leqslant\|x\|$ 即 $\|P\|\leqslant1$；又对 $x\in M$（$x\neq0$）有 $Px=x$，故 $\|P\|\geqslant1$。
- (3) *因为* $y\in M$ 时 $Py=y$，故 $P(Px)=Py=y=Px$。
- (4) 对 $x=y+z$、$x'=y'+z'$（$y,y'\in M$；$z,z'\in M^\perp$），*因为* 两个分量互相正交，
  $$\langle Px,x'\rangle=\langle y,y'+z'\rangle=\langle y,y'\rangle,\qquad\langle x,Px'\rangle=\langle y+z,y'\rangle=\langle y,y'\rangle,$$
  两者相等，故 $P^*=P$。
- (5)(6) 直接由分解 $x=y+z$ 读出。$\square$

**定理（投影算子与闭子空间一一对应，代数刻画）**：设 $P\in\mathcal B(H)$。则
$$P\ \text{是某个闭子空间上的正交投影}\iff P^2=P\ \text{且}\ P^*=P.$$
且此时 $P=P_M$ 中的 $M=\mathcal R(P)$ 由 $P$ 唯一确定。

**证明**：

- $(\Rightarrow)$ 即上面的性质 (3)(4)。
- $(\Leftarrow)$ 设 $P^2=P$、$P^*=P$，令 $M=\mathcal R(P)$。**先证 $M$ 闭**：若 $y_n=Px_n\to y$，*因为* $P$ 连续，$Py_n=P^2x_n=Px_n=y_n$，令 $n\to\infty$ 得 $Py=y$，故 $y\in\mathcal R(P)=M$。**再证 $P=P_M$**：对任意 $x$，*因为* $P(Px)=Px$ 得 $Px\in M$；令 $z=x-Px$，*因为* $P^*=P$、$P^2=P$，
  $$\langle z,Px'\rangle=\langle x-Px,Px'\rangle=\langle Px,x'\rangle-\langle Px,Px'\rangle=\langle Px,x'\rangle-\langle P^2x,x'\rangle=0,$$
  对一切 $x'$ 成立，故 $z\in M^\perp$。于是 $x=Px+z$ 正是 $x$ 沿 $M$ 与 $M^\perp$ 的分解，由唯一性得 $Px=P_Mx$。
- **唯一性**：若 $P=P_M=P_N$，则 $M=\mathcal R(P)=\mathcal R(P_M)=M$，故 $N=M$。$\square$

**推论（投影的序结构）**：

- **正交投影的和**：若 $M\perp N$（即 $M\subset N^\perp$），则 $P_M+P_N=P_{M\oplus N}$，且 $P_MP_N=P_NP_M=O$；
- **乘积为零 $\iff$ 值域正交**：$P_MP_N=O\iff M\perp N$；
- **包含关系**：$M\subset N\iff P_M=P_NP_M=P_MP_N$。

**反例（幂等但不自伴，不是正交投影）**：在 $\mathbb R^2$ 上取
$$P(x_1,x_2)=(x_1+x_2,\ 0).$$
*因为* $P^2(x_1,x_2)=P(x_1+x_2,0)=(x_1+x_2,0)=P(x_1,x_2)$，$P$ **幂等**；但 *因为* $\langle Pe_1,e_2\rangle=\langle(1,0),(0,1)\rangle=0$ 而 $\langle e_1,Pe_2\rangle=\langle(1,0),(1,0)\rangle=1$，两者不等，$P^*\neq P$，**不是自伴**。它的值域是 $x$ 轴，但它是"沿斜方向 $(1,-1)$ 投影"的**斜投影**（平行投影），不是正交投影。**这说明 $P^2=P$ 单独不够——必须加上 $P^*=P$ 才是正交投影。**

**例题**：设 $H=L^2[-1,1]$，$M=\{f\in H:f\ \text{是偶函数}\}$，求 $P_M$ 的显式表达式，并求 $f(t)=t+t^2$ 的投影与到 $M$ 的距离。

- **原始信息**：内积 $\langle f,g\rangle=\int_{-1}^1f(t)g(t)\,\mathrm dt$。
- **判断 $M$ 是闭子空间**：*因为* 偶函数全体是 $H$ 的线性子空间，且若 $f_n\to f$（$L^2$ 收敛）而每个 $f_n$ 偶，则 *因为* $L^2$ 收敛蕴含存在子列几乎处处收敛（Ch4 §4.3 的 Riesz 定理），该子列几乎处处偶，故 $f$ 几乎处处偶，即 $f\in M$——$M$ 闭。
- **求正交补**：*因为* 任一 $g\in H$ 可写成偶部与奇部之和
  $$g_e(t)=\frac{g(t)+g(-t)}{2},\qquad g_o(t)=\frac{g(t)-g(-t)}{2},$$
  且 *因为* $\int_{-1}^1g_e(t)g_o(t)\,\mathrm dt=0$（被积函数是奇函数），$M^\perp=\{g:g\ \text{几乎处处奇}\}$。
- **写出投影算子**：由正交分解的唯一性，
  $$(P_Mf)(t)=\frac{f(t)+f(-t)}{2}.$$
- **代入 $f(t)=t+t^2$**：
  $$(P_Mf)(t)=\frac{(t+t^2)+(-t+t^2)}{2}=t^2.$$
- **求距离**：*因为* $f-P_Mf=t$ 是奇函数，
  $$d(f,M)=\|f-P_Mf\|_2=\left(\int_{-1}^1t^2\,\mathrm dt\right)^{1/2}=\sqrt{\frac23}\approx0.816.$$
- **结论**：$f$ 在偶函数子空间上的最佳逼近是它的**偶部** $t^2$，残差是它的**奇部** $t$；这也直接验证了最佳逼近的几何意义——**残差必须与逼近子空间正交**（$t\perp$ 一切偶函数）。

> **这一节真正要说的是什么**：内积让"算子"这门学科有了三样东西——**大小**（算子范数，且"有界 ⟺ 连续"让连续性变得可计算）、**转置**（共轭算子 $T^*$，从而自伴/酉/正规三类算子可定义）、**几何对应**（投影算子与闭子空间一一对应，且 $P^2=P,\ P^*=P$ 两条代数条件就完全刻画了几何对象）。**Hilbert 空间上的几何问题，从此可以翻译成算子的代数问题。**

---

## 去脉（学完去哪）

- **当代应用**：
  - **量子力学**：可观测量 = 自伴算子（谱 = 测量可能值），时间演化 = 酉算子（保概率），投影算子 = 测量装置。$P^2=P$、$P^*=P$ 这两条公理正是"重复测量不改变结果"的代数表述。
  - **数值线性代数**：正交投影是 Krylov 子空间方法（GMRES、共轭梯度）的核心；斜投影对应 Petrov–Galerkin 方法。
  - **统计学**：最小二乘估计 $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}y$ 就是 $y$ 在列空间上的正交投影。
  - **图像处理**：正交投影是"去噪"的原型——把观测投影到信号子空间上。
- **跨领域解读**：共轭算子 $T^*$ 在有限维就是矩阵的**共轭转置**；$\|T^*T\|=\|T\|^2$ 这条 $C^*$ 恒等式，是把算子代数（$C^*$-代数）与量子场论联系起来的起点。
- **高层视角**：本章前三节已经完成"几何 ⟹ 代数"的翻译。下一节（§5.4）在此之上再问一句：**哪些算子在无穷维里仍像矩阵一样"可控"？** 答案是紧算子——它有离散谱、有 Fredholm 二择一、有谱分解。这是把无穷维问题化归为有限维问题的最后一块拼图。

## 防跳跃

- [ ] $\mathcal B(H)$ 完备性的完整证明（用一致有界性把算子列的收敛逐点拼出极限算子）——一般赋范空间版本见 Ch6 §6.2
- [ ] 无穷维空间上无界线性泛函的存在性（依赖 Ham–Banach 定理或 Zorn 引理）——见 Ch6 §6.3
- [ ] $\|T\|=\sup_{\|x\|=1}|\langle Tx,x\rangle|$（自伴算子范数的二次型公式）的证明
- [ ] 投影算子的序结构（$P_M\leqslant P_N\iff M\subset N$）与"投影格"的完整理论
- [ ] 部分等距算子与极分解 $T=U|T|$（共轭算子的进一步应用）
- [ ] 正规算子谱定理（一般正规算子的谱测度形式）——超出本节范围，需测度论工具
- [ ] 无界算子（闭算子、定义域的处理）：量子力学中位置算子、动量算子都不属于 $\mathcal B(H)$

## 来源与映射

| 本节点内容 | 来源 | 处理 |
|---|---|---|
| 线性算子/泛函记号、五个标准例子 | 旧《Ch8》§1.1 | 原文迁移 |
| 有界线性算子定义与"放大倍数"读法 | 旧《Ch8》§2.1 | 原文迁移 |
| 定理：有界 $\iff$ 连续（含完整推导） | 旧《Ch8》§2.2 定理 1 | 原文迁移 |
| 线性泛函的零空间判据 | 旧《Ch8》§2.3 定理 2 | 原文迁移 |
| 反例：零空间闭但算子无界 | 旧《Ch8》§5.4 | 原文迁移 |
| 算子范数定义与三种等价算法 | 旧《Ch8》§2.4 | 原文迁移 |
| 积分算子范数（用卢津定理）、Volterra 算子范数 | 旧《Ch8》§2.5 例 1、例 2 | 原文迁移 |
| 反例：微分算子无界 | 旧《Ch8》§2.5 例 3 | 原文迁移 |
| $\mathcal B(H)$ 的 Banach 代数结构 | 旧《Ch8》§2；郭版教材 §5.3.1 | 新写（按 Hilbert 空间口径组织，一般版本指向 Ch6 §6.2） |
| 共轭算子 $T^*$ 的存在唯一性与性质 | 旧《Ch9》§5.1 | 原文迁移 |
| 自伴/酉/正规算子的定义与关系 | 旧《Ch9》§5.2 | 原文迁移 |
| 自伴算子判定（引理 + 定理 + 实空间反例） | 旧《Ch9》§5.3 | 原文迁移 |
| 酉算子性质与单向移位反例 | 旧《Ch9》§5.4 | 原文迁移 |
| 正规算子与笛卡儿分解 | 旧《Ch9》§5.5 | 原文迁移 |
| 投影算子的定义与基本性质 | 旧《Ch9》§2.2；郭版教材 §5.3.3 | 原文迁移 + 补完整证明 |
| 投影算子与闭子空间的一一对应（代数刻画） | 郭版教材 §5.3.3 | 新写补缺 |
| 反例：幂等但不自伴（斜投影） | 郭版教材 §5.3.3 | 新写 |
| 例题：偶函数子空间上的投影 | 郭版教材 §5.3.3 投影算子性质 | 新写（据定理自编计算例） |