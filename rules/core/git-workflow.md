# Git 管理规则（git-workflow）

> 定义项目的 git 使用规范。核心规则 · 学科无关。
> 与 `decision-trees.md` 的话题生命周期（TOPIC OPEN/CLOSE）配合。

## 一、提交时机

| 时机 | 说明 |
|------|------|
| **checkpoint 创建（OPEN）** | 实质新话题出现（判定见 `decision-trees.md` §1）→ 建 `_checkpoints/{文章名}.md` + commit `[TOPIC <文章名>][OPEN]` |
| **文章创建/修改/升级** | 写文章、升级正式资产后提交 |
| **链接/拆分/合并/归档/删除** | 任何结构变化后提交（文章名写进提交信息） |
| **规则/规范变更** | 修改 skill/规则/架构后提交 |

## 二、提交信息规范

```
[TOPIC <文章名>][OPEN]   建立 checkpoint 草稿
[TOPIC <文章名>][CLOSE]  升级为正式文章 / 归档 / 删除
[rule] / [build] / [docs] / [fix]   规则、构建、文档、修复
```

- **git event 不区分**：只保留 OPEN / CLOSE 两个生命周期标记，不做 STEP/FIX/REVIEW 细分
- **按文章名闭合**，不按主题
- commit 只记生命周期与修改范围，不复制文章完整内容

示例：
```
[TOPIC 概念-随机事件][OPEN] 建立草稿
[TOPIC 概念-随机事件][CLOSE] 升级为正式文章
[node] 新增：概念-大数定律
```

## 三、提交内容

### 必须提交
- `_checkpoints/`（草稿/快照，防丢失）
- 文章（正式 + 临时）
- 规则/规范/模板
- 工具脚本

### 不提交（gitignore）
- 学生个人笔记（`personal/` 可选）
- 学习画像数据（`profiles/` 可选）
- 临时文件（`_temp/`、`_scratch/`）
- Obsidian 本地配置（`.obsidian/`）

## 四、分支策略

- **默认单分支**（`main`/`master`）——个人学习项目
- 试点/多人协作时：`seed`（共享地基）与 `personal`（个人）分离
- 已有 seed 分发 → 学生 fork/复制 → 在 personal 上生长

## 五、检索与恢复

- 查某次话题：`git log --grep "[TOPIC"`
- 查某篇文章历史：`git log -- <文件>`
- 恢复中断：`git log --grep "[TOPIC"` 找未闭合话题（按文章名）→ 询问用户继续

## 六、隐私

- 学生个人笔记/画像**可选提交**（呼应本地运行 + 数据采集架构）
- 默认不提交 `personal/`，学生自主决定是否共享
