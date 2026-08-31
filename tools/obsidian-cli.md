# Obsidian CLI 使用指南（跨项目通用）

> 官方命令行工具，Command-line control of Obsidian：<https://obsidian.md/cli>
> 面向 **AI harness / 自动化脚本 / 高级用户**；不绑定具体项目——任何依赖 Obsidian vault 的项目可直接复制或链接本文。
> 本文所有命令均在 **Windows 11 + Git Bash + Obsidian 1.13.7（installer 1.12.7）** 实测通过（2026-08-29）。
> 本仓库内的用法唯一来源（M5）：其他文件只引用，不复制命令细节。

## 1. 前置条件

1. 安装 **Obsidian 桌面端 1.12.7+**（installer 版本）；
2. 开启 CLI：**Settings → About → Command line interface**，按提示注册后**重启终端**；
3. 验证：

```bash
obsidian help      # 输出命令全表即成功（stderr 里可能有无害的 libpng warning，见 §5）
obsidian version   # 如：1.13.7 (installer 1.12.7)
```

> Obsidian 桌面端需处于运行状态；若未运行，第一条命令会自动启动它。

## 2. 核心概念（先读，避免踩坑）

| 概念 | 说明 |
|------|------|
| vault | Obsidian 以 vault 为单位管理；一台机器可有多个 vault，用 `obsidian vaults verbose` 列出全部 |
| 多 vault 环境 | 只要机器上有多个 vault，**所有命令必须显式 `vault=<名称>`**，否则读写会打到当前 active vault，极易写错库 |
| 文件定位 | `file=<名称>`：按 wikilink 语义按名称解析（可省 .md）；`path=<folder/note.md>`：精确路径。**自动化一律用 `path=`**，不依赖索引、不怕重名 |
| 引号 | 含空格的值必须加引号：`name="My Note"` |
| 转义 | `content=` 值中 **`\n` = 换行，`\t` = 制表符**（字面量，由 CLI 还原为真实字符） |
| active file 缺省 | 大部分命令省略 file/path 时作用于"当前打开的文件"——自动化不要依赖缺省，永远显式指定目标 |

命令基本形式：

```
obsidian <command> [options]     # 选项形如 key=value；vault=<名称> 可加在任意命令上
obsidian help <command>          # 查看单条命令的完整选项
```

## 3. 命令速查（按自动化场景分组）

### 3.1 读取 / 查询

| 命令 | 作用 | 示例 |
|------|------|------|
| `read` | 读文件内容 | `obsidian read vault=V path="folder/note.md"` |
| `file` | 文件元信息（path/name/size/created/modified） | `obsidian file vault=V path="folder/note.md"` |
| `files` | 列文件 | `obsidian files vault=V folder="assets/xxx"` |
| `folders` | 列目录 | `obsidian folders vault=V` |
| `search` | 全文搜索（返回命中文件路径） | `obsidian search vault=V query="关键词" path="folder" limit=10` |
| `search:context` | 搜索并带命中行上下文 | `obsidian search:context vault=V query="关键词"` |
| `links` | 列出文件的**出链**（解析到目标路径） | `obsidian links vault=V path="folder/note.md"` |
| `backlinks` | 列出文件的**入链** | `obsidian backlinks vault=V path="folder/note.md" counts` |
| `outline` | 列出文件标题层级 | `obsidian outline vault=V path="folder/note.md" format=tree` |
| `wordcount` | 字数统计 | `obsidian wordcount vault=V path="folder/note.md"` |
| `tags` / `properties` | 列标签 / frontmatter 属性 | `obsidian tags vault=V path="folder/note.md" counts` |
| `recents` | 最近打开的文件 | `obsidian recents vault=V` |

### 3.2 全库体检（图谱质量）

| 命令 | 作用 |
|------|------|
| `unresolved` | **坏链清单**（wikilink 指向不存在的文件）——AI 写完文章必查 |
| `orphans` | 无入链的文章（孤立文章） |
| `deadends` | 无出链的文章 |

```bash
obsidian unresolved vault=V counts   # counts 附计数；verbose 附来源文件
obsidian orphans vault=V
```

### 3.3 写入 / 维护

| 命令 | 作用 | 关键选项 |
|------|------|---------|
| `create` | 新建文件 | `path=`（或 `name=`）、`content=`、`template=`、`overwrite`（已存在时覆盖）、`open` / `newtab`（创建后打开） |
| `append` / `prepend` | 尾插 / 头插内容 | `content=`、`inline`（不追加换行） |
| `move` / `rename` | 移动 / 重命名 | `path=` + `to=` / `name=` |
| `delete` | 删除（默认进系统回收站） | `permanent` 跳过回收站 |
| `property:set` / `property:remove` | 写 / 删 frontmatter 属性 | `name=`、`value=`、`type=text\|list\|number\|checkbox\|date` |

### 3.4 界面 / 日常

`open`（打开文件）、`daily` 与 `daily:append|prepend|read|path`（日记）、`tab:open`、`tabs`、`random`、`bookmarks`、`reload`（重载 vault）、`restart`、`vault`（当前 vault 信息）。

### 3.5 模板

| 命令 | 作用 |
|------|------|
| `templates` | 列出 vault 内模板 |
| `template:read name=<名> resolve title=<标题>` | 读模板内容并解析 `{{...}}` 变量 |
| `template:insert name=<名>` | 向 active file 插入模板 |

### 3.6 高级 / 开发者（谨慎）

`eval`（执行 JS）、`dev:cdp`、`dev:dom`、`dev:screenshot`、`dev:console`、`devtools`——能力强、破坏面大，自动化脚本默认不要用。另有 `history:*` / `sync:*` 系列可读取并恢复文件历史版本（依赖 Obsidian File Recovery / Sync）。

## 4. AI 创建笔记的标准回路（推荐固化）

```
① 防重      obsidian search vault=V query="<标题关键词>"      # 确认无同主题文章
② 创建      obsidian create vault=V path="folder/note.md" content=<全文，\n 转义> [overwrite]
③ 读回      obsidian read vault=V path="folder/note.md"      # 核对 frontmatter 与结构
④ 链接校验   obsidian links vault=V path="folder/note.md"     # 出链是否解析到真实文件
⑤ 全库坏链   obsidian unresolved vault=V counts               # 创建后必查一次
⑥ 可选      obsidian open vault=V path="folder/note.md"      # 在界面中打开给用户看
```

## 5. 实测踩坑（重要）

1. **长文 `content=` 必须转义换行**：真实换行直接传参会把命令截断；须把真实换行替换为字面量 `\n`（`\t` 同理），由 CLI 还原。
2. **shell 里手工拼长内容必翻车**：中文、撇号（如 `Africa's`）、双引号混在一起时引号转义几乎必错。**用 Python `subprocess` 列表参数**（见 §6），让参数传递机制处理转义。
3. **Windows 命令行长度上限约 32K 字符**：`content=` 加转义后约等于文件大小；超过 ~20K 字符的长文改为 `create` 写骨架 + `append` 分段写入。
4. **stderr 的 libpng warning 是无害噪音**：本机每次调用都输出 `libpng warning: iCCP...`，判断成败只看 **returncode + stdout**。
5. **多 vault 漏 `vault=` 会写错库**：写入前先 `obsidian vaults verbose` 确认目标库名。
6. **content 中本来就有字面量 `\n` 文本时会被还原成换行**（markdown 正文一般不会出现）；含"反斜杠 + n/t"的内容先确认再写入。
7. `delete` 默认进系统回收站（可找回），加 `permanent` 才是真删。
8. **`reload` 会重写 `graph.json` 的视图状态，可能清空 `colorGroups`（图谱配色）**：`obsidian reload vault=<名>` 会重新序列化并写回 `.obsidian/graph.json`，若图谱视图未把配色加载进内存，`colorGroups` 会被写成空数组、`scale` 被重置。**不是配色配置丢了，而是视图状态文件被覆盖成默认**。恢复：`git checkout -- .obsidian/graph.json`，或一键 `python tools/graph-style/configure.py` 重新写入统一配色。`doctor.py` 已内置“图谱配色”检查，丢了会提示。

## 6. Python 调用模板（可直接复制）

```python
import subprocess

def obsidian(*args: str, timeout: int = 60) -> str:
    """调用 Obsidian CLI，返回 stdout。stderr 中的 libpng 噪音一律忽略。"""
    r = subprocess.run(["obsidian", *args], capture_output=True,
                       text=True, encoding="utf-8", errors="replace", timeout=timeout)
    if r.returncode != 0:
        raise RuntimeError(f"obsidian {' '.join(args)} 失败:\n{r.stderr}")
    return r.stdout

def to_cli_content(text: str) -> str:
    """真实文本 → CLI content= 值（换行/制表符 → 字面量 \\n / \\t）。"""
    return text.replace("\r\n", "\n").replace("\t", "\\t").replace("\n", "\\n")

def create_note(vault: str, rel_path: str, content: str, overwrite: bool = True) -> str:
    args = ["create", f"vault={vault}", f"path={rel_path}", f"content={to_cli_content(content)}"]
    if overwrite:
        args.append("overwrite")
    return obsidian(*args)

def read_note(vault: str, rel_path: str) -> str:
    return obsidian("read", f"vault={vault}", f"path={rel_path}")

def check_links(vault: str, rel_path: str) -> str:
    return obsidian("links", f"vault={vault}", f"path={rel_path}")
```

## 7. 移植到其他项目

- 本文**不依赖任何具体项目**：`vault=<名称>`、`path=` 由调用方给定，示例中的路径仅作演示；
- 其他依赖 Obsidian 的项目可将本文原样复制到自己的 `tools/`（或等价目录），只改项目内的指针引用；
- 命令全集以 `obsidian help` 为准（CLI 随 Obsidian 版本演进），本文记录的是 1.13.7 的实测子集。

---

**本仓库（ai-study-method / AItutor）内的引用点**：

- 规则指针：`AGENTS.md` §三·流程引用表（Obsidian CLI 用法行）+ §四·工作方式（Obsidian 优先）
- 初始化规范：`rules/core/init-spec.md`（依赖清单 + 初始化自动化策略；CLI 用法细节已收敛到本文）
- 工具索引：`tools/README.md`
