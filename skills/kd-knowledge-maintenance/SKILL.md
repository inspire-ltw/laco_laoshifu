---
name: kd-knowledge-maintenance
description: 在用户要求更新 KD 本地知识库时导入资料、核对冲突，维护概念多简称、数据集代号、出处与索引；适用于 source 知识和 skills 路由维护，不因普通查询自动改写知识库。
---

# KD 知识库维护

按真实路径向上定位 KD 项目根，先读 [知识库入口](../../source/README.md)、`source/catalog.json` 与 [缺口与冲突](../../source/knowledge/gaps-and-conflicts.md)，确认更新主题、来源与覆盖范围。临时假设不自动升级为共享知识；现场字典、状态表、配方与验收要求须附来源、版本、生效范围与确认状态。一词多义按 [名称消歧流程](../../source/workflows/name-disambiguation.md) 保留局部 `scope`，不因单次判断推广全库。

## 分层更新

- **原文快照（`source/references/kd/`）**：不悄悄改写原文；仅用户要求刷新时运行 `python source/tools/kb.py snapshot --source "原始目录"`（变更审阅后加 `--update`），默认保留历史快照。
- **知识与工作流**：领域解释写 `source/knowledge/`，执行规范写 `source/workflows/`，缺口与矛盾记入 `gaps-and-conflicts.md`，避免多处复制同一数值表。
- **术语主表（`source/glossary.json`）**：同源维护概念与 `short_names`（字段：`name`、`kind`、`status`、`scope`、`sources`），保留 `aliases` 兼容；数据集证据放 `source/evidence/`；推断候选不设 `auto_expand=true`。英文缩写维护全称、`full_name_status`、`category`、`usage`、`notes`、`sources`。[名称对照表](../../source/knowledge/name-crosswalk.md) 为派生文件，禁止手改。
- **Skills 维护**：仅在入口、触发边界或工作流变化时调整，保持真实路径定位，不改动用户其他 Agent 设置。

## 验证与交付

在项目根按序执行（先 `crosswalk`，再 `index` 与 `verify`）：

```powershell
python source/tools/kb.py crosswalk
python source/tools/kb.py index
python source/tools/kb.py verify
python source/tools/kb.py crosswalk --check
python source/tools/kb.py index --check
python source/tools/kb.py search "本次新增术语" --limit 5
python source/tools/kb.py abbr "本次新增简称" --json
```

交付时列明更新主题、来源、未决冲突与验证结果，不把导入日期当作原文发布日期。
