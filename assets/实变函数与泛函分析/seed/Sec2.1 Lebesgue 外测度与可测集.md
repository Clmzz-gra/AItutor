---
type: 节
formal: true
subject: 实变函数与泛函分析
created: 2026-09-21
updated: 2026-09-21
tags: [math, 实变函数与泛函分析]
chapter: 2
section: 2.1
---
# Sec2.1 Lebesgue 外测度与可测集

> 定位：本节把"长度"从区间推广到一般集合——先对**任意**集合定义外包上界（外测度），再用 Carathéodory 条件筛出"上界即真值"的可测集，并盘点这批集合到底有哪些。
> 教材：郭懋正《实变函数与泛函分析》§2.1（p.45–60）
> 来源：旧讲解包《Ch3 测度论》的「引言」「一、整体认知」「三、主体之一：外测度」「四、主体之二：Carathéodory 条件」「五、主体之三：盘点可测集类」「六、边界：不可测集」；郭版教材 §2.1.3（新写补缺：抽象测度空间与完备化）

> [!info] 关联笔记
> - 父级：[[Ch2 Lebesgue 测度]]
> - 前置：Ch1 §1.3（n 维欧氏空间）｜ 后续：[[Sec2.2 Lebesgue 可测函数]]
> - 概念：[[概念-外测度与Caratheodory条件]]、[[概念-有理数与无理数集的测度]]、[[概念-可数可加性]]

---

## 来龙（为什么需要它）

- **类比已知**：你从小就在用长度、面积、体积——三条最基本的"长度公理"是：非负性 $m(E)\geqslant 0$；有限可加性（有限个两两不交集合之并的测度等于各自测度之和）；正则性 $m([0,1])=1$。这套公理能算区间、能算有限个线段之并，仅此而已。
- **解决新问题**：一旦问"$[0,1]$ 中全体有理数集 $\mathbb{Q}\cap[0,1]$ 的长度是多少"，三条公理**全部沉默**——它不是有限个区间之并。更急迫的是勒贝格积分的机制：勒贝格"横着切值域"，第 $i$ 层的底边是水平集 $A_i=\{x: y_{i-1}\leqslant f(x)<y_i\}$，积分近似为 $\sum_i y_i\cdot m(A_i)$。**想算积分，就必须先会量 $A_i$ 这类集合。**
- **理论/应用需要**：没有测度，"几乎处处（a.e.）"这句话根本说不出来——现代分析大量结论是"除去一个测度为零的集合之外成立"。1933 年 Kolmogorov 的概率公理化可以整句翻译为：**事件 = 可测集，概率 = 测度**；没有本节，概率公理没有地基。

三个需求指向同一个缺口：

```
黎曼积分失败 ────┐
"几乎处处"没定义 ──┼──→ 缺口：任意集合的"大小"没有严格定义
概率无法公理化 ──┘
                        │
                        ▼
        外包（外测度）→ 筛选（Carathéodory）→ 验证（可数可加）
                 → 盘点（可测集类）→ 边界（不可测集）
```

## 主体（核心内容）

### §2.1.1 外测度

**第一步：先承认三条"长度公理"**

对某集合族 $\mathcal{M}$ 中的每个集合 $E$，对应实数 $m(E)$（读作"$E$ 的测度"，即给集合 $E$ 赋一个"大小"），满足：

1. **非负性**：$m(E)\geqslant 0$；
2. **有限可加性**：若 $E_1,\dots,E_n$ 两两不相交，则 $m(E_1\cup\cdots\cup E_n)=m(E_1)+\cdots+m(E_n)$；
3. **正则性**：$m([0,1])=1$。

> **停顿自问**：这三条能测出什么？——只有区间、有限个线段之并这些"规矩"的集合。一旦问 $\mathbb{Q}\cap[0,1]$ 的长度，三条公理全都沉默：它不是有限个区间的并。

**第二次尝试：把"有限可加"改成"无限可加"——失败**

**反例（为什么不能无限制推广，强制动作）**：单点集 $\{a\}$ 的长度应为 $m([a,a])=a-a=0$。如果允许**任意**无限可加，那么

$$[0,1]=\bigcup_{x\in[0,1]}\{x\}$$

是**不可数个**单点的并。逐点求和 $\sum_{x\in[0,1]}m(\{x\})=0$，于是 $m([0,1])=0$——与正则性 $m([0,1])=1$ 矛盾。

**诊断**：问题出在"任意无限"——$[0,1]$ 是**不可数集**，不能写成**可数**个单点之并。勒贝格的做法是**只要求可数可加性**：

> **定义（勒贝格测度公理）** 对某集合族 $\mathcal{M}$，$m$ 满足非负性、正则性 $m([a,b])=b-a$，以及
>
> - **可数可加性**（也称可列可加性）：若 $\{E_i\}_{i=1}^{\infty}$ 两两不相交，则
>   $$m\!\left(\bigcup_{i=1}^{\infty}E_i\right)=\sum_{i=1}^{\infty}m(E_i).$$

在这个公理下：$\mathbb{Q}\cap[0,1]$ 可数、每个单点测度 $0$，所以它的测度**必须**是 $0$；而 $[0,1]$ 中无理数集不可数，可数可加性**不再强迫**它为 $0$——由 $1=m([0,1])=m(\mathbb{Q})+m(\text{无理数})$ 反推出无理数集测度为 $1$。

> **停顿自问**：为什么可数可加性能绕开上面的悖论？——因为可数可加只对**可数并**生效，而 $[0,1]$ 无法写成可数个单点之并。这就是 Ch1 里"可数 vs 不可数"第一次在实战中定生死。

于是本章的全部工作浓缩为三个问题：

1. **存在性**：满足三条勒贝格公理的 $m$ 是否存在？
2. **定义域**：$\mathcal{M}$ 里有哪些集合？怎么判定 $E\in\mathcal{M}$？
3. **完备性**：每个集合都有测度吗？（答案：没有——见本节的 Vitali 构造。）

先预告两个贯穿全章的符号，后面不再"凭空出现"：

- $m^{*}E$（读作"$E$ 的外测度"）$=$ 用可数开区间覆盖 $E$ 的所有体积总和的下确界——通俗说就是"外包成本"；
- $mE$（读作"$E$ 的测度"）$=$ 把 $m^{*}$ 限制到"可测集"上得到的真正大小。

两者的关系先记住一句：**$m^{*}$ 是上界，$m$ 是筛选后的真值。**

**内填外包法与 Carathéodory 的简化（动机）**

测量不规则图形的面积，小学的方法是**内填外包**：外面包住图形的格子面积下确界（过剩近似），里面填满图形的格子面积上确界（不足近似），两者相等就是面积。勒贝格的**原始定义**就是这条路：外测度 $m^{*}$（外包）与内测度 $m_{*}$（内填）相等即"可测"。

**但这条路有代价**：要分有界/无界两种情形讨论，内测度的性质每一条都要分类证明，繁琐。

**Carathéodory 的简化**（本教材采用）：**丢掉内测度**，只保留外测度 $m^{*}$，外加一个纯用 $m^{*}$ 写出的筛选条件。它一刀切出恰好与"内外相等"相同的集合类，证明却清爽得多。两种定义的等价性见教材附录一。

> **核心洞察**：本章的全部智慧可以浓缩为一句话——**先对一切集合定义"上界"（外测度），再筛选出"上界不虚报"的集合（可测集），最后证明在这批集合上"上界"变成了真正的"大小"（测度）。** 这是"外定义 → 内筛选 → 得到良定义"的通用数学范式。

**为什么这样定义外测度：三个设计决策**

**目标**：对**任意** $E\subseteq\mathbb{R}^n$ 定义 $m^{*}E$，并且当 $E$ 是区间时 $m^{*}E$ 必须等于熟知体积 $|E|$。

**① 为什么用"覆盖"，取"下确界"？**
因为对任意 $E$，直接求"体积"没有意义；但用已知体积的区间去**包住** $E$ 总是可能的。所有覆盖体积构成一个非负数集，取下确界就得到 $E$ 的"最小覆盖成本"。

**② 为什么用可数个区间，不用有限个？（反例，强制动作）**
看 $E=\mathbb{Q}\cap[0,1]$。若只允许**有限个**开区间覆盖 $E$：这有限个区间连同端点一起必覆盖稠密集 $E$ 的闭包 $[0,1]$，所以覆盖总体积至少 $1$，于是"有限覆盖外测度" $(\geqslant 1)$ 就测不出"有理数长度应为 0"这件事。同理无理数集也至少 $1$，$[0,1]$ 被拆成两份后总长 $\geqslant 2$——荒谬。
**因为**可数覆盖允许我们给第 $i$ 个点配长度 $\varepsilon/2^i$ 的区间，总长只有 $\varepsilon$；有限覆盖做不到这种"逐点微调"。

**③ 为什么用开区间，不用闭区间？**
因为左开右闭区间去掉边界后与开区间体积相同，两者在"体积"意义上无差别；而**可数个开区间的并恰是开集**，于是外测度定义等价于"用开集外包"。开集的构造已有完整结论（$\mathbb{R}$ 中非空开集 = 可数多个互不相交的开区间之并），而且开集是后面最先被证明可测的集合之一。

> **定义（勒贝格外测度）** 设 $E$ 为 $\mathbb{R}^n$ 中任一点集（在 $\mathbb{R}^n$ 中，"开区间"指开长方体 $(a_1,b_1)\times\cdots\times(a_n,b_n)$，$|I|$ 读作"$I$ 的体积"）。对每一列覆盖 $E$ 的开区间 $\bigcup_{i=1}^{\infty}I_i\supset E$，作体积总和 $\mu=\sum_{i=1}^{\infty}|I_i|$（允许 $\mu=\infty$）。所有这些 $\mu$ 组成的下方有界数集的下确界，称为 $E$ 的**勒贝格外测度**（$L$ 外测度），记为 $m^{*}E$（读作"$E$ 的外测度"）：

$$m^{*}E=\inf_{E\subset \bigcup_{i=1}^{\infty}I_i}\ \sum_{i=1}^{\infty}|I_i|.$$

**"外"字的含义**：从外部逼近。真正的测度应当 $\leqslant$ 外测度；若还能从内部逼近到同一个值，才是"可测"（Carathéodory 条件正是这件事的等价表述）。

**三条基本性质（推导全程）**

**性质 1（非负）**：$m^{*}E\geqslant 0$，且 $m^{*}(\varnothing)=0$（$\varnothing$ 读作"空集"）。
*因为*每个覆盖的体积和 $\geqslant 0$，下确界也 $\geqslant 0$；空集可被任意小的区间覆盖，故 $m^{*}(\varnothing)=0$。

**性质 2（单调性）**：$A\subset B\Rightarrow m^{*}A\leqslant m^{*}B$。
*因为*覆盖 $B$ 的任何一列开区间自动覆盖 $A$，所以覆盖 $A$ 的候选集**更多**，下确界更小（或相等）。

**性质 3（次可数可加性）**：$m^{*}\!\left(\bigcup_{i=1}^{\infty}A_i\right)\leqslant \sum_{i=1}^{\infty}m^{*}A_i$。

> 这是外测度最核心的一条性质，证明里的 $\varepsilon/2^n$ 技巧全章复用，建议亲手推导一遍。

**目标**：任给 $\varepsilon>0$，证明 $m^{*}(\bigcup_i A_i)\leqslant \sum_i m^{*}A_i+\varepsilon$。

- **第 1 步（把下确界翻译成具体覆盖）**：对每个 $n$，*因为* $m^{*}A_n$ 是覆盖 $A_n$ 的区间列总体积的**下确界**（未必取到），所以存在一列开区间 $I_{n,1},I_{n,2},\dots$ 覆盖 $A_n$，且
  $$\sum_{m=1}^{\infty}|I_{n,m}|\leqslant m^{*}A_n+\frac{\varepsilon}{2^n}.$$
  （利用下确界性质挑选了接近下确界的开覆盖）
  *为什么误差给 $\varepsilon/2^n$？* 为了第 3 步能求和：$\sum_n \varepsilon/2^n=\varepsilon$。
- **第 2 步（拼装成一个大覆盖）**：全体 $\{I_{n,m}\}_{n,m}$ 是**可数个**区间（可数个可数集的并仍可数——用到了 Ch1），且覆盖 $\bigcup_n A_n$，故
  $$m^{*}\!\left(\bigcup_n A_n\right)\leqslant \sum_{n,m=1}^{\infty}|I_{n,m}|.$$
- **第 3 步（算总账）**：
  $$\sum_{n,m}|I_{n,m}|=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}|I_{n,m}|\leqslant \sum_{n=1}^{\infty}\left(m^{*}A_n+\frac{\varepsilon}{2^n}\right)=\sum_{n=1}^{\infty}m^{*}A_n+\varepsilon.$$
- *因为* $\varepsilon$ 任意，令 $\varepsilon\to0$（严格说：若左边 $>$ 右边，取 $\varepsilon$ 小于其差即矛盾），得证。

> **停顿自问**：证明中哪一步用到了"可数"？——第 2 步"可数个可数集的并仍可数"。如果把可数改成不可数，这步就垮了。这再次呼应"任意无限可加失败"的诊断。

**三个定调例子（演绎：最小实例手动走）**

**例 1（稠密可数 → 零测）**：$E=\mathbb{Q}\cap[0,1]$，则 $m^{*}E=0$。

把 $E$ 排成 $\{r_1,r_2,\dots\}$。任给 $\varepsilon>0$，对第 $i$ 个点配区间

$$I_i=\left(r_i-\frac{\varepsilon}{2^{i+1}},\ r_i+\frac{\varepsilon}{2^{i+1}}\right),$$

*因为* $|I_i|=\varepsilon/2^i$ 且 $\sum_i \varepsilon/2^i=\varepsilon$，所以 $m^{*}E\leqslant \varepsilon$。*因为* $\varepsilon$ 任意且 $m^{*}E\geqslant 0$，所以 $m^{*}E=0$。

**例 2（疏朗不可数 → 也零测，教材没有但极其重要）**：康托尔三分集 $C$ 满足 $m^{*}C=0$。

*因为* $C\subset F_n$（$F_n$ 是 $2^n$ 个长度 $3^{-n}$ 的闭区间之并），把这些闭区间各稍加膨胀成开区间（总长最多额外 $\varepsilon/2$），并取 $n$ 使 $(2/3)^n<\varepsilon/2$，得到一个总长 $<\varepsilon$ 的**开**覆盖，故 $m^{*}C\leqslant\varepsilon$，从而 $m^{*}C=0$。

> **对比（易混概念）**：$\mathbb{Q}\cap[0,1]$ **稠密、可数**，测度 $0$；康托尔集 $C$ **疏朗、不可数**，测度也为 $0$。"测度"既不等于"稠密程度"，也不等于"元素多少"——它是**集合被区间逼近的几何成本**。

**例 3（锚点：区间）**：对任何区间 $I$（开/闭/半开半闭），$m^{*}I=|I|$。

- **方向 $\leqslant$**：取一个比 $I$ 稍大的开区间 $I'$，使 $|I'|<|I|+\varepsilon$。*因为* $I'$ 本身就是一个合法覆盖，故 $m^{*}I\leqslant |I'|<|I|+\varepsilon$；令 $\varepsilon\to0$ 得 $m^{*}I\leqslant |I|$。
- **方向 $\geqslant$（难点，用 Heine–Borel 有限覆盖定理）**：先设 $I=[a,b]$ 闭。任取覆盖列 $\{I_i\}$ 使 $\sum_i|I_i|<m^{*}I+\varepsilon$。*因为* $[a,b]$ 是有界闭集，由有限覆盖定理，存在**有限**多个 $I_1,\dots,I_n$ 仍覆盖 $[a,b]$。*因为* $[a,b]=\bigcup_{i=1}^{n}([a,b]\cap I_i)$，有限个区间覆盖一个闭区间，初等几何给出
  $$|I|\leqslant\sum_{i=1}^{n}|I\cap I_i|\leqslant\sum_{i=1}^{n}|I_i|\leqslant\sum_{i=1}^{\infty}|I_i|<m^{*}I+\varepsilon.$$
  令 $\varepsilon\to0$ 得 $|I|\leqslant m^{*}I$。对任意区间 $I$，取闭区间 $I_1\subset I\subset I_2$ 夹逼：$|I_1|\leqslant m^{*}I\leqslant|I_2|$，令 $|I_2|-|I_1|\to0$ 即得。

> **为什么必须用有限覆盖？** 可数个区间可以切得极碎去覆盖 $[a,b]$，你无法逐段论证"总长不小于 $b-a$"；有限覆盖把问题降级为**有限个区间**的初等事实。这是本章第一次"用紧性换加法"。

**反例与缺陷：外测度还不是测度**

外测度的三性质里只有**次可加**（$\leqslant$）没有**可加**（$=$）。教材直言：存在互不相交的集合列 $\{E_i\}$ 使

$$m^{*}\!\left(\bigcup_{i=1}^{\infty}E_i\right)<\sum_{i=1}^{\infty}m^{*}E_i.$$

**严谨性说明**：这样的集合列无法用"区间拼出来"，必须借助后面的不可测集（从而依赖选择公理）。所以现在先承认这个缺陷、继续前进；到本节的 Vitali 构造，你会亲眼看到严格不等式是如何被构造出来的。

| 对比项 | 外测度 $m^{*}$ | 目标：测度 $m$ |
|--------|----------------|----------------|
| 定义域 | **所有**集合 | 可测集类 $\mathcal{M}$ |
| 非负、单调 | ✔ | ✔ |
| 可加性 | 次可加（$\leqslant$） | **可数可加（$=$）** |
| 与区间 | $m^{*}I=|I|$ | $mI=|I|$ |

> **核心洞察（§2.1.1）**：外测度 = 集合的最小"包裹成本"：用可数个开区间从外部覆盖，取所有覆盖体积的下确界。它对一切集合都有定义，代价是只有次可加性。两个例子定调：可数集（哪怕稠密）测度为零；区间测度等于长度（有限覆盖定理是 $\geqslant$ 方向的真正功臣）。接下来的全部工作，就是把这枚"上界"修成"真值"。

### §2.1.2 Lebesgue 可测集

**来龙：从"哪些集合应该可测"反推判据**

我们不知道 $\mathcal{M}$ 里有什么，但有三件事是**必须**的：

1. $\mathcal{M}$ 对可数并、交、余、差封闭（否则测度没法做运算）；
2. $\mathcal{M}$ 包含一切开区间（正则性要求）；
3. 在 $\mathcal{M}$ 上，可数可加成立。

从这三条**反推**：设 $E\in\mathcal{M}$。任取开区间 $I$，*因为* $I,E\in\mathcal{M}$ 且 $\mathcal{M}$ 封闭，所以 $I\cap E,\ I\cap E^c\in\mathcal{M}$；又 *因为* $I=(I\cap E)\cup(I\cap E^c)$ 是**不相交**并，可加性给出

$$m^{*}I=m^{*}(I\cap E)+m^{*}(I\cap E^c). \tag{2}$$

**反过来**，若存在某个开区间 $I$ 使 (2) 式不成立，$E$ 就**不配**进 $\mathcal{M}$。

> **追问**：为什么直觉上是"$E$ 把 $I$ 切成两半，两半外测度相加恰好等于 $I$ 的测度"？因为可测集应当是一把"不渗漏的刀"——它切任何集合都不损耗外测度。

**引理：从"所有开区间"升级到"所有测试集"**

**引理** 设 $E\subset\mathbb{R}^n$。则 (2) 式对**任何开区间 $I$** 都成立 $\iff$ 对**任何点集 $T$** 都有

$$m^{*}T=m^{*}(T\cap E)+m^{*}(T\cap E^c). \tag{3}$$

**证明（必要性方向，全程推导）**

- **充分性**：取 $T=I$ 即得，平凡。
- **必要性**：设 (2) 对所有开区间成立。任取点集 $T$ 与 $\varepsilon>0$。
  - *因为* $m^{*}T$ 是下确界，存在开区间列 $\{I_i\}$ 使 $T\subset\bigcup_i I_i$ 且 $\sum_i |I_i|\leqslant m^{*}T+\varepsilon$。（下确界翻译，同 §2.1.1。）
  - *因为* $T\cap E\subset \bigcup_i (I_i\cap E)$，$T\cap E^c\subset \bigcup_i(I_i\cap E^c)$，由次可加性与单调性：
    $$m^{*}(T\cap E)\leqslant\sum_i m^{*}(I_i\cap E),\qquad m^{*}(T\cap E^c)\leqslant\sum_i m^{*}(I_i\cap E^c).$$
  - 两式相加，*因为* 每个 $I_i$ 满足 (2)：
    $$\begin{aligned}
    m^{*}(T\cap E)+m^{*}(T\cap E^c)
    &\leqslant \sum_i\Big[m^{*}(I_i\cap E)+m^{*}(I_i\cap E^c)\Big]\\
    &=\sum_i |I_i|\leqslant m^{*}T+\varepsilon.
    \end{aligned}$$
  - 令 $\varepsilon\to0$（$\varepsilon$ 任意），得 $m^{*}(T\cap E)+m^{*}(T\cap E^c)\leqslant m^{*}T$。
  - **反向** *因为* $T=(T\cap E)\cup(T\cap E^c)$，由次可加性：$m^{*}T\leqslant m^{*}(T\cap E)+m^{*}(T\cap E^c)$。
  - 双向夹逼，得 (3)。$\square$

> **这步为什么漂亮**：它把"对所有集合成立"这个吓人的要求，降级为"对所有开区间成立"——开区间是一类体积已知、结构清楚的集合。这就是"测试集"思想的第一次胜利。

**定义：Carathéodory 条件**

> **定义（$L$ 可测集）** 设 $E\subset\mathbb{R}^n$。若对**任意**点集 $T$（读作"测试集"），
> $$m^{*}T=m^{*}(T\cap E)+m^{*}(T\cap E^c),$$
> 则称 $E$ 是 **$L$ 可测的**（勒贝格可测）。此时把 $m^{*}E$ 改记为 $mE$，称为 $E$ 的 **$L$ 测度**。$L$ 可测集全体记为 $\mathcal{M}$。

**逐字拆解**：

- $T\cap E$：测试集落在 $E$ 里的部分；
- $T\cap E^c$：测试集落在 $E$ 外（$E^c$ 读作"$E$ 的补集"）的部分；
- 等式说：**$E$ 切任何 $T$，两半外测度之和 = 原外测度，不损耗、不虚增**。
- 注意反向不等式 $m^{*}T\leqslant m^{*}(T\cap E)+m^{*}(T\cap E^c)$ 由次可加性**永远**成立，所以验证可测性时只需证 $\geqslant$ 方向。

**正例（立即检验）**：$E=\varnothing$、$E=\mathbb{R}^n$ 都满足条件（请自验：$T\cap\varnothing=\varnothing$，$T\cap\varnothing^c=T$）。区间可测稍后由"零测集与区间"一段给出。

**反例预告（不剧透）**：本段末尾的 Vitali 集 $Z$ 不满足该条件——存在测试集 $T$ 使等式失效。所以 Carathéodory 条件不是空话：它真的会淘汰一些集合。

**定理 1：可测性的"分离形式"（更顺手的等价刻画）**

**定理 1** $E$ 可测 $\iff$ 对任意 $A\subset E,\ B\subset E^c$，总有

$$m^{*}(A\cup B)=m^{*}A+m^{*}B.$$

**证明**：

- $(\Rightarrow)$ 取测试集 $T=A\cup B$。*因为* $T\cap E=A$、$T\cap E^c=B$，代入 (3) 即得。
- $(\Leftarrow)$ 对任意 $T$，令 $A=T\cap E\subset E$，$B=T\cap E^c\subset E^c$。*因为* $A\cup B=T$，由假设得 (3)。

**直觉**：Carathéodory 条件说"$E$ 切 $T$ 不损耗"；分离形式说"$E$ 内任取一份、$E$ 外任取一份，两份合起来的外测度就是各自之和"——即 $E$ 内部与外部**互不干扰**。这个形式在定理 3、6 的证明里反复使用，务必熟练。

**封闭性：可测集能放心做集合运算（定理 2–5）**

**定理 2（补集封闭）** $S$ 可测 $\iff$ $S^c$ 可测。
*因为*条件 (3) 中 $E$ 与 $E^c$ 位置完全对称，交换即得。

**定理 3（并封闭 + 不交可加）** 设 $S_1,S_2$ 可测，则 $S_1\cup S_2$ 可测；且若 $S_1\cap S_2=\varnothing$，对任意 $T$ 有

$$m^{*}\big[T\cap(S_1\cup S_2)\big]=m^{*}(T\cap S_1)+m^{*}(T\cap S_2).$$

**证明思路（两次"切割"）**：要证 (3) 对 $S_1\cup S_2$ 成立，即

$$m^{*}T=m^{*}\big[T\cap(S_1\cup S_2)\big]+m^{*}\big[T\cap(S_1\cup S_2)^c\big].$$

- *因为* $S_1$ 可测：$m^{*}T=m^{*}(T\cap S_1)+m^{*}(T\cap S_1^c)$；
- 对第二项再用 $S_2$ 可测：$m^{*}(T\cap S_1^c)=m^{*}(T\cap S_1^c\cap S_2)+m^{*}(T\cap S_1^c\cap S_2^c)$；
- 代入得三项之和。由德摩根公式 $S_1^c\cap S_2^c=(S_1\cup S_2)^c$，第三项就是目标第二项；
- 前两项合并：$T\cap S_1\subset S_1$ 且 $T\cap S_1^c\cap S_2\subset S_1^c$，由**定理 1（分离形式）**，
  $$m^{*}(T\cap S_1)+m^{*}(T\cap S_1^c\cap S_2)=m^{*}\big[(T\cap S_1)\cup(T\cap S_1^c\cap S_2)\big]=m^{*}\big[T\cap(S_1\cup S_2)\big].$$
  这就是不交并的可加公式；并封闭性随之得证。$\square$

**推论 1** 有限个可测集之并可测；当它们两两不相交时，对任意 $T$：

$$m^{*}\!\left(T\cap\bigcup_{i=1}^{n}S_i\right)=\sum_{i=1}^{n}m^{*}(T\cap S_i).$$

（归纳法，*因为*每次加一个集合用一次定理 3。）

**定理 4（交封闭）** $S_1,S_2$ 可测 $\Rightarrow S_1\cap S_2$ 可测。
*因为* $S_1\cap S_2=(S_1^c\cup S_2^c)^c$，用定理 2、3 与德摩根公式。

**定理 5（差封闭）** $S_1,S_2$ 可测 $\Rightarrow S_1\setminus S_2$（读作"$S_1$ 减 $S_2$"）可测。
*因为* $S_1\setminus S_2=S_1\cap S_2^c$，用定理 2、4。

**定理 6：可数可加性——从"$\leqslant$"到"$=$"的跨越（核心，推导全程）**

**定理 6** 设 $\{S_i\}_{i=1}^{\infty}$ 是一列**互不相交**的可测集，则 $\bigcup_{i=1}^{\infty}S_i$ 可测，且

$$m\!\left(\bigcup_{i=1}^{\infty}S_i\right)=\sum_{i=1}^{\infty}mS_i. \tag{7}$$

> 这是全章的心脏。它一次性兑现两件事：可测集对**可数并**封闭；外测度限制在可测集上**真正可数可加**。

**证明（分两半）**

**第一半：先证 $\bigcup_i S_i$ 可测。** 任取测试集 $T$。*因为*推论 1 给出有限并 $\bigcup_{i=1}^{n}S_i$ 可测，故

$$\begin{aligned}
m^{*}T&=m^{*}\!\left[T\cap\bigcup_{i=1}^{n}S_i\right]+m^{*}\!\left[T\cap\left(\bigcup_{i=1}^{n}S_i\right)^c\right]\\
&\geqslant m^{*}\!\left[T\cap\bigcup_{i=1}^{n}S_i\right]+m^{*}\!\left[T\cap\left(\bigcup_{i=1}^{\infty}S_i\right)^c\right].
\end{aligned}$$

第二个 $\geqslant$ *因为* $\left(\bigcup_{i=1}^{n}S_i\right)^c\supset\left(\bigcup_{i=1}^{\infty}S_i\right)^c$，用单调性。
再由推论 1（有限不交可加）：

$$=\sum_{i=1}^{n}m^{*}(T\cap S_i)+m^{*}\!\left[T\cap\left(\bigcup_{i=1}^{\infty}S_i\right)^c\right].$$

令 $n\to\infty$，*因为*左边与 $n$ 无关而右边部分和递增，得

$$m^{*}T\geqslant \sum_{i=1}^{\infty}m^{*}(T\cap S_i)+m^{*}\!\left[T\cap\left(\bigcup_{i=1}^{\infty}S_i\right)^c\right].$$

*因为* $\bigcup_i(T\cap S_i)=T\cap\bigcup_i S_i$，由次可加性 $\sum_i m^{*}(T\cap S_i)\geqslant m^{*}(T\cap\bigcup_i S_i)$，故

$$m^{*}T\geqslant m^{*}\!\left[T\cap\bigcup_{i=1}^{\infty}S_i\right]+m^{*}\!\left[T\cap\left(\bigcup_{i=1}^{\infty}S_i\right)^c\right].$$

反向 $\leqslant$ 由次可加性恒成立。于是 $\bigcup_i S_i$ 可测。

**第二半：证 (7)。** 在第一半的不等式中取特殊测试集 $T=\bigcup_{i=1}^{\infty}S_i$。*因为* $T\cap S_i=S_i$ 且 $T\cap(\bigcup_i S_i)^c=\varnothing$，得

$$m\!\left(\bigcup_{i=1}^{\infty}S_i\right)\geqslant\sum_{i=1}^{\infty}mS_i.$$

反向由外测度次可加性给出 $\leqslant$。双向得 (7)。$\square$

**推论 3（不相交化技巧）** 任意一列可测集 $\{S_i\}$ 的可数并也可测：

$$\bigcup_{i=1}^{\infty}S_i=S_1\cup(S_2\setminus S_1)\cup\big(S_3\setminus(S_1\cup S_2)\big)\cup\cdots$$

*因为*右端各加项两两不相交且都可测（定理 3、5），用定理 6 即得。

> **核心洞察**：证明的精髓是"**先有限，后取极限**"——有限并的好性质来自定理 3，极限步允许 $n\to\infty$ 是因为不等式对每个 $n$ 都成立。这与次可加性的 $\varepsilon$ 技术一样，是实变函数的基本呼吸节奏。

**定理 7：可数交封闭**

**定理 7** 可测集列 $\{S_i\}$ 的可数交 $\bigcap_{i=1}^{\infty}S_i$ 可测。
*因为* $\left(\bigcap_i S_i\right)^c=\bigcup_i S_i^c$（德摩根公式），用定理 2 与推论 3。

**定理 8 与定理 9：测度与极限可交换（核心 + 基础，标准四层）**

**来龙**：积分收敛定理（Levi、Fatou、Lebesgue 控制收敛，见 Ch3 §3.2）全部建立在"测度能穿过极限"这件事上。这里先把集合版的极限定理打好。

**定理 8（递增列的连续性 / 下连续性）** 设 $\{S_n\}$ 递增（$S_1\subset S_2\subset\cdots$），$S=\bigcup_{n=1}^{\infty}S_n=\lim_{n\to\infty}S_n$，则

$$mS=\lim_{n\to\infty}mS_n.$$

**证明（推导全程）**：把 $S$ 写成互不相交的"环形分解"：

$$S=S_1\cup(S_2\setminus S_1)\cup(S_3\setminus S_2)\cup\cdots$$

*因为*各加项可测且互不相交（定理 5），由定理 6：

$$mS=\sum_{i=1}^{\infty}m(S_i\setminus S_{i-1})\quad(S_0=\varnothing)=\lim_{n\to\infty}\sum_{i=1}^{n}m(S_i\setminus S_{i-1})=\lim_{n\to\infty}m\!\left[\bigcup_{i=1}^{n}(S_i\setminus S_{i-1})\right]=\lim_{n\to\infty}mS_n.$$

（最后两步：有限不交可加 + 望远镜求和 $S_n=\bigcup_{i=1}^{n}(S_i\setminus S_{i-1})$。）$\square$

**定理 9（递减列的连续性 / 上连续性）** 设 $\{S_n\}$ 递减（$S_1\supset S_2\supset\cdots$），$S=\bigcap_{n=1}^{\infty}S_n$。**若 $mS_1<\infty$**，则

$$mS=\lim_{n\to\infty}mS_n.$$

**证明**：*因为* $\{S_1\setminus S_n\}$ 是递增列且 $\bigcup_n(S_1\setminus S_n)=S_1\setminus S$，由定理 8：

$$\lim_{n\to\infty}m(S_1\setminus S_n)=m(S_1\setminus S).$$

*因为* $S_n\subset S_1$、$S\subset S_1$ 且 $mS_1<\infty$，减法合法：

$$m(S_1\setminus S_n)=mS_1-mS_n,\qquad m(S_1\setminus S)=mS_1-mS.$$

代入即得 $mS=\lim_n mS_n$。$\square$

**反例（条件 $mS_1<\infty$ 不可少）**：取 $S_n=(n,\infty)$。*因为* $S_1\supset S_2\supset\cdots$ 且 $\bigcap_n S_n=\varnothing$，所以 $mS=0$；但每个 $mS_n=\infty$，故 $\lim_n mS_n=\infty\neq 0$。
**对比**：$S_n=(0,1/n)$ 满足 $mS_1=1<\infty$，$\bigcap_n S_n=\varnothing$，$mS_n=1/n\to0$ 与定理 9 一致——不是"递减到空集"有问题，是"从无穷大往下减"不合法（$\infty-\infty$ 无意义）。

> **多视角**：概率论里，这两个定理就是**概率的连续性**：事件列 $A_n\uparrow A$ 时 $P(A_n)\to P(A)$；$A_n\downarrow A$ 时同样成立（概率测度总有限，所以递减情形无条件）。

**零测度集：外测度为零自动可测**

**定理（零测度集）** (1) 凡 $m^{*}E=0$ 的集合都可测，称为**零测度集**；(2) 零测度集的任何子集仍为零测度集；(3) 有限个或可数个零测度集之并仍为零测度集。

**证明**：

- (1) 任取测试集 $T$。*因为* $T\cap E\subset E$，由单调性 $m^{*}(T\cap E)\leqslant m^{*}E=0$，故 $m^{*}(T\cap E)=0$。于是
  $$m^{*}T\geqslant m^{*}(T\cap E^c)=m^{*}(T\cap E^c)+0=m^{*}(T\cap E^c)+m^{*}(T\cap E),$$
  （第一个 $\geqslant$ 用单调性，$T\cap E^c\subset T$），反向 $\leqslant$ 恒成立，故 $E$ 可测。
- (2) 单调性直接给 $m^{*}A\leqslant m^{*}E=0$。
- (3) 次可加性给出 $m^{*}(\bigcup_i E_i)\leqslant\sum_i m^{*}E_i=0$。$\square$

**快捷键**：以后想证明一个集合可测，只要能说明"它被某个零测集包含"，就赢了。

**区间、开集、闭集都可测**

**定理（锚点兑现）** 区间 $I$（开、闭、半开半闭）可测，且 $mI=|I|$。

**证明思路（$\mathbb{R}$ 情形，演示"测试"怎么做）**：取任一与 $I$ 不同的开区间 $I_0$，要证

$$|I_0|=m^{*}(I_0\cap I)+m^{*}(I_0\cap I^c).$$

*因为* $I_0\cap I$ 是区间（体积已知），而 $I_0\cap I^c$ 至多分解成两个互不相交的区间，其外测度等于长度和，于是左边 $\geqslant$ 右边；反向由次可加性恒成立。再由上面的引理把"所有开区间"升级为"所有 $T$"，即 $I$ 可测。$\mathbb{R}^n$ 同理（$I_0\cap I^c$ 至多 $2n$ 片）。$mI=|I|$ 来自 §2.1.1 例 3。$\square$

**定理** 开集、闭集都可测。
*因为*非空开集 = 可数个互不相交的（左开右闭）区间之并，区间可测 + 可数并封闭 $\Rightarrow$ 开集可测；闭集 = 开集之补，用补集封闭。$\square$

**$\sigma$-代数：把刚才的成果正式命名**

> **定义（$\sigma$-代数，读作"sigma 代数"）** 设 $\Omega$ 是 $\mathbb{R}^n$ 的一些子集组成的集类，满足：
> 1. $\varnothing\in\Omega$；
> 2. $E\in\Omega\Rightarrow E^c\in\Omega$（补封闭）；
> 3. $E_n\in\Omega\ (n=1,2,\dots)\Rightarrow \bigcup_{n=1}^{\infty}E_n\in\Omega$（可数并封闭）。
>
> 则称 $\Omega$ 是 $\mathbb{R}^n$ 的一个 $\sigma$-代数。

**直觉**：$\sigma$-代数 = "做测度论运算不会跑出去"的最小语法环境——补和可数并封闭后，可数交、差也自动封闭（德摩根公式）。**为什么要求可数而不是有限？** 因为测度公理要求可数可加，集合运算也必须配套可数。

**总结句**：由前面的定理 2、6、7，$L$ 可测集全体 $\mathcal{L}$（即 $\mathcal{M}$）是一个 $\sigma$-代数。

**Borel 代数：由开集"生成"的最小 $\sigma$-代数**

**两个生成概念**：

- 任意一族 $\sigma$-代数的交仍是 $\sigma$-代数（逐条验证三条公理）。
- 因此对任意集族 $\Sigma$，"所有包含 $\Sigma$ 的 $\sigma$-代数之交"是**包含 $\Sigma$ 的最小 $\sigma$-代数**，称为**由 $\Sigma$ 生成的 $\sigma$-代数**。

> **定义（Borel 代数）** 由 $\mathbb{R}^n$ 中全体**开集**生成的 $\sigma$-代数记为 $\mathcal{B}$（读作"$B$"或"Borel 代数"），其元素称为 **Borel 集**（博雷尔集）。

**定理** $\mathcal{B}\subset\mathcal{L}$：一切 Borel 集都是 $L$ 可测的。
*因为*开集可测，而 $\mathcal{L}$ 是包含全体开集的 $\sigma$-代数，故最小者 $\mathcal{B}\subset\mathcal{L}$。

**对比（易混）**：

| | Borel 集类 $\mathcal{B}$ | Lebesgue 可测集类 $\mathcal{L}$ |
|---|---|---|
| 来源 | 开集经**可数**次交并余差生成 | Carathéodory 条件筛选 |
| 零测集的任意子集 | **不**一定在里面 | 一定在里面 |
| 大小 | 基数 $\mathfrak{c}$ | 基数 $2^{\mathfrak{c}}$（更大，见结构定理） |
| 用途 | 概率论事件域的标准选择 | 积分论/分析的标准选择 |

**$G_\delta$ 与 $F_\sigma$：两类最常用的 Borel 集**

> **定义** $G_\delta$ 型集 = 可数个开集之交（$\delta$ 取自德语 Durchschnitt，"交"）；$F_\sigma$ 型集 = 可数个闭集之并（$\sigma$ 取自法语 somme，"和"；$F$ 取自法语 fermé，"闭"）。

**例子**：

- $\mathbb{Q}$ 是 $F_\sigma$ 集：*因为* $\mathbb{Q}=\bigcup_{r\in\mathbb{Q}}\{r\}$ 是可数个单点闭集之并。
- 无理数集 $\mathbb{R}\setminus\mathbb{Q}$ 是 $G_\delta$ 集：*因为* $\mathbb{R}\setminus\mathbb{Q}=\bigcap_{r\in\mathbb{Q}}(\mathbb{R}\setminus\{r\})$，每个 $\mathbb{R}\setminus\{r\}$ 是开集。

$G_\delta$、$F_\sigma$ 都是 Borel 集（开闭的可数运算），故都可测。

**结构定理：可测集 = Borel 集 ± 零测集（核心 + 进阶，证明全程）**

**悬念**：$\mathcal{L}$ 比 $\mathcal{B}$ 多出来的集合长什么样？答案是——**只多出"零测度的边角料"**。

**定理** 设 $E$ 可测，则存在 $G_\delta$ 型集 $G\supset E$，使 $m(G\setminus E)=0$。

**证明（两步）**

**Step 1（先做到"开集逼近到 $\varepsilon$"）**：任给 $\varepsilon>0$，存在开集 $G\supset E$ 使 $m(G\setminus E)<\varepsilon$。

- 情形 $mE<\infty$：*因为* $mE$ 是外测度（可测集上 $m=m^{*}$），由定义存在开区间列 $\{I_i\}$ 覆盖 $E$ 且 $\sum_i|I_i|<mE+\varepsilon$。令 $G=\bigcup_i I_i$（开集），*因为* $E\subset G$ 且
  $$mE\leqslant mG\leqslant\sum_i mI_i=\sum_i|I_i|<mE+\varepsilon,$$
  故 $m(G\setminus E)=mG-mE<\varepsilon$（这里 $mE<\infty$ 保证减法合法）。
- 情形 $mE=\infty$：把 $E$ 分解为可数多个互不相交**有界**可测集之并 $E=\bigcup_n E_n$（$mE_n<\infty$）。对每个 $E_n$ 用上一段，得开集 $G_n\supset E_n$ 使 $m(G_n\setminus E_n)<\varepsilon/2^n$。令 $G=\bigcup_n G_n$。*因为*
  $$G\setminus E=\bigcup_n G_n\setminus\bigcup_n E_n\subset\bigcup_n(G_n\setminus E_n),$$
  由次可加性，$m(G\setminus E)\leqslant\sum_n m(G_n\setminus E_n)<\varepsilon$。（$\varepsilon/2^n$ 技巧第三次出场。）

**Step 2（把 $\varepsilon$ 收成 0）**：对 $\varepsilon_n=1/n$ 依次取开集 $G_n\supset E$ 使 $m(G_n\setminus E)<1/n$。令

$$G=\bigcap_{n=1}^{\infty}G_n.$$

*因为*可数个开集之交，$G$ 是 $G_\delta$ 型集，$G\supset E$；且对每个 $n$，$m(G\setminus E)\leqslant m(G_n\setminus E)<1/n$，令 $n\to\infty$ 得 $m(G\setminus E)=0$。$\square$

**定理（对偶形式）** 设 $E$ 可测，则存在 $F_\sigma$ 型集 $F\subset E$，使 $m(E\setminus F)=0$。
**证明**：对 $E^c$ 用上一定理，得 $G_\delta$ 型集 $G\supset E^c$ 使 $m(G\setminus E^c)=0$。令 $F=G^c$。*因为* $G^c$ 是可数个闭集之并，$F$ 是 $F_\sigma$ 型集；$F\subset E$ 且

$$m(E\setminus F)=m(E\setminus G^c)=m(E\cap G)=m(G\setminus E^c)=0.\ \square$$

**全景公式**：任意可测集 $E$ 可写成

$$E=G\setminus M=F\cup N,\qquad G\in G_\delta,\ F\in F_\sigma,\ m(M)=m(N)=0.$$

**读法**：可测集 = Borel 集 + 零测集的子集（微调）。**推论**：$\mathcal{L}$ 恰好是"Borel 集再塞进所有零测集的子集"所得的 $\sigma$-代数（这叫 $\mathcal{B}$ 的**完备化**）。基数对比也源于此：康托尔集有 $2^{\mathfrak{c}}$ 个子集，且每个都是零测集（故可测），所以 $|\mathcal{L}|=2^{\mathfrak{c}}>|\mathcal{B}|=\mathfrak{c}$——**不可测以外，"几乎所有"子集都是可测的，但能被显式写出来的只有 $\mathfrak{c}$ 个 Borel 集**。

**正则性：测度 = 开集外包的下确界 = 紧集内填的上确界**

**定理** 设 $E$ 可测，则

1. **外正规性**：$mE=\inf\{mG:G\text{ 开集},\ G\supset E\}$；
2. **内正规性**：$mE=\sup\{mK:K\text{ 紧集},\ K\subset E\}$。

**证明概要**：

- (1) 当 $mE=\infty$ 平凡；当 $mE<\infty$，Step 1 已给出：任意 $\varepsilon>0$ 有开集 $G\supset E$ 使 $mG<mE+\varepsilon$，即下确界被 $mE$ 从上下夹住。
- (2) 有界情形：取闭区间 $I\supset E$，对 $I\setminus E$ 用外正规性得开集 $G\supset I\setminus E$ 使 $m(G\setminus(I\setminus E))<\varepsilon$；令 $K=I\setminus G$，则 $K$ 紧、$K\subset E$ 且 $m(E\setminus K)<\varepsilon$。无界情形：用 $E_n=\{x:d(x,0)<n\}\cap E$ 截断，*因为* $E_n\uparrow E$ 且每个 $E_n$ 有界，对每个 $E_n$ 取紧集 $K_n$ 逼近后取极限（定理 8）。
- 反之（习题）：有界集 $E$ 若满足"外包下确界 = 内填上确界"，则 $E$ 可测——这就是勒贝格原始定义的等价形式。

**直觉**：这组定理为"内填外包"的动机补上了严谨证明：**Carathéodory 方案与原始内测度方案殊途同归**。

**边界：不可测集（Vitali 构造，1905）**

**悬念收口：Carathéodory 条件到底筛掉了什么？**

前面证明了 $\mathcal{L}$ 对可数运算封闭、装下了所有 Borel 集和零测集。自然要问：**每个集合都可测吗？** 若答案是肯定的，Carathéodory 条件就成了空摆设。Vitali 的回答是：不。并且**不可测集不是病态的边角料，它恰好说明三条勒贝格公理不能同时推广到所有集合**。

构造思路（先看地图，再看细节）：如果能造出一个集合 $Z$，把它平移可数次得到 $\{Z_n\}$，使得

- $1^\circ$ $\bigcup_n Z_n\supset[0,1]$（拼起来够大）；
- $2^\circ$ $Z_n$ 两两不相交，且 $\bigcup_n Z_n\subset[-1,2]$（整体有界）。

那么 $Z$ **必**不可测。*因为*：若 $Z$ 可测，由平移不变性每个 $Z_n$ 可测且 $mZ_n=mZ$；可数可加性给出

$$m\!\left(\bigcup_n Z_n\right)=\sum_{n=1}^{\infty}mZ_n=\sum_{n=1}^{\infty}mZ.$$

又由 $1^\circ,2^\circ$ 与单调性：

$$1=m[0,1]\leqslant m\!\left(\bigcup_n Z_n\right)\leqslant m[-1,2]=3,$$

于是 $\sum_n mZ$ 必须**有限**（从而 $mZ=0$）又必须**大于 $0$**（否则左边为 $0<1$）——矛盾。$\square$

**工具：勒贝格测度的平移不变性**

> **定义** 平移 $\tau_\alpha:\mathbb{R}\to\mathbb{R}$，$\tau_\alpha(x)=x+\alpha$（$\alpha\in\mathbb{R}$）；集合平移 $\tau_\alpha E=\{x+\alpha:x\in E\}$（读作"$E$ 平移 $\alpha$"）。

**定理** 对任何 $E\subset\mathbb{R}$，$m^{*}E=m^{*}(\tau_\alpha E)$；且 $E$ 可测时 $\tau_\alpha E$ 也可测。

**证明**：

- 不变性：*因为* $I_i$ 是开区间 $\Rightarrow\tau_\alpha I_i$ 是等长的开区间，且 $E\subset\bigcup_i I_i\Leftrightarrow\tau_\alpha E\subset\bigcup_i\tau_\alpha I_i$，两类覆盖一一对应、体积和相同，故下确界相同。
- 可测性：任取 $T$，*因为* $\tau_\alpha(T\cap E)=\tau_\alpha T\cap\tau_\alpha E$、$\tau_\alpha(T\cap E^c)=\tau_\alpha T\cap\tau_\alpha E^c$，把 $E$ 的可测条件整体平移：
  $$m^{*}(\tau_\alpha T)=m^{*}(\tau_\alpha T\cap\tau_\alpha E)+m^{*}(\tau_\alpha T\cap\tau_\alpha E^c),$$
  而 $\tau_\alpha T$ 可跑遍所有集合，故 $\tau_\alpha E$ 可测。$\square$

（同理有反射不变性 $mE=m(-E)$——把 $\alpha$ 换成取负号。）

**Vitali 构造（逐段推导）**

**第 1 步：把 $[0,1]$ 按"相差有理数"分类。**
对 $\xi,\eta\in[0,1]$，规定 $\xi\sim\eta\iff \xi-\eta\in\mathbb{Q}$。*因为*这是等价关系（自反：差 $0$；对称：差取负；传递：两个有理差相加），$[0,1]$ 被分成一族**两两不相交**的等价类 $E(\xi)=\{\xi+r:\xi+r\in[0,1],\ r\in\mathbb{Q}\}$。
（两类的交非空 $\Rightarrow$ 它们实际上是同一类：若 $\zeta\in E(\xi)\cap E(\eta)$，则 $\zeta-\xi,\zeta-\eta\in\mathbb{Q}$，故 $\eta-\xi\in\mathbb{Q}$，于是 $E(\xi)=E(\eta)$。）

**第 2 步：每个等价类挑一个代表，组成 $Z$。**
由**选择公理**（AC：对一族两两不相交的非空集合，可以同时从每个集合中挑出一个元素组成新集合），从每个等价类中同时取一个元素，组成集合 $Z\subset[0,1]$。*因为*每类恰好被取一个，所以：

$$\text{对任何 }\xi\in[0,1],\quad E(\xi)\cap Z\ \text{是单元素集}. \tag{★}$$

**第 3 步：平移。** 把 $[-1,1]$ 中的有理数排成一列 $r_1,r_2,\dots$（可数，见 Ch1），令

$$Z_n=\tau_{r_n}Z=Z+r_n,\qquad n=1,2,\dots$$

**第 4 步：验证 $1^\circ$（覆盖 $[0,1]$）。**
任取 $\xi\in[0,1]$，由 (★) 存在唯一的 $\eta\in E(\xi)\cap Z$。*因为* $\xi\sim\eta$，故 $\xi-\eta\in\mathbb{Q}$；又 $\xi,\eta\in[0,1]$，故 $\xi-\eta\in[-1,1]$，于是 $\xi-\eta=r_k$ 是枚举列中的某一项。*因为* $\xi=\eta+r_k\in Z+r_k=Z_k$，所以 $\xi\in\bigcup_n Z_n$。由 $\xi$ 任意，

$$[0,1]\subset\bigcup_{n=1}^{\infty}Z_n.$$

**第 5 步：验证 $2^\circ$（两两不交 + 有界）。**

- 不交：若 $\xi\in Z_l\cap Z_n$ 且 $l\neq n$，则 $\xi-r_l,\xi-r_n\in Z$。*因为* $(\xi-r_l)-(\xi-r_n)=r_n-r_l\in\mathbb{Q}$，这两点属于**同一等价类**；又 $r_l\neq r_n$ 故 $\xi-r_l\neq\xi-r_n$ 是同一类中**两个不同**元素——与 (★)（每类只取一个代表）矛盾。
- 有界：*因为* $Z\subset[0,1]$ 且 $r_n\in[-1,1]$，所以 $Z_n\subset[-1,2]$，故 $\bigcup_n Z_n\subset[-1,2]$。

**第 6 步：结论。** 由上面的判定引理，$Z$ 不可测。$\square$

**后果与高层视角**

1. **不可测集到处都是**：把 $[0,1]$ 换成任何正测度集 $E$ 重做构造，得 $E$ 中也有不可测子集。所以不可测集不是孤例。
2. **四条愿望不可兼得**：在 $\mathbb{R}$ 上不存在同时满足——任何子集可测、$m[0,1]=1$、可数可加、运动不变——的测度。要"所有集合都有大小"，就必须放弃至少一条。
3. **Banach（1923）的退让**：只要求**有限可加**，则在 $\mathbb{R}$、$\mathbb{R}^2$ 上存在定义于一切子集、正则且运动不变的 Banach 测度——但有限可加测度做不了极限定理，用处不大（$\mathbb{R}^3$ 以上连这也做不到，Banach–Tarski）。
4. **不可数可加更不行**：若允许不可数可加，则 $E=\bigcup_{x\in E}\{x\}$ 使一切集合测度归零。
5. **高层视角**：不可测集的构造真正用到的"非构造"一步只有**选择公理**。Solovay（1970）证明：在 ZF + 依赖选择（DC）下，若存在不可达基数，可以有一个模型使**实数的一切子集都 Lebesgue 可测**。所以"不可测集存在"不是集合论的必然，而是"AC + 三条测度公理"的共同后果——这正说明 Carathéodory 条件是公理体系里最省事的那条边界。

**易错点清单（先看再做题）**

1. Carathéodory 条件中的 $T$ 是**任意**点集，不是"任意开区间"。两者等价是引理的**结论**，别把结论当定义用。
2. 验证可测性只需证 $\geqslant$ 方向——反向恒成立，但写证明时请把双向都说清。
3. 定理 6 的并集要求**互不相交**才给等式；任意可数并的可测性靠推论 3 的不相交化，不靠定理 6 直接给等式。
4. 定理 9 忘掉 $mS_1<\infty$ 是本节最高频错误；$(n,\infty)$ 反例必须能默写。
5. "$m^{*}E=0\Rightarrow E$ 可测"——外测度为零自动可测，这是很多"零测集论证"的快捷键。

> **核心洞察（§2.1.2）**：Carathéodory 条件 = 只用外测度自举出可测集类：$E$ 可测当且仅当它切任何测试集 $T$ 都"不损耗"外测度。从这一个条件出发，补、并、交、差、可数并、可数交全部封闭，且外测度在可测集上兑现了可数可加性（定理 6）与极限连续性（定理 8/9）。可测集类的画像出奇地干净——**区间可测是锚点，开闭可测是扩散，结构定理给出终极公式：可测集 = Borel 集 ± 零测集。** 换句话说，Carathéodory 条件筛出来的 $\mathcal{L}$，比 $\mathcal{B}$ 多出的全部东西就是"零测度的边角料"。**一句话：外测度给"大小"一个上界，Carathéodory 条件挑出"上界即真值"的集合。**

```
零测度集
区间 ──► 开集 ──► 闭集
              │
              ▼
        Borel 代数 B（由开集生成的最小 σ-代数）
              │  + 所有零测度集的子集
              ▼
     Lebesgue σ-代数 L = { G∖M : G∈Gδ, M 零测 } = { F∪N : F∈Fσ, N 零测 }
              │
              ▼
     正则性：mE = inf 开集外包 = sup 紧集内填
              │
              ▼
     Vitali 构造：确有不可测集——L 无法装下所有集合
```

### §2.1.3 测度空间

**来龙：为什么要把 Lebesgue 测度"抽象化"**

Lebesgue 测度的性质中，"零测集的子集可测""可数并封闭""可数可加"这几条是**最基本的**。这就启发我们：若把这些性质直接作为基本假设引进某种**抽象测度**，则它将自动具有一系列与 Lebesgue 测度相似的性质，从而把测度论的应用范围从 $\mathbb{R}^n$ 拓广到任意集合 $X$（概率空间、函数空间、离散空间……）。这一步是本节唯一从郭版教材新写补缺的部分。

**定义：$\sigma$ 代数与可测空间**

> **定义（可测空间）** 设 $X$ 是一个非空集，$\mathcal{F}\subset 2^X$ 是 $X$ 的一个 $\sigma$ 代数（$2^X$ 读作"$X$ 的幂集"，即 $X$ 的一切子集组成的集类），则称 $(X,\mathcal{F})$ 为一个**可测空间**；每个集合 $A\in\mathcal{F}$ 称为 **$\mathcal{F}$ 可测集**，或简称为可测集。

**定义：测度与测度空间**

> **定义（测度与测度空间）** 设 $(X,\mathcal{F})$ 是可测空间。若集函数 $\mu:\mathcal{F}\to[0,\infty]$（$\mu$ 读作"测度"）满足：
> (1) $\mu(\varnothing)=0$；
> (2) 若 $A_n\in\mathcal{F},\ n=1,2,\dots$ 互不相交，有
> $$\mu\biggl(\bigcup_{n}A_n\biggr)=\sum_{n}\mu(A_n),$$
> 则称 $\mu$ 为 $(X,\mathcal{F})$ 上的一个**测度**，称三元组 $(X,\mathcal{F},\mu)$ 为**测度空间**。性质 (2) 称为测度的 **$\sigma$ 可加性**（即前面反复使用的"可数可加性"）。

**完备测度与完备化**

> **定义（完备测度）** 若还假定测度 $\mu$ 满足条件：
> $$\text{若 } B\subset A\in\mathcal{F},\ \mu(A)=0,\ \text{则 } B\in\mathcal{F},$$
> 则称 $\mu$ 是**完备测度**，$(X,\mathcal{F},\mu)$ 是**完备测度空间**。

**为什么"完备"值得单独命名？** 因为它对应一个真实的技术需求：在 $\mathbb{R}^n$ 中，$(\mathbb{R}^n,\mathcal{B},m)$（Borel 集 + Lebesgue 测度）**不是**完备的——康托尔三分集 $C$ 是 Borel 集且 $mC=0$，但 $C$ 有 $2^{\mathfrak{c}}$ 个子集，其中绝大多数**不是** Borel 集（$\mathcal{B}$ 只有 $\mathfrak{c}$ 个元素）。而 $(\mathbb{R}^n,\mathcal{L},m)$（Lebesgue 可测集 + Lebesgue 测度）是完备的——这正是上一段结构定理的推论：$\mathcal{L}=\mathcal{B}$ 再塞进所有零测集的子集。把不完备的测度空间补成完备的，这个操作就叫**完备化**。

**Lebesgue 测度的定位**：由结构定理，$(\mathbb{R}^n,\mathcal{L},m)$ 就是 $(\mathbb{R}^n,\mathcal{B},m)$ 的完备化。

**其他基本概念：有限测度、概率测度、$\sigma$ 有限测度**

设 $(X,\mathcal{F},\mu)$ 是测度空间。

- 若 $\mu(X)<\infty$，称 $\mu$ 为**有限测度**；
- 若 $\mu(X)=1$，则称 $\mu$ 为**概率测度**，$(X,\mathcal{F},\mu)$ 称为**概率测度空间**；
- 对集合 $A\in\mathcal{F}$，若存在 $A_n\in\mathcal{F},\ n=1,2,\cdots$，使得 $A=\bigcup_{n}A_n,\ \mu(A_n)<\infty$，则称 $A$ 具有 **$\sigma$ 有限测度**；若 $X$ 本身具有 $\sigma$ 有限测度，则称 $\mu$ 为 **$\sigma$ 有限测度**。

**测度的例子（例题）**

**例 1** Lebesgue 测度 $m$ 是 $(\mathbb{R}^n,\mathfrak{M})$ 上的一个 $\sigma$ 有限测度（$\mathfrak{M}$ 即前面记作 $\mathcal{L}$ 的 Lebesgue 可测集类）。
*因为*：把 $\mathbb{R}^n$ 写成可数个有界可测集之并（例如以原点为中心、边长 $2k$ 的开方体之并），每个的测度有限。

**例 2（Gauss 测度）** 在 $(\mathbb{R}^n,\mathfrak{M})$ 上引入

$$p(A)=\frac{1}{(2\pi)^{\frac{n}{2}}}\int_A \mathrm{e}^{-\frac{1}{2}\sum_{j=1}^{n}x_j^2}\,\mathrm{d}x_1\mathrm{d}x_2\cdots \mathrm{d}x_n,$$

易见 $p$ 是 $(\mathbb{R}^n,\mathfrak{M})$ 上一个**概率测度**（即多元标准正态分布）。

**例 3（计数测度）** 设 $X$ 是一个非空集，取 $\sigma$ 代数 $\mathcal{F}=2^{X}$。对任意有限集 $A\in\mathcal{F}$ 令 $\mu(A)=|A|$（$|A|$ 读作"$A$ 的元素个数"）；对任意无限集 $A\subset X$ 令 $\mu(A)=\infty$。则 $\mu$ 满足测度定义的两条，称为 $X$ 上的**计数测度**。
*因为* $\mu(A)=0\iff A=\varnothing$，所以 $\mu$ 是 $X$ 上的**完备**测度。易见 $\mu$ 是 $\sigma$ 有限测度 $\iff$ $X$ 是可数集。

**例 4（Dirac 测度）** 设 $X$ 是一个非空集，任意取定元素 $x\in X$，对任意集合 $A\subset X$ 定义 $\nu(A)=\chi_A(x)$（$\chi_A$ 读作"$A$ 的特征函数"，在 $A$ 上取值 $1$、在 $A$ 外取值 $0$）。则容易验证 $\nu$ 是 $X$ 上的一个**完备概率测度**，称为元 $x$ 处的 **Dirac 测度**，记作 $\delta_x$。

**例 5（测度的线性组合）** 设 $\mu_n$ 是 $(X,\mathcal{F})$ 上的测度，$a_n\in[0,\infty)$，$n=1,2,\cdots$。对任意集合 $A\in\mathcal{F}$ 令 $\mu(A)=\sum_n a_n\mu_n(A)$，则易见 $\mu$ 也是 $(X,\mathcal{F})$ 上的一个测度，记作 $\mu=\sum_n a_n\mu_n$。
例如，若以 $\delta_n$ 记 $\mathbb{N}$ 上点 $n$ 处的 Dirac 测度，则 $\mu=\sum_{n=1}^{\infty}\delta_n$ 恰是 $\mathbb{N}$ 上的**计数测度**。

**例 6（测度的搬运：像测度）** 设 $(X,\mathcal{F},\mu)$ 是一个测度空间，$f:X\to Y$ 是一个一一满映射。令 $\mathcal{G}=\{f(A)\mid A\in\mathcal{F}\}$，又对每个 $B\in\mathcal{G}$ 定义 $\nu(B)=\mu(f^{-1}(B))$，则显然三元组 $(Y,\mathcal{G},\nu)$ 是一个测度空间。
例如取 $X=[0,2\pi)$、$\mu$ 是 $X$ 上的 Lebesgue 测度 $m$，令 $Y=\{z\in\mathbb{C}\mid |z|=1\}$，则

$$f:X\to Y,\quad a\mapsto \mathrm{e}^{\mathrm{i}a}$$

是一一满映射。于是 $Y$ 上有测度 $\nu(B)=m(f^{-1}(B))$，它是圆周 $Y$ 上**弧长概念**的推广。

**测度空间上的四条基本性质（定理 2.1.13）**

**定理** 设 $(X,\mathcal{F},\mu)$ 是一个测度空间，则测度 $\mu$ 具有以下性质：

1. **单调性**：若 $A_1\subset A_2$，则 $\mu(A_1)\leqslant \mu(A_2)$；
2. **次可加性**：$\mu\!\left(\bigcup_{k=1}^{\infty}A_k\right)\leqslant \sum_{k=1}^{\infty}\mu(A_k)$；
3. **上连续性**：若 $\{A_n\}\subset\mathcal{F}$ 是一升列，则
   $$\mu\!\left(\bigcup_{n=1}^{\infty}A_n\right)=\lim_{n\to\infty}\mu(A_n);$$
4. **下连续性**：若 $\{A_n\}\subset\mathcal{F}$ 是一降列，且 $\mu(A_1)<\infty$，则
   $$\mu\!\left(\bigcap_{n=1}^{\infty}A_n\right)=\lim_{n\to\infty}\mu(A_n).$$

**读法对照**：这四条与前面 Lebesgue 测度的定理 8/9 一字不差——**这正是抽象化的收益**：在 $(\mathbb{R}^n,\mathcal{L},m)$ 里辛辛苦苦证明的结论，一旦作为公理写进定义，就在一切测度空间上自动成立，不必重证。

**反例（完备性不可省）**：取 $X=[0,1]$、$\mathcal{F}=\mathcal{B}$（Borel 集）、$\mu=m$（Lebesgue 测度）。令 $A=C$（康托尔三分集），则 $A\in\mathcal{B}$ 且 $\mu(A)=0$。取 Vitali 集的构造思想在 $C$ 上重做（或用 $C$ 到 $2^{\mathbb{N}}$ 的一一对应），可得 $C$ 的子集 $B\notin\mathcal{B}$。*因为* $B\subset A$ 且 $\mu(A)=0$，但 $B\notin\mathcal{F}$——所以 $(\mathbb{R},\mathcal{B},m)$ **不是**完备测度空间。
**对比**：同一个集合 $B$ 在 $(\mathbb{R},\mathcal{L},m)$ 中属于 $\mathcal{F}$（结构定理：零测集的子集仍可测）。**差别只在 $\sigma$ 代数选得够不够大**，不在测度本身。

> **对比（长度公理 → 测度公理）**：本章开头的三条"长度公理"在这里被升级为**测度三公理**：定义域是 $\sigma$-代数、$\mu(\varnothing)=0$、可数可加。长度公理是经验直觉，测度公理是可检验的数学对象。

> **核心洞察（§2.1.3）**：测度空间 $(X,\mathcal{F},\mu)$ 是本节全部成果的"封装形式"。它把"集合 + 可做可数运算的集类 + 可数可加的赋值"三件套抽象出来，于是同一个定理可以同时讲 Lebesgue 测度、概率、计数测度、Dirac 测度。而"完备化"则是这道封装上唯一的补丁位：不完备的空间可以通过把零测集的子集塞进 $\sigma$ 代数来补全，Lebesgue 测度空间正是 Borel 测度空间的完备化。

## 去脉（学完去哪）

- **当代应用**：
  - **概率论**：Kolmogorov（1933）把概率论翻译成本节语言——测度空间 $(\mathbb{R}^n,\mathcal{B},m)$ ↔ 概率空间 $(\Omega,\mathcal{F},P)$，$P(\Omega)=1$；可测集 ↔ 事件；$\sigma$-代数 ↔ 事件域；可测函数 ↔ 随机变量；a.e. 成立 ↔ 几乎必然（a.s.）；定理 8/9 ↔ 概率的连续性；零测度集 ↔ 零概率事件。
  - **分形与几何测度论**：把外测度定义中的 $|I_i|$ 换成"尺度函数" $\varphi(\operatorname{diam}E_i)$，同一套筛选流程产生 **Hausdorff 测度**——分形维数的定义工具（康托尔集在 $\alpha=\log 2/\log 3$ 处测度跳变）。
  - **Lebesgue–Stieltjes 测度**：把"区间长度 $b-a$"换成"分布函数增量 $g(b)-g(a)$"，得到 L-S 测度——概率论中随机变量分布的严格载体；其一切性质就是复制本节的三性质 + Carathéodory 条件。（郭版未覆盖此部分，补充阅读见 `seed/_extra/程其襄版/Ch6 微分与不定积分`。）
- **跨领域解读**：本节是"**给集合赋权、然后求和取极限**"这一通用范式的原型。凡是需要把"大小/概率/权重"与**可数并**和**极限**和平相处的理论，都是这套框架的应用实例。
- **高层视角**：**外包（外测度）→ 筛选（Carathéodory）→ 结构（Borel ± 零测）** 三步走，是"外定义 → 内筛选 → 得到良定义"的通用数学范式。下一节（见 Sec2.2）的第一位顾客就是函数：**可测函数 = 水平集可测的函数**，其定义直接建立在"$\{f>a\}\in\mathcal{L}$"之上；再往后 Ch3 的三大极限定理（Levi / Fatou / 控制收敛）则直接调用本节的定理 6、8、9。

## 防跳跃

- [ ] 内测度 $m_{*}$ 的完整定义与"内外相等"的证明（教材附录一）——本节只给了动机与结论
- [ ] Carathéodory 条件与"内外测度相等"两种定义的严格等价证明
- [ ] 选择公理（AC）的精确陈述、它与 ZF 的独立性、以及 Vitali 构造中"非构造性"一步的详细辨析
- [ ] 不可测集的存在性是否依赖 AC —— Solovay 模型的细节（不可达基数假设）
- [ ] Borel 分层（Borel hierarchy）与解析集、投影集（描述集合论）
- [ ] Hausdorff 测度与 Hausdorff 维数的完整定义
- [ ] Lebesgue–Stieltjes 测度（郭版未覆盖，见 `_extra/程其襄版/Ch6 微分与不定积分`）
- [ ] 完备化的**一般构造**（把零测集子集统一塞进 $\sigma$ 代数的最小扩张）——郭版 §2.1.3 只给了完备测度的定义与 Lebesgue 测度的定位，一般构造未展开

## 来源与映射

| 本节点内容 | 来源 | 处理 |
|---|---|---|
| 三条长度公理 → 任意无限可加失败（$[0,1]$ 拆成不可数个单点）→ 只保留可数可加 → 有理数集测度必为 0 → 无理数集测度为 1 | 旧《Ch3 测度论》§1.1、§1.2 | 原文迁移（完整推演链保留） |
| 中心问题与本章路线、内填外包法与 Carathéodory 的简化、全章全景图 | 旧《Ch3 测度论》§1.3、§1.4、§1.5 | 原文迁移 |
| 为什么需要测度（三条需求：黎曼积分失败 / a.e. 无定义 / 概率公理化） | 旧《Ch3 测度论》「引言」 | 提炼迁移（并入「来龙」） |
| 前置知识补给站（可数集、下确界、开集构造定理、Heine–Borel、康托尔集、选择公理） | 旧《Ch3 测度论》「二、前置知识补给站」 | 拆散并入正文各处（避免与 Ch1 重复） |
| 外测度的三个设计决策、定义、三条基本性质（含 $\varepsilon/2^n$ 全程推导） | 旧《Ch3 测度论》§3.1–§3.3 | 原文迁移 |
| 三个定调例子（$\mathbb{Q}$ 零测 / 康托尔集零测 / $m^{*}I=\|I\|$） | 旧《Ch3 测度论》§3.4 | 原文迁移 |
| 反例与缺陷：外测度只有次可加 | 旧《Ch3 测度论》§3.5 | 原文迁移 |
| Carathéodory 条件的动机（三条必备性质反推）、引理（开区间 → 任意测试集）、定义、定理 1 分离形式 | 旧《Ch3 测度论》§4.1–§4.4 | 原文迁移 |
| 定理 2–5（补/并/交/差封闭）、推论 1、定理 6（可数可加，全程推导）、推论 3（不相交化）、定理 7 | 旧《Ch3 测度论》§4.5–§4.7 | 原文迁移 |
| 定理 8/9（测度与极限交换）+ 反例 $(n,\infty)$、易错点清单 | 旧《Ch3 测度论》§4.8、§4.9 | 原文迁移 |
| 零测度集、区间/开集/闭集可测、$\sigma$-代数、Borel 代数、$G_\delta$/$F_\sigma$、结构定理、正则性 | 旧《Ch3 测度论》§5.1–§5.7 | 原文迁移 |
| 测度、测度空间的定义（与 $\sigma$-代数一起） | 旧《Ch3 测度论》§5.3 | 原文迁移 |
| Vitali 不可测集的完整构造（6 步）、平移不变性、后果与高层视角 | 旧《Ch3 测度论》§6.1–§6.5 | 原文迁移 |
| 去脉：可测函数 / 积分 / 概率论 / $L^p$ / 抽象测度与分形 | 旧《Ch3 测度论》§7.1–§7.6 | 提炼迁移（跨章引用改写为纯文本） |
| 抽象测度空间 $(X,\mathcal{F},\mu)$ 的定义、完备测度与完备化、有限/概率/$\sigma$ 有限测度 | 郭版教材 §2.1.3（定义 2.1.12） | 新写补缺 |
| 测度的例子（Lebesgue / Gauss / 计数 / Dirac / 线性组合 / 像测度） | 郭版教材 §2.1.3（例 5–例 10） | 新写补缺 |
| 测度空间四条基本性质（单调、次可加、上连续、下连续） | 郭版教材 §2.1.3（定理 2.1.13） | 新写补缺 |
| 完备性反例（$(\mathbb{R},\mathcal{B},m)$ 不完备） | 旧《Ch3 测度论》§5.6 + 郭版 §2.1.3 | 综合改写 |
| 自测题 Q1–Q5、讲给别人听清单 | 旧《Ch3 测度论》§8.1、§8.2 | 并入正文各处（作为例题/反例/易错点），检验回路留待习题层 |